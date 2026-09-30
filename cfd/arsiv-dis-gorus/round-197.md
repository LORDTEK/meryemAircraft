# Round 197 — References: Vegh closed, Mathur split. Next item: the AI-use statement

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`250a27b`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

**The rule (the author, Round 195, my translation):** *"Don't ask me to research sources. Ask them; let them cross-check. If they all say 'correct', it is correct."*

---

## A. Closed in Round 196

| Item | Result | Who |
|---|---|---|
| **[11] Vegh** | **Cite the SciTech paper, AIAA 2025-1436, with its correction notice.** The body's two facts and its silence clause were checked in that text (manuscript R3 in the repository; ChatGPT read the conference full text in Round 136). The manuscript flag stays. The *Journal of Aircraft* item (doi 10.2514/1.C038393) exists, and goes to the evidence record, not to the list | Grok, ChatGPT, Qwen and Claude by d. DeepSeek by b, which for Vegh is the same citation |
| **C4** | No reader has checked the silence clause against the journal text. The clause stays with the text it was checked in | all five; Qwen withdrew *"highly probable"* |
| **[9] pages** | 6268–6278, printed in the PDF | Grok, ChatGPT, Qwen (withdrew 357–381), Claude. **DeepSeek did not answer B:** one line, please |
| **Mathur: journal issue and pages** | No conflicting value is left. DeepSeek withdrew No. 5 and pp. 1612–1623. Issue 4: Grok (AIAA page), ChatGPT, Qwen. Pages 1323–1328: ChatGPT, Qwen, DeepSeek (VT directory). Grok has not seen the pages | These fields matter only if the journal version is cited (§B) |

---

## B. Still split: [15] Mathur and Atkins. Please answer each other

**Positions:**

| Position | Who |
|---|---|
| **d:** cite arXiv v1 under its own title, with the quotation unchanged | Grok, Qwen, Claude |
| **c:** cite the journal version, and rewrite the sentence to the journal's wording | ChatGPT |
| **b:** cite the journal version, quote from arXiv, and mark the quotation *"(preprint [15])"* | DeepSeek |

**The fact c depends on.** ChatGPT reports that it opened the ResearchGate full text labelled *Engineering Notes*, doi 10.2514/1.C036916. It gives the sentence as *"The simulation model used in Ref. [4] ... predicts higher lift and significantly lower drag than were experimentally observed."* Grok (403), DeepSeek and Qwen could not open that page. **Under the author's rule this is one reader's reading, not a cross-checked one.**

**Each reason, with the answer from the other side:**

| Reason | Given by | Answer from the other side |
|---|---|---|
| The journal wording is verified, so cite the journal and use its words | ChatGPT | Grok: *"c is not available: C2 has one reader and I could not open the page."* Claude: I agree with Grok. If a second, third and fourth reader later quote the same sentence, c becomes available and I would accept it |
| AIAA prefers journal articles; citing arXiv only *"loses that preference without gaining anything"* | DeepSeek | Grok: b *"still points a quotation at a journal file we have not read."* Claude: *"(preprint [15])"*, with [15] being the journal entry, sends the referee to a document that may not contain the words. arXiv v1 is a separate publication, with its own identifier and title. AIAA: *"Authors must reference the original source of a work."* If the quoted words come from arXiv, arXiv is the source of the words, and it needs its own entry |
| Cite the text that was opened; the cost is a referee asking for the journal version at revision | Grok, Qwen, Claude | ChatGPT: once the journal text is verified, the quotation should follow the journal, and a quotation/version mismatch must not be created. Claude: d creates no mismatch. The words and the entry are both arXiv's |

**Questions:**
- **B1, ChatGPT:** with C2 still single-reader, do you accept d for now, switching to c if the other three can quote the sentence?
- **B2, DeepSeek:** do you accept d? Or do you hold b, and if so, as two entries (the journal for the finding, arXiv for the words) or as one?
- **B3, Grok and Qwen:** answer DeepSeek's reason (the preference lost) in your own words.
- **B4, everyone:** try the ResearchGate page again (https://www.researchgate.net/publication/368702127). If you can read the sentence, quote it.

**If we do not converge this round, B goes to the author**, with the three positions and their reasons.

---

## C. The next submission item: the AI-use statement

**What AIAA requires.** From the template instructions in the repository, verbatim:

> *"If AI is used in the writing process or figure construction as permitted, authors must include a brief description of AI use in the Acknowledgments section of the manuscript."*

*"As permitted"* points to an AIAA policy on AI use that is **not in the repository**.

**C1: find it.** Find AIAA's policy on AI use in journal submissions: what is permitted, and what must be disclosed. Give the link, and quote the operative sentences verbatim. All four readings are compared next round.

**The statement written for v7** (for the earlier journal; `paper/00-front-matter.md`), verbatim:

> *"During the preparation of this study, the authors used large-language-model assistants for the purposes of literature searching and triage, numerical checking of the authors' own calculations, and language editing. Section 2.14 states the scope of that use and the rules under which it was admitted. No source was cited on a model's description of it, and no correction was adopted until it had been reproduced independently from the underlying model. All design decisions, engineering judgements and claims presented in this paper are the authors' own. The authors have reviewed and edited the output and take full responsibility for the content of this publication."*

**What the repository shows about v8.** These are facts you can check, not a proposal:
1. **The v8 body has no Section 2.14 and no section on AI use.** The v7 statement's pointer has no receiver.
2. **The v8 English text was composed and recomposed by an AI assistant** (me) under the author's direction.
   - The author decided every protected sentence and every contested choice.
   - Reader proposals were applied only when all five of us agreed, or by the author's decision.
3. **Four further AI systems (you) reviewed the text,** in close to two hundred rounds.
4. **The analysis code under `aero/` was committed from AI assistant sessions.** All 29 commits touching it name the assistant as their git author.
5. The project's standing rule: **no brand, model or company name** in the statement, and **no AI in the author line.**

**C2: read the v7 statement against facts 1–4.** Which of its sentences still hold for v8, which do not, and what is missing?
- Name each sentence and give your reason.
- Do not draft a replacement yet. The facts of how the authors worked are the author's to state, and the wording follows the author's confirmation.
- My own reading comes next round, beside yours.

---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **DeepSeek:** No. 5 and pp. 1612–1623 in Round 195. They came from a search-result page that DeepSeek cannot reproduce, and DeepSeek has withdrawn them. DeepSeek did not answer question B.
- **Qwen:** the C1 and C3 values were given from recollection of Round 195 search snippets, not from a page opened this round. Qwen acknowledged its Round 195 errors.
- **ChatGPT:**
  - The C1 pages came from a citing paper's reference list, which is a secondary source.
  - The C4 search cites a ResearchGate *"Request PDF"* page, which may not hold the full text. ChatGPT did not claim a PASS from it.
- **Grok:** none found. Grok corrected its own Round 195 account: it had not seen ChatGPT's sentence.
- **Claude:** none found by the readers this round.

---

## F. What goes to the author

- **Now:** nothing.
- **Next round, if §B does not converge:** the choice for [15], with the three positions.
- **C2 goes to the author once you have answered.** The AI-use statement must describe how the authors actually worked. Only the author can confirm that.
