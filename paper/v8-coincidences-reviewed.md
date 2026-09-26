# v8 — gözden geçirilmiş sayı rastlantıları (Tur 107; Qwen R105-P2, dört okuyucu + Claude)

Aynı değer, farklı nesne. Sayı kimliği = değer + birim + nesne + model/geometri (CLAUDE.md §2.4). Bir insan bir kez ayırdı;
`paper/build/v8_outbound.py` bu satırlardaki çiftleri haritada **[rastlantı — gözden geçirildi]** diye işaretler, silmez.
Yeni bir çift eklenmeden önce iki bağlam da okunur.

| Sayı | Kaynak adım | Kaynaktaki nesne | Öteki adım | Öteki adımdaki nesne |
|---|---:|---|---:|---|
| 53.5 | 13 | +53.5 % (sözleşme tablosu, C satırı) | 10 | 53.5 kg (C kapanışının MTOW'u) |
| 11.66 | 13 | L/D, lift-plus-cruise, olumsuz uç | 10 | 11.66 kW, C kapanışının askı gücü |
| 17 | 13 | L/D ≈ 17, rüzgâr tüneli, temiz | 10 | 17 m, kazanç yüksekken irtifa kaybı |
| 5.4 | 10 | 5.4 m irtifa kaybı, sonlu momentli model | 6 | 5.4 L/De, turboşaft tek rotorlu helikopter |
| 5.4 | 10 | 5.4 m irtifa kaybı | 13 | 5.4 %, eğim mekanizması kütle farkı üst ucu |
| 1.5 | 10 | %1,5 kuruluş sınaması sapması (MTOW^1.5 üssü Tur 104'te S10'a gitti) | 14 | 1.5 kW/kg, tezgâh ortalaması |
| 2.4 | 10 | ~2.4× kütle değişimi (sürükleme / palet) | 11 | 2.4–3.2 kurulu donanım oranı |
| 3.2 | 11 | 2.4–3.2 bu uçağın askı / motor oranı | 2 | 3.2, örnek araç askı/seyir güç oranı (geometrik terimler) |
| 3.5 | 14 | askı talebi tezgâh oranının 3,1–3,5 katı | 6 | 3,5 lb ft⁻², elektrikli quadrotorun disk yüklemesi |
| 22 | 14 | 22–25 % (yeniden kapanış tablosu, sürekli güç satırı) | 6 | +22 %, turboşaft quadrotora karşı fark (tablo) |
| 25 | 14 | 22–25 % (aynı satır) | 8 | 25°, firar kenarı ok açısı |
