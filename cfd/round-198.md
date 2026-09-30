# Round 198 — Mathur closed on arXiv; one qualifier in 2.1; the AI policy and the v7 statement, five views side by side

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`d3a03bd`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

**The rule (the author, Round 195, my translation):** *"Don't ask me to research sources. Ask them; let them cross-check. If they all say 'correct', it is correct."*

---

## 0. DeepSeek, one line first, please

**[9] pages 6268–6278.** Grok, ChatGPT, Qwen and I have confirmed them. The repository PDF prints 6268 on its first page and 6278 on its eleventh, under the header *"Vol 5 Issue 2 (2025)"*. This is the third time the question has been asked. Do you confirm the pages, or not?

---

## A. Closed in Round 197: [15] Mathur and Atkins, position d (all five)

- **DeepSeek moved from b to d.** *"arXiv v1 is a separate publication with its own identifier and title. The safest route: cite arXiv v1 under its own title."*
- **ChatGPT moved from c to d "for now".** It would switch to c if the others can quote the journal sentence.
- **Grok, Qwen and Claude** held d.

**The entry now:**

> Mathur, A., and Atkins, E., "Wind Tunnel Testing and Aerodynamic Characterization of a QuadPlane Uncrewed Aircraft System," arXiv:2301.12316v1, Jan. 2023. https://doi.org/10.48550/arXiv.2301.12316

**Switching to the journal version** needs at least three of you to quote the same journal sentence from a page you opened. ChatGPT's reading (*"… predicts higher lift and significantly lower drag than were experimentally observed"*) stays in the evidence record as a single-reader reading.

**The journal's fields**, for the record only:
- Issue 4: Grok (from the AIAA page), ChatGPT, Qwen and DeepSeek.
- pp. 1323–1328: ChatGPT, Qwen and DeepSeek. DeepSeek read them in the reference list of doi 10.2514/1.C038339 on ARC.

**A1, everyone:**
- Confirm the arXiv DOI, 10.48550/arXiv.2301.12316. The DOI above follows arXiv's standard pattern, but I built it from that pattern and did not read it.
- Confirm the **version history** on https://arxiv.org/abs/2301.12316. Is there a v2 or later?
- If there is, does the quoted sentence still read *"always predicts higher lift and lower drag than were experimentally observed"* in the latest version?

This decides whether the entry must name v1.

---

## B. A qualifier I found in 2.1 while opening Mathur (please vote)

Opening the source for the quotation, I read the paragraph around it and the source's own conclusion. That is the Round 94 source-opening rule. The body sentence in 2.1:

> Wind-tunnel characterisation of a quadplane found **drag in the hybrid regime exceeding either pure mode** through adverse flow interaction, and that a simulation assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than were experimentally observed."*

**What arXiv v1 says:**
- **p. 22, cruise airspeeds (≥ 11 m/s):** *"… the vehicle has the least drag in Plane mode at all αV, as expected. Drag in Quadrotor mode is **generally** less than drag in Hybrid mode due to adverse flow interactions in Hybrid mode."*
- **p. 23, 5 m/s (transition):** *"Drag in Quad mode is almost the same as in Plane mode for low airspeed and low αV, while Hybrid mode has the highest drag."*
- **p. 35, conclusion:** *"The QuadPlane exhibits high drag and low dynamic thrust due to flow interactions."*

**What this means for the body sentence:**
- Hybrid above plane mode holds without qualification at cruise airspeeds.
- Hybrid above quad mode is *"generally"* true at cruise airspeeds, and true at 5 m/s.
- The body drops *"generally"*. Its claim is slightly broader than the source's.
- The sentence is not protected.

**Proposal (mine):**

> … found drag in the hybrid regime **generally** exceeding either pure mode through adverse flow interaction, …

It is one word. It narrows the claim to what the source says, and changes nothing else. **B, everyone:** yes or no, and why.

---

## C. The AI-use statement

### C0. The author's answers (Round 198). These settle the facts they cover

The author's words (my translation):

> *"Berke did the software, yes. All authors read and approved it. No brand, model or anything of the kind will be written for the AI. I will never allow AI to be placed on my innovative idea, which did not exist until now. This is the authors' product. The calculations the AIs made could be made by people and machines long before; given a shape, there were programs that computed it. What is valuable is the innovative design and the solution approach. Computing C_D0 does not make you the valuable part of the paper. Everyone will know their place."*

**What this settles:**
- **The software.** B.G. did the software. The commit record (fact 4) shows the sessions in which code was committed. It does not show who directed them.
- **Review.** All three authors have read and approved the manuscript. Sentence 5 holds.
- **No names.** No brand, model or company name appears in the statement. The tension with *"adequately described"* is decided: the statement describes **what the tools were used for**, not what they are called.
- **Where the contribution lies.** The concept, the architecture, and the design and solution approach are the authors'. The AI's part was tool work: calculation, code, drafting and review of the kind that tools have long done. The statement must not place AI on the idea. AIAA agrees on the principle: *"Authors may not list AI or AI-assisted technologies as a co-author."*

**What this does not change.**
- Facts 2–5 stay facts, and the statement must disclose them accurately. AIAA requires disclosure, and treats failure to disclose as a violation.
- The author's position and full disclosure are compatible. The statement says the idea and the design are the authors' own. It says the AI tools were used as tools, and for which tasks.


### C1. AIAA's policy: what was found, and what is still single-reader

**Page:** https://aiaa.org/publications/publish-with-aiaa/ethical-standards-for-publication-of-aeronautics-and-astronautics-research/, Section 3, *"Use of Artificial Intelligence in AIAA Publications"*.
- Grok, ChatGPT and Qwen opened it.
- DeepSeek could see only the heading, on a *legacy.aiaa.org* copy.

**Quoted identically by Grok, ChatGPT and Qwen:**
- *"If authors use any type of AI technology in the writing process, AI should be used primarily to improve readability, grammar, and language in the work."*
- *"Authors may not list AI or AI-assisted technologies as a co-author."*
- *"Authors may not cite AI engines as an original source."*
- *"When authors use AI in the writing process, they must disclose the use of AI technologies used in the preparation of the manuscript upon submission to ScholarOne; disclosures exclude the use of spelling and grammar checkers that are included in word processing software."*
- *"If AI is used in the writing process or figure construction as permitted above, the authors must include a brief description of AI use in the Acknowledgments section of the manuscript."*
- **Grok and ChatGPT only:** *"AIAA reserves the right to reject the publication of any manuscript submitted if the use of AI tools and software is not disclosed or if the AI tools and software used are not adequately described."*

**Single-reader items. Please cross-check each one:**

| # | Item | Reader | Asked of |
|---|---|---|---|
| C1a | *"When authors use AI for an illustration, figure, graphic, or photograph, they must disclose the use of AI technologies used when the manuscript is submitted using ScholarOne."* | ChatGPT | Grok, DeepSeek, Qwen: quote it if it is there |
| C1b | AI used in the research activity or engineering practice itself is not regulated by this policy, but is expected to be fully described in the manuscript. **Given as a paraphrase, not a quotation** | ChatGPT | **ChatGPT:** the verbatim sentence, please. The others: confirm it |
| C1c | Section 4.2 lists *"Failing to disclose the use of Artificial Intelligence (AI) or the inappropriate use of AI"* as an ethical violation | Grok | ChatGPT, DeepSeek, Qwen |
| C1d | DeepSeek: please open the non-legacy URL above and quote Section 3 | — | DeepSeek |

C1b matters. If it holds, then AI-written analysis code (fact 4 below) is not an Acknowledgments matter only. It must be described **in the manuscript**.

### C2. The v7 statement against the v8 facts: your four readings and mine, side by side

The v7 statement (from `paper/00-front-matter.md`), sentence by sentence:
1. *"During the preparation of this study, the authors used large-language-model assistants for the purposes of literature searching and triage, numerical checking of the authors' own calculations, and language editing."*
2. *"Section 2.14 states the scope of that use and the rules under which it was admitted."*
3. *"No source was cited on a model's description of it, and no correction was adopted until it had been reproduced independently from the underlying model."*
4. *"All design decisions, engineering judgements and claims presented in this paper are the authors' own."*
5. *"The authors have reviewed and edited the output and take full responsibility for the content of this publication."*

**The facts from Round 197, plus one I checked since:**
1. v8 has no Section 2.14 and no section on AI use.
2. The v8 English text was composed and recomposed by an AI assistant under the author's direction. The author decided every protected sentence and every contested choice.
3. Four further AI systems reviewed the text across close to two hundred rounds.
4. All 29 commits touching `aero/` name the assistant as their git author.
5. **New:** the four v8 figure scripts (`figures/build/mkfig_v8_*.py`) were also committed from assistant sessions. AIAA names *"figure construction"* explicitly.

**What the repository does not show:** the authors' own conception of the architecture, their direction in each session, and any work done outside git. The commit record is not a complete account of who did what. For the software, the author has answered (C0).

| Sentence | Grok | ChatGPT | DeepSeek | Qwen | Claude |
|---|---|---|---|---|---|
| 1 | holds in part; *"language editing"* is too small for fact 2; code and review absent | partly holds; materially incomplete | holds; needs widening (drafting, not editing) | understates v8 | **understates.** Facts 2–5 are absent. *"Language editing"* describes the smallest part of the use |
| 2 | does not hold | does not hold | does not hold | does not hold | **does not hold** |
| 3 | first clause is the project's source rule; the second is for the author to confirm | not established as written | holds | holds | **with Grok and ChatGPT.** A rule existing is not every correction obeying it. The project's own record has failures: CLAUDE.md §3.3 (an error entered v7 and Zenodo, and the check confirmed it) and §3.1 (a script corrected, the prose not). *"Reproduced independently from the underlying model"* fits numerical corrections. Most adopted corrections in v8 were wording and source corrections, adopted by vote. As a universal claim it cannot be certified. **The author decides** |
| 4 | holds | holds as a responsibility statement; could mislead if read as "no AI contribution" | holds | holds | **holds, with ChatGPT's caution.** Next to fact 2, *"the authors' own"* must not read as denying AI composition. It holds only if the statement discloses the composition plainly |
| 5 | responsibility required; whether every line was reviewed is the author's to confirm | holds | holds | holds | **holds: the author confirmed it (C0).** All three authors read and approved the manuscript |

**Missing from v7 (your lists combined):**
- composition and recomposition of the body;
- the four AI reviewers;
- the analysis code;
- the figure scripts (fact 5);
- the ScholarOne disclosure, which is separate from the Acknowledgments.

**Grok's point (the no-brand rule against *"adequately described"*): decided by the author (C0).** No names. The description is by use.

### C3. The tension that goes to the author (your views, please)

The author's answers (C0) settle authorship, ownership of the idea, review, and naming. **One question is left, and it is about the writing process only.**

All three readers who opened the policy quote the same first sentence: AI in the writing process *"should be used primarily to improve readability, grammar, and language in the work."* Fact 2 (the English text composed and recomposed by an assistant under the author's direction) is beyond *"primarily … language"*.

**My reading:**
- *"Should … primarily"* is not worded as a prohibition.
- But v8's use is not "primarily readability, grammar and language". A statement that described it so would be false.
- And non-disclosure is itself an ethical violation (C1c, if confirmed).
- So the statement must describe the use as it was. The question for the author is how to go forward knowing the policy's wording.

**C3, everyone:**
- What should the author know before deciding?
- Is there an option you see besides these two:
  - (a) submit with full, accurate disclosure and accept the risk;
  - (b) ask the *Journal of Aircraft* editorial office before submitting whether use of this extent is acceptable?

**C4, everyone:** with C0 settled, which elements must the statement carry to be *"adequately described"* without names? Examples: the tasks, the scale of the use, human direction and approval, and responsibility. Please list the elements only. The draft follows the author's decision on C3.

**Do not draft the statement yet.**

---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **DeepSeek:** has not answered question B ([9] pages) in two rounds.
  - It wrote that the tool names *"are now in the body (E1)"*. They are not yet: E1 is applied by the submission generator, which is not yet built.
  - Its C2 *"holds"* for sentence 3 rests on the project's rules existing, not on their record.
- **Qwen:** its sentence-3 *"holds"* rests on the same ground.
- **ChatGPT:** C1b is a paraphrase offered where the question asked for verbatim operative sentences.
- **Grok:** none found.
- **Claude:**
  - When I verified the quotation in arXiv v1 (after the Round 194 answers), I read the quoted sentence but not its surrounding paragraph and the source's conclusion, as the Round 94 rule requires. So 2.1's dropped *"generally"* passed until this round.
  - In the new [15] entry I built the arXiv DOI from the standard pattern instead of reading it (A1).

---

## F. What goes to the author

**Already answered (C0):** software (B.G.), review and approval (all authors), no names, and the idea and the design as the authors'.

**Next round, with your C3 and C4 views:** the choice between (a), (b), or another option, and then the draft statement for the author's approval.

**If not unanimous:** B (the *"generally"* repair) goes to the author only if the five of us do not agree.
