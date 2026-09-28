# v8 — kanıt durumu ve kaynak konumları (Tur 90; ChatGPT'nin dört düzeyi, DeepSeek'in kapsam sütunu, Qwen P1)

Düzeyler: **verified** (belge açıldı, sayı birebir) · **attributed but unverified** (kaynak adı var, bu turda açılmadı) ·
**model-derived** (makalenin kendi denklemi/hesabı) · **unsupported** (ne belge ne hesap — silinir ya da daraltılır).

| Adım | İddia | Düzey | Belge ve konum (PDF sayfası) | Kapsam |
|---|---|---|---|---|
| 2E | geri çekme sürüklemeyi ~%30 azalttı | verified (Tur 89–90) | `references/conv_doctoral_dissertation_alessandro_bacchini-5_260916_203618.pdf` — s. 4 ("around 30%"), s. 158 ("The drag reduction is 30%") | tek çalışma; Mini Talon / SkyProwler rüzgâr tüneli (Tablo 35: 63 / 34 / 30 %) |
| 2E | mekanizma araç kütlesinin %5'i | verified | aynı belge, s. 183 | yolcu eVTOL uygulaması |
| 2E | azami menzil 119 → 121 km | verified | aynı belge, s. 183 | aynı |
| 2E | menzili en uzun kılan hız +5 m/s ("the great advantage") | verified (S-18) | aynı belge, s. 183 | aynı |
| 2E | "Bill 2 was converted almost exactly into Bill 1" | model-derived (makalenin okuması) | — | tek örnek; genelleme iddiası yok |
| 2D | kuyruk üstü "beşte bir" | **unsupported → silindi (S-14)** | yok | — |
| 2B–2C | NASA çalışmaları, rüzgâr tüneli, quadplane, 26 pervane | attributed but unverified (bu turlarda açılmadı) | Tur 45'te NASA belgeleri açılmıştı; kalanlar ilgili blok açılınca | — |
| 14 | uçuşta kullanılan 24S paket: sistem 0.892 kW/kg sürekli; birim paket 0.724 kW/kg | verified (Tur 91) | `references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf` — "724 W/kg (110 A) · 892 W/kg (440 A)" | VS-210, 210 kg sınıfı eVTOL |
| 14 | birim paket 10.68C, en yüksek 55.1 °C (60 °C sınırına 4.9 °C pay) | verified (Tur 91) | aynı belge | tezgâh deneyi |
| 14 | ~1.5 kW/kg, ~4 dakika | model-derived (kaynağın akım, gerilim ve paket kütlesinden) | aynı belge | — |
| 14 | NASA destekli tasarım çalışması 4 kW/kg, "about twice that of existing batteries" | **verified (Tur 92)** | `references/Barrett-2023_NIAC_solid-state-EAD-propulsion_MIT.pdf` — PDF s. 16 | NIAC tasarım çalışması; varsayım, ölçüm değil |
| 14 | aynı çalışma: "the specific power of lithium-polymer batteries in the literature can be as high as 3 kW/kg" | verified that the study says it (Tur 92); the underlying figure is **attributed** (the study's ref. [60], not opened) | aynı belge, PDF s. 34 | **S-19 çözüldü (Tur 93):** gövdeye alıntı olarak girdi — "which it cites rather than measures" |
| 14 | Barrett ref. [60] = J. M. Rheaume, C. Lents, "Energy Storage for Commercial Hybrid Electric Aircraft", SAE Technical Paper 2016-01-2014 (2016), doi 10.4271/2016-01-2014 | **attributed** — açılmadı; SAE ücretli. (pdftotext çıktısında Barrett'in kaynakçası DOI'yi "2016-012014" diye okuyor; baskı hatası mı çıkarma artığı mı, basılı sayfada denetlenmedi.) | Barrett PDF s. 34, kaynakça [60] | yazar erişebilirse `references/`'e; erişilemezse gövde sayıyı Barrett'e atfetmeye devam eder |
| 14 | Barrett'in kendi sonucu: darbe akım sınırı süreklinin iki katından fazla olabilir; "it may be possible to design a battery pack with the required specific power using existing technology"; askı ≤ 20 s | **verified that the study says it** (Tur 94, PDF s. 32, 34–35); **attributed conclusion, not a built pack** (Grok P55) — sonraki taslak bunu "existing technology meets the demand"e çeviremez | Barrett PDF s. 32, 34–35 | S-20; gövdede "may be possible" olarak |
| 14 | 4 kW/kg | **verified as a design assumption** (ChatGPT: makine okunur tabloda "verified"e indirgenmez — Barrett'in varsaydığı olarak doğrulandı, ulaşılmış kapasite olarak değil) | Barrett s. 16 | — |
| 1 | XV-3 ilk askı Ağustos 1955; XV-15 askı Mayıs 1977 | verified (Tur 94) | `references/19810010574.pdf` | S-23 |
| 1 | DelftaCopter: cyclic + collective hatveli ana rotor; 1 m çap "a compromise"; değişken hatve "two extra actuators … added weight from the mechanisms" (Wong ve ark. 2007'yi aktararak) | verified (Tur 94) | `references/Wagter_et_al_2018_Journal_of_Field_Robotics.pdf` | S-22 |
| 1 | Oosedo 2013 kontrol yüzeysiz kuadrotor kuyruk üstü | attributed (De Wagter kaynakçasında başlık) | De Wagter 2018 | — |
| 1 | Escareno 2007 eşeksenli çift, "at the cost of an extra motor and coaxial system" | verified that De Wagter says it | De Wagter 2018 | 1E |
| 1 | SkySwift 2025: BWB kuyruk üstü, karşıt dönüşlü, afet müdahalesi, XFLR5 VLM + Fluent RANS, winglet, geçiş | verified (Tur 94) | SkySwift PDF | 1E |
| 1 | "several are in service" | **gövdede kaynaksız.** Aday kaynak: Bacchini tezinde V-22 2007'de kabul, "More than 200 V-22 were in service in 2014"; Harrier "the first operational VTOL attack aircraft"; F-35 "now in service" (Tur 94'te açıldı; basılı s. 49, 53, 68) — hepsi **insanlı** | `references/conv_doctoral_dissertation_alessandro_bacchini-…pdf` | oylamada |
| 5 | NASA 1984 incelemesi: iniş takımı "limited to relatively low allowable sink rates"; "tip-over tendencies were a constant worry in gusty air and on uneven ground, particularly with the propellers turning"; iniş güçlüğü "these tail-sitter designs"e: omuz üstü bakış, türbülans, yere yakın düşük kontrol gücü; "hovering over a given spot and touching down precisely was extremely difficult" | verified (Tur 94–95) | `references/19840014464.pdf`, "In retrospect" paragrafı | S-24, S-25 onarıldı |
| 5 | XFY-1 satırı: "Tip-over tendencies noted when on ground in gusty air. Difficult to hover precisely over a spot. Control power about all axes reduced in ground effect. … Gust sensitivity bothersome to pilot during takeoff and landing phases." | verified (Tur 94–95) | `references/19810010574.pdf` | — |
| 6 | J&S 2022 Tablo 3 tam: L/De QSMR 5.4 (TS) / 6.0 (E); side-by-side 5.9 / 7.2; quadrotor 4.9 / 5.8; L+C 8.5 (TE) / 7.9 (E); tiltwing 8.6 (TE). Disk yüklemesi quadrotor 3.5 (TS) / 3 (E) lb/ft² | verified (Tur 95) | `references/1521_Johnson & Silva_122721.pdf`, PDF s. 70 | gövde yalnız quadrotor ikisini alıyor; L+C ve tiltwing Adım 4 gövdesinde; **helikopterler hiçbir yerde yok → S-27** |
| 6 | Bacchini & Cestino 2019: "The multirotor is more efficient in hover. The vectored thrust jet is more efficient in cruise and has a higher range. The lift + cruise is a compromise." Sonuç: "Long-range missions cannot be accomplished by multirotors" | verified (Tur 95) | `references/Bacchini-Cestino-2019_…Aerospace.pdf`, özet ve sonuç | "vectored thrust" örneği Lilium (dönen kanallı fanlar) — tanık kanat için, mekanizma için değil; kayıt |

## Kaynak-sonuç işareti (Tur 96; DeepSeek, ChatGPT'nin değerleri; dört okuyucu + Claude)

Açılan her kaynağın **kendi** sonucu ya da hemen çevresi, gövdedeki alıntıya göre ne yapıyor.

| Kaynak | Gövdenin aldığı | Kaynağın kendi sonucu / çevresi | İlişki | Gövdede |
|---|---|---|---|---|
| Bacchini tezi s. 183 | Bill 2 → Bill 1 dönüşümü | hız kazancı ("the great advantage") | niteler | S-18 ile alındı |
| **Veri kümesi evi ≠ her iddianın tanığı** (Tur 115; ChatGPT, dört okuyucu + Claude) | NASA beş aile çalışması (J&S 2022) | kimlik, seçim gerekçesi, görev, üç tasarım → Adım 4 · 1.2 % / 9.4 % → turbo-elektrik L+C / tilt-wing çifti · "not enough to counter" → tümü elektrikli L+C / quadrotor (S-43) · rota tarifleri → Adım 1 · Fatura 1 bulgusu → Adım 2 | kayıt | tanık kapsamı denetim maddesi |
| J&S 2022 (`references/1521_Johnson & Silva_122721.pdf`, pdf s. 11; Tur 113 açıldı, paragrafın tamamı okundu) | Adım 4: "the source states the second half of the prediction in its own words" | cümle **all-electric** L+C'yi **quadrotor**la kıyaslıyor ("reduces the battery weight compared to the quadrotor, but not enough to counter the increase in structure and propulsion weight"); aynı paragraf: "Generally, structural and propulsion weights increase with the number of rotors" | **niteler** (tanık kapsamı: Adım 4'ün test çifti turbo-elektrik L+C / tilt-wing, quadrotor "for scale") | S-43 adayı, okuyuculara |
| Bacchini tezi s. 141 (Tur 111 açıldı; paragrafın tamamı okundu) | Fatura 2: "motorların ürettiği sürükleme önemli" | "We did not choose the motors paying attention to their size and their drag"; "the drag produced by the means [beams] is limited" | **çelişir** (kirişler) / **niteler** (motor seçimi) | S-42 |
| Barrett 2023 s. 16, 34–35 | 4 kW/kg, "about twice that of existing batteries" | 3 kW/kg literatürde; darbe akımı; "may be possible … using existing technology"; askı ≤ 20 s | **yumuşatır** | S-19, S-20 ile alındı |
| Yu 2025 | 0.724 / 0.892 kW/kg; 10.68C; 55.1 °C | uçuşta kullanılan sistem | destekler | — |
| De Wagter 2018 | "theoretically impossible"; DelftaCopter "a compromise" | DelftaCopter değişken hatveli; değişken hatve çare, iki eyleyici ve kütle bedeli | **niteler** | S-22 ile alındı |
| NASA 1984 inceleme | boş ağırlık kazancı; üç iniş güçlüğü | takım düşük çöküş hızıyla sınırlı; engebeli zeminde devrilme; güçlük "these tail-sitter designs"in | **niteler** | S-24, S-25 ile alındı |
| NASA 1981 inceleme | XFY-1 altı geçiş; motor ve dişli kutusu | XFY-1 satırı: devrilme, hassas askı, yer etkisinde düşük kontrol gücü | destekler | — |
| J&S 2022 Tablo 3 | quadrotor 4.9 / 5.8; L+C 8.5; tiltwing 8.6 | helikopterler 5.4–7.2 (yan yana elektrikli 7.2, kanatsız); L+C elektrikli 7.9 | **niteler** | S-27 oylamada (R-4 göndergesiyle); L+C ve tiltwing Adım 4'te |
| Bacchini & Cestino 2019 | çok rotorlu kısa menzil, "vectored thrust" seyirde verimli | "The lift + cruise is a compromise"; vectored thrust örneği Lilium (dönen fanlar) | destekler | — |
| Bacchini tezi s. 49, 53, 68 | (önerildi, alınmadı) V-22 hizmette | insanlı | **kapsam dışı** (tanık kapsamı) | alınmadı |
| 1G | Merical, Beechner & Yelvington 2014, "Hybrid-Electric, Heavy-Fuel Propulsion System for Small Unmanned Aircraft", SAE 2014-01-2222: "A series hybrid-electric propulsion system has been designed for small rapid-response unmanned aircraft systems"; "Development of the hybrid propulsion system is ongoing, with current efforts focused on … gearing up for a future hardware demonstration" | **attributed — yalnız özet**, yazarın yapıştırdığı (Tur 97); PDF açılmadı (SAE ücretli) | SAE Mobilus özeti | **Kaynak-sonuç: niteler** — tasarım ve benzetim, donanım gösterimi gelecekte; "established precedent"i değil "has been designed for"ı taşır. S-29 |
| Merical ve ark. 2014 (özet) | seri hibrit emsali (1G) | tasarım + benzetim; donanım gösterimi "future" | **niteler** | S-29 oylamada |
| 1G | Schoemann 2014, TUM doktora tezi "Hybrid-Electric Propulsion Systems for Small Unmanned Aircraft": (s. 7) seri yapılandırma tanımı; (s. 25) *"there are neither manned nor unmanned commercial hybrid-electric aircraft on the market now. The aircraft that were flown are technology demonstrators."*; *"The only prototype of an unmanned aircraft with hybrid-electric propulsion system to the author's knowledge was built at the Air Force Institute of Technology"*; Harmats & Weihs 1999: *"the parallel configuration proves to be more efficient than the series configuration"*; (s. 26) DA36 E-star, *"The title of the world's first series hybrid-electric aircraft is claimed by Siemens AG, Diamond Aircraft and EADS"*, E-star 2 *"had its maiden flight in June 2013"*; (s. 30) *"It is affirmed in HARMON (2005) and HARMATS & WEIHS (1999) that the parallel configuration is best suited for unmanned hybrid-electric aircraft."* | **verified** (Tur 97; yazar `cfd/document.pdf` olarak yükledi → `references/Schoemann-2014_TUM-PhD_hybrid-electric-propulsion-small-UAV.pdf`) | basılı s. 7, 25, 26, 30 | **Kaynak-sonuç: çelişir** — 2014 itibarıyla 1G'nin "established precedent in small uncrewed aircraft" ifadesini taşımıyor; seri hibrit insanlı motorlu planörde uçmuş, küçük İHA için tasarlanmış (Merical 2014). Literatür İHA için paraleli yeğliyor: bizim seri seçimimizin gerekçesi verimlilik değil mimari (Adım 7, 8) — kayıt |
| Schoemann 2014 (TUM tezi) | seri hibrit emsali (1G) | 2014'te ticari hibrit uçak yok; uçanlar gösterici; İHA için paralel daha uygun | **çelişir** | S-29 oylamada |
| 8 | NACA TR-796: "The value of the directional-stability parameter Cnβ, recommended for conventional airplanes, is usually greater than 0.001 per degree"; kuyruksuzlar için "should be as great as required on conventional airplanes"; modeller "a value of Cnβ of only one-third this amount" ile uçmuş, en iyi uçuş nitelikleri 0.001 üstünde | verified (Tur 98) | `references/NACA-TR-796_…TAILLESS-airplanes.pdf` | **Kaynak-sonuç: destekler** (üçte bir ile uçuş kaydı 39 mm'yi tutucu kılar) |

**Boşluk araması (Tur 120).** Arama kaydı ayrı dosyada: `paper/v8-gap-search.md` (Qwen R118-P2 protokolü; ChatGPT'nin oyu
bekleniyor). Oradaki adaylar **açılmadı**; kaynak-sonuç işareti ancak PDF depoya girip okununca verilir.

**Tur 121 — ChatGPT R119 (kayıt; dört okuyucu + Claude).** Adım 5: *"The present arrangement takes the weight benefit and extends it
by giving the same structure the control duty as well."* NASA kaynağı (19840014464) yalnız ağırlık kazancını söylüyor; kontrol görevini
aynı yapıya vermek bu makalenin tasarımıdır. **Kaynak-sonuç: destekler (ağırlık kazancı) / söylemiyor (kontrol görevi).** Cümlenin öznesi
(*"The present arrangement"*) bunu zaten söylüyor; değişiklik yok.

**Tur 121 — yazarın yüklediği iki belge, tam okundu (Claude, 2026-09-27).** İstenen Vegh 2025 ve Rohith ve ark. değil; başka iki belge.

| Belge | Nereye dokunuyor | Kaynağın kendi sonucu / niteleme | Kaynak-sonuç |
|---|---|---|---|
| **Rheaume & Lents 2016**, SAE 2016-01-2014 (`references/Rheaume-Lents-2016_…pdf`) — tek koridorlu yolcu uçağı, 62 000 kg, iki GTF, kalkış ve tırmanışta 2 500 HP elektrik takviye, **türbinler seyre göre boyutlu**, tasarım noktası 1 500 kWh / 5 000 HP | **Adım 14** (tampon özgül gücü): Tablo 1 Li-ion 1 800 W/kg [12], Li-Po 3 000 W/kg [12], süperkapasitör 500–10k [8] ve 10k–100k [14] W/kg (özgül enerji 1–10 Wh/kg). **Adım 7 / 3** (kaçış koşulunun ilkesi): sürekli güç birimini seyre göre boyutlayıp tepeyi elektrik depodan karşılamak — başka sınıfta, paralel hibritte | *"The best metrics in each category for each battery type were selected. Such batteries are not commercially available since they are usually optimized either for specific energy or specific power."*; *"the battery discharge rate metrics are not considered here"*; *"specific power is a significant driver of battery weight but was not considered in this analysis"*; sonuç: turbojeneratör en umut verici, batarya ancak 1 000 Wh/kg'da rekabetçi | **Adım 14'ün 3 kW/kg'ı için: niteler** — aynı sınıf rakam (Li-Po 3 000 W/kg) burada da **alıntı** (Shukla & Kumar 2013), kategori en iyisi, özgül enerjiyle aynı anda erişilemez. **Adım 7'nin "None of the three elements is new"i için: destekler** (ilke başka nüfusta var). **Tanık kapsamı:** insanlı yolcu uçağı, paralel hibrit, kalkış/tırmanış — bizim seri hibrit, 50 kg İHA, askı tepesi değil |
| **Yang, Zhu, Zhang & Wang 2018**, IROS (`references/Yang-Zhu-2018_IROS_…pdf`) — uçan kanat kuyruk üstü, 2,23 kg, iki CW/CCW pervane **yan yana**, iki elevon, iki 6S LiPo | **Adım 1** dolu liste: askı kontrolünün yerleşik cevabı slipstream içinde yüzey — ikinci tanık. **Adım 1 / 8 / 9** reddedilen kanal: itki ekseni (zb) etrafında kontrol **diferansiyel elevonla**; pervane karşı momenti (M_l + M_r) gözlemcide **bozucu** olarak kestirilip bastırılıyor, kanal olarak kullanılmıyor. **Adım 8** eksen adları: askı gövde çerçevesi (Wang 2014'ün yer değiştirmesiyle tutarlı) | *"The on-going transition and horizontal flight of the tailsitter … are the main future works."* — yalnız askı ve dikey uçuş uçuldu (3–4 m/s rüzgârda) | **Adım 1 "surface in the slipstream": destekler.** **"Using it is a choice, and so is declining it": destekler** (reddetme de uygulamada var — ama yan yana, eşeksenli değil; tanık kapsamı). **Boşluk öğeleri:** a evet (uçan kanat), b hayır (eşeksenli değil), c evet (eğme/hatve yok), d hayır (iki elevon), e hayır (tümüyle elektrikli), f hayır |

**Tur 128 — Rohith ve Vegh: İZ, KANIT DEĞİL** (DeepSeek'in önerisi; okuma durumu açık yazılsın diye). Depoda PDF yok; hiçbir sayı ya da
alıntı metne girmez (P116). Okuma yalnız ChatGPT'nin, ResearchGate görüntüsünden (Tur 126); öteki üç okuyucu ve Claude açmadı.

| Belge | Okunan | Sınıflama (Tur 127, dört okuyucu + Claude) | Kaynak-sonuç |
|---|---|---|---|
| **Rohith, Sridharan & Govindarajan**, *J. Aircraft*, doi 10.2514/1.C038443 | tam metin (ChatGPT; s. 1, 9–11, 13–15) | (a) evet, (e) evet; **(c) hayır** — kuyruk üstüye çevirme *"fixed wings and collective pitch change mechanisms"* ekliyor (s. 13–14) | Adım 7'nin *"None of the three elements is new"* ve *"some of them together"*ini **destekler** (en yakın aynı sınıf tanık: kuyruk üstüde depodan askı tepesi); boşluğu **söylemiyor** |
| **Vegh**, AIAA SciTech 2025, doi 10.2514/6.2025-1436 | konferans tam metni (ChatGPT; s. 1, 5–6, 10–11, 26) | (a), (b), (e) evet. **(c) gösterilmedi** — "collective" eşleşmesi yok, açık ifade de yok; yokluk sayılmaz. **(d) görüntüden kurulamadı** — gövde, yatay ve dikey kuyruk var; kuyruklarda kumanda yüzeyi sayısı bildirilmemiş (Grok, Qwen, ChatGPT) | boşluğu **söylemiyor** |
| **Vegh**, *J. Aircraft*, doi 10.2514/1.C038393 | yalnız özet | — | — |

**Tur 131 — Silva, Johnson ve ark. 2018 (NASA 20180006683, `references/20180006683.pdf`), Tur 130'da açıldı (S-54).**

| Belge | Nereye dokunuyordu | Kaynağın kendi sonucu / niteleme | Kaynak-sonuç |
|---|---|---|---|
| Silva ve ark. 2018 — NASA kavram araçları (dört tip, Adım 4'ün Johnson & Silva 2022'sinden **önceki** boyutlandırma kümesi) | Adım 2 Fatura 1 paragrafı (**Tur 131'de silindi**) | s. 14: *"The weight of the Lift+Cruise concepts is heavier in general than for the other vehicles. This is not driven by the cruise power draw … the most likely targets for reducing vehicle weight are the extra empty weight items on board in hover (wing and propeller)."* — askıda taşınan **seyir** donanımı. Başka sayfada: *"with the Lift+Cruise being heaviest"* | Fatura 1 okuması için **çelişir** (kaynak aynasını söylüyor); gövdede kullanılmıyor. DeepSeek: yapılandırmanın kanadını askıda taşıması sorusuna (S-56) kayıt olarak ilgili — tanık kapsamı farklı (rakip sınıfı), gövdeye girmez |

**Tur 134 — Rohith, Sridharan & Govindarajan 2026 AÇILDI** (`references/Rohith-Sridharan-Govindarajan-2026_JAircraft_…pdf`, yazar
yükledi; Claude tam okudu: özet, §II yapılandırmalar, eğitim yükseltme yolu, §III sonuçlar, Sonuçlar). ChatGPT'nin Tur 126 okuması
**doğrulandı** (kolektif hatve, %110 seyir, takviye bataryası).

| Belge | Nereye dokunuyor | Kaynağın kendi sonucu / niteleme | Kaynak-sonuç |
|---|---|---|---|
| Rohith ve ark. 2026, *J. Aircraft* 63(2):575–591 — 100 kg çok rotorlu ve kanatlı çift kanat kuyruk üstü türevleri; **boyutlandırma çalışması** (HYDRA, SAND) | Adım 1 dolu liste (öneri, Tur 134); Adım 7 *"some of them together"* tanığı (öneri) | s. 575: *"The engine was sized to provide cruise power, while a 'boost' battery was sized to provide the necessary additional power required to take off and land vertically."* s. 585: *"110% cruise instead of 150% hover … the single biggest driver for empty weight reduction."* s. 586: dönüşüm *"fixed wings and collective pitch change mechanisms for the rotor blades"* ekliyor. s. 580: *"Variable-pitch and variable-RPM prop-rotors enable good hover figures of merit and good cruise propeller efficiencies with the same blade shape. The cost … is paid up-front in additional parts as well as development time to fine-tune flight controls, especially during transition."* Sonuç 2: kanatlı kuyruk üstünün seyir aerodinamik verimi çok rotorlununkinin *"nearly 3×"* (s. 589) | Adım 7'nin *"None of the three elements is new … some of them together"*ini **destekler** (depodan askı tepesi + kuyruk üstü); boşluğu **söylemiyor** — (c)'yi karşılamıyor (kolektif/değişken hatve). Adım 1'in *"known result"* maddesini **destekler** (s. 580). Uçurulmuş araç değil; tanık kapsamı: 100 kg, boyutlandırma |

**Tur 135 — Rohith gövdede** (dört okuyucu + Claude): Adım 1 dolu liste satırı (s. 575, 586) ve Adım 7 tanık cümlesi (Rheaume ile).
Durum: **kanıt, okundu** (Qwen P1). *"nearly 3×"* (s. 589): **iz, gövdede değil** — farklı ölçüt ve farklı boyutlandırma aracı; Adım 6'nın
yönüne üçüncü taraf bir tutarlılık işareti olarak kayıtta (DeepSeek P1); yalıtım çifti kuralı gereği gövdeye girmez. s. 580 (değişken
hatve): gövdeye girmez (Adım 1'in maddesinde iki kaynak var).

**Vegh — durum (Qwen P2):** **iz, doğrulanmadı.** Depodaki dosya yalnız düzeltme duyurusu (doi 10.2514/6.2025-1436.c1: Tablo 2 değişti; s. 11
cümlesinden *"tail volume"* silindi); (c) ve (d) hakkında bir şey söylemiyor. Asıl bildiri (10.2514/6.2025-1436) ve dergi sürümü
(10.2514/1.C038393) depoda yok. Hiçbir yerde düzeltme duyurusu makale gibi anılmaz (ChatGPT; H taramasında denetlenir).

**Tur 136 — Vegh konferans bildirisi (doi 10.2514/6.2025-1436): ChatGPT okudu, depoda değil.** Belge türü: **tam metin, ResearchGate
görüntüsü, yalnız ChatGPT** (ChatGPT'nin sürüm etiketi kuralı; Qwen'in "belge türü" alanı oyda). Kaynak-sonuç: boşluğu **söylemiyor**;
kendi sınırları: pil teknolojisi ticari değil (s. 11), daha yüksek doğrulukta analiz önerisi (s. 26), rüzgârda kalkış/iniş incelenmedi
(s. 5). Dergi sürümü (10.2514/1.C038393) ve düzeltme duyurusu (…1436.c1) ayrı kayıtlar; bulgular sürümler arasında taşınmaz.

**Tur 137 — Vegh müsveddesi depoda ve Claude okudu** (`references/Vegh-2025_MANUSCRIPT-R3-clean_…pdf`). **Belge türü: yazar müsveddesi,
düzeltme 3 (temiz), kamuya açık; dizgilenmiş sürüm değil; hangi yayına karşılık geldiği dosyada yok.** Sayfalar bu dosyanınki
(ChatGPT'nin ResearchGate sayfalarından bir iki sayfa kayık — ör. *"beyond commercially available"* burada s. 10, ChatGPT s. 11).
ChatGPT'nin Tur 135 raporundaki her olgu bu dosyada **doğrulandı**: eşeksenli kuyruk üstü (s. 4); aynı gövde ve kuyruk geometrisi,
yatay kuyruk 58 ft², dikey kuyruk 27 ft², rüzgârda kalkış/iniş incelenmedi (s. 5); SOFC *"in a series hybrid arrangement, providing
electrical power to a battery that in turn provides electrical power to an electric motor"* (s. 7); yakıt pili *"unable to completely
power the aircraft in hover out of ground effect at takeoff"* (s. 13); pil varsayımı ticari değil (s. 10); *"partially decoupled power requirements between hover and
forward flight"* (s. 20); *"control characteristics … would vary substantially"* (s. 24); daha yüksek doğrulukta analiz önerisi (s.
26). **"collective", "cyclic", "control surface", "elevator", "rudder", "elevon", "attitude", "transition", "blended", "flying wing"
hiç geçmiyor; "novel" yok; "first" yalnız başka bağlamlarda.** Ek bulgu, s. 4: kuyruk üstüler *"offer reduced mechanical complexity for
conversion compared to tiltrotor and tiltwing aircraft"* (kaynağın [4]'üne dayanarak).

| Belge | Nereye dokunuyor | Kaynak-sonuç |
|---|---|---|
| Vegh müsveddesi (R3) | Adım 1 dolu liste (öneri, Tur 137) | (b)+(e) birlikte **destekler** (dolu); (a) **hayır** (gövde + kuyruklar); (c), (d) **söylemiyor**; boşluğu **söylemiyor**. s. 4'ün mekanik karmaşıklık cümlesi Adım 1'in *"The route itself is established"*ini **destekler** |

**Tur 138 — Vegh satırı Adım 1'e girdi (Öneri V; dört okuyucu + Claude; son yan cümle kalır, *"reported in 2025"* yer tutucu).**
Alıntılar müsveddeye karşı yeniden denetlendi: *"coaxial tailsitter concept"* (s. 4), *"in a series hybrid arrangement, providing
electrical power to a battery that in turn provides electrical power to an electric motor"* (s. 7), *"unable to completely power the
aircraft in hover out of ground effect at takeoff"* (s. 13; kaynakta özne *"The fuel cell (and diesel engine for the diesel-electric
case) was unable …"*, ve *"for the baseline aircraft (and all aircraft sized for this study)"* diye sürüyor — satırdaki *"the fuel cell
alone"* bu cümlenin yakıt pili kolunu, seri hibrit düzeninde pilsiz hâli anlatır).

- **Yokluk arama listesi (DeepSeek P4 — "the paper does not state" iddiasıyla birlikte taşınır).** Müsveddenin tamamında aranan ve
  **geçmeyen**: *"variable pitch", "propeller pitch", "blade pitch", "fixed pitch", "fixed-pitch", "swashplate", "collective", "cyclic",
  "control surface", "elevator", "rudder", "elevon", "attitude", "transition", "blended", "flying wing", "novel", "governor", "rpm"*.
  **Geçen ve bağlamı:** *"pitch"* bir kez, s. 19 — *"increases the required pitch angle for forward flight"* (uçağın yunuslama açısı,
  kanat yüklemesi bağlamında; rotor hatvesi değil). *"control"* s. 24 (*"control characteristics … would vary substantially"*, boş kuyruk
  geometrisiyle) ve s. 28 (kaynakça başlığı). *"torque"* s. 6, 16, 21, 22 — hepsi motor özgül torku (boyutlandırma), kumanda değil.
  *"yaw"*, *"moment"* geçmiyor; *"roll"* yalnız bir yazar adında (s. 29).
- **Kayda değer, gövdeye girmez:** s. 14 — loiter, seyir ve alçalma bölümlerinde *"rotor tip speed was lowered to 80% of the hover
  value"*. Bu **devir** değişimidir, hatve değil; rotorların hatve değiştirip değiştirmediğini söylemez. Boyutlandırma aracı NDARC
  (kaynakça [7]) ve rotor *"blade loading"* ile tanımlanıyor; bundan hatve çıkarımı **yapılmaz** (kaynak sessizliği, yokluk değil —
  Qwen P1'in oydaki koruması).
- **Sürüm bayrağı — gönderimden önce sabitlenecek (DeepSeek P1, Qwen P2, ChatGPT):** iki aday yayın — AIAA SciTech 2025, doi
  10.2514/6.2025-1436; *J. Aircraft*, doi 10.2514/1.C038393. *"reported in 2025"* yer tutucudur; tarih kimliği **2025 → SciTech bildirisi
  (sürüm) → müsvedde R3 karşılığı** biçiminde kurulacak (ChatGPT), yalnız *"müsvedde → 2025"* biçiminde değil. Dizgilenmiş sürüm elde
  edilirse alıntılar ve sayfalar ona karşı yeniden denetlenir.

**Kanıt satırı alanları (Tur 138'de kabul; dört okuyucu + Claude).** Her kanıt satırı dört alan taşır: **(1) tür/sürüm; (2) depoda: evet/hayır;
(3) okuyan: kim, hangi sürüm; (4) doğrulama: depo PDF'ine karşı / tek okuyucu görüntüsü / yalnız özet.** Beşinci alan (alıntı sayfa tabanı,
DeepSeek) oyda. İlk uygulama:

| Belge | Tür/sürüm | Depoda | Okuyan (sürüm) | Doğrulama | Alıntı sayfa tabanı (oyda) |
|---|---|---|---|---|---|
| Vegh müsveddesi R3 | yazar müsveddesi, düzeltme 3, temiz; yayın karşılığı dosyada yok | evet | Claude (R3) | depo PDF'i | müsvedde |
| Vegh SciTech 2025 (10.2514/6.2025-1436) | konferans tam metni | hayır | ChatGPT (ResearchGate görüntüsü) | tek okuyucu görüntüsü | ResearchGate (müsveddeden 1–2 sayfa kayık) |
| Vegh düzeltme duyurusu (…1436.c1) | yalnız düzeltme | evet | Claude | depo PDF'i | — (makale gibi anılmaz) |
| Vegh *J. Aircraft* (10.2514/1.C038393) | dergi makalesi | hayır | kimse (yalnız özet) | yalnız özet | — |
| Rohith ve ark. 2026 | *J. Aircraft* 63(2):575–591, dizgilenmiş | evet | Claude (dizgilenmiş) | depo PDF'i | dizgilenmiş |

**Tur 140 — Oosedo ve ark. 2013 depoda ve Claude okudu** (`references/Oosedo-2013_ICRA_quad-rotor-tailsitter-without-control-surfaces.pdf`;
yazar yükledi). Alanlar: **tür/sürüm** ICRA 2013 bildirisi, dizgilenmiş (IEEE Xplore, doi 10.1109/ICRA.2013.6630594), s. 317–322 · **depoda** evet ·
**okuyan** Claude (dizgilenmiş) · **doğrulama** depo PDF'i · **alıntı sayfa tabanı** dizgilenmiş. Önceki durum: **attributed** (yalnız başlık, De Wagter
2018 s. 24) — artık **verified primary**.

- **Araç:** dört rotor + sabit kanat (R/C uçak kanadı, NACA0010, açıklık 0,99 m); *"it does not use any control surfaces even in the level
  flight"* (s. 317); kanatçık sabitlenmiş (*"we fixed the aileron to prevent it from moving"*, s. 318); *"A fixed pitch propeller and a brushless DC
  motor are used as propulsion units"* (s. 318). Kütle 1,18 / 1,39 kg (s. 320).
- **Deney:** askı, geçiş ve seyir uçuşu, açık havada; seyir *"for 8 seconds"*, toplam uçuş 33 s; seyir referans yunuslaması −75° (s. 321).
  *"we could verify the transition and level flight with the developed quad rotor tail-sitter VTOL UAV, which does not have any control
  surfaces"* (s. 322).
- **Kontrol kanalları (s. 319):** *"The PID controller generates the desired differential thrusts for Xb, Yb axis control, the desired torque for
  Zb axis control"*; dağıtıcı her motorun devrini hesaplıyor. Zb itki eksenidir; kaynak ona **yaw** diyor ve *"The coordinate system of the
  aircraft is consistent in every flight modes"* (s. 318) — bizim adlandırmamızda gövde yatış ekseni (CLAUDE §0.1: eksen adları yer değiştirir).
  Yani **tepki torku kanalını kontrol kanalı olarak kullanıyor**. Adım 1'in *"A quadrotor tail-sitter produces a rolling moment from the reaction
  torque of four independently driven rotors"* cümlesini **destekler** (denetim tablosu satırı artık birinci elden).
- **Kanat–iz etkileşimi (s. 320):** pervanelerin altındaki kanada çarpan iz Zb etrafında pervane karşı-torkunun tersine moment üretiyor;
  *"the effect of the slipstream leads to the difficulty of the attitude control"*; çözüm kanadı izin dışına almak (yıldız tipi) ya da yardımcı
  kanat. Tork katsayısı çapraz tipte yarıya iniyor (Şekil 4). **Bizim askı için:** burun çiftinin izi iç kanadı ve şeridi yalıyor; eşeksenli karşı
  dönüşlü çiftte artık dönme hesaplanmadı — Adım 14 girişim satırı yalnız Fatura 2'ye (seyir) bakıyor (Tur 140 önerisi).
- **Geçişte irtifa kaybı (s. 321–322):** *"the altitude significantly fell in transition flight … The cause of altitude loss in transition flight is
  a lack of wing lift. The transition flight was performed quickly, resulting in producing very little flight speed."* Adım 10'un sonlu momentli
  sonucuyla **nitel olarak uyumlu**; tanık kapsamı farklı (1,39 kg, hızlı geçiş, farklı kontrolcü) — yalnız kayıt.
- **Rota ve mekanizma (s. 317):** *"a tail-sitter aircraft is the simplest way to achieve the VTOL maneuver since it does not require extra actuators
  for the VTOL maneuver"*; Quadshot için *"this UAV requires six actuators for flying"* — eyleyici sayımı mantığı. Adım 1'in *"The route itself is
  established"*ini destekler; kayıt.
- **"three times" (s. 317):** *"the quad rotor tail-sitter UAV can fly three times longer distance compared with that of the conventional quad rotor
  helicopter"* — kaynağın **önceki benzetimi** [8]; bu bildiri ölçmüyor ve *"In the future, we will verify the improvement of energy efficiency"*
  (s. 322). **Kendi sonucu söylemiyor/yumuşatıyor**; gövdeye girmez.
- **Sınıflama:** kuyruk üstü evet; (a) hayır (kanat + dört rotorlu çerçeve, BWB değil); (b) hayır (dört tek rotor); **(c) evet** (sabit hatve, yönlendirme
  yok); **(d) evet** (hiç hareketli yüzey yok); (e) söylemiyor (güç kaynağı adı yok); (f) hayır. Boşluğu **söylemiyor**; engel değil.
- **Yokluk arama listesi:** battery 0, hybrid 0, coaxial 0, contra 0, counter-rotat 0, blended 0, flying wing 0, variable pitch 0, collective 0,
  cyclic 0, swirl 0, fuel 0; "engine" 1 (kurum adı); "tilt" 14 (tilt-rotor ve "tilt-twist" kontrol yöntemi).

**Tur 141 — kaynak durumu (P-d, ChatGPT; dört okuyucu + Claude) ilk uygulama: Adım 1'in dolu listesi ve son paragrafı.**
Durumlar: verified primary / verified secondary / attributed (yalnız başlık) / unverified. ChatGPT'nin inceltmesi (ikincil, dolu bir öğeyi kurarken
birincile denk sayılmaz) oyda.

| Adım 1 iddiası | Tanık | Durum | Not |
|---|---|---|---|
| XFY-1 1954, altı geçiş, motor ve dişli kutusu | NASA 19810010574 (tarihçe incelemesi) | verified secondary | programın kendi belgesi değil |
| *"The route itself is established"* (dörtlü + kanat, birkaç eyleyici, on yıldan fazla) | De Wagter 2018 s. 2 (tarama); Oosedo 2013 s. 317 (örnek) | verified secondary + verified primary (bir örnek) | |
| kumanda yüzeysiz kuyruk üstü, 2013 | Oosedo 2013 | **verified primary** (Tur 140) | |
| eşeksenli çift *"proposed specifically to remove the reaction torque …"* (gerekçe yan cümlesi) | Escareno ve ark. 2008 s. 262 | **verified primary** (Tur 142) | DeepSeek P1: paragraf içinde yan cümle başına durum |
| aynı cümle, *"at the cost of an extra motor and the coaxial arrangement"* (bedel yan cümlesi) | De Wagter 2018 s. 3; birincilin eldeki sayfaları bedeli başka sözcükle adlandırıyor: *"it increases the mechanical complexity"* (2008 s. 262) | **verified secondary**; birincil nitelemesi bulundu (kaynak açma kuralı) | Tur 142 önerisi (gövdede birincilin sözcükleri) |
| 2014 MAV *"to compensate each other's torque"* | Wang ve ark. ICAS 2014 | verified primary | |
| iz içindeki yüzey (2014, 2018) | Wang 2014; Yang-Zhu 2018 IROS | verified primary | |
| tepki torku kanalı, 2012 | Zhang ve ark. 2012 | verified primary | |
| kuadrotor kuyruk üstü tepki torkuyla yatış | Oosedo 2013 s. 319 | verified primary (Tur 140) | kaynağın adı *yaw* (Zb = itki ekseni = bizim gövde yatış ekseni; Qwen P2) |
| BWB kuyruk üstü 2025 | SkySwift | verified primary | |
| seri hibrit + kanatlı kuyruk üstü 2026 | Rohith ve ark. 2026 | verified primary | |
| eşeksenli kuyruk üstü + seri hibrit depo 2025 | Vegh müsveddesi R3 | verified primary (müsvedde) | sürüm gönderimden önce |
| pervane uzlaşması, *"theoretically impossible"*; DelftaCopter *"a compromise"* | De Wagter 2018 s. 2 ve kendi aracı | verified primary (De Wagter'in kendi cümlesi) | |
| seri hibrit *"flown in a crewed motor glider"* | Schoemann 2014 tezi s. 25–26 | verified secondary | |
| seri hibrit *"designed for small uncrewed aircraft"* | Merical ve ark. 2014 | **verified primary — abstract only** (Tur 142, dört okuyucu + Claude; ChatGPT'nin adlandırması) | okuma derinliği zaten *doğrulama* alanında ("yalnız özet") |
| *"Tail-sitting aircraft are seventy years old"* | XFY-1 (NASA 1981) | verified secondary | |
| *"blended wing bodies have been a standing subject of transport research for three decades"* | Liebeck 2004, *J. Aircraft* 41(1), 10–25 (`references/Liebeck-2004_…pdf`) s. 10: *"in 1988, when NASA Langley Research Center's Dennis Bushnell asked …"*; *"A NASA/industry/university team was formed in 1994"* | **verified primary** (Tur 142) | 1988 → 2026: 38 yıl — *"three decades"* doğru ama eksik söylüyor (Tur 142 önerisi) |

**Oosedo 2013, ek kayıt (DeepSeek R140-P2):** tepki torku kanalını **kullanan** ikinci birincil tanık — Adım 1'in *"Using it is a choice, and so is
declining it"* çerçevesi artık iki birincil tanıkla (Zhang 2012 eşeksenli çiftte, Oosedo 2013 dört tek rotorda); gövdeye girmez.
**Eksen adı koruması (Qwen R140-P2):** kaynak Zb = itki ekseni, adı *yaw*; bizim adlandırmamızda gövde yatış ekseni (askıda yön, seyirde bank).

**Tur 142 — Escareno 2007 ve 2008, Liebeck 2004 depoda ve Claude okudu** (yazar yükledi).

- **Escareno, Stone, Sanchez, Lozano 2007**, ECC 2007, s. 3385–3390 (`references/Escareno-2007_…pdf`; tam, IEEE Xplore). Alanlar: bildiri, dizgilenmiş ·
  depoda · Claude · depo PDF'i · dizgilenmiş. **Kaynak olgusu:** *"The roll torque is obtained from the difference of the rotors angular velocities.
  Since the control surfaces are submerged in the propeller slipstream (prop-wash), the aerodynamic forces are generated by the elevator and ailerons
  deflections to provide the pitch and yaw motion, respectively"* (s. 3389) — tepki torku kanalını **kullanan üçüncü birincil tanık**; iz içindeki
  yüzey cevabının bir örneği daha. *"the tilt-wing, tilt-rotor and tilt-body, do so at the expense of significantly increased mechanical complexity
  compared to a tail-sitter that uses propeller wash over normal aircraft control surfaces"* (s. 3385). **Kaynak sessizliği:** metinde *"coaxial"*,
  *"counter"*, *"contra"* yok — De Wagter'in *"proposed a coaxial dual propeller version"* (2007'ye atfı) bu metinde görünmüyor (yalnız *"rotors"*,
  çoğul). **Kaynağın kendi sınırı:** deney yalnız dikey kipte tutum kararlılığı (s. 3389–3390); geçiş benzetimde.
- **Escareno, Sanchez, Garcia, Lozano 2008**, *J. Intelligent and Robotic Systems* 54, 261–273, *Unmanned Aircraft Systems* (Springer) içinde —
  **yalnız s. 261–262** (`references/Escareno-2008_…PARTIAL…pdf`). Alanlar: kitap bölümü, dizgilenmiş, **kısmi** · depoda · Claude · depo PDF'i (kısmi) ·
  dizgilenmiş. **Kaynak olgusu:** *"A logical drawback arising from single-propeller aircrafts is the vulnerability to reacting torque … An alternative
  way to face the reacting torque, without using complementary controls, is the use of counter-rotating propellers. This configuration increases the
  thrust and reduces the size of the vehicle but it increases the mechanical complexity"*; tail-sitter *"lacks of swashplate or tilting elements"*;
  *"We have fused the previous concepts to obtain a vehicle that offers the mechanical simplicity of tail-sitter and the operational flexibility of
  coaxial rotorcrafts"* (s. 262). Araç: *"Twister"*, eşeksenli dönüştürülebilir İHA. **Eldeki sayfalarda yok:** *"extra motor"*, *"slightly higher
  efficiency"* (De Wagter'in 2008'e atfettiği) — kısmi olduğu için yokluk sayılmaz. **Sınıflama (eldeki sayfalardan):** kuyruk üstü evet; (a) yok
  bilgisi; (b) evet; (c) söylemiyor; (d) söylemiyor; (e) hayır bilgisi yok; (f) hayır.
- **Liebeck 2004**, *J. Aircraft* 41(1), 10–25, doi 10.2514/1.9084 (`references/Liebeck-2004_…pdf`; dosya adı "2012", içerik 2004). Alanlar: dergi,
  dizgilenmiş · depoda · Claude · depo PDF'i · dizgilenmiş. s. 10: BWB çalışmasının 1988'de NASA Langley sorusuyla başladığı; 1994'te NASA/sanayi/
  üniversite ekibi. **Kaynak olgusu, kayıt:** BWB taşıtında *"Trailing-edge devices and winglet rudders are called on to perform a host of duties,
  including basic trim, control, pitch stability augmentation, and wing load alleviation"* — büyük BWB'nin kumanda yüzeyi yükü; bizim (d) ile karşıtlık,
  gövdeye girmez.
- **Kaynak durumu güncellemesi (P-d):** Escareno gerekçe yan cümlesi verified primary; bedel yan cümlesi verified secondary (birincil nitelemesi
  bulundu); Liebeck verified primary; Merical verified primary — abstract only.

**Tur 143 — eşeksenli maddenin kaynak ayrımı (DeepSeek R142):** gövdedeki *"coaxial"* **Escareno 2008**'e (s. 262, Twister) dayanır; Escareno 2007 metni
*"coaxial"* demiyor. İki Escareno ayrı tanıktır: 2007 → rota karşılaştırması (W, s. 3385) ve tepki torku kanalı kullanımı (s. 3389); 2008 → eşeksenli
çiftin gerekçesi ve bedeli (E-1, s. 262). **Kaynak bağlamı (Qwen R142-P2, oyda):** 2007'nin tanık aracı iz içinde kumanda yüzeyi kullanıyor (bizim reddettiğimiz);
W alıntısı bunu kendi sözleriyle söylüyor.

**Tur 143 — öğe karar kurallarıyla (Q-P1, birleşik metin teyide) yeniden sınıflama:** Rheaume & Lents (e) *"kısmen (paralel)"* → **hayır** (paralel hibrit
(e) değildir). Oosedo (d) **evet** kalır (kilitli kanatçık hareketli aygıt sayılmaz — Grok). Yang (a) evet, Rohith (a) hayır, Vegh (a) hayır, Escareno 2007
(d) hayır: kurallarla tutarlı.

**Tur 144 — kanıt satırı alanları yeniden düzenlendi (P-h, dört okuyucu + Claude; DeepSeek'in iki alanı):** tür/sürüm · depoda · okuyan ·
**erişim derinliği** (tam / kısmi / yalnız özet / yalnız başlık ya da kaynakça / okunmadı) · **doğrulama** (depo PDF'i / tek okuyucu görüntüsü / ikincil
kaynak / doğrulanmadı) · alıntı sayfa tabanı. Örnek: Vegh — konferans bildirisi, **kısmi**, **tek okuyucu görüntüsü** (ChatGPT); müsvedde R3, **tam**,
**depo PDF'i** (Claude). Escareno 2008 — **kısmi**, depo PDF'i.

**Tur 144 — alıntı kilidi (P-i, ChatGPT; dört okuyucu + Claude):** kaynaktan türeyen her cümle *birebir alıntı* / *sadık aktarma* (tırnaksız) / *bizim
sınıflamamız*; tırnak yalnız birebir metne; aynı cümlede alıntı ve aktarma varsa ayrı işaretlenir. **Alıntı bağlamı (Q-P2b):** gövdeye giren her yeni
alıntı için tanık ile yapılandırmamız arasındaki yorumu etkileyen fark kayda yazılır (W: 2007 aracı iz içinde kumanda yüzeyi kullanıyor).

**Tur 144 — Adım 1 dolu listesinin son kanıt denetimi (Qwen R143-P1):** her dolu-öğe iddiasının en az bir **verified primary** tanığı var mı?

| Adım 1 iddiası | En güçlü tanık | Sonuç |
|---|---|---|
| rota kurulu | Oosedo 2013 s. 317 (örnek); De Wagter 2018 s. 2 (tarama) | birincil ✓ |
| rota karşılaştırması (W) | Escareno 2007 s. 3385 | birincil ✓ |
| kumanda yüzeysiz 2013 | Oosedo 2013 | birincil ✓ |
| eşeksenli çift (E-1) | Escareno 2008 s. 262; Wang 2014 | birincil ✓ |
| iz içindeki yüzey | Wang 2014; Yang-Zhu 2018 | birincil ✓ |
| tepki torku kanalı | Zhang 2012; Oosedo 2013 s. 319; Escareno 2007 s. 3389 | birincil ✓ |
| BWB kuyruk üstü 2025 | SkySwift | birincil ✓ |
| seri hibrit + kanatlı kuyruk üstü | Rohith 2026 | birincil ✓ |
| eşeksenli + seri hibrit depo | Vegh müsveddesi R3 | birincil (müsvedde; sürüm gönderimden önce) ✓ |
| pervane uzlaşması | De Wagter 2018 | birincil ✓ |
| XFY-1 1954 (rota tarihi) | NASA 19810010574 | **ikincil** — istisna: tarih cümlesi, boşluğun dolu bir öğesi değil; D-P2 izi: program belgesi aranmadı |
| seri hibrit motorlu planörde uçtu | Schoemann 2014 s. 25–26 | **ikincil** — istisna: *"None of the elements is new"* paragrafı; D-P2 izi: planörün kendi belgesi aranmadı |
| seri hibrit küçük İHA için tasarlandı | Merical 2014 | birincil, yalnız özet |
| BWB otuz yılı aşkın | Liebeck 2004 s. 10 | birincil ✓ |

**Sonuç:** boşluğun dolu öğelerinin hepsinde birincil tanık var. İki ikincil satır tarih/genel cümlelerde; oyda (Tur 144): istisna olarak mı kalsın, birincil mi aransın.
