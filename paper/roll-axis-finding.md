# Yatış ekseni — İKİ HATA, ikisi de doğrulandı

**Tarih: 2026-09-20. Qwen ve ChatGPT bağımsız olarak iki ayrı hata buldu. İkisi de gerçek.**
İkisi de kendim türetildi ve kaynakta bulundu; hiçbiri olduğu gibi aktarılmadı.

---

## HATA 1 — Askıda "bank" yanlış. Qwen buldu.

### Kinematik, kendim türettim

Gövde eksenleri: **X_b** burundan, **Y_b** sağ kanattan, **Z_b** planforma dik.
İtki X_b boyunca. Konum r = (0, y, z) için M = r × F:

| Kaynak | Moment ekseni | Gövde adı |
|---|---|---|
| Üst/alt çifti (z = ±0,71 m) | Y_b | **yunuslama** |
| Sağ/sol çifti (y = 1,726 m) | Z_b | **sapma** |
| X_b ekseni | — | **sıfır**, her itki X_b'ye paralel |

**Askıda (burun yukarı, +90°):** X_b = **dikey**, Y_b = sağ (yatay), Z_b = ileri (yatay).

| Gövde ekseni | Askıda ne yapar |
|---|---|
| yunuslama (Y_b, yatay) | öne/arkaya eğilme |
| **sapma (Z_b, yatay)** | **sola/sağa eğilme = BANK** |
| **yatış (X_b, DİKEY)** | **yön değişimi = YAW** |

### Kaynakta ne yazıyor

§2.10, satır 866–868:

> *"Hover is the harder case… At zero airspeed only the inboard part of the strip is loaded, by
> the nose propeller's slipstream, and the same circulation model over the slipstream-washed
> area gives 6.0 to 12.0 N·m — **enough for a thirty-degree bank in 1.5 to 2.1 s.**"*

**Şerit X_b etrafında moment üretir. Askıda X_b dikeydir. Ürettiği şey bank değil, YÖN
DEĞİŞİMİDİR.** Sayı doğru olabilir (X_b etrafında 30° dönüş), **kelime yanlış.**

### Ve doğrusu bizim lehimize

Qwen'in asıl bulgusu şu: **eksenler askı ile seyir arasında görev değiştiriyor.**

| Aygıt | Seyirde | Askıda |
|---|---|---|
| Sağ/sol uç çifti | sapma | **bank** |
| Üst/alt uç çifti | yunuslama | öne/arkaya eğilme |
| **Şerit** | **yatış** | **yön** |

Askıda yanal konum denetimi **bank** ister — ve bank, **en uzun kolu olan** sağ/sol
çiftinden geliyor (1,726 m). Askıda en az acil eksen olan **yön**, en zayıf aygıttan
(şerit) geliyor. **Tahsis aslında elverişli, ama makale bunu tersinden anlatıyor.**

---

## HATA 2 — "Yatış pervanelerle ÜRETİLEMEZ" yanlış. ChatGPT buldu. Bu daha ağır.

### Kaynakta ne yazıyor

§2.10, satır 811–814:

> *"every thrust vector is parallel to the body axis, so no combination of settings produces a
> rolling moment."*
>
> *"**Roll cannot be produced by propellers at all**, because every pair is coaxial and
> torque-balanced by construction."*

**Birinci cümle doğru** — itkiler X_b'ye paralel, X_b etrafında **itkiden** moment çıkmaz.

**İkinci cümle yanlış.** Tepki torkunu atlıyor. §2.9 şunu söylüyor:

> *"**Each rotor is driven by its own electric machine** on a common axis."*

**Bağımsız sürülen iki karşıt rotor farklı devirlerde döndürülebilir ve torkları artık
birbirini götürmez.** Net tork X_b etrafındadır — yani gövde yatışı, askıda yön.

### Büyüklüğü — ihmal edilebilir değil

Burun çifti askıda 10,9 kW, ω ≈ 273 rad/s → **rotor başına ≈ 20 N·m.**

| Dengesizlik | Net X_b torku |
|---|---|
| %5 | 1,0 N·m |
| %10 | 2,0 N·m |
| %20 | 4,0 N·m |
| **%30** | **6,0 N·m** |

**Şerit askıda 6,0–12,0 N·m veriyor.** Yani %30'luk bir devir dengesizliği **şeridin alt
ucuyla aynı mertebede.** Bu bir kanal ve makale onu yok sayıyor.

(Uç çiftleri için önemsiz: rotor başına 0,077 N·m.)

### Ve makale kendi kendisiyle çelişiyor

§2.9, askı tork artığı için:

> *"Either the residual is small enough to be absorbed by the **speed trim of the pairs** —
> which this study has not shown — or a fourth duty falls on the strip."*

**"Çiftlerin hız trimi" tam olarak diferansiyel devirdir.** Yani makale bir yerde X_b torkunun
hız trimiyle üretilebileceğini varsayıyor, başka bir yerde *"yatış pervanelerle üretilemez"*
diyor. **İkisi aynı anda doğru olamaz.**

### Doğru ifade

> Yatış, itki vektörlerinden **üretilemez** — hepsi gövde eksenine paraleldir.
> Tepki torkundan **üretilebilir**, çünkü her rotorun kendi makinesi vardır.
> **Bu yapılandırma onu kontrol kanalı olarak KULLANMAMAYI seçer**, çiftleri tork dengeli
> işletir, ve yatışı şeride verir. Bu **fiziksel bir imkânsızlık değil, bir tasarım kısıtıdır.**

---

## Neyi etkiliyor

| Yer | Ne değişiyor |
|---|---|
| `CLAUDE.md` §0.1 | *"Yatış eşeksenli pervanelerle ÜRETİLEMEZ"* — **kuralın kendisi bu hatayı taşıyor.** Yazarın onayına sunuluyor |
| §2.10 | İki cümle: *"cannot be produced at all"* ve *"thirty-degree bank"* |
| Adım 7 | Sınır paragrafı |
| Adım 8 | Yatış paragrafı ve askı tork artığı |
| Adım 5 | Askıda gösterilmeyenler listesi |

## Bunun uçağa etkisi — zayıflatmıyor, güçlendiriyor

**Bir iddia zayıflıyor** (*"üretilemez"* → *"kullanılmıyor"*), **ama uçak güçleniyor:**

1. **Askı tork artığının bir çözümü var.** Adım 8'in açık kalemiydi; hız trimi gerçekten
   bir kanal, ve §2.9 bunu zaten sezmiş.
2. **Şerit için bir yedek var.** Askıda şerit yalnız slipstream'in yıkadığı bölümden basınç
   buluyor; diferansiyel devir hava hızından bağımsız çalışır.
3. **Ve takas artık adı konmuş bir seçim.** *"Yapamıyoruz"* demek zayıftır; *"kullanmıyoruz,
   çünkü pervaneleri tork dengeli işletmek girdap ve verim açısından tercih ediliyor, ve
   bedeli şerittir"* — bu bir mimari karardır ve fiyatlanabilir.

**Ama bedeli sayılmadı.** Diferansiyel devir itki asimetrisi ve verim kaybı getirir, ve rotor
ataleti yüzünden yavaştır. Hiçbiri hesaplanmadı. **Yeni açık kalem.**
