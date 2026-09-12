# Kaynakça — yerel PDF dizini

Bu dizin, çalışma sırasında **doğrudan okunan** birincil kaynakları tutar.
Makalenin atıf listesi burada değil, `makale/kaynakca-en.md` dosyasındadır.
Buradaki dosyalar okunmak için var, atıf için değil — bazıları okundu ve
**bilerek atıf yapılmadı** (aşağıda işaretli).

**Depoda iki kaynak dizini var, karıştırılmamalı:**

| Dizin | İçerik | Neden ayrı |
|---|---|---|
| `cfd/kaynak/` | CFD doğrulama kaynakları (NASA TMR, NAS teknik raporu, NACA 0012 doğrulama vakası) | Sayısal iddialara **dayanak**. `cfd/veri/referans.py` ve `cfd/ortak/cagi.py` bu dosyalara sayfa numarasıyla atıf yapar; taşınırsa kod bozulur. |
| `kaynakca/` (bu dizin) | Genel okuma kaynakları | Koda gömülü atıf yok. Okunup anlaşılmak için var. |

## Okuma notları nerede

Her kaynağın **ne verdiği ve neyi vermediği** `aero/README.md` içinde,
okundukları sırayla yazılı. Bu tablo yalnızca dosyanın neden burada
olduğunu söyler.

## Kuyruksuz / uçan kanat kararlılık ve kontrol

| Dosya | Ne için |
|---|---|
| `NACA-TR-796_...pdf` | **En verimli tek kaynak.** Toe açısının işareti (yüksek AR → toe-out), C_n_β ölçütü (0,001/derece), 0,01c spoiler eşiği, tek yönlü çıkıntının yunuslama cezası, gövdenin destabilize edici etkisi. Kaynakça [19]. |
| `NACA-ACR-L4H19_1944_tailless-tip-fins.pdf` | ⚠️ **TR-796 ile AYNI rapor** — savaş zamanı ön baskısı. OCR'ı kötü; alıntılar TR-796'dan alındı. Silinmedi çünkü ön baskı olduğu belgelenmiş olsun. |
| `NACA-TM-4649_Moul_...pdf` | 60° ok açılı dört uçan kanat, −8°…48°: yön kararlılığı kararsız/nötr, ve AR ile şiddetlenen pitch-up. Kaynakça [20]. |
| `NACA-WR_swept-all-wing-free-flight-directional.pdf` | Serbest uçuş: düşük C_n_β'da **düşük etkin dihedral gerekir**, yoksa Dutch roll sönümsüz kalır. Bizim C_l_β = −0,045 tam bu tarafta. |
| `NASA-TM-78767_...pdf` | Uç podlarında dikey kuyruk: optimum toe açısı ~1,5°, ve %75 daha büyük alan L/D'yi değiştirmiyor. Kaynakça [34]. |
| `NASA-TM-4726_Lepsch_...pdf` | Uç finleri **uç plakası** gibi davranıp taşımayı artırıyor. Bizim fairing'imiz tam veterli değil; **aktarılmıyor**, ve nedeni yazıldı. |

## Kesit verisi ve refleks (S4)

| Dosya | Ne için |
|---|---|
| `NACA-TR-460_Jacobs-1933_...pdf` | 2R212'nin **ölçülmüş** C_m0 = +0,004'ü. Denge zincirinin dayandığı tek ölçüm. Kaynakça [17]. |
| `Selig-UIUC_Low-Speed-Airfoil-Data-V1.pdf` / `-V2.pdf` | ⚠️ S4'ü **kapatmıyor ve kapatamaz**: UIUC düzeneği momenti ölçmüyor, Tablo 3.1'in tamamı Eppler/ISES/XFOIL çıktısı. Tek uçan-kanat kesiti MH45 → **−0,006**. Kaynakça [36]. |
| `Shinde-2020_...pdf` | ❌ **Hiçbir sayısı alınmadı** — C_m0 tablosu kendi metniyle çelişiyor. Yalnız gereksinim ifadesi ve kesit ailesi listesi için anıldı. Kaynakça [27]. |

## BWB aerodinamiği ve yöntem

| Dosya | Ne için |
|---|---|
| `quasi-3D-aero-method-BWB-UAV_Aerospace.pdf` | 🔴 **Yöntemimize en sert itiraz:** VLM, BWB'de C_L'i %30–38 eksik veriyor ve yazarlar VLM'i trim analizinden çıkarıyor. Ayrıca BWB pitch-break mekanizması. Kaynakça [39]. |
| `Wang-Zhou-2022_small-BWB-UAV-aero-design-validation_Aerospace.pdf` | 🔑 RANS + **rüzgâr tüneli**: α > 10°'de CFD ölçümden belirgin sapıyor. Geçiş momentinin neden ölçüme ait olduğunu gösteren kaynak. Kaynakça [44]. |
| `BWB-low-Mach-aerodynamic-performance_Fluids.pdf` | Refleksi tasarım değişkeni yapıp 2,44° burulmayla dengeliyor; statik pay ölçütü (0,1–0,3) ve C_m_α aralığı (−0,3…−1,5). Kaynakça [41]. |
| `SugarGabor-Botez_nonlinear-VLM-viscous-strip-coupling.pdf` | ⚠️ Bu dosyayı önce `Gallay-Laurendeau` diye adlandırmıştım, **yanlıştı.** S1'in istediği iskoz hesabın yöntemi. Kaynakça [40]. |
| `Falkner_ARC-RM-2749_...pdf` | VLM'in hangi büyüklükte hızlı yakınsadığı — §6'nın yöntem savunması. Kaynakça [24]. |
| `NASA-1976_Smith-Bhateley_...pdf` | VLM'in **kullanılmadığı** sınır: hücum kenarı girdap ayrılması. Kaynakça [25]. |
| `Cambridge-2009_laminar-flying-wing-conceptual-design.pdf` | Ölçek bizden çok uzak (80 m / 69 t / M 0,58). Yalnız t/c = %28 seçimi bağlam olarak alındı; **sayı girmedi.** |

## Gurney / şerit / ayrılma denetimi

| Dosya | Ne için |
|---|---|
| `Traub-2024_...pdf` | Şeridin yükseklik-etki tablosu ve düzlemsel/düzlemsel-olmayan e değerleri. Kaynakça [31]. |
| `NASA-TM-112990_Ross-Storms_...pdf` | Ölçülmüş h/c eşiği (%1,5) ve ters sapma. Kaynakça [32]. |
| `NASA-CR-194793_Buchholz_...pdf` | Konik Gurney'in **üç ekseni** birden yüklemesi. Kaynakça [33]. |
| `Yang-2020_...pdf` | Türbülansta bozulma (%19'da "negligible") ve perdövites sonrası zayıflama. Kaynakça [35]. |
| `Liu-2025_Gurney-flap-LE-TE_Fluids.pdf` | ⚠️ Yang'ın tersi: α = 20°'de C_l +%93,7, C_d +%0,4. **Benzetim**, ve sade kanat tabanı deneyin %25 altında. Kaynakça [37]. |
| `NASA-TM-4071_Neuhart-Pendergraft_...pdf` | Re = 8.588'de mekanizma korunuyor (birinci mertebede inviscid), ve 0,0125c / 0,05c direnç eşiği. Kaynakça [38]. |

## Kuyruk-oturur geçiş: kontrol ve uçuş

| Dosya | Ne için |
|---|---|
| `Li_transition-optimization-VTOL-tailsitter.pdf` | Uçuş denemeli, ve **hiç yunuslama momenti taşımıyor.** Kaynakça [28]. |
| `Lyu_hierarchical-control-...IROS.pdf` | Elevon'suz uçurulmuş: asılı ve geçişte iyi, **düz uçuşta motor doyumu.** Kaynakça [29]. |
| `arXiv-2412.06197_tailsitter-transition-review.pdf` | CRC-20: "geçiş tamam, düz uçuş sorunlu" — ikinci program. Kaynakça [30]. |
| `Carter-2021_VT-thesis_...pdf` | Kontrol ilkemizin öncülü + aynı örüntünün üçüncü örneği. Kaynakça [30 civarı]. |
| `tailsitter-transition-L1-neural-adaptive-control_CJA-2023.pdf` | Alanda **doğrusal olmayan C_m(α)** taşıyan tek örnek — ama eğri ödünç, fark uyarlamalı ağla kapatılıyor. Kaynakça [42]. |
| `arXiv-2312.10761_tailsitter-transition-control.pdf` | Pervane izinden etkin α'yı momentum kuramıyla kuruyor — bizim `etkin_alfa()`'mızın güncel teyidi. Kaynakça [43]. |
| `arXiv-1810.11534_simple-controller-...pdf` | Lyapunov tabanlı basit geçiş denetleyicisi. Okundu; **yeni bir şey vermedi**, atıf yok. |
| `time-optimal-altitude-hold-transition_Aerospace.pdf` | "Transition corridor" terimi ve zaman-optimal geçiş. Kaynakça [31 civarı]. |

## Boyutlandırma ve mimari karşılaştırma

| Dosya | Ne için |
|---|---|
| `Bacchini-Cestino-2019_...pdf` | Tampon özgül gücü (700–1300 W/kg) — §8'in en ciddi maruziyeti. Kaynakça [26 civarı]. |
| `Johnson-Silva_NASA-concept-vehicles-AAM.pdf` | Beş araçlı NASA tablosu; §3.7'deki yanlış iddiayı **çürüten** kaynak. |
| `Ugwueze-2023_eVTOL-sizing-method_Aerospace.pdf` | AR 7,0'da e = 0,85 — bizim varsayımımızın konvansiyonel olduğunun kanıtı. ⚠️ Aynı makale pil enerji yoğunluğunu iki yerde **"275 kW/kg"** yazıyor (birim hatası); o sayı alınmadı. |
| `NotreDame_NASW-4435_design-study.pdf` | ❌ **Atıf yapılmadı — gri literatür** (1991 öğrenci tasarım önergesi). Ama 2R212 kullanıp üstüne 2° refleks + −8° elevatör gerektirmesi §7'yi bağımsız doğruluyor. |

## CFD geçiş modelleme (kod tarafı)

| Dosya | Ne için |
|---|---|
| `Langtry_2006_PhD.pdf` | γ-Re_θ geçiş modelinin birincil kaynağı; ağ gereksinimleri s. 42–43. OpenFOAM `kOmegaSSTLM` bunun uygulamasıdır. |
| `Medida_2014_PhD_Maryland.pdf` | γ-Re_θ-SA: geçiş denklemlerini Spalart–Allmaras'a bağlar. Bkz. `cfd/gecis-modeli-fizibilite.md`. |

## Diğer

| Dosya | Ne için |
|---|---|
| `7178ed2b-...pdf` | TÜRKPATENT, *Patent/Faydalı Model Başvuru Kılavuzu*. |

## Notlar

- `Kap01_05_1.pdf` **iki kez silindi.** `Langtry_2006_PhD.pdf` ile bit-bit
  aynıydı (md5 `937e4f6f3e2cc66b03b8903d033b01f9`); ilk silinişinden sonra
  yeniden yüklenmiş. İçerik kaybı yok, aynı dosya duruyor.
- Dosyalar git geçmişinde kalıcı olduğu için silmek depo boyutunu
  küçültmez (dizin ~225 MB); bu yüzden ileride kaynak eklerken boyuta
  dikkat.
- ⚠️ **İki dosya yanlış adlandırılmıştı** ve ikisi de okuma sırasında
  yakalandı: `Gallay-Laurendeau` → `SugarGabor-Botez`, `Zhang-2022` →
  `Wang-Zhou-2022`. Kaynakları "içerik doğrulayarak" adlandırdığım iddiası
  bu iki dosyada doğru değildi. Yeni kaynak eklerken **açıp ilk sayfaya
  bakılacak**, dosya adına güvenilmeyecek.
- Yeni kaynak eklenirken bu tabloya bir satır eklenmeli; yoksa altı ay
  sonra dosyanın neden orada olduğu bilinmez.
