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

