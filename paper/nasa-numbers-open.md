# NASA sayıları — AÇIK DOĞRULAMA KALEMİ

**Durum: AÇIK. Hiçbir yeni sayı makaleye girmiyor.**

## Sorun

Tur 43'te Grok, ChatGPT ve Qwen §3.1'in NASA karşılaştırmasını sorguladı ve **tilt-wing'in
brüt ağırlığını** istediler — tablodaki eksik hücre. Üç okuyucu ve bir web araması **dört ayrı
sayı kümesi** verdi:

| Kaynak | tilt-wing DGW | lift+cruise DGW | not |
|---|---|---|---|
| **Makalemiz (§3.1)** | **yok** | 7 271 lb | quadrotor 3 678 lb, L/D_e 4,9 / 8,5 / 8,6 |
| Grok | ~6 760 lb | ~8 190 lb ("güncellenmiş") | *"bir RVLT tablosu sürümü"* der |
| ChatGPT | 6 584 lb | 7 271 lb | 2022 Johnson–Silva, Tablo 3 dediği yer |
| Web araması özeti | 8 210 lb | 3 740 – 6 480 lb | quadrotor elektrik 3 470 lb |

**ChatGPT ile arama özeti tilt-wing'de birbirini çürütüyor: 6 584'e karşı 8 210 lb.**

## Neden çözülmedi

`ntrs.nasa.gov` ve `rotorcraft.arc.nasa.gov` bu ortamda **egress proxy tarafından kapalı.**
Kaynağı açıp tabloyu okuyamadım.

## Kural

`CLAUDE.md` §3: hiçbir iddia denetlenmeden aktarılmaz. Ve bu projenin **zaten bir kez ödediği**
bedel: Bacchini'nin *"%38 sürükleme / %13 menzil"* sayıları bir **arama özetinden** alınmıştı ve
tezin kendisi %34 ve +%1,7 diyordu. Tez birinci elden okununca ortaya çıktı.

**Dolayısıyla tilt-wing ağırlığı makaleye GİRMİYOR** ve Adım 4 onsuz yazıldı.

## Daha ciddi olan

Grok şunu da söyledi: *"O iki ağırlık, RVLT tablolarının bir sürümüdür."* Yani **§3.1'in kendi
3 678 / 7 271 sayıları da hangi tablodan geldiği söylenmeden duruyor.** ChatGPT bunları 2022
Johnson–Silva Tablo 3'te birebir bulduğunu söylüyor; doğrulayamadım.

Ayrıca ChatGPT *"dört VTOL mimarisi"* ifadesinin **yanlış** olduğunu, setin QSMR, side-by-side,
quadrotor, lift+cruise ve tiltwing ailelerini içerdiğini söylüyor. Doğrulayamadım; ifade
ihtiyatla **"several"** olarak değiştirildi.

## Yazara düşen — Bacchini'de yapıldığı gibi

**Belge indirilip tablo birinci elden okunacak.** Gereken:

1. Makalenin tam künyesi (yıl, tablo numarası).
2. Her satır için: yapılandırma adı, tahrik türü, **brüt ağırlık (lb)**, **L/D_e**.
3. Tasarım görevi (faydalı yük, menzil).
4. Kaç ayrı VTOL ailesi boyutlandırılıyor.

Adaylar (ikisi de bu ortamdan kapalı):
- `https://ntrs.nasa.gov/api/citations/20210026170/downloads/1521_Johnson & Silva_122721 .pdf`
- `https://rotorcraft.arc.nasa.gov/Publications/files/TVF2026_JohnsonSilva.pdf`

## Okunduğunda ne değişecek

Grok'un **asıl** bulgusu bu sayıya bağlı: quadrotor ile lift+cruise karşılaştırması **üç şeyi
birden** değiştiriyor (mimari, tahrik, kanadın varlığı). Temiz kontrol **tilt-wing'e karşı
lift+cruise** — ikisi de kanatlı, ikisi de turbo-elektrik, biri adanmış kaldırma taşıyor öteki
taşımıyor. O karşılaştırma **Fatura 1'i yalıtıyor.**

ChatGPT'nin sayıları doğruysa (tilt-wing 8,6 / 6 584 lb, L+C 8,5 / 7 271 lb), temiz kontrol
şunu verir: **aynı seyir verimi, adanmış kaldırma için +%10 ağırlık.** Bu, quadrotor
karşılaştırmasından çok daha güçlü bir sınama olur.

**Ama sayı doğrulanmadan yazılmaz.**
