# Round 27 — desk-rejected twice in 24 hours. A post-mortem, and a strategy question.

---

## 0. What this round is

**The manuscript you reviewed in Rounds 22–26 was submitted, and it was rejected
twice in twenty-four hours without ever reaching a reviewer.** This round is not a
request to re-read the paper. It is a request to help us read the *rejection*, and
to answer one question the author is asking directly:

> **Can this work reach a Q1 journal? If yes, by what route? If no, say so plainly.**

We want your judgement on the diagnosis, not consolation. If the honest answer is
that the work is not Q1 material, that is a useful answer and we would rather have
it now than after three more rejections.

**One thing we ask you to actually do** is in Section 6: act as the desk editor, on
a three-minute budget, using only the material reproduced in Section 5. That is the
decision we lost, and we would rather see it simulated than speculated about.

---

## 1. How to verify anything below

Repository: `https://github.com/LORDTEK/meryemAircraft`

| File | Raw URL (pinned to a commit, HTTP 200 checked today) | SHA-256 (first 12) |
|---|---|---|
| Submitted manuscript | `https://raw.githubusercontent.com/LORDTEK/meryemAircraft/e45d43c/makale/makale-v7.md` | `c5b0cd898d20` |
| Supplementary | `https://raw.githubusercontent.com/LORDTEK/meryemAircraft/e45d43c/makale/makale-v7-ek.md` | `36b0b82477af` |
| Submission log + post-mortem (Turkish) | `https://raw.githubusercontent.com/LORDTEK/meryemAircraft/b648148/makale/drones-gonderim.md` | — |

`makale-v7.md` is byte-identical to what you reviewed in Round 26 and to what was
submitted. It is also deposited at Zenodo, DOI `10.5281/zenodo.22745666`. **It has
not been edited since submission and will not be** — this repository has twice paid
the price of two different files sharing one name, so corrections go into a new
version number, never into a published one.

---

## 2. The paper, in five lines, for anyone joining now

An accounting framework for the cruise-efficiency penalty of hybrid VTOL aircraft,
charged in three coupled currencies — hover hardware carried through cruise, its drag
when exposed, and continuous power sized by a condition lasting two percent of the
flight — plus an uncrewed tail-sitting blended-wing body as the case that instantiates
the framework's escape condition.

**Three architectural claims, each against a different opponent:** runway independence
(against fixed-wing), wing-borne cruise efficiency (against multirotors), and **no
propulsor-reorientation mechanism** (against tilting layouts — the airframe rotates,
the propulsors do not). **One claim explicitly declined:** range against the other
hybrids, because the ranking reverses with the sizing contract. The paper also states
that the configuration **is not shown to be flyable** — the power budget needs 3.8
times the highest measured battery specific power.

Methods: blade-element momentum theory, vortex-lattice with a viscous section method,
RANS with a three-level grid study, and a closed sizing loop across three contracts
and two scales (50 kg and 1000 kg).

---

## 3. What happened, with dates

| When | What |
|---|---|
| **14 Sep 2026, 15:06** | Submitted to **Drones** (MDPI), Article. ID `drones-4595522`. Status "Pending review". |
| **15 Sep 2026** | **Drones**: out of scope. Not sent for review. Transferred to **Aerospace** (MDPI) under the alternative-journal option on the submission form. New ID `aerospace-4595522`. |
| **15 Sep 2026** | **Aerospace**: received the same day, **rejected the same day.** Not sent for review. |

**Drones, verbatim:**

> "Unfortunately, we are unable to process your manuscript further in Drones as it
> appears to be out of scope. Your manuscript has been transferred to Aerospace in
> accordance with your alternative journal selection at submission."

**Aerospace, verbatim:**

> "We regret to inform you that we will not be processing your submission further.
> Submissions sent for peer-review are selected based on discipline, novelty and
> general significance, in addition to the usual criteria for publication in scholarly
> journals. Therefore, our decision does not necessarily reflect the quality of your
> work."

Elapsed time from Drones submission to final rejection: **under 24 hours.** No
referee, no technical comment, no specific objection. Two form letters.

---

## 4. What was actually in front of the editor

Measured today from the submitted files, not quoted from memory:

| Quantity | Value |
|---|---|
| Main manuscript | **79 pages**, 35 969 words, 22 tables, 12 figures |
| Supplementary | **60 pages**, 32 393 words |
| Cover letter | 740 words, 2 pages |
| Authors | Three, all surname Gülmen, all listed **"Independent Researcher, Türkiye"**, no institutional affiliation |
| Title | *The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System* |

**139 pages were not read in one day.** That is the single fact this whole round
turns on. The decision was made on some subset of {title, abstract, keywords, page
count, cover letter, author block}. The rejection therefore carries **no information
about the physics, the sizing loop, the RANS study, or any claim you spent five
rounds testing.** Not in our favour, and not against us. It was not evaluated.

---

## 5. The material the decision was probably made on

Reproduced in full so you can judge it without fetching anything.

**Title:** The Architectural Cost of Hybrid VTOL: meryemAircraft, a Propeller-Driven
Tail-Sitting Blended-Wing-Body Without a Dedicated Lift System

**Keywords:** vertical take-off and landing; tail-sitter; blended wing body; uncrewed
aerial vehicle; series hybrid propulsion; cruise efficiency; aircraft configuration design

**Abstract (212 words by `wc -w`), as submitted:**

> Hybrid vertical take-off and landing (VTOL) aircraft pay for runway independence in
> cruise efficiency. That cost is architectural, charged in three coupled currencies —
> hover hardware carried through cruise, its drag when exposed, and continuous power
> sized by a two-percent-of-flight condition — each remedy reducing one by raising
> another. Escape requires one set of hardware serving both regimes in one orientation,
> with the hover peak from a buffer. Tilting architectures meet it by rotating their
> propulsors, at the cost of a pivot and a control problem. An uncrewed tail-sitting
> blended-wing body is proposed as an alternative route: the airframe rotates and the
> propulsors do not, so there is no pivot, nacelle actuator or variable-pitch hub. Pitch
> and yaw come from differential thrust; roll, which coaxial pairs cannot produce, comes
> from one moving strip. What is eliminated is the propulsor-reorientation mechanism, not
> every moving part. Architectural rankings belong to sizing contracts, not to
> architectures; three are reported, and the configuration holds a 32 to 36 percent mass
> advantage over a lift-plus-cruise layout under all three but loses range under equal
> fuel fractions, driven by the free-wheeling drag of its own attitude rotors. No range
> superiority is claimed. It is not shown to be flyable: the budget needs 3.8 times the
> highest measured battery specific power.

**From the cover letter, the scope section's closing paragraph — verbatim:**

> "We note that the closest literature to this work, and six of our references, appear
> in Aerospace. We are submitting to Drones rather than to Aerospace because the
> constraints that generate every result here — uncrewed operation, small scale, no
> runway, an operator who is not an airline — are the constraints of this journal's
> subject, not of aerospace generally."

---

## 6. What we ask you to do first

**Simulate the desk editor.** Give yourself three minutes and only Section 5. You are a
Drones section editor with forty submissions this week. Answer four things:

1. Reject, or send out for review?
2. If reject — what is the *first* thing that made you decide, and at what second?
3. Is "out of scope" a truthful description of your reason, or a polite formula?
4. Would a different title, abstract or cover letter have changed your answer? Rewrite
   whichever one you think was decisive.

Please answer this **before** reading Section 7, so that our interpretation does not
contaminate yours. Then tell us whether Section 7 matches what you found.

---

## 7. Our interpretation, offered for attack

Written by the AI assistant that prepared the submission. It includes its own errors
because they are part of the evidence.

**7.1 Two of the decisive inputs were self-inflicted, and both are documented.**

*The cover letter named the competing journal.* The paragraph quoted in Section 5 was
written to pre-empt the objection "why Drones and not Aerospace." The effect was to put
the transfer destination, in writing, in the first section a scope editor reads. Whether
it caused the transfer is unknowable; that it was written is not.

*Length was sent as-is on the assistant's recommendation.* The risk was identified before
submission, named in the checklist as "the editor may return it from the desk," and a
prepared rebuttal was written — the rebuttal being that the framework and the case that
falsifies it cannot be separated without leaving a framework with no test and a
configuration with no reason. That rebuttal may well be correct. It was never heard,
because **a manuscript returned from the desk does not get to argue.** A defence that
cannot be delivered does not exist in practice.

**7.2 An error made after the rejection, corrected by the author.**

The assistant's first proposal was to split the paper in two — framework and case — on
the grounds that two journal-sized papers pass the desk more easily than one 79-page one.
The author's objection was immediate and correct:

> "Does splitting it get us closer to Q1? The more comprehensive thing isn't Q1, but cut
> in half it becomes Q1?"

He is right, and the error is worth naming precisely because it is the kind you may be
about to make too. **Splitting changes the probability of being read. It does not change
quality, novelty or significance, which is what journal tier is supposed to track.** The
assistant answered a "how do we not get desk-rejected" question with a proposal, and
presented it as though it answered "how do we reach a better journal." Those are different
questions and conflating them was sloppy.

So the real question is the author's, and it is open: **is there a route from here to Q1,
and does it run through making the work different, or only through presenting it
differently?**

**7.3 Candidate diagnoses. We think more than one is true; we do not know the weights.**

- **A — Format mismatch, not quality.** 139 pages is not an "Article" in any journal whose
  Article format is 8–12 000 words. It may be a **Review**, a monograph, a thesis chapter,
  or two papers. If this is the whole story, the work is fine and the container was wrong.
- **B — No validation.** There is no prototype, no flight test, no closed-loop transition
  simulation. Everything is analytical plus RANS. The paper says so honestly, including
  that the design is not shown to be flyable. **Is honest non-flyability publishable, or
  is it the thing that ends the conversation?** We think this is the strongest candidate
  and the least comfortable one.
- **C — Credibility signalling.** Three authors sharing a surname, all "Independent
  Researcher, Türkiye", no institution. We have no evidence this was weighed. We would be
  naive to assume it was not.
- **D — The title.** It carries a project name, *meryemAircraft*. To an editor skimming,
  a named aircraft in a title can read as a product announcement rather than a
  contribution.
- **E — Genuinely out of scope.** The contribution is aircraft-design accounting,
  illustrated on a UAV. Perhaps Drones was simply right.

---

## 8. The questions

Answer the ones you can judge. Say "I don't know" where you cannot — a confident guess is
worse than a gap, and we will be comparing four sets of answers against each other.

1. **Diagnosis.** Rank A–E by how much each contributed. Add anything we missed. Which is
   the *binding* constraint — the one that, unfixed, guarantees the next rejection?
2. **Q1, directly.** Is a Q1 venue reachable for this work? Under what conditions? If it
   requires something we do not have — hardware, a flight test, an institution, a
   co-author with a track record — say which, and say whether it is the *only* route.
3. **Does the split help or hurt?** Take the author's objection seriously and answer it on
   its merits. Two papers, one shortened paper, or the 139 pages intact in a venue that
   accepts that length?
4. **Venue.** Name specific journals, with quartiles as you understand them, and say for
   each what would have to change. We are aware our own quartile knowledge may be stale —
   correct us. Include review journals and conference routes if you think they apply.
5. **Validation.** How far does a credible closed-loop transition simulation get us, in the
   absence of hardware? Is a sub-scale demonstrator the actual unlock, and is it worth the
   cost relative to another paper?
6. **The 3.8× power gap.** The paper discloses that the design is not shown to be flyable.
   Is this scientific integrity that a good editor rewards, or is it, to a desk editor, the
   sentence that ends the review? Should it be stated differently — same honesty, different
   placement?
7. **Cover letter and title.** If you rewrote them, show us. Short and specific beats
   general advice.
8. **Appeal.** We assume appealing an MDPI desk rejection is not worth the time. Correct us
   if you disagree.

---

## 9. What we will not do

- We will not edit v7. It is published and fingerprinted; corrections become v8.
- We will not quietly drop the disclosure that the design is not shown to be flyable, or
  the declined range claim. If honesty costs us a venue, we pay it.
- We will not claim mechanical simplicity as a reliability result. The third claim is a
  **count** of eliminated mechanism classes, not a measurement of part count, mass, failure
  modes or maintenance. None of those were measured.

---

## 10. Where the previous rounds stand

Rounds 22–26 found four real defects, three of them in text the assistant wrote while
*summarising* the paper, each contradicting a section of the paper itself: a claim of "no
general architectural superiority" that denied the paper's own two earned claims; "no
mechanism that moves", contradicted by the roll strip of §2.10; "the strip produces no
pitching moment", contradicted by the same section's ΔC_m of 0.005–0.032; and a claim that
sea level was "the conservative choice", which the paper's own range equation does not
support. All four were corrected before submission and are recorded, with attribution to
whoever caught them, in the repository.

Two items were found after submission and are still open, waiting for v8: a **missing
reference** — Bacchini, Cestino, Magill & Verstraete, *Impact of lift propeller drag on the
performance of eVTOL lift+cruise aircraft*, Aerospace Science and Technology 2021, 109,
106429, which is a wind-tunnel measurement of precisely our largest ledger entry and is
absent from a bibliography that leans on the same group's other data — and a duplicated
sentence in §1.4.

Neither of these was the reason for the rejection. Nothing was the reason we can point to.
That is exactly the problem we are asking you to help with.
