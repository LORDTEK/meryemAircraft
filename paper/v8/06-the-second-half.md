# Step 6 — The second half: cruise carried on a wing

**v8 taslağı, birinci yazım.** İskeletin 6. adımı. Rakip **çok rotorlu**, ve **yalnız bu
eksende.** Adım 5'in simetriği.

**Kural denetimi:** sabit kanatlıya karşı **hiçbir menzil ya da verim karşılaştırması yok**
(§0, birinci yasak hata) · *"inşa gereği"* geçmiyor · **boyutlandırıldı / gösterilmedi**
ayrımı Adım 5'teki gibi ortada · karşılaştırma **tek bir birimde** yapılıyor.

**Tur 48, dört okuyucudan sonra — beş değişiklik.** (1) η_p aralığının **tarifi yanlıştı**
(ChatGPT): 0,632–0,683 tek paletin iki noktası değil, **dört palet ailesinin** yayılımı.
(2) Braket artık **çarpım matrisi** olarak veriliyor ve iki yayılım türü ayrılıyor:
sürükleme **belirsizlik**, palet ailesi **sabitlenmemiş tasarım seçimi**. (3) İki quadrotor
**eşit** sunuluyor; *"birincil karşılaştırma"* kalktı (ChatGPT, Grok, DeepSeek). (4) `P`'nin
hangi güç olduğu **sayfanın içinde** kanıtlanıyor — Grok elektrik satırı için haklı olarak
sordu; kaynak **batarya kapasitesi** türevinde ayrımı yapıyor, yani soru **bizim lehimize**
kapanıyor. (5) **Dördüncü çekince** eklendi (ChatGPT): analiz zincirleri eşleşmiyor.
**Reddedilen:** DeepSeek'in *"quadrotor'un iki görevli uzlaşması yok"* çekincesi —
kaynak §6.3 quadrotor'un askı ve seyir arasında tam da o uzlaşmayı yaptığını gösteriyor.

**Bu sayfa yazılırken bir hesap yapıldı ve bir iddia daraldı.** Makale çok rotorlu
karşılaştırmasını iki **farklı türden** sayıyla yapıyordu: NASA'nın *etkin* L/De = 4,9'u ile
bizim *aerodinamik* 8,8–10,8'imiz. İkisi aynı birime çevrilince pay **+%80…+%121'den
+%14…+%51'e** iniyor, ve bir köşede işaret dönüyor. Hesap: `aero/effective_ld.py`,
kayıt: `paper/effective-ld-finding.md`. **Sayfa düzeltilmiş sayıyla yazıldı.**

---

## The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the rotorcraft — multirotor and helicopter alike — and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** The claim is
confined to the one thing the rotorcraft family structurally lacks: **a surface that carries the
cruise lift.**

### What the requirement is

Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A rotorcraft meets that requirement completely.**

What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

### What the configuration does instead

**Cruise lift is carried by the airframe itself.** At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

**A rotorcraft's rotors must produce the lift and the propulsive force
together, throughout cruise.** This aircraft separates them: a surface holds the aircraft up and a
propeller pushes it along, and **the wing produces its lift without a separate continuous power
supply of its own** — the power the aircraft spends in cruise goes to overcoming drag, of which
the lift's share is the induced part.

**But the size of the resulting advantage is a calculation, not a consequence of that
statement**. The rest of this section is the calculation,
and it gives a smaller number than the structural statement invites.

### What the margin actually is, in one currency

The sizing set of Section 4 reports an **effective lift-to-drag ratio**, `L/De = WV/P`: a system figure of merit that already
contains the propulsive efficiency of whatever produces the thrust, so **a force ratio cannot be placed beside it.** In level cruise,
with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

**Which power `P` denotes is not assumed here**, because reading it as electrical rather than shaft power would make this
configuration's figure incomparable with the published one. The source writes hover power with the figure of merit applied, which is
shaft power, and applies the propulsion-system efficiency separately, for the all-electric entries as for the shaft-driven ones.

The aerodynamic ratio is **8.79 to 10.82**, with the tip frames and the free-wheeling tip-pair rotors (Section 8) already charged; that
spread is **uncertainty**, the zero-lift drag bracket. The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade
families that meet the hover figure of merit; that spread is **not uncertainty** but a design variable this study has not fixed.

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.79** (adverse drag) | 5.56 | 6.00 |
| **L/D 10.82** (favourable drag) | 6.84 | 7.39 |

**These are the bounding corners of a product, not four simulated aircraft.** Across the examined envelope they give **5.56 to
7.39**; for the best examined blade family, at 0.683, **6.00 to 7.39**. Which blade a designer would choose also turns on structural
loads, acoustics, the motor operating point, rotor inertia and manufacture, **none of which is modelled in this work** (Supplement S6).
Section 10 carries one blade into a closed sizing loop; until then no corner is presented as the aircraft's performance.

### What the comparison gives, against both published quadrotors

The sizing set contains two quadrotors for the same mission, and **neither is treated here as the primary one.**

| | L/De | vs examined envelope 5.56 – 7.39 | vs best examined family 6.00 – 7.39 |
|---|---:|---|---|
| Quadrotor, turboshaft | 4.9 | +13 % … +51 % | **+22 % … +51 %** |
| Quadrotor, all-electric | 5.8 | −4 % … +27 % | **+3 % … +27 %** |

**Against the turboshaft quadrotor the sign holds at every corner of both readings**; closing it would need a propeller efficiency
of 0.557, against 0.632 for the least efficient blade family examined.

**Against the all-electric quadrotor it does not hold at the low corner**, and that result is reported as a result rather than as a
caveat. That vehicle reaches 5.8 with 1 742 lb of battery and nearly twice the gross weight for the same mission, 7 221 lb against
3 678 lb. **That higher gross weight is consistent with the mass charge Section 2 describes**; this table alone does not establish the
causal link, and Section 4 sets out the independent evidence for it.

The same sizing set gives four entries for its two helicopter types, at 5.4 to 7.2, and against them the result is
mixed: this configuration is ahead of the turboshaft single-main-rotor helicopter at every corner,
the two middle entries fall inside its envelope, and only its top corner is ahead of the
all-electric side-by-side helicopter, which has no wing either. The qualifications below apply to them too.

**So the second claim is narrower than the structural statement invites**: carrying cruise lift on a wing is worth roughly an eighth
to a half against the turboshaft reference, and against the all-electric one it ranges from slightly behind to comfortably ahead
depending on the drag outcome and the blade — a measurable advantage, not a change of category. What compresses it is the cruise
efficiency of the fixed-pitch blade: at a propeller efficiency of 0.85 the same airframe reaches 7.47 to 9.20. Whether a
variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and declines to attribute all of it to the hub.

### Five qualifications: three run against this configuration, one has no computed direction, and one bounds what the comparison can be called

**Scale.** The compared vehicles are larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6), and **Reynolds number
favours the larger aircraft**, so the smaller design is at a disadvantage in this comparison rather than an advantage.

**The quadrotor is a good quadrotor**: both quadrotors have unusually low disc loadings. **Nothing here is compared against a poor
example.**

**The speeds are not matched, and the direction of that mismatch is calculable.** The reference is quoted at its best-range speed, this configuration at its cruise condition, 1.49 times stall, rather than at its best point, 1.26. **The reference is therefore given its best speed and this configuration is not given its best speed, and the margin is
positive anyway.** **The best point is not an available option** — cruising there leaves too little margin above the stall — **so this
fixes a direction, not a magnitude.**

**The atmospheres are not matched.** The published sizing mission is flown at *"5,000-ft altitude and ISA + 20°C"*; every number in
this work is at sea level. **The direction of that mismatch is not claimed here**, because it has not been computed.

**The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called.** The published value comes from a fully sized vehicle in an integrated design system; the value here is a converted metric at a prescribed cruise condition, taken before the sizing closure of Section 10. So this is a comparison of two
independently produced figures in a common definition, not a controlled numerical reproduction, and nothing in it should be read as
validation of either, or as a completed aircraft-level comparison.

### What is sized, and what is not demonstrated

**Sized.** The drag build-up and its bracket, the lift-to-drag ratio from the drag polar, the propeller efficiency from
blade-element momentum theory at two operating points, and the range that follows from the chain.

**Not demonstrated.** **No part of this has been measured**: there is no wind-tunnel or flight test in this work, and the drag
coefficient is a build-up with a declared bracket. The planform was chosen rather than optimised. **The span efficiency used
throughout this section is the computed value, 0.817, not the assumed 0.85**, from a vortex-lattice solution of the trimmed planform.
And for the methods used here, and for the published comparisons against which they were checked, **the aerodynamic predictions
diverge above roughly ten degrees of incidence**: three methods of three fidelities depart at the same place, the highest of them
against wind-tunnel measurement. That is a statement about these methods on this class of configuration, not about what any method
could achieve; it does not touch the cruise numbers above, which sit at a few degrees, but it bounds what this section may be read to
support, and the transition of Sections 7 and 10 passes through that band.

### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces nothing and presents the aircraft's
largest surface to ground wind; the tailless planform constrains the sweep; and the fixed-pitch propeller is why the margin above
sits where it does. Section 11 charges the third. The first two are inside Section 10's closed numbers but are not separated out as
charges, and the wing's exposure to ground wind is not priced in this work.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 191 — son okuma onarımı D1** (beşimiz): *"the rotorcraft, multirotor and helicopter alike,"* → *"the rotorcraft — multirotor and helicopter alike —"* (iç açıklama; E5'in helikopter girişi korunur). Eski paragraf S6'da | Tur 189 cevapları |
| **Tur 170 — yazarın notları üzerine kısaltma uygulandı** (Tur 168–169: işlemlerde dört okuyucu + Claude; korunan cümle taşımaları yazar kararı E13). Değişen her paragrafın eski hâli ekin bu adıma ait bölümünde aynen (*"… before the Round 170 shortening"*). Yeni (R) cümleler Tur 170 §2'de okuyucu vetosuna açık; sonuç teyide | `paper/build/v8_round170_texts.py`, `v8_round170_apply.py` |
| **Tur 171 — R9 onarıldı** (Grok vetosu, Tur 170): 4.6 ölçek cümlesinde "of order 50 kg and 1 000 kg" iki isimden birine asılabiliyordu → "larger than both designs studied here, which are of order 50 kg and 1 000 kg (Supplement S6)". Kütleler Tur 170 öncesi 4.6'da da vardı (Qwen); yeni sayı yok. **R8 değişmedi:** beş etken eski 4.4'ün üçüncü cümlesinde birebir duruyordu (Tur 169 eki, S6); Grok'tan vetoyu geri çekmesi istendi. Teyide (Tur 171 §1) | Grok, Qwen |
| **Tur 149 — L-3 satır 4 uygulandı:** *"free-wheeling attitude rotors"* → *"free-wheeling tip-pair rotors"*. W-13 kapandı | Tur 148 §3 |
| **Tur 148 — W-13 uygulandı** (DeepSeek; dört okuyucu + Claude): *"free-wheeling attitude rotors (Section 8, *What this inventory does not settle*)"* → görünümde 6.1. W-4, L-1 kapandı | Tur 147 §3 |
| **Tur 147 — W-4 ve L-1 uygulandı** (bütün okuma; dört okuyucu + Claude): W-4 *"roughly a quarter to a half"* → *"roughly an eighth to a half … (a quarter to a half for the best examined blade family)"*; L-1 (korunan) *"gives its two helicopter types at"* → *"gives four entries for its two helicopter types, at"* — `v8-caveats.md` güncellendi | Tur 146 §5 |
| **Tur 132 — S-56 uygulandı (R; dört okuyucu + Claude):** *"Section 11 charges all three."* → *"Section 11 charges the third. The first two are inside Section 10's closed numbers — the wing's mass in the empty fraction, the constrained planform in the computed span efficiency — but neither is separated out as a charge, and the wing's exposure to ground wind is not priced in this work."* Kanat kütlesi `aero/baseline.py` f_govde 0,30; açıklık verimi 0,817 trimli VLM (Ek S6) | S-56 |
| **Tur 131 — S-55 onarıldı:** *"which Section 10 states explicitly is not its best"* → *"which is not its best"* (silme; dört okuyucu + Claude). **S-56 açık:** *"Section 11 charges all three"* — (b) uygulanmadı, düzeltilmiş R oyda (kanat kütlesi ve planform kapanışın içinde, ayrılmamış; yer rüzgârı fiyatlanmamış) | S-55, S-56 |
| **Tur 123 — uzunluk geçişi, ilk kısım** (dört okuyucu + Claude): **S-48** onarıldı (*"and whether it is ahead of the best examined blade family depends on the drag bracket"* çıktı — tablo +3…+27 %); **M3** L/D_max formülü ve 11,65 / 10,08 Ek S6'ya (kimlikleriyle), yön cümlesi kaldı; **M7** *"and 3.9 percent below the assumption"* Ek S6'ya, *"a vortex-lattice solution"* kaldı. M1 uygulanmadı (Claude'un önerisi P'nin kimliğini taşıyan cümleleri de taşıyordu; düzeltilmiş hâli oyda). Özgün adım Ek S6'da tam. 2 145 → 2 108 | Tur 122 metni §3, §4 |
| **Tur 98 (dört okuyucu + Claude; yazar kararı E5):** eksen yayılımı P-a–P-d — "the alternative is the rotorcraft, multirotor and helicopter alike", "the rotorcraft family", "A rotorcraft meets…", "A rotorcraft's rotors…", korunan ölçek cümlesi "1 660 to 3 275 kg" (SbS TS 3 665 lb = 1 662 kg). Kaynak alıntıları ("multirotors are efficient in hover") ve belirli referanslar (quadrotor) değişmedi. Özgün paragraflar Ek S6'da | J&S Tablo 3 |
| **Tur 97 — yazar kararı (b):** helikopterler de rakip. S-27 6D'ye: "The same sizing set gives its two helicopter types at 5.4 to 7.2, and against them the result is mixed: …" (turboşaft tek rotorluya karşı her köşede önde; ortadaki ikisi zarfın içinde; elektrikli yan yana rotorluya karşı yalnız en üst köşe); nitelemeler bunlara da uygulanıyor. Korunan (166). Eksen yayılımı (6A, 6B, 6C, 6E ölçek, Adım 9, 10, 15) okuyuculara | J&S Tablo 3 PDF s. 70; DGW: 3 951 / 5 980 / 3 665 / 5 547 lb |
| **Tur 97 (dört okuyucu + Claude):** R-5 — 6D zayıf silme "The four corners are not demonstrated aircraft states" onarımıyla uygulandı; S-28 — "Its disc loading is 3.5 lb ft⁻², and the all-electric one's is 3; both are unusually low" ("unusually efficient" çıktı; "good quadrotor" bizim ifademiz, J&S'de yok). **S-27 (R-4) yazar kararı bekliyor** (helikopter ekseni). Özgün paragraflar Ek S6'da | J&S Tablo 3 |
| **Tur 96 (yeniden kurma; dört okuyucu + Claude):** envanter ve yön sütunu teyit edildi. 6A yinelemesi ("A runway-launched aeroplane…"), 6B yinelemesi ("It is not a deficient machine…"), 6G'deki ikinci 7,47–9,20 çıktı; S-26 başlığı onarıldı. **Uygulanmadı:** S-27 (R-4 gönderge), 6D zayıf silme (R-5 "They"), S-28 (ayrışık). Özgün paragraflar Ek S6'da | J&S Tablo 3, PDF s. 70 |
| **Tur 60:** 52,3–57,5 kg | DeepSeek; `aero/closure-result.txt` |
| Çok rotorlu piste ihtiyaç duymuyor; eksik makine değil | §1, satır 160–163 |
| Kanatsız araç her saniyeyi kurulu güçle satın alıyor | §1, satır 161–163 |
| *"Multirotors are efficient in hover and suited to short-range missions…"* | §4.2, satır 2478–2481 |
| Kaldırma bir yüzeyde mi rotorda mı — yapısal, sözleşme değiştirmez | §4.2, satır 2504–2506 |
| **`L/De = WV/P` tanımı** | Johnson & Silva 2022, gösterim listesi s. 94 — **birinci elden** |
| **L/De propulsor verimini İÇERİR** (η_h/FM simetrisinden kanıtlandı) | aynı belge, denklem 2 (s. 645) ve denklem 3 (s. 658); `paper/effective-ld-finding.md` §2 |
| Aerodinamik L/D 8,80–10,82, rotorlar ve uç çerçeveleri **faturalanmış** | §3.6 Tablo 9, satır 1511; *"the tip frames and the free-wheeling rotors charged to this configuration alone"* satır 1500; braket §3.10 / Ek S1 |
| η_p = 0,632–0,683, iki noktalı BEMT | `paper/nose-pair-finding.md`, `paper/chain-resolve-finding.md` |
| **L/De çarpım matrisi: 5,56 · 6,01 · 6,84 · 7,39** | `aero/effective_ld.py`, `aero/effective-ld-result.txt` |
| Sürükleme yayılımı **belirsizlik**, palet ailesi **seçim** | C_D0 braketi §3.10/Ek S1; palet ailesi `aero/nose_propeller_crossing.py` — 2 ve 3 pala × c_l 0,55 ve 0,70, dördü de FM = 0,599 tutturuyor |
| `L/De`'deki P **mil gücüdür**; ayrım kaynağın **batarya kapasitesi** türevinde | Johnson & Silva denklem (1)–(3), s. 640–658: `Ecap = Ecruise + Ehover + Ereserve`, sonra `Ecruise = (Pc/ηc)·t`, ve askıda `Ph = W√(W/2ρA)/FM` ile η_h **dışarıda** — **birinci elden** |
| NASA aracı NDARC (boyutlandırma) + CAMRAD II / CHARM (rotor) ile üretildi | aynı belge §2.1 ve §2.2, satır 189–211 — **birinci elden** |
| Quadrotor turboşaft L/De 4,9; DGW 3.678 lb; disk yüklemesi 3,5 lb/ft² | NASA Tablo 3, s. 70 — **birinci elden** |
| Sayı **Vbr**'de, yani *"best-range speed"* | aynı belge s. 386: *"Cruise is flown at best-range speed (Vbr, 99% high side)"* — **birinci elden** |
| Quadrotor elektrik L/De 5,8; DGW 7.221 lb; batarya 1.742 lb | NASA Tablo 3, s. 70 — **birinci elden** |
| Payın kapanması için gereken η_p = 0,557; hesaplanan en kötü 0,632 | `aero/effective-ld-result.txt` |
| η_p = 0,85 olsaydı L/De 7,47–9,20 | aynı betik, `lde(8.79024, .85)` ve `lde(10.81908, .85)` |
| **L/D hassas değerleri 8,79024 / 10,81908**; Tablo 9 yuvarlanmış 8,80 basıyor. Tur 52'de hassas değerlere geçildi, B köşesi 6,01 → **6,00** | `aero/drag_sweep.py:ld()`; DeepSeek 8,79/8,80 tutarsızlığını yakaladı |
| Karşılaştırılan araçlar 1.670–3.275 kg | NASA Tablo 3, DGW satırı |
| Seyir 1,49 × stall, **en iyi L/D noktası değil**; L/D_max 25,3 m/s'de, stall'ın 1,26 katı | §2.12, satır 971–977 |
| Hiçbir rüzgâr tüneli, hiçbir uçuş denemesi yok | §4.4, satır 2549 |
| Planform süpürme/incelme/kalınlık **seçildi, optimize edilmedi** | §4.5, satır 2656–2658 |
| **Açıklık verimi 0,817 KULLANILIYOR**, 0,85 değil — braketin üç L/D'si de bu değerden | `aero/drag_sweep.py:40` `E_SPAN = 0.817`; kuruluş sınaması yayımlanan temiz gövde 13,44'ü %0,33 içinde yeniden üretiyor |
| 0,817 hesaplanmış değer, varsayımın %3,9 altında | §4.5, satır 2658–2660; kaynağı `paper-v5-supp.md` satır 130–134, trimli −9° washout VLM çözümü |
| On derece üstünde üç yöntem üç aslılıkta sapıyor; en yükseği ölçüme karşı | §3.17, satır 2400–2408; §4.4, satır 2647–2650 |
| Kuyruksuz planform süpürmeyi kısıtlıyor; yunuslama momenti gövdeden | §2.8, satır 741–743 |

**Bu sayfada BİLEREK olmayanlar:**

- **Çok rotorluya karşı hiçbir MENZİL sayısı.** Bu çalışmada boyutlandırılmış bir çok rotorlu
  yok; karşılaştırma yalnız seyir verimi ekseninde ve yalnız yayımlanmış boyutlandırma
  setinin sayılarıyla yapılıyor. Menzil karşılaştırması iddia edilse uydurma olurdu.
- **Sabit kanatlıya karşı hiçbir şey.** §0'ın birinci yasak hatası.
- **"Farklı verim sınıfı" (different efficiency class) ifadesi.** +%14 bir sınıf farkı
  değildir; hesap bunu gösterdi ve ifade kullanılmıyor.
- **Bizim kütle üstünlüğümüz.** Çok rotorluya karşı kütle bu sayfanın ekseni değil; Fatura 1
  Adım 2'de kuruluyor, ölçülüyor Adım 11 ve 12'de.
