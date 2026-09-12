# Zenodo v5 — ne yüklenecek, hangi alana ne yazılacak

Bu dosya senin için. Zenodo'ya ben giremiyorum; aşağısı el ile yapılacak işin
tamamı, sırayla.

---

## 1. Doğru yere yükle

v4 kaydına git (`zenodo.org/records/22664634`) ve **"New version"** de. Sıfırdan
yeni kayıt açma — o zaman concept DOI kopar, v3 → v4 → v5 zinciri bozulur ve
makalede "the repository this paper cites" dediğimiz şey iki ayrı yere işaret
etmeye başlar.

Yeni sürüm kendi DOI'sini alır; eski sürümlerin DOI'leri çalışmaya devam eder.

## 2. Yüklenecek dosyalar

| Dosya | Nereden |
|---|---|
| `meryemAircraft-makale.pdf` | `makale/pdf/` — şekilli ana makale |
| `meryemAircraft-ek.pdf` | `makale/pdf/` — altı ek, tek belge |
| `makale-v5.md` | `makale/` — makine okunabilir hali |
| `makale-v5-ek.md` | `makale/` — eklerin markdown hali |

Önceki sürümün dosyaları taşınmaz; her sürüm kendi dosya setini tutar.

**Markdown'ları da koymamın sebebi:** bazı yapay zekâ ortamları PDF açamıyor ama
düz metni okuyabiliyor. Bu turda tam olarak o sorunu yaşadık.

## 3. Alanlara ne yazılacak

**Version:** `5`

**Publication date:** yüklediğin gün

**Title:** değişmiyor —
*The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven
Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System*

**Description:** `makale/zenodo-v5.md` dosyasının tamamı. Önce sürüm notu, sonra
`---`, sonra özet. v3 ve v4'te de bu düzen kullanıldı.

**Authors:** Meryem Gülmen, Berke Gülmen, Ömer Gülmen — hepsi *Independent
Researcher*. ORCID varsa ekle; zorunlu değil.

**Keywords:** ön bilgideki yedi anahtar kelimenin aynısı.

**License:** v4'te ne seçildiyse aynısı. Değiştirme — sürümler arasında lisans
değişikliği okuyucuyu şaşırtır.

**Related identifiers:** `https://github.com/LORDTEK/meryemAircraft` →
*is supplemented by*.

## 4. Yükledikten sonra bana söyle

Yeni kaydın DOI'sini ya da bağlantısını ver. `cfd/dis-gorus-20-*.md` içinde
**iki yerde** `[ZENODO-V5-BAĞLANTISI]` yazan yer tutucu var; onları doldurup
metni sana geri veririm. O metin yapay zekâlara gidecek olan.

---

## Bir not — makale henüz dergiye gitmedi

Zenodo kaydı bir ön baskı değil, bir **çalışma kaydı**. Dergi (Drones) daha
önce yayımlanmamış olmayı şart koşuyor ama hakem sürecinden geçmemiş ön baskıları
kabul ediyor. Zenodo'ya koymak gönderimi engellemiyor.

Yine de gönderim sırasında **kapak mektubunda** Zenodo kaydından söz et — dergi
"daha önce çevrimiçi erişime açılmış mı" diye sorduğunda cevap hazır olsun. Bunu
saklamak, sonradan çıkması hâlinde gereksiz bir sorun yaratır.
