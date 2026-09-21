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
- **İrtifa.** Hesaplar deniz seviyesinde; NASA karşılaştırması 5.000 ft + ISA+20°C'de.
  Seyir karşılaştırmasına etkisinin **yönü hesaplanmadı.**

## Süreç kalemleri

- Zenodo DOI, başlık (≤12 kelime), özet (100–200 kelime)
- Şekillerin 600 dpi yeniden dışa aktarımı, üstyazılar 20–25 kelimeye
- Boş `presentation/` ve `video/` dizinleri
- Ulaşılamayan commit `942bf452…` için GitHub gc
