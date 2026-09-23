# Ertelenmiş kararlar — yazarın açıkça "sonraya" dediği şeyler

**Bu dosyanın var olma nedeni:** yazar Tur 50'de şunu söyledi —
*"Ben unutabilirim sen sağa sola notunu al."*
Burası o not. **Her tur sonunda bu listeye bakılır.**

---

## Açık — henüz karar verilmedi

| # | Konu | Durum | Kim gündeme getirdi |
|---|---|---|---|
| **E1** | **Kısaltma / oran.** Adım 1'in 1954 XFV-1 / XFY-1 anlatısı (~800 kelime) boşluk iddiası daraldıktan sonra "dekoratif" hâle geldi. Ayrıca 2 ile 4 arasında, ve 3'ün izin verilen maliyetler listesi ile 7'nin "koşulun söylemedikleri" arasında yineleme var. | **ERTELENDİ.** Yazar, Tur 50: *"Kısaltma en son yapacağız şimdi değil."* 10–14 yazıldıktan sonra tek seferde yapılacak. | DeepSeek, Grok |
| **E2** | **"Zero-bill condition" adı.** Ad sayısal, koşul yapısal. Adım 2'nin tilt satırı düzeltilince (Fatura 3 ayakta kalıyor) ad savunulabilir hâle geldi, ama gerginlik duruyor. Alternatifler: *"the single-propulsor condition"*, *"the no-reorientation condition"*. | **ERTELENDİ.** Yazar, Tur 50: *"Ad konusu da sonraya bırakılabilir."* | DeepSeek, Grok |

## Karara bağlanmış — kayıt için

| # | Konu | Karar | Tur |
|---|---|---|---|
| K1 | Açıklık verimi | **0,817** — ve denetimde zaten kullanıldığı çıktı (`drag_sweep.py:40`) | 50 |
| K2 | Palet ailesi | **Zarf olarak kalsın.** Mekanizma: `baseline.py` L/D'yi girdi alıyor, dört köşe = dört kapanış | 50 |
| K3 | Adım 10'un C_D0'ı | **Tutarlı braket 0,0285–0,0381.** Yayımlanan 0,0248 braketin iki ucunun da altında | 50, dördü de hemfikir |
| K4 | Katkı sayısı | **Tek katkı: mimari** | 35 (`CLAUDE.md` §0.6) |
| K5 | Hedef dergi | *Journal of Aircraft* (AIAA) | — (`CLAUDE.md` §4) |

## Açık teknik kalemler — makalede "hesaplanmadı" diye duruyor

Bunlar karar değil, **yapılmamış iş.** Adım 14'ün malzemesi.

- **Tepki torku kanalını bırakmanın bedeli.** İtki asimetrisi, verim kaybı, rotor ataletinden
  gelen gecikme. Hiçbiri hesaplanmadı. Bir kontrol tahsis çalışması gerektirir.
- **Kapalı çevrim askı kontrolü.** Momentler hesaplandı, tahsis kapatılmadı, hiçbir şey
  benzetilmedi.
- **Dikey iniş ve girdap halkası durumu.** Analiz edilmedi.
- **İniş geçişi.** İleri geçişle simetrik değil; hiçbir şekil tarif etmiyor.
- **Geçiş yunuslama momenti.** Üç yöntem üç aslılıkta ~10° üstünde sapıyor; ölçüme ait.
- **Motor yerleşimi, hava alışı, soğutma.** Makalede hiç yok (arandı).
- **Tamponu askı enerjisinden türetmek.** Tampon her iki ölçekte de GİRDİ (%3,6 / %4,0);
  hiçbir kod onu askı enerjisinden türetmiyor. Bu yüzden Fatura 1 ölçekte sınanamıyor (Adım 12)
  ve hafif ölçekte açık kW/kg %17 oynarken sabit kalıyor (Adım 11). Türetmek batarya özgül gücü
  sorusuna girer — **Adım 14'ün 3,8× paragrafıyla birlikte ele alınmalı.**
- **İrtifa.** Hesaplar deniz seviyesinde; NASA karşılaştırması 5.000 ft + ISA+20°C'de.
  Seyir karşılaştırmasına etkisinin **yönü hesaplanmadı.**

## Adım 11 yazılmadan önce okunacak — DeepSeek'in çift sayım uyarısı, Tur 52

Adım 10'un sayıları şunları **zaten** içeriyor:

| Kalem | Nerede |
|---|---|
| Uç çerçeve sürüklemesi + serbest dönen rotorlar | L/D braketinin içinde (8,79–10,82) |
| Sabit hatve uzlaşması | η_p aralığının içinde (0,632–0,683) |
| Burulma bedeli | açıklık veriminin içinde (0,817) |
| Hepsinin kütle ve güç sonuçları | MTOW'un içinde (52,3–57,5 kg) |

> **Defter bunları TEKRAR eklerse, ChatGPT ve Grok'un döngüde yakaladığı çift sayımın düz yazı
> hâlidir.** Defterin işi: kapanışın sayılarının **neyi zaten içerdiğini çözmek**, ve **neyi
> içermediğini adlandırmak** — tepki torku kanalını bırakmanın bedeli, 5,4 m geçiş tabanı,
> şeridin eyleyici kütlesi, uç çiftlerine bağlı kalkış marjı.
>
> **Özellikle sabit hatve:** *"ve sabit hatve uzlaşması %X'e mal oluyor"* denmez. Denecek olan:
> *"yayımlanan zincirin varsaydığı 0,80'e karşı hesaplanan 0,632–0,683 sabit hatve uzlaşmasını
> yansıtıyor; bu çalışma onu kaynak başına ayrıştırmıyor."*

## Süreç kalemleri

- Zenodo DOI, başlık (≤12 kelime), özet (100–200 kelime)
- Şekillerin 600 dpi yeniden dışa aktarımı, üstyazılar 20–25 kelimeye
- Boş `presentation/` ve `video/` dizinleri
- Ulaşılamayan commit `942bf452…` için GitHub gc
