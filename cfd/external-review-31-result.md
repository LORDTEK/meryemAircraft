# Round 27 — what the four readings said, and what I verified

Four independent readings of `external-review-31.md`. Each was asked to simulate the desk
editor **before** reading our own diagnosis. This file records the result, the one
new fact the round produced, and the audit of every number they put in our mouth.

---

## 1. The desk-editor experiment: 4 / 4 reject

| Reader | Verdict | Decided at | What it saw first |
|---|---|---|---|
| A | Reject | 30–60 s | Scale of the package, then the title |
| B | Reject | ~20 s | The cover letter's closing paragraph |
| C | Reject | 5–10 s | Page count; then the author block at 30–45 s |
| D | Reject | ~105 s | Dashboard page count + author block at 0:00 |

No reader sent it out. Three of four named the page count as the first trigger; the
fourth named the cover letter. All four named, in some order, the same four items:
**length, title, cover letter, and the abstract's closing sentence.**

---

## 2. The finding that changes the diagnosis — verified independently of the readers

Two readers said the *Drones* aims-and-scope page carries a written clause about
theoretical aircraft-design papers. **I checked it rather than repeating it.** The
clause exists:

> "If the manuscript is dealing with general theoretical aircraft design, it is
> recommended to validate the theoretical/numerical results with experimental data
> from a study of an unmanned platform, **at least at a laboratory scale**."

and alongside it:

> "The manuscript submitted must clearly and directly address topics related to
> unmanned platforms."

**Consequence.** "Out of scope" was probably not a polite formula. Our manuscript is
general theoretical aircraft design, it carries no experimental data of any kind, and
it says so in its own abstract. We failed a published, checkable requirement of the
journal we chose.

**This is my fourth error of the submission, and the largest.** The checklist in
`drones-submission.md` walked nine sections of the submission form and never once
compared the manuscript against the journal's own stated requirements. Everything
that was checked was checked well — numbers, links, figure order, word counts — and
the one thing that decided the outcome was never opened.

Rule for v8, and it is mechanical: **before naming a target journal, read that
journal's aims, scope and special requirements in full, and write down, requirement
by requirement, whether this manuscript meets it.** A verification suite that audits
the manuscript against itself but never against the venue is auditing the wrong thing.

---

## 3. Where all four agreed

- **Reject as submitted.** Unanimous, and none of them needed more than two minutes.
- **Diagnosis A — format/length — is first or joint-first.** Unanimous.
- **Diagnosis E — genuinely out of scope, in the sense of "this is not about unmanned
  aircraft" — is false.** Unanimous. The topic belongs; the package did not.
- **Do not send 139 pages anywhere.** Unanimous, with no dissent on any variant.
- **Drop the project name from the title.** Unanimous.
- **Never name another journal in a cover letter.** Unanimous.
- **Keep the 3.8× disclosure. Move it.** Unanimous — out of the abstract's closing
  position, into results/limitations, reframed as a quantified technology gap the
  framework isolated rather than as a confession that the design fails.
- **Do not appeal.** Unanimous.
- **Q1 is reachable, but not as v7.** Unanimous. Not one reader said the work is
  below Q1; all four said the container is wrong.

---

## 4. Where they split — and the author's objection

The author's objection to the split proposal was put to all four verbatim:

> "Does splitting it get us closer to Q1? The more comprehensive thing isn't Q1, but
> cut in half it becomes Q1?"

- **Two readers sided with the author** and argued against splitting. The sharpest
  version: split only if each half has its own question, and here neither does — the
  framework without the case is an essay, the case without the bills is another
  unbuilt tail-sitter. Their remedy is one paper cut hard, roughly 10–16 000 words,
  with the present supplement doing the work of a supplement.
- **Two readers recommended splitting** — but both explicitly conceded the author's
  point first. One stated plainly that splitting changes the probability of being
  read and nothing else, and recommended it anyway because the current format
  guarantees rejection. The other reframed it as quality versus form factor.

**So the objection was not refuted.** Three of four accepted it outright; the fourth
answered a different question. What all four agree on is the operative act — the 139
pages must come down — and they differ only on whether the reduction is achieved by
cutting or by dividing. That is a smaller disagreement than it first appears.

---

## 5. Validation — the useful convergence

- A closed-loop 6-DOF transition simulation moves the work from kinematic estimate to
  dynamic feasibility, and closes the "purely speculative" objection. **It does not
  satisfy the laboratory-scale clause quoted above** — that clause asks for
  experimental data, and another simulation is not experimental data.
- The framework contribution **needs no hardware at all**.
- The configuration contribution does. The cheapest unlock named is not a flying
  demonstrator but **one measured quantity on an unmanned article** — the strip's
  ΔC_L in a small tunnel, or free-wheeling versus stopped-rotor drag on a sting. A
  sub-scale flying demonstrator is stronger and far more expensive.

---

## 6. Audit of what the readers put in our mouth

Nothing is passed on from a reading without being checked against the manuscript.

| Claim in a reader's suggested text | Verdict |
|---|---|
| "requires a battery specific power of 5.63 kW/kg" | **Correct.** 5.63 kW kg⁻¹ appears throughout §3 and the supplement. Not invented. |
| "at the measured rate take-off mass rises 38 %" | **Correct.** The Highlights say the budget "re-closes 38 percent heavier at that measured rate". |
| "validated against NASA sizing data" | **Overstated but grounded.** A NASA sizing set of four VTOL architectures is used, and §3 calls it "a direct test of" the framework. *Tested against* is accurate; *validated against* is stronger than the paper claims. Do not adopt the stronger wording. |
| Journal quartiles | **Conflicting between readers** and between databases. Verify per database and category before targeting anything. |

**No fabricated numbers this round.** In earlier rounds there were some; this time the
readers stayed inside the manuscript. The one wording to reject is "validated".

### Quartile, checked

*Drones* is **CiteScore Q1 in Aerospace Engineering**; its JCR placement is in Remote
Sensing, reported as Q1/Q2 depending on the source and year. So the journal that desk-
rejected us **was already a Q1 venue by the aerospace measure.** We did not lose on
tier ambition. We lost on a scope clause we never read, with a manuscript three times
the length the format takes.

---

## 7. One reader's point worth keeping for v8

The missing Bacchini 2021 wind-tunnel reference should not be added as a bibliography
line. It measures precisely what our second bill predicts, so it belongs in the
discussion as corroboration of the framework — a paragraph, not a citation. That turns
the round's most serious omission into the framework's only external experimental
support, which is exactly what the venue clause asks for and we do not otherwise have.
