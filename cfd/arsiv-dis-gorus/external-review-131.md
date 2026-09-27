# Round 127 — ChatGPT's reading of Rohith and Vegh, for the other three to judge. Step 8 applied (S-51, S-52, P117, N1, voice); please confirm. Step 15's lists. And the whole paper's length, with numbers.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`6396b85`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**
> - Appendix A: Step 15.
> - Appendix B: ChatGPT's report on Rohith and Vegh, verbatim.

---

## 1. Rohith and Vegh — ChatGPT's reading; Grok, DeepSeek and Qwen, please judge it

The author asked ChatGPT to give everyone what it read. **Its report is Appendix B, verbatim.**

**What ChatGPT did and did not read.** It says so itself:
- **Rohith et al.** — the full article, rendered on ResearchGate, with page numbers.
- **Vegh, SciTech 2025 (doi 10.2514/6.2025-1436)** — the full conference paper, the same way.
- **Vegh, *J. Aircraft* (doi 10.2514/1.C038393)** — only the abstract page (*"No full-text available"*).

**ChatGPT corrected its own Round 123–124 account.** The Vegh geometry comes from the conference paper, not the journal version. It
also declined to reproduce long verbatim passages from copyrighted papers, and gave short quotations plus paraphrase with page
provenance instead.

**The substance, as ChatGPT reports it:**

**Rohith** (pp. 1, 9–11, 13–15):
- a winged **biplane** tail-sitter at 100 kg;
- a series-hybrid powertrain;
- *"the engine was sized to provide cruise power"*, *"110% cruise instead of 150% hover"*, with a boost battery supplying the vertical
  flight;
- the tail-sitter conversion adds *"fixed wings and collective pitch change mechanisms"*.
- Elements (a) and (e). **Not (c).**

**Vegh, conference** (pp. 1, 5–6, 10–11, 26):
- an **unmanned long-endurance coaxial tail-sitter**;
- a common geometry with **fuselage, wing, horizontal tail and vertical tail**;
- four propulsion systems (diesel, parallel-hybrid diesel, turboshaft, series-hybrid SOFC);
- hybrid-electric architectures *"partially decouple"* hover power from the size of the energy-conversion system.
- The attitude-control mechanism is not found in the text (a gap, not filled).
- Elements (a), (b) and (e). **Not (d)** as far as the geometry shows.

**My reading.**
- **Neither closes the gap.** Both occupy exactly what the gap sentence already concedes: *"Each half of the required capability is well
  served … And the third route is occupied."*
- **Both are close witnesses for Step 7's *"None of the three elements is new … some of them together"*.** Rohith states Section 3's
  escape condition in a tail-sitter: the continuous plant sized for cruise, the hover peak from a store.
- **Once the PDFs are in the repository and read**, they belong in Step 1's occupied list, with scope on the same line (Grok P111's
  form), and in the Step 7 witness sentence that is waiting.
- **Nothing is drafted from this report yet** (Grok P116). A rendering read by one reader is a lead, not evidence.

**Grok, DeepSeek, Qwen — please judge, in the author's spirit (*"one mind is sharpened by another"*):**
1. Does anything in ChatGPT's report stand in the way of the author's claim — the contribution sentence, or the gap sentence?
2. Is the element classification right? Answer especially on (c) for Vegh (no collective pitch found, but no explicit statement either)
   and on (d) for Vegh (tails are named; whether they carry control surfaces is not reported).
3. Does Rohith's *"engine sized to provide cruise power"* with a boost battery change how Step 3 or Step 7 should present the escape
   condition? My view: no. Step 3 never claims the condition is new, and Step 7 already says the elements are not. But it is the closest
   same-class witness yet.

---

## 2. Step 8 — applied; please confirm (2 045 → 2 000)

All items below were agreed by all four of you and me. The complete frozen text is in Supplement S8.

**S-52 (R)**, in [7]:
> *"… and it must be opposed continuously, either by a control surface, which costs drag, or by ~~differential thrust~~ **the reaction
> torque of other rotors run at a different speed**, which costs a control channel."*

Retired phrase (Grok P119): *"or by differential thrust, which costs a control channel"*. ChatGPT's consistency note: *"A counter-rotating
pair does not produce it"* is true at equal speeds, and [9] already qualifies the speed-trimmed case. No further change.

**P117 (R)**, in [14]:
> *"**Pitch and yaw come from differential thrust between the tip pairs** (body axes, as fixed in the note below), and the two axes
> do not have the same moment arm."*

**S-51 (c)**, in [24]:
> *"Two items belong here rather than in a later list~~, because both are properties of the hardware just described~~."*

**N1**, in [4]. Deleted: *"Thickness runs from 25 % of chord at the root to 12 % at the tip, and chord from 0.970 m to 0.236 m."*
Moved to S8 with identity: *"On the 50 kg reference design, thickness runs from 25 % of chord at the root to 12 % at the tip, and chord
from 0.970 m to 0.236 m (realised planform, `aero/planform.py`)."* **Please check the S8 wording.**

**Voice:**
- **V1:** *"The reason is narrow ~~and worth stating as such~~: **reaction torque.**"*
- **V2:** *"**One part is not airframe ~~and is easy to omit from a list of this kind~~: the flight control system.**"*
- **V3:** *"The propellers rotate~~, as propellers do,~~ and their shaft speed is commanded …"*
- **V5:** *"**The tip pairs are the parts that fail the escape condition.**"* (*"and naming them here is the point of listing them"* removed)
- **V4 and V6 stay** (all four of you and me; DeepSeek changed its vote on V6).

**Still open on S-51 (two proposals):**
- **DeepSeek:** delete [24] entirely. The heading already introduces the block, and *"Two"* then need not be defended.
- **Grok P120:** the heading *"What this inventory does not settle"* does not cover [29], which is settled. Either retitle the block or
  move [29].

My view:
- **Delete [24] (DeepSeek).** It is a deletion. Grok and Qwen read *"two"* as [25]–[27] and [28]+[30], with [29] settled inside the
  block; ChatGPT treats the numeral as prose; DeepSeek prefers no count. Deleting the sentence ends the disagreement without a new
  predicate.
- **On P120:** a retitle is an R to a heading. The deletion-only alternative is to leave [29] where it is; it explains why [28]'s
  second cruise state matters.
- My vote: keep the heading. Grok, does [29] under that heading mislead a reader, or only fail to be covered by it?

**Qwen R126-P2 checked:** no step counts actuators. The only phrases are *"the propulsion motors together with the strip"* (Step 7) and
*"the propulsion motors plus the strip's actuation"* with *"How many actuators that is, this study does not fix"* (Step 8).

**If you confirm, Step 8 closes at 2 000.**

---

## 3. Step 15, *Four axes, and where the paper stops* — your lists (Appendix A)

The last architecture step.
- **Size:** 349 words, against a plan of 250.
- **Protected:** 4 sentences.

**Standing checks to apply:**
- **T1's home is Step 9; Step 15 consumes it and does not rebuild it** (Round 114).
- **Qwen R108-P2:** a debt/scope check against Step 14's sixteen unknowns. Does Step 15 promise anything Step 14 leaves open?
- **Qwen R116-P2:** a consumption map: every Step 15 claim, with its home section.
- **P104:** the author's *"seeing"* is not a sentence here.
- **§0.8:** the spirit is carried by placement and voice, never by a stronger predicate.

**Please give:**
- the core;
- what stays;
- P71 pairs;
- negatives with their homes;
- voice by the agreed method;
- the consumption map.

**My own reading.** Step 15 is already near its floor.
- Each axis paragraph restates a T1 row with its limit.
- The closing sentence (protected) is the paper's own statement of what it offers.

**Two questions for you:**
- **(i)** *"nothing in this work addresses certification"* — I searched every step: certification appears **only here**. Is it a
  new scope statement introduced in the conclusion? If so, should it stay (a true limit) or go (nothing earlier prepares it)?
- **(ii)** *"positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against the other"* —
  does it match Section 6's numbers and wording after S-48?

---

## 4. The paper's length — the numbers, before they go to the author

Every architecture step is now measured. **Body prose, tables excluded:**

| Step | Words | Plan |
|---|---:|---:|
| 1 | 1 517 | 850 |
| 2 | 1 786 | 750 |
| 3 | 1 351 | 650 |
| 4 | 1 279 | 350 |
| 5 | 1 133 | 600 |
| 6 | 1 883 | 850 |
| 7 | 1 163 | 900 |
| 8 | 2 000 | 900 |
| 9 | 1 020 | 400 |
| 10 | 953 | 1 550 (10–13 together) |
| 11 | 831 | |
| 12 | 1 000 | |
| 13 | 1 214 | |
| 14 | 1 165 | 450 |
| 15 | 349 | 250 |
| **Total** | **18 644** | **8 500** |

*AIAA's own count* (`paper/v8-budget.md`): a Regular Article is **10 000–12 000 words, with figures and tables counted** at 200, 450
or 700 each.

- **The body is about 2.2 times the prose plan**, before any table or figure.
- **The method works as designed:** no claim, limit or mechanism sentence is lost.
- **That is exactly why it cannot reach the plan.**
  - Deletion-only recomposition took the calculation steps to about 40 % of their length.
  - It took the framework and architecture steps to 80–95 %, because their protected sentences and their evidence set a floor.

**This goes to the author.** Before it does, **each of you: what would you do?** Give a concrete proposal with its cost. Answer the other
readers' proposals too. For example:
- a second pass on the architecture steps with R allowed (vetoed sentence by sentence);
- whole blocks to the supplement with a one-paragraph summary in the body;
- merging steps;
- a different article type;
- or accepting the overrun and arguing for it.

The author has said: *"the solution cannot be pruning"*, and *"if we shorten, we shorten from everywhere"*. Both hold.

---

## 5. Errors this round

**Mine.** None found; please look.

**ChatGPT.**
- You corrected your own earlier claim that you had read the Vegh journal version: only its abstract was open. That is the right
  correction, made without being asked.
- **The S-49 map row** is recorded as accepted.

**Grok.** You call *"Items that belong here rather than in a later list follow."* *"still a deletion"*. It adds *"follow"*, so it is an R.

**DeepSeek, Qwen.** None found. Qwen withdrew its Round 125 count plainly.

---

## 6. To vote

| # | Item | My vote |
|---|---|---|
| a | §1: judge ChatGPT's Rohith and Vegh report — obstacle? classification? Step 3/7 presentation? | no obstacle; classification right; no change before the PDFs |
| b | §2: confirm Step 8 (closes at 2 000) and the S8 wording | confirmed |
| c | §2: delete [24] entirely (DeepSeek) | yes |
| d | §2: P120 (retitle the block, or move [29]) | keep the heading |
| e | §3: Step 15 lists, (i) certification, (ii) the quadrotor wording | — |
| f | §4: your length proposal, with its cost | — |
| g | Qwen R126-P1 (Step 8 → Step 11 drag-ledger map, when Step 11 is re-read); R126-P2 (checked: no actuator count anywhere) | yes; done |

---

## 7. Your own proposals

As always: anything you see, with your reason.

If you open a PDF, name it and the page. If you could not open it, give no number from it.

---

## Appendix A — Step 15 as it stands now (body only)

### Four axes, and where the paper stops

The paper makes its claims on four axes, against four opponents (Section 9), and on each it stops where
its evidence stops.

**Cruise efficiency, against rotorcraft — claimed against multirotors, and bounded; mixed against helicopters.** Cruise lift is carried on a surface
rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement:
positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against
the other (Section 6). Nothing is claimed against rotorcraft on vertical capability.

**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The
vertical phase was sized with an energy store whose required performance the sources consulted here do not
report as built (Section 14). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency.

**The mechanism required to change regime, against tilting architectures — the contribution.** The
configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so
carries none of the mechanism classes Section 7 counts: no pivot, no nacelle or rotor-group actuator, no
variable-pitch hub, no dedicated lift rotors, and — while the tip pairs free-wheel or are held by motor torque — no
rotor stowing, indexing or stopping mechanism (Section 7's note). Roll
comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what
declining it costs is not computed. **This is a count of mechanism classes, not a claim that nothing moves, and not a
claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate
question, and it is not settled here.

**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing
contract (Section 13).

**The loop closes; the aircraft is not shown to.** Section 14 lists what would settle the rest; nothing in
this work addresses certification. What the paper offers is **a configuration sized to combine
runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism
that reorients a propulsor, and an account of what the combination costs.**


---

## Appendix B — ChatGPT's report on Rohith and Vegh (Round 126 answer, §1–§4, verbatim)

#### 1. Rohith, Sridharan & Govindarajan — what I actually read

**S. K. Rohith, Ananth Sridharan & Bharath Govindarajan, “Hybrid Powertrain Systems for 100 kg Multicopters and Tailsitters,” Journal of Aircraft, DOI 10.2514/1.C038443.**

The ResearchGate rendering exposes the full article, including its page-numbered text. ([ResearchGate][1])

###### Abstract — p. 1

The abstract says the paper sizes:

* quadcopter, hexacopter and octacopter configurations;
* corresponding **winged biplane tailsitter** variants;
* 100 kg takeoff mass;
* 25–250 km missions;
* battery + internal-combustion-engine/generator/rectifier hybrid powertrains.

It explicitly states that the engine is sized for cruise power while a **boost battery supplies the additional power required for vertical takeoff and landing**. ([ResearchGate][1])

A short verbatim excerpt:

> “the engine was sized to provide cruise power” ([ResearchGate][1])

The rest of the abstract is best treated as paraphrase rather than reproduced verbatim.

---

##### Tail-sitter geometry and collective pitch — pp. 13–14

This is the particularly relevant passage for the present paper.

In the incremental-development section, the authors define two upgrades:

1. converting a quadcopter into a **biplane tailsitter**;
2. changing the battery-electric power plant to a **series-hybrid** power plant on the tailsitter.

The first conversion explicitly adds:

* fixed wings;
* **collective-pitch change mechanisms**;
* new rotor blades, hubs and motors.

The second replaces the large battery with:

* engine;
* generator;
* rectifier;
* smaller boost battery;

while retaining the common airframe, rotors, hubs, motors and fixed wings. ([ResearchGate][2])

The key short quotation is:

> “fixed wings and collective pitch change mechanisms” ([ResearchGate][2])

This is therefore a **directly verified reason why Rohith does not close the paper's “no variable-pitch/no reorientation” combination**.

---

##### Series-hybrid sizing — pp. 9–11

The paper's Section C describes the series-hybrid case.

The relevant findings are:

* the series-hybrid engine/generator/rectifier are sized at **110% of cruise power**;
* the battery has an additional energy budget for intermittent high-power operation;
* in the detailed comparison, motors/ESCs are sized for 150% hover power;
* the battery supplies the excess power for transient flight;
* changing the engine sizing target from 150% hover to 110% cruise is identified as the major driver of the empty-weight reduction. ([ResearchGate][2])

The source's short wording:

> “110% cruise instead of 150% hover” ([ResearchGate][2])

There is also a useful mission-level result: at the maximum-payload cruise speeds, the tailsitter obtains more than 80% of its hover power from the battery in the reported sensitivity study. ([ResearchGate][2])

So the paper is a **very close witness to the “continuous plant below hover peak + store supplies the difference” principle**, while simultaneously containing a collective-pitch mechanism.

---

##### Rohith conclusions — p. 15

The conclusions state, among other things, that:

* winged VTOL UAVs reduce airframe drag and cruise rotor power relative to multicopters;
* series-hybrid powertrains can reduce power-system weight and increase payload capability;
* the boost battery makes the powertrain more complex but enables higher payload, reduced fuel burn and smaller engines/generators/rectifiers;
* the authors identify controls and aeromechanics as important to the overall hybrid-VTOL design problem. ([ResearchGate][2])

The paper therefore supports the proposed Step 7 witness **without threatening the six-element gap**:

| Element                      | Rohith                          |
| ---------------------------- | ------------------------------- |
| Winged tailsitter            | **Yes**                         |
| Hybrid / boost battery       | **Yes**                         |
| Engine below hover peak      | **Yes**                         |
| No variable/collective pitch | **No**                          |
| No reorientation mechanism   | **Not established as required** |
| Your three-charge accounting | **No**                          |

**Conclusion for your paper:** once the PDF is formally deposited and read under your rule, Rohith is a strong Step 7 witness for “some of them together” and especially for the peak-from-store principle. It does **not** close the six-element combination.

---

#### 2. Vegh — conference paper

##### AIAA SciTech 2025

**J. Michael Vegh, “Hybrid-Electric Design Studies for a Long-Endurance Tailsitter Concept,” AIAA SciTech 2025, DOI 10.2514/6.2025-1436.**

I opened the full-text ResearchGate rendering. ([ResearchGate][3])

###### Abstract — p. 1

The abstract describes a conceptual comparison of four propulsion systems for a long-endurance tailsitter:

1. diesel;
2. parallel-hybrid diesel;
3. turboshaft;
4. series-hybrid SOFC.

It says the hybrid-electric configurations partially decouple hover power requirements from energy-conversion-system size and that the results depend on high-C-rate/high-specific-energy batteries and a short-hover/longer part-power duty cycle. ([ResearchGate][3])

Short quotation:

> “four different propulsion systems” ([ResearchGate][3])

---

##### Geometry — pp. 5–6

This is directly verified.

The paper states that all aircraft in the study share the same fuselage and empennage geometry. The common geometry table includes:

* fuselage;
* wing;
* horizontal tail;
* vertical tail.

The table gives the common horizontal- and vertical-tail geometry as well. ([ResearchGate][4])

The paper also describes the study as applying the hybrid-electric drivetrains to an **unmanned long-endurance coaxial tailsitter concept**. ([ResearchGate][4])

Therefore:

* **coaxial tailsitter:** yes;
* **fuselage:** yes;
* **horizontal tail:** yes;
* **vertical tail:** yes.

That is sufficient for the Step 1 distinction.

---

##### Four propulsion architectures — p. 6

The conference paper explicitly lists:

* pure diesel;
* diesel parallel hybrid;
* pure turboshaft;
* series-hybrid SOFC.

([ResearchGate][4])

The series-hybrid SOFC is therefore not an inferred architecture; it is explicitly one of the four cases.

---

##### Battery / hover treatment — pp. 10–11 and later

The battery discussion says batteries can provide high specific power for transient response and short, high-power hover requirements. The paper assumes a particular pack-level specific energy and continuous C-rate and sizes the battery around a four-minute maximum-continuous-power condition. ([ResearchGate][4])

The optimization discussion later says the diesel-electric and SOFC architectures partially decouple hover and forward-flight power requirements, allowing a less efficient short-duration hover condition while using more efficient energy-conversion systems for forward flight. ([ResearchGate][4])

This is again a strong witness for the **power-decoupling principle**.

---

##### Attitude-control question — important gap

I searched the full conference rendering for explicit discussion of **“attitude”** and **“collective”**.

The rendering does **not** return an explicit “attitude” passage, and there is no “collective” match. ([ResearchGate][4])

Therefore I will **not** claim from this source that Vegh uses collective pitch, nor will I claim a particular hover/cruise attitude-control mechanism.

What we can safely say is that its common geometry includes conventional horizontal and vertical tails, and it is a coaxial tailsitter.

---

##### Vegh conclusions — p. 26

The conference conclusion says the four tailsitter propulsion architectures were compared/optimized and that hybrid-electric systems offer design flexibility by using heavier but more efficient energy-conversion systems for climb/forward flight while batteries and electric motors serve short-duration hover. ([ResearchGate][4])

It concludes that the SOFC series-hybrid case has attractive long-endurance characteristics but depends on maturation of higher-specific-power SOFC technology and/or combined-cycle approaches. ([ResearchGate][4])

---

#### 3. Vegh journal version — what I actually verified

The later **Journal of Aircraft** record is:

**J. Michael Vegh, “Hybrid-Electric Design Studies for Long-Endurance Tailsitter Concept,” DOI 10.2514/1.C038393.**

The ResearchGate page confirms the DOI and provides the abstract, but explicitly says **“No full-text available.”** ([ResearchGate][5])

So I can verify from that record:

* the title;
* journal identity;
* DOI;
* four propulsion architectures;
* hybrid-electric decoupling concept;
* battery/high-C-rate dependence;
* short-hover/part-power duty cycle;
* SOFC conclusion.

But I **cannot honestly provide page-specific geometry/control passages from the journal version**, because I did not open its full text.

That distinction should go into the evidence file.

---

#### 4. What this does to Step 1 / Step 7

Nothing changes **before repository deposition and direct reading**, exactly as the author says.

But once the PDFs are formally read:

###### Rohith

Can support:

> **winged tailsitter + series hybrid + boost battery / cruise-sized engine**

while simultaneously documenting:

> **collective-pitch mechanism**

Therefore it strengthens, rather than weakens, the claim that the literature contains substantial subsets of the combination without establishing all of it together.

###### Vegh

Can support:

> **coaxial tailsitter + hybrid-electric propulsion**

while its documented common geometry includes:

> **fuselage + horizontal tail + vertical tail.**

Again, it occupies a large subset without closing the complete combination.

The important point is exactly the author's intersection logic: **the gap is not “none of these elements has appeared”; it is that the combination taken together with its price remains unestablished.**

---
