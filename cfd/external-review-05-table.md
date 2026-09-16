# Dış görüş — Tur 5: tablo tamamlandı, sonuç beklenmedik

Önceki turda "yerelleşmiş k kaçışı, sebebi ölçüldü, çaresi yok" diye
sormuştum. İkiniz de aynı deneyi ilk sıraya koydunuz: **SA çözümünden
ısınmış başlangıç.** Yapıldı, çalıştı, tablo tamamlandı — ve sonuç
beklediğim şey değil.

---

## Giriş — ne yapıldı

Formülümü ikiniz de düzelttiniz ve düzeltmeler farklıydı:

- **YZ1:** `k = ν_t·ω` SST'nin kendi bağıntısını sağlamıyor; SST'nin
  ν_t = a₁k/max(a₁ω, S·F₂) ilişkisi tersine çevrilmeli.
- **YZ5:** duvara yakın `ω = S/√β*` geçersiz; viskoz ω ile karıştırılmalı,
  ve `nuTilda` değil **`nut`** kullanılmalı.

İkisini birleştirdim ve S hesabını tamamen atlayan bir yol buldum.
Logaritmik tabaka dengesinden (ν_t = κ u_τ y, k = u_τ²/√β*):

    ω_turb = ν_t / (√β* · κ² · y²)
    ω      = max(ω_turb, 6ν/(β₁y²), ω_∞)
    k      = max(ν_t · ω_turb, k_∞)

Denetim: ν_t = κ u_τ y konunca k = u_τ²/√β* çıkıyor, yani doğru
log-tabaka değeri. Duvar mesafesi `scipy` cKDTree ile duvar yüz
merkezlerinden. U ve p de SA'nın 5000. adımından alındı.

Üretilen alanın denetimi:

| | üretilen | beklenen |
|---|---|---|
| sınır tabaka k (ortanca) | 0,00189 | ~0,005 |
| sınır tabaka k (%95) | 0,00425 | ~0,005 |
| genel en büyük k | 0,602 | (çöken koşuda 8,2) |

**Tek değişen başlangıç alanıydı.** Ağ, şemalar, sınır koşulları,
gevşetme, `relTol` — hepsi aynı.

## Sonuç: çalıştı

| | tek biçimli başlangıç | ısınmış başlangıç |
|---|---|---|
| ulaşılan adım | 2169 / 2186'da `SIGFPE` | **5000, çökme yok** |
| `bounding omega` | çok | **hiç** |
| k_max sonu | 3,4e5 → patlama | 0,0197 (tekdüze düşerek) |
| Ux artığı | 1,1e−04 (2000'de) | **7,1e−07** (5000'de) |

Kuvvetler de oturmuş:

| adım | C_D | C_L | basınç | viskoz |
|---|---|---|---|---|
| 4000 | 0,012588 | −0,00178 | 0,003909 | 0,008679 |
| 4500 | 0,012559 | +0,00063 | 0,003882 | 0,008677 |
| 5000 | **0,012532** | +0,00145 | 0,003856 | 0,008676 |

500 adımda %0,22 değişim, viskoz bileşen tamamen sabit.

---

## Gelişme — ve beklemediğim şey

Tablo tamamlanınca çıkan:

| | SA | k-ω SST | model farkı |
|---|---|---|---|
| y⁺≈20 | 0,0145209 | 0,0134376 | **+8,06%** |
| y⁺≈1 | 0,0147498 | **0,0125320** | **+17,70%** |
| **duvar etkisi** | **+1,58%** | **−6,74%** | |

**İki model duvar çözümlendiğinde ters yönlere gidiyor.** SA'nın
sürüklemesi artıyor, k-ω'nınki azalıyor. Model farkı iki katına çıkıyor.

Bu, kayıtta duran ifadeyi çürüttü:

> "C_D0 = 0,0141 ± ~%5, iki modelin duvar çözümlü/düşük y⁺ değerlerinin
> ortası (SA 0,01475; k-ω y⁺≈20 0,01344)."

O ortalama **iki farklı duvar çözünürlüğünü** eşliyordu — YZ5'in "iki
tavanın karışması" uyarısı tam buydu. İkisi de y⁺≈1'de olunca:

| | |
|---|---|
| orta nokta | **0,013641** |
| yarı-açılım | **±%8,13** |
| eski 0,0141 | yeni ortanın %3,4 üstünde |

Sayı az değişiyor, **bant %5'ten %8'e genişliyor.**

## Makaleye işlendi

§6.6 ve 8. bölüm güncellendi: 0,0141 ± %5 → 0,0136 ± %8; şerit tahminine
göre %9 → %6; toplam 0,0224 → 0,0219; varsayıma marj %11 → %13.

Üç ifade de düzeltildi:

1. **"Duvar duyarlılığı doyuma ulaşıyor"** kaldırıldı — iki model ters
   yönlere gidiyor. Eski %5'in nasıl yanlış kurulduğu açıkça yazıldı.
2. **"O birleşim yakınsamadı"** düzeltildi — artık yakınsıyor. Yerine
   `kOmegaSSTLM`'in T3A'da çalıştığı (türbülanslı bölgede birkaç yüzde,
   geçiş ~%25 erken) ama düşük-Tu rejiminde doğrulanamadığı yazıldı.
3. **Isınmış başlangıç şartı** gizlenmedi: *"yakınsamış kararlı çözüm
   başlangıç koşulundan bağımsız olmalıdır ve iki çözüm incelenen her
   tanıda uyuşuyor; ama bu bağımsızlık burada gösterilemedi, çünkü
   bağımsız başlangıç hiç yakınsamıyor."*

Makalenin doğrulama betiği (40 kontrol) sapmasız geçti.

## Şu an dönen

YZ5'in hatırlattığı **`blended false`** koşusu — Tur 2'de tasarlanıp hiç
yapılmayan tek değişkenli test, artık ısınmış başlangıç üzerinde.
`bl_C` ile arasında tek satır fark var.

(Bir işletim notu: ilk denemede koşu 19. adımda sessizce öldü — çökme
mesajı yok, disk ve bellek bol, sayılar sağlıklıydı. Süreç ağacı
oturum temizliğine takılmıştı. İzlenen arka plan mekanizmasıyla yeniden
başlatıldı.)

---

## Sorular

### 1. En önemlisi: %17,7'lik ayrımı nasıl raporlamalı?

İki model duvar çözümlendiğinde ters yönlere gidiyor ve %17,7 ayrılıyor.
Ben ortalamalarını alıp ±%8,13 dedim. **Bu doğru mu?**

Aklımdaki itiraz: %17,7 ayrılan iki sayının ortalaması, ikisinin de
olmadığı bir yerde duruyor. "Ortalama ± yarı-açılım" ifadesi, sanki
gerçek değer ortada bir yerdeymiş gibi okunuyor. Alternatif, iki değeri
ayrı ayrı verip **hiç ortalamamak**:

> "Duvar çözümlü çözüm iki türbülans modeliyle 0,01253 ve 0,01475
> veriyor; aradaki %17,7 model-biçim belirsizliğidir."

Hangisi daha savunulabilir?

### 2. y⁺=1'de hangi modele güvenmeli?

Duvar çözümlendiğinde SA yukarı, k-ω aşağı gidiyor. Literatürde bu ayrım
biliniyor mu, ve **bir tanesini tercih etmek için fiziksel bir gerekçe
var mı**? Yoksa "ikisi de eşit derecede meşru, aradaki fark belirsizliğin
kendisidir" mi demeli?

### 3. Isınmış başlangıç bağımlılığı ne kadar ciddi bir zayıflık?

Yakınsamış kararlı çözüm başlangıçtan bağımsız olmalı. Burada o
bağımsızlık **gösterilemedi** çünkü bağımsız başlangıç yakınsamıyor.
Elimde şu var: iki çözüm (SA ve ısınmış k-ω) incelenen her tanıda —
artık, k_max, y⁺, C_L, kuvvet bileşenleri — tutarlı. Ama bu bir kanıt
değil.

Hakem bunu ne kadar ciddiye alır? Bağımsızlığı göstermenin başka bir
yolu var mı (örneğin farklı bir ısınmış başlangıçtan, mesela k-ω'nın
y⁺≈20 çözümünden başlatmak)?

### 4. Hot spot mekanizması — hâlâ çıkarmalı mıyım?

YZ1 haklı olarak "artık k_max değil, **k'yı hangi terim büyüttü**"
demişti: S, Ω, F₂, P_k, sınırlayıcı sonrası P̃_k, β\*kω. Çöken koşunun
2100. adım alanı hâlâ diskte.

Ama hot spot artık yok. Bu ölçüm hâlâ değerli mi, yoksa **çözülmüş bir
sorunun otopsisi** mi? Makaleye girmeyecekse yapmaya değer mi?

### 5. Ve asıl soru: CFD'yi burada bırakmalı mıyım?

Bu, ilk turdaki eleştirinize dönüyor. **Beş turdur CFD yapıyorum.**
Bu turda kazanılan, C_D0'ın %3,4 değişmesi ve bandının %5'ten %8'e
genişlemesi. Bu arada Tur 1'de ikinizin de "makalenin merkezi zayıflığı"
dediği şey **hâlâ yapılmadı**: aynı denklemlerle boyutlandırılmış
karşılaştırmalı bir temel (Lift+Cruise / tilt). Başlık da hâlâ
"Eliminating" diyor, oysa kendi bulgumuz ~%12 gövde sürüklemesi.

Dürüst sorum: **yanlış ekseni optimize etmeye devam mı ediyorum?**
CFD'yi burada dondurup karşılaştırmalı temele geçmek mi doğru — yoksa
`blended false` ve bir-iki koşu daha tamamlanmadan tablo eksik mi kalır?

Sizden istediğim, "ikisi de yapılsın" değil, **hangisinin önce
geleceği.**
