# Step 9 — What is not claimed

**v8 taslağı, birinci yazım.** İskeletin 9. adımı. **Hiçbir sayıdan önce.**

**Kural denetimi:** sayfada **tek bir sayı yok** · bu bir **sınır tanımı**dır, ikinci bir
kısıtlar bölümü değil (ChatGPT'nin şartı) — kapanmayanlar Adım 14'te · retler, dört eksenin
**sonucu** olarak sunuluyor, savunma listesi olarak değil (DeepSeek) · §0'ın dört ekseni ve
§0.1'in sınırı burada yazılı hâle geliyor.

---

## What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's
own numbers because a boundary drawn after the results would be a retreat, and one drawn before
them is a commitment.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference
matters: the boundary below is about claims the paper **declines to make**, most of which it
could not make on any evidence; Section 14 is about questions the paper **does not answer**, and
which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

The boundary is easiest to state as a consequence of the claim structure rather than as a list
of denials, so the structure comes first. Comparison is only meaningful against a named
alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency and range | Multirotors | **Claimed.** A vehicle carrying its cruise lift on a wing is in a different efficiency class from one carrying it on rotors, and no sizing contract moves a vehicle between those classes. |
| Operation without a runway | Fixed-wing aircraft | **Claimed**, in the sense stated below. |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is
the paper's own central finding: against the other hybrids the ranking depends on the sizing
contract, and it reverses across the three contracts reported in Section 13. A paper that
quoted one of those orderings as a result would be reporting its own choice of contract. **No
range claim is made against the tilting or lift-plus-cruise families in either direction**, and
a reader who finds one implied anywhere in this paper should treat it as an error rather than
as a claim.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.** The vertical axis is where the
fixed-wing family is the opponent; the range axis is not. A runway-launched aircraft that never
claimed vertical capability pays none of the charges of Section 2, and nothing here competes
with it on distance.

**2. It does not claim vertical capability against multirotors.** That comparison runs the other
way and would be absurd. The multirotor family is the opponent on cruise efficiency only.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class
of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic
surface, it is named where the elimination is claimed rather than later, and it also pitches the
nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
maintenance burden were not measured, and nothing here supports a statement about reliability.
What is offered is a **count** of mechanism classes that a tilting architecture requires to
change regime and that this arrangement does not. A count is not a reliability argument, and
readers who convert one into the other are not quoting this paper.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met
in the propulsor that carries the aircraft and is not met in the attitude system, which is
carried through cruise producing moments rather than thrust. Section 3 names that case as
partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition
concerns three specific charges. A configuration may avoid all three and still be unbuildable,
uncontrollable, or unsuited to its mission, and the accounting says nothing against that
possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover
peak onto a store converts a power-system charge into a mass one; serving two regimes with one
set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed,
neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the
transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been
run on this geometry, and the transition analysis is a calculation whose assumptions are stated
where it appears. **"By construction" throughout this paper means "by the sizing", never "by
demonstration."**

### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might
suggest, and the narrower statement is the one the paper defends: **a configuration that
combines runway-independent vertical operation with wing-borne cruise efficiency, and that
reaches that combination with no mechanism that reorients a propulsor.**

Each half of that has a named opponent and neither half is a record. What is new is the
conjunction and the means, and the means is what Sections 7 and 8 describe and what Section 11
prices.

### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
what it demands of anyone who uses the framework afterwards.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Dört eksen, dört ayrı rakip | `CLAUDE.md` §0 tablosu |
| Kanatla taşıma ile rotorla taşıma ayrı verim sınıfı; sözleşme sınıf değiştirmez | §4.2, satır 2498–2502 |
| Öteki hibritlere karşı menzil iddiası **yok**, iki yönde de | §4.2, satır 2513–2517; §3.6, satır 1563–1566 |
| Sıralama sözleşmeye göre tersine dönüyor | §3.6; `paper/chain-resolve-finding.md` |
| Sabit kanatlı menzilde rakip değil; hibrit bandın iki kenarı | §4.2, satır 2482–2489 |
| Elenen şey bir **mekanizma sınıfı**, "hiç hareketli parça yok" değil | `CLAUDE.md` §0.1; §1, satır 289–293 |
| Şerit tek hareketli aerodinamik yüzey ve burnu aşağı yunuslatıyor | §2.10, satır 815–818; §3.17 |
| "Mekanik olarak daha basit" denmez; denen şey bir **sayım** | `CLAUDE.md` §0.1 |
| Kısmî örnekleme: burun çifti sağlar, tutum sistemi sağlamaz | §2.7, satır 692–700; Adım 3, 4. başarısızlık kipi |
| Koşulu sağlamak uçağı **daha iyi** yapmaz | §3.1, satır 1126–1130 |
| Tampon: güç sistemi faturasını kütle faturasına çevirir | Adım 3, izin verilen bedel 1 |
| Sabit hatve iki rejimde birden en iyi olamaz | `paper/nose-pair-finding.md` |
| Uçuş gösterilmedi; *"inşa gereği"* = boyutlandırma | `CLAUDE.md` §0.3; §4.3 |
| Sözleşmesiz sıralama verilmez | §3.6, satır 1563–1564 |

**Bu sayfada BİLEREK olmayanlar: tek bir sayı yok.** İskelet bu adımı *"hiçbir sayıdan önce"*
diye konumlandırıyor ve gerekçesi sayfanın ilk paragrafında: sonuçlardan **sonra** çizilen
sınır bir geri çekilmedir, **önce** çizilen bir taahhüttür.

**Adım 14 ile farkı** ChatGPT'nin Tur 43 şartıdır ve sayfa bunu kendisi söylüyor: burası
**iddia etmeyi reddettiklerimiz**, orası **cevaplamadığımız sorular**. Biri kapsam, öteki borç.

**Yapı DeepSeek'in önerisi.** Retler bir savunma listesi olarak değil, dört eksenin **sonucu**
olarak sunuluyor: makale üçünde iddia ediyor, dördüncüsünde reddediyor, ve reddin gerekçesi
makalenin kendi merkezi bulgusu.
