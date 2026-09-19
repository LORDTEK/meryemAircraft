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

If the accounting of Section 2 is right, then for a common mission:

> **A configuration that carries a dedicated lift system should pay for it in gross weight, and
> that payment should not be recovered by whatever cruise efficiency the arrangement buys.**

This is sharper than it first appears, because **it forbids the obvious defence.** The natural
reply to Bill 1 is that a dedicated lift system is worth its mass, since it frees the airframe
to be a good cruise aircraft. The prediction concedes that reply and then denies its
sufficiency: it says the efficiency gain is **real** and still **insufficient**. An accounting
that merely said "carrying hardware costs mass" would be unfalsifiable. This one can fail — and
it fails if a set of architectures sized on a common mission shows the efficiency credit
covering the weight charge.

### The data

The check uses a NASA study that sizes four VTOL architectures against a single mission with
common tools and common assumptions — a study conducted for its own purposes, with no
relationship to the present work, and which does not use the accounting of Section 2 or any
other. The mission is 1 200 lb of payload over 75 nautical miles. The relevant quantities are
the effective lift-to-drag ratio in cruise and the design gross weight.

| Configuration | Effective L/D | Design gross weight | Dedicated lift hardware |
|---|---:|---:|---|
| Turboshaft quadrotor | 4.9 | 3 678 lb | none — no cruise wing to carry it for |
| Turbo-electric lift-plus-cruise | 8.5 | 7 271 lb | yes |
| Tilt-wing | 8.6 | — | none — the same hardware serves both regimes |

### The result

**The lift-plus-cruise configuration's cruise efficiency is about seventy percent better than
the quadrotor's, and it is nearly twice as heavy.** That is the prediction, and it is worth
being explicit about why it is not a counter-example to it: the efficiency credit is exactly
what the accounting says a dedicated lift system buys, and the weight charge is exactly what it
says the buyer pays. The charge survives the credit.

**The framework does not predict these numbers.** It predicts an ordering, and the ordering
holds on a data set it had no part in producing.

### The row that does not flatter this paper

The fourth column above contains a row worth stating plainly rather than leaving in a table.
**The tilt-wing reaches an effective lift-to-drag ratio of 8.6 — higher than every
lift-plus-cruise entry in the set — while carrying no dedicated lift system at all.** It is the
one configuration in that study which uses the same hardware in both regimes, and on this
measure it does best.

That is consistent with the accounting, and it is not consistent with any suggestion that the
architecture proposed later in this paper is the only way to avoid the first charge. **The
tilting family avoids it too, and this independent set says so.** What separates the two is not
this axis; it is what each pays to achieve the avoidance, and that question is not settled by a
sizing study.

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

**Tur 34'ün iki kararı bu sayfada uygulanıyor.** Adım erken ve kendi başına duruyor (Grok,
konumunu değiştirerek). Ve **"validation" kelimesi hiçbir biçimde geçmiyor** (ChatGPT): sayfa
çerçevenin tamamını değil, **tek bir çürütülebilir öngörüyü** sınadığını söylüyor.

**Bu sayfada BİLEREK olan bir şey:** tilt-wing satırı. Set, tilt ailesinin de birinci faturadan
kaçtığını söylüyor ve bu, bu makalenin mimarisinin tek yol olduğu izlenimini **çürütüyor.**
Satır tabloda bırakılmadı, kendi başlığıyla anlatıldı.

**Bu sayfada BİLEREK olmayanlar:** bu uçak, bu uçağa ait hiçbir sayı, ve sınamanın bu uçak
hakkında bir şey gösterdiği iddiası.
