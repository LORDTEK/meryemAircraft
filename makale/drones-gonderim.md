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

`makale/uretim/mkdocx.py` `makale-v6.md`'den okuyup MDPI düzeninde `.docx`
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
| **Abstract** | `00-on-bilgi.md` → Abstract bloğu. **199 kelime**, derginin "about 200" sınırının altında |
| **Keywords** | vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle; series hybrid propulsion; cruise efficiency; aircraft configuration design |
| **Highlights** | `00-on-bilgi.md` → Highlights bloğu. İki başlık, her birinde iki madde — derginin istediği biçim |
| **Corresponding author** | Meryem Gülmen, meryemgulmen@outlook.com |
| **Affiliation** | Independent Researcher, Türkiye |
| **Article type** | Article (Communication değil — 31 500 kelime) |

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
> an accounting framework in three coupled currencies. Its central result is
> methodological: architectural rankings are properties of the sizing contract
> under which a comparison is made, not of the architectures compared. We report
> three contracts and the ranking changes between them.
>
> An uncrewed tail-sitting blended-wing body is developed as the case that
> instantiates the framework's escape condition, sized at two scales, and carried
> far enough to report what instantiating it costs — including two charges the
> configuration was initially assumed to avoid and which computation showed it
> does not.
>
> We state plainly that the aircraft is not shown to be flyable. It contains no
> wind-tunnel measurement and no flight test, its mass budget closes only on a
> battery specific power above any measured on a flown pack, and the transition
> pitching moment is identified as blocked on measurement rather than on effort.
> The framework does not depend on that outcome, and no claim of general
> architectural superiority is made.
>
> The computational record — mesh generator, case setups, grid-convergence study,
> and the scripts behind every figure — is openly available, and an archived
> version of this manuscript with its supplementary material is deposited at
> Zenodo (DOI: 10.5281/zenodo.22144194).
>
> The authors have filed a patent application covering the configuration
> (Türkpatent 2026/014570); this is declared in the manuscript.
>
> Yours sincerely,
> Meryem Gülmen, on behalf of the authors

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

1. **`dogrula.py` çalıştır.** 40 kontrol + bayat sayı denetimi. Şu an 0 sapma.
2. **PDF'i aç ve göz gezdir** — özellikle Şekil 2 ve Şekil 9 gibi geniş
   grafiklerin sayfaya sığdığını, tabloların taşmadığını.
3. **Özetin kelime sayısı** — 199. Kaynağa dokunulursa yeniden say.

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
