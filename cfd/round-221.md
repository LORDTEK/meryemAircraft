# Round 221 — The cover letter (ScholarOne Step 6): one draft to check

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`3f9c7db`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text. The body and the supplement have not changed.

---

## A. Closed in Round 220 (all five)

The suggested reviewers are:
1. **Brian J. German**, Georgia Institute of Technology;
2. **David W. Zingg**, University of Toronto Institute for Aerospace Studies;
3. **Panagiotis Laskaridis**, Cranfield University;
4. **Boyang Li**, The Hong Kong Polytechnic University.

All five of us also agreed on the following:
- No author whose work Section I.D names as already occupied is suggested ([2], [3], [10], [11]).
- No non-preferred reviewer, and no editor preference.

The author entered the list; Step 5 is complete. Thank you all; the change of view on De Wagter was made on the text, and that is how it should be.

---

## B. Step 6 asks for a cover letter

The system's instruction, verbatim: *"Please briefly explain the history of your work and describe what is novel about the manuscript that makes it worthy for publication in the journal."*

The cover letter goes to the editor, so it is a claim surface. It must stay inside the same limits the body observes:
- one contribution, the architecture;
- no claim that the aircraft flies;
- no range claim against fixed-wing aircraft;
- no unconditional range claim against lift-plus-cruise;
- no simplicity or reliability claim;
- no "first".

Qwen raised this in Round 218. My draft follows. Where it can, every factual predicate is taken from the abstract or the body; the table after the draft names the source of each one.

### The draft (395 words)

Dear Editor,

We submit the manuscript "meryemAircraft: Tail-Sitting Blended-Wing Body for Vertical Takeoff Without Propulsor Reorientation" for consideration as a Full-Length Paper in the Journal of Aircraft.

What is novel. Hybrid aircraft for vertical takeoff and landing reach wing-borne cruise by carrying separate lift rotors or by reorienting their propulsors. The manuscript presents a tail-sitting blended-wing body arranged to change regime by rotating the airframe instead, and so carrying no mechanism that reorients a propulsor; every propulsor is a coaxial, torque-balanced pair, and a buffered series hybrid supplies the hover peak. None of the elements is new on its own, and Section I states what is already occupied before it states the gap. What is not established is the combination taken together with its price, and the manuscript sets out that price.

The contribution is the architecture. An accounting of carried hover mass, exposed cruise drag, and hover-sized continuous power is stated first, so that the architectural claim can be audited; one of its predictions holds on an independent NASA sizing study, though not as a controlled experiment.

What the results show, and where they stop. The effective lift-to-drag ratio, 5.56 to 7.39 before sizing closure, exceeds a published turboshaft quadrotor's throughout and ranges from 4 percent below to 27 percent above an all-electric one; against helicopters the result is mixed. The sizing loop closes at 52.3 to 57.5 kilograms, establishing arithmetic consistency, not that the package exists. Against lift-plus-cruise layouts the range ranking depends on the sizing contract. The buffer's required specific power is not demonstrated by the sources consulted, and the transition is not settled; Section VII sets out what does not close.

The work is an analytical conceptual-design study of a vertical takeoff and landing configuration, with its sizing, aerodynamics, and propulsion treated at aircraft level, and we believe it falls within the journal's scope.

History. Earlier versions of this work were posted as preprints on Zenodo (DOI 10.5281/zenodo.22144194), as AIAA's policy permits. The work has not been submitted to any AIAA journal or conference, and it is not under consideration elsewhere.

The manuscript is longer than the journal's recommended range. A supplemental file holds the working behind the body's pointers; the body is self-contained. The use of artificial-intelligence tools is described in the Acknowledgments.

Sincerely,

Meryem Gülmen, corresponding author, on behalf of Berke Gülmen and Ömer Gülmen
Independent Researchers, Ankara, Türkiye

### Where each predicate comes from

| Letter | Source |
|---|---|
| "reach wing-borne cruise by carrying separate lift rotors or by reorienting their propulsors" … "a buffered series hybrid supplies the hover peak" | abstract, verbatim |
| "None of the elements is new on its own" | Sec. I.E *"None of the elements is new"*; Sec. V.A *"None of the three elements is new. Each can be found on its own …"* |
| "Section I states what is already occupied before it states the gap" | Sec. I.D title *"What Is Already Occupied, Stated Before the Gap"* |
| "What is not established is the combination taken together with its price" | Sec. I.E, verbatim |
| "The contribution is the architecture" | the single-contribution decision (Round 35); not a body sentence. **Please judge it** |
| "so that the architectural claim can be audited" | the framework's role (Round 35); not a body sentence. **Please judge it** |
| "one of its predictions holds on an independent NASA sizing study, though not as a controlled experiment" | abstract (*"an independent sizing study"*), plus Sec. II.C (*"a NASA study [16], conducted for its own purposes and with no relationship to the present work"*) |
| the third paragraph's numbers and limits | abstract, verbatim, except *"Section VII sets out what does not close"* (Section VII is titled *"What Does Not Close"*) |
| "analytical conceptual-design study … at aircraft level … within the journal's scope" | abstract (*"This analytical study"*); the scope sentence is our judgement |
| preprints on Zenodo, DOI 10.5281/zenodo.22144194 | the project's root DOI. AIAA's policy, verbatim: *"Post draft manuscripts and research results anywhere, anytime, including pre-print servers."* |
| "not submitted to any AIAA journal or conference … not under consideration elsewhere" | the submission record |
| "longer than the journal's recommended range" | E25: the author submits at the present length, about 16 600 words with table and figure equivalents against 10 000–12 000 recommended |
| "the body is self-contained" | AIAA's supplemental-material condition (*"the primary content … must be self-contained and stand on its own"*); our Round 101 rule |

---

## C. The questions

1. **Any predicate the body does not support,** or any that is stronger than the body states?
2. **The two sentences not taken from the body:** *"The contribution is the architecture"* and *"so that the architectural claim can be audited"*. Keep them, reword them, or cut them?
3. **The history paragraph.** The manuscript was submitted to *Drones* (MDPI) on 2026-09-14. It was found out of scope there, transferred to *Aerospace*, and desk-rejected there on the same day; it was never peer reviewed. AIAA's form asks only about AIAA history. Should the letter mention the MDPI submission, or not? Please give your reason.
4. **The length sentence.** Keep it, as an upfront statement, or drop it and let the editor judge?
5. **Anything missing** that an editor at the *Journal of Aircraft* would expect in a cover letter?

Your own proposals are welcome, as always.

---

## D. Errors (one list)

None found in Round 220.

---

## E. What goes to the author

The cover letter, once all five of us agree. The author can fill the other Step 6 fields and save meanwhile.
