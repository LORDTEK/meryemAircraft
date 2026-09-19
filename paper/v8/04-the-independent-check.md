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

The check uses a NASA study that sizes several VTOL architecture families against a single
mission with common tools and common assumptions. It was conducted for its own purposes, has no
relationship to the present work, and does not use the three-bill accounting of Section 2 or any
framework derived from it. It is used here for three reasons, stated so that the choice is not
merely the one that agreed: it holds the mission fixed across architecture families, it applies
one set of tools to all of them, and it reports both quantities this prediction needs. The
mission is 1 200 lb of payload over 75 nautical miles.

| Configuration | Effective L/D | Design gross weight | Dedicated lift hardware |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none — the rotors serve both regimes |
| Turbo-electric lift-plus-cruise | 8.5 | 7 271 lb | yes |
| Tilt-wing | 8.6 | *(not reproduced here — see below)* | none — no dedicated lift group |

### The result

**The lift-plus-cruise configuration's cruise efficiency is about three-quarters better than the
quadrotor's — a factor of 1.74 — and it is nearly twice as heavy, a factor of 1.98.** That is the prediction, and it is worth
being explicit about why it is not a counter-example to it: the efficiency credit is exactly
what the accounting says a dedicated lift system buys, and the weight charge is exactly what it
says the buyer pays. The charge survives the credit.

**The framework does not predict these numbers**; without the input fractions it predicts no
magnitudes at all. What it predicts is that the amplified weight charge survives the efficiency
credit, and on this pair it does.

**That pair is not a clean isolation of the charge, and the limitation is ours to state.** The
quadrotor and the lift-plus-cruise entry differ in three ways at once: one carries a dedicated
lift group and the other does not, but they also differ in powertrain, and one has a cruise wing
while the other has none. The comparison therefore supports a weaker proposition than the
prediction as stated — that adding a wing and a lift group together still costs mass — and
Section 2 had already called that much obvious.

**The comparison that would isolate the charge is the tilt-wing against the lift-plus-cruise
entry**: both winged, both turbo-electric, one carrying a dedicated lift group and one not. That
is the test this prediction deserves, and it requires the tilt-wing's design gross weight, which
is why the table above leaves that cell empty rather than filling it. **The figure is not
reproduced here because it has not been read from the source by the present authors.** Three
independent readers of a draft of this section supplied three different values for it, and a
fourth was returned by a literature search; that is reason enough to obtain the table rather
than to quote a number. The cell is left open deliberately, and the isolation test is owed.

### The tilt-wing is the instructive case

The tilt-wing entry reaches an effective lift-to-drag ratio of 8.6, at least matching the best
lift-plus-cruise entry in the set, while carrying **no dedicated lift group at all.** The margin
over 8.5 is one tenth and nothing is claimed from its direction; what matters is that it is not
lower.

Two things follow, and the second is the more useful.

**First, the architecture proposed later in this paper is not the only way to avoid the first
charge.** The tilting family avoids it too, and an independent set says so.

**Second, and this is what the row is actually for: the tilt-wing is the transfer property of
Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the
mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the
actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to
that family. The row therefore does two jobs: it denies this paper a uniqueness it has not
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

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
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
