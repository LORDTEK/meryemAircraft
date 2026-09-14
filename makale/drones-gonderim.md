# Drones gönderim kontrol listesi

Bu dosya senin için. Ben dergi sistemine giremiyorum; aşağısı elle yapılacak
işin tamamı, **yapılması gereken sırayla**. Her maddenin yanında durumu var:
**HAZIR** (bende bitti, kopyala–yapıştır), **SENDEN** (senin bilgin ya da kararın
gerekiyor), **KARAR** (iki seçenek var, seçmen gerek).

---

## 0. Durum — iki madde kapandı

**Yazar katkıları onaylandı** (senin "iş paylaşımı o şekilde" onayınla), taslak
işareti kaldırıldı. **Zenodo kök DOI'si eklendi:** Data Availability artık
`https://doi.org/10.5281/zenodo.22144194` taşıyor — bütün sürümlere işaret eden,
sabit olan.

**Gönderimi durduran madde kalmadı.**

---

## 0b. Kapanan maddenin kaydı

### Yazar katkıları — **ONAYLANDI**

`00-on-bilgi.md` içindeki Author Contributions bloğu hâlâ **⚠️ TASLAK** işaretli.
Ben yazdım, varsayımla: sorumlu yazar Meryem, denetleyen Ömer, yazılım Berke.

**Bu blok MDPI'da koşulsuz zorunlu ve uydurma bir katkı beyanı yayın etiği
ihlalidir.** Kimin ne yaptığını ben bilemem.

Şu an yazan:

> Conceptualization, Ö.G. and M.G.; Methodology, Ö.G. and M.G.; Software, B.G.;
> Formal Analysis, M.G. and B.G.; Investigation, M.G., B.G. and Ö.G.; Data
> Curation, B.G.; Writing — Original Draft, M.G.; Writing — Review & Editing,
> M.G., B.G. and Ö.G.; Visualization, B.G.; Supervision, Ö.G.; Project
> Administration, M.G.

Onaylandı ve taslak işareti kaldırıldı. Sonradan değiştirmek istersen söyle.

### Zenodo DOI — **EKLENDİ**

Data Availability artık şunu taşıyor:

> …are openly available at https://github.com/LORDTEK/meryemAircraft, and an
> archived version of this manuscript with its supplementary material is
> deposited at https://doi.org/10.5281/zenodo.22144194 (concept DOI, resolving
> to the latest version).

---

## 1. Gönderim biçimi — **MDPI ŞABLONU, ÜRETİLDİ**

Kararın MDPI şablonu yönünde. Şablona **elle dökmedim, ürettim** — 70 sayfa,
172 tablo satırı ve 12 şekil elle taşınacak iş değil, ve bu depoda bir sürüm
elle toparlandığı için yanlış tablo taşımıştı.

`makale/uretim/mkdocx.py` `makale-v8.md`'den okuyup MDPI düzeninde `.docx`
üretiyor: başlık, üstsimgeli yazar/kurum satırları, `Abstract:`, `Keywords:`,
numaralı bölümler, `Figure N.` altyazıları, tablolar, **derginin kendi
sırasındaki** arka madde blokları, ve numaralı kaynakça.

**Kayma denetimi — üretilen belge kaynağa karşı:**

| | kaynak | .docx |
|---|---:|---:|
| kelime | 31 200 | **31 198** |
| şekil | 12 | **12** |
| kaynak girdisi | 51 | **51**, 1–51 tam |
| beyan bloğu | 8 | **8**, MDPI sırasında |
| ham markdown kalıntısı (`**`, `<sup>`, `>`) | — | **0** |
| Türkçe çalışma notu | — | **0** |

Üretirken beş kusur çıktı ve hepsi düzeltildi: üstsimgeler ham `<sup>` olarak
kalıyordu; alıntı işaretleri paragraf ortasında duruyordu; beyanlar gövdeden
önce geliyordu (MDPI kaynakçadan önce, ama gövdeden sonra ister); beyan alt
başlıkları hiç basılmıyordu; ve kaynakçanın üç girdisi italikle başladığı için
bir öncekine yapışmıştı.

**Grok ve ChatGPT'ye soracağın şey:** kaymanın gözle görülür bir yerde kalıp
kalmadığı. Yukarıdaki tablo makine denetimi; şablona özgü biçim kaymalarını
(tablo taşması, şekil yerleşimi, sayfa kırılması) onlar daha iyi görür.

## 2. Yüklenecek dosyalar — **HAZIR**

| dosya | nereden | ne olarak |
|---|---|---|
| `meryemAircraft-MDPI.docx` | `makale/pdf/` | **Manuscript** — MDPI düzeninde, gönderilecek olan |
| `meryemAircraft-MDPI-ek.docx` | `makale/pdf/` | **Supplementary File** — aynı düzende |
| `meryemAircraft-makale.pdf` | `makale/pdf/` | yedek; sistem PDF isterse |
| `meryemAircraft-ek.pdf` | `makale/pdf/` | yedek |
| `sekil01`…`sekil12` | `gorsel/cikti/` | **Figures**, ayrı ayrı, yüksek çözünürlüklü |

> **Sürüm:** gönderilecek metin **v8**'dir. Zenodo'da v6 yayımlandı ve
> Zenodo'ya yatırılan **v7**'dir (DOI **10.5281/zenodo.22745666**,
> concept DOI **10.5281/zenodo.22144194**); v8 ondan **tek satır** farklıdır —
> gönderimi yapan yazarın da corresponding author olması. `makale/SURUMLER.md`
> hangi dosyanın nerede yayımlandığını ve v8'in neden ayrı bir sürüm olduğunu
> tutuyor. v8 Zenodo'ya yüklenmiyor.

Şekiller yeniden numaralandı (ilk atıf sırasına göre) ve dosya adları da
döndü; numara ile ad artık tutuyor. On üç dosyanın hepsi, `.docx` içinde
yerleştirildikleri genişlikte **387 dpi'ın üstünde**; en düşüğü Şekil 6, en
yükseği Şekil 5 (694 dpi). Üç boyutlu görünüşler bunun için yeniden
üretildi — önceki sürümde Şekil 6 yalnızca 258 dpi veriyordu ve MDPI'ın
300 dpi alt sınırının altındaydı. Dokuzunun ayrıca vektör (`.svg`) sürümü
var; MDPI çizgi grafiklerinde vektörü tercih ediyor, o dokuzu `.svg` olarak
yükle.
**Ayrı dosya olarak da yükle**, PDF'in içinde gömülü olması yetmiyor.

---

## 3. Sistemin isteyeceği alanlar — **HAZIR, kopyala–yapıştır**

| alan | değer |
|---|---|
| **Title** | The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System |
| **Abstract** | `00-on-bilgi.md` → Abstract bloğu. **214 kelime**. Dergi "about 200 words maximum" diyor; 214 "about 200" içinde sayılır ama teknik ön denetim itiraz ederse kısaltılacak yer, tilt paragrafının ikinci yarısıdır |
| **Keywords** | vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle; series hybrid propulsion; cruise efficiency; aircraft configuration design |
| **Highlights** | `00-on-bilgi.md` → Highlights bloğu. İki başlık, her birinde iki madde — derginin istediği biçim |
| **Corresponding author** | **İki kişi:** Meryem Gülmen (meryemgulmen@outlook.com) ve Ömer Gülmen (lordtek@me.com). Sistemde ikisini de corresponding olarak işaretle |
| **Submitting author** | Ömer Gülmen. MDPI'da submitting ≠ corresponding; gönderimi oluşturan hesap sistemde yönetir, ama **yazışma corresponding author'a gider** — bu yüzden Ö.G. de corresponding yapıldı |
| **Affiliation** | Independent Researcher, Türkiye |
| **Article type** | Article. **Ana metin 36 200 kelime, ek belge 33 100 kelime** — bu uzun bir makale ve aşağıda 7. maddede ayrı ele alınıyor |

**ORCID:** dergi zorunlu tutmuyor ama istiyor. Üç yazarın da varsa gir; yoksa
orcid.org'dan beş dakikada alınır ve ileride işine yarar.

---

## 4. Beyan blokları — **HAZIR**, PDF'in içinde

Sekizi de basılıyor ve doğrulandı. Sistem ayrıca ayrı alanlarda da isteyebilir;
o zaman PDF'ten kopyala:

Supplementary Materials · Author Contributions · Funding · Data Availability ·
Acknowledgements · Conflicts of Interest · Dual-Use Research of Concern · Patents

**Dikkat — Conflicts of Interest'te patent beyanı var:**

> The authors have filed a patent application covering the aircraft configuration
> described in this paper (Türkpatent application 2026/014570).

Bu doğru ve beyan edilmesi zorunlu. Dergi bunu reddetmez; **beyan etmemek**
reddettirir.

---

## 5. Kapak mektubu — **HAZIR**, aşağıda taslak

Drones kapak mektubu istiyor. Kısa tutmak doğru. Taslak:

> Dear Editors,
>
> We submit "The Architectural Cost of Hybrid VTOL" for consideration as an
> Article in *Drones*.
>
> The paper treats the cruise-efficiency penalty of hybrid VTOL aircraft as an
> architectural property rather than an implementation defect, and develops it as
> an accounting framework in three coupled currencies: hover hardware carried
> through cruise, its drag when exposed, and continuous power sized by a condition
> holding some two percent of the flight. Every architectural remedy we survey
> reduces one by raising another.
>
> **The configuration we propose addresses a specific gap.** Tilting architectures
> satisfy the framework's escape condition — one propulsion group serving both
> regimes — by rotating their propulsors, and pay a pivot, its actuators, a
> gyroscopic moment during the rotation and a transition control problem for it.
> Those are mechanical and control costs rather than aerodynamic ones. We propose
> an alternative route to the same condition: an uncrewed tail-sitting blended-wing
> body in which **the airframe rotates and the propulsors do not**. There is no
> pivot, no nacelle actuator, no variable-pitch hub and no retraction mechanism;
> pitch and yaw are produced by differential thrust between fixed-pitch propellers,
> and roll — which coaxial torque-balanced pairs cannot produce at any setting — by
> a single variable-extension strip. **What we claim to eliminate is a mechanism
> class, not every moving part, and the paper is explicit about the distinction.**
>
> A second result is methodological and independent of the configuration:
> architectural rankings are properties of the sizing contract under which a
> comparison is made, not of the architectures compared. We report three contracts
> and the ranking changes between them. **We therefore do not claim a range
> advantage over the other hybrid families; we report that the tilting layout leads
> on range under all three contracts, and that result stands in the paper.**
>
> The case is sized at two scales and carried far enough to report what
> instantiating the escape condition costs — including two charges the
> configuration was initially assumed to avoid and which computation showed it does
> not, one of which reverses a range comparison against our own case.
>
> We state plainly that the aircraft is not shown to be flyable. There is no
> wind-tunnel measurement and no flight test; the mass budget closes only on a
> battery specific power about 3.8 times the highest yet measured on a flown pack;
> the transition pitching moment is blocked on measurement rather than on effort;
> the roll strip's actuation is unsized; and the landing transition is unmodelled.
> The framework does not depend on that outcome, and the architectural claims above
> are claims about hardware topology rather than about demonstrated performance.
>
> The computational record — mesh generator, case setups, grid-convergence study,
> and the scripts behind every figure — is openly available, and an archived
> version of this manuscript with its supplementary material is deposited at
> Zenodo: this version is DOI 10.5281/zenodo.22745666, and DOI
> 10.5281/zenodo.22144194 is the concept identifier that resolves to the latest
> version.
>
> The authors have filed a patent application covering the configuration
> (Türkpatent 2026/014570); this is declared in the manuscript.
>
> Yours sincerely,
> Ömer Gülmen, on behalf of the authors
> (corresponding authors: Meryem Gülmen, meryemgulmen@outlook.com; Ömer Gülmen,
> lordtek@me.com)

**Yapma:** "kırk iç tutarlılık kontrolü, sıfır sapma" gibi bir cümle koyma. Bir
dış okuma bunu açıkça uyardı ve haklı — hakemi denetlemeye davet eder.

---

## 6. Önerilen hakemler — **SENDEN, KARAR**

MDPI genellikle 3–5 isim istiyor (zorunlu değil). Aday alanlar, makalenin kendi
kaynakçasından, çıkar çatışması olmayanlar:

- Blended-wing-body İHA aerodinamiği — Panagiotou / Yakinthos grubu (kaynak 39),
  Wang & Zhou (44), Lampropoulos ve diğ. (41)
- Kuyruk-üstü geçiş kontrolü — Li ve diğ. (28), Lyu ve diğ. (29), Zhong ve diğ. (42)
- eVTOL boyutlandırma ve karşılaştırma — Bacchini & Cestino (21), Ugwueze ve diğ. (26)

**Karar senin.** Aynı kurumdan, ortak yayından veya kişisel bağlantıdan kimseyi
önerme — dergi denetliyor.

**Hariç tutulacak hakem** alanı da var; kullanmak için bir sebebin varsa kullan.

---

## 7. Göndermeden önce son üç kontrol — **HAZIR**

1. **`dogrula.py` ve `baglanti.py` çalıştır.** 43 sayısal kontrol + 9 yasaklı bayat değer + bağ dokusu (işaretçiler doğru yere çözülüyor mu, tablo/şekil atıfları tutuyor mu). Şu an 0 sapma.
2. **PDF'i aç ve göz gezdir** — özellikle Şekil 2 ve Şekil 9 gibi geniş
   grafiklerin sayfaya sığdığını, tabloların taşmadığını.
3. **Özetin kelime sayısı** — 214. `mksurum.py` 215'i aşarsa kurulumu durduruyor, yani sessizce büyüyemez.

### Ve dördüncü bir şey, kontrol değil **karar**: makale uzun

Ana metin **36 200 kelime**, ek belge **33 100**. *Drones* katı bir sınır koymuyor
ama bu, tipik bir dergi makalesinin üç katı. İki sonuç doğurabilir:

- **Editör masadan çevirebilir** ("please condense"), ki bu hakemliğe hiç
  gitmeden gelir.
- **Ya da uzunluğu haklı bulabilir**, çünkü makale bir çerçeve *ve* onu
  somutlaştıran bir vaka çalışması taşıyor ve ikisini ayırmak ikisini de
  zayıflatır.

**Benim görüşüm: olduğu gibi gönder.** Kısaltmak için tek gerçek yer, düzeltme
izlerinin ("bir önceki sürüm şunu diyordu") gövdeden eke taşınmasıdır — yaklaşık
2 000 kelime — ama o izler bu makalenin en güçlü tarafı ve bir dış okuma onları
açıkça övdü. Editör isterse kısaltırız; kendiliğinden feda etmeyelim.

**Hazır olması gereken cevap:** *"The paper carries a framework and the case that
instantiates it. The case is what makes the framework falsifiable — it is where
the framework's own prediction is tested against a configuration and twice found
against it. Separating them would leave a framework with no test and a
configuration with no reason."*

---

## 8. Gönderim sonrası — bilmen gerekenler

**Süre.** Drones ortalama ilk karar ~16 gün, kabulden yayına ~3 gün. Hızlı bir
dergi; hazırlıklı ol.

**Ücret.** Açık erişim, APC var. 2026 için Drones'un APC'si yaklaşık 2 600 CHF.
İndirim olasılıkları: ilk kez yayımlayan yazarlar, davetli özel sayı, ya da
kurumsal anlaşma. **Gönderimden önce sistemin APC sayfasına bak** — kabul
sonrası sürpriz olmasın.

**Zenodo ile çakışma yok.** Zenodo kaydı ön baskı değil, çalışma kaydı; MDPI
ön baskıyı da kabul ediyor. Kapak mektubunda anmak doğru, gizlemek yanlış.

**Hakem geldiğinde bana getir.** Dört dış okumayla kurduğumuz düzenin aynısını
hakem raporuna uygularım: her iddiayı dosyaya karşı doğrular, hangisinin haklı
hangisinin olmadığını ayırırım.
