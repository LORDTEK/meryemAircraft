# Boşluk araması — kayıt (CLAUDE §2.2; Tur 119 kararı)

Yazar, Tur 119: *"Arama kısmını okuyucular yapsın sen de kendi aramanı yapacaksın."* Bu dosya **aramaların kaydıdır**.
Protokol Qwen R118-P2'nin önerisidir; ChatGPT'nin oyu Tur 120'de soruldu. Her arama tarihi, aracı, sorgusu ve bulduklarıyla
buraya girer. Okuyucuların aramaları geldikçe aynı biçimde eklenir.

**Aranan şey: boşluk cümlesinin öğeleri** (Adım 1, *"The gap, stated precisely"*):

| # | Öğe |
|---|---|
| a | blended-wing-body (ya da uçan kanat) kuyruk üstü |
| b | **her** propulsor eşeksenli, tork dengeli bir çift |
| c | propulsor'ü yeniden yönlendiren mekanizma yok: pivot yok, eğme yok, değişken hatve yok |
| d | tek bir hareketli düzenek dışında aerodinamik kumanda yüzeyi yok |
| e | tamponlu seri hibrit güç |
| f | taşınan askı kütlesi, açıkta seyir sürüklemesi ve askıyla boyutlanan sürekli güç için açık muhasebe |

**Ölçüt.** Bir kaynağın öğelerin **hepsini bir arada** taşıması boşluğu kapatır. Kısmi birleşimler Adım 1'in dolu listesine
aday olur (S-45: *"some of them together"*).

---

## Arama 1 — Claude, 2026-09-27

**Araç.** Genel bir web arama motoru; sorgu başına en çok ~10 bağlantı. Görülen yalnız **arama motorunun özet parçaları**.
**Hiçbir belge açılmadı:** WebFetch `patents.google.com`, `news.lockheedmartin.com` ve `search.informit.org` için ağ vekilince
engellendi, öbürleri denenmedi. **Hiçbir veri tabanı doğrudan sorgulanmadı:** AIAA ARC, IEEE Xplore, NTRS, Espacenet, USPTO,
Scopus ve Web of Science yok.

**Sorgular (12):**
1. `blended wing body tail-sitter UAV coaxial contra-rotating propellers`
2. `tail-sitter UAV series hybrid electric coaxial rotors long range`
3. `tailsitter flying wing coaxial rotor pairs wingtips torque balanced no control surfaces`
4. `patent tail-sitter aircraft blended wing coaxial counter-rotating propellers wingtip`
5. `tail-sitter VTOL roll control spoiler strip instead of reaction torque differential coaxial`
6. `Sikorsky Rotor Blown Wing tail sitter configuration prop-rotors cyclic control hybrid-electric`
7. `tail-sitter blended wing body multiple coaxial propeller pairs differential thrust pitch yaw roll spoiler`
8. `VTOL tailsitter flying wing US20050178879 abstract propellers`
9. `"tail-sitter" "series hybrid" UAV`
10. `"Rolling control of a tail-sitter aircraft with no control surfaces" APISAT 2024`
11. `Double Hybrid Tailsitter Unmanned Aerial Vehicle With Vertical Takeoff and Landing propulsion configuration`
12. `tail-sitter UAV "coaxial" "hybrid" engine generator buffer battery VTOL fixed pitch four coaxial pairs`

**Sonuç.** Bu ön aramada **öğelerin hepsini bir arada taşıyan bir kaynak bulunamadı.** Bu, §2.2 anlamında **belgelenmiş arama
değildir.** Veri tabanı sorgulanmadı, belge açılmadı, özetler arama motorunun kendi özetidir. **Boşluk cümlesinin biçimi
değişmez.**

**Adaylar.** Hiçbiri açılmadı. **Aşağıdaki nitelemeler arama özetlerinden alındı**; hiçbir sayı ya da alıntı metne girmez
(§2.1). Her biri için PDF gerekiyor.

| # | Aday | Özetin söylediği | Öğeler | Nereye aday |
|---|---|---|---|---|
| L1 | **US 2005/0178879 A1**, *VTOL tailsitter flying wing* (Y. Mao; başvuru 2004; özete göre terk edilmiş) | dört pervane: sol kanat, sağ kanat, üst ve alt dikey kuyruk; kanat çifti ile kuyruk çifti ters yönde döner; **bütün uçuş evrelerinde tam tutum diferansiyel güçle**; üst çift seyirde kapatılıp katlanabiliyor | a (uçan kanat), c?, d? | Adım 1'in *"attitude without aerodynamic control surfaces"* maddesi (2013'ten önce, ama patent başvurusu, uçuş değil); Adım 7'nin durdurma/katlama sınıfı |
| L2 | **Sikorsky Rotor Blown Wing (RBW)** — basın 2024–2025; patent US 2017/0297699 *Quad rotor tail-sitter aircraft with rotor blown wing configuration* | kuyruk üstü; iki pervane-rotor; helikopter ve uçak kipinde uçtu; bataryalı 52 kg prototip; **kolektif ve çevrimsel (cyclic) kumandalı** rotorlar; hibrit-elektrikle büyütme amacı. **Bir özet "eğilebilen naseller" diyor, patent özeti demiyor — çelişik, açılmadan hüküm yok** | a?, e? | dolu liste: rotanın endüstriyel ölçekte çağdaş örneği; değişken hatve göbeği taşıyor, yani (c)'yi taşımıyor |
| L3 | **APISAT 2024**, *Rolling control of a tail-sitter aircraft with no control surfaces* (Informit) | tork farkıyla yatış kumandası seyirde "considerably less efficient"; itki farkıyla yatış mümkün; dihedral sapma kumandasını yatışa çeviriyor | d | **Adım 1, 5, 8, 9: reddedilen tepki torku kanalının bedeli** — bu kaynak kanalın seyirdeki zayıflığını nicelendiriyor olabilir. Açılırsa kaynak-sonuç işareti gerekir (§2.1) |
| L4 | **Double Hybrid Tailsitter UAV with VTOL** (IEEE, belge 9739654, 2022) | uçan kanat; bir içten yanmalı güç grubu (seyir) + iki elektrikli grup (dikey); elektrikli pervaneler hücum kenarında sabit; iki irtifa dümeni yüzeyi ve iki dikey stabilizör; iki yönde geçiş uçuldu | a, e (seri değil, ayrı güç grupları) | dolu liste: hibrit güçlü kuyruk üstü uçtu |
| L5 | Başka görülenler | U-Lion (2017; eşeksenli çift yalpa çemberinde, itki yönlendirmeli); US 2021/0362851 (kuyruk üstü çift kanat, eğilebilen eşeksenli rotor); US 5,381,985 (tiltwing için kanat ucunda karşıt dönüşlü proprotor); US 11,718,398 B2 (üflemeli uçan kanat CTOL/VTOL kuyruk üstü); MATEC 2018 (kumanda yüzeysiz simetrik dört rotorlu çift kanat kuyruk üstü); arXiv 2309.13559 ve 2511.04251 (swashplate'siz çift rotorlu kuyruk üstü); Cai ve ark. 2024 (tüpten fırlatılan kuyruk üstü) | tek tek | çoğu (c)'yi taşımıyor (eğme ya da hatve mekanizması); ayrıntı için açılmalı |

**Sınır.** Bu aramanın bulamaması aranmadığının kanıtı değildir (§2.2). Ölçüt yalnız öğelerin **bir arada** bulunmasıdır; tek tek
her öğe zaten dolu (Adım 1).

---

## Okuyucuların aramaları (Tur 120 cevapları, 2026-09-27)

**Dördünün ortak sonucu:** a–f'nin hepsini bir arada taşıyan kaynak bulunmadı. **Hiçbiri veri tabanını doğrudan sorgulayamadı,
hiçbiri PDF açmadı.** Grok, ChatGPT ve DeepSeek bunun §2.2 anlamında belgelenmiş arama olmadığını açıkça yazdı; Qwen *"The gap
holds"* dedi (fazla okuma).

| Okuyucu | Araç ve erişim | Sorgular | Adaylar (yalnız özet; açılmadı) |
|---|---|---|---|
| **Grok** | genel web dizini; ARC, Xplore, NTRS, Espacenet, USPTO, Scopus, WoS erişilemedi | 5, sorgu dizgeleriyle; her birinin ilk sayfası (~8–12 sonuç) | **WO2025255583A1** (BWB kuyruk üstü; a); **Vegh, *Hybrid-Electric Design Studies for a Long-Endurance Tailsitter*, AIAA SciTech 2025 / *J. Aircraft*** (eşeksenli kuyruk üstü; dört tahrik düzeninden biri seri hibrit SOFC; e); Double Hybrid (L4); EP3912910 (eşeksenli, eğilebilir; c'yi taşımıyor); DARPA Tern (kolektif + çevrimsel; c'yi taşımıyor); Tal & Karaman uçan kanat kuyruk üstü (a, d'ye yakın; b yok); APISAT 2024 (L3; indirilebilir PDF bulamadı) |
| **ChatGPT** | genel web araması; veri tabanları doğrudan değil | 6+ sorgu kümesi (terim birleşimleri; tam dizgeler ve sonuç sayıları yok) | **Cai ve ark. 2024** (eşeksenli, itki yönlendirmeli, iki eksenli yalpa çemberi; c'yi taşımıyor); **Vegh 2025/2026** (seri hibrit + eşeksenli kuyruk üstü; yatay ve dikey kuyruk → d'yi taşımıyor); **Rohith, Sridharan & Govindarajan, *Hybrid Powertrain Systems for 100 kg Multicopters and Tailsitters*** (seri hibrit, takviye bataryası, motor seyre göre boyutlanmış; kolektif hatve → c'yi taşımıyor; e ve f'ye yakın); Novlit 2014 (depoda; d'yi taşımıyor); US 2025/0010988 *Blended Wing Body Tailsitter UAV* (elevon/flap ya da itki yönlendirme); **kendi ön baskımız** (hariç tutulmalı) |
| **DeepSeek** | hiçbir veri tabanına erişemedi | — | yok. *"This is a failed search"* — dürüst kayıt |
| **Qwen** | ARC, Xplore, Scopus, WoS erişilemedi; Google Patents, NTRS, Google Scholar kullandığını söylüyor | 3, dizgeleriyle; sonuç sayısı yok | L1 *"Various authors, 2023/2024 conferences"* — **belirli bir belge değil**; L2 Sikorsky RBW patenti; L3 Double Hybrid (başlığı yanlış verilmiş); L4 APISAT 2024. Adaylar *"from open snippets/training data"* — eğitim verisi kaynak değildir |

**Öne çıkan: Vegh.** İki okuyucu bağımsız olarak buldu; Grok'a göre *Journal of Aircraft*'ta — **hedef dergimiz.** Eşeksenli
kuyruk üstü + seri hibrit: boşluk cümlesinin (b)/(e) kesişimine en yakın aday. **İlk indirilecek belge.** Sonra Rohith ve ark. (e + f'ye
yakın: askı tepesini takviye bataryasına verip motoru seyre göre boyutlamak — Adım 3'ün kaçış koşuluyla aynı fikir olabilir; açılmadan
hüküm yok), sonra WO2025255583A1 ve US 2025/0010988 (BWB kuyruk üstü patentleri).

## Açılan belgeler (Tur 121, yazar yükledi, Claude tam okudu)

| Belge | a | b | c | d | e | f | Not |
|---|---|---|---|---|---|---|---|
| Yang ve ark. 2018 IROS, uçan kanat kuyruk üstü | evet | hayır (iki pervane yan yana, CW/CCW) | evet | hayır (iki elevon) | hayır (LiPo) | hayır | dolu liste adayı: uçan kanat + tork dengeli çift + slipstream elevonu; karşı moment bozucu olarak |
| Rheaume & Lents 2016 SAE, yolcu uçağı enerji depolama | hayır | hayır | — | — | kısmen (paralel hibrit, takviye) | hayır | kuyruk üstü değil; Adım 14 ve Adım 7 için kanıt, boşluk için değil |

**Hâlâ indirilmedi:** Vegh (AIAA SciTech 2025, doi 10.2514/6.2025-1436; *J. Aircraft* 10.2514/1.C038393 — Grok'un verdiği DOI'ler,
doğrulanmadı), Rohith ve ark. (*J. Aircraft* 10.2514/1.C038443, Grok), WO2025255583A1, US 2025/0010988 A1.

**Tur 123 — yazar DOI'leri verdi, henüz erişemedi:** Rohith, Sridharan & Govindarajan, *J. Aircraft*, https://doi.org/10.2514/1.C038443 ;
Vegh, AIAA SciTech 2025, https://doi.org/10.2514/6.2025-1436 . Okuyuculara verildi (açabilirlerse okusunlar; açmadıkları belgeden sayı ya
da alıntı yok).

**Tur 122 cevapları (dört okuyucu + Claude):** Yang 2018 ve Rheaume & Lents 2016 iddiaya **engel değil**. Yang dolu listeye ikinci tanık
(Grok P111 cümlesi Tur 123'te oyda); Rheaume & Lents Adım 7'de öğe tanığı (Adım 7 açılınca).

**Tur 125 — Vegh iki ayrı kayıt** (ChatGPT, Grok'un Tur 121'deki DOI'lerini doğruluyor): konferans bildirisi AIAA SciTech 2025,
doi 10.2514/6.2025-1436 (yazarın verdiği); dergi makalesi *J. Aircraft*, doi 10.2514/1.C038393. ChatGPT'nin Rohith ve Vegh okuması hâlâ
yalnız ChatGPT'nin; PDF'ler bekleniyor (Grok P116: doğrulanmamış bir okumadan cümle yazılmaz).

