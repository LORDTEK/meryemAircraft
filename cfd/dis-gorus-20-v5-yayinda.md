# Round 15 — v5 is out. Two ways in, and one question I actually need answered.

Last round four of you read the paper independently. Three findings were real and
changed a number; one confident claim turned out to be about a file its author had
not opened. Both outcomes are in Section 3 below, named, because a review process
that only records its hits is not a review process.

The paper has since been restructured and released. This is what changed, how to
read it, and what I am asking for.

---

## 1. How to read it — pick whichever your tools allow

**If you can browse.** The repository is public and always current:

```
https://raw.githubusercontent.com/LORDTEK/meryemAircraft/main/makale/makale-v5.md
https://raw.githubusercontent.com/LORDTEK/meryemAircraft/main/makale/makale-v5-ek.md
```

Plain Markdown. The first is the paper, the second is the six supplementary files in
one document. Two more worth opening if you have room: `aero/README.md` is the running
correction record, and `aero/itki.py` is the thrust-budget script behind Section 2.

**If you prefer a citable archive.** The work is deposited with a DOI that always
resolves to the most recent version:

```
[ZENODO-KOK-DOI]
```

That is the all-versions DOI deliberately, so that this link does not go stale the next
time the paper is revised. It carries the article as a PDF with all twelve figures, the
supplementary material as a second PDF, and both as Markdown — because in the last round
one of you could not open a PDF and another could not fetch a URL at all, and both said
so, which was the right answer.

**If you can do neither, say so at the top of your reply.** Last round one reviewer
reported on the contents of a file it had not retrieved, and told me my build pipeline
was broken on the strength of it. That cost me the twenty minutes it took to disprove.
"I cannot read the current version, so here is what I can check from what I have" is a
better answer and I will use it.

### Before you read a word of it: check that it is the current version

This matters on either route. The archive lists every earlier deposit in a sidebar, and
the repository carries three hundred commits of history behind the current file.
**Earlier versions contain errors this one has corrected** — a comparative table that was the wrong table, a
thrust-to-weight ratio the installed power does not supply, a battery figure taken across
three different stations. Reviewing one of those and reporting it back to me costs us
both a round, and it has already happened once.

**You want Version 5, dated 12 September 2026.** Three things in the text itself will
tell you, without trusting any label:

| | current | superseded |
|---|---|---|
| numbered sections | **five**, the second *Materials and Methods* | nine, the second *Background* |
| battery buffer requirement | **5.63 kW/kg** | 4.61 kW/kg |
| thrust-to-weight in transition | **1.066 – 1.132** | 1.2 |

If you see the right-hand column, stop and say so rather than reviewing it.

---

## 2. What changed since you last saw it

**The structure.** Nine sections became five: Introduction, Materials and Methods,
Results, Discussion, Conclusions. That is the section list the target journal requires,
and it was mandatory rather than stylistic. All forty-one subsections survive; no
paragraph was deleted. The renumbering was machine-checked — roughly one hundred and
eighty cross-references remapped in one pass, then every one verified against a
surviving heading.

**Four numbers moved.**

- The comparative sizing table in the body was the wrong table — an external comparison
  of three flying eVTOLs with the column headers altered. Three of you caught it. The
  paper's own three-architecture, three-contract result is now in its place.
- Hover power is thrust equal to weight, so the installed power buys T/W = 1.00 and no
  climb. The margin comes from the four attitude-control propellers: 1.066 with full
  rotation authority retained, 1.132 with none. Never the 1.2 previously assumed. The
  altitude-loss result survives at both reference rotation times and down to T/W = 1.00,
  but acquiring the entry climb costs 3.9 s and 9.6 m instead of 2.6 s and 6.4 m, and a
  rotation begun from rest is markedly worse than was reported.
- The battery buffer, taken at the bus rather than by differencing two shaft stations,
  asks **5.63 kW/kg to hover and 6.48 to leave the ground** — a factor of 3.8 over the
  highest rate measured on a flown pack, not the 3.1 implied before.
- The tip propellers are no longer described as producing attitude moments and nothing
  else, because they no longer do.

**One open source request closed, against us.** The tip-frame fairing is a symmetric
section at Re ≈ 80 000, toed one to two degrees, and its side force was computed from an
assumed lift-curve slope of 4 per radian. A compilation already in our own reference
list reports a measured deadband in the lift curve near zero incidence for symmetric
sections at exactly that Reynolds number — absent higher up, absent on cambered
sections. The assumption is an upper bound, not a conservative choice, because what the
measurements remove is the curve's linearity rather than the size of its slope. The
source names the remedy (camber the fairing) and the paper declines to resize it, since
picking a slope off a curve nobody has measured is the error being recorded.

**Front and back matter** now carry Highlights, Author Contributions, a Supplementary
Materials statement, a Patents statement, a dual-use note, and an abstract cut from 588
words to 220.

---

## 3. Last round, scored

Not to keep points. Because how you were wrong is information I can use.

**Real, and fixed:** the wrong comparative table; the thrust-to-weight contradiction;
the bus-versus-shaft buffer error; the misattributed citations; the drag build-up table
that did not sum to its own total; the rotation margin of 1.14 rather than 1.59; control
power going as the inverse cube rather than the inverse square of rotation time; range
containing propulsive efficiency after all; two sections claiming no experiment was
needed while the conclusion said otherwise; and — the sharpest catch of the round — the
paper still saying the tip propellers do nothing but produce moments, several pages
after establishing that they carry the take-off margin.

**Checked and did not hold.** A claim that the fixed-fuel-mass column was numerically
wrong: the paper is right, and the objection held take-off mass fixed while changing the
fuel rule, which is not a contract. A claim that the coaxial pair needed twice the disc
area: single disc plus interference is the standard treatment and the paper uses it. A
claim that the endurance arithmetic did not close: it closes to three figures once 1.7 kW
is read as the rounded value it is. A claim that our NASA figures were wrong and should
be replaced: opening the source showed our figures verbatim correct and only the citation
number wrong — the objection said three things were wrong and one was.

**And one that was about a file that had not been opened.** Three specific errors were
reported as still present in the repository, with a closing note that our build script
must not be pulling current versions. All three had been fixed and pushed; the raw file
disproves each in one request. I mention it because the instruction from the previous
round — *give me the sentence you are relying on, not just the citation* — applies to a
correction exactly as it applies to a claim.

---

## 4. What I am asking

**First: where is it wrong.** Not weak — wrong. Show the arithmetic if you are
correcting a number, so I can reproduce it. If you are relying on a source, quote the
sentence. If you cannot verify something, say which and why.

**Second, the one I most want answered: which calculation should we run next?**

Last round produced four different recommendations, and they do not agree. Rather than
ask again in the abstract, here they are — argue for one, or against one, or propose a
fifth:

1. **RANS against vortex-lattice on the trimmed planform**, comparing not just total lift
   but the spanwise loading ratio and the moment-to-lift ratio. Decides whether the
   paper's cancellation argument — that a common magnitude error drops out of ratios —
   is usable. Counts against us if the ratio moves the neutral point out of the
   packaging window or changes the trim washout by more than a degree.
2. **Blade-element/momentum on one tip pair at the cruise advance ratio and zero shaft
   torque.** Decides whether Bill 2 is actually absent, since that claim rests on two
   assumed coefficients thirty times apart. Counts against us if the zero-torque drag
   increment reaches 0.004, which is what we already charge for the frames.
3. **Re-close the light design at a measured pack**, running the sizing loop with the
   buffer at 1.5 kW/kg instead of 5.63 — buffer mass raises take-off mass, which raises
   hover power, which raises buffer mass. Decides whether "does not close" is a thin
   margin or a divergent loop. Counts against us if it settles with payload intact.
4. **Six-degree-of-freedom transition with several borrowed pitching-moment models**,
   run as a sensitivity rather than a prediction. Decides whether the point-mass
   altitude result survives rotational dynamics. Counts against us if any plausible model
   produces a failed rotation or control saturation.

Say **what** to compute, **what the answer decides**, and **what result counts against
us**. A calculation whose every outcome supports the paper is not worth the time.

Two things need a tunnel and I am not asking you to route around them: the transition
pitching moment above roughly ten degrees of incidence, and the side force on the faired
tip frame at Re ≈ 80 000.

**Third:** the paper is about 20 700 words with no journal length limit. If you think
that is wrong for the reader rather than for the rules, say so — but after the first two
questions, not instead of them.
