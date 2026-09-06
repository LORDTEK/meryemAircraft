# Geçiş modeli: fizibilite notu

Tarih: 2026-09-06
Kaynaklar: `kaynakca/Langtry_2006_PhD.pdf`, `kaynakca/Medida_2014_PhD_Maryland.pdf`

## 1. Sorun

`makale/bolumler/06-reference-designs.md` §6.6'da C_D0 için iki rakam var:

| Kaynak | C_D0 |
|---|---|
| Temiz yüzey / geçişli varsayım (analitik) | 0.0073 |
| 3-B CFD, tam türbülanslı k-ω SST | 0.0141 |

Aradaki 2× fark, C_D0'daki **en büyük tek belirsizlik**. Kapatmanın tek yolu
geçiş modelli bir koşu. Şimdiye kadar yapılamadı çünkü:

- OpenFOAM v1912'de tek geçiş modeli `kOmegaSSTLM` (Langtry–Menter γ-Re_θ).
- Bu model y⁺ ≈ 1 gerektiriyor **ve** bir ω denklemi taşıyor.
- k-ω SST y⁺ ≈ 1'de beş ayrı denemede diverge etti (61, 154, 68, 6, 54 adım;
  ikisinde `bounding omega`). Kademeli başlangıç kurtarmadı.
- Spalart–Allmaras **aynı ağda** y⁺ ≈ 1'de sorunsuz yakınsıyor, ama
  OpenFOAM v1912'de SA tabanlı geçiş modeli yok.

## 2. Medida (2014) ne sunuyor

γ-Re_θ-SA modeli: aynı iki taşınım denklemini (γ ve Re_θt) k-ω yerine
**Spalart–Allmaras**'a bağlıyor. Yani ω denklemi hiç devreye girmiyor;
tıkanıklık çözülmüyor, ortadan kalkıyor.

Türbülans modeline bağlanma noktası tek satır (tez Denk. 3.67):

    Dν̃/Dt = γ·P_ν − D_ν + (1/σ)[∇·((ν+ν̃)∇ν̃) + c_b2(∇ν̃)²]

Sadece **üretim** terimi γ ile çarpılıyor; yok etme terimi ölçeklenmiyor
(Langtry'nin k denkleminde yaptığının aksine — orada D_k de ölçekleniyor).

## 3. OpenFOAM'da ne kadarı hazır

Kaynak ağacı elimizde: `/tmp/ofsrc/openfoam-1912.200626`.
`RAS/kOmegaSSTLM/kOmegaSSTLM.C` (639 satır) γ ve Re_θt denklemlerini
zaten kuruyor. Yeniden kullanılabilecek altyapı:

- Re_θt taşınım denklemi (`correctReThetatGammaInt`, satır 552-568) —
  Medida bu denklemi **hiç değiştirmemiş** (tez §3.3: "The transport
  equation for Reθt was not altered from its original form"). c_θt = 0.03
  ve σ_θt = 2 katsayıları da aynı. Doğrudan alınabilir.
- λ_θ yinelemeli çözümü, F(λ_θ), θ_BL / δ_BL / δ, F_θt sınır tabaka
  algılama fonksiyonu — hepsi kodlu, hepsi değişmeden geçerli.
- Re_v = d²S/ν, F_onset yapısı, denklem birleştirme ve sınırlama
  (`bound`, `relax`, `fvOptions`) iskeleti.

Değişecekler:

| Terim | kOmegaSSTLM (OF v1912) | Medida γ-Re_θ-SA | İş |
|---|---|---|---|
| R_T | k/(ν·ω) | ν_t/ν | 1 satır |
| P_γ | c_a1 F_len S √(γ F_onset)(1−c_e1 γ) | F_onset·G_onset·max(Ω/F_len, 1/F_len,min) | yeniden yaz |
| D_γ | c_a2 Ω F_turb γ (c_e2 γ−1) | Ω γ (1−G_onset) | yeniden yaz |
| F_onset2 tavanı | 2.0 | 4.0 | sabit |
| F_onset3 | max(1−(R_T/2.5)³, 0) | max(2−(0.25R_T)³, 0) | 1 satır |
| F_length | Re_θt korelasyonu | **sabit 40.0** (F_len,min = 2.5) | sadeleşme |
| Re_θc | Re_θt korelasyonu | **0.62·Re_θt** | sadeleşme |
| Re_θt0 | Langtry korelasyonu (Denk. 3.32) | parçalı doğrusal tablo (Tablo 3.1) | fonksiyon değişimi |
| Tu | k'dan hesaplanır | **sözlükten sabit** | sadeleşme |
| Ayrılma kaynaklı γ_sep | var | **çıkarılmış** | sil |
| Bağlanma | γ_eff P_k, min(max(γ,0.1),1) D_k | γ P_ν, D_ν ölçeklenmez | yeni, daha basit |
| SA tabanı | — | dönme düzeltmeli SA (SA-R): Ω → Ω + 2·min(0, S−Ω) | küçük ekleme |

Net: sadeleşen kalem sayısı, yeni yazılacaktan fazla. Kaba tahmin
~250-350 satır C++ ve bir `Make/` klasörü; `libmyTurbulenceModels.so`
olarak derlenip `controlDict`'te `libs` ile yüklenir, OpenFOAM kurulumuna
dokunmadan.

Hesap maliyeti: Medida §3.5, SA'nın yaklaşık **iki katı**. Kabul edilebilir.

## 4. Tek ciddi engel: G_onset yerel değil

Medida tez s.64, kendi ifadesiyle:

> "G_onset can be evaluated by a summation of F_onset along a grid line in
> the wall-normal direction. This aspect of the modified destruction term
> makes the new model **non-local in the wall normal direction**. The
> evaluation of this term does not pose any difficulty in structured
> meshes, but **may not be suitable for unstructured meshes**, unless the
> boundary layer region is resolved using a patched structured mesh."

G_onset tanımı: bir akış-yönü istasyonunda, duvar-normal doğru boyunca
max(F_onset1) > 1.0 ise 1, değilse 0.

OpenFOAM'ın veri yapısı yapısal-olmayan; "grid line" kavramı yok. Ama
**bizim ağımız yapısal bir C-grid** ve üreteci kendi yazdığımız
`cfd/ortak/cagi.py`. Yani (i, j, k) indislemesi bize ait; duvar-normal
hat adreslemesini başlangıçta bir kez kurup hat boyunca indirgeme yapmak
mümkün. Medida'nın izin verdiği "patched structured mesh" durumu tam
olarak bu.

Yine de bu, projeye özgü ~100 satırlık ek adresleme kodu demek ve modeli
genel amaçlı olmaktan çıkarıyor.

## 5. Yan bulgu: ağ normal büyüme oranı sorun değil

Langtry tez s.42: geçiş modeli için duvar-normal genişleme oranı 1.1–1.15
öneriliyor. Bizim ağda `_geometrik` (`cfd/ortak/cagi.py:139`) ilk hücre
2.48e-5c, toplam 100c, n_normal = 113 ile r ≈ 1.12 veriyor. Tam aralıkta.
Yani k-ω'nun y⁺=1'de patlaması normal yönde ağ kalitesinden değil.

Langtry ayrıca (s.42) geçiş ve türbülans denklemlerinin **sınırlı 2. mertebe
upwind** ile çözülmesi gerektiğini vurguluyor; y⁺ > 5'te geçiş noktası
yukarı akışa kayıyor. Bu, mevcut şema seçimimiz için de doğrudan bir uyarı.

## 6. Sonuç

| | |
|---|---|
| Teknik olarak mümkün mü | Evet |
| Ana risk | G_onset'in yerel-olmaması → özel hat adresleme |
| İkincil risk | Model sıkıştırılabilir, yapısal, overset bir çözücüde (OverTURNS) kalibre edildi; sıkıştırılamaz simpleFoam'a taşınırken katsayılar aynı kalır mı doğrulanmalı |
| Doğrulama yolu | T3A / T3B düz levha (Tablo 3.1'in kalibrasyon durumları), sonra S809 veya Eppler 387 kanat profili — ikisi de tezde ölçümle karşılaştırılmış |
| Tahmini iş | Model ~300 satır + hat adresleme ~100 satır + düz levha doğrulaması |
| Alternatif (ucuz) | Sabit geçiş noktası: seçilen x/c'ye kadar üretimi kapat, alt-üst sınır koştur. 0.0073-0.0141 aralığını daraltır, kapatmaz. |

Karar: G_onset için yerel bir yaklaşım (surrogate) bulunabilirse iş
belirgin şekilde küçülür. Bu, dışarıya sorulacak asıl soru.
