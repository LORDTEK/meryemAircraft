# Bacchini karşılaştırması — v8 için taslak metin

**Durum: TASLAK. Hiçbir yere işlenmedi.** v7 dondurulmuş; v8 bölüm bölüm
kurulacak ve içeriği yazar belirleyecek. Bu dosya, Fatura 2 bölümüne hazır
girecek metni ve ardındaki aritmetiği tutar.

Kaynak: `bacchini-reading-record.md` — tezden birinci elden okundu.

---

## 1. Önce karar: neyi karşılaştırıyoruz, neyi karşılaştırmıyoruz

### Karşılaştırılamayacak olan: mutlak katsayılar

| | Bacchini | Biz |
|---|---:|---:|
| Disk alanı | 0,203 m² (4 × APC 10×4,5) | 0,251 m² (8 disk) |
| Kanat alanı | 0,314 m² | 1,979 m² |
| **Disk / kanat** | **%64,5** | **%12,7** |

**Beş kat farklı.** Onların ΔC_D'si ile bizimkini yan yana koymak anlamsız
olurdu. Sayıların birbirine yakın çıkması bir tesadüf olurdu, doğrulama değil.

### Karşılaştırılabilecek olan: cezanın temiz gövdeye oranı

Bu, makalemizin **zaten kullandığı** çerçevedir — §3.3 serbest dönme yükünü
"varsayılan temiz gövde sürüklemesinin yüzde altmış ikisi" diye veriyor.

| | Ceza | Temiz gövde C_D0 | **Oran** |
|---|---:|---:|---:|
| **Biz** — sekiz serbest dönen disk, *hesaplanmış* | 0,0154 | 0,0248 | **%62** |
| **Bacchini** — standart quadplane donanımı, *ölçülmüş* | 0,0150 | 0,0230 | **%65** |

Bacchini'nin sayıları: C_L = 0,4'te quadplane C_D = 0,044, çekilmiş 0,029;
indüklenen pay k·C_L² = 0,0060 (Tablo 37, k = 0,0378) ikisinden de düşüldü.
Geri çekilmiş yapılandırma temiz uçakla aynı ölçülüyor (ikisi de 0,029), yani
0,0230 gerçek bir temiz gövde değeridir.

**%62'ye karşı %65.** Biri hesap, öteki ölçüm; iki ayrı mimari, iki ayrı ölçek,
iki ayrı Reynolds sayısı. **Uyuşan şey tek bir katsayı değil, mimari cezanın
büyüklük mertebesidir** — ve metin bunu böyle söylemeli, daha fazlasını değil.

---

## 2. Taslak metin — Fatura 2 bölümüne

> **An independent wind-tunnel measurement of the same bill.** Bacchini tested
> four models of a small uncrewed aircraft in the University of Sydney 7 ft by
> 5 ft tunnel at a chord Reynolds number of 280 000: a clean airframe, a
> standard quadplane conversion carrying four lift propellers on booms, and a
> third airframe able to retract those propellers into the fuselage [K1]. At the
> cruise lift coefficient of 0.4 the standard quadplane measured a drag
> coefficient of 0.044 against 0.029 with the propellers retracted, the retracted
> configuration being indistinguishable from the clean airframe. Removing the
> induced term common to both leaves a zero-lift penalty of 0.0150 on a clean
> airframe of 0.0230 — **65 percent** — against the **62 percent** this section
> computes for the free-wheeling tip rotors of the present configuration. The
> two aircraft share neither scale nor layout nor disc-to-wing area ratio, which
> differs by a factor of five, so the agreement is one of magnitude and not of
> coefficient. It is nonetheless the only external measurement of this bill
> available, and it places the present calculation in the range that a tunnel has
> actually recorded.

> **The same measurement qualifies a recommendation drawn from it.** Bacchini's
> quadplane was tested with its propellers locked perpendicular to the flow and
> locked parallel to it, reaching maximum lift-to-drag ratios of about 9 and 13
> respectively against about 17 with the motors removed, and concludes from the
> difference that takeoff propellers "must be free to rotate and to align to the
> airflow" [K1]. The measurement supports the comparison it makes; the
> recommendation extends it to a state that was not tested. A propeller free to
> rotate does not align — it turns. At zero shaft torque the present
> configuration's tip propellers settle at 25 000 rpm and sweep their discs, and
> the charge computed above, 0.0154, is twenty times the 0.0008 of the same blade
> held edge-on. **Freedom and alignment are different states, and the first does
> not produce the second.** Holding a blade aligned requires a mechanism to hold
> it, which is mass and a failure mode — the transfer of Bill 2 into Bill 1 that
> Section 2 describes, arriving once more.

> **What that transfer costs has also been measured.** The retraction mechanism
> of Bacchini's model weighed 200 g of a 2 456 g aircraft, eight percent of
> take-off mass. Applied to a published passenger design at a 30 percent drag
> reduction and a retraction system of five percent of vehicle mass — with that
> mass taken from the battery, since the battery is the one component that can be
> changed without disturbing the rest — maximum range rose from 119 km to 121 km,
> **an increase of under two percent**, while the speed for maximum range rose by
> 5 m s⁻¹ [K1]. The drag bill was genuinely reduced and genuinely paid for, and
> the range column barely moved. That is the transfer this paper's framework
> predicts, measured and priced by someone else.

---

## 3. Yazarın kuralına uygunluk denetimi

- ✅ *"Bir önceki sürümde şöyleydi"* yok. Metin tek başına duruyor.
- ✅ Her sayı tezin kendi sayfasından. İndüklenen payın düşülmesi bizim
  aritmetiğimiz ve öyle işaretli.
- ✅ Mimari önde: üç paragraf da bir faturaya ya da bir fatura dönüşümüne
  bağlanıyor, hesap kendi başına anlatılmıyor.
- ✅ İstenmeyen veri saklanmamış: %62'nin %65'ten *düşük* olduğu, ölçeklerin
  uyuşmadığı, uyuşmanın mertebe düzeyinde olduğu açıkça yazılı.

## 4. Yazılmadan önce kapanacak iki madde

1. **Yazar künyesi.** Tez *"Bacchini, Cestino, Verstraete, Van Magill"* diyor;
   elimizdeki not *"Bacchini, Cestino, Magill, Verstraete"*. AIAA bütün yazarları
   tam ve doğru ister. **Yayımlanmış künye teyit edilmeden atıf yazılmaz.**
2. **Hangi kaynağa atıf.** Ölçümleri tezden okuduk; dergi makalesi aynı işin
   hakemli sürümü. AIAA *"cite the original source"* diyor ve dergi sürümünü
   tercih ediyor. **Önerim: ikisini de anmak** — ölçüm için tez (okuduğumuz),
   hakemli sürüm için makale. Tez `iris.polito.it`'te açık erişim, yani AIAA'nın
   *"readily accessible published material"* şartını karşılıyor.

## 5. Ölçekleme gerilimi — denetlendi, çelişki YOK

Tez §5.4.3: askı başarımını korumak için disk alanı geometrik büyütmeden hızlı
büyümek zorunda, dolayısıyla geri çekmenin kazancı tam ölçekte **daha büyük.**

Makalemizin §3.9'u serbest dönme yükünü 50 kg'da 0,0154'ten 1000 kg'da 0,0051'e
**düşürüyor** — ilk bakışta ters yön. **Ama çelişki yok, çünkü §3.9 bu itirazı
zaten yanıtlıyor:**

> *"The disc-to-wing area ratio is constant to three digits, and contributes
> nothing… The bill falls because the reference dynamic pressure rises and the
> blade thins, not because the wing outgrows the disc."*

Diskler 50 kg'da 0,251/1,98 ve 1000 kg'da 2,82/22,24 — **ikisi de 0,127.** Yük
düşüyor çünkü kanat katılığı 0,075'ten 0,044'e iniyor ve seyir dinamik basıncı
1,78 kat artıyor. İki çalışma **farklı şeyleri sabit tutuyor**: Bacchini askı
süresini, biz disk yüklemesini. Aynı fizik, farklı kısıt.

**Sonuç: gövdede bir cümleyle geçilir, bölüm açmayı gerektirmez.**
