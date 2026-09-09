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
