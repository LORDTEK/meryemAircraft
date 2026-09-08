# Tur 3 — kütle bütçesi denetimi

Geçen turda üçünüz de aynı şeyi söylediniz: CFD'yi kapat, temel modeli
düzelt, kütle bütçesini bileşen düzeyine indir. Üçü de yapıldı. Bu
metin sonuçları veriyor.

**Ağırlık üçüncü bölümde.** İlk ikisi geçen turun kapanışı, kısa
tutuldu. **Kütle bütçesi yeni ve hiç denetlenmedi** — asıl bakılacak
yer orası.

---

# 1. CFD — verdiğim yorumu geri aldım

YZ1 ve YZ3, iki SST çözümünün basınç alanını karşılaştırmamı istedi.
Yapıldı (yeni koşu yok, iki yakınsamış alan duruyordu). Sonuç beni
çürüttü.

**Geri aldığım:** *"kararlı RANS iki ayrı durağan çözüme oturuyor."*

Neden yanlış:
- **Ayrılma topolojisi birebir aynı:** iki vakada da %0,02 ters akış
  alanı, aynı x aralığı (1,003–1,740 m).
- **Fark açıklık boyunca düzgün dağılmış** — sekiz bandın her biri
  farkın ~1/8'ini taşıyor. Gerçek bir ikinci çözüm dalı yerelleşirdi.

**Yerine geçen ölçüt.** Kesitler simetrik NACA 00xx, burulma yok,
α = 0 → **C_L sıfır olmak zorunda:**

| | C_L | Cp üst/alt asimetrisi |
|---|---|---|
| bl_C (SA-ısınmış) | +1,45e−03 | 0,0249 |
| bl_E (y⁺≈20'den taşınmış) | **+1,35e−04** | **0,0011** |

bl_E her ölçütte ~10 kat daha iyi. Asimetrinin indüklenen sürüklemesi
ihmal edilebilir (C_D'nin milyonda 9'u) — yani **sebep değil, belirti**;
ama hangi çözümün daha iyi koşullandığını söyleyen ölçüt o.

Böylece YZ1'in "üçüncü başlangıç gerekmez" ile YZ3'ün "gerekir"
ayrışması çözüldü: **üçüncü koşu yerine simetri ölçütü karar verdi.**
Aralık (0,01201–0,01253) yine yazılıyor; tek değer gerekirse bl_E,
artığa göre değil fiziğe göre seçiliyor.

**Soru 1:** Bu ölçüt meşru mu? Karşı argüman şu olabilir: ağ üst/alt
tam simetrik değilse iki vaka da eşit etkilenirdi, dolayısıyla farkın
kaynağı çözümdür — bu savunma yeterli mi?

---

# 2. Üç sözleşme — YZ3 haklıydı

YZ1 ve YZ5, "sabit yakıt kesrinde menzilin MTOW'dan bağımsız olması
Breguet'nin doğru özelliğidir" dedi. Doğru. YZ3 bunun **karşılaştırma
sözleşmesi** olarak sonucu ürettiğini gördü. Üçü de uygulandı; C'ye
"tilt seyirde sıfır ceza öder" hediyesi hâlâ dururken:

| C'nin A'ya göre menzili | sabit yakıt **kesri** | sabit yakıt **kütlesi** | sabit **MTOW**+faydalı |
|---|---|---|---|
| B — lift+cruise | −%14,4 | −%36,5 | −%72,6 |
| **C — tilt** | **+%12,0** | **+%0,2** | **−%19,1** |

L/D çarpanıyla çapraz tarandığında 12 kutunun yalnızca 3'ünde C önde,
üçü de birinci sütunda.

**YZ3'ün bir sayısını düzelttim:** sabit yakıt kütlesinde elle −%7
demiş; 60,3 kg'ı kullanmış ama o *sabit kesir* MTOW'u. Yakıt
sabitlenince C'nin MTOW'u 55,9'a kapanıyor → **+%0,2**. Sabit MTOW'da
YZ3 tam tutuyor: elle −%19, model −%19,1.

**Soru 2:** Üçünden hangisi makalenin **ana** tablosu olmalı? Yoksa üçü
de eşit ağırlıkta mı verilmeli?

---

# 3. KÜTLE BÜTÇESİ — asıl denetlenecek yer

Makale §6.2'nin kesirleri (%30 yapı / %16 tahrik / %4 pil / %8 aviyonik
/ %16 yakıt → **%26 faydalı yük**) aşağıdan yukarı yeniden kuruldu.
Kural: hiçbir kalem hedef kesirden geri çözülmedi.

## 3.1 İlk koşu bir uyarı verdi

İlk sürüm **%42,8** faydalı yük verdi. Kendi hedefini %60 aşan bir
bütçe iyi haber değil, **kalem eksikliği işaretidir.** Arandı, yedi
kategori eksik çıktı (3,4 kg): bağlantı elemanı/yapıştırıcı/boya,
erişim kapakları, motor yatağı-soğutma-egzoz, eş eksenli
göbek-mil-yatak, sinyal demeti, faydalı yük arayüzü, temas pedleri.
Ayrıca **belirsizlik payı** (kurunun %12'si) yoktu.

## 3.2 Nasıl hesaplandı

**Yapı.** Islak alan planformdan ve NACA 00xx kalınlık dağılımından
integralle: **4,14 m²** (planform 1,98 m²). Kabuk 1,5 kg/m² karbon
sandviç → 6,20 kg. İç yapı (kaburga, bölücü, yapıştırma) kabuğun %45'i.
**Uç çerçeveleri iniş halinden boyutlandı** — bu uçak onların üzerine
iniyor: 3 g dikey iniş, ağırlığın yarısı tek çerçeveden, post konsol
kirişi → 0,95 kg (ikisi, fittingler dahil).

**Kiriş.** n_ult = 5,25'te kök eğilme momenti **934 N·m**; 400 MPa'da,
yapısal derinlik 0,9 × kök kalınlığı → başlık alanı **10,7 mm²**,
kütlesi **41 gram** = MTOW'un binde 8'i.

**Tahrik.** Burun motoru **hover tepesine**, ICE **seyre** boyutlanıyor
— makalenin merkezi iddiası bütçede de böyle görünüyor: 2,73 kg
elektrik makinesi / 2,60 kg motor+jeneratör (4 kW/kg ve 1 kW/kg).

    m_kiris   = 2·2·ρ·[M_kök/(σ·h)]·(b/2)·0,35
    m_kabuk   = σ_alan · S_ıslak
    m_motor   = P_hover / (kW/kg)
    m_ICE     = P_seyir_derecelendirme / (kW/kg)

## 3.3 Sonuç — hafif hat kapanıyor

| grup | ölçülen | hedef |
|---|---|---|
| yapı | %23,8 | %30 |
| tahrik | %15,2 | %16 |
| pil | %3,6 | %4 |
| sistem + belirsizlik payı | %11,0 | %8 |
| yakıt | %16,0 | %16 |
| **faydalı yük (artan)** | **%30,4** | **%26** |

**+2,2 kg elde kalıyor.**

## 3.4 Ama payın tamamı tek bir sayıda

13 kg faydalı yük hangi değerde kapanmaz:

| varsayım | taban | kırılma | pay |
|---|---|---|---|
| **kabuk kg/m²** | 1,50 | **1,783** | **%19** |
| iç yapı / kabuk | 0,45 | 0,723 | %61 |
| belirsizlik payı | 0,12 | 0,219 | %82 |
| bağlantı oranı | 0,10 | 0,297 | %197 |
| motor kW/kg | 4,00 | 2,433 | %39 |
| ICE+jeneratör kW/kg | 1,00 | 0,623 | %38 |

Diğer her şey ciddi kötüleşebilir, tasarım kapanır. **Kabuk 1,78
kg/m²'yi geçerse kapanmaz.** Belirsizlik payı satırının okunuşu:
bütçeye **4,5 kg daha sayılmamış kütle** girebilir, fazlası giremez.

## 3.5 Ağır hat KAPANMIYOR — asıl açık soru

Kabuk kütlesi ~ ölçek², MTOW ~ ölçek³. Alan yoğunluğu sabit kalırsa
kabuk *kesri* 1/ölçek düşer — büyük uçakta kaplama incelmediği için bu
açıkça yanlış. Sabit kesir için alan yoğunluğu ~ ölçek¹ gerekir. Gerçek
üs arada ve **ölçülmedi:**

| üs | kabuk kg/m² | faydalı kg (hedef 260) |
|---|---|---|
| 0,00 | 1,50 | 359 ✓ |
| 0,25 | 2,03 | 313 ✓ |
| **0,467** | **2,64** | **260 — kırılma** |
| 0,50 | 2,74 | 251 ✗ |
| 1,00 | 5,02 | 52 ✗ |

## 3.6 Kendi şüphelerim — buralara bakın

1. **Yapı %23,8 çıktı, hedef %30 idi.** Bütçe kendi hedefinden hafif
   geliyor. İlk turda 7 kategori kaçırdığıma göre daha kaçırıyor
   olabilir miyim? Hangi kategoriyi göremiyorum?

2. **Kabuk 1,5 kg/m² savunulabilir mi?** 50 kg sınıfı, %25 kalın BWB,
   içinde bütün sistemleri barındıran, uç çerçevelerinden iniş yükü
   geçen bir yapı için. Bütün sonuç buna asılı.

3. **İç yapı = kabuğun %45'i** en zayıf halka. Bunun fiziksel bir
   temeli yok, pratikten alınmış bir orandır. Daha iyi bir kurma
   biçimi var mı?

4. **"Yapıyı mukavemet belirlemiyor"** çıkarımı doğru mu? Kiriş 41
   gram. Bu, bu ölçekte bilinen bir sonuç mu, yoksa bir şeyi mi
   atlıyorum (burulma kutusu, yerel yükler, flutter, uç çerçeve
   bağlantısındaki yığılma)?

5. **Ağır hattaki üs.** 0,467 eşiğinin altında mı üstünde mi olması
   beklenir? Bunu ölçmenin makul bir yolu var mı, yoksa "ölçülmedi,
   açık" diye mi bırakılmalı?

6. **Uç çerçevesi iniş halinden boyutlandı** ama tek yük hali o değil:
   pervane itkisi momenti, yer rüzgârı, yana yatık iniş. En kötü hal
   gerçekten dikey iniş mi?

---

# SORULAR

1. **Simetri ölçütü meşru mu?** (Bölüm 1)
2. **Üç sözleşmeden hangisi ana tablo olmalı?** (Bölüm 2)
3. **3.6'daki altı şüpheden hangisi gerçek hata?** Ve **listemde
   olmayan neyi görüyorsunuz?** — asıl aradığım bu.
4. **Sıradaki iş ne olmalı?** Elimde kalan: 6-DoF geçiş benzetimi
   (YZ3 "Q1 için şart", YZ5 "şart değil"), ağır hattaki kabuk üssünün
   ölçülmesi, makalenin yeniden okunması. Hangisi?
