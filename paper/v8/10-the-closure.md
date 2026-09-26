# Step 10 — Analytical closure of the sizing loop

**v8 taslağı, birinci yazım.** İskeletin 10. adımı. **İlk sayısal adım** — 1'den 9'a
kadar hiçbir sayfa bu uçağa ait bir kapanış vermedi.

**Kural denetimi:** başlık *"and where it fails"* içermiyor (ChatGPT, Tur 34 — o ifade
batarya açığını bu bölüme çeker; açıklar 14'te yaşar) · *"analytical"* fiziksel kapanışı
zaten reddediyor · **3,8× burada GEÇMİYOR** (Grok'un şartı: *"bir sayı, iki rol, tek
paragraf"* — 3,8× yalnız Adım 14'ün) · Qwen'in şartı: *elverişli sonuç, sonra kırılma*
yapısı **bölünmeden, tek yerde** duruyor · menzil iddiası yalnız çok rotorluya karşı.

**Girdi yuvası Tur 51'de denetlendi.** ChatGPT ve Grok bir çift sayım yakaladı; kod
doğruladı. `aero/closure_inputs.py` yuvayı kuruluş sınamasıyla sabitliyor, `aero/closure.py`
dört kapanışı çalıştırıyor.

---

## Analytical closure of the sizing loop

This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. **Closing a sizing loop mathematically is not the same thing as closing an aircraft physically.** This section does the first: what it produces is a set of consistent numbers on a declared set of assumptions.

Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10). **If no fixed point exists, the declared sizing package does not close.**

### The inputs, and why there are four closures rather than one

**The zero-lift drag coefficient is uncertainty:** a consistent build-up places it between 0.0285 and 0.0381 (Section 11), and a designer does not choose where the real aircraft falls in that range. **The blade family is a design variable this study has not fixed:** four nose-blade families that meet the hover figure of merit span cruise propeller efficiencies of 0.632 to 0.683, and the study carries all four rather than pretending to have chosen. **The published zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of the bracket, outside the supported range.

The loop holds wing loading, disc loading and aspect ratio fixed, so **the cruise lift coefficient is unchanged at 0.450 in every closure** (geometry in Supplement S10); the claim is that C_L is unchanged, not that C_D0 is exactly so. The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 8, and **the control moment arms of Section 8 are therefore reference values that this closure does not re-derive.** **These are the same configuration at four closed masses rather than four configurations** — but anything that depends on the arms is carried at the reference geometry and is not an output of the loop.

Run on the published drag coefficient without the rotor term and the published propeller efficiency, the same construction reproduces the published aircraft within 1.5 percent (Supplement S10). That check is the only place in this section where the published value appears, so the closures report a change of inputs, not of method.

### The four closures

**On these assumptions all four converge**, for the 50 kg design — the only one carried through this loop.

| | C_D0 | η_p | L/D | L/De | MTOW | Empty fraction | Hover power, rotor shaft | Engine rating, shaft | Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 0.0381 | 0.632 | 8.79 | 5.56 | 57.5 kg | 0.614 | 12.53 kW | 5.17 kW | 927 km |
| **B** | 0.0381 | 0.683 | 8.79 | 6.00 | 55.8 kg | 0.607 | 12.17 kW | 4.65 kW | 1 002 km |
| **C** | 0.0285 | 0.632 | 10.82 | 6.84 | 53.5 kg | 0.597 | 11.66 kW | 3.91 kW | 1 141 km |
| **D** | 0.0285 | 0.683 | 10.82 | 7.39 | 52.3 kg | 0.592 | 11.40 kW | 3.54 kW | 1 233 km |

*L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed within each closure, so the closure changes
neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four
simulated aircraft.*

**Payload is an input, fixed at 13 kg; take-off mass is the output**, and the payload fraction runs from 0.25 down to 0.23. **The blade that is best before the loop is still best after it.** There was no reason to assume so: propeller efficiency propagates through cruise power into engine size, engine size into mass, and mass back into hover power, and a loop can reverse a local ranking. At both ends of the drag bracket the higher-efficiency family closes to the longer range — **a result of the closure rather than an assumption carried into it.**

### The transition

The sizing above says nothing about whether the aircraft can change regime. **The question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss.** Every transition figure here belongs to a reference design at its published mass and is not an output of the closure. In the first, a point-mass model with the body angle driven kinematically, a rotation entered in a 5 m s⁻¹ climb loses no altitude at either reference rotation time: 2 s for the 50 kg design and 5.1 s for the 1 000 kg one. Solved instead with rotational dynamics and a finite control moment, **and with the aerodynamic pitching moment set to exactly zero, so that nothing favourable is borrowed**, the 50 kg design **loses 5.4 m at the same reference condition.** The loss is not an artefact of the controller: it is unchanged across three reference profiles, appears without the control moment saturating, and grows as the gains are raised (Supplement S10). **What the kinematic model leaves out is not the difficulty of turning the aircraft but the trajectory the aircraft flies while it is being turned.** **So the zero-altitude-loss result is a property of the model that produced it.**

What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above roughly ten degrees of incidence, the band the rotation passes through (Section 14). With a borrowed moment the spread is wide enough that no number from it is reportable: some models complete the rotation, some saturate the tip pairs, and some tumble. **That spread is itself the finding.** **Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude.** Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here.

### What closing does and does not establish

It establishes that the architecture is arithmetically self-consistent on a declared package, at four corners of that package. **It does not establish that the package exists.** The energy store this closure assumes is the item Section 14 examines, and the examination does not end well. These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against one (Section 6 compares cruise efficiency), and the comparison with the other hybrids depends on the sizing contract (Section 13).

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 104 — Adım 10 yeniden kuruldu** (Tur 101–103; dört okuyucu + Claude, her ayrışık satır oylandı; R cümlelerine veto yok): `drafts/10-recomposed.md` uygulandı. Kaynak 83 geri (D29b, korunur); kaynak 20–23 eke, 67 J24'e; **R16 + P17 eke — kural (iii), yazar kararı (E7, Tur 104)**; J32 + P33 gövdede (DeepSeek; sonra dördü). Özgün gövde Ek S10'da tam | `drafts/10-recomposed.md` §3 iz |
| **Tur 103 (Tur 102: ChatGPT ve DeepSeek inceltmesi; Grok ve Qwen aynı okumayı yazdı — teyide):** dipnot "the loop holds both factors fixed within each closure" — L/D köşeden köşeye değişir (sürükleme braketi), döngü onu yeniden yazmaz | Tur 102 cevapları |
| **Tur 102 (Tur 101 oybirliği; T4):** tabloya L/De sütunu (5,56 / 6,00 / 6,84 / 7,39 = L/D × η_p) ve dipnot: "L/De = L/D × η_p at the cruise condition; the loop holds both factors fixed
within each closure, so the closure changes neither. The four L/De values are the bounding corners of that product, carried into the closures as inputs, not four simulated aircraft." (G, C, D, K önerileri birleşti — teyide). Adım 6'nın köşe tablosu Adım 6 yeniden kurulurken taşınır. Özgün tablo Ek S10'da | Adım 6 köşe tablosu; `drafts/objects.md` T4 |
| **Tur 98 (dört okuyucu + Claude; E5):** "the rotorcraft comparison"; "No multirotor or helicopter is sized in this work, so no range comparison is made against either". Özgün Ek S10'da | Adım 6 |
| **Tur 88 (dört okuyucu + Claude):** "cannot charge for the trajectory" → "cannot account for" — fatura sözcüğü genel fiil (A′; Qwen P2 taraması) | Tur 87 metni §2 |
| **Tur 73:** birinci geçişten 10.2 (alan sabit tutulsaydı karşı-olgusu) ve 10.4 (nokta kütle modelinde optimize edilecek süre yok paragrafı) uygulandı — dört okuyucu + Claude. **10.1, 10.3, 10.5 vetolandı** (ChatGPT; 10.3'e Grok da) → kaynak kaldı. Hüküm cümlesi korunan listeye | Tur 72 metni §4 |
| **Tur 61:** yayılım tablosu tek cümleye indi (dört okuyucu + Claude hemfikir, A6); dört sayı aynen | `aero/closure-result.txt` YAYILIMLAR |
| **Tur 60:** üç ölçeklenmeyen şey (uç disk çapı eklendi); çerçeve+rotor katsayıları S_ref 1,979 m² üzerinde — sabit tutmak donanımı kanatla büyütmek demek; referans boyutta kalsa %4–13, 0,0009–0,0028 küçülürdü, kapanış almıyor; terim birliği | Grok; `aero/closure.py`, `closure-result.txt`; `aero/tip_propeller.py` S_REF; `verify.py` iki yeni kontrol |
| **Tur 59:** kapanış geometrisi 2,07–2,27 m², 3,53–3,70 m, 1,23–1,29 m — eski alt uçlar (1,98 / 3,45 / 1,20) **50 kg referans geometrisiydi**, kapanış değil | `aero/closure.py` GEOMETRI bloğu, `closure-result.txt`; `verify.py` Adım 10 geometri denetimi (eski alt ucu reddeder) |
| **Tur 58, P3:** bu bölüm düzeni fiyatlıyor; mekanizma sayımı yalnız envantere dayanıyor | Adım 9 bağımlılık tablosu; Adım 15 (*"It rests on the inventory of Sections 7 and 8"*) |
| MTOW = m_faydalı/(1 − f_boş − f_enerji); f_boş kurulu güce, güç MTOW^1.5'e bağlı | §2.12; `aero/baseline.py:boyutlandir`, satır 104–124 |
| Tutarlı braket 0,0285–0,0381, rotor terimi iki uçta da 0,0154 | `aero/drag_sweep.py` satır 41–48 ve docstring |
| Yayımlanan 0,0248 **iki ucun da altında** | aynı betik, *"IKI UCUN DA ALTINDA"* çıktı satırı |
| η_p = 0,632–0,683, dört palet ailesi | `aero/nose-propeller-crossing.txt` |
| η_p döngüye **iki kez** giriyor; ikisi birlikte ölçekleniyor | `baseline.py:111` (`eta_seyir`) ve `:126` (`eta_zincir`); `chain_resolve.gorev_ile` |
| L/D yuvasına aerodinamik oran girer, L/De değil | `aero/closure_inputs.py`, kuruluş sınamasıyla |
| **Kuruluş sınaması:** 49,4 kg / 11,88 / 1.585 km vs yayımlanan 50,1 / 11,88 / 1.583 | `aero/closure.py`, sapma %1,5 · %0,0 · %0,1 |
| **Dört kapanış tablosu** | `aero/closure-result.txt` |
| Yayılımlar: MTOW %9,9 · askı %9,9 · menzil %33,0 · motor %46,1 | aynı çıktı |
| Sürükleme braketi: MTOW %6,9, menzil %23,1; palet ailesi: %2,9 ve %8,1 | aynı çıktı |
| En iyi palet kapanıştan **sonra da** en iyi, iki sürükleme ucunda da | aynı çıktı |
| Faydalı yük 13 kg; pay 0,23–0,25 | `baseline.py` GOREV `m_faydali`; `closure-result.txt` |
| Nokta kütle, iki serbestlik, kinematik gövde açısı; yavaş dönüş **daha az** kaybettiriyor | **§3.15** *Transition time: slower is better*, satır 2198–2212 |
| 5 m/s tırmanışla irtifa kaybı **sıfır**; referans süreler **2 s hafif, 5,1 s ağır**; T/W 1,066'dan 1,00'e | §3.15, satır 2217–2221 |
| Moment 1/t_r², güç 1/t_r³; optimum yok | §3.15, satır 2208–2214 |
| Dönme dinamiği + sonlu moment + **sıfır** aerodinamik moment → **5,4 m** | §3.15, satır 2224–2228; ve **§4.7** satır 2823–2827 |
| Kayıp kontrolcü artefaktı değil; üç profilde de aynı, doymadan, kazanç artınca **büyüyor**, 17 m'ye çıkıyor | §3.15, satır 2229–2234 |
| Ödünç momentle sonuç dağılıyor: kimi tamamlıyor, kimi doyuyor, kimi takla atıyor | §3.15, satır 2236–2240 |
| *"No current method"* ifadesi **kullanılmadı** — Adım 6'da daraltılan ifadenin geniş hâli; kendi denetimimde yakalandı | §3.1 propagasyon kuralı; Adım 6 *"for the methods used here"* |

**Bu sayfada BİLEREK olmayanlar:**

- **3,8× ve batarya açığı.** Grok'un şartı: bir sayı, iki rol, tek paragraf. Kapanış adımı
  ilan edilmiş paketin kapandığını söyler; **o paketin var olmadığını Adım 14 söyler.**
- **Öteki hibritlere karşı hiçbir sıralama.** Adım 13'ün işi.
- **Sabit kanatlıya karşı hiçbir şey.**
- **Defter kalemleri** — sürükleme dökümü, kütle dökümü, serbest dönen rotorların bedeli:
  Adım 11.
