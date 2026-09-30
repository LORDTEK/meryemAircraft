# *Journal of Aircraft* şartları — şart şart makaleye karşı (2026-09-30)

CLAUDE.md §4'ün dergi şartı kuralı: bir hedef dergiye gönderilmeden önce derginin şartları **baştan sona okunur** ve **şart şart** makaleyle karşılaştırılır.

**Kaynaklar** (hepsi bu turda baştan sona okundu):
- **[S]** `references/AIAA-2024-09_journal-page-limits-and-word-count-guidelines.pdf`: *Journal Page Limits and Word Count Guidelines*, Rev. August 2024, 1 sayfa. **Tur 154'ten beri depoda.** Yazar 2026-09-30'da aynısını yeniden yükledi; SHA-256 aynı olduğu için kopya silindi.
- **[T]** `references/AIAA-journal-LaTeX-template-instructions_Preparation-of-Papers.pdf`: *Preparation of Papers for AIAA Technical Journals*, LaTeX şablonunun talimat metni, 9 sayfa. Yazar yükledi (2026-09-30; özgün adı `mqqbqqvyhtwm.pdf`).
- **[D]** `references/AIAA-manuscript-template-2025.docx`: Word şablonu. Yazar yükledi (2026-09-30). Biçim için kullanılır; ayrı bir şart metni taşımıyor.
- **[W]** AIAA yazar sayfalarının metni: başlık, yazarlık, dipnot, semboller, şekiller, tablolar, listeler, kaynaklar, özet, noktalama ve üslup. **Yazar sohbete yapıştırdı** (2026-09-30). Aşağıdaki alıntılar o metinden birebirdir; metnin kendisi depoda yok.

**Benim hatam.** Tur 187 ve sonrasında yazara *"uzunluk sınırı kayıtta 'bulunamadı'; derginin yönergesine karşı hiç okunmadı"* dedim ve belgeyi yeniden istedim. Oysa [S] Tur 154'ten beri depodaydı (`references/README.md` satır 151). Ayrıca Round 101'deki 12 000 kelime hedefi zaten ondan türetilmişti. `target-journal.md`'deki "bulunamadı ⚠️" satırları Tur 154'ten beri bayattı. Yokluk demeden önce depoyu aramadım (§3.0 kabul (1)'in ihlali).

---

## 1. Uzunluk

| Şart | Kaynak | Bizim durumumuz |
|---|---|---|
| *"Regular/Full Articles 7 – 10 pages; 10,000 – 12,000 words"*, *"*Or equivalent space for figures/tables"*; tek sütunluk şekil/tablo 200, çift sütunluk 450, büyük çift sütun tablo 700 kelime | [S] | Gövde düzyazısı ~13 405 kelime. Altı tablo, kabaca 2 000–2 700 kelime eşdeğeri: 2.1 çare tablosu 450–700, 4.4 ve 4.5 ikişer 200, 5.1 sınıf tablosu 200–450, 6.1 kapanış tablosu (10 sütun) 450, 8.2 eksen tablosu 450. Özet ~150–200. **Toplam ≈ 15 700–16 500, önerilen üst sınırın %30–40 üstünde.** |
| *"A journal editor at his or her own discretion may request that a manuscript be shortened or expanded"*; sınırlar **önerilir** (*"Recommended"*), zorunlu değil | [S] | Aşım bir ret gerekçesi olarak yazılmamış, ama editör kısaltma isteyebilir. **Karar yazarın** (bkz. §9, soru 1) |

## 2. Başlık, yazarlar, dipnotlar

| Şart | Kaynak | Durum |
|---|---|---|
| Başlık *"no more than 12 words"*; jargon, kısaltma ve akronim yok; artikelle (The, A, An) başlamaz; *"preliminary"* ya da *"exploratory"* yok | [W] | **Başlık yok.** Yazılacak. §0'a göre bir iddia yüzeyi olduğu için okuyucu turuna gider |
| Yazarlar: tam ad; kurum, şehir, eyalet, posta kodu, ülke. İlk sayfa dipnotu: unvan, bölüm, AIAA üyelik derecesi; *"corresponding author"* ve e-posta dipnotta | [W], [T] | **Yazar bilgisi yazardan gelecek** |
| Başka yerde dipnot *"discouraged"* | [W], [T] | Gövdede dipnot yok ✓ |

## 3. Özet ve terimler

| Şart | Kaynak | Durum |
|---|---|---|
| Özet tek paragraf, **100–200 kelime**; kaynak numarası yok; şekil, tablo ve bölüm atfı yok; üçüncü şahıs; anahtar kelimeler ve önemli bulgular ilk iki cümlede; başlığı ilk cümlede tekrar etmez; yeni sayısal verileri içerir, yer varsa | [W], [T] | **Özet yok.** Yazılacak. Makalenin en yoğun iddia yüzeyi; §0'ın dört ekseni, korunan sınırlar ve sayı kimliği burada sınanır. Okuyucu turuna gider |
| Terimler listesi isteğe bağlı; **kullanılırsa** özetle giriş arasında durur, bütün sembolleri birimleriyle içerir, tanımlar metinde tekrarlanmaz; akronim terimler listesine girmez, metinde ilk geçtiği yerde açılır | [W], [T] | Gövdede sembol az ama var: `L/De`, `C_L`, `C_D0`, `η_p`, `η_h`, `DL`, `ρ`, `W`, `V`, `P`, `AR`, `e`, `MTOW`, `f_empty`… Liste kullanılırsa tam olmalı. Akronimlerin (VTOL, BWB, RANS, ISA, NASA hariç) ilk geçişte açılması denetlenecek |

## 4. Bölüm yapısı ve başlıklar

| Şart | Kaynak | Durum |
|---|---|---|
| *"Please omit section numbers before all headings unless you refer frequently to different sections. Use Roman numerals for major headings if they must be numbered."* Alt başlıklar büyük harfle (A, B), alt-alt başlıklar Arap rakamıyla | [T] | Bölümlere sık atıf yapıyoruz (82 bölümler arası işaretçi), yani numara kalır. **Dönüşüm:** 1–8 → I–VIII; 2.1 → II.A; *"Section 6.1"* → *"Sec. VI.A"* (*"Use the following standard abbreviations … before numbers: Eq., Fig., Sec."*, [W]). Mekanik iş; bir betikle üretilir |
| *"There must be at least 2 of all subheadings and sub-subheadings."* | [T] | Denetlenecek; tek alt başlıklı bir bölüm varsa başlık italik olur ve paragrafa katılır |
| Sonuç bölümü özeti tekrarlamaz ve kaynak atfı içermez; numaralı son bölümdür. Ek, fon ve teşekkür numarasızdır | [T] | Bölüm 8 sonuç işlevi görüyor; kaynak atfı yok ✓. Özet yazılınca tekrar denetlenecek |

## 5. Kaynaklar

| Şart | Kaynak | Durum |
|---|---|---|
| Kaynaklar köşeli parantezle numaralı ve metinde sırayla atıflı: [1], [1, 2], [1–3] | [W], [T] | **Gövdede atıf numarası yok.** Kaynaklar tarifle anılıyor (*"a tail-sitter study reported in 2007"*). Her birine numara, kaynakçaya tam kayıt |
| Kaynakçada bütün yazarlar yazılır (*"et al."* yok); dergi adı tam; sayfa, cilt ve sayı; mümkünse DOI | [W], [T] | `references/README.md` ve `paper/v8-evidence.md` bilgilerin çoğunu tutuyor; her kayıt tamlanacak |
| *"Authors must reference the original source of a work, not a secondary source."* | [W] | **Açık risk.** Kanıt kaydında *verified secondary* ve *attributed* durumlu tanıklar var (P-d, Tur 141). Her biri için birincil kaynak ya bulunur ya da cümle ondan arındırılır |
| *"References must be limited to readily accessible published material"*; özel yazışma ve kişisel web sitesi kaynakçaya girmez | [W], [T] | Müsvedde tanıklar (Vegh R3 müsveddesi, P-b) dizgilenmiş sürüme karşı uzlaştırılır (zaten kayıtlı kural) |
| Mümkünse konferans bildirisi yerine dergi makalesi atıflanır | [W], [T] | Tanık listesi bu gözle taranacak |

## 6. Listeler, tablolar, denklemler, şekiller

| Şart | Kaynak | Durum |
|---|---|---|
| *"Bullets and dashes are never used to introduce entries in a list."* Listeler 1), 2), 3) biçiminde | [W] | **Gövdede madde işaretli iki liste var**: 2.2'nin izin verilen altı maliyeti ve 5.1'in üç öğesi. Numaralı listeler de (2.2'nin dört başarısızlık kipi, 8.5'in sekiz maddesi) *"1."* biçiminde; hepsi 1) biçimine çevrilecek (mekanik) |
| Tablo: en az iki sütun ve iki satır; başlık üstte; numaralı; metinde sırayla atıflı; dikey çizgi yok; resim olarak eklenmez | [W], [T] | Altı tablonun **numarası ve başlığı yok.** Metin onlara *"the table above"*, *"this table"* diye gönderme yapıyor. Numara, başlık ve *"Table n"* atfı eklenecek; alındı kuralı buna da uygulanır (T2, T3 korunan göndermeler) |
| Denklemler numaralı, sağda parantez içinde; semboller terimler listesinde ya da denklemden hemen sonra tanımlı; resim değil | [T], [W] | Gövdede birkaç denklem var (2.1 güç oranı, 4.4 L/De, 2.1 MTOW). Numaralanacak |
| Şekil **şartı yok**; şekil varsa altyazı en çok 20–25 kelime, 8 punto harf | [W], [T] | **E19'daki park soru böylece kapanıyor: yönergelerde şekil zorunluluğu yok.** Şekil eklemek yazarın isteğine kalır |

## 7. Üslup (kopya düzenlemede de yapılır, ama bizim yapmamız beklenir)

| Şart | Kaynak | Gövdede |
|---|---|---|
| Amerikan yazımı | [W], [T] | *favourable* ×7, *modelled* ×5, *favour(s)* ×4, *optimised* ×2, *centre(line)* ×3, *idealised*, *idealisation*, *characterisation*, *analysed*, *analyses* (fiil) → Amerikan biçimi |
| *"Avoid using dashes in scholarly writing. Pairs of dashes can be replaced with commas or parentheses"* | [W] | Gövdede çok sayıda uzun tire var. **Tur 191'de 4.1'e tireli bir ifade (D1) koyduk**; yönergeye göre parantez olmalı: *"the rotorcraft (multirotor and helicopter alike)"*. Tireler toptan virgül, parantez ya da iki nokta ile değiştirilir; anlamı etkileyen her değişiklik okuyucu teyidine gider |
| *"Italics strictly used for visual emphasis is discouraged"*; vurgu için kalın yazı da dergi biçiminde yok | [W], [T] | Gövdede yoğun **kalın** vurgu var. Gönderim sürümünde kaldırılır; adım kaynakları kalın kalabilir (üretici betik) |
| Beş ve daha çok haneli sayılarda virgül (12,000); dört hanede virgül yok (2000) | [W] | Gövde ince boşluk kullanıyor (*"1 000 kg"*, *"7 271 lb"*) → *"1000 kg"*, *"7271 lb"* |
| *"Avoid above and below"*; *preceding* ya da *next* kullanılır | [W] | Numarasız işaretçiler (*"the table above"*, *"below"*). Tablo numaralanınca çoğu çözülür |
| Tek haneli sayılar yazıyla (birimle kullanılanlar hariç) | [W] | Taranacak |
| *"Use compared with"* (farkları incelemek için); *"since"* ve *"while"* sınırlı; *"prior to"* yerine *"before"* | [W] | Taranacak |

## 8. Gönderim ve politika

| Şart | Kaynak | Durum |
|---|---|---|
| Tek sütun, çift aralık; LaTeX ya da Word şablonu; PDF yüklemesi önerilir | [T], [D] | **Biçim seçimi yazarın:** LaTeX mi Word mü |
| *"Your manuscript cannot be published by AIAA if … The work has been published or is currently under consideration for publication or presentation elsewhere."* | [T] | **Açık soru:** makalenin v7 sürümü Zenodo'da (DOI 10.5281/zenodo.22144194). Belgeler ön baskıdan (preprint) söz etmiyor. AIAA'nın ön baskı politikası ayrıca okunmalı. *Drones*/*Aerospace* gönderimi masadan reddedildi ve sonuçlandı; yalnız AIAA dergi ve konferans geçmişinin beyanı isteniyor |
| Yapay zekâ kullanıldıysa *"authors must include a brief description of AI use in the Acknowledgments section"* | [T] | Teşekkür bölümü yazılacak; CLAUDE.md §4: marka, model ve şirket adı yok, YZ yazar satırında yok |
| Fon kaynakları bölümü; ScholarOne'daki fon verisiyle eşleşmeli | [T] | Yazardan (fon yoksa bölüm yok) |
| Telif beyanı makaleye yazılmaz | [T] | ✓ |
| **Ek malzeme (supplement)** | — | **Belgelerde hiç geçmiyor.** Gövde 34 yerde *"Supplement S#"* diyor. JoA'nın ek malzeme kabul edip etmediği ve biçimi okunmadı. Kabul etmiyorsa bu gönderim için yapısal bir sorun olur. **Açık soru** |

## 9. Yazara sorular

1. **Uzunluk.** Önerilen aralık 10–12 bin; biz tablolarla ~16 bindeyiz. (a) Böyle gönderilsin, editör isterse kısaltılır. (b) Gönderimden önce yeni bir kısaltma aşaması.
2. **Ek malzeme ve ön baskı.** AIAA'nın *Supplemental Materials* ve *preprint* politika sayfalarının indirilip yüklenmesi. Bu ortamdan aiaa.org'a erişim yok.
3. **Biçim.** LaTeX mi Word mü?
4. **Yazar bilgisi.** Ad, kurum, adres, unvan, AIAA üyeliği, fon.

## 10. Önerilen iş sırası (yazar onayıyla)

1. **Yazar kararları** (§9).
2. **Başlık ve özet.** İddia yüzeyi oldukları için okuyucu turuyla, §0'a karşı.
3. **Kaynakça.** Tanık listesinden numaralı kaynakça; ikincil ve *attributed* tanıklar için birincil arama.
4. **Mekanik dönüşüm.** Bir üretici betik: adım kaynakları → gönderim metni. Roman rakamlı bölümler, *Sec.*, numaralı tablo ve denklemler, listeler, Amerikan yazımı, sayı biçimi, kalın vurgunun kaldırılması. **Adım kaynakları değişmez; çıktı denetlenir** (§2.5, W-1).
5. **Üslup geçişi.** Tireler, *above/below*, sözcük kullanımı. Anlam değiştiren her değişiklik okuyucu teyidine gider.
6. **Terimler listesi** (kullanılacaksa), **teşekkür** (YZ beyanı), **fon**.
7. **Son alındı ve sayı denetimi** gönderim çıktısında, sonra ScholarOne.
