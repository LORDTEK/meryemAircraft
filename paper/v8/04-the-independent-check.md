# Step 4 — An independent quantitative check

**v8 taslağı, birinci yazım.** İskeletin 4. adımı. Tur 34'te karara bağlandı: **erken**, ve
**kendi adımı olarak.** Grok'un konumunu değiştirirken verdiği gerekçe belirleyiciydi:
*"Kendine hizmet ettiği kuşkusu başlıkta başlar, defterde değil."*

**Kural denetimi:** *"validation"* kelimesi **geçmiyor** (ChatGPT, Tur 34) · sınanan şey
**aletin tek bir öngörüsü**, çerçevenin tamamı değil · veri **bu çalışmanın üretmediği** veri ·
öngörü veriden **önce** konuyor.

---

## An independent quantitative check

An accounting proposed by the same people who then use it to argue for a configuration invites
one obvious objection: that the charges were chosen because a particular aircraft happens not to
pay them. The objection arises at the title, not at the ledger, so it is answered here — before
any configuration is described — and it is answered in the only way that settles anything, by
testing a prediction the accounting makes against numbers this work did not produce.

**What follows is not a test of the whole framework.** It checks one falsifiable consequence on
one independent data set. That is a narrow thing, and it is stated narrowly.

### The prediction, stated before the data

**The prediction has two halves, and only the first is a derivation.** Saying so is what makes
the check worth running.

> **First half, derived from Section 2.** A configuration carrying a dedicated lift system pays
> for it in gross weight, and the payment is amplified: additional empty mass enters through a
> multiplier that grows as the empty-mass fraction rises, and the same increment is charged
> again in hover.
>
> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover
> that payment. Section 2 predicts the charge and the amplification; **it does not prove that
> the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower
> the energy fraction at the same time, and which wins is a closure result rather than a
> consequence of the accounting.

The check tests the second half on independent data, with the first half supplying the reason to
expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit
enters linearly through the cruise lift-to-drag ratio.

That distinction decides what a failure would mean. **If some data set showed the credit covering
the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be
refuted is the expectation that the amplified charge outweighs the linear credit, and that is
worth testing precisely because it could go either way.

**The prediction is also mission-dependent**, and the page would be weaker for hiding it. The
mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with
distance. A long enough mission is where the credit is most likely to cover the charge, and the
mission used below is short. **The counter-set is therefore a common-mission sizing study at
longer range in which a dedicated-lift configuration is both more efficient and no heavier than
one without.** None is known to the authors, and the invitation is meant literally.

### The data

The check uses a NASA study that sizes **five VTOL architecture families**, most in two
propulsion variants — nine designs in all — against a single mission with common tools and
common assumptions. It was conducted for its own purposes, has no
relationship to the present work, and does not use the three-bill accounting of Section 2 or any
framework derived from it. It is used here for three reasons, stated so that the choice is not
merely the one that agreed: it holds the mission fixed across architecture families, it applies
one set of tools to all of them, and it reports both quantities this prediction needs. The
mission is 1 200 lb of payload over 75 nautical miles.

Three of the nine designs matter here. The turboshaft quadrotor reaches an effective lift-to-drag ratio of
4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes.
**The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group —
eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none:
eight proprotors, reoriented.**

### The result

**The primary comparison is the last two designs**, because they isolate the charge. The
lift-plus-cruise and tilt-wing entries share the mission, the payload, the turbo-electric
propulsion architecture and the presence of a cruising wing. **They are not identical in every
other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the
other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is
that one carries a dedicated lift group through cruise and the other does not.** The comparison is
the closest the published set comes to isolating that charge; it is not a controlled experiment.

**The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated
lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the
design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net
difference between two architectures, not the measured mass of a lift group**, and the
published weight breakdown is what makes it informative rather than merely large.

**The published weight breakdown shows the transfer property of Section 2 — the mechanism giving part
of the structural saving back — inside a breakdown this work did not produce**, although the categories
it reports do not account for the whole difference (Supplement S4).

**And the source states the second half of the prediction in its own words.** Discussing why the
all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high
cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the
quadrotor, *"but not enough to counter the increase in structure and propulsion weight."* That
is the efficiency credit conceded and found insufficient, by the authors of the data rather than
by the authors of the prediction.

**The quadrotor is reported for scale, not as the test**: against it the lift-plus-cruise design
changes three things at once, and the contrast is in Supplement S4.

**The framework does not predict any of these numbers**; without the input fractions it predicts
no magnitudes. What it predicts is that the amplified weight charge survives the efficiency
credit, and on the isolated pair it does so with the credit reduced to nothing.

### The tilt-wing is the instructive case

The tilt-wing is the entry that carries the isolation test above, and it is also the entry that
denies this paper a claim it might otherwise be read as making.

**The architecture proposed later in this paper is not the only way to avoid the first charge.**
The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the
two matched designs, and an independent set says so. The margin in cruise efficiency is one
tenth and nothing is claimed from its direction; what matters is that the dedicated lift group
does not buy an efficiency advantage to set against its mass.

**Second, and this is what the entry is actually for: the tilt-wing is the transfer property of
Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the
mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the
actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to
that family. The entry therefore does two jobs: it denies this paper a uniqueness it has not
earned, and it confirms the property the accounting is built on. What separates the tilting
family from the configuration described later is not this axis; it is what each pays, and a
sizing study does not settle that.

### What this check does and does not establish

It establishes that one prediction of the accounting holds on data produced elsewhere, for
purposes unrelated to this argument. That is the whole of it.

**It does not establish that the accounting is complete**, that the three charges are the only
costs an architecture pays, or that avoiding them makes an aircraft better. The accounting says
an architecture that avoids the three is cheaper in those three currencies and nothing more; a
configuration may avoid all three and still be unbuildable, uncontrollable, or unsuited to its
mission. Sections 10 and 14 are about exactly that possibility for the configuration proposed
here.

**It does not establish anything about the configuration this paper proposes**, which has not
yet been described, and which is not in the study used here. A reader who wants to know whether
the accounting flatters that configuration will have to wait for Section 11, where it is applied
to it and where the answer is not uniformly favourable.

What the check is for is narrower and comes earlier: **an instrument whose first use is to
measure the thing its authors are advocating should be shown working on something else first.**
That is what this section does, and it is the reason it appears here rather than after the
aircraft.

**The instrument is now fixed, and it is not modified again.** Sections 2 and 3 defined what any
architecture in this corner pays and what escaping it would require; this section tested one
falsifiable consequence of that definition on data produced by other people for other aircraft.
**Everything that follows is measured with it rather than added to it.** The next two sections
describe the two capabilities the mission asks for, one at a time and each against the family
that structurally lacks it, before Section 7 asks whether one aircraft can hold both.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 63 — N2 ve N4** (dört okuyucu + Claude hemfikir): tablo düzyazıya (sayılar aynen); ağırlık dökümü paragrafı ve quadrotor karşıtlığı Ek S4'e aynen; gövdede aktarımın sonucu (Qwen'in şartı) ve *"kategoriler farkın tamamını açıklamıyor"* çekincesi kaldı | Johnson & Silva 2022 Tablo 3; `paper/v8/supplement.md` S4 |
| **Tablo 3, Johnson & Silva 2022, s. 70 — birinci elden okundu** | `cfd/1521_Johnson & Silva_122721.pdf` |
| Quadrotor TS 4,9 / 3 678 lb · L+C TE 8,5 / 7 271 lb · **Tiltwing TE 8,6 / 6 584 lb** | Tablo 3, doğrulandı |
| Yapı: L+C 2 670 lb, Tiltwing 1 954 lb · Tahrik: 1 772 / 1 918 lb · Boş: 5 809 / 5 130 lb | Tablo 3 |
| L+C TE tahriki: *"8x126 + 821"* — sekiz kaldırma motoru artı seyir motoru | Tablo 3, Power satırı |
| *"but not enough to counter the increase in structure and propulsion weight"* | s. 70, Tablo 3'ün üstü |
| *"five aircraft types so far"* — dört değil | s. 70 |
| Öngörü: adanmış kaldırma sistemi brüt ağırlıkta ödenir ve verim kredisi bunu kurtarmaz | §3.1, satır 1108–1112 |
| *"Verim kazancı gerçek ve yine de yetersiz"* — bariz savunmayı yasaklıyor | §3.1, satır 1112–1113 |
| Ortak görev: 1 200 lb faydalı yük, 75 deniz mili | §3.1, satır 1115–1116 |
| Turboşaft quadrotor: L/D_e = 4,9, brüt ağırlık 3 678 lb | §3.1, satır 1116–1118 |
| Turbo-elektrik lift+cruise: L/D_e = 8,5, 7 271 lb | §3.1, satır 1118–1119, kaynak [22] |
| *"Seyir verimi yüzde yetmiş daha iyi ve neredeyse iki katı ağır"* | §3.1, satır 1119–1120 |
| Tilt-wing: L/D_e = 8,6, setteki her lift+cruise'dan yüksek, adanmış kaldırma yok | §3.1, satır 1121–1123 |
| Tilt-wing setteki **aynı donanımı iki rejimde de kullanan tek** yapılandırma | §3.1, satır 1123 |
| Çerçeve sayıları öngörmez, ağırlık cezasının verim kredisinden sağ çıkacağını öngörür | §3.1, satır 1123–1125 |
| Çerçeve, üçten kaçınmanın uçağı **daha iyi** yapacağını iddia etmez | §3.1, satır 1126–1128 |
| Üç faturanın tek maliyet olduğu iddia edilmez | §3.1, satır 1130–1132 |

**Aritmetik denetimi:** 8,5 / 4,9 = 1,735 → *"yaklaşık yüzde yetmiş daha iyi"* ✓ ·
7 271 / 3 678 = 1,977 → *"neredeyse iki katı"* ✓.

**Tur 45: sayılar birinci elden doğrulandı ve yalıtma testi yapıldı.**

Yazar beş PDF'i depoya yükledi. `poppler-utils` kuruldu, Tablo 3 okundu. **Çelişkinin nedeni
çıktı: dört okuyucu ÜÇ AYRI BELGE okumuş ve her biri kendi belgesi için birebir doğru
aktarmış.** Grok 2018 AIAA'yı (o tabloda tiltwing sütunu yok ve 8,5 gerçekten elektrikli
L+C'ye ait), ChatGPT ve Qwen 2022 makalesini, DeepSeek 2023 sunumunu. **Kaynak kuralı tam
olarak işe yaradı.**

**Bizim sayılarımız doğru çıktı** — §3.1'in 4,9 / 3 678 lb ve 8,5 / 7 271 lb'ı Tablo 3'te
birebir var. Grok'un *"bir RVLT sürümü"* şüphesi haklıydı ama bizim sürümümüz doğru sürümdü.

**Eksik hücre doldu ve sayfanın merkezi değişti.** Artık birincil karşılaştırma quadrotor
değil, **lift+cruise'a karşı tiltwing**: ikisi de kanatlı, ikisi de turbo-elektrik, aynı görev,
tek değişken adanmış kaldırma grubu. Tiltwing %1,2 daha verimli ve **%9,4 daha hafif.** Grok'un
istediği temiz kontrol buydu; ChatGPT de bunu birincil yapmamızı söyledi.

**Ve NASA öngörünün ikinci yarısını kendi sözleriyle söylüyor.** Ağırlık dökümü de aktarımı
gösteriyor: L+C yapıda +716 lb, tiltwing tahrikte +146 lb geri veriyor.

**ChatGPT haklıydı: "dört VTOL mimarisi" yanlış.** Makale *"five aircraft types so far"* diyor.
Düzeltildi. Kayıt: `paper/nasa-numbers-open.md`.

---

**Tur 43'te düzeltilenler — merkezde bir mantık kusuru vardı.**

**Grok, ChatGPT ve Qwen bağımsız olarak aynı şeyi buldu:** öngörü §2'den **türetilmiyor.**
§2 kütle cezasını ve çarpanla büyümesini veriyor; **verim kredisinin kaybedeceğini
kanıtlamıyor.** Adanmış kaldırma sistemi boş kütle kesrini yükseltirken enerji kesrini
düşürebilir ve hangisinin kazandığı bir kapanma sonucudur. Sayfa artık öngörüyü **iki yarıma
ayırıyor** ve yalnız birincisinin türetme olduğunu söylüyor. ChatGPT bunu *"turun en önemli
kavramsal meselesi"* diye işaretledi.

Bunun bir sonucu var ve yazıldı: **kredi cezayı karşılasaydı Fatura 1 çürümezdi** — kütle yine
ödenmiş olurdu. Çürüyecek olan, çarpanla büyüyen cezanın doğrusal krediyi yendiği beklentisi.

**Qwen ve DeepSeek: öngörü göreve bağlı.** Kütle cezası kabaca sabit, verim kredisi mesafeyle
birikiyor. Yazıldı, ve karşı-setin ne olduğu **somut olarak** adlandırıldı: uzun menzilli ortak
görevli bir boyutlandırma çalışması.

**GROK'UN EN AĞIR BULGUSU — karıştırıcı değişkenler.** Quadrotor ile lift+cruise çifti **üç
şeyi birden** değiştiriyor: adanmış kaldırma, tahrik, ve kanadın varlığı. *"İki kat kütle,
'verim kredisi kaldırma grubunu karşılayamadı' değildir. O karşılaştırma artı o karıştırıcılardır."*
Haklı, ve §3.1 bu haliyle yıllardır duruyordu. Sayfa artık **kendi sınırını kendisi söylüyor**
ve temiz kontrolün ne olduğunu adlandırıyor: **tilt-wing'e karşı lift+cruise** — ikisi de
kanatlı, ikisi de turbo-elektrik.

**Ve o kontrol yapılamadı, çünkü tilt-wing ağırlığı doğrulanamadı.** Üç okuyucu üç ayrı sayı
verdi, arama dördüncüsünü verdi, NASA alan adları bu ortamda kapalı. Hücre **bilerek boş
bırakıldı** ve nedeni sayfada yazılı. Kayıt: `paper/nasa-numbers-open.md`.

**ChatGPT: "dört VTOL mimarisi" yanlış.** Set QSMR, side-by-side, quadrotor, lift+cruise ve
tiltwing ailelerini içeriyor. Doğrulayamadım; ihtiyatla **"several"** oldu.

**Qwen: "yaklaşık yüzde yetmiş" eksik söylüyor** — 8,5/4,9 = 1,735, yani %73,5. *"Yaklaşık
dörtte üç"* ve çarpanlar açıkça yazıldı.

**ChatGPT: başlık gazetecilik.** *"The row that does not flatter this paper"* dergi düzyazısı
değil, hakem beklentisiyle kendini savunan bir yazar gibi okunuyor. *"The tilt-wing is the
instructive case"* oldu.

**Qwen: tilt-wing satırının asıl işi başka.** Satır yalnız "tek yol biz değiliz" demiyor —
**§2'nin aktarım ilkesinin başkasının verisinde görünmesi.** Tilt-wing kütle cezasından
kaçmıyor, onu **taşıyor**: mekanizmaya, gyroskopik bağlaşıma, geçiş kontrolüne. Yazıldı, ve
satır artık savunma değil doğrulama yapıyor.

**DeepSeek: "neden bu çalışma"** söylenmemişti. Üç gerekçe yazıldı. Ve *"or any other"*
daraltıldı, quadrotor satırının *"taşıyacağı seyir kanadı yok"* ifadesi düzeltildi.

**Tur 34'ün iki kararı bu sayfada uygulanıyor.** Adım erken ve kendi başına duruyor (Grok,
konumunu değiştirerek). Ve **"validation" kelimesi hiçbir biçimde geçmiyor** (ChatGPT): sayfa
çerçevenin tamamını değil, **tek bir çürütülebilir öngörüyü** sınadığını söylüyor.

**Bu sayfada BİLEREK olan bir şey:** tilt-wing satırı. Set, tilt ailesinin de birinci faturadan
kaçtığını söylüyor ve bu, bu makalenin mimarisinin tek yol olduğu izlenimini **çürütüyor.**
Satır tabloda bırakılmadı, kendi başlığıyla anlatıldı.

**Bu sayfada BİLEREK olmayanlar:** bu uçak, bu uçağa ait hiçbir sayı, ve sınamanın bu uçak
hakkında bir şey gösterdiği iddiası.
