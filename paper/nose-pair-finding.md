# Burun çiftinin çift görev denetimi — HESAPLANDI

**Durum: KAPANDI. Makalenin η_p = 0,80'i hak edilmiyor.**
Karar: yazar, Tur 38 — *"Hesabı yapalım, iki noktalı BEMT'yi programa al."*
Kod: `aero/nose_propeller.py`, `aero/nose_propeller_crossing.py`.
Çıktılar: `aero/nose-propeller-result.txt`, `aero/nose-propeller-crossing.txt`.

---

## 0. ÖNEMLİ SINIR — bu olgu literatürde BİLİNİYOR

Tur 46'da okunan De Wagter ve ark. 2018 (`references/Wagter_et_al_2018_Journal_of_Field_Robotics.pdf`)
insansız kuyruk üstü literatürünü tarıyor ve şunu doğrudan söylüyor:

> *"the fixed-pitch propellers make it **theoretically impossible** to be very efficient in both
> hovering and forward flight."*

Aynı belge kendi rotorunu *"a **compromise** between efficient hover and efficient forward
flight"* diye tarif ediyor ve çapını o esasa göre seçiyor.

**Dolayısıyla aşağıdaki hesabın bulduğu OLGU yeni değildir.** Yeni olan tek şey, o uzlaşmanın
**bu mimari için nicelenmesi** ve boyutlandırma döngüsünden geçirilmesidir: makalenin kendi FM
hedefinde η_p'nin ne çıktığı, zincire ne yaptığı, ve menzile ne yaptığı. **İddia buna göre
yazılacak** — *"keşfettik"* değil, *"ölçtük ve faturaladık."*

## 1. Soru neydi

Makale aynı **sabit hatveli** burun çiftine iki ayrı rejimden iki ayrı verim atfediyor:

| Ne | Değer | Nerede | Rejim |
|---|---|---|---|
| Askı figure of merit | **0,599** | §3.3 (1248), §3.8 (1725), §3.17 (2320) | askı |
| Seyir pervane verimi | **0,80** | §2.12 (982), zincir: *"propeller 0.80 — overall 0.176"* | seyir |

İkisinin **aynı palet geometrisinden** çıktığı hiçbir yerde gösterilmiyor. Dahası, makale
burun çiftinin devrini, pala sayısını, veterini ya da burulmasını hiçbir rejimde vermiyor
— tasarım tablolarında yalnız **çap** ve **disk yüklemesi** var. Uç çiftleri aynı makalede
yedi pala tasarımı, devir, uç Mach sayısı ve sayısal bir ceza alıyor (§3.4). Uçağın her iki
rejimde **bütün** itkisini üreten parça hiçbirini almıyor.

## 2. Yöntem

Uç çiftleri için yazılmış pala-eleman kodu (`aero/tip_propeller.py`) burun geometrisine
uygulandı. **Aynı denklemler olduğunu iddia etmek yetmediği için**, `capraz_denetim()` genel
motoru uç çiftinin kendi durumunda koşturuyor ve `tip_propeller.py` ile karşılaştırıyor:

```
                            om r/s     T (N)    cift W
nose_propeller motoru         2179      8.10       257
tip_propeller.py              2179      8.10       257
guc sapmasi 0.00 %
```

Sapma %2'yi aşarsa betik **durur ve sonuç yayımlanmaz.**

**Palet ailesi.** İlk plan dört köşeydi: askı için tasarla/seyirde koştur, ve tersi.
**Hesabın kendisi bu planı çürüttü.** Askı için tasarlanan palet bir **helikopter rotoru**
çıkıyor — hatve kökte 19°, uçta 6,9° — ve 30 m/s'de ancak uç Mach 0,96'da net itki veriyor.
Soru "H mi C mi" değil, **ikisinin arasında makalenin iki sayısını birden veren bir palet
var mı** sorusuymuş. Qwen bunu önceden söylemişti.

Aile tek parametreli: veter askı itkisinden sabitlenir, burulmaya düzgün bir kayma Δθ
eklenir. Δθ = 0 helikopter rotoru, Δθ büyük pervane. Parametre tam olarak takasın kendisi.

## 3. Takas — süpürme

2 pala/rotor, hedef kesit c_l = 0,55:

| Δθ (°) | ω_askı | M_uç | askı kW | **FM** | ω_seyir | J | **η** |
|---|---|---|---|---|---|---|---|
| 0 | 273 | 0,48 | 8,06 | **0,812** | 385 | 0,41 | **0,394** |
| 5 | 221 | 0,39 | 7,94 | 0,825 | 280 | 0,56 | 0,542 |
| 10 | 195 | 0,34 | 8,20 | 0,798 | 216 | 0,73 | 0,611 |
| 15 | 204 | 0,36 | 13,06 | 0,501 | 174 | 0,90 | 0,661 |
| 20 | 218 | 0,39 | 19,26 | 0,340 | 144 | 1,09 | 0,710 |
| 25 | 214 | 0,38 | 21,36 | 0,306 | 121 | 1,30 | 0,754 |
| 30 | 206 | 0,36 | 21,45 | 0,305 | 103 | 1,52 | **0,791** |

Takas tek yönlü ve monoton: **hatve artınca η yükseliyor, FM düşüyor.** Öteki üç ailede
(2 pala/c_l 0,70; 3 pala/c_l 0,55; 3 pala/c_l 0,70) aynı biçim.

## 4. Sonuç — makalenin FM'ini tutturan palet seyirde ne veriyor

Δθ üzerinde ikiye bölme, FM = 0,599 hedefiyle:

| pala | c_l | Δθ | FM | **η** | J | zincir | menzil km |
|---|---|---|---|---|---|---|---|
| 2 | 0,55 | 13,7 | 0,603 | 0,648 | 0,86 | 0,1426 | 1294 |
| 2 | 0,70 | 10,5 | 0,598 | **0,683** | 0,80 | 0,1504 | 1364 |
| 3 | 0,55 | 11,6 | 0,598 | **0,632** | 0,80 | 0,1391 | 1262 |
| 3 | 0,70 | 8,7 | 0,591 | 0,643 | 0,76 | 0,1415 | 1283 |

> **η = 0,632 – 0,683**, makalenin **0,80**'ine karşı.
> Zincir 0,176 → **0,139 – 0,150**.
> Hafif tasarımın menzili 1598 km → **1262 – 1364 km**, yani **%14,6 – %21,0 düşüş.**

**Ve ters yön de bedava değil.** η = 0,79'u veren palet (Δθ = 30) FM = 0,305 veriyor; o
palette askı gücü 10,9 kW değil **21,5 kW**, yani iki katı. Tampon, kütle bütçesi ve motor
boyutlandırması baştan değişir. **İki sayı tek palette birlikte yok, ve hangi ucu seçerseniz
seçin öteki uçtan ödüyorsunuz.**

Makalenin FM = 0,599 seçimi bu yüzden **düşmanca bir okuma değil** — menzil için aslında
elverişli uçtadır. Hak edilmeyen şey FM değil, ona eşlik ettiği söylenen η'dir.

## 5. Bu hesabın aleyhine olan şeyler — okuyucu bunları bilmeli

1. **Eşeksenli karşıt dönüşün girdap geri kazanımı SAYILMIYOR.** Çift, tek disk üzerinde
   2B paletle modelleniyor. Gerçek bir karşıt dönüşlü çift bundan bir miktar iyidir, yani
   **η tahminimiz muhafazakâr tarafta.** Bu, bulgunun en güçlü karşı argümanıdır ve
   büyüklüğü hesaplanmadı. Tipik girdap geri kazanımı payı η'yi 0,65'ten belki 0,70'e
   taşır — **0,80'e değil.**
2. **Aile tek parametreli.** Veter askıdan sabit, yalnız burulma kayıyor. Tam optimize
   edilmiş bir uzlaşma paleti daha iyisini verebilir. Ne kadar, hesaplanmadı.
3. **Kesit NACA 0012, veri NeuralFoil.** Pala sayısı, kesit ve veter dağılımı **seçildi,
   ölçülmedi** — çünkü makalede yok.
4. **Sıkıştırılabilirlik yok.** Geçiş noktalarında uç Mach ≤ 0,48; sorun değil.
5. **İkiye bölme 7 tur**, bu yüzden FM tam 0,599 değil 0,591–0,603 aralığına oturuyor.

## 6. Bu hesabın kendi hatası — ve onu ne yakaladı

İlk sürüm çifti, her biri **tam A alanına** sahip iki ayrık disk olarak modelledi ve
makalenin **tek diskli** ideal gücüne karşı okudu. Sonuç **FM = 1,083** oldu.

**Figure of merit birden büyük olamaz.** Sayının imkânsız olması, onu yakalayan şey oldu.
Çifte fiziksel olarak sahip olmadığı iki kat eyleyici disk alanı verilmişti. Düzeltildi:
tek disk, 2B palet, tam itki — makalenin kendi DL = T/A boyutlandırmasıyla aynı anlaşma.

## 7. Makaleye ne girecek

- *"runs at its design condition throughout"* ve *"at its design point"* **girmiyor.**
  Hesaptan bağımsız olarak: mimari iddia **yönelimdir**, verim değil.
- Seyir pervane verimi **0,80 değil, hesaplanmış aralık** olarak raporlanacak; zincir ve
  ondan türeyen her menzil yeniden çözülecek.
- Askı FM 0,599 **duruyor** — hesap onu destekliyor, hatta üstünde pay var.
- §5'teki beş sınır, uç çiftleri için yazılan sınır paragrafıyla aynı dürüstlükle yazılacak.

**Menzil düşüşü tezi tehdit etmiyor** (`CLAUDE.md` §0.7): menzil iddiası yalnız çok
rotorluya karşıdır ve 1262 km ile 1598 km arasındaki fark o eksende hiçbir şey değiştirmez.
Değişen şey, makalenin bir sayıyı hak edip etmediğidir.
