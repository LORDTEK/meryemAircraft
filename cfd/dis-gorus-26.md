# Round 22 — deposited once, corrected since. Read it whole, then in parts.

**Status.** Version 6 was deposited on Zenodo after Round 21. It is public. It
is also **already out of date**, because the week since has produced one
correction that came from the author, one from an external reading, and five
that came out of chasing those two. A corrected version will replace it before
the paper goes to *Drones*. That is what this round is for.

**You have one file: `makale-v6.md`, the main text, 32 300 words.** You do not
have the supplementary document (six files, 32 400 words), you do not have the
figures, and you do not have the code. The main text carries **figure citations
but no figure captions**, and it carries **all 22 table captions**. Where
something below depends on a figure you cannot see, the figure is described.

**Method, again: part → whole → part.** Read what interests you; then read the
paper as one object and ask whether it holds together; then go back. Round 21
was the first round anyone read it end to end. This is the second, and the
argument has been touched in four places since.

---

## 0. The most important catch of this round was not made by any of you

It was made by the author, and it was made against me.

While tightening the Introduction after Round 21, I inserted the sentence
*"No claim of general architectural superiority is made."* I meant it as
scope discipline. The author read it and objected, in substance: *we have an
architectural superiority claim — that is the whole reason this configuration
exists. It needs no runway, and it goes far beyond a multirotor.*

**He was right and I was wrong, and the error was not small.** My sentence
denied the two claims the paper actually earns while trying to disclaim a third
it never made. Worse, it contradicted Section 4.2 of the same document, which
argues a range band against multirotors.

The passage now separates three claims by status:

1. **Escapes the runway requirement** — sound, true by construction.
2. **Retains a cruising wing, and therefore a range, that no multirotor has** —
   sound, and carried by the paper's own cited data: a turboshaft quadrotor at
   an effective L/D of **4.9**, against this configuration's **8.8 to 10.8**
   across its computed drag bracket.
3. **A ranking against the other hybrid architectures** — *not* claimed,
   because Section 3.6 shows it reverses with the sizing contract.

**Please attack this passage** (Introduction, "Two architectural claims are
made and a third is not"). It is the newest load-bearing text in the paper and
it has had one reading. Specifically: is claim 2 defensible on a *cited* L/D of
4.9 versus a *computed* 8.8–10.8? Those are not the same kind of number. Say so
if you think the comparison is unfair.

**Why this is told at length.** A model that over-corrects a paper into denying
its own thesis is a failure mode worth naming, and it is one none of the four of
you caught in three rounds of reading the same Introduction.

---

## 1. The paper, in two hundred words

Hybrid VTOL aircraft pay for runway independence in cruise efficiency. The paper
treats that as *architectural* and builds an accounting framework: the penalty is
charged in three coupled currencies — **Bill 1**, hover hardware carried as dead
mass; **Bill 2**, its drag when exposed; **Bill 3**, continuous power sized by a
condition holding some two percent of the flight. Every remedy surveyed reduces
one by raising another. Escape requires four things at once: the same hardware,
in the same orientation, doing the same job, with the hover peak from a buffer.

**Headline: architectural rankings belong to sizing contracts, not to
architectures.** Three contracts are reported and the ranking reverses between
them.

The case is an uncrewed tail-sitting blended-wing body — one coaxial nose pair
for both regimes, four counter-rotating pairs at the tips for attitude, no
elevons, no rudder, no tilt, no dedicated lift system — instantiated at 50 kg and
1000 kg and carried far enough to show what instantiating the escape condition
costs. What it costs, principally, is the free-wheeling drag of its own attitude
rotors: a bill the configuration was assumed to avoid, and charging it reverses
one of the three range comparisons.

Not claimed: that the aircraft is flyable, or that any architecture is generally
superior to any other.

---

## 2. Current numbers, as the deposited and corrected versions both stand

| Quantity | Light | Heavy |
|---|---:|---:|
| MTOW | 50 kg | 1000 kg |
| Span | 3.45 m | 11.55 m |
| Wing area | 1.98 m² | 22.24 m² |
| Disc loading | 44.2 kg m⁻² | 43.7 kg m⁻² |
| Cruise speed | 30 m s⁻¹ | 40 m s⁻¹ |
| Cruise L/D, published assumption | 12.0 | 13.6 |
| Cruise L/D, rotors charged | 8.49 | 11.78 |
| Hover power | 10.9 kW | 216.2 kW |
| Range, rotors charged | — | 1 571 km |

| Contested quantity | Value |
|---|---|
| Zero-lift drag, assumed | 0.0248 |
| Zero-lift drag, computed bracket | 0.0285 – 0.0381 (the assumption is **below both ends**) |
| Free-wheeling ΔC_D0, eight tip discs, light | 0.0154 – 0.0423 |
| Mass advantage over lift-plus-cruise | 32 – 36 % (was quoted 37 %, on two different drag bases) |
| RANS/VLM loading ratio K_L | 0.796, converged over three meshes |
| Available T/W during rotation | 1.066 light, 1.041 heavy (1.132 / 1.082 with no rotation authority retained) |

---

## 3. What was done with Round 21, and what it turned into

Round 21 produced one external finding of consequence, from the reading of the
**Word/MDPI submission file**: *the figures appear out of order — Figure 12 is
printed before Figure 3.*

That was correct. Verifying it produced four things worth reporting.

**(a) It was worse than reported.** The actual caption order was
`1, 2, 12, 3, 4, 5, 6, 7, 8, 11, 9, 10`. **Figure 11 was also out of place** and
nobody had said so.

**(b) The defect was not where it was assumed to be.** The converter places each
figure after the paragraph that first cites it, and it does that correctly. The
fault was in the **manuscript's citation order** — the text cited Figure 12 in
Section 2.3 and Figure 3 in Section 2.5. Fixing the converter would have fixed
nothing. All twelve are now renumbered by first mention, and the renumbering was
carried through the figure files and the scripts that draw them so that names
and numbers cannot drift apart again.

**(c) Chasing it exposed a figure that contradicted its own section.** Figure 12
plots transition altitude loss against rotation time at thrust-to-weight ratios
of **1.1, 1.2, 1.3 and 1.5**. Section 3.15, one paragraph above it, says: *"An
earlier version of this section assumed T/W = 1.2, which the installed power does
not supply at any setting."* The tables in that section had been recomputed at
the ratios the aircraft actually has. **The figure had not.** It is now drawn at
1.066 and 1.132 (light) and 1.041 and 1.082 (heavy) — the two ratios each
design's own installed power supplies, with and without rotation authority held
in reserve.

**This is the second time in this project that a corrected number left a stale
twin somewhere else in the document.** The first was the drag bracket, which was
found in three places including a supplementary section whose prose contradicted
its own table. If you look for nothing else, look for this pattern.

**(d) Four other defects came out of the same pass**, none of them reported by
anyone:

- **Raw LaTeX in four places.** `$$\Delta C_{D0} \propto \sigma R^2/(qS)$$` in
  the main text and three blocks in the supplementary were passing through both
  the PDF and the Word converters **unrendered** — printing as literal source. In
  the file you have, these are now plain indented Unicode equations, matching the
  convention the rest of the paper already used.
- **Highlights missing from the submission file.** The mandatory MDPI Highlights
  block was in the PDF and **absent from the `.docx`** — the one file that gets
  submitted. This is the second occurrence of exactly this failure: an earlier
  round found four mandatory declaration blocks missing from the built PDF.
- **A hard-coded list went stale the moment numbers moved.** The PDF builder
  held `GENIS = {"2","9"}` — "figures 2 and 9 are too wide for portrait, print
  them full-page landscape." After renumbering, Figure 9 is no longer the flight
  profile (aspect 2.06) but the roll strip (aspect 1.21), and a figure that
  should be portrait was being printed sideways. The list is gone; the builder
  now measures the aspect ratio of the file.
- **Twenty-two tables, two captions.** Only "Table 1" and "Table 4" existed, both
  survivors of an older four-chapter numbering; Tables 2 and 3 never existed at
  all. All 22 are now numbered, captioned and cited in the text. **You can see
  all 22 captions in the file you have — please read them as a set.** They were
  written in one pass and have had no external reading.

---

## 4. What we are not claiming to have fixed

**The open items are unchanged and none of them closed this round:**

1. **The battery buffer.** The 50 kg design's budget needs a specific power
   about **3.8 times** the highest rate yet measured on a production cell. The
   paper says so. The aircraft is not shown to be flyable and the paper does not
   claim it is.
2. **The transition rests on a pitching-moment coefficient no current method
   predicts reliably.** With zero aerodynamic pitching moment the light design
   loses 5.4 m where the kinematic model reports zero. With a borrowed moment the
   spread is wide enough that no number from it is reportable — some models
   complete the rotation, some saturate, some tumble. That spread is stated as
   the finding.
3. **The take-off margin and the attitude authority are drawn from the same four
   propellers and cannot both be had in full.** Recorded as an open item.
4. **No wind tunnel, no flight test.** Two quantities are computed rather than
   assumed (three-dimensional zero-lift drag; station-by-station span
   efficiency); everything else is analytical estimate from stated assumptions.

---

## 5. What we want from this round

Ranked. Answer what you can; say which you skipped.

**1. The whole-object question, again, and harder.** The paper has been
rebuilt in Sections 3.3, 3.6, 3.15 and now the Introduction. Read it end to end
and tell us whether it still reads as **one argument** or as a sound argument
with four repairs bolted on. Be specific about where the seam shows.

**2. The Introduction's three-claim passage** (Section 0 above). Is claim 2
fair? Is the distinction between claims 2 and 3 one a reviewer will accept, or
will it read as having it both ways — "we are superior to multirotors but
decline to be ranked against our actual competitors"?

**3. The table captions, as a set.** Twenty-two of them, written in one pass.
Are any of them describing a different table from the one beneath it? Are any
making a claim the table does not support?

**4. Hunt for stale twins.** Twice now a corrected number has left an
uncorrected copy elsewhere. The corrections since deposit are: the L/D bracket
8.8–10.8; the mass advantage 32–36 %; T/W 1.066/1.041; heavy range 1 571 km;
K_L 0.796. **Search the file for older values of these and tell us where they
survive.** This is the single most useful mechanical thing you can do.

**5. Is depositing a corrected version the right call?** Version 6 is public and
citable. The changes since are: one substantive text correction (the three-claim
passage), one precision correction in Section 4.2, figure and table numbering
throughout, and four production defects. Our reading is that the first alone
justifies a new version, because the deposited text currently denies a claim the
same document argues. Disagree if you think that overstates it.

**6. Anything the four of you have collectively missed for twenty-two rounds.**
Asked seriously. The author caught this round's most important error. That is a
result about the reading, not about the author.

---

## 6. A note on how to be useful here

The most productive objections in this project have all had the same shape:
**check an arithmetic or internal-consistency claim the paper makes about
itself, and if it fails, do not accept the replacement without measuring it.**

Round 19's best objection was that a section's *explanation* of its own scale
behaviour was arithmetically false. It was. Chasing it found a code defect that
had manufactured a physical finding all four readers had flagged as a submission
blocker — the finding was withdrawn.

Round 21's best objection was that figures printed out of order. They did.
Chasing it found a figure that contradicted the paragraph above it.

Small catches have been worth more than large opinions, every single round.
