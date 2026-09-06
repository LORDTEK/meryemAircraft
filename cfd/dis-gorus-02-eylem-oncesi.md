# Dış görüş — Tur 2: eylem öncesi mutabakat

Bu metin, iki adım atmadan **önce** dış görüş almak için yazıldı. Kendi
kendine yeter; okuyanın önceki turu görmüş olması gerekmez. Amaç onay
almak değil, **itiraz varsa koşuyu başlatmadan duymak**.

---

## Giriş — bağlam ve önceki turun sonucu

Kuyruk üstü oturan, karma kanat-gövde (BWB) gövdeli bir VTOL İHA
konfigürasyon çalışması. Çıktı bir bilimsel makale; CFD makalenin ana
katkısı değil, mimari iddiayı destekleyen kısım.

Açık kalan tek büyük belirsizlik sıfır-kaldırma sürüklemesi:

| Kaynak | C_D0 |
|---|---|
| Analitik, temiz yüzey + geçişli sınır tabaka | 0.0073 |
| 3-B CFD, **tam türbülanslı** k-ω SST, GCI'li, ±%5 | 0.0141 |

Geçiş (transition) modelli bir koşu bu aralığı daraltırdı. Yapamadım:
OpenFOAM v1912'nin tek geçiş modeli `kOmegaSSTLM` ve hem y⁺≈1 hem bir ω
denklemi istiyor; k-ω SST bu ağda y⁺≈1'de beş denemede de ıraksadı
(61, 154, 68, 6, 54 adım; ikisinde `bounding omega`). Spalart–Allmaras
**aynı ağda** y⁺≈1'de sorunsuz koşuyor ama OpenFOAM v1912'de SA tabanlı
geçiş modeli yok.

Önceki turda iki bağımsız görüş aldım. İkisi de aynı sonuca vardı ve
ikna oldum:

> Özel türbülans modeli (Medida γ-Re_θ-SA) **yazma**. Önce sabit geçiş
> konumu taraması yap. Konfigürasyon makalesi için tam geçiş modeli şart
> değil; dürüst bir aralık daha savunulabilir.

O turdan iki düzeltme de not edildi:

1. **6 mı 60 mı.** OpenFOAM v1912 `omegaWallFunctionFvPatchScalarField.C:220`
   `omegaVis = 6ν/(β₁y²)`, β₁ = 0.075 kullanıyor — bu Wilcox'un y→0
   asimptotik çözümü. Menter'in *pratik duvar sınır koşulu* olan
   60ν/(β₁Δy₁²) ise kasten ~10× daha sert, farklı bir büyüklük. İkisi
   karıştırılmamalı; ben önceki metinde ikincisini kastetmiştim ama
   ayrımı yazmamıştım.
2. **`nNonOrthogonalCorrectors`.** Bir görüş "belirtmiyorsun" dedi;
   belirtiyorum, değeri 2 (`cfd/naca/kur.py:279`).

**Eksik yakalandı ve kabul edildi:** doğrulama planım T3A/T3B → S809/E387
idi. T3A/T3B **yüksek serbest akım türbülansı** (bypass) vakaları; bizim
seyir koşulumuz Tu ≪ %1, yani **doğal geçiş** rejimi. Doğal geçiş vakası
(Schubauer–Klebanoff veya T3A-) eklenmeden bir geçiş modeli doğrulanmış
sayılmaz. Bu benim planımın gerçek açığıydı.

---

## Gelişme — kaynak kodunda bulduğum yeni şey

Önceki turdan sonra `omegaWallFunction`'ın OpenFOAM v1912 kaynağını
satır satır okudum. İki şey buldum. Her ikisi de daha önce hiç
denemediğim bir ayarı işaret ediyor.

### Bulgu 1: OpenFOAM'ın kendi yorumu varsayılanı reddediyor

`omegaWallFunctionFvPatchScalarField.C`, satır 222-228:

> "Switching between the laminar sub-layer and the log-region rather than
> blending has been found to provide more accurate results over a range of
> near-wall y+. **For backward-compatibility the blending method is
> provided as an option.**"

Ama `blended_` varsayılan değeri `true` (satır 273 ve 310). Yani kodun
kendi yorumunun "daha az doğru" dediği mod, geriye uyumluluk için
varsayılan bırakılmış. Benim beş denememin beşi de bu varsayılanla koştu.

### Bulgu 2: Farkın mekanizması — duvar hücresindeki üretim terimi

İki mod yalnızca ω değerinde ayrılmıyor. Duvar hücresine eklenen
türbülans kinetik enerji üretimi G de değişiyor (satır 233-259):

```
bool includeG = true;
if (blended_) {
    omega0[celli] += w*sqrt(sqr(omegaVis) + sqr(omegaLog));
} else {
    if (nutw.yPlusLam() < yPlus) { omega0[celli] += w*omegaLog; }
    else                        { omega0[celli] += w*omegaVis;
                                  includeG = false; }
}
if (includeG) {
    G0[celli] += w*(nutw + nuw)*magGradUw*Cmu25*sqrt(k[celli])
                 /(nutw.kappa()*y[facei]);
}
```

Yani:

- **`blended true` (varsayılan):** G duvar hücresine **her zaman**
  ekleniyor, üstelik **logaritmik tabaka** ifadesiyle.
- **`blended false`:** y⁺ < y⁺_lam (≈11.5) ise `includeG = false`,
  G eklenmiyor.

Kritik nokta: eklenen ifade **1/y ile ölçekleniyor**. y⁺≈20'den y⁺≈1'e
inerken duvar hücresi yüksekliğini yaklaşık 20 kat küçülttüm, dolayısıyla
bu terim yaklaşık 20 kat büyüdü — ve viskoz alt tabakada, log-yasası
ifadesinin geçerli olmadığı bir yerde uygulanıyor.

### Hipotezim

y⁺≈1'de `blended true` modu, viskoz alt tabakadaki duvar hücresine
geçersiz bir log-tabaka üretim terimi enjekte ediyor; bu terim 1/y ile
büyüyor; k şişiyor; ω denklemi bunu takip edemiyor ve `bounding omega`
ile ıraksıyor.

Bu hipotez şunu da açıklar: **SA neden aynı ağda sorunsuz koşuyor.**
SA'da k denklemi yok, dolayısıyla bu üretim terimi de yok.

Ve bu hipotez doğruysa çare **tek satırlık bir sözlük değişikliği:**
`blended false;`

### Kendi hipotezime karşı itirazlarım

Dürüst olmak için, bunun yanlış olabileceği üç yol:

1. **Ağ suçlu olabilir.** Ağın azami ortogonal-olmama açısı ≈89.7° ve bu
   kanat ucundaki O-H "kelebek" kapak bölgesinde. Önceki turdaki bir görüş,
   SA'nın koşmasının ağı akladığı anlamına gelmediğini, sorunun
   "kötü ağ × kırılgan ω denklemi" çarpımı olabileceğini söyledi. Haklı
   olabilir. `blended false` çalışmazsa bu ilk şüpheli.
2. **`bounding omega` sonuç olabilir, sebep değil.** Basınç çözümündeki
   bir bozulma önce gelip ω'yı sonra bozuyor olabilir; ben ters yönde
   nedensellik kuruyor olabilirim.
3. **Çalışsa bile fizik daha doğru olmayabilir.** Yakınsamak ile doğru
   olmak aynı şey değil. Yakınsarsa GCI ve y⁺ duyarlılığı yeniden
   yapılmalı.

---

## Sonuç — atmak istediğim iki adım

### Adım 1 — `blended false` testi (bir sözlük satırı, bir koşu)

**Ne değişiyor:** `0/omega` dosyasındaki duvar sınır koşuluna
`blended false;` eklenecek. Başka hiçbir şey değişmeyecek — ağ, şemalar,
gevşetme katsayıları, `nNonOrthogonalCorrectors 2`, hepsi aynı kalacak.
Amaç tek değişkenli bir test.

**Koşu:** k-ω SST, y⁺≈1, α = 0°, Re_kök = 1.99e6. En az **600 adım** —
önceki ıraksamaların en geci 154. adımdaydı, o yüzden testin o noktanın
çok ötesine geçmesi şart. (Bu disiplini daha önce bir kez ihlal ettim:
40 adımlık bir testte "düzeldi" dedim, koşu 138. adımda çöktü.)

**Ne kanıtlar:** Yakınsarsa, `kOmegaSSTLM` yolu hiç C++ yazmadan açılır.
Geçiş modeli sorusu tamamen farklı bir yere taşınır.

**Ne kanıtlamaz:** Yakınsaması C_D0'ın daha doğru olduğunu göstermez.
Yakınsarsa GCI ve y⁺ duyarlılık çalışması yeniden koşulmalı.

**Iraksarsa:** Hipotez çürütülür, kayda geçer, uç kapak topolojisi bir
sonraki şüpheli olur. Maliyet: bir koşu.

### Adım 2 — sabit geçiş konumu taraması

Adım 1'in sonucundan bağımsız olarak yapılacak; iki bağımsız görüşün de
önerdiği ucuz deney.

**Tasarım:** SA, y⁺≈1 (yakınsadığı bilinen kurulum). Seçilen x_tr/c
konumunun yukarı akışında SA üretim terimi kapatılacak; aşağı akışta
serbest. Tarama noktaları: **x_tr/c = 0.05, 0.15, 0.30, 0.50, 0.70**.
Çıktı: C_D0(x_tr/c) eğrisi ve §6.6'ya bir şekil.

**Uygulama niyetim:** OpenFOAM `fvOptions` içinde bir
`scalarCodedSource`, `nuTilda` üzerinde, maskeye göre üretimi bastıran
bir kaynak terimi.

**Burada bir incelik var ve emin değilim.** Kanat ok açılı ve veter
açıklık boyunca değişiyor. Dolayısıyla maske **küresel x** ile değil,
**yerel veter kesri** ile tanımlanmalı; yoksa kök ile uç farklı x/c'de
tetiklenir. Bunu her hücre için yerel hücum/firar kenarı x'ine göre
hesaplamayı planlıyorum, ama bunun ucuz ve doğru yolu konusunda emin
değilim.

**Nasıl sunulacak:** "C_D0 için alt ve üst **sınır**" **denmeyecek** —
bunların matematiksel anlamda garantili bounds olduğu kanıtlanmadı.
Bunun yerine "two bounding scenarios" / "a bracketing range under
laminar-transition and fully turbulent assumptions" ve tarama bir
**transition-sensitivity analysis** olarak sunulacak.

---

## Sorular

**1. Bulgu 2'deki nedensellik zinciri sağlam mı?**
"blended modda log-tabaka G terimi viskoz alt tabakaya 1/y ölçeğinde
enjekte ediliyor → k şişiyor → ω ıraksıyor" — bu makul mü, yoksa fazla
temiz bir hikâye mi? y⁺≈1'de `blended false` kullanımının bilinen bir
emsali var mı?

**2. Adım 1'i tek değişkenli tutmak doğru mu?**
Aynı anda ω gevşetmesini de düşürmek (0.7 → 0.4) testi "kirletir" ama
başarı şansını artırır. Tek değişkenli saflık mı, yoksa pratik olup
sonra geri alarak ayrıştırmak mı?

**3. Adım 2'de maske nasıl tanımlanmalı?**
Ok açılı, değişken veterli bir kanatta yerel veter kesri maskesinin
OpenFOAM `fvOptions` içinde ucuz ve doğru uygulaması ne? Yerel hücum
kenarını her hücre için hesaplamak yerine daha temiz bir yol var mı?

**4. SA'da geçişi "üretimi kapatarak" taklit etmek doğru mu?**
Alternatifler: ν̃'yı yukarı akışta sıfırda dondurmak, ya da ν_t'yi
maskelemek. Hangisi fiziksel olarak daha az yanıltıcı? Üretimi kapatmak
ν̃'nın yukarı akıştan taşınmasına izin verir; bu istenen mi?

**5. Beş nokta yeterli mi?**
x_tr/c = 0.05...0.70 aralığı ve beş nokta, C_D0(x_tr) eğrisini makale
için yeterince tanımlar mı? Aralık genişletilmeli mi (0.90'a kadar)?

**6. Atladığım bir şey var mı?**
Bu iki adımı koşmadan önce sorulması gereken ama sormadığım bir soru
varsa, asıl duymak istediğim o.
