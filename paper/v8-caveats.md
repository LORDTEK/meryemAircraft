# v8 — kesilemeyecek çekinceler (Tur 60/61)

**Ne:** Tur 60'ta okuyuculara soruldu: *"hangi nitelendirme kesilirse bir iddia aşırı iddiaya döner?"* Grok ve DeepSeek
birebir alıntıyla cevap verdi. **Her alıntı metne karşı denetlendi** (`paper/build/v8_caveats.py`): hepsi metinde, doğru
adımda. Üçü hafif yeniden ifadeydi; metindeki birebir hâliyle yazıldı.

**Ne için:** kısalan her taslak bu listeye karşı denetlenir. Bir satır düşerse denetim bağırır; o satırın bilerek
çıkarıldığı ya da başka bir adıma taşındığı ancak **yazarın kararıyla** kaydedilir.

**Biçim:** `…` birden çok parçayı ayırır; her parça aynı adımda bulunmalı. Karşılaştırma büyük/küçük harfe ve
boşluğa duyarsız. `G` = Grok, `D` = DeepSeek, `C` = ChatGPT, `Q` = Qwen, `K` = Claude.

**Tur 61 eklemeleri:** okuyucuların *"eksik"* dediği 35 satır (hepsi metinde doğrulandı) ve Grok'un parça uyarısıyla Adım 8'in tam cümlesi.
**Çıkarma önerileri** (Grok: 3 satır, Qwen: 2 satır) **uygulanmadı** — DeepSeek hiçbirini çıkarmaz dedi, oy birliği yok.

| Adım | Çekince | Öneren |
|---:|---|---|
| 1 | The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor. | G |
| 1 | None of the elements is new | G |
| 1 | Some of the difficulties were real, internal, and are inherited here. | D |
| 1 | Using it is a choice, and so is declining it. | D |
| 2 | The accounting claims transfer. It does not claim that every architecture is equally good. | G |
| 2 | A remedy whose cost falls outside the three charges does not refute the accounting…but it is not thereby exempt from being counted. | G |
| 2 | A framework that could absorb any cost by declaring it out-of-scope would be unfalsifiable. | D |
| 2 | The statement is deliberately confined to architectures with a dedicated lift subsystem. | D |
| 2 | they are not assumed to be independent physical causes | D |
| 3 | It means zero of the three charges as Section 2 defines them…It does not mean an architecture that costs nothing | G |
| 3 | It does not claim the trade is favourable. | G |
| 3 | An architecture may meet the condition where it carries the aircraft and fail it elsewhere | G |
| 3 | Whether such an architecture might avoid the three charges by some other route is a separate question this paper does not settle. | G |
| 3 | A store is permitted…It does not claim the trade is favourable. | D |
| 3 | Releasing the engine is not releasing the electrical path. | D |
| 3 | Rotating the airframe is permitted and is not priced here. | D |
| 3 | Serving two regimes with one set of hardware has a price of its own…The condition permits that cost and does not measure it. | D |
| 3 | An architecture that reorients a propulsor does not satisfy the condition as written…the condition is a definition, not a law, and it can be too narrow without being wrong. | D |
| 4 | What follows is not a test of the whole framework. | G |
| 4 | only the first is a derivation | G |
| 4 | They are not identical in every other respect…the comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment. | G |
| 4 | It checks one falsifiable consequence on one independent data set. | D |
| 4 | Second half, not derived. | D |
| 4 | It does not establish that the accounting is complete…or that avoiding them makes an aircraft better. | D |
| 5 | Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency. | G |
| 5 | Not demonstrated, and the list is not short. | D |
| 5 | The saving has precedent and it is not this paper's observation. | D |
| 6 | The size of the resulting advantage is a calculation, not a consequence of that statement. | G |
| 6 | These are the bounding corners of a product, not four simulated aircraft. | G |
| 6 | Against the all-electric quadrotor it does not hold at the low corner, and that result is reported as a result rather than as a caveat. | G |
| 6 | This is a comparison of two independently produced figures in a common definition, not a controlled numerical reproduction. | G |
| 6 | is not claimed here, because it has not been computed. | G |
| 6 | Nothing here is claimed against fixed-wing aircraft. | D |
| 6 | Whether 0.683 is the blade a designer would actually choose is not settled here. | D |
| 6 | No part of this has been measured. | D |
| 6 | The span efficiency used throughout this section is the computed value, 0.817, not the assumed 0.85. | D |
| 6 | the aerodynamic predictions diverge above roughly ten degrees of incidence | D |
| 7 | The instantiation is therefore partial. | G |
| 7 | This is not a configuration in which nothing moves. | G |
| 7 | Nor is this a claim of mechanical simplicity. | G |
| 7 | Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper. | G |
| 7 | The mechanism claim is about hardware and survives that limit. The transition claim is not made. | G |
| 7 | The qualification in that sentence is not decoration | D |
| 8 | What declining it costs is not counted in this work. | G |
| 8 | The free-wheeling state is physically determinate: the rotor settles where net shaft torque is zero. The stopped state is not. | G |
| 8 | should be read as the state Section 11 defines rather than as the state a particular installation would reach. | D |
| 8 | How many actuators that is, this study does not fix. | D |
| 9 | No range claim is made against the tilting or lift-plus-cruise families in either direction. | G |
| 9 | is not computed anywhere in this paper. | G |
| 9 | The mechanism claim is a statement about what hardware is present | D |
| 9 | The separate claim that this aircraft can actually perform the regime change is not settled | D |
| 9 | By construction" throughout this paper means "by the sizing", never "by demonstration. | D |
| 9 | no comparison in this paper should be quoted without the contract it was computed under. | D |
| 10 | Closing a sizing loop mathematically is not the same thing as closing an aircraft physically. | G |
| 10 | These are the same configuration at four closed masses rather than four configurations | G |
| 10 | The closures do not take that reduction, and it has not been run through the loop. | G |
| 10 | So the zero-altitude-loss result is a property of the model that produced it. | G |
| 10 | That spread is itself the finding. | G |
| 10 | Whether a real aircraft loses 5.4 m, more, or less is not settled by anything here. | G |
| 10 | If no fixed point exists, the declared sizing package does not close. | D |
| 10 | Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the manoeuvre costs altitude. | D |
| 10 | It does not establish that the package exists. | D |
| 11 | It attributes. It does not add. | G |
| 11 | no scalar aggregate is defined | G |
| 11 | The ledger does not attribute the whole of that gap to the absence of variable pitch. | G |
| 11 | No variable-pitch counterfactual was computed. | G |
| 11 | The buffer fraction is an input to the loop, not a result of it | G |
| 11 | Bill 3 is removed from the engine and left standing on the electrical system. | G |
| 11 | There is no single figure for what the architecture costs. | D |
| 11 | The rotor line rests on section drag at low Reynolds number. | D |
| 11 | The tip-frame term is an attribution, not a marginal removal cost. | D |
| 11 | Rotor–structure and rotor–wing interference is not modelled and is not carried as a line. | D |
| 12 | That near-constancy is a property of the constant-disc-loading rule, not a finding about Bill 3. | G |
| 12 | This paragraph compares the reference pair only. | G |
| 12 | Bill 1 is not tested. | G |
| 12 | It is consistent with the separability Section 2 asserts; it is not a verification of separability as a general property. | G |
| 12 | The test is deliberately weak | D |
| 12 | It cannot show that they are independent in general | D |
| 12 | The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number. | D |
| 13 | What the bound gives is a size, not an order. | G |
| 13 | how much of it they fill is not computed | G |
| 13 | A ranking against a competitor modelled as a bound is not a ranking, and no range claim is made against the tilting family in either direction. | G |
| 13 | Which architecture ranks first under a fixed take-off mass is therefore decided, in this model, by a mass fraction of the competitor that this study has not measured. | G |
| 13 | These are three different questions, not three estimates of one answer. | D |
| 13 | Holding Bill 3 common is a choice of question, and it has a direction | D |
| 13 | The choice runs against this configuration. | D |
| 13 | The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour. | D |
| 13 | Neither figure is measured. | D |
| 13 | The sign under a fixed take-off mass is not a result about the architectures; it is a result about that parameter. | D |
| 13 | Comparing computed figures against assumed ones favours whichever is assumed more optimistically. | D |
| 14 | The package Section 10 closes on does not exist with any store the sources consulted here report as built. | G |
| 14 | It does not reach the mechanism claim. | G |
| 14 | The loop closes; the aircraft is not shown to. | G |
| 14 | for the first item the answer is no | D |
| 14 | The comparison is between unlike ratings | D |
| 14 | The gap is real on every one of them; the factor quoted is peak demand against bench average. | D |
| 14 | These masses are the Section 10 package with one input changed. | D |
| 14 | They are not a structural closure at 100 kg | D |
| 15 | This is a count of mechanism classes, not a claim that nothing moves, and not a claim of mechanical simplicity or reliability | D |
| 15 | Whether this aircraft completes the rotation is a separate question, and it is not settled here | D |
| 1 | What is not established is the combination taken together with its price. | G |
| 7 | What this paper contributes is that combination, the condition its primary propulsor is designed to satisfy, and the price the configuration pays for pursuing it. | G |
| 9 | It is not a list of the study's open questions. | G |
| 13 | The mechanism claim is not a ranking and is not at stake here | G |
| 10 | This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on the count of mechanism classes, which rests on the inventory of those sections alone. | G |
| 6 | The compared vehicles are 1 660 to 3 275 kg | D |
| 6 | Reynolds number favours the larger aircraft | D |
| 6 | The quadrotor is a good quadrotor. | D |
| 6 | Nothing here is compared against a poor example. | D |
| 6 | The speeds are not matched, and the direction of that mismatch is calculable. | D |
| 6 | The atmospheres are not matched. | D |
| 6 | The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called. | D |
| 6 | The best point is not an available option | D |
| 6 | so this fixes a direction, not a magnitude | D+Q |
| 10 | the control moment arms of Section 8 are therefore reference values that this closure does not re-derive | D |
| 11 | The corner that needs the most buffer per kilogram is given the smallest buffer | D |
| 11 | that is a declared assumption of the closure rather than an outcome of it | D |
| 12 | Much above 1 000 kg a single nose pair can no longer hold | D |
| 3 | It is not a claim that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim that satisfying it is desirable. | C+Q |
| 1 | What follows is therefore not a claim to an empty field. | Q |
| 1 | The route is not claimed to have been waiting to be found. | Q+G |
| 2 | The table is not a census of the field; it lists the moves whose transfers are documented, and a remedy absent from it is not thereby claimed to cancel a charge. | Q |
| 4 | The framework does not predict any of these numbers; without the input fractions it predicts no magnitudes. | Q |
| 4 | The prediction is also mission-dependent, and the page would be weaker for hiding it. | Q |
| 5 | This section does not assert the outcome of a calculation it does not contain. | Q |
| 6 | The reference is therefore given its best speed and this configuration is not given its best speed, and the margin is positive anyway. | Q |
| 7 | The assembly is not offered as novel because it is an assembly. | Q |
| 8 | Either the residual is small enough to be absorbed that way, which this study has not shown and which would mean the architecture spends a little of the channel it declined, or a fourth duty falls on the strip. | Q |
| 9 | It does not claim that the aircraft flies. | Q |
| 10 | The published zero-lift value of 0.0248 is not used. | Q |
| 11 | No line item at the adverse end is an independent measurement, and they should not be subtracted from one another as if they were. | Q |
| 12 | A change from 3.6 to 4.0 percent is a change between two choices, not a scaling result, and it cannot be offered as evidence that Bill 1 moves with size in either direction. | Q |
| 13 | The competitors are therefore this planform with two add-ons, not independently designed aircraft of their families. | Q |
| 13 | And nothing here ranks architectures for a mission. | Q |
| 14 | The ranges of 927 to 1 233 km survive the re-closure only because the fuel fraction is held, on an aircraft three-quarters heavier; they do not survive as 13 kg carried that far on a store that has been built. | Q |
| 11 | No new physical cost term is introduced here. | Q |
| 11 | Every cost named below is already inside the closure of Section 10. | Q |
| 6 | variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and declines to attribute all of it to the hub | Q |
| 4 | The quadrotor is reported for scale, and the isolation test above is what carries the prediction | Q |
| 1 | they are the only one of those documented obstacles an uncrewed aircraft removes | Q |
| 12 | Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry. | G+K |
| 10 | the question is asked in two models, only the second of which carries rotational dynamics, and that one does not support a zero altitude loss | C+G+D+Q+K |
| 4 | The instrument is now fixed, and it is not modified again. | G+C+D+Q+K |
| 4 | Everything that follows is measured with it rather than added to it. | G+C+D+Q+K |
| 14 | The escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component whose required performance has not been demonstrated. | G+C+D+Q+K |
| 2 | The same work finds the retraction's advantage elsewhere — the speed that maximises range rose by 5 m/s — which is a performance this accounting does not price. | G+C+D+Q+K |
| 2 | Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question | G+C+D+Q+K |
| 2 | If that architecture already sizes its continuous plant by the hover peak, tilting leaves Bill 3 no worse…what keeps the row from refuting the accounting is the part of its cost that falls outside the three — which is why that part is listed | G+C+D+Q+K |

## Ruh cümleleri (Tur 61, Claude'un önerisi)

Çekince listesi aşırı iddiaya karşı korur; bu liste **ters yöne** karşı korur: kısaltmada kavrayışı taşıyan cümlenin
kaybolmasına (CLAUDE.md §0.8). Aynı denetimle sınanır.

| Adım | Cümle | Öneren |
|---:|---|---|
| 1 | The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor. | K |
| 6 | The two halves are now on the table separately. Section 7 is where they are combined, and the combination is what this paper is for. | C |
| 7 | What this paper contributes is that combination, the condition its primary propulsor is designed to satisfy, and the price the configuration pays for pursuing it. | G |
| 7 | That single move is what removes the need for the mechanism. | K+C |
| 15 | What the paper offers is a configuration sized to combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism that reorients a propulsor, and an account of what the combination costs. | K |
| 7 | The configuration is arranged to change regime by rotating the airframe. The propulsors hold their orientation relative to the body from take-off to cruise; what changes is the orientation of the body relative to the flight path. | G |
| 3 | The answer is a definition, derived by inverting the table, and it is stated here before any configuration is offered so that the standard is not taken from the thing it will be used to measure. | G+C+D+Q+K |
| 3 | Read one at a time, these are ways to pay. Read as a conjunction, they are a condition. | G+C+D+Q+K |
| 3 | An architecture does not incur the three charges if the propulsors that carry the weight…produce both the hover thrust and the cruise…is supplied from a store rather than from permanently installed continuous power | D |
| 8 | The tip pairs are the parts that fail the escape condition | D |
| 2 | is the origin of all three charges below | Q |
| 2 | A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape. | G |
| 14 | The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures | C+D+G+Q+K |
| 1 | The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines rather than a limit it inherits | G+C+D+Q+K |
| 14 | The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack with the required specific power may be possible with existing technology | D+G+C+Q+K |
| 5 | What that refusal costs in authority and in response time is not computed | G+C+D+Q+K |
| 5 | A tail-sitting aircraft on the ground is more prone than a conventional one to tip over, in crosswind and on uneven ground. | G+C+D+Q+K |
| 6 | The same sizing set gives its two helicopter types at 5.4 to 7.2, and against them the result is mixed | D+G+C+Q+K |
| 14 | this aircraft's vertical phases occupy about a minute in all (Section 2), and how long each draws the peak is not computed here | C+G+D+Q+K |
| 9 | Claimed against multirotors, and bounded; against helicopters the published comparison is mixed and no advantage is claimed. | C+G+D+Q+K |
