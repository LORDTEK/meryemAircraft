# NASA sayıları — **KAPANDI.** Birinci elden okundu.

**Durum: ÇÖZÜLDÜ, 2026-09-20.** Yazar beş PDF'i depoya yükledi (`6adbf8e`), `poppler-utils`
kuruldu, tablolar birinci elden okundu.

**Sonuç: makalemizin sayıları DOĞRU. Kimse yanlış okumamış — üç farklı belge okumuşlar.**

---

## 1. Neden çelişiyorlardı

Dört okuyucu dört sayı kümesi verdi. Hepsi **kendi belgesi için doğru.**

| Belge | Yıl | Quadrotor TS | Lift+Cruise TE | Tiltwing TE |
|---|---|---|---|---|
| Silva ve ark., AIAA Aviation | 2018 | 4,9 / **3 735 lb** | **7,2 / 6 013 lb** | *yok* |
| **Johnson & Silva, *The Aeronautical Journal*, Tablo 3** | **2022** | **4,9 / 3 678 lb** | **8,5 / 7 271 lb** | **8,6 / 6 584 lb** |
| Pollard ve ark., multi-tiltrotor sunumu | 2023 | 4,9 / 3 735 lb | 7,8 / 7 651 lb | 8,5 / 6 423 lb |

- **Grok** 2018 AIAA'yı açtı ve **birebir doğru** aktardı (3 735 / 6 013 / 8 210, L/D_e 4,9 /
  7,2 / 8,5; tiltwing sütunu yok). Doğrulandı: o tabloda **8,5 gerçekten elektrikli L+C'ye,
  8 210 lb'a ait.**
- **ChatGPT ve Qwen** 2022 makalesini açtı ve **birebir doğru** aktardı.
- **DeepSeek** 2023 sunumunu açtı ve **birebir doğru** aktardı.

**Grok'un tek yanlışı çıkarımıydı:** *"Makalede duran çift bu tablo değil."* Doğru — ama
bizim makalemiz 2018'i değil **2022'yi** ([22]) alıntılıyor, ve orada çift **tam olarak var.**

**Kaynak kuralı işe yaradı.** Herkes belgesini adlandırdığı anda çelişki kendiliğinden çözüldü.

## 2. Bizim sayılarımız — doğrulandı

`paper/paper-v7.md` §3.1'deki her sayı **Johnson & Silva 2022, Tablo 3'te birebir var:**

| | Makalemiz | Tablo 3 | |
|---|---|---|---|
| Quadrotor TS, L/D_e | 4,9 | **4,9** | ✓ |
| Quadrotor TS, DGW | 3 678 lb | **3 678 lb** | ✓ |
| Lift+Cruise TE, L/D_e | 8,5 | **8,5** | ✓ |
| Lift+Cruise TE, DGW | 7 271 lb | **7 271 lb** | ✓ |
| Tiltwing TE, L/D_e | 8,6 | **8,6** | ✓ |
| Görev | 1 200 lb / 75 nm | **1 200 lb / 75 nm** | ✓ |

**Hiçbir düzeltme gerekmiyor.** Grok'un *"bir RVLT sürümü"* şüphesi haklıydı ama bizim
sürümümüz doğru sürümdü.

## 3. Eksik hücre doldu

**Tiltwing TE: L/D_e 8,6, DGW 6 584 lb.** Aynı tablo, aynı atıf, aynı görev.

**Adım 4'ün yalıtma testi artık yapılabilir:**

| | L/D_e | DGW | adanmış kaldırma |
|---|---:|---:|---|
| Lift+Cruise, turbo-elektrik | 8,5 | 7 271 lb | **var** — 8 kaldırma motoru + 1 seyir motoru |
| Tiltwing, turbo-elektrik | 8,6 | 6 584 lb | **yok** — 8 eğilen proprotor |

İkisi de kanatlı, ikisi de turbo-elektrik, aynı görev. **Tiltwing %1,2 daha verimli ve
%9,4 daha hafif.** Tahrik ve kanat sabit; değişen tek şey adanmış kaldırma grubu. Grok'un
istediği temiz kontrol budur.

**Ve ağırlık dökümü aktarımı gösteriyor:**

| | yapı | tahrik | boş ağırlık |
|---|---:|---:|---:|
| Lift+Cruise TE | 2 670 lb | 1 772 lb | 5 809 lb |
| Tiltwing TE | 1 954 lb | 1 918 lb | 5 130 lb |
| **fark** | **L+C +716 lb** | **Tiltwing +146 lb** | **L+C +679 lb** |

Lift+cruise yapıda ödüyor; tiltwing tahrikte biraz geri veriyor. Net 679 lb.

## 4. NASA'nın kendi cümlesi — Fatura 1'i kendi sözleriyle söylüyor

Tablo 3'ün hemen üstünde, s. 70:

> *"The high cruise efficiency of the lift+cruise type reduces the battery weight compared to
> the quadrotor, **but not enough to counter the increase in structure and propulsion weight**,
> so the all-electric lift+cruise aircraft is the heaviest design."*

**Bu, Adım 4'ün öngörüsünün ikinci yarısının kaynağın kendi ağzından söylenmiş hâlidir:**
verim kredisi gerçek ve ağırlık cezasını karşılamıyor. Çıkarım yapmamıza gerek yok.

## 5. "Dört VTOL mimarisi" YANLIŞ — ChatGPT haklı

Makalenin kendi cümlesi, s. 70:

> *"All aircraft (**five aircraft types so far**, two propulsion architectures for most, plus
> numerous excursions) were designed to the same mission."*

Beş tip: QSMR, side-by-side, quadrotor, lift+cruise, tiltwing. Tablo 3'te **dokuz tasarım.**
§2.2'nin *"four VTOL architectures"*ı düzeltilecek.

## 6. 2023 revizyonu — sağlamlık kontrolü olarak

Multi-tiltrotor sunumu aynı araçları yeniden boyutlandırmış ve dipnotu şunu söylüyor:
*"Lift+Cruise TE: updated assumptions **to maintain consistency with Tiltwing**."* Yani 2023
çifti daha özenle eşleştirilmiş bir karşılaştırma.

| | 2022 | 2023 |
|---|---|---|
| Tiltwing TE | 8,6 / 6 584 lb | 8,5 / 6 423 lb |
| Lift+Cruise TE | 8,5 / 7 271 lb | 7,8 / 7 651 lb |
| **tiltwing avantajı** | %1,2 verim, **%9,4 hafif** | %9,0 verim, **%16,0 hafif** |

**Öngörü iki sürümde de tutuyor, 2023'te daha güçlü.** Ama 2023 bir sunum slaytı, hakemli
makale değil ve *"Version 0"* diyor. **Gövdede 2022 kullanılacak**, 2023 bir sağlamlık notu
olarak anılabilir.

## 7. Depodaki belgeler

`references/1521_Johnson & Silva_122721.pdf` — **2022, Tablo 3, s. 70. Ana kaynak.**
`references/div-class-title-...-div.pdf` — aynı makalenin Cambridge kopyası.
`references/20180006683.pdf` — Silva ve ark. 2018 AIAA, Tablo 3 s. 11–12.
`references/202305-Multi-Tiltrotor-Publication.pdf` — Pollard ve ark. 2023 sunumu, s. 19.
`references/NASA-TM-20210017971.pdf` — Whiteside ve ark., tiltwing tasarım raporu.
