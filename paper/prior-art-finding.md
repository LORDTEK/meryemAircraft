# Boşluk iddiası ÇÜRÜTÜLDÜ — ve düzeltme daralmak

**Durum: DÜZELTİLDİ, 2026-09-20.** Üç okuyucu bağımsız olarak aynı şeyi söyledi, yazar iki
belgeyi depoya yükledi, ikisi de birinci elden okundu.

**Bulgu: Adım 1'in boşluk cümlesi yanlıştı.**

---

## 1. Yanlış olan ne

Adım 1 şunu yazıyordu:

> *"The route that refuses both — one set of hardware, never reoriented, with the airframe
> turning instead — was flown once, in 1954 … and **has not been revisited as a design
> proposition** since the constraints that stopped it were removed."*

ve

> *"**Every** architecture that puts one set of hardware into both regimes does so by
> reorienting the propulsors."*

**İkisi de yanlış.** Grok, ChatGPT ve DeepSeek bağımsız olarak yakaladı. ChatGPT'nin ifadesi:
*"Modern kuyruk üstü İHA'lar apaçık karşı örnek."*

## 2. Okunan iki belge

### De Wagter ve ark. 2018, *Journal of Field Robotics* — DelftaCopter
`references/Wagter_et_al_2018_Journal_of_Field_Robotics.pdf`, birinci elden okundu.

Giriş bölümü **tam olarak bizim tasarım uzayımızın literatür taraması.** İçinde:

- *"The first hybrid tail-sitters were combinations of fixed-pitch quad-rotor helicopters with a
  flying wing such as the Quadshot… four propellers and typically two aerodynamic actuators."*
- **Escareno ve ark. (2007, 2008): tek pervanenin tork problemini çözmek için eşeksenli çift
  pervane** — *"which also results in slightly higher efficiency at the cost of an extra motor
  and coaxial system."*
- **Oosedo ve ark. (2013), ICRA:** *"Development of a quad rotor tail-sitter VTOL UAV **without
  control surfaces** and experimental verification."*
- Ve en önemlisi: *"the fixed-pitch propellers make it **theoretically impossible** to be very
  efficient in both hovering and forward flight."*

**Son madde doğrudan bizim burun çifti bulgumuzu ilgilendiriyor.** DelftaCopter'in kendi
tahrik bölümü de aynı takası yapıyor: *"the propulsion is designed to be a **compromise**
between efficient hover and efficient forward flight,"* 1 m çap *"bir uzlaşma olarak"* seçilmiş,
25° burulma.

> **Sabit hatvenin iki rejimde birden verimli olamaması bu literatürde BİLİNEN bir sonuçtur.**
> Biz onu keşfetmedik. **Bizim yaptığımız, onu bu mimari için nicelemek ve boyutlandırma
> döngüsünden geçirmekti.** İddia buna göre daraltılacak.

### Pathak 2025, *Journal of Informatics Education and Research* — SkySwift V1.0
`references/Design+of+Flying+Wing+Tail+Sitter+Contra-Rotating+Propeller+VTOL+Sky+Swift+V1.0+UAV_Final.pdf`

Başlık ve özet **rahatsız edici derecede yakın:** *"hybrid flying-wing tailsitter UAV designed
specifically for **disaster management and rapid response** … The airframe is a **blended
wing-body**, with forward-swept wings … uses a **contra-rotating pusher** configuration."*

Yani: BWB + kuyruk üstü + karşıt dönüşlü pervane + afet müdahalesi. Dört öğe de bizde var.

**Ama okuyunca fark çıkıyor ve fark bizim asıl iddiamızın tam olarak olduğu yer:**

| | SkySwift V1.0 | Bu çalışma |
|---|---|---|
| Kumanda yüzeyleri | **Var** — *"to validate **control surface** and propeller effectiveness"* | **Yok** (şerit hariç) |
| Tutum kontrolü | Kumanda yüzeyleri + pervane | Diferansiyel itki + şerit |
| Pervane düzeni | Tek karşıt dönüşlü itici | Burunda bir çift + uçlarda dört çift |
| Tork dengesi | — | Her çift eşeksenli, **net açısal momentum nominal sıfır** |
| Tahrik | Batarya | **Seri hibrit + tampon** |
| Kütle dökümü / boyutlandırma kapanışı | Yok | Var, iki ölçekte |
| Mimari muhasebe | Yok | Üç fatura, üç sözleşme |

**Yine de bu, boşluk iddiasını daraltmak için yeterli sebep.** Yayın yeri bir aerouzay dergisi
değil ve yazar bir lise öğrencisi, ama **bir yenilik iddiası için yayın yerinin kalitesi
önemli değildir** — yapılandırma basılı hâlde var.

## 3. Düzeltilmiş boşluk

**Boşluk artık tarihsel değil, mimari ve nicel.**

> Kuyruk üstü ilkesi ne yeni ne de terk edilmiş: 1954'te uçtu ve o zamandan beri insansız
> kuyruk üstü literatürü onu tekrar tekrar ele aldı. Kumanda yüzeysiz kuyruk üstü de var
> (Oosedo 2013). BWB kuyruk üstü de var (SkySwift 2025). Sabit hatvenin iki rejim uzlaşması da
> bilinen bir sonuç (De Wagter 2018).
>
> **Bulunmayan şey, bu seçimlerin bir arada ve bedeliyle birlikte kapatılmış hâlidir:**
> eşeksenli ve tork dengeli çiftlerle — yani tepki torkundan ve net açısal momentumdan da
> vazgeçerek — kumanda yüzeyi olmadan, seri hibrit tamponla, ve **taşınan askı kütlesi, açıkta
> seyir sürüklemesi ve askı tepesiyle boyutlanan sürekli güç** üzerinden açık bir mimari
> muhasebeyle, iki ölçekte ve üç boyutlandırma sözleşmesi altında.

**Oosedo'nun dört rotorlu kuyruk üstüsüyle fark bir SEÇİMDİR, bir fizik sınırı değil.**

> **DÜZELTME, Tur 47.** Bu satır önce şöyle yazılmıştı: *"ayrı dört rotor tepki torkuyla
> üçüncü ekseni üretebilir; bizimki her çift eşeksenli ve tork dengeli olduğu için
> **üretemez**."* **İkinci yarısı yanlıştı.** Eşeksenli bir çift de üretebilir — iki rotoru
> farklı devirlerde döndürmek yeter, ve §2.9 her rotorun kendi elektrik makinesinde olduğunu
> söylüyor. Zhang ve ark. 2012 (`references/ica20120400001_12673514.pdf`) tam olarak bunu yapıyor:
> *"Roll motion is controlled by the **differential velocity of the two motors**."*
> Ayrıntı: `paper/roll-axis-finding.md`.

Doğrusu: bizimki her çifti **tork dengeli işletmeyi seçiyor**, böylece tepki torkunu kontrol
kanalı olarak harcamıyor, ve ekseni şeride veriyor. Kazanılan şey tork dengesi ve nominal sıfır
net açısal momentum; ödenen şey bir kanal. **Bu takasın kendisi — kanalı bilerek bırakıp bedelini
tek bir hareketli yüzeyle ödemek — literatürde bulunamadı**; bulunan şey tersi, yani kanalın
kullanılması (Zhang 2012) ya da slipstream içinde kumanda yüzeyleri (Novlit 2014).

## 4. Neyi değiştiriyor

| Sayfa | Ne değişiyor |
|---|---|
| **Adım 1** | Boşluk cümlesi yeniden yazıldı; *"tekrar ele alınmadı"* ve *"her mimari"* çıktı |
| **Adım 7** | *"What is new"* → *"What this paper examines"*; öğeler listesine kuyruk üstü İHA literatürü eklendi |
| **Adım 9** | Aynı düzeltme |
| **`nose-pair-finding.md`** | Sabit hatve uzlaşmasının **bilinen** olduğu, bizim katkımızın **niceleme** olduğu not düşüldü |

## 5. Yöntem notu

**Kaynak kuralı ikinci kez işe yaradı ve bu sefer bizim aleyhimize.** Bir tur önce kural
bizim sayılarımızı doğrulamıştı; bu tur boşluk iddiamızı çürüttü. İkisi de aynı kuralın
sonucu.

**Ve bu, hakemden önce bulundu.** Bir hakem SkySwift'i ya da Oosedo'yu tek bir atıfla masaya
koysaydı, *"tekrar ele alınmadı"* cümlesi makaleyi tek başına bitirirdi.
