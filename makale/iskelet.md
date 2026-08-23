# Makale İskeleti — v1

**Dil:** İngilizce · **Durum:** yapı onayı bekliyor · **Kural:** makale ⊆ patent başvurusu

**Merkez tez (N58):**
> Hibrit VTOL mimarisi, taktik kullanımı **seyir veriminden keserek** satın alır.
> Bu kesinti mimarinin kendisinden doğar, uygulama kalitesinden değil.
> İşte o kesintiyi ödemeyen bir konfigürasyon.

**Yazım kuralları — istisnasız uygulanacak:**
- Şirket ismi üzerinden kurgu yok. "X'i yendik" cümlesi metinde geçmez (N58).
- Hesaplanmış sayı, ölçülmüş sayının karşısına "üstünlük" olarak konmaz.
- Doğrulanmamış her sayı, doğrulanmamış olduğu söylenerek verilir.
- Ok açıları "seçilmiştir" diye sunulur, "türetilmiştir" diye değil (N4).

---

## Bölüm planı

### 1. Introduction
**İddia:** Sabit kanat menzil verir ama altyapı ister; döner kanat dikey kalkış verir
ama menzil vermez. İkisini birleştirme ihtiyacı gerçektir ve bugüne kadar bedelle
karşılanmıştır.

*İçerik:* İki aile, iki sınır. Problemin tanımı. Makalenin iddiası ve katkı listesi.
*Uzunluk:* ~1 sayfa.

---

### 2. Background: seventy years of attempts
**İddia:** Pist gereksinimini kaldırma çabası yetmiş yıldır kesilmedi; bu, ihtiyacın
gerçek olduğunun kanıtıdır. Denemelerin çoğu, kavramın kendisi çürüdüğü için değil,
**konsepte dışsal** sebeplerle sona ermiştir.

*İçerik:*
- Pervaneli kanat-gövde / gövdesiz denemeler: Burnelli (test sorunsuz, üretim siparişi
  yok), Northrop XB-35 (güç aktarma organları, kanat değil), Vought V-173/XF5U (düşük
  hız iddiasını kanıtladı, jet çağına yenildi)
- Kuyruğa oturanlar: XFV-1 (motor gecikmesi), XFY-1 (**pilot** — omuz üstünden bakarak
  iniş, uzman pilot zorunluluğu)
- Hilal kanat: Handley Page Victor, ok açısı/veter/kalınlık üçlü dağılımı
- Modern hibrit VTOL: lift+cruise ve tilt aileleri
- **Ana çıkarım:** XFY-1'i öldüren şey aerodinamik değil insandı. O kısıt insansız
  araçta yoktur.

*Uzunluk:* ~2 sayfa. Bu bölüm "olamaz" hissini kurar; çözümün vurucu olması buna bağlı.

---

### 3. The architectural tax of hybrid VTOL
**İddia:** Hibrit VTOL üç fatura öder — kütle, sürükleme, boyutlandırma. Bu faturalar
birbirine **dönüştürülebilir ama ortadan kaldırılamaz**; çünkü mimariden doğarlar.

*İçerik:*
- Yapısal sebep: hover donanımı uçuşun %100'ünde taşınır, %2'sinde kullanılır
- **Fatura 1 — kütle:** ikinci itki setinin ölü ağırlığı
- **Fatura 2 — sürükleme:** açıkta duran rotorlar. Yayımlanmış sayılar: hibrit modda
  rotor-iz girişimi sürüklemeyi %20–40 artırır; pervaneleri içeri çekmek parazit
  sürüklemenin %38'ini geri kazandırır; yüksek seyir hızında rotor kaynaklı sürükleme
  kanadın biçim sürüklemesini geçer
- **Fatura 3 — boyutlandırma:** hover gücü seyir gücünün kat kat üstünde; güç sistemi
  görevin %2'sine göre boyutlanır
- **Dönüştürülebilirlik:** ayrık elektrikli kaldırma fatura 3'ü çözer ama 1'e çevirir;
  katlanabilir rotor 2'ye saldırır ama mekanizma ekler; tilt 1'den kaçar ama mekanik
  karmaşıklık, jiroskopik moment ve geçiş kontrolü getirir
- **Pazar sonucu:** hibrit dar bir banda sıkışır — altında multirotor ucuz, üstünde
  piste dayalı sabit kanat verimli

*Uzunluk:* ~2 sayfa. **Makalenin omurgası budur.**

---

### 4. Proposed configuration
**İddia:** Kuyruğa oturan, kanat-gövde, kumanda yüzeyi olmayan, tüm kumandasını sabit
pervanelerden alan bir konfigürasyon, üç faturayı da doğurmadan aynı kabiliyeti verir.

*Alt bölümler:*
- **4.1 Overview** — konfigürasyonun tek şekilde özeti
- **4.2 Planform** — kanat-gövde; değişken ok açısı (burunda 40°, arkada 20°); ok
  açısının çift görevi (aerodinamik + kuyruksuz yunuslama kolu); uç tutukluğu
  önlemesi; kalınlık ve veter dağılımının ok açısıyla birlikte hareketi
- **4.3 Propulsion** — koaksiyel karşıt dönüşlü çiftler; tek gerekçe ters tork
  eliminasyonu; net açısal momentumun da sıfırlanması ve geçişte jiroskopik momentin
  doğmaması; seri hibrit (yakıt → motor → jeneratör → elektrikli rotorlar); motorun
  seyre göre boyutlandırılması ve hover tepesinin pil tamponundan karşılanması
- **4.4 Control without control surfaces** — burunda itki, uçlarda yalnız kumanda;
  yunuslama ve yönelme moment denklemleri; **yuvarlanma momentinin paralel itkilerle
  üretilemeyeceğinin gösterilmesi** ve gövde altı kanatçık çözümü; kanatçığın ana
  pervane izinde çalışması (q = T/A) ve böylece sıfır hava hızında da moment üretmesi
- **4.5 Structure and ground contact** — uç iskeletleri; beş nokta temas; iskeletin
  aynı zamanda iniş yapısı olması

*Uzunluk:* ~3 sayfa. En çok şekil bu bölümde.

---

### 5. How the architectural tax is avoided
**İddia:** Üç fatura, bu konfigürasyonda ödenmez — çünkü hover ve seyir **aynı
donanımı** kullanır.

*İçerik:* Bölüm 3'ün üç faturasına birebir cevap.
- Fatura 1 — ikinci itki seti yok; aynı pervaneler her iki rejimde çalışır
- Fatura 2 — seyirde açıkta duran kaldırma rotoru yok
- Fatura 3 — güç sistemi seyre göre boyutlanır; hover tepesi ≈%3 MTOW'luk pil
  tamponundan karşılanır
- **Ödenen bedel dürüstçe:** kumanda pervanelerinin ölü ağırlığı (askı gücünün
  %15'inden azı), uç iskeletlerinin sürüklemesi, ve geçiş manevrası

*Uzunluk:* ~1,5 sayfa. **Makalenin ödeme noktası.**

---

### 6. Reference designs at two scales
**İddia:** Aynı konfigürasyon, 20 kat kütle aralığında aynı oranlarla çalışır.

*İçerik:*
- **6.1 Sizing method** — kullanılan denklemler ve varsayımlar açıkça
- **6.2 Light reference, 50 kg** — geometri, güç, menzil
- **6.3 Heavy reference, 1000 kg** — aynı şekil, 3,35 kat uzunluk ölçeği
- **6.4 Scale behaviour** — sabit disk yüklemesi kuralı; askı gücünün L^3,5 ile
  büyümesi ve mevcut gücün L³ ile büyümesi; **geçiş süresinin ölçek-değişmez
  olmadığı** (ağır hat 4 s)
- **6.5 Context** — mevcut VTOL araçların MTOW tablosu, kaynaklarıyla ve tanım
  uyarılarıyla. **Karşılaştırma yapılır, hüküm verilmez.**

*Uzunluk:* ~2,5 sayfa.

---

### 7. Flight profile and transition
**İddia:** Geçiş, hover'dan başladığı için aerodinamik dirençle karşılaşmaz; hızlı
yunuslama irtifa kaybını karesel olarak azaltır ve kanat birkaç saniyede devralır.

*İçerik:*
- Beş aşama: duruş, kalkış, geçiş, seyir, iniş
- Geçişin başlangıcında q → 0; kritik bölge orta yay
- T = W/cosθ ve yatay ivme g·tanθ; itki tekilliğine neden ulaşılamadığı
- İrtifa kaybı ∝ t_r², gereken kumanda itkisi ∝ 1/t_r²; optimumun uç pervanelerini
  boyutlandırması

*Uzunluk:* ~1,5 sayfa. Hakemin en çok kazacağı yer burasıdır; en dikkatli yazılacak
bölüm de budur.

---

### 8. Limitations
**İddia:** Bu bir konfigürasyon çalışmasıdır; deneysel doğrulama içermez.

*Açıkça söylenecekler:*
- CFD yok, rüzgâr tüneli yok, uçuş testi yok
- Kütle bütçesi bir **hedeftir**, bulgu değil; kâğıt uçaklar tipik olarak %20–40
  hafif çıkar
- Ok açıları seçilmiştir; transonik literatürden alınan bant kendi rejimimize göre
  yeniden türetilmemiştir
- Yuvarlanma otoritesi mertebe tahminidir; sönümleme ve kanatçık etkinliği katsayıları
  literatürden alınmıştır
- Sabit geometri, tam tork dengesini tek noktada verir; **seçilen nokta seyirdir** ve
  hover'da küçük bir artık tork kalır
- Girdap halkası durumu, dik inişte incelenmemiştir

*Uzunluk:* ~1 sayfa. **Bu bölüm makalenin güvenilirliğini kurar, zayıflatmaz.**

---

### 9. Conclusion
**İddia:** Faturanın mimariden doğduğu gösterildi; onu doğurmayan bir mimari önerildi
ve iki ölçekte sayıya döküldü.

*Uzunluk:* ~0,5 sayfa.

---

## Şekil planı

| # | Şekil | Kaynak |
|---|---|---|
| 1 | İki aile ve sınırları — kavramsal | çizilecek |
| 2 | Yetmiş yıllık deneme zaman çizelgesi | çizilecek |
| 3 | Üç fatura ve birbirine dönüşümü | çizilecek |
| 4 | Konfigürasyon — üç görünüş (üst, yan, ön) | 3B model |
| 5 | Konfigürasyon — serbest görünüş | 3B model |
| 6 | Değişken ok açısı ve kalınlık dağılımı | 3B model + grafik |
| 7 | Pervane yerleşimi ve moment kolları | çizilecek |
| 8 | Kanatçık ve ana pervane izi | 3B model + çizim |
| 9 | Uçuş profili, beş aşama | çizilecek |
| 10 | Geçiş: irtifa kaybı ve kumanda itkisi, t_r'ye göre | grafik |
| 11 | İki hat yan yana, aynı ölçekte | 3B model |
| 12 | Faydalı yük oranı – menzil düzlemi, üç aile | grafik (N60) |

## Tablo planı

| # | Tablo |
|---|---|
| 1 | Üç fatura ve mimarilere göre ödenme biçimi |
| 2 | İki referans tasarımın karşılaştırması |
| 3 | Mevcut VTOL araçların MTOW'ları, kaynaklarıyla |
| 4 | Geçiş süresi ve kumanda gücü, iki hat için |

---

## Karar bekleyen üç şey

1. **Hedef mecra.** Yapıyı, uzunluğu ve biçimi belirler.
2. **Başlık.** Mimariyi işaret etmeli, aracı değil.
3. **Yazar ve kurum satırı.** Bağımsız mucit olarak mı, bir bağlantı üzerinden mi.
