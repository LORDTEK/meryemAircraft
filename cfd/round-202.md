# Round 202 — The author's decisions; Figure 1; the official class; the style pass, sentence by sentence

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`a0e0667`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. The author's decisions (E32)

The author's words, in my translation: *"Why is there no picture in the paper? Without a picture, is the reader to imagine it in his head? There must be at least one picture. Perhaps one from the upper diagonal while it sits on its tail. Let us not shorten; we continue with JoA. I uploaded the zip file …"*

**What this settles:**
- **Journal:** the *Journal of Aircraft* stays the target. The SCImago 2025 quartile (Q2, Round 201) is recorded and not argued further.
- **Length:** no shortening before submission. E25 stands. The three of you who recommended a cut are recorded.
- **Figure:** at least one picture. The author specified the view: the aircraft sitting on its tail, seen from above at an angle (§B).
- **Template:** the author uploaded the Overleaf zip (the one all four of you named). The build now uses AIAA's own `new-aiaa.cls` with `\documentclass[journal]{new-aiaa}`. It compiles cleanly to 33 pages.

---

## B. Figure 1 (new): please check it in words, since you may not be able to see the image

**Image link (repository, for those who can open it):** https://github.com/LORDTEK/meryemAircraft/blob/main/figures/output/v8-f1-standing.png

**How it was made:**
- It is a rendering of the repository's own 3D model of the 50 kg reference design (`figures/source/body-study.html`, the same model behind the earlier three-view figures; span 3.454 m in the model, 3.453 m in the body).
- The model has an upright-stance mode, and the figure uses it.
- The script is `figures/build/mkfig_v8_stand.py`.

**What it shows:**
- The aircraft stands with its longitudinal axis vertical and the nose pair at the top.
- The four tip frames reach down to a ground grid, with the tip pairs at the frame ends. The keel line runs down the centreline to the ground.
- The strip lies along the lower surface.
- The camera is about 31° above the horizontal, at an angle off the strip side.
- There are no labels and no scale bar (in perspective a single scale bar would be misread). The figure therefore adds no number.

**One change to the model's defaults:** the model draws a 4-blade and a 3-blade nose rotor. **I set every rotor to two blades**, because that is what the analysis code uses (`aero/tip_propeller.py`: `B = 2`; the nose-propeller study: *"2 pala"*). The blade shape is the model's own, not the computed geometry. The caption says *"blades schematic"*.

**Caption (24 words):**
> The 50 kg reference design standing on its tail: nose pair uppermost, tip frames and keel on the ground, strip on the lower surface; blades schematic

**Where it is cited:** Section III, at the first sentence that describes the stance. *"The aircraft stands on its tail, with its longitudinal axis vertical, in its own storage attitude (Fig. 1)."* The next sentence names the five ground points (the four lower ends of the tip frames and the aft end of the keel). The figure shows them.

**B, everyone:**
1. Does the caption name anything the body does not define (the visual-premise rule, Round 103)? The terms are *nose pair*, *tip frames*, *keel*, *strip*.
2. Is *"blades schematic"* enough of a qualifier, or should the caption say what is not schematic?
3. Is Section III the right place for the first citation? Or would you cite it at Sec. V.B's inventory?

---

## C. Round 201's split items: please answer each other

| Item | Change it | Keep it | Asked of |
|---|---|---|---|
| **Table 6 caption** *"The four claim axes and their opponents"* | Grok, ChatGPT, Claude: two of the four rows are *"not claimed"*, so *"claim axes"* reads as if all four were claims. Proposed: *"The four axes and their opponents"* | DeepSeek, Qwen: *"claim axes"* is the paper's own term for axes on which it makes or declines claims | DeepSeek and Qwen: does the shorter caption lose anything? |
| **[2] after *"for over a decade"*** | ChatGPT, DeepSeek, Qwen: make it **[2, 3]**. Oosedo 2013 anchors the decade | — | **Grok:** you wrote that [2] should not carry the decade alone unless [3] is added. Do you accept [2, 3]? |
| **[6] repeated on the elevon sentence** | Qwen: drop it; the previous sentence already cites the vehicle | Grok, ChatGPT, DeepSeek: keep it; it is a second claim from the same paper | **Qwen:** do you accept keeping it? |

---

## D. The style pass: every change, before and after

All five of us voted for doing it now (Round 201 C). These are the rules, with your refinements merged:
- **A pair of dashes** becomes parentheses only when the inserted part is a qualifier (Grok). If it is short and nonrestrictive it becomes commas (ChatGPT). If it is a second predicate, the sentence is rewritten instead.
- **A single dash** becomes a colon when what follows explains, restates or lists (DeepSeek, Qwen). It becomes a semicolon when it joins an independent clause. It becomes a comma when only a short appositive follows.
- ***above* and *below***, where they point at text, become *preceding*, *following*, *next*, or a section reference. Physical uses stay: *above ground*, *above the stall*, *above roughly ten degrees*, *below a Reynolds number of 10⁵*.
- **Emphasis italics are removed.** The two definitions become plain sentences.
- **The run-in numbered items** of Sec. VIII.D (*"3. It does not claim …"*) become *"3) …"*.

**What is left in the output:**
- no dash in the prose;
- the four physical *above/below*;
- one ambiguous case, A11 (*"the fixed-pitch propeller is why the margin above sits where it does"*), left unchanged. **Is *"above"* there positional or physical?**

**Points I ask you to look at in particular:**
- **D55** is the only change of a word. *"and the accounting — which is what Sections 5.1 and 5.2 describe"* becomes *"; that is what"*. A comma before *"which"* would attach it to *"the accounting"* alone; the dash attached it to all three items.
- **D33.** The ratio moves after a colon: *"1.726 m: 2.43 times the pitch arm, a consequence of the layout"*. Does *"a consequence"* still attach to the ratio?
- **A12.** *"is named next"*: the strip is named in the paragraph after Table 4, not in the next sentence. Is *"next"* accurate enough?
- **A01.** *"the gap below"* becomes *"the gap set out in Section 1.5"* (Sec. I.E in the output).
- **Protected sentences.** Thirteen of the changes touch the protected register:
  - **punctuation only, in eleven:** D11, D15, D18, D28, D36, D43, D44, D45, D48, D53, D56;
  - **italics only, in one:** I7;
  - **one word, in one: A02.** The protected definition *"is the origin of all three charges below"* becomes *"… charges that follow"*.

  The American spelling of Round 201 had already reached protected sentences too (D45: *favours* → *favors*). The author is asked for one decision covering format-only changes (punctuation, spelling, italics), and separately for A02 (§H). My detection was weak: the first pass found eleven, and the second added A02 and I7. **Please check the list against the register.**

**The full list** (the generator's report, verbatim; `D` = dash, `T` = table cell, `A` = above/below, `I` = italics, `L` = list numbering):

- **D01** `this work is aimed at sit — wildfire` → `this work is aimed at sit: wildfire`
- **D02** `torque-balanced pair — so that reaction torque and net angular momentum are given up along with the reorientation mechanism — carrying` → `torque-balanced pair (so that reaction torque and net angular momentum are given up along with the reorientation mechanism), carrying`
- **D03** `on the order of a minute — roughly two percent` → `on the order of a minute, roughly two percent`
- **D04** `#### Bill 1 — mass` → `#### Bill 1: mass`
- **D05** `Mass growth feeds itself — MTOW = m_payload / (1 − f_empty − f_energy) puts additional empty mass through a multiplier that grows as the denominator shrinks — and in` → `Mass growth feeds itself (MTOW = m_payload / (1 − f_empty − f_energy) puts additional empty mass through a multiplier that grows as the denominator shrinks), and in`
- **D06** `#### Bill 2 — drag` → `#### Bill 2: drag`
- **D07** `charged mainly by the motors — hardware that cannot` → `charged mainly by the motors: hardware that cannot`
- **D08** `per unit time in cruise — so it grows` → `per unit time in cruise, so it grows`
- **D09** `#### Bill 3 — power system sizing` → `#### Bill 3: power system sizing`
- **D10** `or both — and whichever is chosen` → `or both, and whichever is chosen`
- **D11** `smaller than the reduction — measured in the same currency` → `smaller than the reduction, measured in the same currency`
- **D12** `when the sizing rule changes — toward the lighter arrangement as the rule weights mass more — and will reverse` → `when the sizing rule changes (toward the lighter arrangement as the rule weights mass more) and will reverse`
- **D13** `while changing flight regime — by rotating the whole body, or otherwise — is not in the inversion` → `while changing flight regime (by rotating the whole body, or otherwise) is not in the inversion`
- **D14** `only in part — for instance in its primary propulsor while a secondary set fails them — in which case` → `only in part (for instance in its primary propulsor while a secondary set fails them), in which case`
- **D15** `this paper does not settle — the condition is a definition` → `this paper does not settle; the condition is a definition`
- **D16** `five VTOL architecture families — nine designs in all — against` → `five VTOL architecture families (nine designs in all) against`
- **D17** `a dedicated lift group — eight lift motors` → `a dedicated lift group: eight lift motors`
- **D18** `in every other respect — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — but the difference` → `in every other respect (one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing), but the difference`
- **D19** `transfer property of Section 2.1 — the mechanism giving part of the structural saving back — inside a breakdown` → `transfer property of Section 2.1 (the mechanism giving part of the structural saving back) inside a breakdown`
- **D20** `each fail that test — including` → `each fail that test, including`
- **D21** `charged to the mass budget once — Section 5.2 gives` → `charged to the mass budget once; Section 5.2 gives`
- **D22** `or the control architecture — and because` → `or the control architecture, and because`
- **D23** `The second half — cruise carried on a wing rather than on rotors — is the subject` → `The second half (cruise carried on a wing rather than on rotors) is the subject`
- **D24** `the alternative is the rotorcraft — multirotor and helicopter alike — and as in` → `the alternative is the rotorcraft (multirotor and helicopter alike), and as in`
- **D25** `is left with one job — producing the thrust` → `is left with one job: producing the thrust`
- **D26** `continuous power supply of its own — the power the aircraft spends` → `continuous power supply of its own; the power the aircraft spends`
- **D27** `the drag outcome and the blade — a measurable advantage` → `the drag outcome and the blade: a measurable advantage`
- **D28** `not an available option — cruising there leaves too little margin above the stall — so this fixes` → `not an available option (cruising there leaves too little margin above the stall), so this fixes`
- **D29** `in the literature and in hardware — Section 1 says where` → `in the literature and in hardware; Section 1 says where`
- **D30** `The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied` → `The principle behind the third element (a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store) has been applied`
- **D31** `the body's longitudinal axis — the roll axis in body terms — in both regimes` → `the body's longitudinal axis (the roll axis in body terms) in both regimes`
- **D32** `relative to the earth — it stands vertical` → `relative to the earth: it stands vertical`
- **D33** `at the semi-span, 1.726 m — 2.43 times the pitch arm` → `at the semi-span, 1.726 m: 2.43 times the pitch arm`
- **D34** `Extension is the control variable — the strip is modulated, not switched — and deploying it` → `Extension is the control variable (the strip is modulated, not switched), and deploying it`
- **D35** `deployable in two halves — one side alone` → `deployable in two halves: one side alone`
- **D36** `produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped` → `produced by something (motor holding torque, an electrical brake, a mechanical lock), and a stopped`
- **D37** `for the 50 kg design — the only one carried` → `for the 50 kg design, the only one carried`
- **D38** `still best after it — a result of the closure` → `still best after it: a result of the closure`
- **D39** `#### Bill 2 — the drag of hover hardware` → `#### Bill 2: the drag of hover hardware`
- **D40** `exposed by the vertical-phase layout — the tip frames and the free-wheeling tip-pair rotors — is 69 percent` → `exposed by the vertical-phase layout (the tip frames and the free-wheeling tip-pair rotors) is 69 percent`
- **D41** `#### Bill 1 — carried mass` → `#### Bill 1: carried mass`
- **D42** `#### Bill 3 — released from the engine` → `#### Bill 3: released from the engine`
- **D43** `the light one is therefore the less certain — and it is the one` → `the light one is therefore the less certain, and it is the one`
- **D44** `cruise penalties — nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers — would have to fill` → `cruise penalties (nacelle drag, pivot fairing, hover-sized rotors flown as cruise propellers) would have to fill`
- **D45** `assumed more optimistically — in propeller efficiency` → `assumed more optimistically: in propeller efficiency`
- **D46** `inside the envelope, change sign — so the ordering` → `inside the envelope, change sign, so the ordering`
- **D47** `It is stated in that order — first the obstacle` → `It is stated in that order: first the obstacle`
- **D48** `can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pack` → `can exceed continuous ones (by more than a factor of two in one commercial module it cites), a pack`
- **D49** `times the bench rate — the highest figure obtained from a measurement — and 6.2` → `times the bench rate (the highest figure obtained from a measurement) and 6.2`
- **D50** `The architecture claim — that the configuration is arranged to change regime with no mechanism that reorients a propulsor — is a count` → `The architecture claim, that the configuration is arranged to change regime with no mechanism that reorients a propulsor, is a count`
- **D51** `or the transition aerodynamics — but it does depend` → `or the transition aerodynamics, but it does depend`
- **D52** `the range result or the energy store — nor on the transition` → `the range result or the energy store, nor on the transition`
- **D53** `What that refusal costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia — is not computed` → `What that refusal costs (in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia) is not computed`
- **D54** `a *class of mechanism* — the one that` → `a class of mechanism: the one that`
- **D55** `and the accounting — which is what Sections 5.1 and 5.2 describe` → `and the accounting; that is what Sections 5.1 and 5.2 describe`
- **D56** `and — while the tip pairs free-wheel or are held by motor torque — no rotor stowing` → `and (while the tip pairs free-wheel or are held by motor torque) no rotor stowing`
- **T1h** `What it creates — a bill by its number, any other cost in words` → `What it creates (a bill by its number, any other cost in words)`
- **T1a** `| 3 — the cruise engine no longer sizes to hover | 1 and 2 — many rotors` → `| 3: the cruise engine no longer sizes to hover | 1 and 2: many rotors`
- **T1b** `| 2 — the exposed rotor is removed from cruise | 1 — mechanism,` → `| 2: the exposed rotor is removed from cruise | 1: mechanism,`
- **T1c** `| 1 — one propulsion group serves both regimes | kilograms, not Bill 1 — the pivot` → `| 1: one propulsion group serves both regimes | kilograms, not Bill 1: the pivot`
- **T1d** `supplies its hover peak — with no store, the power plant is sized by the hover peak; and` → `supplies its hover peak (with no store, the power plant is sized by the hover peak); and`
- **T1e** `| 1 and 3 — one propulsor is retrimmed` → `| 1 and 3: one propulsor is retrimmed`
- **T1f** `kilograms, not Bill 1 — pitch hub and actuation` → `kilograms, not Bill 1: pitch hub and actuation`
- **T1g** `| 1 and 2 — smaller, lighter, cleaner rotors | 3 — hover power rises` → `| 1 and 2: smaller, lighter, cleaner rotors | 3: hover power rises`
- **T1i** `| 3 — hover power falls | 1 and 2 — larger structure` → `| 3: hover power falls | 1 and 2: larger structure`
- **T4a** `| Pivot or tilting joint | Tilting architectures | — |` → `| Pivot or tilting joint | Tilting architectures | None |`
- **T4b** `| Nacelle or rotor-group actuator | Tilting architectures | — |` → `| Nacelle or rotor-group actuator | Tilting architectures | None |`
- **T4c** `or feather a rotor unused in one regime | — |` → `or feather a rotor unused in one regime | None |`
- **T4d** `| Dedicated lift rotors | Lift-plus-cruise architectures | — |` → `| Dedicated lift rotors | Lift-plus-cruise architectures | None |`
- **T4e** `from the cruise flow by such means | — (see note) |` → `from the cruise flow by such means | None (see note) |`
- **T6a** `This is the paper's contribution — a count of mechanism classes` → `This is the paper's contribution: a count of mechanism classes`
- **T6b** `| Other hybrids — lift-plus-cruise, tilt |` → `| Other hybrids (lift-plus-cruise, tilt) |`
- **A01** `the gap below is not a historical one` → `the gap set out in Section 1.5 is not a historical one`
- **A02** `the origin of all three charges below` → `the origin of all three charges that follow`
- **A04** `they are the first failure mode below` → `they are the first failure mode that follows`
- **A05** `The mission used below is short` → `The mission used here is short`
- **A07** `The qualifications below apply to them too` → `The qualifications that follow apply to them too`
- **A10** `it does not touch the cruise numbers above` → `it does not touch the preceding cruise numbers`
- **A12** `is a control surface, of a different class, and is named below` → `is a control surface, of a different class, and is named next`
- **A13** `that cancellation is no longer exact (below)` → `that cancellation is no longer exact (discussed later in this section)`
- **A14** `(body axes, as fixed above)` → `(body axes, as fixed earlier in this section)`
- **A15** `The sizing above says nothing` → `The preceding sizing says nothing`
- **A16** `would most change the numbers above` → `would most change the preceding numbers`
- **A18** `the boundary below is about claims` → `the boundary that follows is about claims`
- **I1** `in which *every* propulsor` → `in which every propulsor`
- **I2** `only *one orientation relative to the airframe*` → `only one orientation relative to the airframe`
- **I3** `*Cruise thrust in this paper means the thrust that balances cruise drag.*` → `Cruise thrust in this paper means the thrust that balances cruise drag.`
- **I4** `*Note.* The stopping class` → `Note: The stopping class`
- **I5** `*(This paper fixes body-axis naming throughout.` → `(This paper fixes body-axis naming throughout.`
- **I6** `The two conventions are not mixed here.)*` → `The two conventions are not mixed here.)`
- **I7** `The *size* of the resulting advantage` → `The size of the resulting advantage`
- **I8** `The design *sizes* vertical operation` → `The design sizes vertical operation`
- **L1** `1. ` → `1) `
- **L2** `2. ` → `2) `
- **L3** `3. ` → `3) `
- **L4** `4. ` → `4) `
- **L5** `5. ` → `5) `
- **L6** `6. ` → `6) `
- **L7** `7. ` → `7) `
- **L8** `8. ` → `8) `

**D, everyone:** for each change, **yes**, or **no with the smallest repair**. Check two things in particular:
- whether a qualifier's scope moved (the reason the dashes were done now and not left to copy-editing);
- whether a protected sentence changed anything but punctuation.

---

## E. Next: the journal supplement

All five of us agreed in Round 201 (D) on the plan:
- a second generator writes the journal supplement from the working part of `paper/v8/supplement.md` only;
- the S-numbers stay;
- a receipt check covers every body pointer;
- the audit archive stays in the repository and on Zenodo.

It is built next. Its output and its receipt table come in the next round.

---

## F. Your own proposals

Open, as always.

---

## G. Errors (one list)

- **Claude:** I had not checked the target journal's quartile before work began on it, although the author had said the calculations were done *"for Q1"* (Round 61). Round 201 found SJR 2025 Q2. The author has now decided to stay with the *Journal of Aircraft*.
- **Qwen:**
  - The Q2 answer gave no page it had opened.
  - Its Q3 proposals would move Sec. I.D's occupied-literature detail and II.A's bill derivations. Both are protected by earlier decisions: the gap rule (what is occupied is stated in the body before the gap), and the Round 173 closure.
- **DeepSeek:**
  - Its Q2 history (*"Q1 for 2021–2024"*) conflicts with Grok's (*"Q1 through the mid-2010s"*). It is unresolved, and is now moot.
  - One of its AIAA citations came from a third-party mirror (`klabs.org`), not from AIAA.
- **Grok, ChatGPT:** none found.

---

## H. What goes to the author

**Two decisions:**
1. May **format-only** changes be made in protected sentences in the submission output? These are punctuation (a dash becoming a comma, parentheses, a colon or a semicolon), American spelling, and the removal of italics. No word changes. This covers twelve protected sentences, and the spelling already applied.
2. **A02:** the protected definition *"is the origin of all three charges below"* becomes *"… that follow"* (AIAA: avoid *"below"*). Yes or no.
