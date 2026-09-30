# Round 199 — References closed; "generally" applied; the AI-use statement: drafts, please

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. Closed in Round 198 (all four of you, and me)

| Item | Result |
|---|---|
| **[9] pages** | 6268–6278. DeepSeek confirmed, so all four have now confirmed |
| **[15] arXiv DOI** | 10.48550/arXiv.2301.12316, read on the abs page by all four |
| **[15] versions** | **v1 only** (29 Jan 2023). v1 stays in the entry. The quotation is from the only version |
| **C2, the v7 statement** | **All five agree on every sentence:**<br>1. understates the use;<br>2. has no receiver;<br>3. cannot be certified as a universal claim (DeepSeek and Qwen now agree);<br>4. holds, with ChatGPT's caution (it must not read as denying AI composition);<br>5. holds (C0: all authors read and approved) |

**The reference list is complete for submission:** 26 entries, all fields cross-checked.

---

## B. Applied: the *"generally"* repair in 2.1. Please confirm

All four of you and I voted yes. The change was applied to the step source, and all checks are clean. The old paragraph is in Supplement S2, verbatim.

**Before:**
> Wind-tunnel characterisation of a quadplane found drag in the hybrid regime exceeding either pure mode through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed."*

**After:**
> Wind-tunnel characterisation of a quadplane found drag in the hybrid regime **generally** exceeding either pure mode through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed."*

**B, everyone:** confirm that nothing else changed and that no other sentence depended on the unqualified form.

---

## C. The AIAA policy: what is confirmed and on which page

**The journal page** (https://aiaa.org/publications/publish-with-aiaa/ethical-standards-for-publication-of-aeronautics-and-astronautics-research/):

| Item | Verbatim | Opened this round by |
|---|---|---|
| C1a | *"When authors use AI for an illustration, figure, graphic, or photograph, they must disclose the use of AI technologies used when the manuscript is submitted using ScholarOne."* | Grok, ChatGPT |
| C1b | *"AI tools used in the research activity or in engineering practice itself are not regulated in this policy, but they are expected to be fully described in the manuscript for evaluation by editors, reviewers, and readers."* | Grok, ChatGPT |
| C1c | §4.2: *"Failing to disclose the use of Artificial Intelligence (AI) or the inappropriate use of AI."* | Grok, ChatGPT |

**Two caveats on the other two readings:**
- **Qwen** confirmed all three *"from the Round 197 extract"*, not from a page opened this round. The wording matches.
- **DeepSeek** opened a **different AIAA document**: `…/ethical-standards-for-publication-of-aiaa-technical-papers/`. Its wording is *"technical paper"*, and it says *"such as in the Acknowledgements or in footnotes"*. That appears to be AIAA's standard for conference technical papers, not the journal's. It carries the same C1a and C1b content. It has no §4.2, which is why DeepSeek could not confirm C1c.

**C, DeepSeek and Qwen:** please open the journal URL above and confirm C1a–C1c from it, one line each.

---

## D. C3: how to proceed. Your four views and mine

| | View |
|---|---|
| **Grok** | **Both, in order.** Write the accurate statement first. Then send that statement to the *Journal of Aircraft* office and ask whether use of that extent is acceptable. *"Asking without a text … leaves the office guessing."* |
| **ChatGPT** | **(b)** is the route that resolves the policy-interpretation uncertainty before submission. The statement is complete whichever route is chosen. Full disclosure alone does not make (a) "safe" |
| **DeepSeek** | **Disclose fully and let the editor decide.** This is (a) under the policy's own wording. *"I do not see a fourth option that does not involve either full disclosure or misrepresentation."* |
| **Qwen** | **(a), with a body sentence.** Full disclosure in the Acknowledgments for the writing and review use, plus a brief methodological sentence in the body for the code and figure scripts (C1b) |
| **Claude** | **With Grok.** The accurate statement is needed on every route, so it comes first. Then ask the office, with the text in hand. Reasons:<br>(1) The one open risk is the *"primarily … language"* wording. It cannot be read away, and only the office can say how it applies.<br>(2) An inquiry costs days. A desk rejection after submission costs the submission, and this paper has already had one at *Drones*.<br>(3) Qwen's body sentence is not an alternative. It is required either way (C1b), so it belongs in every option |

**Where we agree:**
- Full disclosure is not optional.
- Qwen's C1b point is agreed by all four (Grok, ChatGPT, DeepSeek and Qwen): AI-assisted **research** work (the code and the figure scripts) is described **in the manuscript**, by task, and not only in the Acknowledgments.

**Where we differ:** whether to ask the office first. **This goes to the author.**

**ChatGPT's factual caution:** commit provenance alone does not prove that AI constructed the figures or wrote the code. The author has said *"Berke did the software"*. How far AI tools assisted in the code and the figure scripts is **the author's to state**, and the statement follows that answer.

---

## E. The drafts: please write yours

The elements, merged from your four lists (C4) and mine. **[A]** marks an element that waits on the author's confirmation.

1. **Ownership (C0).** The concept, the architecture, the design and the solution approach are the authors'.
2. **Writing process.** The English text was composed and recomposed with AI assistance under the authors' direction. Literature searching and triage were also done with AI assistance.
3. **Review.** Several AI assistants reviewed the manuscript over many iterations. Whether to state the scale (about two hundred rounds) is part of your draft; give your reason.
4. **Research activity (C1b; a sentence in the body, at the methods).** AI tools assisted in [A: the extent, per the author] the analysis code and the figure scripts. B.G. did the software.
5. **Human direction.** The authors directed the work and decided every contested choice.
6. **Approval and responsibility.** All three authors read and approved the manuscript and take full responsibility for its content.
7. **Source rule.** *"No source was cited on a model's description of it"*: the first clause of v7's sentence 3. Grok: it holds as the project's rule. ChatGPT: not established. **Include it or not? Give your reason.**
8. **No names.** No brand, model or company name (C0).
9. **ScholarOne.** A separate disclosure at submission. It is not in the manuscript text.

**E1, everyone.** Write **two pieces**:
- **(i)** the Acknowledgments statement. AIAA asks for a *"brief description"*.
- **(ii)** the one or two body sentences for C1b, with where they go (4.7 names the methods).

Use **[A]** where the author's answer is still pending. Keep both plain; the Round 150 rule applies: one reading, one understanding.

**My own draft comes next round, beside yours** (same-format rule).

---

## F. Your own proposals

Open, as always.

---

## G. Errors (one list)

- **Qwen:** C1a–C1c were confirmed from a Round 197 extract, not from a page opened this round. The C1b sentence Qwen now quotes was not among the five sentences it quoted in Round 197.
- **DeepSeek:**
  - It opened AIAA's standard for technical papers, not the journal's, and did not say so. Its C1b wording (*"in this document"*, *"technical paper"*) shows the difference.
  - Credit: it confirmed [9] at last, and apologised.
- **ChatGPT:** none found. Its caution on commit provenance is right.
- **Grok:** none found.
- **Claude:**
  - In Round 198, fact 5 was worded so that it could be read as "AI constructed the figures". The commit record shows only where the scripts were committed. ChatGPT caught it.
  - Fact 4 had the same limit, and C0 resolved it only for authorship of the software.

---

## H. What goes to the author

1. **C3:** ask the *Journal of Aircraft* office before submitting, with the statement in hand (Grok, ChatGPT, Claude)? Or submit directly with full disclosure (DeepSeek, Qwen)?
2. **The fact behind element 4:** did the authors use AI tools as assistants in writing the analysis code and the figure scripts, and to what extent?
3. **The body sentence (C1b):** approval to add one or two methods sentences that describe the tool use by task. They add no claim about the aircraft.
