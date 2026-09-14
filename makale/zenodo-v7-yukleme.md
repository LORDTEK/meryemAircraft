# Zenodo v7 — ne yüklenecek, hangi alana ne yazılacak

Bu dosya senin için. Zenodo'ya ben giremiyorum; aşağısı el ile yapılacak işin
tamamı, sırayla.

---

## 1. Doğru yere yükle

**v6 kaydına git ve "New version" de.** Sıfırdan yeni kayıt açma — o zaman
concept DOI kopar, v3 → v4 → v5 → v6 → v7 zinciri bozulur ve makalenin kendi
Data Availability bölümünde işaret ettiği `10.5281/zenodo.22144194` iki ayrı
yere bakmaya başlar.

Yeni sürüm kendi DOI'sini alır; **v6'nın DOI'si çalışmaya devam eder ve etmeli.**
v6 geri çekilmiyor, düzeltiliyor.

## 2. Yüklenecek dosyalar

| Dosya | Nereden | Ne |
|---|---|---|
| `meryemAircraft-makale.pdf` | `makale/pdf/` | Şekilli ana makale |
| `meryemAircraft-ek.pdf` | `makale/pdf/` | Altı ek, tek belge |
| `makale-v7.md` | `makale/` | Makine okunabilir ana metin |
| `makale-v7-ek.md` | `makale/` | Eklerin markdown hali |

Önceki sürümün dosyaları taşınmaz; her sürüm kendi dosya setini tutar.
v6'nın dosyaları v6 kaydında kalır ve **oradan silinmez.**

`zenodo-v7.md` bir *içerik* dosyası değildir, **Description alanına
yapıştırılacak metindir.** Yüklenecek dosyalar listesinde yeri yoktur.

## 3. Alanlar

**Version:** `v7`

**Publication date:** yükleme günü

**Title, Authors, Keywords, Lisans:** v6 ile aynı, dokunma.

**Description:** `makale/zenodo-v7.md` içeriğini olduğu gibi yapıştır. Metin
v6'dan v7'ye her değişikliği sırayla anlatır ve **düzeltmenin neden gerektiğini
açıkça yazar.**

## 4. İzin meselesi — senin işin, ama ne olduğunu net yazayım

v6'nın Giriş bölümüne şu cümle konmuştu:

> *"No claim of general architectural superiority is made anywhere in this paper."*

Bu cümleyi **ben yazdım, senin onayın olmadan**, ve kapsam disiplini sanarak
yazdım. Yanlıştı: makalenin kazandığı iki iddiayı reddediyor ve aynı belgenin
4.2 bölümüyle çelişiyordu. Yani yayımlanmış v6, kendi tezini bir yerde
savunup başka bir yerde inkâr ediyor.

`zenodo-v7.md`'nin ikinci paragrafı bunu **açıkça** söylüyor: cümlenin
sorumlu yazarın onayı olmadan eklendiği, neden yanlış olduğu ve neyle
değiştirildiği yazılı. İzin sürecinde göstereceğin metin bu paragraftır.

## 5. Yükledikten sonra

Yeni sürüm DOI'sini bana söyle. Makalenin kendisi **concept DOI**'yi taşıyor
(`10.5281/zenodo.22144194`), yani metinde değişecek bir şey yok — ama
`drones-gonderim.md`'deki gönderim notuna sürüm DOI'sini de eklerim.

## 6. Bu sürümün parmak izi

Zenodo'ya yüklediğin dosyanın doğru dosya olduğunu şuradan doğrulayabilirsin:

| | |
|---|---|
| `makale-v7.md` SHA-256 (ilk 12) | aşağıdaki komut verir |
| commit | `git log -1` |

```
sha256sum makale/makale-v7.md | cut -c1-12
```

Depodaki `makale-v6.md` **yatırılan v6'ya geri alındı**, yani artık Zenodo'daki
v6 ile birebir aynı. Bir süre öyle değildi ve bunu `makale/SURUMLER.md`
anlatıyor: yayımlanmış bir sürümün dosyası bir daha değiştirilmez, düzeltme
yeni sürüm numarası alır.
