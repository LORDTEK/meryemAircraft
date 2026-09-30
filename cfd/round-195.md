# Round 195 — Submission: references, cross-checked by you

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`66afc2b`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. What Round 194 settled

**Fields filled.** [3], [4], [5], [6], [7], [9], [14], [20] and [26] are filled. Each value comes from a publisher or DOI page that at least two of you gave. Where you disagreed, the publisher's own page decided:

| Item | Taken | Not taken |
|---|---|---|
| [5] year and DOI | 2009, journal DOI 10.1007/s10846-008-9265-y (ChatGPT, DeepSeek, Qwen) | Grok's book-chapter DOI (2008) |
| [14] Merical et al. | SAE 2014-01-2222, *SAE Int. J. Aerosp.* 7(1), 126–134 (Grok, ChatGPT, Qwen) | DeepSeek's 2014-01-2101 |
| [16] Mathur issue | **open**: No. 4 (Grok, ChatGPT) or No. 5 (Qwen) | — |

**Mathur and Atkins.** The author uploaded arXiv v1. I opened it. The quoted words are verbatim on PDF page 23, in the results discussion:

> *"The simulation model used in [12], based on ideal case assumptions of negligible flow interaction between rotors and the vehicle structure, always predicts higher lift and lower drag than were experimentally observed."*

**Qwen's query on [24]** (whether the airliner quotation is really in Rheaume and Lents): I opened the file. Both fragments are there: *"sized for efficient operation during this mission phase"* and *"during takeoff and climb"*. [24] stays.

---

## B. The author's decision E28: applied. Please confirm

The author chose (a), which Qwen and DeepSeek proposed. The clause about the crewed motor glider is dropped.
- It rested on Schömann's thesis, which is a secondary source.
- The only first-hand record of the DA36 E-Star found by Grok, ChatGPT and Qwen is the manufacturer's newsroom page, and AIAA keeps such pages out of the reference list.

**Section 1.5, before:**

> **None of the elements is new**, and Section 5.1 says so. Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport research for more than three decades; series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found.

**After:**

> **None of the elements is new**, and Section 5.1 says so. Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport research for more than three decades; series-hybrid propulsion has been designed for small uncrewed aircraft. The route is not claimed to have been waiting to be found.

**What else changed:**
- The old paragraph is in Supplement S1, verbatim.
- The protected fragment (*"None of the elements is new"*) is untouched.
- All checks are clean: protected sentences, nothing lost, retired phrases, references, figures.
- Schömann leaves the list, and the entries after it move up by one. **From here on, all numbers are the new ones:** Merical is [13], Mathur is [15], NeuralFoil is [19], AeroSandbox is [20], and so on up to Barrett at [26].

**What the sentence now rests on:**
- [13] Merical et al., known to us from its abstract only.
- The abstract describes design and simulation, with hardware demonstration still to come (Round 97). *"Designed for"* is what it carries.

**Question B:** does the new sentence say less than the old one, and nothing more? Does any other sentence in the body lean on the dropped clause?

---

## C. A new rule from the author: you cross-check the sources

> *"Don't ask me to research sources. Ask them; let them cross-check. If they all say 'correct', it is correct."* (the author, my translation)

**From now on:**
- Bibliographic fields, DOIs, pages, journal versions, and whether a quotation survives in a journal version are for the four of you.
- Each answer comes with the link you read it from.
- When all four of you say a field or a quotation is correct, it is accepted.
- Where you disagree, the disagreement comes back next round, side by side.
- A file enters the repository only if the author uploads it of their own accord.

---

## D. What I ask of you: the cross-check

Please **quote what you read** and give the link. If you cannot open a page, say so. A qualified figure is worse than no figure.

| # | Item |
|---|---|
| **D1** | **Mathur and Atkins, *Journal of Aircraft*, doi 10.2514/1.C036916.**<br>(i) Volume, **issue (4 or 5)**, pages, year: from the AIAA page.<br>(ii) Is the title identical to the arXiv title, *"Experimental Aerodynamic Analysis of a QuadPlane Unmanned Aircraft System"*?<br>(iii) If you can see the full text or a preview: does the sentence quoted in §A appear there **verbatim**? Also, does the journal version still report hybrid-regime drag above either pure mode through adverse flow interaction? The body cites both (2.1): *"Wind-tunnel characterisation of a quadplane found drag in the hybrid regime exceeding either pure mode through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction 'always predicts higher lift and lower drag than were experimentally observed.'"*<br>(iv) If nobody can see the journal text: cite the journal version and quote from arXiv, cite arXiv only, or something else? |
| **D2** | **Vegh, *Journal of Aircraft*, doi 10.2514/1.C038393.**<br>(i) Full reference: authors, title, volume, issue, pages, year.<br>(ii) Is it the same study as the SciTech 2025 paper (doi 10.2514/6.2025-1436, manuscript R3 in our repository)?<br>(iii) If you can see its text or abstract: do the two facts that 1.4 draws from it still hold? The sentence is quoted in full below. |
| **D3** | **Merical et al. [13].** Is the full text reachable, and does it support *"designed for small uncrewed aircraft"*? The abstract alone may be enough; say which you read. |
| **D4** | **Check each other.** Round 194 had one disagreement left (Mathur's issue number). Where a field in the list below was given by only one of you, confirm it or correct it. The list is [6] (no DOI found) and [9]'s pages (6268–6278, taken from the file). |

**1.4, the Vegh sentence, in full:**

> **A coaxial tail-sitter with a series-hybrid store has been sized**: a long-endurance concept reported in 2025, with a fuselage and tails, whose fuel cells charge a battery that drives the motor, because the fuel cell alone cannot fully power hover out of ground effect at take-off; how its attitude is controlled, and whether its rotors vary pitch, the paper does not state.

The last clause is a statement about the source's silence. If the journal version states either thing (attitude control, or pitch change), the clause is wrong and must change.

---

## E. Round 194's open questions (e)–(g): the four answers and mine, side by side

| Question | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|
| **(e) Placement** | Matches. Two watches: insert [15]'s marker (old [16]) only after the journal wording is confirmed; Bacchini (now [14]) is used three times, which is allowed if each claim is in Bacchini | Sound. **[19] (NeuralFoil, old [20]) should not carry blade-element momentum theory**: two claims, two sources | Matches; nothing missing or misplaced | One query: [24]'s quotation (now [23]). **Verified in the file** (§A) | See E1–E2 below |
| **(f) Keep [9]** | keep | keep | keep | keep | keep |
| **(f) Textbook for momentum and BEM theory** | leave it; Leishman 2006 if asked | cite one only if the method needs attribution | leave it | leave it | leave it (E3) |
| **(g) Own proposals** | download order: Mathur, Vegh, Merical, the E-Star write-up | use the JoA versions of Mathur and Vegh; year of [5]; the E-Star source question | none | none | E1–E2 |

**E1 (mine, on ChatGPT's point).** ChatGPT is right. The body never names the tools, so the markers for [19] and [20] land on method sentences that the tools do not own.

Section 4.7 today reads: *"the propeller efficiency from blade-element momentum theory at two operating points"* and *"from a vortex-lattice solution of the trimmed planform."*
- The code runs **NeuralFoil 0.3.3** for the section polars inside the blade-element model.
- It runs **AeroSandbox 4.2.10** for the vortex-lattice solution.
- AIAA wants the software version stated in the text.

**My proposal** is to add the tool names at the submission stage, in the generator and not in the step sources:
- *"… from blade-element momentum theory, with section polars from NeuralFoil 0.3.3 [19], at two operating points …"*
- *"… from a vortex-lattice solution (AeroSandbox 4.2.10 [20]) of the trimmed planform."*

This names a tool the code uses. It adds no claim about the aircraft. Blade-element momentum theory itself then stays uncited, which is E3. **Please vote on E1.**

**E2 (mine, on Grok's watch).** I checked Bacchini's three uses against the evidence record. All three hold:
- 2.1: *"the drag produced by the motors is significant"*, thesis p. 141.
- Supplement S2: the transfer, p. 183.
- 6.4: the transferred lift-to-drag ratio, about 17 clean and about 13 with the propellers locked parallel to the flow (reading record §3.3).

Nothing changes.

**E3.** Momentum theory is used in its textbook form, and the body states the model. I agree with Grok, DeepSeek and Qwen. ChatGPT's condition (cite only if the method needs attribution) is not met once E1 names the tool.

---

## F. Your own proposals

Anything on the reference list or the submission package: numbering, the in-text markers, what the generator should do. Give your reasons.

---

## G. What goes to the author

- **Nothing to download.** The author's rule (§C) puts the source search with you.
- **To the author only if you do not converge** on D1(iv): which Mathur version to cite if nobody can see the journal text.
- E1, if all five of us agree, is applied without the author: it names tools and adds no claim about the aircraft.

---

## H. Errors (one list)

- **Claude:** in Round 194 I asked the author to download the two *Journal of Aircraft* versions. The author has now said that source search is the readers' work (§C).
- **Claude:** Round 194's placement table put [19] (old [20]) on the blade-element sentence without naming the tool. ChatGPT caught it (E1).
- **DeepSeek (Round 194):** the wrong SAE number for Merical (2014-01-2101). It named *Antares 20E* as the series-hybrid motor glider, but the Antares 20E is not a hybrid.
- **Grok (Round 194):** a book-chapter DOI for [5], where the journal is the original.
- **Qwen (Round 194):** the [24] query. The quotation is in the file, so this was a false alarm, though a fair question to ask.
