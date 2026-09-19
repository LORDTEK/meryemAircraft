# Burun çiftinin çift görev denetimi — açık bulgu

**Durum: AÇIK. Tur 36'da dört dış okuyucunun dördü de bağımsız olarak buldu.**
Kaynak: `cfd/external-review-40.md` §3'te sorulan soru; cevaplar Tur 36.

---

## Ne bulundu

Makale §3.3'te şunu yazıyor:

> *"The nose pair is the cruise propulsor and **runs at its design condition throughout**."*

ve §2.9'un faz listesinde:

> *"**Cruise.** …The nose pair is now the cruise propulsor **at its design point**."*

Pervaneler **sabit hatveli** — eleme listesi *"no variable-pitch hub"* diyor. Sabit
hatveli bir pala tek bir geometrik hatveye sahiptir ve verimi tek bir ilerleme oranında
tepe yapar. Askı J ≈ 0; seyir sonlu bir J. Elektrik tahrik devir aralığı verir, **hatveyi
değiştirmez**, ve verim tepesinin yerini belirleyen hatvedir.

## Asimetri — makale aynı denetimi uç çiftlerine uyguluyor

§3.4, uç çiftleri için:

> *"The trend across the seven designs is the trade stated plainly: the blade that hovers
> well free-wheels fastest and drags most. Section 2.9 rules out the escape, because these
> pairs are of fixed geometry and cannot feather."*

> *"What would settle it is a propeller design study that optimises the blade across both
> duties rather than for hover alone, or a variable-pitch tip pair — which is a mechanism,
> and mechanisms are what this configuration was built to avoid."*

Uç çiftleri için **yedi pala tasarımı, Tablo 4, devir ve uç Mach sayısı, ve sayısal bir
ceza (ΔC_D0 = 0,0154)** var. Burun çifti için **hiçbiri yok.**

## Sayıların kendisi — doğrulandı

| Ne | Değer | Satır | Hangi rejim |
|---|---|---|---|
| Askı figure of merit | **0,599** | §3.3 (1248), §3.8 (1725), §3.17 (2320) | askı |
| Seyir pervane verimi | **0,80** | §2.12 (982), zincir: *"propeller 0.80 — overall 0.176"* | seyir |
| Ana pervane çapı, hafif | 1,20 m | 1609 | — |
| Seyir hızı, hafif | 30 m s⁻¹ | 1615 | — |
| Ana pervane çapı, ağır | 5,40 m | 1675 | — |
| Seyir hızı, ağır | 40 m s⁻¹ | 1679 | — |

**İki verim iki ayrı rejimden alınmış ve ikisi de aynı sabit hatveli burun çiftine
atfediliyor.** Tek bir palanın ikisini birden verdiği hiçbir yerde gösterilmiyor.

## Kendi bulduğum, dış okuyucuların söylemediği

**Makale burun çiftinin devrini, pala geometrisini ya da herhangi bir pala-eleman
hesabını hiçbir rejimde vermiyor.** Tablolarda yalnız **çap** ve **disk yüklemesi** var.
Uç çiftlerinin Tablo 4'te devri, uç Mach'ı ve yedi tasarımı varken, burun çiftinin bir
çapı ve iki varsayılmış verim sayısı var. Asimetri tek bir cümlede değil, **belgelemenin
tamamında.**

Dolayısıyla Qwen ve DeepSeek'in verdiği J tahminleri (≈0,5–1,0 ve ≈0,5–0,6) **kaynakta
doğrulanamadı** — çünkü kaynakta devir yok. İki tahmin de akla yatkın, ikisi de
belgelenmemiş.

## Okuyucuların hükmü

| | Okuma | Not |
|---|---|---|
| **Grok** | Kaynak cümleler için (1), **uçak için (2)** | *"Reading 3 ('RPM saves it') is exactly the unstated reason. If it is true, write the map. If you cannot, you do not have reading 3."* |
| **DeepSeek** | **(2)** | Cümle şimdi çıkar, hesap programa girer, menzil değişebilir |
| **Qwen** | **(2)** | *"The motor can move the operating point along the advance-ratio axis; it cannot move the efficiency peak."* |
| **ChatGPT** | **(1)** | Cümle daralt, yeni hesap gerekmez; *"sized for its cruise design point"* |

**Üçe bir, okuma (2).** ChatGPT'nin gerekçesi zayıf değil: mimari iddia için "design
condition throughout" zaten **gerekli değil**, gereken şey yönelimin sabitliği. Ama
ChatGPT'nin kendisi de *"'penalty yok' denemez"* diyor.

## Yapılanlar

- **Adım 7'ye girdi** (`paper/v8/07-the-combination.md`): sabit hatvenin iki rejime
  bedelsiz hizmet etmediği, bunun değişken hatve göbeğini reddetmenin **bedeli** olduğu,
  ve tahrikin denetlendiği yerde yazılacağı. Şerit ve kalkış marjıyla aynı yöntem.
- Tablodaki *"Variable-pitch hub"* satırının kendini çürüten yan cümlesi düzeltildi.
  (Grok ve Qwen bağımsız olarak yakaladı; yan cümleyi bir tur önce **ben** eklemiştim.)

## Yapılmayanlar — yazarın kararına açık

1. **İki noktalı BEMT.** Uç çiftleri için kullanılan pala-eleman kodunu burun çiftine, iki
   işletim noktasında (askı J ≈ 0 ve seyir J) koşmak. Çıktı: 0,80'in doğrulanması ya da
   düzeltilmesi. Düzelirse **menzil değişir.**
2. v8'de §3.3'ün karşılığı yazılırken *"design condition throughout"* **yazılmayacak.**
   Bu, hesap yapılsın ya da yapılmasın geçerli.

**Uyarı:** hesap yapılırsa işaretini tahmin etmeyelim. Grok: *"Do not guess the sign."*
