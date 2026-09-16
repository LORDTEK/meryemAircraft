# meryemAircraft — çalışma kuralları

## 0. İDDİANIN NE OLDUĞU. Bunu bir daha kaçırma.

Bu çalışmanın **var oluş nedeni mimari yeniliktir.** Menzil rekoru değildir.
Aşağıdaki dört satır projenin omurgasıdır ve her metin, her düzeltme, her
özet bunlarla tutarlı olmak zorundadır.

**Rakip kim, hangi eksende — dördü de ayrı:**

| Eksen | Rakip | Durum |
|---|---|---|
| **Menzil / seyir verimi** | **Çok rotorlu (quadcopter)** | **Yeniyoruz. Yeter.** |
| **Piste ihtiyaç / dikey iniş kalkış** | **Sabit kanatlı** | **Yeniyoruz. İnşa gereği.** |
| **Mekanik ve kontrol basitliği** | **Tilt mimarileri** | **Asıl katkı bu.** |
| Menzil, öteki hibritlere karşı | Lift+cruise, tilt | **İDDİA EDİLMİYOR.** Sözleşmeye göre tersine döner. |

**Yapılmayacak iki hata — ikisini de yaptım, ikisi de yazar tarafından
yakalandı:**

1. **Sabit kanatlıyla menzilde yarışmak.** Planörden daha uzağa gitmeyi kim
   iddia edebilir? Neden edelim? Mesafede çok rotorluyu yenmek yeterlidir.
2. **Çok rotorluyla dikey iniş kalkışta yarışmak.** Saçmadır. O eksende
   rakibimiz sabit kanatlıdır ve üstünlük inşa gereğidir.

Ben uzun süre tam tersini yaptım: menzilde sabit kanatla, taktik avantajda
çok rotorluyla yarıştım. Her karşılaştırmayı yanlış rakibe karşı kurdum.

**Tilt mimarilerine karşı iddia menzil DEĞİLDİR, mekanizmadır.** Tiltler
bugün yaygın değil; nedeni mekanik karmaşıklık, gyroskopik bağlaşım ve geçiş
kontrol problemi. Bu çalışma **o probleme alternatif bir çözüm öneriyor:**
aynı rejim geçişi, dönen hiçbir mekanizma olmadan, kumanda yüzeyi olmadan,
değişken hatve olmadan — yalnız sabit hatveli pervanelerin diferansiyel
itkisiyle. Katkı budur.

**Sayılar değişmez.** Menzil açığı 24–45 %, kütle üstünlüğü 32–36 %, bunların
hepsi dürüstçe raporlanmaya devam eder. Değişen şey **neyin iddia edildiğidir.**
Öteki hibritlere karşı menzil sıralaması bir boyutlandırma sonucudur, tez
değildir.

**"Genel mimari üstünlük iddiası yoktur" gibi bir cümle bir daha yazılmaz.**
Bir kez yazıldı, 4.2 ile çelişti ve makalenin kendi tezini inkâr etti.

### 0.1 Üçüncü iddianın SINIRI. Bunu da bir daha aşma.

İddiayı düzeltirken hemen aşırıya kaçtım ve **makalenin kendi §2.10'uyla çelişen**
bir cümle yazdım: *"hareket eden mekanizma yok", "hiçbir aerodinamik kumanda
yüzeyi yok", "her eksendeki her moment diferansiyel itkiden".* Üçü de **yanlış.**

**Yatış (roll) eşeksenli pervanelerle ÜRETİLEMEZ.** §2.10 bunu türetiyor: her
çift eşeksenli ve tork dengeli, hiçbir ayar yatış momenti vermiyor. Yatışı alt
yüzeydeki **değişken uzantılı şerit** sağlıyor ve makale ona *"uçaktaki tek
hareketli aerodinamik yüzey"* diyor.

**Doğru iddia dar olanıdır:**

> Tilt mimarilerine karşı ortadan kaldırılan şey **propulsor'ü yeniden
> yönlendiren mekanizma sınıfıdır** — pivot yok, nasel eyleyicisi yok, değişken
> hatve göbeği yok, dönen kütleden gyroskopik moment yok. **Uçakta hiç hareketli
> parça olmadığı DEĞİL.** Yunuslama ve sapma diferansiyel itkiden; yatış
> şeritten. Eyleyici envanteri: motorlar **artı bir şerit eyleyicisi.**

**"Mekanik olarak daha basit" de denmez** — parça sayısı, kütle, arıza kipi,
bakım hiçbiri ölçülmedi. Denen şey bir **sayımdır**, güvenilirlik iddiası değil.

Bunu üç dış okuyucu bağımsız olarak yakaladı ve biri yanlış dosyayı okurken
yakaladı, çünkü §2.10 her iki sürümde de aynıydı. **Ders: bir iddiayı
düzeltirken, yeni iddianın makalenin kendi bölümleriyle çelişip çelişmediğini
denetle.** Doğru çerçeve, yanlış kapsamla yazılırsa yine yanlıştır.

### 0.2 Aynı hata ÜÇÜNCÜ kez oldu. Kural artık mekanik.

§2.10 çelişkisini düzeltirken §3.17'ye *"şerit yunuslama momenti üretmez"*
yazdım. §2.10 ise şeridin **burnu aşağı yunuslattığını** söylüyor
(ΔC_m 0,005–0,032). Yine düzeltmenin kendisi yeni bir çelişki doğurdu.
Ayrıca dayanağı olmayan bir sayı uydurdum: *"artı bir şerit eyleyicisi."*
Makale şeridin eyleyici sayısını hiçbir yerde vermiyor; §2.10 onu **iki
yarım** olarak tarif ediyor.

**Bundan sonraki kural — istisnasız:**

> Bir iddiayı ya da bir özeti yazdıktan sonra, içindeki **her olgusal
> yüklem** için o iddianın özetlediği bölümü AÇ ve oku. Sayı veriyorsan
> o sayının kaynakta geçtiğini gör. Bir şeyin *olmadığını* söylüyorsan,
> onun olduğunu söyleyen bir bölüm var mı diye ara.

Üç turda üç kez: "hiçbir mimari üstünlük yok" (4.2 ile çelişti),
"hareket eden mekanizma yok" (2.10 ile çelişti), "şerit yunuslama momenti
üretmez" (yine 2.10 ile çelişti). Üçü de **özet yazarken** oldu. Özet
yazmak, bu projede en yüksek hata oranlı iştir.

## 1. Yazışma ve üslup

- Kullanıcıyla **Türkçe**. Öteki YZ'lere (ChatGPT, Grok, DeepSeek, Qwen)
  giden metinler **İngilizce**.
- Acımasız dürüstlük. Cesaretlendirme yok. Aşırı mühendislik yok.
- Kullanıcı YZ yorumlarını uzun uzun okumaz; **özetle.**

## 2. Dış görüş metinlerinin standardı

Her metin **kendi kendine yetmeli** ve süreci çıplaklığıyla ortaya koymalı:
ne yaptın, ne buldun, ne umuyordun, hangi aşamadasın, hangi aşamalar için
özellikle yorum istiyorsun, bir önceki turdaki iddialar ne oldu. **Herkes her
şeyi bilsin.**

- **Okuyucuya dosyayı doğrulama yolu ver:** depo bağı, commit karması,
  SHA-256, birkaç saniyelik arama. Bir okuyucu bayat dosya okuduysa hüküm
  verme, **kontrol imkânı ver.** Bu ders pahalıya öğrenildi.
- Kendi bulgularını ve **kendi hatalarını** da yaz. Bir düzeltmenin yan
  hasarıysa öyle işaretle.
- Büyük aşama öncesi **parça–bütün–parça** okuma iste.

## 3. Doğrulama

Hiçbir iddia denetlenmeden aktarılmaz — ne YZ'lerinki ne benimki.

- `paper/build/verify.py` — sayısal denetim (43 kontrol) + yasaklı bayat
  değer listesi.
- `paper/build/links.py` — bağ dokusu: işaretçiler çözülüyor mu, **doğru
  yere mi** çözülüyor, tablo/şekil atıfları tutuyor mu.
- Bir denetim yazdığında **eski hatayı geri koyup yakalayıp yakalamadığını
  sına.** Sessizce boş dönen bir denetim, hiç olmayandan beterdir; bu bir kez
  oldu.

## 4. Depo

- Geliştirme dalı: `claude/ecstatic-cori-6w30at`. `main` de güncel tutulur.
- **Başka hiçbir repository'ye dokunulmaz.** Başkalarının uzun emeği var.
- Yayın: Zenodo (kök DOI 10.5281/zenodo.22144194), hedef dergi *Drones* (MDPI).
- YZ kullanım beyanında **marka/model/şirket adı geçmez**; YZ yazar satırında
  asla yer almaz.
- Uygulama alanları: **orman yangını gözlem/müdahale** ve **piste ihtiyaç
  duymayan yerlere kargo.**
