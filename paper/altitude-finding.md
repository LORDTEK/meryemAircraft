# İrtifa — yazarın sorusu, ve açtığı delik

**Soru (yazar):** *"Şimdi biz bu çalışmaları deniz seviyesinde mi yapıyoruz? Galiba irtifa
da bu hesapları etkileyecek bir etmen. Dolayısıyla belki de makalede en azından 'hesaplar şu
irtifa için yapılmıştır' demek gerekebilir."*

**Kod:** `aero/nose_propeller_altitude.py` · **Çıktı:** `aero/nose-propeller-altitude.txt`

---

## 1. Evet, deniz seviyesi — ve makale bunu zaten söylüyor

Kodda ρ = 1,225 her yerde: `baseline.py`, `closure.py`, `rotation.py`, `tip_propeller.py`,
`yaw.py`, ve yeni yazılan burun çifti hesabı. İstisna yok.

Makale de söylüyor. §2.12, *"Assumptions carried throughout: **sea-level density**; no
compressibility…"* Ve arkasından bunu savunan bir paragraf var — üstelik kendi eski hatasını
düzelterek:

> *"**Sea-level density is a deliberate choice and not an oversight.** An earlier version of
> this paragraph called it the conservative one… **that reasoning is wrong and the paper's own
> range equation shows why.** Range here is f_fuel · E* · η_chain · (L/D) / g, in which
> **density does not appear**: at a fixed lift coefficient a thinner atmosphere is flown faster
> for the same lift-to-drag ratio, and the range is unchanged. **Altitude would move these
> figures only by moving L/D**… The choice matches the intended missions — wildfire observation
> and cargo delivery to sites without a runway — which are flown low, and it keeps the hover and
> cruise calculations on one atmosphere so that **the ratio between them, which is what the
> three bills are about, is not carrying a density change as well.**"*

**Yani istediğiniz cümle zaten var, ve gerekçesiyle birlikte var.**

## 2. Ama sorunuz o paragrafta bir delik buldu

O paragraf **pervane hesabından önce** yazıldı. İddiası şu: yoğunluk menzil denklemine
girmiyor, dolayısıyla irtifa menzili ancak L/D üzerinden etkiler.

**η_chain'in içinde η_p var.** Ve η_p, askı ile seyir arasındaki **ilerleme oranı açıklığına**
bağlı:

- **Askı:** J = 0. İrtifadan **bağımsız**.
- **Seyir:** sabit C_L'de V ~ 1/√ρ. İrtifayla **büyür**, dolayısıyla J büyür.

Paragrafın kendi argümanı — *"ince hava daha hızlı uçulur"* — çift görev açıklığını **açan**
şeyin ta kendisi. Yani yoğunluk menzil formülüne doğrudan girmiyor ama **η_p üzerinden ikinci
bir kanaldan giriyor**, ve o kanal paragraf yazıldığında yoktu.

## 3. Hesaplandı

Aynı palet ailesi, aynı FM hedefi (0,599), 2 pala, c_l 0,70:

| irtifa | ρ | V (m/s) | FM | **η_p** | J | askı kW |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1,2250 | 30,0 | 0,598 | **0,683** | 0,80 | 10,94 |
| 1000 | 1,1117 | 31,5 | 0,601 | 0,677 | 0,82 | 11,44 |
| 2000 | 1,0066 | 33,1 | 0,602 | 0,671 | 0,84 | 12,00 |
| 3000 | 0,9093 | 34,8 | 0,590 | **0,663** | 0,87 | 12,87 |

**FM sütunu üzerine bir not — DeepSeek yakaladı.** 3000 m satırında FM = 0,590, Tur 38'de
beyan ettiğim 0,591–0,603 toleransının **dışında.** Bu bir irtifa etkisi değil, yedi turluk
ikiye bölmenin artığı; ama beyan edilen tolerans yanlıştı ve düzeltiliyor. Ve masum değil:
**Qwen askı gücü artışını ayrıştırdı ve denetledim** — yoğunluk payı √(1,2250/0,9093) = 1,1607,
FM payı 0,598/0,590 = 1,0136, çarpım 1,1764; gözlenen 12,87/10,94 = 1,1764. **%0,0006 hatayla
tutuyor.** Yani o 0,008'lik FM sapması, %17,6'lık artışın **%1,36'sını** taşıyor.

**Yön hesaplandı, büyüklük küçük.** η_p 3000 m'de 0,683 → 0,663, yani **göreli %2,9 düşüş.**
Kıyas: 0,80 → 0,65 açığı %19. İrtifa kanalı ikinci derece.

**Askı gücü ikinci derece DEĞİL.** 10,94 → 12,87 kW, **%17,6 artış.** Tampon, motor
derecelendirmesi ve kütle bütçesi bundan etkilenir; menzilden çok daha fazla.

## 4. Sonuç

1. Makalenin *"deniz seviyesi"* ilanı **duruyor ve yeterli.**
2. §2.12'nin *"irtifa menzili yalnız L/D üzerinden etkiler"* cümlesi **eksik**. Bir yan cümle
   gerekiyor: η_p da irtifayla değişir, çünkü çift görev açıklığı açılır; hesaplanan etki 3000 m
   için göreli %2,9 ve **aleyhimize**.
3. *"A design intended to cruise high would need the whole chain re-run"* cümlesi **zaten
   doğru** ve şimdi bir sayıyla destekleniyor.
4. Görev profili (orman yangını, piste ihtiyaç duymayan yere kargo) alçak uçuş demek,
   dolayısıyla seçim göreve uygun. Ama **sebebi "etkisi yok" değil, "etkisi küçük ve hesaplandı."**

**Yazarın sezgisi doğruydu ve bulduğu şey sandığından dar ama gerçek:** eksik olan ilan değil,
ilanın gerekçesindeki bir kanaldı.
