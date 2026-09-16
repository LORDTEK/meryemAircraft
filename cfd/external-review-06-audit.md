# Metodolojik denetim — kritik hata var mı?

Aradığım şey nüans değil. **Sonucu geçersiz kılacak bir hata var mı?**
Varsa şimdi bulmanın tam zamanı.

Metni denetim riskine göre ağırlıklandırdım. CFD zinciri beş turdur
sizin denetiminizden geçti; **karşılaştırmalı temel modeli dün yazıldı,
bir kez doğrulandı, hiç denetlenmedi** ve sonucu makalenin iddiasını
kısmen zayıflatıyor. Ağırlık orada.

Ama önce, sizin istediğiniz sınamanın sonucu geldi ve **beklediğim gibi
çıkmadı**. Onu başa alıyorum.

---

# 0. BAŞLANGIÇ BAĞIMSIZLIĞI ÇÜRÜTÜLDÜ

YZ1'in istediği sınama buydu: k-ω SST y⁺≈1 çözümü, farklı bir
başlangıçtan yeniden üretilebiliyor mu? Koşu bitti. **Hayır.**

| koşu | başlangıç | C_D | basınç | viskoz | son artık |
|---|---|---|---|---|---|
| bl_C | SA çözümünden ısıtılmış | 0,012532 | 0,003856 | 0,008676 | 7,1e−07 |
| bl_E | y⁺≈20 SST çözümünden taşınmış | **0,012011** | 0,003362 | 0,008649 | **1,0e−07** |

İkisi de 5000 adım koştu, ikisi de hiç `bounding omega` vermedi, ikisi de
son 500 adımda durağan. bl_E üç koşunun **en iyi artığına** ulaştı — yani
"biri yakınsamamış" denemiyor.

**Fark %4,34 ve tamamı basınçta:** basınç %12,8 ayrışıyor, viskoz
bileşen binde üç içinde **aynı**. Aynı viskoz sürükleme + ayrışan basınç
sürüklemesi → uyuşmazlık sınır tabakasında değil, ayrılma/iz bölgesinde.

Vakaların başlangıç dışında aynı olduğu doğrulandı: `polyMesh` aynı inode
(birebir aynı ağ dosyası), aynı `transportProperties`, aynı
`turbulenceProperties`, beş alanın `boundaryField` blokları aynı.
Başlangıç alanları ise gerçekten farklı: ν_t tepe değeri 10,8×, k tepe
değeri 5,9× ayrı.

**Okumam:** kararlı RANS burada birden fazla durağan çözüme oturuyor.
Ayrılmalı akışta bilinmeyen bir durum değil, ama **sayının tekliğini
ortadan kaldırıyor**. Makaleye bu şekilde yazdım: SST y⁺≈1 için tek
değer değil, **0,01201–0,01253** aralığı; toplam 0,0203–0,0230; varsayılan
0,0248 hâlâ hepsinin üstünde. Aralık "ölçülmüş yayılım" olarak
etiketlendi — üçüncü bir başlangıcın içeride kalacağının garantisi yok.

**Size sorum:** bu okuma doğru mu, yoksa gözden kaçırdığım daha basit bir
açıklama mı var (ör. taşıma yönteminin kendisi — `mapFields` bu kurulumda
kırık olduğu için en yakın komşu ataması kullandım; duvar yakınında bu
kaba bir işlem)? Bu ihtimali düşündüm ama viskoz bileşenin binde üç
içinde aynı çıkması ona karşı bir delil gibi duruyor: taşıma hatası
duvarda olsaydı ilk bozacağı şey viskoz sürükleme olurdu.

---

# A. KARŞILAŞTIRMALI TEMEL (asıl denetlenecek yer)

## Ne yapıyor

Aynı görevi üç mimariyle boyutlandırıp üç faturayı (kütle, sürükleme,
güç sistemi) sayısallaştırıyor.

| | mimari |
|---|---|
| A | kuyruk üstü, tamponlu seri hibrit (makalenin konfigürasyonu) |
| B | lift + cruise (iki tahrik grubu) |
| C | tilt (tek grup, eğme mekanizması) |

## Denklemler

    MTOW    = m_faydalı / (1 − f_boş − f_yakıt)
    P_hover = W^1.5 / (FoM · √(2ρA))
    P_seyir = W·V / (L/D) / η_seyir
    R       = f_yakıt · E* · η_zincir · (L/D) / g

Tahrik kütlesi **kurulu güce bağlı** (aksi hâlde Bill 3 kütle sütununda
görünmüyor), bu yüzden çözüm yinelemeli:

    f_tahrik = 0,108 + (P_kurulu/1000) / 1,0 / MTOW      [kW/kg, kg]
    MTOW_yeni = m_faydalı / (1 − f_boş − f_yakıt)         → sabit nokta

## Kalibrasyon — makalenin kendi tasarımından geri çözüldü

| büyüklük | değer | nereden |
|---|---|---|
| FoM (hover) | 0,599 | P_hover = 10,9 kW, MTOW 50 kg |
| η_seyir | 0,721 | P_el = 1,7 kW, L/D 12 |
| motor payı | 1,53 × | motor 2,6 kW / seyir 1,7 kW |
| özgül güç | 1,0 kW/kg | varsayım (küçük içten yanmalı + jeneratör) |
| f_tahrik sabit | 0,108 | 0,16 − 2,6/1,0/50 |

## Doğrulama

Model önce makalenin **kendi** tasarımını üretmeli:

| | model | makale | fark |
|---|---|---|---|
| MTOW | 50,008 kg | 50,0 | %0,0 |
| f_tahrik | 0,160 | 0,160 | %0,0 |
| motor | 2,603 kW | 2,6 | %0,1 |
| L/D | 12,00 | 12,0 | %0,0 |
| menzil | 1600 km | 1598 | %0,1 |
| P_hover | 10,90 kW | 10,9 | %0,0 |

## Mimari farkları nereden geliyor

**Ortak (üçünde de aynı):** görev (13 kg faydalı, 30 m/s), kanat
yüklemesi 25,3 kg/m², disk yüklemesi 44,2 kg/m², f_gövde 0,30,
f_aviyonik 0,08, f_yakıt 0,16, f_tampon 0,04, enerji zinciri.

| fark | değer | kaynak |
|---|---|---|
| A'nın L/D çarpanı | 1/1,12 | makale §5.2: uç çerçeveleri seyir sürüklemesinin %12'si |
| B'nin L/D çarpanı | 13/17 = 0,765 | makale §3.3, **rüzgâr tüneli**: temiz 17 → hover donanımı takılı 13 |
| C'nin L/D çarpanı | 1,0 | seyirde açık hover donanımı yok — **tilt'in lehine, kasten** |
| B'nin ek kütlesi | parametre | ölçüm yok; tarandı |
| C'nin eğme mekanizması | 0,05 | §3.5'teki geri çekme mekanizmasının %5'i — **mertebe çapası, eşdeğerlik iddiası değil** |

## Ağır hat (1000 kg) — yeniden ayar YOK

Model hafif hatta kalibre edildi; ağır hat, tek bir sayı bile
değiştirilmeden öngörü olarak koşuldu (tek istisna: motor payı, §6.3'ün
kendi sayılarından 1,385):

| | model | makale | fark |
|---|---|---|---|
| MTOW | 1013,4 kg | 1000 | +%1,3 |
| L/D | 13,60 | 13,6 | %0,0 |
| P_hover | 219,5 kW | 216,2 | +%1,5 |
| motor | 56,2 kW | 54,3 | +%3,5 |
| menzil | 1813 km | 1814 | −%0,1 |

**Bulduğum tutarsızlık:** motor derecelendirme payı hafif hatta 1,529,
ağır hatta 1,385 — %10,4 fark, makalede **hiçbir yerde
gerekçelendirilmemiş**. Model bunu ancak elle ayrı verilerek
kapatabiliyor. Bu makalenin kendi içinde bir açık mı, yoksa ölçek
etkisiyle gerekçelendirilebilir mi?

## Sonuç

**Düzey 1** — üçünde de tamponlu seri hibrit (A'nın Bill 3 avantajı
kasten verildi):

| | f_boş | MTOW | L/D | menzil |
|---|---|---|---|---|
| A | 0,580 | **50,0** | 12,00 | 1600 |
| B | 0,689 | 86,0 | 10,28 | 1370 |
| C | 0,624 | 60,3 | **13,44** | **1792** |

Ağır hatta aynı sıralama: A 1013 kg / 1813 km, B 1765 kg / 1553 km,
C 1224 kg / **2031 km**. Yani tilt'in üstünlüğü ölçekten bağımsız —
kalibrasyon artığı değil, modelin yapısal sonucu.

**Düzey 2** — mimariye özgü güç sistemi (motor hover'a boyutlanıyor):
B hiç kapanmıyor (kütle sarmalı ıraksıyor); C'nin MTOW'u 294,6 kg,
motoru 64,2 kg (A'nın 2,6 kg'ına karşı).

## Kendi şüphelerim — buralara bakın

1. **Tilt menzilde A'yı %12 geçiyor.** Makalenin iddiasını zayıflatıyor.
   Sebebi C'ye verdiğim L/D çarpanı 1,0. Bu doğru mu, yoksa tilt
   nasel'leri/mekanizması seyirde bir bedel öder mi?

2. **Sabit yakıt kesrinde menzil kütleden bağımsız** (R formülünde MTOW
   yok). Yani ek kütle menzili değil faydalı yük *payını* değiştiriyor.
   Bu doğru bir özellik mi, yoksa formülasyon hatası mı? Sabit yakıt
   **kütlesi** ile kurmak daha mı doğru olurdu?

3. **Kanat ve disk yüklemesini üç mimaride de sabit tuttum.** Gerçekte
   her mimari kendi optimumuna boyutlanır. Bu, karşılaştırmayı
   bozuyor mu?

4. **f_gövde = 0,30 üçünde de aynı.** Ama §3.2'nin alıntıladığı NASA
   incelemesi, dağıtılmış kaldırmanın *yapıyı* da ağırlaştırdığını
   söylüyor ("to safely transmit power to the extremities... obvious
   weight penalty"). B'nin gövde kesri daha yüksek olmalı mıydı?

5. **Özgül güç 1,0 kW/kg** tek uydurulmuş sayı. Düzey 2'de sonucu
   belirleyen o. Ne kadar yanlış olabilir?

6. **Düzey 2 adil mi?** Gerçek bir Lift+Cruise motoru hover'a
   boyutlamaz, kaldırmayı bataryayla yapar. O hâlde Düzey 2 bir
   korkuluk mu, yoksa "tampon herkese açık, o hâlde Düzey 1 adil"
   çıkarımı mı doğru?

---

# B. CFD ZİNCİRİ (sıkıştırılmış — beş turdur denetlendi)

## Sayılar

| | SA | k-ω SST |
|---|---|---|
| y⁺≈20 | 0,014521 | 0,013440 |
| y⁺≈1 | 0,014750 | **0,01201–0,01253** |
| duvar etkisi | +1,58% | −6,7 … −10,6% |

Model açılımı y⁺≈1'de **%18**, başlangıç açılımı **%4,3** (bölüm 0).
Ortalama alınmıyor; değerler ayrı veriliyor, aralıklar "spread" diye
etiketleniyor.

Kontrol koşusu: `blended false` → 0,012530 (%0,016 fark, önemsiz —
hipotez iki yönden de çürütüldü).

## Kritik yöntem kararları

| karar | gerekçe |
|---|---|
| `gmshToFoam -keepOrientation` | varsayılan sezgi ince hücrelerde 31 868 negatif hücre üretiyordu |
| `Aref` = ağdan ölçülen izdüşüm alanı (0,989612 m²) | Σ\|Sf_y\|/2; `planform.py` ile %0,037 uyum |
| kuvvet duvar gradyanından | `forceCoeffs` bu kurulumda kırık; 1. ve 2. mertebe karşılaştırıldı, fark %0,06 |
| y⁺ **alan ağırlıklı** | yüz sayısına göre ortalama uç kapağın etkisiyle 11 622 veriyordu |
| ısınmış başlangıç | tek biçimli alan yerel k adası üretip 2170 civarında çöküyor |
| ısınmış alan formülü | ω = max(ν_t/(√β\*κ²y²), 6ν/(β₁y²), ω∞), k = ν_t·ω_turb — log-tabaka dengesinden; S hesabı gerekmiyor |
| α = 0 = C_L = 0 | kesitler simetrik NACA 00xx, burulma yok; **ölçüldü**: C_L = −0,022, C_Di karşılığı C_D'nin %0,23'ü |

## Bilinen sınırlar

- k-ω y⁺=1 çözümü **ancak ısınmış başlangıçla** elde edilebiliyor ve
  başlangıç bağımsızlığı **çürütüldü** (bölüm 0).
- Doğal geçiş **doğrulanamadı**: `kOmegaSSTLM` T3A'da çalışıyor
  (türbülanslı bölge ±%5, geçiş ~%25 erken) ama düşük-Tu rejiminde
  eğitim ağı ölçeklenerek kullanılamıyor (hücum kenarı k üretimi,
  serbest akım çürümesi). Geçişli C_D0 iddiası **yok**.
- Deneysel doğrulama yok.

---

# SORULAR

1. **A bölümündeki altı şüpheden hangisi gerçek bir hata?** Hepsine
   değil, sonucu geçersiz kılacak olana bakın.
2. **Gördüğünüz ama benim listemde olmayan bir hata var mı?** Asıl
   aradığım bu.
3. **Bölüm 0'daki okuma doğru mu?** Çoklu çözüm mü, yoksa taşıma
   yönteminin artığı mı? Aralığı olduğu gibi yayımlamak doğru davranış
   mı, yoksa üçüncü bir başlangıç mı denenmeli?
4. **Sonraki aşama ne olmalı?** Elimde kalanlar: temel modelin makaleye
   bölüm olarak yazılması, başlığın "Eliminating" → "Reducing"
   değişimi, 6-DoF geçiş benzetimi, kütle bütçesinin bileşen düzeyinde
   kapatılması. Sıra ne olmalı — ve hangisi Q1 için **gerçekten**
   gerekli? (CFD dondurulmuş durumda; sizin tavsiyenizle.)
