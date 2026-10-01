# Round 222 — The cover letter, second pass; and the two AI-use fields you have not yet seen

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`3d317bd`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. Facts checked this round against the submitted body and abstract

| Phrase in the letter | Where it stands | Who said what |
|---|---|---|
| *"The contribution is the architecture"* | **Body, Sec. I.E**, verbatim: *"The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor."* | Grok and DeepSeek: my table's *"not a body sentence"* was wrong. **They are right; it is my error.** |
| *"audited"* | **Body, Sec. I.E**: *"… and audited explicitly against carried hover mass, exposed cruise drag and hover-sized continuous power …"* | DeepSeek: *"'Audited' is the body's word."* Grok: *"The body says the accounting is what the paper is checked against, not that the claim is audited."* |
| *"one of its predictions holds on an independent … sizing study, though not as a controlled experiment"* | **Abstract, verbatim** (*"NASA"* from Sec. II.C) | ChatGPT proposes *"is supported by … though not by a controlled experiment"* |
| *"establishing arithmetic consistency, not that the package exists"* | **Abstract, verbatim** | ChatGPT: *"an interpretation rather than a body statement"*; proposes *"this establishes a closed sizing result, not that the package exists"*. Qwen: *"a precise reflection of Section 6.1"* |

---

## B. The five positions, side by side

| Question | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|
| 1. Predicates | pass | pass, with two repairs (*"holds"*; *"arithmetic consistency"*) | pass | pass | pass. Both phrases ChatGPT would repair are the abstract's own words. The letter and the abstract go to the same editor, and I would not have them say the same thing two ways |
| 2a. *"The contribution is the architecture"* | keep (Sec. I.E) | keep | keep (Sec. I.E) | keep | keep (Sec. I.E) |
| 2b. *"so that the architectural claim can be audited"* | reword: *"… can be checked"* | reword: *"making the architectural claim quantitatively explicit"* | keep (*"the body's word"*); *"checked against an explicit accounting"* acceptable | keep | keep: *"audited"* is Sec. I.E's word. Grok's *"checked"* is acceptable to me. ChatGPT's form loses the link to the accounting being a test |
| 3. Mention the MDPI submission | **yes**, one sentence: the instruction asks for *"the history of your work"*, and *"a later finding of that record is worse than one sentence now"* | no: the form asks about AIAA history; the MDPI outcomes are irrelevant to the content | no: not peer review; it invites questions. If a field asks, answer it truthfully | no: the form asks only about AIAA history | **no**, for the reasons ChatGPT, DeepSeek and Qwen give. But Grok's reading of the instruction is accurate: it says *"history of your work"*, not *"AIAA history"*. This goes to the author if we stay split |
| 4. Length sentence | keep | keep, shortened: *"The manuscript exceeds the journal's recommended length; the body is self-contained, and the supplemental file contains the working material behind its pointers."* | keep | keep | keep. ChatGPT's shorter form is acceptable to me |
| 5. Missing | nothing | nothing | the corresponding author's email in the signature; a date (optional); a named subject area (optional) | *"All authors have read and approved the final manuscript, and we have no conflicts of interest to disclose."* | the email: **yes**; it is already in the manuscript's footnote. A date: no, since ScholarOne stamps it. Qwen's sentence: the first half is in our Acknowledgments. *"No conflicts of interest"* is the authors' own declaration, so it goes to the author |

**Please reply to each other where you differ, not only to me.**
- **Grok:** please answer the three who would not mention the MDPI submission. **ChatGPT, DeepSeek, Qwen:** please answer Grok's reading of *"the history of your work"*.
- **ChatGPT:** on 1 and 2b, do the facts in §A change your view? The other three would keep the abstract's and the body's words.

---

## C. The two AI-use fields (added to Round 221 after you received it)

You did not see this part of Round 221; it was added after the text had gone to you. Here it is in full.


The form asks: *"Was artificial intelligence (AI) or an AI-based tool used to generate significant content in this manuscript, including writing text, creating figures, generating a literature review, etc.?"*
- Our Acknowledgments say the tools were used *"to draft and revise the English text, to search the literature"*, so the author answered **Yes**. The language question is also **Yes**.
- A required field then appeared: *"Please provide a detailed explanation of how AI was used to generate content in this manuscript."*

My draft (197 words; no brand, model or company name, per our rule):

> The authors used general-purpose large-language-model assistants, under their direction, in four ways. (1) Text: the assistants drafted and revised the English text from the authors' instructions and earlier drafts. (2) Literature: the assistants searched the literature; quotations and numbers taken from sources were checked against the source documents themselves, not against search summaries, and the one source known only from its abstract is used only for what that abstract states. (3) Review: several assistants were used as independent readers of the manuscript, to find errors, unsupported statements and inconsistencies between sections; their proposals were applied only after being checked against the manuscript and its sources, with contested points decided by the authors. (4) Calculations and figure: the assistants wrote and ran the analysis code (sizing, aerodynamic, propulsion and transition calculations) under the authors' direction, and the script that renders Figure 1 from the design geometry; the numerical results are reproduced by these scripts, and automated checks compare the numbers in the text with their outputs. The concept, architecture, design and solution approach are the authors' own. No AI tool is an author; all three authors read and approved the manuscript and take full responsibility for its content.

A third required field: *"Please provide a detailed explanation of how AI was used to improve the language in this manuscript."* My draft (120 words):

> The authors' working language is Turkish; the assistants rendered the authors' content in English and then improved the language of the manuscript under the authors' direction: grammar, clarity, concision, consistent terminology, American spelling, and the journal's style for headings, references and units. Several assistants read the text independently and proposed wording changes; each change was compared with the text it replaced, and a change that altered a claim, a limit or a number was rejected. Sentences that state the paper's claims and limits were kept on a list that may be changed only by the authors' decision, and scripts checked that every such sentence survived each revision and checked key numbers against the analysis outputs. The authors read and approved the final text.

**Facts the draft rests on:**
- [13] (Merical) is known to us from its abstract only (Round 195). The body uses it only for *"series-hybrid propulsion has been designed for small uncrewed aircraft"*.
- Figure 1 is rendered by `figures/build/mkfig_v8_stand.py`, which I wrote, from the three-dimensional model of the reference design.

**A gap this reveals.** The form's question names *"creating figures"*, and AIAA requires, verbatim: *"if AI was used in the writing process or figure construction … a brief description of its use in the Acknowledgments section"*.
- The Acknowledgments sentence (E31, the author's decision) names text, literature, review and calculations. **It does not name the figure.**
- Options:
  - **(a)** add *"and to write the code that renders Figure 1"* to the Acknowledgments sentence. This is the author's decision, and the PDF and the source are rebuilt and re-uploaded.
  - **(b)** leave the sentence as it is, on the reading that rendering code falls under *"as a tool in carrying out the calculations"*.
  - **(c)** another form.

My view is (a), because the form itself names figures, and a field that says more than the Acknowledgments is the kind of mismatch the Step 6 check is meant to catch.

---

---

## D. The questions

1. **The cover letter:** your view on 1, 2b, 3, 4 and 5 after §A and §B.
2. **The two AI-use explanations (§C):** is any statement inaccurate, or stronger than the Acknowledgments?
3. **The figure gap (§C):** (a), (b) or (c), with your reason.

---

## E. Errors (one list)

- **Claude:** the Round 221 source table said *"The contribution is the architecture"* is *"not a body sentence"*. It is a protected body sentence in Sec. I.E. Grok and DeepSeek caught it.
- **Claude:** I did not check that *"audited"* is also Sec. I.E's word. DeepSeek did.
- **Claude:** §C was added to Round 221 after it had gone to you, so none of you saw it. It is given in full above.

---

## F. What goes to the author

The cover letter and the two AI-use texts, once all five of us agree. These go to the author in any case:
- the figure gap, (a) or (b), which is the author's decision because it changes the Acknowledgments sentence;
- the conflict-of-interest sentence, which only the authors can make;
- the MDPI question, if we stay split.
