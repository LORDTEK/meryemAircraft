# v8 park listesi (Tur 146; Öneri F-1, dört okuyucu + Claude)

**Kural (F-1):** bu aşama bitene kadar yeni kural, alan ya da denetim türü yalnız **şimdiki gövde metninde bulunmuş adlı bir kusurla**
gelirse kabul edilir. Öteki her öneri buraya yazılır ve **yalnız bir sonraki aşamanın başında** okunur. Park edilen öneri bütün okumanın
soru listesine giremez (ChatGPT, A-3 oyda). Önceden kabul edilmiş denetimler aşama boyunca yürürlükte.

| # | Öneri | Kimden | Tur |
|---|---|---|---|
| H-3 | yüklem-atıf kapsamı: bir tanığa dayandırılan her olgusal yüklem, atıf kaydında onu destekleyen bir yan cümleye eşlenir | ChatGPT | 144 |
| — | atıf haritası sütunları: desteklenen yüklem (ChatGPT); gövde konumu, alıntı durumu, tanık türü (DeepSeek); tam şema (Qwen P1) | ChatGPT, DeepSeek, Qwen | 144 |
| D-P2 | karmaşıklık korumasına yakın eşanlamlılar (*"simpler"*, *"less complex"*, *"fewer parts"*) | DeepSeek | 144 |
| D-P3 | her karar kuralı için bir olumlu bir olumsuz çalışılmış örnek | DeepSeek | 144 |
| D-P4 | atıf haritası satırları gövdede ilk geçiş sırasıyla; eski `paper/references.md` emekliye ya da eşlemeye | DeepSeek | 144 |
| Q-P2 | *"seventy years"* için tarih çıpası (XFY-1 1954 → 72 yıl) | Qwen | 144 |
| — | numarasız işaretçiler (*above*, *below*) için alındı denetimi (Tur 132'de "bir sonraki aşamanın adayı" diye kaydedilmişti; W-1'in iki öğesi gövde kusuru olarak ayrıca onarılıyor) | Claude | 132 / 146 |

**Aşama sonrasına, park değil, gönderim öncesi listesinde:** H-2 atıf haritasının kurulması (F-2) — `paper/deferred-decisions.md`.

**Tur 205 (Claude, F-1 altında park; gövde kusuru değil):** `aero/roll.py` şeridin alanını **açıklık boyunca** (`ys` 0 → 1,164 m) integre ediyor; şerit planformda 45° eğik, kendi boyu daha uzun. Normal kuvvete cos²(45°) uygulanıyor. Hangi uzunluğun doğru olduğu yeniden hesaplanmadı. Gövdede şerit kuvveti ya da yatış momenti sayısı yok; ekin S8'i yalnız açıklık boyunu (1,164 m, yarı açıklığın %67'si) veriyor.

**Tur 214 (DeepSeek, gönderim sonrası öneri):** Bölüm 2.1'in *f_energy*'si ile Ek S10'un *f_fuel*'u için tek ad. DeepSeek ve Claude: kusur değil, özelleştirme.

- **[2026-10-01, gönderim Step 5 sırasında, Claude] Vegh [11] dergi sürümü olabilir.** Hakem önerisi için yapılan bir web aramasının özeti, *"Hybrid-Electric Design Studies for Long-Endurance Tailsitter Concept"*in *Journal of Aircraft*'ta (23 Aralık 2025) yayımlandığını söylüyor. **Doğrulanmadı** (arama motoru özeti belge değildir, Tur 119). Kaynakçamız AIAA Paper 2025-1436'yı (konferans) gösteriyor. Gönderim sonrası: dergi sürümü var mı, alıntılar ve "the paper does not state" cümleleri dergi sürümünde aynen duruyor mu — okuyuculara (Tur 195 kuralı).
- **Önerilen hakemler (Step 5, 2026-10-01):** B. Govindarajan (University of Maryland), C. De Wagter (TU Delft), P. Panagiotou (Aristotle University of Thessaloniki) — üçü de kaynakçada atıflı çalışmaların yazarı, yazarlarla ortak çalışmaları yok; kurumlar web aramasıyla, e-posta verilmedi.
