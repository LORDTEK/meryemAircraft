# Kaynak avı — gönderim öncesi okunacaklar, öncelik sırasıyla

Üç bağımsız değerlendirmenin (11. tur) ittifak ettiği sonuç: **hedef 40–70 değil,
~25 kaynak.** Doldurma yapılmayacak. Ama şu anda üç iddia atıfsız duruyor ve
onlar taşıyıcı.

> ⚠️ **Aşağıdaki kaynak adları değerlendiricilerin hafızasından geldi ve BEN
> HİÇBİRİNİ OKUMADIM.** Bu, daha önce üç yanlış sayı veren kaynak sınıfının ta
> kendisidir. Adlar birer **iz**dir, atıf değil. Her biri bulunup açılacak,
> içindeki sayı gözle görülecek, ancak ondan sonra metne girecek. Bulunamayan ya
> da iddia edileni söylemeyen bir kaynak sessizce düşer.

## Bu ortamın sınırı

Dergi sitelerine erişemiyorum (Zenodo bile engelli). PDF'leri **siz** bulup
`kaynakca/` altına yükleyeceksiniz; ben okuyup metne bağlarım, ve
`makale/kaynaklar.md`'ye hangi sayının hangi sayfadan geldiğini yazarım.

---

## 🔴 ŞART — bir iddia doğrudan buna dayanıyor

### 1. Gurney flap / kenar çıtası kaldırma artışı (ΔC_L)
**Neden:** §4.4'ün yatış gereksinimi. Şerit 20°/s için ΔC_L ≈ 0,12 istiyor.
Bu sayının *makul* olup olmadığı tümüyle bu literatüre bakıyor. Şu an metin,
sayıyı gereksinim olarak veriyor ve literatür hakkında **hiçbir şey iddia
etmiyor** — bu dürüst ama eksik.
**İzler:** Liebeck 1978 (*Journal of Aircraft*, özgün Gurney çalışması);
Neuhart & Pendergraft 1988 (AIAA); Wang, Li & Choi 2008 (*Progress in Aerospace
Sciences*, derleme).
**Aranan:** kaldırma artışının **sayısı**, hangi yükseklik/veter oranında ve
hangi Reynolds'ta ölçüldüğü. İki birincil çalışma yeter.

### 2. Refleks kesitlerin verebildiği C_m0
**Neden:** §7.6'nın denge penceresi. Metin artık bir aralık **benimsemiyor** —
CG sınırını C_m0'ın fonksiyonu olarak tablo hâlinde veriyor. Ama tablonun hangi
satırının ulaşılabilir olduğunu söylemek için bir ölçüm lazım.
**İzler:** Lissaman 1983 (*Annual Review of Fluid Mechanics*, düşük Re
profilleri); ya da doğrudan bir profil kataloğundan **tek bir refleks kesit** ve
onun kendi C_m0'ı.
**Aranan:** tek bir kesit, adıyla ve sayısıyla. Genel "tipik olarak şu kadar"
cümlesi kurulmayacak.

### 3. Kuyruksuz uçakta uç yüzeyleriyle yön kararlılığı
**Neden:** §4.4'ün sapma bulgusu. Planform C_n_β = 0 veriyor; kararlılık uç
çerçevesi kılıfından gelmek zorunda. Kılıfın eğim katsayısı için 4/rad
**varsayıldı** ve metinde varsayım olduğu yazılı.
**Aranan:** uç kanatçığı / uç finiyle yön kararlılığı sağlayan kuyruksuz bir
konfigürasyon, ve fin etkinliğinin ölçülmüş bir değeri.

### 4. Güncel kuyruk-üstü İHA çalışmaları (2015–2025)
**Neden:** yenilik iddiası ve giriş bölümünün literatür bağlamı. Şu anda tek bir
kuyruk-üstü çalışmaya atıf var. Hakem "bu alan çokça çalışıldı" der ve haklı olur.
**Aranan:** 2–3 birincil çalışma; tercihen geçiş manevrası ve yönelim kontrolü
üzerine, mümkünse deneyli. arXiv kabul.

---

## 🟠 BEKLENEN — yokluğu iddiayı yıkmaz, hakem arar

### 5. eVTOL boyutlandırma / mimari karşılaştırma
NASA çalışması zaten elimizde ve doğru kullanılıyor; yanına 2 kaynak daha.

### 6. Kanat-gövde (BWB) İHA aerodinamiği
1–2 kaynak. Makalenin yeniliği BWB derlemesi değil, fazlasına gerek yok.

### 7. Seri hibrit İHA tahriki
1–2 kaynak. Ana sonuç momentum/sürükleme/güç ölçeklemesinden geliyor.

### 8. Düşük en-boy oranlı ok kanatta girdap kafes doğruluğu
Tek bir metodolojik kaynak yeter.

### 9. §6.6'nın sayısal doğrulaması için standart atıflar
Celik 2008 (GCI) ve Menter (SST) — eğer metinde o yöntemlerin sayısı
kullanılıyorsa. Kullanılmıyorsa gerekmez.

---

## Düşenler

**Stall sonrası C_m 0,1–0,3.** Metinden **çıkarıldı**. Gerekçe: yörünge boyunca
çözülmüş bütçe onu zaten geride bıraktı, ve genel aralık atfedilebilir bir
kaynağa dayanmıyordu. En kolay silinen atıfsız iddia buydu, ve silinmesi
makaleyi zayıflatmadı — güçlendirdi.

**Uç çerçevesi C_D'sini yeniden araştırmak.** Üç değerlendirme de "bırakın"
dedi. Sınırlar bölümünde düşük Reynolds uyarısıyla duruyor.

**CFD belirsizliğini yeniden açmak.** Üçü de "dokunmayın" dedi.

---

## Atıf dürüstlüğü kuralı — üçünün de aynı yere bastığı nokta

Bir aralığı **atfetmek** de bir iddiadır. *"Şu aralıkta değerler bildirilmiştir
[x,y]"* cümlesi, [x] ve [y] açılıp o aralık görülmedikçe kurulamaz. Ama şu ayrım
meşru ve kullanılacak:

> **Literatür ifadesi:** "X ve Y çalışmaları, kendi deney koşullarında yaklaşık
> şu aralıkta kaldırma artışları bildiriyor."
> **Bizim gereksinimimiz:** "Bu konfigürasyon ΔC_L = 0,12 istiyor."

İkisi karıştırılmayacak. Literatür bağlam verir, bizim hesabımız gereksinimi
verir.

**Birinci elden okuma kuralı makaleye yazılmayacak** (özür gibi durur), **kapak
mektubuna** yazılacak.

---

# İNDİRME BAĞLANTILARI (09.09.2026)

> ⚠️ **Bu bağlantıları arama sonuçlarından topladım; HİÇBİRİNİ AÇMADIM.** Bu
> ortamdan arxiv, ntrs, mdpi, doi — hiçbirine erişemiyorum (proxy engelli),
> yalnızca arama yapabiliyorum. Yani başlıkların doğruluğunu, içeriğin iddia
> edileni söyleyip söylemediğini ve erişilebilirliği **doğrulayamadım**.
> Siz indirin, `kaynakca/` altına koyun, ben okuyayım.
>
> Arama özetleri bana bazı sayılar da verdi (örn. "%1,5 veter Gurney → ΔC_Lmax
> ≈ 0,3", "NACA 4412'de 1,49 → 1,96"). **Bunları metne yazmadım ve
> yazmayacağım** — tam olarak bu sınıftaki özetler daha önce bize üç yanlış sayı
> vermişti. PDF açılıp sayı gözle görülene kadar hiçbiri makaleye girmez.

**Erişim işaretleri:** 🟢 serbest PDF beklenir · 🟡 belirsiz · 🔴 ücretli olabilir

---

## 🔴 ŞART 1 — Gurney / çıta kaldırma artışı

| | Bağlantı | Erişim |
|---|---|---|
| *Lift enhancement of an airfoil using a Gurney flap and vortex generators* (NASA Ames, NACA 4412 rüzgâr tüneli) | <https://ntrs.nasa.gov/citations/19930040765> | 🟢 |
| *A Water Tunnel Study of Gurney Flaps* (NASA TM 4071) | <https://ntrs.nasa.gov/api/citations/19890004024/downloads/19890004024.pdf> | 🟢 doğrudan PDF |
| *Experimental and Computational…* (NASA TM 110432) | <https://ntrs.nasa.gov/api/citations/19970012496/downloads/19970012496.pdf> | 🟢 doğrudan PDF |
| *Static Extended Trailing Edge for Lift Enhancement* (NASA) | <https://ntrs.nasa.gov/api/citations/20070030823/downloads/20070030823.pdf> | 🟢 doğrudan PDF |
| *Canard Enhancement with Gurney Flaps* (DTIC AD1062413) | <https://apps.dtic.mil/sti/html/tr/AD1062413/index.html> | 🟢 |
| *Effects of Gurney Flaps on a NACA0012 Airfoil* (Springer) | <https://link.springer.com/article/10.1023/A:1015679408150> | 🔴 |
| *Aerodynamic Loads Alteration by Gurney Flap* (arXiv) | <https://arxiv.org/pdf/1809.06975> | 🟢 |

⚠️ **Teknik uyarı, önemli.** Gurney literatürünün tamamı, **firar kenarında,
akışa dik** duran bir çıtayı ölçüyor. Bizim şeridimiz firar kenarında değil,
alt yüzeyde, kök veterinin ~%15'inden başlayıp **45° köşegen** uzanıyor.
Yani benzetme göründüğü kadar sıkı değil: bu kaynaklar **bağlam** verir
("bu sınıf cihazlar bu mertebede artış üretebiliyor"), **aktarılabilir bir sayı
vermez**. Metinde de böyle kullanılacak.

## 🔴 ŞART 2 — Refleks kesit C_m0

| | Bağlantı | Erişim |
|---|---|---|
| Kuyruksuz/uçan kanat profil veritabanı (Hepperle) | <https://www.mh-aerotools.de/airfoils/flywing1.htm> | 🟢 |
| Kuyruksuz uçaklar için profil tasarımı (Hepperle, 3. bölüm) | <https://www.mh-aerotools.de/airfoils/nf_3.htm> | 🟢 |
| Uçan kanat profil veritabanı (aerodesign.de) | <https://www.aerodesign.de/english/profile/profile_s.htm> | 🟢 |

**Aranan:** genel bir aralık değil, **tek bir refleks kesit**, adıyla ve kendi
C_m0'ıyla. Tablomuzun hangi satırına oturduğunu o söyleyecek. Hepperle'nin
sayfaları hakemli dergi değil — eğer oradan bir kesit seçersek, o kesitin
**birincil** kaynağını (profil kataloğu ya da özgün yayın) da bulmamız gerekir.

## 🔴 ŞART 3 — Uç yüzeyleriyle yön kararlılığı

| | Bağlantı | Erişim |
|---|---|---|
| *Flutter and Directional Stability of Aircraft with Wing-Tip Fins* (J. Aircraft) | <https://arc.aiaa.org/doi/10.2514/1.C031978> | 🔴 |
| *Design and Flight Tests of a Small Flying Wing UAV* (MDPI Aerospace 13(3):240) | <https://www.mdpi.com/2226-4310/13/3/240> | 🟢 açık erişim |
| *Assessment of C-Type Winglet Integration on a Fixed-Wing BWB UAV* (MDPI Eng. Proc.) | <https://www.mdpi.com/2673-4591/133/1/95> | 🟢 açık erişim |

## 🔴 ŞART 4 — Güncel kuyruk-üstü İHA çalışmaları

| | Bağlantı | Erişim |
|---|---|---|
| ⭐ *YawSitter: Modeling and Controlling a Tail-Sitter UAV with **Enhanced Yaw Control*** | <https://arxiv.org/html/2510.02968v1> | 🟢 |
| *Global Incremental Flight Control for Agile Maneuvering of a Tailsitter Flying Wing* | <https://arxiv.org/pdf/2207.13218> | 🟢 doğrudan PDF |
| *Control of a Tail-Sitter VTOL UAV Based on Recurrent Neural Networks* | <https://arxiv.org/abs/2104.02108> | 🟢 |
| *A Universal Optimal Control Strategy for a Tailsitter UAV* | <https://arxiv.org/pdf/2605.01556> | 🟢 |
| *Lifting-wing Quadcopter Modeling and Unified Control* | <https://arxiv.org/pdf/2301.00730> | 🟢 |
| *Biplane-Quadrotor Tail-Sitter UAV: Flight Dynamics and Control* (JGCD) | <https://arc.aiaa.org/doi/10.2514/1.G003201> | 🔴 |

⭐ **YawSitter'ı önce indirin.** Başlığından anlaşıldığı kadarıyla doğrudan
kuyruk-üstü bir aracın **sapma kontrolü** üzerine, ve bizim dünkü sapma
bulgumuz tam oraya bakıyor. Bize ya destek verir ya da düzeltir; ikisi de
işimize yarar.

## 🟠 BEKLENEN 5 — eVTOL boyutlandırma

| | Bağlantı | Erişim |
|---|---|---|
| NASA TM-20210017971, *Design of a Tiltwing Concept Vehicle for UAM* | <https://rotorcraft.arc.nasa.gov/Publications/files/NASA-TM-20210017971.pdf> | 🟢 doğrudan PDF |
| *Design of a Six-Tiltrotor Concept Vehicle for UAM* (NTRS) | <https://ntrs.nasa.gov/api/citations/20240008060/downloads/1724_Jeong_Final_062524.pdf> | 🟢 doğrudan PDF |
| *NASA concept vehicles and the engineering of AAM aircraft* (Aeronautical J.) | <https://www.cambridge.org/core/journals/aeronautical-journal/article/nasa-concept-vehicles-and-the-engineering-of-advanced-air-mobility-aircraft/AA7E668D759491B1889299819A2F2715> | 🟡 |

## 🟠 BEKLENEN 6 — Kanat-gövde (BWB) İHA aerodinamiği

| | Bağlantı | Erişim |
|---|---|---|
| *Design, Computational Aerodynamic… VTOL-Configured Hybrid BWB UAV* (Wiley, açık) | <https://onlinelibrary.wiley.com/doi/10.1155/2023/9699908> | 🟢 |
| *Aerodynamic design of a blended wing body VTOL UAV* (IOP, açık) | <https://iopscience.iop.org/article/10.1088/1742-6596/2965/1/012020> | 🟢 |

## 🟠 BEKLENEN 7 — Seri hibrit İHA tahriki

| | Bağlantı | Erişim |
|---|---|---|
| *The Design of Improved Series Hybrid Power System Based on Compound-Wing VTOL* (**Drones** 8(11):634) | <https://www.mdpi.com/2504-446X/8/11/634> | 🟢 |
| *On the Range Equation for Hybrid-Electric Aircraft* (Aerospace 10(8):687) | <https://www.mdpi.com/2226-4310/10/8/687> | 🟢 |
| *A Review of Hybrid-Electric Propulsion in Aviation* (Aerospace 12(10):895) | <https://www.mdpi.com/2226-4310/12/10/895> | 🟢 |

💡 Birincisi **Drones'un kendi sayfalarında** ve tam bizim mimarimiz
(seri hibrit + VTOL). Dergiye kendi yayımladığı işi atıf vermek her zaman iyi
karşılanır.

## 🟠 BEKLENEN 8 — Girdap kafes doğruluğu

| | Bağlantı | Erişim |
|---|---|---|
| *Application of the vortex-lattice technique to thin wings with vortex separation* (NASA) | <https://ntrs.nasa.gov/api/citations/19760021089/downloads/19760021089.pdf> | 🟢 doğrudan PDF |
| *Review of vortex lattice method for supersonic aircraft design* (Aeronautical J.) | <https://www.cambridge.org/core/journals/aeronautical-journal/article/review-of-vortex-lattice-method-for-supersonic-aircraft-design/56AC0DDC2161FEF838A72EACD3748AB7> | 🟡 |

---

## İndirme sırası önerisi

Hepsini indirmeyin. **Şu beşle başlayın**, hepsi serbest ve doğrudan PDF:

1. `19930040765` (Gurney, NASA Ames rüzgâr tüneli) — Şart 1
2. `arxiv 2510.02968` (YawSitter) — Şart 4, ve dünkü bulguya en yakın
3. `mdpi 2226-4310/13/3/240` (uçan kanat İHA uçuş denemeleri) — Şart 3
4. `mdpi 2504-446X/8/11/634` (Drones, seri hibrit VTOL) — Beklenen 7
5. `NASA-TM-20210017971` (eVTOL boyutlandırma) — Beklenen 5

Bunlar geldiğinde okur, hangi sayının hangi sayfadan geldiğini
`makale/kaynaklar.md`'ye yazar, metne bağlarım. Refleks kesit (Şart 2) en
zoru — orada muhtemelen birlikte karar vermemiz gerekecek.
