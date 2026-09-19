# Zincir ve menziller yeniden çözüldü

**Girdi:** `paper/nose-pair-finding.md` — makalenin askı FM'ini tutturan palet seyirde
η_p = 0,632–0,683 veriyor, makale 0,80 diyor.
**Kod:** `aero/chain_resolve.py`, `aero/nose_propeller_heavy.py`.
**Çıktı:** `aero/chain-resolve-result.txt`, `aero/nose-propeller-heavy.txt`.

---

## 0. Önce doğrulama — zincir makalenin basılı sayılarını yeniden üretiyor mu

Evet, birebir. Değiştirilmemiş ayarla §3.6'nın **yayımlanmış** satırı:

| | sabit yakıt kesri | sabit yakıt kütlesi | sabit MTOW |
|---|---:|---:|---:|
| B — lift + cruise | **+21,1 %** | **−5,4 %** | **−44,9 %** |
| C — tilt | **+58,3 %** | **+49,2 %** | **+35,7 %** |

Makalenin §3.6'da basılı olan sayılar bunlardır. Zincir doğrulanmadan hiçbir yeni sayı
raporlanmadı.

## 1. Zincir

Motor 0,28 × jeneratör 0,90 × güç elektroniği 0,95 × makine 0,92 = **0,2202**, pervane hariç.

| | η_p | zincir | hafif menzil | ağır menzil |
|---|---:|---:|---:|---:|
| makalenin varsayımı | 0,800 | 0,1762 | 1598 km | 1814 km |
| hesaplanan, üst uç | 0,683 | 0,1504 | **1364 km** | — |
| hesaplanan, alt uç | 0,632 | 0,1392 | **1262 km** | — |

**Ağır hat kendi iki noktalı hesabını aldı** — hafif hattın oranı taşınmadı:

| pala | c_l | FM | **η** | menzil |
|---|---|---:|---:|---:|
| 2 | 0,55 | 0,597 | 0,616 | 1398 km |
| 2 | 0,70 | 0,597 | **0,669** | 1517 km |
| 3 | 0,55 | 0,601 | 0,619 | 1404 km |
| 3 | 0,70 | 0,603 | 0,656 | 1488 km |

> Ağır: η = **0,616–0,669**, menzil 1814 → **1398–1517 km**, düşüş **%16,4–22,9**.
> Hafif: η = **0,632–0,683**, menzil 1598 → **1262–1364 km**, düşüş **%14,6–21,0**.

**Ceza ölçekle kaybolmuyor**, ağır uçta biraz daha kötü. Bu §3.9'u ilgilendirir: üç fatura
ölçekle ayrışıyor, ama pervane cezası ayrışmıyor.

## 2. En önemli modelleme kararı — ve açıkça söyleniyor

`baseline.py`'de `eta_zincir` **GOREV** sözlüğünde, yani üç mimaride de aynı. Bu, her üçüne
0,80 vermek demek. Hesap A için bunun yanlış olduğunu gösterdi. B ve C için de yanlış mı?

| | Neden | η_p |
|---|---|---|
| **A** kuyruk üstü | Tek **sabit hatveli** propulsor, iki görev | **0,632–0,683 (hesaplandı)** |
| **B** lift + cruise | Seyir pervanesi **yalnızca seyir** yapar; askıyı ayrı rotorlar yapar → palet seyir için tasarlanabilir | 0,80 korunur |
| **C** tilt | Tek propulsor iki görev, **ama değişken hatve göbeği var** → palet her rejimde ayarlanır | 0,80 korunur |

**Üçüncü satır sonucun kendisidir.** Makale değişken hatve göbeğini elediğini söylüyordu ama
**neye mal olduğunu hiç yazmamıştı.** Şimdi bir sayı var.

**C için 0,80 bir fizik iddiası değildir.** Makalenin kendi anlaşması budur: *"C_LD = C_eta =
1,00 varsayılanı, tilt'in seyirde HİÇBİR aerodinamik veya itki cezası ödemediği
İDEALLEŞTİRİLMİŞ ÜST SINIRDIR."* Gerçek tilt-rotorların seyir verimi bundan kötüdür; sınır
olarak okunur, sonuç olarak değil.

## 3. Yayımlanmış tablo, yeniden çözülmüş

| | basılı | A üst uç | A alt uç |
|---|---:|---:|---:|
| **B**, sabit yakıt kesri | +21,1 % | +41,8 % | +53,3 % |
| **B**, sabit yakıt kütlesi | **−5,4 %** | **+14,4 %** | **+25,9 %** |
| **B**, sabit MTOW | −44,9 % | −24,3 % | −11,5 % |
| **C**, sabit yakıt kesri | +58,3 % | +85,5 % | +100,4 % |
| **C**, sabit yakıt kütlesi | +49,2 % | +80,5 % | +98,7 % |
| **C**, sabit MTOW | +35,7 % | +73,5 % | +96,3 % |

A'nın kendi sayıları (rotorlar faturalanmış hal): menzil 1133 → **895–967 km**,
MTOW 54,5 → **57,6–59,4 kg** (seyir gücü artınca motor büyüyor, döngü geri besliyor).

### 3.1 Kırılan cümle

§3.6 şunu diyor:

> *"Against lift-plus-cruise the conclusion now depends on the rule: **the tail-sitter leads
> under two of the three and loses the third**…"*

**İşaret sabit yakıt kütlesinde dönüyor: −5,4 % → +14,4 % / +25,9 %.** Kuyruk üstü artık
**üçte ikisinde değil, üçte birinde** önde (yalnız sabit MTOW). Cümle olduğu gibi duramaz.

### 3.2 Ayakta kalan

**Sözleşme bağımlılığı duruyor.** B'ye karşı sıralama hâlâ sözleşmeye göre **tersine
dönüyor** — B iki sözleşmede önde, birinde arkada. Bulgu C ayakta; değişen şey, dönüşün
2'ye 1 değil 1'e 2 olması. Tilt'e karşı zaten menzil iddiası yoktu ve şimdi de yok; paylar
büyüdü, o kadar.

## 4. Karşı senaryo — hepsi aynı cezayı öderse

**İlk yazımda bunu yanlış ayarda koşturdum ve Qwen'in itirazı onu buldurdu.** §3'ün karşı
senaryosu rotor terimi **öncesi** ayardaydı; yayımlanmış tablo ise rotorlar faturalanmış
halde. Karşılaştırılması gereken şey ikincisiydi. Doğrusu:

| | yayımlanmış ayar, A = 0,80 | **aynı ayar, hepsi 0,632** |
|---|---:|---:|
| B, sabit yakıt kesri | +21,1 % | **+21,1 %** |
| B, sabit yakıt kütlesi | −5,4 % | **−5,7 %** |
| B, sabit MTOW | −44,9 % | **−42,3 %** |
| C, sabit yakıt kesri | +58,3 % | +58,3 % |
| C, sabit yakıt kütlesi | +49,2 % | +51,8 % |
| C, sabit MTOW | +35,7 % | +42,8 % |

> **Ceza simetrik olsa bile işaret SÖZLEŞMELER ARASINDA dönüyor:** sözleşme 1'de +21,1
> (B önde), sözleşme 2'de −5,7 ve sözleşme 3'te −42,3 (A önde). Dönüş 1 ile 2 arasında.

*(Bu satır bir **karşı-olgusaldır**: B ve C'ye A'nın hesaplanmış veriminin verilmesi, bulgunun
cezaya bağlı olup olmadığını sınamak içindir. B ve C'nin pervanelerinin gerçekten 0,632 verdiği
iddia edilmiyor. — Qwen'in uyarısı. Ayrıca sütunları satırlarla karıştıran bir yanlış okuma
oldu; dikkatli bir okuyucu karıştırdıysa hakem de karıştırır, bu yüzden başlıklar değiştirildi.)*

**Sözleşme bağımlılığı bulgusu, cezanın mimariye özgü olmasına BAĞLI DEĞİL.** Ters dönüş
her iki senaryoda da var. Mimariye özgü ceza **dönüşün yerini** kaydırıyor (2'ye 1 yerine
1'e 2), **varlığını** değil.

Yüzdeler simetrik senaryoda neredeyse değişmiyor ama **tam olarak** değişmiyor değil
(−5,4 → −5,7; −44,9 → −42,3): kapanma döngüsü geri besliyor, çünkü düşen η_p seyir gücünü,
seyir gücü motoru, motor kütleyi büyütüyor.

## 5. Kendi kodumuzda bulduğumuz şey

`baseline.py`'nin `duyarlilik_C()` işlevi **tilt'i** askıya boyutlanmış palet için
cezalandırıyor ve η'yı 0,85'e kadar tarıyor. Gerekçesi kodda yazılı:

> *"eta -- pal hover'a boyutlanmis (yuksek disk yuku, yanlis burulma) → **seyirde A'nin
> pervanesinden IYI olmasi beklenmez**"*

Yani **A'nın pervanesi, rakibin cezalandırıldığı ölçüt olarak kullanılmış** — ve kendisi hiç
ölçülmemiş. Aranan türden kendine hizmet eden varsayım tam olarak budur ve makalenin kendi
kodunda, yazılı hâlde duruyordu.

## 6. Makalede ne değişecek

1. §2.12'nin zinciri: *"propeller 0.80 — overall 0.176"* → **mimariye özgü**, A için
   hesaplanmış aralık.
2. §3.7 ve §3.8'in menzil satırları → **1262–1364 km** ve **1398–1517 km**.
3. §3.6'nın tablosu ve **"üçte ikisinde önde"** cümlesi.
4. §3.9 (ölçek): pervane cezasının ölçekle **ayrışmadığı** eklenir.
5. Özet ve vurgular: 1598/1814 geçen her yer.
6. Üçüncü iddianın bedeli artık **sayısaldır** — değişken hatve göbeğini reddetmek
   seyir veriminde 0,80 yerine 0,63–0,68 demek.

## 7. Sınırlar — §1'dekiler burada da geçerli

En güçlü karşı argüman aynı: **eşeksenli karşıt dönüşün girdap geri kazanımı sayılmıyor**,
yani η tahmini muhafazakâr tarafta. O pay η'yı belki 0,70'e taşır, 0,80'e değil. Aile tek
parametreli; kesit NACA 0012; pala sayısı ve veter seçildi, ölçülmedi.

**Menzil düşüşü tezi tehdit etmiyor** (`CLAUDE.md` §0.7). Tehdit ettiği tek şey §3.6'nın
bir cümlesidir, ve o cümle düzeltilir.
