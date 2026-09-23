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
