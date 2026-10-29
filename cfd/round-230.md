# Round 230 — Where is v9 ready to be published, at the venue that does the authors the most credit?

**Readers:** all channels. This round opens a new stage: choosing the venue. This text was prepared by the Claude session that works in the repository. It states only facts with their basis. The Claude session's own view goes beside everyone's in the next round, under the standing rule.

**The author's question, in full:** *Where is this work, published as v9 on Zenodo (https://zenodo.org/records/23754355) and the product of a great deal of effort, ready to be published so that it brings the authors the most credit?*

---

## 1. What the work is (facts for the venue question)

**The record.** Zenodo v9 is a new version under the concept DOI 10.5281/zenodo.22144194; the version DOI is 10.5281/zenodo.23754355, resource type Publication / Preprint, licence CC BY 4.0.
- The Claude session could not open the record from its environment (the network proxy refused it, HTTP 403). The facts below come from the authors' upload notes for v9.
- Please open the record yourself and say if anything differs.

**Title (per the upload notes):** *meryemAircraft: A Blended-Wing-Body Tail-Sitter with Body-Fixed Coaxial Propulsors.*

**Files deposited:**
- the paper (preprint, without vitae);
- the supplement (Table S0 and Sections S1–S11);
- the LaTeX sources;
- the analysis code at a recorded commit of https://github.com/LORDTEK/meryemAircraft;
- the record of the blind re-implementation: frozen text with SHA-256, the pre-run declaration, the list of the 58 compared values with their status, prompt, scripts, outputs, and the diff of every change after the freeze;
- the additional checks.

**Abstract (as deposited):**

> Hybrid vertical-takeoff aircraft change between hover and cruise by carrying two propulsor sets or reorienting one. meryemAircraft, a 50 kg tail-sitting blended-wing body for a 13 kg payload, does neither: its fixed-pitch coaxial pairs keep one body-relative orientation while the whole airframe rotates, so it carries none of the mechanism classes a tilting architecture uses to change regime. It is priced in three costs of hover: carried hover mass, exposed cruise drag and continuous power sized to the hover peak. On a buffered series hybrid, the nose pair, which supplies hover and cruise thrust, incurs none of them; the attitude-control tip pairs and frames stay in the cruise flow, taking 50 to 80 percent of zero-lift drag across the drag sources examined. With the assumed frame drag the sizing loop closes at 52.3 to 57.5 kg, at an effective lift-to-drag ratio 13 to 51 percent above a published turboshaft quadrotor's; across those sources the envelope, not a confidence interval, is 50.7 to 66.1 kg and 699 to 1,401 km. The range margin of a lift-plus-cruise layout over this aircraft shifts by 67 to 77 percentage points across three sizing contracts, so the ranking depends on the contract. No store reported as built delivers the required specific power; hover heading authority, the transition and landing remain open.

**Nature of the work:**
- An analytical conceptual-design study of one configuration.
- No aircraft built, no flight test, no wind tunnel; computational methods only (vortex-lattice, blade-element momentum with NeuralFoil polars, a 3-DOF transition model, a sizing loop).
- The contribution is the architecture. The accounting and the sizing contracts are its instruments.
- 27 pages in `elsarticle` preprint format, with a separate supplement.
- One independent check of reproducibility: two blind re-implementations from the frozen text.

**The authors:**
- Three independent researchers with no institutional affiliation and no funding. The cost of publication therefore matters.
- The corresponding author is Meryem Gülmen.
- The authors hold Turkish patent application TR 2026/014570 (filed 26 August 2026) on the aircraft and the roll strip. The paper declares it.

**Submission history (all desk decisions; no reviewer has read the work):**

| Date | Venue | Outcome, as recorded |
|---|---|---|
| 2026-09-14 | *Drones* (MDPI) | Found out of scope and transferred to *Aerospace* without review. The *Drones* scope page, which was not read before submitting, asks that general theoretical aircraft-design papers be validated with experimental data from at least a laboratory-scale uncrewed platform. |
| 2026-09-15 | *Aerospace* (MDPI) | Desk-rejected the same day ("discipline, novelty and general significance"). The text then had a 35,827-word body. |
| 2026-10-02 → 10-14 | *Journal of Aircraft* (AIAA), Full Paper, v8 | Desk-rejected by the Associate Editor: *"The paper does not provide any developments that are of archival nature."* |

The present v9 is shorter and restructured around the architecture. It was prepared for *Aerospace Science and Technology* (Elsevier). The authors' notes mention an AST submission version with vitae and photographs. The author will say whether it has been submitted; please treat AST as a candidate like any other.

**Standing rules that bind any answer:**
- **The venue rule.** Before a venue is named as a target, its aims, scope and special requirements are read in full and compared with the paper item by item. *Drones* was submitted to without reading its scope page; that cost one rejection.
- **The source rule.** Any statement about a venue that could be wrong needs a link opened in this round, and the quoted sentence where the claim rests on one. This covers scope, preprint policy, AI policy, length limits, fees, indexing, quartile, impact factor and deadlines. A figure you did not open this round is not given. A hedged number is worse than none, because it enters the record as data.

---

## 2. Questions

**Q1. Venues.** Name up to five venues, journals or conferences, ranked by the credit they would bring the authors. Limit yourself to venues where v9, essentially as it stands (no experiment, no new research phase), has a realistic chance of being sent to review and accepted. For each, give:
- (a) the aims-and-scope page, with a link and the sentence that admits an analytical conceptual-design study of one configuration without experiments, or the sentence that excludes it;
- (b) the preprint policy, with a link and a quotation. v9 and its predecessors are public on Zenodo under CC BY 4.0;
- (c) the policy on generative-AI use, with a link and a quotation. AI tools were used for text, literature search, review and analysis code, and the paper says so;
- (d) the length or page limits, against v9's 27 pages and separate supplement;
- (e) the indexing and quartile or impact figure, with the source page and its year;
- (f) the publication cost for authors without funding: APC or a subscription route;
- (g) for conferences, the next deadline, with a link, and whether a conference paper can later be extended into a journal paper at the same publisher;
- (h) what in v9 would have to change for that venue (format, length, framing), without new research;
- (i) the desk-rejection risk in the light of the two recorded reasons: "experimental validation" and "no developments of archival nature". Say what in v9 now answers them, or does not.

**Q2. "Ready".** Is v9 ready for the venue you rank first? If not, name the single change that would most raise its chance of review without new research, and say why.

**Q3. Credit against acceptance.** Where the most prestigious venue and the most likely venue differ, which would you advise for these authors at this point, and why? Is there a sequence, for example a conference first and then a journal? If you propose one, give the venue rules that allow it, with links.

**Q4. Venues to avoid.** Name any venue a reader might propose that you would advise against for this paper, with the reason and a link: scope, predatory practice, preprint conflict, or AI policy.

**Q5. Open proposals,** each with its reason.

Each channel's answers go side by side to every channel next round. Answer each other's reasons by name there.

---

## 3. Answer format

Give your channel name first. Answer Q1 as one block per venue, (a)–(i), each with its link. Then answer Q2–Q5. Mark every item you did not open this round as "not opened", and give no number for it.

## 4. What goes to the author after this round

- The venues on which the channels converge, with each one's requirements as quoted, so that the author can decide.
- Where the channels diverge, the reasons side by side.
- Any requirement that would need a change to v9 before submission.
