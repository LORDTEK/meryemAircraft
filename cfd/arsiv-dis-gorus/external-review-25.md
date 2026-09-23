# Round 21 — the last round before deposit. Read it whole, then in parts.

**Nothing is public yet.** Version 6 is built and not deposited. After this
round it goes to Zenodo, and from Zenodo to *Drones*. This is the last reading
before either.

**A note on method, requested for this round.** Please do **part → whole →
part**. Read the sections that interest you; then read the paper as one object
and ask whether it holds together as a single argument; then go back to the
parts with whatever the whole told you. The last four rounds have been
part-only, and they have been very effective at catching numbers — three code
defects and two false findings came out of them. What no round has done yet is
ask whether the thing reads as one paper. That question is now the one that
matters, because the argument has been rebuilt twice since anyone last read it
end to end.

**Read this document alone.** You do not need the manuscript. Every number
below is cross-checked against `paper-v6.md`.

---

## 0. Credit where it is due

**Qwen has been the most detailed reader of the last three rounds, and it is not
close.** Round 19's mechanism objection — that Section 3.9's explanation of the
scale behaviour was arithmetically false — was the single most productive
sentence any of you has written. Nobody else checked the geometry. Chasing it
produced a code defect that had manufactured a physical finding all four of you
then flagged as a submission blocker.

Round 20 repeated the pattern: Qwen noticed that the dual-use statement still
said "near 1800 km" after the heavy range moved to 1 571. A trivial-looking
catch. Going to fix it exposed that **four mandatory declaration blocks were
missing from the built PDF entirely** — see Section 4.

Qwen also corrected DeepSeek on a point of direction that we had not checked
either, and was right. See Section 3.

This is said plainly because the others should know what a useful objection
looks like: *check an arithmetic claim the paper makes about itself, and if it
fails, do not accept the replacement without measuring it.*

---

## 1. The paper, in two hundred words

Hybrid VTOL aircraft pay for runway independence in cruise efficiency. The paper
treats that as *architectural* and builds an accounting framework: the penalty is
charged in three coupled currencies — **Bill 1**, hover hardware carried as dead
mass; **Bill 2**, its drag when exposed; **Bill 3**, continuous power sized by a
condition holding two percent of the flight. Every remedy surveyed reduces one by
raising another. Escape requires four things at once: the same hardware, in the
same orientation, doing the same job, with the hover peak from a buffer.

**Headline: architectural rankings belong to sizing contracts, not to
architectures.** Three contracts reported.

The case is an uncrewed tail-sitting blended-wing body — one coaxial nose pair for
both regimes, four counter-rotating pairs at the tips for attitude, no elevons, no
rudder, no tilt, no dedicated lift system — instantiated at 50 kg and 1000 kg and
carried far enough to show what instantiating the escape condition costs.

Not claimed: that the aircraft is flyable, or that any architecture is generally
superior.

---

## 2. Current numbers

| Quantity | Value |
|---|---|
| Zero-lift drag bracket, computed | 0.0285 – 0.0381 |
| Assumed C_D0 | 0.0248 — below both ends |
| Light design, cruise L/D | 10.82 – 8.80 |
| Light design, **range** | **1 173 – 1 442 km** |
| Heavy design, cruise L/D | 11.78 |
| Heavy design, **range** | **1 571 km** |
| Free-wheeling rotor drag, light / heavy | 0.0154 / 0.0051 |
| Heavy tip-pair figure of merit | 0.652 – 0.660, against 0.599 required |
| **Mass advantage over lift-plus-cruise** | **32 – 36 %** |
| Range vs B, fixed fuel fraction | B leads, +24 to +45 % |
| Range vs B, fixed take-off mass | A leads, −29 to −43 % |
| Range vs B, fixed fuel mass | sign changes inside the bracket |
| RANS/VLM ratio *K_L* | 0.796, converged over three meshes |
| Loading redistribution | 2.75° → 1.04° trim twist → **0.8 %** on range |
| Abstract | 195 words |
| References | 51, numbered 1–51, no gaps, none uncited |

---

## 3. What was done with Round 20

**All four of you withdrew the heavy tip-pair blocker.** Verified since: the wrong
figures never went public. `paper-v5.md`, the deposited version, contains no
0.547, no 0.0033, no 1 649, no 12.37. They existed only in the undeposited v6.

That settles a disagreement between you. **Grok and ChatGPT were right on the
facts** — nothing deposited, so do not autopsy the bug in the article. **Qwen's
premise was wrong** ("because the wrong figure was in a deposited version"). The
withdrawal paragraph is cut to two sentences; the clip error lives in the
repository README and the version note.

**Q1, the heavy label — you voted (c), (c), (c), (b).** Taken as (c), but every
one of you attached the same condition and it has been met: **the closure
condition now sits beside the table in §3.8, not sixty pages away.** Grok's
formulation was adopted almost verbatim. DeepSeek's and Qwen's point about the
difference being categorical is also now stated: the light design has an assumed
value, a break-even and 2.2 kg of margin; the heavy design has a break-even on an
unmeasured exponent and no assumed value at all. *Closes conditionally* and
*closure undetermined* are different statements and the paper now makes both.

**Q2 — Grok alone proposed splitting §3.9, and it was the sharpest idea of the
round.** Bill 2's scaling is computed: two blade-element solutions, solidity and
dynamic pressure, and it never touches the shell-mass exponent. It survives
whatever the heavy design is called. Bill 1's scaling *is* the unmeasured
exponent. One heading carrying both as equal was wrong. Split.

**Q3 — no relabel for the light design.** Qwen was right that its condition is
already in §3.7; the asymmetry was on the heavy side and is gone.

**Q4 — Qwen corrected DeepSeek and was right.**

| | A | B | A lighter by |
|---|---:|---:|---:|
| bracket, favourable (low drag) | 51.1 kg | 75.5 kg | **32.3 %** |
| bracket, adverse (high drag) | 53.9 kg | 83.9 kg | **35.7 %** |

The advantage is *larger* at the adverse end, because the lift-plus-cruise
layout's mass grows faster with drag than this one's. So the conservative single
figure is **32 %, at the favourable end** — not 36. DeepSeek had the ends
reversed. It is counterintuitive, so the paper now says it explicitly.

**Also done:** the 2.6° is no longer called a threshold but what it is, a unit
conversion; ChatGPT's caution about "converged" spilling from the integrated ratio
onto the near-tip discrepancy is applied; Grok's advice not to advertise the
internal check count in correspondence is taken.

**One correction to us, from ChatGPT:** our Round 20 document quoted blade
solidity twice — 0.0215 and 0.044 — without saying the first was the buggy value
and the second the corrected one. Both true, neither labelled. The manuscript
carries only the corrected values; the defect was in our briefing.

---

## 4. Fixing Qwen's small catch exposed a large one

The dual-use statement still read "computed range near 1800 km" after the heavy
range moved to 1 571. Going to change it, the statement turned out not to be in
the built PDF at all.

**The PDF builder emitted four of eight declaration blocks.**

| block | in source | in built PDF |
|---|---|---|
| Supplementary Materials | yes | **no** |
| Patents | yes | **no** |
| Author Contributions | yes | **no** |
| Dual-Use Research of Concern | yes | **no** |
| Acknowledgements, Conflicts, Data, Funding | yes | yes |

All four were written in the front-matter source and none was wired into
production. **This is precisely the defect Grok caught with Highlights two rounds
ago, recurring.** Two of the four are unconditionally mandatory for the target
journal — Author Contributions in CRediT form, and Patents, because a patent
application exists. All four are now emitted in the journal's own order, and a
missing block halts the build rather than warning.

**We record this because of what it says about the division of labour.** Twice now
the external reading has caught a *wrong sentence*, and chasing the wrong sentence
has found a *defect in the generator*. You read the output; we have to read the
machine. A small wrongness in the output is often the visible end of a large one
inside.

---

## 5. Bibliography check — done, and it is clean

The reference list entered by hand on the existing Zenodo record was compared
against the built PDF, entry by entry.

| check | result |
|---|---|
| entries in the deposited record | **51** |
| entries in the built PDF | **51**, numbered 1–51 |
| gaps or duplicate numbers | **none** |
| order | **identical, all 51 positions** |
| first author and title, position by position | **identical** |
| citations without a reference | **none** |
| references without a citation | **none** |
| bibliography changed between v5 and v6 | **no — byte-identical** |

So the deposited metadata is current and needs no edit for version 6. The only
substantive finding is the last row of the source check: **15 of the 51 references
are cited only in the supplement and never in the main body.** That is the one
point worth your opinion — **Q1 below.**

A table listing all 51 with a column showing body, supplement or both is in the
repository as `paper/bibliography-zenodo-compare.md`.

---

## 6. Open items, unchanged

1. **Trimmed geometry not solved.** The mesh generator takes stations as span,
   leading edge, chord and thickness — no twist field. All RANS is on the
   untwisted planform.
2. **Near-tip loading disagreement is real** and survives threefold refinement.
   Its effect on the three span integrals is bounded at about 2.5 %.
3. **Heavy design's structural closure undetermined** — now stated in §3.8.
4. **Transition pitching moment** blocked on measurement, not effort.
5. **Overall lift ratio runs opposite** to the published comparison cited.
   Reported, not reconciled.

---

## 7. What we want this round

**Q1 — Fifteen of fifty-one references are cited only in the supplement.** Is that
a problem for a journal whose reference list is expected to serve the article? The
options are to leave it, to move those references to a supplementary
bibliography, or to cite them in the body where the body already discusses the
material. We do not have a view and would like one.

**Q2 — the whole-document question, and the reason for this round.** The argument
has been rebuilt twice since anyone read it end to end: the framing moved from
aircraft-led to framework-led, and every cruise number moved onto a bracket.
**Does it still read as one paper?** Specifically: does the framework in Section 2
still connect to the case in Section 3 now that Section 3's numbers are ranges;
does Section 4 still discuss the paper that Section 3 became; and is there
anything in Section 1 that promises a result Section 5 no longer delivers?

**Q3 — is there a claim left that the paper cannot support?** Not a limitation
honestly stated — a claim. Two rounds ago the answer was the 42 % mass advantage
and it is gone. One round ago it was the heavy design's efficiency and that was a
code defect. If there is a third, this is the round to name it.

**Q4 — what will the first referee object to?** Name the single sentence or number
you would attack if you were assigned this paper and wanted to reject it. We would
rather hear it now.

**Q5 — anything at all before deposit.** Nothing is public. After this round it
is.

Answer from this document. If you want a number that is not here, say which one
rather than inferring it.
