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

### Büyüklüğü — ihmal edilebilir değil, ve ilk tahminim DÜŞÜKTÜ

> **DÜZELTME, aynı tur.** Burada önce şu yazıyordu: *"10,9 kW, ω ≈ 273 rad/s → rotor başına
> ≈ 20 N·m; %30 → 6,0 N·m."* **İki sayıyı karıştırıyordu:** 10,9 kW makalenin **yayımlanmış**
> askı gücü, 273 rad/s ise BEMT tablosunun **d_theta = 0** satırı — yani **seçilmeyen** palet.
> FM = 0,599'u tutturan paletler daha **yavaş** döner, dolayısıyla aynı güç için tork **daha
> büyüktür.** Sayı şimdi seçilmiş paletlerin kendisinden alınıyor: `aero/reaction_torque.py`.

| pala | c_l | ω_askı (rad/s) | çift kW | **rotor başına Q** | %10 net | **%30 net** |
|---|---|---:|---:|---:|---:|---:|
| 2 | 0,55 | 197,3 | 10,85 | **27,5 N·m** | 2,7 | **8,3** |
| 2 | 0,70 | 219,3 | 10,94 | **25,0 N·m** | 2,5 | **7,5** |
| 3 | 0,55 | 201,8 | 10,95 | **27,2 N·m** | 2,7 | **8,1** |
| 3 | 0,70 | 220,3 | 11,08 | **25,2 N·m** | 2,5 | **7,6** |

> **rotor başına 24,9–27,5 N·m** · %10 dengesizlikte **2,5–2,7 N·m** · %30'da **7,5–8,2 N·m**

**Çapraz denetim:** hesaplanan çift gücü 10,85–11,08 kW, makalenin yayımlanmış **10,9 kW**'ını
bağımsız olarak yeniden üretiyor (en büyük sapma **%1,7**). Betik sapma %5'i aşarsa sayıyı
yayımlamadan çıkıyor.

**Şerit askıda 6,0–12,0 N·m veriyor.** Yani %30'luk bir devir dengesizliği şeridin aralığının
**içinde** kalıyor, alt ucunda değil — ve şeridin alt ucunu yakalamak için yalnız **%22–%24**
dengesizlik yetiyor. **Bu bir kanal ve makale onu yok sayıyor.**

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

---

## DOĞRULAMA — iki belge, birinci elden okundu

**Tarih: 2026-09-20.** Yazar iki PDF'i depoya yükledi; ikisi de `pdftotext` ile açıldı ve
alıntılar dosyadan alındı. Hatırlanarak değil.

### Zhang ve ark. 2012 — `references/ica20120400001_12673514.pdf`

Eşeksenli karşıt dönüşlü kuyruk üstü. **HATA 2'yi doğrudan doğruluyor:**

> *"It balances the **anti-torque of the rotors by the inverse rotating of the two rotors**, to
> stabilize the flight attitude."* (satır 128–130)

— yani tork dengesi bizimkiyle aynı gerekçeyle kuruluyor. **Ve sonra o dengeyi bir kontrol
kanalı olarak kullanıyor.** Belgenin Tablo 2'si (satır 159–165), aynen:

| | **Vertical Mode** | **Horizontal Mode** |
|---|---|---|
| Yaw Motion | **Differential velocity of the two motors** | Rudde[r] |
| Pitch Motion | Stabilizer | Stabilizer |
| Roll Motion | Rudde[r] | **Differential velocity of the two motors** |
| VTOL | Increase or decrease the combined thrust of the two motors | – |

**Bu tek tablo iki hatayı birden kanıtlıyor:**

1. **HATA 2.** Eşeksenli, karşıt dönüşlü, tork dengeli bir çift, iki rotoru farklı devirlerde
   döndürülerek gövde ekseni etrafında moment üretir — ve bu uçakta **her iki kipte de birincil
   kanaldır.** *"Pervanelerle üretilemez"* cümlesi yanlıştır.
2. **HATA 1.** **Aynı fiziksel kanal** dikey kipte *"yaw"*, yatay kipte *"roll"* diye
   adlandırılıyor. Eksen adı değişiyor, eksen değişmiyor. Qwen'in bulgusu literatürde
   adı konmuş hâlde duruyor.

Düzyazıda da aynısı: *"In horizontal flight … **Roll motion is controlled by the differential
velocity of the two motors**"* (satır 128–129, sağ sütun).

### Novlit ve ark. 2014 — `references/2014_0529_paper.pdf`

Eşeksenli karşıt dönüşlü kuyruk üstü MAV. **HATA 1'i doğruluyor ve ayrıca Adım 1'e girdi:**

> *"A pair of 10 inches coaxial contra rotating propellers is mounted to **compensate each
> other's torque**."* (satır 58–60)
>
> *"**Elevon and rudder are immersed in the propeller slip stream** to provide three axis
> control moments in hover."*

— askı kontrolünün yerleşik cevabı budur ve biz onu reddediyoruz. Ve eksen adlandırması:

> *"…the definition of the **roll and yaw angles are interchanged.** The roll angle now
> represents the angle between the horizontal surface and the connecting line of the right and
> left wingtips, while the yaw angle represents the rotation around the centerline of the MAV
> fuselage."*

**Bu, Qwen'in bulgusunun literatürdeki karşılığıdır.** Eksenlerin askıda görev değiştirmesi
bilinen bir şeydir ve kuyruk üstü literatürü adını koymuştur. Bizim §2.10'umuz iki anlaşmayı
karıştırdı; kaynak karıştırmıyor.

---

## Neyi etkiliyor

| Yer | Ne değişiyor |
|---|---|
| `CLAUDE.md` §0.1 | **DÜZELTİLDİ** (yazar onayladı, Tur 47): yatış itkiden üretilemez, **tepki torkundan üretilebilir**, yapılandırma onu kullanmamayı **seçer** |
| §2.10 (v7) | İki cümle hatalı: *"cannot be produced at all"* ve *"thirty-degree bank"*. v7 yayımlanmış kayıt olarak duruyor; düzeltme v8'de |
| Adım 7 | **DÜZELTİLDİ** — sınır paragrafı yeniden yazıldı, kaynak satırı Zhang 2012 |
| Adım 8 | **DÜZELTİLDİ** — yatış paragrafı, eksen adlandırması, askı tork artığı paragrafı |
| Adım 5 | **Gerek yok** — Adım 5'te yatış iddiası hiç geçmiyor (arandı) |
| Adım 1 | **EKLENDİ** — Novlit 2014 ve Zhang 2012 "zaten dolu olan" bölümüne girdi; boşluk cümlesindeki *"cannot produce a rolling moment by any setting"* daraltıldı |
| `paper/prior-art-finding.md` | **DÜZELTİLDİ** — *"O takas literatürde bulunamadı"* paragrafındaki *"üretemez"* yanlıştı |

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
