# v8 kısaltma — uzlaşı belgesi

**Yöntem (yazar, Tur 61):** kısaltma doğrudan yapılmaz. Her okuyucunun önerisi herkese yan yana sunulur, görüş
alınır; **önce hemfikir olunanlar işlenir**, ayrışanlar geri sorulur; karar yazarındır. Bu belge her tur
güncellenir.

**Ruh (yazar, Tur 61, CLAUDE.md §0.8):** makale bir kavrayışın sunumudur; hesaplar onu Q1 hakemi önünde
denetlenebilir kılmak için vardır. Ruh yüklemi genişletmez.

**Hedef (`v8-budget.md`):** ~7 500 kelime metin, 6 şekil, 8 tablo. Şu an: 30 096 kelime, 16 tablo, adımlarda şekil yok.

---

## Tur 60 — kimler cevap verdi

| Okuyucu | Durum |
|---|---|
| Grok | **Tam cevap** (7 sorunun hepsi, 49 çekince alıntısı) |
| DeepSeek | **Tam cevap** (7 sorunun hepsi, 53 çekince alıntısı) |
| ChatGPT | Dosyaları aldığını söyledi, **cevap vermedi** — görev bekledi |
| Qwen | Dosyaları aldığını söyledi, **cevap vermedi** — görev bekledi |

Aşağıdaki "uzlaşı" bu yüzden **iki okuyucunun** uzlaşısıdır; Tur 61'de dördüne de sunuluyor.

---

## A. Hemfikir olunanlar (Grok + DeepSeek) — önce bunlar işlenecek

| # | Konu | Uzlaşı |
|---|---|---|
| A1 | Çerçeve kararı | **İkisi de "orantılı kısalsın" okumasını varsaydı**: çerçevenin *işlevleri* korunur (üç fatura, kaçış koşulu ve dört başarısızlık kipi, bağımsız sınama, ölçek bulgusu, sözleşme bulgusu), *adım uzunlukları* korunmaz; bir göstergeye (pointer) indirilmez. Yazarın Tur 61 cümlesi (*"Hesap kısmını neden yaptık? Q1 için."*) bu okumayla tutarlı. **Yazarın onayı bekleniyor.** |
| A2 | Birleştirme | **Adım 7 + Adım 8 tek bölüm** — "çözümlerin birleştirilmesi" kendi bölümü; 3 ya da 4'e katlanmaz. Katkının bölümü budur. |
| A3 | Adım 15 | Kısa bir kapanış: dört eksen, sayıların ardından; ikinci bir Adım 9 değil. |
| A4 | Tek ev | %2 görev çevrimi → **Adım 2**. *"By construction = by the sizing"* → **Adım 9**. Diğer hibritlere menzil iddiası yok → **9 (ret) + 13 (bulgu)**; 15'te bir cümle. Kısmi gerçekleşme → **Adım 3 tanımlar**, 7/8 uygular, gerisi işaret. Mekanizma sınıfı tablosu → **Adım 7**; 15 tabloyu tekrar basmaz. 14'ün borç listesi → **14**; 15 tek paragraf. 1954 anlatısı ve "zaten dolu olan" → ikisi de **Adım 1**'de, sıkıştırılmış. Adım 11'in açılışı/kapanışı → bir kez. |
| A5 | Gövdede kalmalı | Seyir ekseni: Adım 6'nın L/D_e dönüşümü, 5,56–7,39 zarfı, iki quadrotor karşılaştırması, beş nitelendirme (cümle olarak). Pist ekseni: Adım 5'in şartı ve "boyutlandı / gösterilmedi" listesi + Adım 14'ün depo sayıları. Mekanizma: Adım 7 + 8. Menzil reddi: Adım 9'un dördüncü satırı + Adım 13'ün ana tablosu. |
| A6 | Eke gidebilir | Adım 10'un yayılım tablosu (bir cümle kalır); Adım 13'ün duyarlılık matrisi (gövdede en fazla bir satır: kaldırma grubu); Adım 14'ün uzun bilinmeyenler tablosu (gövdede başlıklar/özet); 1954 anlatısının uzun kısmı; Adım 4'ün bir kısmı (Grok: quadrotor karşıtlığı; DeepSeek: ağırlık dökümü) — lift+cruise / tilt-wing izolasyon çifti ve sonucu gövdede kalır. |
| A7 | Tablolar — gövdede | **Altı tabloda uzlaşı:** Adım 6 L/D_e köşeleri · Adım 6 iki quadrotor · Adım 7 mekanizma sınıfları · Adım 10 A–D kapanışları · Adım 13 üç sözleşme · Adım 14 depo yeniden kapanışı. Hedef 8; **iki yer açık** (B7). Dışarıda uzlaşı: Adım 10 yayılım tablosu, Adım 13 duyarlılık matrisi (eke). |
| A8 | Tur 59 düzeltmeleri | İkisi de: kaynaklarına sadık, yeni çelişki yok. |
| A9 | Kesilemeyecek çekinceler | Birleşik liste **100 satır** (`v8-caveats.md`), hepsi metinde doğrulandı; otomatik denetim `v8_caveats.py`. |

## B. Ayrışanlar — Tur 61'de dördüne geri soruluyor

| # | Konu | Grok | DeepSeek |
|---|---|---|---|
| B1 | **"Why the result holds" hangi adım?** | Adım 9 (sınır) | Adım 12 + 13 (ölçek ve sözleşme), ve 12–13'ü 10'dan önceye alıyor |
| B2 | Adım 2, 3, 4 | Tek bölüm, üç alt bölüm | Üç ayrı bölüm |
| B3 | Adım 5 ve 6 | Q2'de "tek bölümde iki kısa yarı", haritasında iki ayrı bölüm (**Grok'un kendi içinde tutarsız**) | Koşut yapı korunsun, iki ayrı bölüm |
| B4 | Tepki torku reddinin evi | **Adım 8** (+1 ve 7'de birer cümle) | **Adım 7 ve 8** |
| B5 | "Geçiş gösterilmedi"nin evi | **Adım 7** | **Adım 9** (sınır) + **Adım 10** (5,4 m) |
| B6 | Sabit hatve açığının evi | **Adım 11** (14,6–21,0 %) | **Adım 6** (açık ve nedeni), 11 atfeder |
| B7 | Kalan iki tablo | Sekize inmek için **Adım 2 aktarım** ve **Adım 11 C_D0 dökümü** kalır; 3, 4 ve **9'un dört eksen tablosu** düzyazıya | **Adım 9 dört eksen** ve **Adım 9 bağımlılık** tabloları gövdede; 2'nin aktarım tablosu ek ya da yoğunlaştırılmış; 11'in dökümü eke, %57–69 gövdede; 3 ve 4 adımlar kalırsa gövdede |
| B8 | Adım 2'nin aktarım tablosu | Gövde (araç) | Ek ya da yoğunlaştır |

**B1 benim çeviri hatamdan doğmuş olabilir.** Yazarın akış öğesi *"ortaya çıkan ürünün sorunsuzluğu"*. Tur 57'deki oran
incelemesinde bunu Adım 8–9'a eşledim ve İngilizceye *"why the result holds"* diye çevirdim. Bu çeviri DeepSeek'i ölçek
ve sözleşme bulgularına yönlendirdi. Doğrusu **"the soundness of the resulting product"** — birleşik uçağın bir bütün
olarak sorunsuz olduğu. Tur 61'de düzeltilip yeniden soruluyor. Eşlemenin kendisi (8–9) da benimdi, yazarın değil.

## C. Açık — yazarın kararı

| # | Konu |
|---|---|
| C1 | A1'in onayı: çerçeve orantılı mı kısalsın? |
| C2 | **Ruh ile öncelik sınırı arasındaki gerilim.** Adım 1 *"not a claim that the route was waiting to be found"* diyor (Tur 46'da üç okuyucunun boşluk iddiasını çürütmesinden sonra). Yazarın Tur 61 duruşu *"görülememişi görmüş olmak"*. Kavrayış **yüklem genişletilmeden** nasıl taşınır? Okuyuculara da soruluyor. |
| C3 | *"Ürünün sorunsuzluğu"* hangi adımlar? (B1) |

---

# Tur 61 — dört okuyucu da cevap verdi; ilk kısaltma kümesi uygulandı

**Yeni kural (yazar, Tur 62 mesajı):** ben de bir okuyucuyum; görüşümü her turda yazarım ve okuyucular onu da
eleştirir. **Uygulama eşiği: dört okuyucu + ben.** (CLAUDE.md §2.3 eki.)

## Oylar (G = Grok, C = ChatGPT, D = DeepSeek, Q = Qwen, K = Claude)

| # | Konu | G | C | D | Q | K | Sonuç |
|---|---|---|---|---|---|---|---|
| A1 | Çerçeve orantılı kısalır, işlevleri korunur | ✓ | ✓ | ✓ | ✓ | ✓ | **Karara bağlandı** (C1 kapandı) |
| A2 | Adım 7 + 8 tek bölüm (birleştirme) | ✓ | ✓ | ✓ | ✓ | ✓ | **Karar**; 8'in bir kısmının "sorunsuzluk"a gidip gitmeyeceği B1'de |
| A3 | Adım 15 kısa kapanış | ✓ | ✓ | ✓ | ✓ | ✓ | **Uygulandı** (1 023 → 337) |
| A4 | Tek evler (2, 9, 9+13, 3, 7, 14, 1, 11) | ✓ | ✓ | ✓ | ✓ | ✓ | **Adım 11 ve 15'te uygulandı**; öteki işaretçiler sonraki kümede |
| A5 | Gövdede kalmalı | ✓ | ✓ | ✓ | ✓ | ✓ | Karar |
| A6 | Eke taşınabilir | ✓ | ✓ | ✓ | ✓ | ✓ | **Üçü uygulandı**: 10 yayılım → cümle; 13 duyarlılık → Ek S13; 14 bilinmeyenler → Ek S14 (gövdede liste). 1954 ve Adım 4 kısmı sonraki kümede |
| A7 | Altı tablo gövdede | ✓ | ✓ | ✓ | ✓ | ✓ | Karar |
| A8 | Tur 59 düzeltmeleri | ✓ | ✓ | ✓ | ✓ | ✓ | Kapandı |
| A9 | Çekince listesi | ✓ | ✓ (*"denetim listesi, birebir zorunluluk değil"*) | ✓ | ✓ | ✓ | Karar; biçim ilkesi aşağıda |
| — | Adım 9 bağımlılık tablosu → düzyazı | ✓ | ✓ | ✓ (Tur 61) | ✓ | ✓ | **Uygulandı** |
| — | Adım 3 ve 4 tabloları gövdede değil | ✓ | ✓ | ✓ | ✓ | ✓ | **Karar**; düzyazıya çevirme sonraki kümede (dikkat isteyen yeniden yazım) |
| C2 | Adım 1: ret cümlesi katkıdan önce, paragraf katkıyla biter | ✓ | ✓ | ✓ | ✓ | ✓ | **Uygulandı** (yüklem değişmedi) |
| B1 | "Ürünün sorunsuzluğu" | 8+9 | 9 + köprü | 8+9 | 9 (8 7'de kalır) | 9 + 8'in "ne hâlâ hareket ediyor / ne başarısız / ne çözülmedi" kısmı | Ortak çekirdek: **9 orada, 12–13 orada değil** (dördü). 8'in yeri açık |
| B2 | 2–4 | tek bölüm | tek bölüm | **üç bölüm** | tek bölüm | tek bölüm | 4–1; **DeepSeek karşı** → uygulanmaz, geri soruluyor |
| B3 | 5 ve 6 | iki bölüm | iki | iki | iki | iki | **Karar** |
| B4 | Tepki torku evi | 8 (+1, 7 birer cümle) | 8 (7 bir cümle) | 7 ve 8 | 8 (7 cümle, 9 sınır) | 8, 7'de seçim cümlesi | Yakın uzlaşı: **8 ev, 7'de bir cümle**; DeepSeek'in *"7 seçimi söyler, 8 sonucu"* bununla uyumlu mu — soruluyor |
| B5 | "Geçiş gösterilmedi" evi | 7 (+10 sayı) | 7 (9 sınır, 10 sayı) | 9 (+10, 7 ayrım) | 9 (+10, 7 işaret) | **7** | 3–2; açık |
| B6 | Sabit hatve açığı evi | 11 | 6 | 6 | 11 | **6** | 3–2; açık |
| B7 | Açık iki tablo yeri | 2 + 9 dört eksen | 2 + 11 döküm | 9 dört eksen + 2 | 9 dört eksen + 11 döküm | **2 + 9 dört eksen** | 2: G C D K (4); 9 dört eksen: G D Q K (4); 11 döküm: C Q (2). Çoğunluk 2 + 9; oy birliği yok |

## Çekince listesi — Tur 61

- Okuyucuların *"eksik"* dediği **35 satır eklendi** (Grok 5, DeepSeek 13, ChatGPT 1, Qwen 18; örtüşenler birleşti), hepsi
  metinde doğrulandı. Grok'un parça uyarısıyla Adım 8'in cümlesi tamlandı. **Toplam 135 çekince + 5 ruh cümlesi = 140.**
- **Çıkarma önerileri uygulanmadı:** Grok 3 satır (Adım 7 *"not decoration"*, Adım 3 tekrar, Adım 15'in iki satırı), Qwen 2
  satır (Adım 10 *"spread is the finding"*, Adım 14 *"for the first item"*). DeepSeek *"hiçbiri yük taşımaz değil"* dedi → oy
  birliği yok. (Adım 15'in iki satırı kısa kapanışta zaten korundu.)
- **Biçim ilkesi (ChatGPT'nin ayrımına benim cevabım):** denetim birebir kalır; bir çekince sıkıştırılırsa **aynı
  commit'te** listedeki satır yeni cümleyle güncellenir ve bir sonraki turda eski/yeni yan yana gösterilir. Böylece hem
  sıkıştırma mümkün hem de hiçbir çekince sessizce düşmez.
- **Ruh cümleleri (benim önerim):** beş cümle — Adım 1 katkı cümlesi, Adım 6 menteşe cümlesi (ChatGPT), Adım 7'nin katkı
  cümlesi (Grok), Adım 7 *"That single move is what removes the mechanism."*, Adım 15 son cümlesi. Aynı denetim.

## Ölçü

| | Tur 60 | Tur 61 kümesinden sonra |
|---|---:|---:|
| Kelime (gövdeler) | 30 096 | **28 515** (−1 581, %5,3) |
| Tablo | 16 | **12** |

---

# Tur 62 cevapları → Tur 63

**Yeni kural (yazar):** uygulanan bir değişiklik, **sonucu herkes tarafından teyit edilene kadar kapanmaz** (CLAUDE.md §2.3).

## Tur 62'de uygulananların teyidi

| Değişiklik | G | C | D | Q | Durum |
|---|---|---|---|---|---|
| Adım 1 ret/katkı sırası | ✓ | ✓ | ✓ | ✓ | **Kapandı** |
| Adım 9 bağımlılık düzyazısı | ✓ | ✓ | ✓ | ✓ | **Kapandı** |
| Adım 10 yayılım cümlesi | ✓ | ✓ | ✓ | ✓ | **Kapandı** |
| Adım 11 kapanış | ✓ | ✓ | ✓ | koşullu: *"No charge on this page is a new one"* korunmuyor | Özü açılışta: *"No new physical cost term is introduced here."* → **çekince listesine eklendi**; Qwen'e teyide |
| Adım 13 → Ek S13 + sarkık atıf | ✓ | ✓ | ✓ | ✓ | **Kapandı** |
| Adım 14 → Ek S14 + liste | **✗ — bir yan cümle düştü** (uç çiftlerinin kalkış payı ile tutum yetkisi arasındaki paylaşımı) | ✓ | ✓ | ✓ | **Geri kondu**; yeniden teyide |
| Adım 15 kısa kapanış | ✓ (liste cümle olarak kaldı, tolere) | ✓ | ✓ | ✓ | **Kapandı** |

## Oylar (G C D Q K)

| # | Konu | G | C | D | Q | K | Sonuç |
|---|---|---|---|---|---|---|---|
| Biçim | Çekince birebir denetlenir; sıkıştırılırsa aynı commit'te güncellenir, eski/yeni gösterilir; güç insan gözüyle | ✓ | ✓ | ✓ (+insan denetimi) | ✓ | ✓ | **Karar** |
| B2 | 2–4 tek bölüm, üç alt bölüm | ✓ | ✓ | ✓ (fikir değiştirdi) | ✓ | ✓ | **Karar** |
| B4 | Tepki torku: ev 8, 7'de seçim cümlesi, 1 ve 15'te yan cümle | ✓ | ✓ | ✓ | ✓ | ✓ | **Karar** — metin işaretçileri taslakla gösterilecek |
| B5 | "Geçiş gösterilmedi": ev 7; 10 sayı; 9 işaret | ✓ | ✓ | ✓ | ✓ (fikir değiştirdi) | ✓ | **Karar** — taslakla gösterilecek |
| — | Adım 14 kapanıştan önce kendi bölümü | ✓ | ✓ | ✓ | ✓ | ✓ | **Karar** |
| — | Adım 9 dağıtılmaz; sekiz ret evinde söyleniyorsa kısalır | ✓ | ✓ (fikir değiştirdi) | ✓ | — | ✓ | Yakın; Qwen açık |
| N2 | Adım 4 tablosu → düzyazı | ✓ | ✓ | ✓ | ✓ | ✓ | **Uygulandı** → teyide |
| N4 | Adım 4 ağırlık dökümü + quadrotor karşıtlığı → Ek S4 | ✓ | ✓ | ✓ | ✓ (sonuç cümlesi kalsın) | ✓ | **Uygulandı** → teyide |
| N1 | Adım 3 tablosu → dört cümle | ✓ (parantez kalsın) | ✓ ama *"complexity"* ölçülmedi; *"case"* | ✓ | ✓ | ✓ | Ifade değişti → **yeni taslak** teyide |
| N3 | 1954 sıkıştırma | ✓ | ✓ | ✓ | ✓ | ✓ | Yön karar; **taslak** teyide (uygulanmadı) |
| B1 | "Sorunsuzluk" dilimi | 9 + 8'in çözülmemiş kalanı; başarısız parçalar 7+8'de | benimki | benimki | benimki | **Grok'un dilimine geçtim** | Açık — Grok'un dilimi soruluyor |
| B6 | Sabit hatve açığı | **✗** — sayı 11'de, reddiyle | 6 | 6 | 6 (fikir değiştirdi) | **Grok'un ayrımına geçtim**: olgu 6'da, sayı ve ret 11'de | Açık — öneri soruluyor |
| B7 | İki tablo yeri | 2 + 9 | **2 + 11** | 2 + 9 | **9 + 11** | 2 + 9 | Açık |
| #4 | *"removes the mechanism"* → *"removes the need for the mechanism"* | — | öneren | — | — | ✓ | Soruluyor |

**Korunan cümleler:** Qwen'in Adım 11 cümlesi çekinceye; Grok (Adım 7 dönüş çifti), DeepSeek (Adım 3 koşul, Adım 8 *"These are
the parts that fail"*), Qwen (Adım 2 köken cümlesi) ruh listesine. Grok'un Adım 6 menteşesini çıkarma önerisi oy birliği değil
(ChatGPT koruyor) → kaldı. Toplam 145.

---

# Tur 63–67 — durum

**Bu belge Tur 63'ten sonra güncellenmemişti** (benim eksiğim; turların ayrıntısı `effective-ld-finding.md`'de, Tur 63–67).
Aşağıdaki özet o kayıtlardan.

| Kalem | Durum |
|---|---|
| Adım 14 onarımı, Adım 11 (Qwen'in şartı), N2, N4, işaretçiler | **Kapandı** (Tur 64) |
| B1 (Grok'un dilimi), B6 (olgu 6'da; sayı ve ret 11'de), B7 (Adım 2 + Adım 9 tabloları gövdede) | **Karar** (Tur 64). B1 yapı kurulurken uygulanacak; B6'nın yerleşimi metinde zaten böyle (%14,6–21,0 yalnız Adım 11'de); B7'nin Adım 11 kısmı bir alt satırda |
| Adım 4 Qwen şartı, Adım 11 dökümü düzyazıya, N1, N3, *"removes the need for the mechanism"* | Uygulandı Tur 64 → **kapandı** Tur 65 |
| Adım 2 *"mechanical complexity"* | Uygulandı Tur 65 → **kapandı** Tur 66 |
| B4 tek ev (Adım 5, 7, 9); ses V1, V6; dokuzuncu tablo Ek S11'e; Adım 14'e girişim | Uygulandı Tur 66 → **kapandı** Tur 67 |
| Ses V3, V5 | **Uygulanmadı** — herkes korudu |
| Ses V4 | **Uygulanmadı** — Grok'un itirazı; ben görüş değiştirdim |
| V2 (Grok'un ifadesi), B5 (Adım 8 ve 9) | Uygulandı Tur 67 → **teyitte** (Tur 67 metni §2) |
| Adım 9 dağıtılmaz; sekiz ret evinde söyleniyorsa kısalır | **Açık** — Tur 63'te Qwen'in oyu yok |
| A4'ün kalan tek-ev işaretçileri (görev çevrimi vb.) | **Açık** |
| Tablo sayısı | **8** (hedef) |

## Hız — Tur 67

| | |
|---|---|
| Ölçüm | 30 096 → 27 689. Tur 62 −1 581; Tur 63–67 ortalama ~165. 7 500'e: ~50 tur (ortalama), >100 tur (son beş) |
| Claude'un ilk önerisi | Bölüm bütçesi + birleştirme bölümü önce — **yazar reddetti** (*"çözüm senin sunduğun gibi budamak olamaz"*), geri çekildi |
| Yazarın çerçevesi | En az 6–8 tur daha makul adım; okuyucuların çözümleri; olmazsa yenilik anlatılarının dışındaki hesap kısımları yontulur (`deferred-decisions.md` E4) |
| Claude'un yeni görüşü | Tutma listesi: adım adım, herhangi birinin listesindeki kalır, gerisi eke aynen; önce hesap kısımları — **oylamaya** |
| Durum | Okuyuculara soruldu (Tur 67 metni §3); çözümler Tur 68'de yan yana |

---

# Tur 68 — hız çözümleri yan yana

| | Grok | ChatGPT | DeepSeek | Qwen | K |
|---|---|---|---|---|---|
| Birim | adım | adım | adım | bölüm | adım |
| Yöntem | taslak | işlev sınıflama + en kısa sadık ifade | tutma listesi | korunan listelere karşı taslak | taslak (plan §6) |
| Önce yapıyı birleştir | evet | evet (en güçlü önerisi) | — | — | evet, üretilmiş görünüm |
| Hesap sırası | 12, 13, 11, 10 | 10, 11, 12, 13, 14 | 10, 11, 12, 13, 14 | 10, 11, 12, 13 | 12, 13, 11, 10 |
| Adım 7–8 | bu blokta yok | en sonda ses geçişi | hesaplara kadar küçük birim; sonra 5–8 tutma listesiyle | en son | bu blokta yok |
| Kelime hedefi | yok | ölçüt değil | — | var (~3 000) | yok (yazar) |

**Beşimizin ortak noktası (yön kararı, metin değişikliği değil):** önce hesaplar; birim bütün bir adım; 7–8 önce açılmaz;
taşınan malzeme eke aynen. **Ayrışan:** yöntem (taslak 4 / tutma listesi 1), yapının önce birleşmesi (2 evet, 2 sessiz),
sıra, Qwen'in kelime hedefi (yazarın kararıyla çelişiyor). **Tutma listesi:** Claude geri çekti. **Karar yazarın.**

**Açık öneriler (Tur 68 metni §7, oylamaya):** yapı birleştirme (G, C) · altı şekil (G) · yapılandırma şekli (D) · Adım 12
dışlamaları ve eşit-Re denetimi eke (G, D, Q) + düşük Re sınırının korunan listeye eklenmesi (K) · Adım 2 açılış cümlesi ilk
cümle (G) · 7–8 taslağı yok (G) · Adım 11 taslağında korunacaklar (G) · iddia omurgası (C) · paragraf başına tek iş (C) ·
7 500 ölçüt değil (C) · ek = gölge makale (C) · Adım 10 ilk geçiş modeli (D) · üç katman kuralı (D) · 10+11 birleşimi (Q) ·
ruh cümleleri bölüm başı/sonu (Q) · tanım tablosu (Q).

**v7 şekilleri:** Şekil 11 v8'in geri aldığı üç ifadeyi taşıyor → kural önerisi oylamada.

**Yazarın kararı:** plan onaylandı (Tur 68). Ürünler Tur 68 metni §7'de: birleştirilmiş görünüm (uygulanmadı — kaynak
değişmedi) ve Adım 12 taslağı (uygulanmadı; veto bekliyor).

# Tur 69

| Kalem | G | C | D | Q | K | Durum |
|---|---|---|---|---|---|---|
| Adım 12 taslağı (veto) | yok | yok | yok | yok | — | **Uygulandı** → teyide |
| Düşük Re sınır cümlesi korunsun | ✓ | ✓ | ✓ | ✓ | ✓ | **Eklendi** (151) |
| Adım 8 bölünmesi | ✓ | ✓ | ✓ | ✓ | ✓ | **Kapandı** |
| On iki eklem | onar (5.1/5.2) | onar | onar (5.1/5.2) | onar (regex) | 5.1/5.2 | **Görünümde onarıldı** → teyide |
| "These are the parts…" eklemi | kendi bağlantısı | olduğu gibi | "The tip pairs are…" | olduğu gibi | DeepSeek | **Açık** |
| 10+11 birleşimi | ✗ | ✗ | ✗ | geri çekti | ✗ | **Kapandı** (yok) |
| Tanım tablosu | ✗ | ✗ | ✗ | geri çekti | ✗ | **Kapandı** (yok) |
| v7 şekil kuralı | ✓ | ✓ (+ şekil–iddia denetimi) | ✓ | ✓ | ✓ | **Kapandı**; ChatGPT eki oylamada |

# Tur 70

| Kalem | G | C | D | Q | K | Durum |
|---|---|---|---|---|---|---|
| Adım 12 uygulaması + S12, eklemler | ✓ | ✓ | ✓ | ✓ | — | **Kapandı** |
| Adım 8 eklemi | DeepSeek'in | DeepSeek'in | kendi | DeepSeek'in (değişti) | DeepSeek'in | **Uygulandı** → teyide |
| Adım 12 ikinci geçiş | ✓ (+2 geri koyma) | ✓ | ✓ | ✓ (+1) | ✓ | **Uygulandı** → teyide |
| Adım 13 birinci geçiş | **13.2 veto**; 13.3, 13.6 geri koy | ✓ | ✓ | ✓ (13.6 notu) | ✓ | **Veto dışı uygulandı** → teyide |
| D/R etiketi (ChatGPT) | — | öneren | — | — | ✓ | Oylamada |
| Ek başlığı: kaynak adım + tur (DeepSeek) | — | — | öneren | — | ✓ | Oylamada |
| Ek kuralı: kaybı olan paragraf tam (Qwen) | — | — | — | öneren | ✓ | **Uygulandı** (S12, S13) + `v8_nothing_lost.py` |
| Adım 4 #18 daraltılmış (ChatGPT, Tur 76) | ✓ | öneren | ✓ | ✓ | ✓ | **Uygulandı** (Tur 77); teyide |
| İki "araç sabit" cümlesi korunan (G P20, Q P2, D) | öneren | ✓ | öneren | öneren | ✓ | **Uygulandı** (154); teyide |
| Adım 2–3 tek envanter, blok blok taslak | ✓ | ✓ | ✓ | ✓ | ✓ | **Envanter Tur 77 metninde**, teyide |
| Yineleme kuralı: iki ev = kesim, işini adlandıran hariç (G P22 + C) | öneren | öneren | — | — | ✓ | Oylamada (Tur 77) |
| "decline the mismatch" cümlesi korunan (Claude) | — | — | — | — | öneren | Oylamada (Tur 77) |
| S-1 tablo mekanizma satırları, (c) (Claude) | — | — | — | — | öneren | Görüş istendi (Tur 77) |
| Adım 4 kapanış (3.1, 3.2, 687/679) | ✓ | ✓ | ✓ | ✓ | ✓ | **KAPANDI** (Tur 78) |
| Yineleme kuralı (G P22 + C) | ✓ | ✓ | ✓ | ✓ | ✓ | **Kabul** (envanterde) |
| "decline the mismatch" korunan | ✓ | ✓ | ✓ | ✓ | öneren | **Uygulandı** (155) |
| S-1 (c) | ✓ (uygulama sonra) | HOLD | ✓ | ✓ | (d)'ye geçti | Açık → (d) oylamada (Tur 78) |
| S-2 "first departure" / S-3 "distinctness" | ✓ | ✓ | ✓ | ✓ | öneren | **Kabul**; S-2 taslakta, S-3 Adım 12 açılınca |
| P24 fatura adı → tanım bayrağı (G) / kural tahsis sınaması (C) | öneren | öneren | — | — | ✓ | İz tablosunda sütun olacak |
| 2E ile 3B: muhasebe / mimari görünüm, tek J (Qwen P2) | — | — | — | öneren | ✓ | 3B taslağında |
