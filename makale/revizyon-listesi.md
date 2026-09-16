# Revizyonda düzeltilecekler

Makale *Drones*'a gönderildi (`drones-4595522`), **masadan reddedildi ve
*Aerospace*'e aktarılıp orada da masadan reddedildi** — 2026-09-15, hakeme
gitmeden. Kayıt ve öğrenilenler: `drones-gonderim.md` §10. Bu liste, gönderimden
**sonra** bulunan ve bir sonraki sürümde düzeltilecek olan şeyleri tutar; artık
hakem raporunu beklemiyor.

Şu anda makaleye dokunmuyoruz: gönderilen dosya ile depodaki dosya ayrışırsa, bu depoda
iki kez bedeli ödenmiş olan "aynı ad, iki içerik" sorunu yeniden doğar.
`SURUMLER.md` kuralı geçerli — düzeltme yeni sürüm numarası alır ve o sürüm
revizyonla birlikte üretilir.

---

## 0. HEDEF DERGİNİN KENDİ ŞARTI — v8'de her şeyden önce gelen madde

*Drones*'un aims & scope sayfasında yazılı, denetlenebilir bir şart var. Tur 27'de
iki dış okuyucu söyledi, ben doğruladım:

> "If the manuscript is dealing with general theoretical aircraft design, it is
> recommended to validate the theoretical/numerical results with experimental data
> from a study of an unmanned platform, **at least at a laboratory scale**."

Makalemiz genel teorik uçak tasarımıdır, **hiçbir deneysel verisi yoktur** ve bunu
kendi özetinde söyler. Yani "kapsam dışı" büyük olasılıkla nazik bir kalıp değil,
**birebir doğru** bir tespitti.

**Bu benim hatam ve gönderimdeki en büyüğü.** `drones-gonderim.md` formun dokuz
bölümünü adım adım yürüdü; derginin kendi şartlarını makaleyle hiç karşılaştırmadı.
Denetlenen her şey iyi denetlendi — sayılar, bağlar, şekil sırası — ve sonucu
belirleyen tek şey hiç açılmadı.

**v8 kuralı, mekanik:** bir hedef dergi adı konmadan önce o derginin aims, scope ve
özel şartları baştan sona okunur ve **şart şart** makaleyle karşılaştırılıp yazılır.
Makaleyi kendine karşı denetleyip yere karşı hiç denetlemeyen bir düzen, yanlış şeyi
denetliyor demektir.

---

## 1. EKSİK KAYNAK — **YAZAR KARARI: KOŞULSUZ, HANGİ DERGİ OLURSA OLSUN**

**Yazarın 2026-09-16 talimatı:** Bacchini 2021 kaynağı, hangi dergiye gidilirse
gidilsin, hesap istemeyen bir yere gidilse bile, **profesyonel biçimde tamamlanacak.**
Bu madde artık isteğe bağlı değil ve bir dergi şartına bağlı değil. Kaynak birinci
elden okunacak, §3.3'e girecek, ve bizim hesabımızla ölçümü karşılaştırılacak.


**Bacchini, A.; Cestino, E.; Magill, B.; Verstraete, D. *Impact of lift propeller
drag on the performance of eVTOL lift+cruise aircraft.* Aerospace Science and
Technology **2021**, 109, 106429.**

Bu makale **tam olarak bizim en büyük defter kalemimizin konusu**: seyirde kaldıraç
pervanelerinin sürüklemesi, ve **rüzgâr tünelinde ölçülmüş.** Pervaneleri geri
çekmek parazit sürüklemeyi %38 azaltıyor, menzili %13 artırıyor.

**Biz aynı olguyu pervane-element momentum kuramıyla hesaplıyoruz (0,0154) ve bu
ölçümü hiç anmıyoruz.** Kaynakçada yok. `00-on-bilgi.md` içindeki bir not, %38/%13
sayılarının *"kaynak henüz birinci elden okunmadı"* diye bilerek dışarıda
bırakıldığını söylüyor — yani bilerek yapıldı, ama gerekçe artık geçerli değil:
makale o olguyu hesaplayan bir bölüm taşıyor.

**Neden ciddi:** aynı grubun *başka* verisini (Tablo 1'in rüzgâr tüneli L/D
değerleri, 13/17 seyir cezası) makalenin omurgasında kullanıyoruz. Onların en
ilgili çalışmasını atlamış görünmek, seçici alıntı izlenimi verir.

**Yapılacak:** kaynağı birinci elden oku, §3.3'e ekle, ve hesabımızla ölçümlerini
karşılaştır. Ölçüm *durdurulmuş/geri çekilmiş* pervane için, bizimki *serbest
dönen* için — aynı şey değil, ve bu farkı yazmak hesabı zayıflatmaz, konumlandırır.

---

## 2. Giriş §1.4'te tekrar

Şu iki cümle üst üste duruyor:

> "...and it is to them, not to any aerodynamic shortcoming, that this paper offers
> an alternative. **This paper offers an alternative route to the same end.**"

Aynı şey iki kez. Tur 25 düzeltmesini yaparken eskisini silmemişim. Olgusal hata
değil, sadece tekrar — ama Giriş'te ve göze çarpar.

**Yapılacak:** ikinci cümleyi sil.

---

## 3. Beklenen hakem itirazları ve hazır cevaplar

Bunlar kusur değil; gönderimden önce dört dış okumanın "hakem şunu soracak"
dediği şeyler. Rapor gelince hangisinin geldiğine bakılır.

| İtiraz | Hazır cevap nerede |
|---|---|
| Mekanizma avantajının nicel karşılaştırması yok (kütle, arıza kipi, güvenilirlik) | İddia bir **sayım**, güvenilirlik iddiası değil; makale bunu açıkça söylüyor |
| Yatış otoritesi ΔC_L ≈ 0,12 ödünç alınmış, bu geometride ölçülmemiş | §2.10 ve §4.6 açık madde olarak taşıyor |
| Şerit eyleyicisi boyutlandırılmamış, üstelik pervane izinde (bant genişliği, yorulma) | §4.6'da açık madde |
| Ağır hat için sürükleme bandı hesaplanmamış | §3.8 asimetriyi adlandırıyor |
| Serbest dönme ile kenarı öne kilitleme arasındaki ticaret fiyatlanmamış (yirmi kat) | §3.3 ve §4.6'da açık madde |
| Makale uzun (35 969 + 32 393 kelime, 79 + 60 sayfa) | `drones-gonderim.md` 7. maddede hazır cevap |

---

## 4. İsteğe bağlı, zamanı olursa

- **Tablo 8'i ortak sürükleme tabanında yeniden hesapla.** Şu an karışık taban
  olduğu üstyazıda yazılı ve nitel sonuç tabandan bağımsız, ama iki dış okuma
  "vakit varsa yap" dedi.
- **Grafik özet (graphical abstract).** MDPI isteğe bağlı tutuyor; revizyonda
  eklenebilir ve görünürlüğe yarar.
- **600 dpi yeniden dışa aktarım** gerekirse; şu an en düşük şekil 387 dpi ve
  MDPI'ın 300 sınırının üstünde.
- **Depo için ayrı bir Zenodo DOI'si üret** (GitHub–Zenodo bağı). Şu an Data
  Availability alanında depo için çıplak GitHub bağı var; bir hakem haklı olarak
  "GitHub kalıcı değil" diyebilir. Kabul öncesi yapılırsa son nüshaya girer.
