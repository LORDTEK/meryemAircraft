# Journal of Aircraft (AIAA) — şart şart uyum listesi

**Kaynak:** AIAA'nın kendi sayfalarından yazar tarafından alınan metin, 2026-09-16.
Birinci elden. `CLAUDE.md` §4'teki kural gereği yazıldı: *Drones*'a gönderirken
derginin kendi şartlarını hiç açmamıştım ve gönderim o yüzden masadan döndü.

**Not:** aşağıdakilerin hepsi yapıştırılan metinden. **Ücretler bu metinde
GEÇMİYOR** — sayfa/renkli şekil bedelleri hakkında elimde yalnız arama motoru
özeti var ve bu projede o kaynak sınıfına sayı bağlanmaz. Ayrı olarak teyit
edilecek (§6).

---

## 1. KAPSAM — geçiyoruz, ve iki sözcük doğrudan bizim lehimize

> "It publishes papers on general aviation, military and civilian aircraft,
> **UAV, STOL and V/STOL**, subsonic, supersonic, transonic, and hypersonic
> aircraft…"

**UAV ve V/STOL adıyla sayılıyor.** Ayrıca kapsamda olan ve bizde bulunan
alanlar: *multidisciplinary design optimization of aircraft*, *flight
mechanics*, *applied computational fluid dynamics*, *aircraft aerodynamics*,
*reliability, maintainability*.

### Ve olmayan şey — bizi *Drones*'ta düşüren madde burada YOK

*Drones* kapsam sayfasında **"en azından laboratuvar ölçeğinde insansız bir
platformdan deneysel veriyle doğrulama"** şartı yazılıydı. **JoA'da böyle bir
madde yok.** Bunun yerine şu var:

> **Numerical and Experimental Accuracy** — "authors should ensure the
> credibility and reproducibility of the numerical aspects of any simulation
> results being reported, and sufficient information should be available for
> readers to independently assess the statistical confidence of results."

Bu bir **deney şartı değil, titizlik ve yeniden üretilebilirlik şartıdır** — ve
bu, bu çalışmanın en güçlü tarafıdır: üç seviyeli ağ yakınsama çalışması, açık
depo, makalenin her başlık sayısını kendi denklemleriyle yeniden hesaplayan
denetim betiği. **Bu maddeyi karşılamak için elimizde olan, başka çoğu
makalede olandan fazla.**

---

## 2. MAKALE TÜRÜ — burada bir KARAR var ve yazara ait

İki tür bize uyuyor ve aralarındaki fark küçük değil.

| | **Full-Length Paper** | **Design Forum** *(yalnız JoA'da var)* |
|---|---|---|
| Tanım | "original, quantitative, detailed technical material, set into perspective relative to prior work" | "design case studies of **actual or notional** air vehicles… **new design methodologies**… emerging trends" |
| Uzunluk | 10 000 – 12 000 kelime | 10 000 – 12 000 kelime |
| Özet | 100–200 kelime | 100–200 kelime |
| **Hakemlik** | EiC eleme → Associate Editor → **iki veya daha çok hakem** | **"do not undergo routine peer review"** |
| Süre | haftalar–aylar | daha kısa |

**Design Forum'un tanımı bize fazlasıyla uyuyor** — *"notional air vehicles"*
ve *"new design methodologies"* ikisi birden bizim tarifimiz. Ve hakemliğe
girmediği için "rüzgâr tüneli nerede" sorusunun makaleyi öldürme ihtimali yok.

**Ama bedeli var ve yazar bunu bilerek seçmeli:** hakemli değil. Hedef *"Q1
hakemli yayın"* ise, Design Forum o hedefi karşılamayabilir — derginin
indekslenmesini taşır ama *peer-reviewed* etiketini taşımaz. Akademik
değerlendirmede ikisi aynı sayılmaz.

**Bu kararı ben vermem.** İki yol:
- **Full-Length Paper** — hakemli, prestijli, ve hakem "bunu ne doğruluyor"
  diye soracak. Cevabımız var (NASA seti, Bacchini, yayımlanmış tünel L/D'leri)
  ama garantisi yok.
- **Design Forum** — kapıdan girme ihtimali çok daha yüksek, hakem süzgeci yok,
  prestij daha düşük.

---

## 3. UZUNLUK — ve gözden kaçması kolay olan asıl kısıt

> "A typical double-spaced Full-Length Paper will be approximately
> **10 000–12 000 words (including equations and equivalent space required for
> figures and tables)**."

**Kritik:** kelime bütçesi **şekil ve tabloların kapladığı yeri de sayıyor.**
Elimizde **12 şekil ve 22 tablo** var. Bunlar bütçeden ciddi bir pay alır, yani
**metne kalan bütçe 10 000'in belirgin şekilde altındadır.**

| | şimdi | hedef |
|---|---|---|
| Gövde | **35 969 kelime** | 10 000 – 12 000 (şekil/tablo dahil) |
| Şekil | 12 | bütçeye göre azaltılacak |
| Tablo | 22 | bütçeye göre azaltılacak |
| Ek belge | 32 393 kelime | ek olarak kalabilir (§5) |

**Yaklaşık üçte bire ineceğiz, ve tablo/şekil sayısı da düşecek.** Dönüşüm
oranını bilmeden kaç tablo kalabileceğini söyleyemem — **AIAA'nın "Journal Page
Limits and Word Count Guidelines" belgesi lazım** (§6).

---

## 4. BAŞLIK ve ÖZET — ikisi de şu an şarta aykırı

### Başlık: en fazla 12 kelime, kısaltma yok

> "The manuscript title is concise (**maximum of 12 words**), in upper- and
> lower-case letters, **without the use of acronyms or abbreviations**."

Mevcut başlık **16 kelime** ve içinde **VTOL** kısaltması var. **İki ayrı
ihlal.** Ve "VTOL"ü açmak dört kelime eder (*vertical take-off and landing*),
yani yalnız açmak yetmez, başlık ayrıca kısalmak zorunda.

`meryemAircraft` kalacak — bu yazar kararı ve on iki kelimenin birini harcar,
sorun değil. Geri kalan on bir kelimeye katkının sığması gerekiyor. **Başlık
işi ertelenebilir bir iş olmaktan çıktı; bir şart hâline geldi.**

### Özet: en fazla 200 kelime, kısaltma yok, sayısal atıf yok

> "a summary-type abstract of **100 to 200 (maximum) words** in one paragraph,
> **without numerical references, acronyms, or abbreviations**."

Mevcut özet **214 kelime** ve **VTOL** geçiyor. Yeniden yazılacak.

---

## 5. EK BELGE — herkesin önerdiği strateji burada izinli, ama bir şartla

> "supplemental files… are intended only to support the primary content
> presented in the article, **which must be self-contained and stand on its
> own. Acceptance for publication will be based solely on the content of the
> article.**"

Yani "ayrıntıyı eke taşı" yapılabilir — **ama hakem yalnızca gövdeye bakar.**
Gövde tek başına yetmek zorunda.

**Bu, yazarın kendi kuralıyla birebir aynı şey:** *"Sunacağın şey bağımsız tek
başına yeter olmalı."* Derginin şartı ile yazarın talimatı çakışıyor.

---

## 6. KAYNAKÇA — bir maddesi bizi doğrudan ilgilendiriyor

AIAA biçimi: numaralı, köşeli parantez `[4]`, metinde geçiş sırasına göre,
kaynakça listesinde **"et al." kullanılmaz, bütün yazarlar yazılır**, dergi ve
yayınevi adları kısaltılmaz, mümkün olan her kaynağa **DOI bağı** konur.
Mevcut kaynakçamız MDPI biçiminde; **tümü dönüştürülecek.**

### Ve bir şart, Veri Erişilebilirliği'ni değiştiriyor

> "**websites where there is no commitment to archiving** may be mentioned
> parenthetically in the text or in a footnote but **should not be cited in the
> reference list**."

**GitHub'ın arşivleme taahhüdü yoktur. Zenodo'nun vardır.** Yani depoya çıplak
GitHub bağıyla atıf yapılamaz; **DOI ile atıf yapılır.** Bu, `revision-list.md`
içindeki "depo için ayrı Zenodo DOI'si üret" maddesini isteğe bağlı olmaktan
çıkarıp **zorunlu** hâle getiriyor.

Bir şart daha: **"Authors must reference the original source of a work, not a
secondary source."** — Bacchini 2021'i birinci elden okuma kararımız derginin
de şartı.

---

## 7. SONUÇ BÖLÜMÜ — şu an aykırı

> "Conclusions provide a detailed discussion of study findings. Do not
> introduce concepts not presented in text; **do not refer to other work.**"

Mevcut Sonuçlar bölümünde **bir kaynak atfı var.** Çıkarılacak.

---

## 8. ZENODO — risk kalktı, ama kabul sonrası için bir soru var

> "Prior to submitting to an AIAA journal or a conference, authors can: **Post
> draft manuscripts and research results anywhere, anytime, including pre-print
> servers.**"

**Zenodo yatırımlarımız sorun değil.** *Drones*'ta bunu beyan etmiştik; AIAA
açıkça izin veriyor. **Gönderimi durduran bir engel yok.**

**Açık kalan soru — kabul sonrası:** AIAA telif hakkını devralıyor, ve kabul
sonrası yazarın kurumsal deposuna koyması izinli ama *"limited to those to
which the author has a direct relationship."* **Zenodo genel bir depodur,
kurumsal değildir.** Gönderimden önce yayımlanmış sürümler izinli olduğuna göre
mevcut v1–v7 güvende görünüyor; **kabul sonrası ne olacağı belirsiz** ve
kabul gelirse AIAA'ya sorulacak. Şimdi karar gerektirmiyor.

---

## 9. USUL

- Gönderim: **ScholarOne** (`mc.manuscriptcentral.com/aiaa`).
- **Bütün yazarlara sistemden doğrulama e-postası gider; hepsi onaylamadan
  gönderim tamamlanmaz.** Meryem ve Berke'nin bu kez *gönderilen sürümü*
  okumuş olması gerekiyor — *Drones*'ta da aynı durum vardı.
- Biçim: **10 punto, çift satır aralığı, tek sütun, Amerikan İngilizcesi.**
- Denklemler resim olamaz; bölüme göre değil **sıralı** numaralanır.
- Semboller çoksa özet ile giriş arasına **Nomenclature** konur. *(Bizde sembol
  çok; bu muhtemelen gerekli.)*
- Fon kaynağı alanı: bizde fon yok, boş geçilecek.
- **Yazar yükümlülüğü:** "each author of a paper will review three papers
  submitted by others." Kabul edilirse bu bir taahhüt.

---

## 10. ŞU AN ELDE OLMAYAN — yazardan istenecek

1. **"Journal Page Limits and Word Count Guidelines"** (Eylül 2024) —
   `https://aiaa.org/wp-content/uploads/2024/12/journalpagelimitsandwordcountguidelines_Sept_2024.pdf`
   **En kritik eksik:** şekil ve tablonun kaç kelimeye denk sayıldığını burası
   söylüyor. Bunu bilmeden kaç tablo ve kaç şekil kalabileceğine karar
   veremem.
2. **Şekil ve tablo kılavuzu** —
   `https://aiaa.org/publications/journals/journal-author/guidelines-for-journal-figures-and-tables/`
3. **Ücretler** — sayfa bedeli ve renkli şekil bedeli. Yapıştırılan metinde
   geçmiyor. Elimdeki tek bilgi arama motoru özeti ve **bu projede o kaynağa
   sayı bağlanmaz.**

---

## 11. ÖZET — nerede duruyoruz

| Şart | Durum |
|---|---|
| Kapsam | ✅ **Geçiyor**, UAV ve V/STOL adıyla sayılı |
| Deneysel doğrulama şartı | ✅ **Yok** — bizi *Drones*'ta düşüren madde burada bulunmuyor |
| Sayısal titizlik / yeniden üretilebilirlik | ✅ **Güçlü tarafımız** |
| Zenodo'da önceden yayımlanmış olmak | ✅ **İzinli** |
| Uzunluk | ❌ 35 969 → 10 000–12 000, **şekil/tablo dahil** |
| Başlık | ❌ 16 kelime ve kısaltma var; sınır 12, kısaltma yasak |
| Özet | ❌ 214 kelime ve "VTOL" geçiyor; sınır 200, kısaltma yasak |
| Kaynakça biçimi | ❌ MDPI biçiminde, AIAA'ya dönüştürülecek |
| Depoya atıf | ❌ GitHub bağı kaynakçaya konamaz; **Zenodo DOI'si zorunlu** |
| Sonuçlar bölümü | ❌ Atıf içeriyor, çıkarılacak |
| Makale türü | ⚠️ **Yazar kararı** — Full-Length (hakemli) / Design Forum (hakemsiz) |
| Ücretler | ⚠️ Teyit edilmedi |

**Gönderimi durduran bir şey yok. Hepsi v8'in yapım listesi.**
