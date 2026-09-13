# Drones gönderim kontrol listesi

Bu dosya senin için. Ben dergi sistemine giremiyorum; aşağısı elle yapılacak
işin tamamı, **yapılması gereken sırayla**. Her maddenin yanında durumu var:
**HAZIR** (bende bitti, kopyala–yapıştır), **SENDEN** (senin bilgin ya da kararın
gerekiyor), **KARAR** (iki seçenek var, seçmen gerek).

---

## 0. Gönderimi durduran iki madde — önce bunlar

### 0.1 Yazar katkıları onayı — **SENDEN, zorunlu**

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

**Yapılacak:** üç yazar da okusun, doğruysa onayla, değilse düzelt. Düzeltince bana
söyle, kaynağa işleyip yeniden kurayım. CRediT sözlüğü dışında terim
kullanılamaz.

### 0.2 Zenodo DOI'si makalede yok — **SENDEN**

Data Availability şu an yalnız GitHub'a işaret ediyor. Zenodo'ya yükledin, ve
dergi kalıcı tanımlayıcı istiyor.

**Bana ver:** v6 sürümünün **concept DOI**'si (bütün sürümlere işaret eden, sabit
olan). Zenodo kayıt sayfasında "Cite all versions" altında görünür,
`10.5281/zenodo.XXXXXXX` biçiminde.

Verince Data Availability'ye şu biçimde ekleyeceğim:

> …are openly available at https://github.com/LORDTEK/meryemAircraft and are
> archived at https://doi.org/10.5281/zenodo.XXXXXXX

---

## 1. Gönderim biçimi — **KARAR**

Drones **Free Format Submission** kabul ediyor: ilk gönderimde MDPI şablonuna
dökmek zorunlu değil, kendi düzenimizde PDF gönderilebilir. Ama IMRaD yapısı,
Highlights, özet sınırı ve beyan blokları **Free Format'ta da zorunlu** —
hepsi bizde var.

| seçenek | ne demek |
|---|---|
| **A — Free Format** (önerim) | Elimizdeki PDF'i olduğu gibi gönder. Kabul sonrası şablona dökülür. |
| B — MDPI şablonu | Word/LaTeX şablonuna şimdi dök. Birkaç saatlik biçim işi, bilimsel katkısı yok. |

**Önerim A.** Sebep: makale 70 sayfa ve 172 tablo taşıyor; şablona dökmek biçim
hatası üretme riski taşıyor ve reddi etkilemiyor. Hakem bilimi okur.

---

## 2. Yüklenecek dosyalar — **HAZIR**

| dosya | nereden | ne olarak |
|---|---|---|
| `meryemAircraft-makale.pdf` | `makale/pdf/` | **Manuscript** (ana belge, 70 sayfa) |
| `meryemAircraft-ek.pdf` | `makale/pdf/` | **Supplementary File** (60 sayfa, S1–S6) |
| `sekil01`…`sekil12` | `gorsel/cikti/` | **Figures**, ayrı ayrı, yüksek çözünürlüklü |

Şekiller denetlendi: on üçünün hepsi ≥1500 piksel genişlikte, dokuz tanesi
300 dpi gömülü. MDPI'ın alt sınırı 1000 piksel ya da 300 dpi — hepsi geçiyor.
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
> Zenodo (DOI: …).
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
