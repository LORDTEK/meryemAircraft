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
| `meryemAircraft-paper.pdf` | `paper/pdf/` — şekilli ana makale |
| `meryemAircraft-ek.pdf` | `paper/pdf/` — altı ek, tek belge |
| `paper-v5.md` | `paper/` — makine okunabilir hali |
| `paper-v5-supp.md` | `paper/` — eklerin markdown hali |

Önceki sürümün dosyaları taşınmaz; her sürüm kendi dosya setini tutar.

**`zenodo-v5-ek.md` diye bir dosya YOK ve olmamalı.** Adlandırmam yanıltıcıydı,
açıklayayım: `zenodo-v5.md` bir *içerik* dosyası değil, Zenodo'nun **Description
alanına yapıştırılacak metin**. Bir kaydın bir tane Description'ı olur, o yüzden
tek dosya. Ek malzeme ise kaydın *içindeki bir dosya* — yukarıdaki tabloda
`meryemAircraft-ek.pdf` ve `paper-v5-supp.md` olarak duruyor. İkisi farklı katman:
biri kaydın metni, diğeri kaydın eki.

**Markdown'ları da koymamın sebebi:** bazı yapay zekâ ortamları PDF açamıyor ama
düz metni okuyabiliyor. Bu turda tam olarak o sorunu yaşadık.

## 3. Alanlara ne yazılacak

**Version:** `5`

**Publication date:** yüklediğin gün

**Title:** değişmiyor —
*The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven
Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System*

**Description:** `paper/zenodo-v5.md` dosyasının tamamı. Önce sürüm notu, sonra
`---`, sonra özet. v3 ve v4'te de bu düzen kullanıldı.

**Authors:** Meryem Gülmen, Berke Gülmen, Ömer Gülmen — hepsi *Independent
Researcher*. ORCID varsa ekle; zorunlu değil.

**Keywords:** ön bilgideki yedi anahtar kelimenin aynısı.

**License:** v4'te ne seçildiyse aynısı. Değiştirme — sürümler arasında lisans
değişikliği okuyucuyu şaşırtır.

**Related identifiers:** `https://github.com/LORDTEK/meryemAircraft` →
*is supplemented by*.

## 4. Yükledikten sonra: **kök DOI'yi** al, sürüm DOI'sini değil

Bu ayrım önemli, çünkü yanlışını verirsek yapay zekâlar altı ay sonra eski bir
sürüme bakıp düzelttiğimiz hataları bize geri raporlar.

Zenodo her kayda **iki** DOI verir:

| | ne yapar |
|---|---|
| **Sürüm DOI'si** | yalnız v5'e çözülür, sonsuza kadar orada kalır |
| **Kök DOI** (concept / all-versions) | **her zaman en son sürüme** çözülür |

Soru metninde **kök DOI** kullanılacak. Böylece v6 çıktığında aynı bağlantı
kendiliğinden v6'yı gösterir ve metni güncellemek gerekmez.

**Nerede yazıyor:** kayıt sayfasının sağ sütununda, *Citation* / *Versions*
bloğunun altında şuna benzer bir cümle var:

> *"Cite all versions? You can cite all versions by using the DOI
> 10.5281/zenodo.XXXXXXX. This DOI represents all versions, and will always
> resolve to the latest one."*

O cümledeki numara kök DOI. Bana onu ver.

**Kullanılan kök adres:** `https://zenodo.org/records/22144194`
(soru metnine yerleştirildi).

*[Doğrulayamadım — Zenodo bu ortamda proxy'de bloklu, ne API ne sayfa açılıyor.
Numaranın kök olduğuna dair dolaylı bir işaret var: 22144194 < 22664634, yani v4
sürüm kaydından küçük, ve Zenodo kök kimliği ilk yatırımda ayırdığı için bu
beklenen düzen. Ama işaret kanıt değil.

**Bir kez şunu kontrol et:** o adresi aç, sayfa "Version 5" gösteriyor mu? Ve sağ
sütunda "This DOI represents all versions, and will always resolve to the latest
one" cümlesi var mı? İkisi de varsa doğru adres. Yoksa söyle, değiştiririm.]*

*[Not: Zenodo bu ortamda proxy tarafından bloklu, kök DOI'yi ben çekemedim.
Numarayı senin kopyalaman gerek.]*

Metin ayrıca bir **sürüm kontrolü** taşıyor: yapay zekâya "v5 / 12 Eylül 2026
arıyorsun, ve metinden şu üç şeyle doğrulayabilirsin — beş bölüm, tampon 5,63
kW/kg, özet uçağın uçabilir gösterilmediğini söylüyor" diyor. Kök DOI yanlışlıkla
eski bir kayda düşerse bile yapay zekâ kendi yakalar.

---

## Bir not — makale henüz dergiye gitmedi

Zenodo kaydı bir ön baskı değil, bir **çalışma kaydı**. Dergi (Drones) daha
önce yayımlanmamış olmayı şart koşuyor ama hakem sürecinden geçmemiş ön baskıları
kabul ediyor. Zenodo'ya koymak gönderimi engellemiyor.

Yine de gönderim sırasında **kapak mektubunda** Zenodo kaydından söz et — dergi
"daha önce çevrimiçi erişime açılmış mı" diye sorduğunda cevap hazır olsun. Bunu
saklamak, sonradan çıkması hâlinde gereksiz bir sorun yaratır.
