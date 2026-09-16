# Dış görüş için soru metni — geçiş modeli (2026-09-06)

Aşağıdaki metin, başka bir yapay zekâya olduğu gibi yapıştırılmak üzere
hazırlandı. Kendi kendine yeter; okuyanın proje hakkında ön bilgisi
olduğu varsayılmaz.

---

## Giriş — bağlam

Bir kuyruk üstü oturan (tail-sitter), karma kanat-gövde (BWB) gövdeli VTOL
İHA konfigürasyon çalışması üzerinde çalışıyorum. Çıktı bir bilimsel makale
ve makalenin sürükleme bütçesi bölümünde kapatamadığım bir belirsizlik var.

Sıfır-kaldırma sürükleme katsayısı C_D0 için iki rakamım var:

| Kaynak | C_D0 |
|---|---|
| Analitik, temiz yüzey + geçişli sınır tabaka varsayımı | 0.0073 |
| 3-B CFD, **tam türbülanslı** k-ω SST | 0.0141 |

Aradaki 2× fark, sürükleme bütçesindeki en büyük tek belirsizlik.
Kapatmanın yolu geçiş (laminar-türbülans transition) modelli bir koşu.
Yapamadım. Nedenini aşağıda ayrıntısıyla anlatıyorum çünkü soru tam olarak
orada.

## Gelişme — teknik durum

**Çözücü ve ağ.** OpenFOAM v1912, `simpleFoam` (sıkıştırılamaz, kararlı hal,
SIMPLE). Ağ kendi yazdığım bir Python üreteciyle kurulan **yapısal C-grid**
(gmsh üzerinden, `gmshToFoam -keepOrientation` ile aktarılıyor). Kanat ucunda
O-H "kelebek" kapak var. Ağ özellikleri:

- Azami ortogonal-olmayanlık ≈ 89.7° (uç kapak bölgesinde)
- Duvar-normal geometrik büyüme oranı r ≈ 1.12, n_normal = 113
- Kanat profili çevresinde 256 düğüm
- Re_kök = 1.99e6 (uçuş koşulu)
- `limited 0.33` ortogonal-olmayanlık düzeltmesi, klasik SIMPLE
  (`consistent no`, p 0.3 / U 0.7), p için GAMG + DICGaussSeidel

**Ne çalışıyor.** y⁺ ≈ 20-43 aralığında duvar fonksiyonlarıyla k-ω SST
sorunsuz yakınsıyor. Grid convergence index (Celik 2008) çalışması yapıldı,
üç ağ seviyesinde asimptotik aralıkta. Belirsizlik bütçesi ±%5 civarında.
Ayrıca **Spalart–Allmaras aynı ağda y⁺ ≈ 1'de sorunsuz yakınsıyor** —
`nutLowReWallFunction` + `nuTilda` duvarda sıfır. Duvar çözünürlüğü etkisini
bu sayede ayırabildim (y⁺ 20 → 1 arasında C_D0 farkı yalnızca %1.6, doyuma
ulaşmış).

**Ne çalışmıyor.** k-ω SST'yi y⁺ ≈ 1'e indirdiğimde beş ayrı denemede de
ω denklemi diverge etti — 61, 154, 68, 6 ve 54 adımda. İkisinde açıkça
`bounding omega` uyarısı geldi. Denediklerim: `omegaWallFunction` (blended),
kademeli başlangıç (y⁺ 20 çözümünden başlayıp dy'yi kademeli düşürmek),
gevşetme katsayılarını düşürmek, ilk 200 adımda upwind. Hiçbiri kurtarmadı.

Bu bir sorun çünkü OpenFOAM v1912'nin **tek** geçiş modeli `kOmegaSSTLM`
(Langtry–Menter γ-Re_θ) ve bu model iki şey birden istiyor: y⁺ ≈ 1 **ve**
bir ω denklemi. Yani yakınsayan modelin (SA) geçiş desteği yok, geçiş
desteği olan modelin (k-ω) benim ağımda y⁺=1'de yakınsaması yok.

**Ne buldum.** Medida'nın 2014 Maryland doktora tezini okudum
(*Correlation-based Transition Modeling for External Aerodynamic Flows*).
γ-Re_θ-SA modeli tam da bu düğümü çözüyor: aynı iki taşınım denklemini
(γ ve Re_θt) k-ω yerine Spalart–Allmaras'a bağlıyor. Bağlantı tek satır
(tez Denk. 3.67): SA'nın **üretim** terimi γ ile çarpılıyor, yok etme terimi
ölçeklenmiyor.

OpenFOAM'ın `kOmegaSSTLM.C` kaynağını inceledim (639 satır). İyi haber:
Re_θt taşınım denklemi, λ_θ yinelemeli çözümü, F(λ_θ), sınır tabaka
algılama fonksiyonu F_θt — hepsi zaten kodlu ve Medida bu denklemi **hiç
değiştirmemiş** (tez §3.3). Değişecekler sınırlı ve çoğu sadeleşme:
R_T = ν_t/ν olacak, F_length sabit 40.0 olacak, Re_θc = 0.62·Re_θt olacak,
Tu k'dan değil sözlükten gelecek, ayrılma kaynaklı γ_sep düzeltmesi silinecek.
Kabaca 300 satır C++, ayrı bir kütüphane olarak derlenip `controlDict`'ten
yüklenebilir.

**Nerede takıldım.** Medida'nın modelindeki G_onset terimi yerel değil.
Tezin kendi ifadesiyle (s. 64):

> "G_onset can be evaluated by a summation of F_onset along a grid line in
> the wall-normal direction. This aspect of the modified destruction term
> makes the new model **non-local in the wall normal direction**. The
> evaluation of this term does not pose any difficulty in structured meshes,
> but **may not be suitable for unstructured meshes**, unless the boundary
> layer region is resolved using a patched structured mesh."

G_onset tanımı: bir akış-yönü istasyonunda, duvar-normal doğru boyunca
max(F_onset1) > 1.0 ise 1, değilse 0.

OpenFOAM'ın veri yapısı yapısal-olmayan; "grid line" diye bir kavram yok.
Ağım aslında yapısal olduğu ve üreteci benim olduğu için (i,j,k) indislemesini
biliyorum; başlangıçta bir kez duvar-normal hat adreslemesi kurup hat boyunca
indirgeme yapabilirim. Ama bu projeye özgü ~100 satır ek kod demek ve modeli
genel amaçlı olmaktan çıkarıyor.

## Sonuç — sormak istediklerim

Beş sorum var, önem sırasıyla:

**1. G_onset için yerel bir yaklaşım (surrogate) var mı?**
Bu tek terim yerelleşirse iş belirgin şekilde küçülür. Aklımda bir ihtimal
var ama emin değilim: Menter, Smirnov, Liu, Avancha'nın 2015 tarihli
*"A One-Equation Local Correlation-Based Transition Model"* çalışması
(Flow, Turbulence and Combustion) Re_θt denklemini tamamen atıp yalnızca γ
denklemi bırakıyor ve tamamen yerel olduğunu iddia ediyor. Bunun SA'ya
bağlanmış bir sürümü var mı? Varsa hangi kaynak? Yoksa, Medida'nın
G_onset'ini bozmadan yerelleştiren bir yaklaşım literatürde denendi mi?

**2. Doğrudan k-ω'nun y⁺=1'deki ıraksaması nasıl aşılıyor?**
Bu daha ucuz yol olurdu — hiç kod yazmadan `kOmegaSSTLM` kullanabilirdim.
Yüksek ortogonal-olmayanlıkta (≈89.7°) ω denklemi için standart çare ne?
Menter'in ω_wall = 60ν/(β₁d²) sabit değeri, blended duvar fonksiyonundan
daha mı dayanıklı? Yoksa 89.7° zaten y⁺=1 için umutsuz mu ve asıl yapılması
gereken uç kapak topolojisini düzeltmek mi? (Not: SA'nın aynı ağda sorunsuz
koşması, sorunun ağdan çok ω denkleminin kendisinden kaynaklandığını
düşündürüyor, ama emin değilim.)

**3. Kalibrasyon taşınabilir mi?**
Medida modelini OverTURNS'te kalibre etmiş: sıkıştırılabilir, yapısal
eğrisel koordinat, overset, örtük zaman ilerletme. Ben sıkıştırılamaz,
sonlu hacim, kararlı hal SIMPLE'a taşıyacağım. F_length = 40.0 ve α = 0.62
gibi katsayılar bu geçişte anlamını korur mu, yoksa yeniden kalibrasyon mu
gerekir? Benzer bir taşıma daha önce yapıldı mı?

**4. Doğrulama sırası ne olmalı?**
Planım: önce T3A/T3B düz levha (Medida'nın kalibrasyon durumları), sonra
S809 veya Eppler 387 kanat profili (ikisi de tezde ölçümle karşılaştırılmış).
Bu sıra mantıklı mı, atlanan bir ara adım var mı?

**5. Strateji sorusu — bu iş buna değer mi?**
Makale bir *konfigürasyon çalışması*, bir CFD metodoloji makalesi değil.
Hakem gözünde, geçiş modelli tam bir koşu gerçekten şart mı? Yoksa
"C_D0 = 0.0073–0.0141 aralığında, alt sınır temiz yüzey varsayımı, üst sınır
tam türbülanslı CFD" şeklinde dürüstçe verilen bir **aralık** yeterli mi?
Ara çözüm olarak sabit geçiş noktası (seçilen x/c'ye kadar üretimi kapatmak)
ile üç-dört noktalı bir tarama, tam modelin yerini tutar mı?

Kısacası: özel bir türbülans modeli yazmaya girişmeden önce, daha ucuz bir
yol olup olmadığını bilmek istiyorum.
