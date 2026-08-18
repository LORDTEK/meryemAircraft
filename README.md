# meryemAircraft

Yeni bir hava aracı tasarımının anlatım ve yayın deposu.

Bu depo bir yazılım projesi değil; bir **tasarımın anlatıya dönüştürülmesi** projesidir.
Amaç, tasarımı önce metinle olgunlaştırmak, sonra sırasıyla makale, görsel, sunum ve
video çıktılarına dökmektir.

## Yol haritası

| Aşama | Çıktı | Durum |
|-------|-------|-------|
| 1 | Tasarım künyesi — tasarımın yazıya dökülmüş tam tanımı | başlıyor |
| 2 | Makale | bekliyor |
| 3 | Görseller (şema, kesit, render) | bekliyor |
| 4 | Sunum | bekliyor |
| 5 | Video | bekliyor |

## Dizin yapısı

```
tasarim/     Tasarımın kendisi: künye, teknik notlar, hesaplar, karar kayıtları
makale/      Makale metni; bolumler/ altında bölüm bölüm taslaklar
gorsel/      kaynak/ düzenlenebilir dosyalar (svg, cad, blend)
             cikti/  yayına hazır dışa aktarımlar (png, pdf)
sunum/       Sunum dosyaları ve konuşma notları
video/       senaryo/ altında metin ve storyboard; kurgu notları
kaynakca/    Kaynaklar, atıflar, okunan literatür
```

## Çalışma ilkesi

Her aşama bir öncekini kaynak alır. Makale tasarım künyesinden, görseller makaleden,
sunum ve video da makale ile görsellerden türer. Böylece sayı, terim ve iddialar
tüm çıktılarda tutarlı kalır; bir yerde düzeltme yapıldığında nereye yayılacağı bellidir.

## Lisans

AGPL-3.0 — bkz. [LICENSE](LICENSE).
