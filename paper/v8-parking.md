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
