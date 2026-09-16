# Sürümler — hangi dosya nerede yayımlandı

Bu dosya bir tuzağı kapatmak için var. Depoda `paper-v5.md`, `paper-v6.md`
ve `paper-v7.md` yan yana duruyor; bir okuyucu haklı olarak "v6 dosyası
Zenodo'daki v6'dır" diye varsayar. Bir süre **öyle değildi**: v6 yatırıldıktan
sonra `paper-v6.md` üzerinde çalışmaya devam edildi, yani depodaki v6 ile
yayımlanmış v6 sessizce ayrıştı. Bu depoda "aynı ad, iki içerik" hatası daha
önce de dışarıya sızmıştı.

**Kural: yayımlanmış bir sürümün dosyası bir daha değiştirilmez.** Düzeltme
yeni bir sürüm numarası alır.

| Sürüm | Depodaki dosya | Yayımlandığı commit | Durum |
|---|---|---|---|
| v5 | `paper-v5.md`, `paper-v5-supp.md` | — | Zenodo'da yayımlandı |
| v6 | `paper-v6.md`, `paper-v6-supp.md` | `f208eca` | Zenodo'da yayımlandı; **dosya o hale geri alındı** |
| v7 | `paper-v7.md`, `paper-v7-supp.md` | `8138b62` | Zenodo'da yayımlandı — DOI `10.5281/zenodo.22745666`, sha `c5b0cd898d20` |

**v7, *Drones*'a gönderilen sürümdür.** Manuscript ID **drones-4595522**,
gönderim 2026-09-14 15:06:04. **2026-09-15'te masadan reddedildi** — *Drones*
kapsam dışı bulup *Aerospace*'e aktardı (`aerospace-4595522`), *Aerospace* aynı
gün reddetti. Hakeme gitmedi; ayrıntı ve öğrenilenler `drones-submission.md` §10.

Ret, v7'yi değiştirmek için gerekçe **değildir**: v7 Zenodo'da yayımlandı ve
orada sabittir. Bu depoda "aynı ad, iki içerik" bedeli iki kez ödendi. Ne
yapılacaksa **v8** olarak yapılır; düzeltmeler `revision-list.md`'de
birikmeye devam eder.

## Yayımlanmış sürümlerdeki yol adları — 2026-09-16 öncesi

**2026-09-16'da depodaki bütün dizin ve dosya adları İngilizceye çevrildi.**
Yayımlanmış sürüm dosyalarının *içeriğine dokunulmadı* — v5, v6 ve v7 bayt bayt
aynıdır, yalnızca dosya adları değişti. Bunun bilinen ve kabul edilen sonucu şudur:
**v5–v7 metinlerinin gövdesinde geçen betik yolları artık depoda o adla yoktur.**

Doğru davranış budur: yayımlanmış bir sürüm dondurulmuş bir belgedir ve kendi
commit'indeki depoya işaret eder. Bu yüzden okuyucuya verilen bağlar commit'e
sabitlenir. v7'yi okuyan biri için çeviri çizelgesi:

| v5–v7 metninde geçen | Bugünkü karşılığı |
|---|---|
| `aero/itki.py` | `aero/thrust.py` |
| `aero/kapanma.py` | `aero/closure.py` |
| `aero/gecis_dinamik.py` | `aero/transition_dynamics.py` |
| `aero/kutle.py` | `aero/mass.py` |
| `aero/temel.py` | `aero/baseline.py` |
| `aero/uc_pervane.py` | `aero/tip_propeller.py` |
| `makale/uretim/dogrula.py` | `paper/build/verify.py` |
| `makale/uretim/baglanti.py` | `paper/build/links.py` |

Tam eşleme, adları çeviren commit'in kendisindedir; o commit'ten önceki her yol
eski adıyla, sonraki her yol yeni adıyla çözülür.

Sürüm numarası `paper/build/version.py` içindedir ve **tek yerdedir**. Önce
öyle değildi: `mkdocx.py`, `mksupppdf.py` ve `links.py` kendi kopyalarını
tutuyordu, ve `links.py` sabit `"v6"` okuduğu için sürüm v7'ye çıktığında
**bayat dosyayı denetleyip "temiz" diyordu.** Geçtiğini sandığın bir denetim,
hiç olmayandan beterdir; bu depoda ikinci kez oldu.


## Sürüm DOI'si makaleye konmaz

Bir sürümün DOI'si, o sürüm yatırıldıktan **sonra** doğar. Makale kendi sürüm
DOI'sini içeremez; içermeye kalkarsa yatırılan dosya ile yereldeki dosya
ayrışır — yani yukarıdaki kural ihlal edilir. Bir kez denendi ve geri alındı.

**Makale yalnızca concept DOI taşır** (`10.5281/zenodo.22144194`), ki zaten
tam olarak bunun için vardır: her zaman en son sürüme çözülür.

**Sürüm DOI'si kapak mektubuna ait**, arşivlenen belgeye değil. Kapak mektubu
arşivlenmez, sonradan yazılır ve ikisini birden verebilir.
