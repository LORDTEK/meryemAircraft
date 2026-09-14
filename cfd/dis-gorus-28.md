# Round 24 — probably the last. Read it whole, then in parts.

---

## 0. FIRST: how to check you have the right file, in ten seconds

**Two of you read a stale file last round and one of those has now done it twice.**
That was partly my fault: I recorded the mismatch as a finding that failed instead of
giving you any way to check. That was the wrong thing to do and it is fixed here.

**The attached `makale-v6.md` is:**

| | |
|---|---|
| SHA-256, first 12 hex | **776d5414c65c** |
| lines (`wc -l`) | **2 924** |
| words (`wc -w`) | **33 766** |
| git commit | **f511e8f** |

*(The word count depends on the tool: `wc -w` gives 33 766, Python's `str.split()`
gives 34 146, because the file uses thin spaces inside numbers like "1 571" and the
two tools disagree about whether those separate words. The SHA is the unambiguous
check.)*

**Three one-second checks. If any fails, you have an older build and should say so
before reviewing:**

1. Search for `0.0216` — must return **zero hits**. (Old drag bracket. Two rounds dead.)
2. Search for `Two architectural claims are made and a third is not` — must be **present**.
3. Count `**Table ` captions — must be **22**.

**The repository is public: `https://github.com/LORDTEK/meryemAircraft`.** The exact
build attached here is at commit `f511e8f`, path `makale/makale-v6.md`. Everything
else referenced below — the solver scripts, the two guards, the correction log in the
commit messages — is in the same tree. If you can fetch a URL, you can verify every
claim in this document yourself rather than taking my word for it. **I should have
given you this link five rounds ago.**

---

## 1. What happened last round, honestly, including who got it wrong

**Grok and DeepSeek read the correct build.** Both reported its word count correctly;
every finding they made checks out against the file.

**Qwen had the correct build and still produced three false findings.** It confirmed
six values that exist *only* in the corrected build — so the file was right — and then
led with *"the one clear stale twin left: both pointers still say Section 3.2,"* quoting
text. The string `Section 3.2` occurs **zero times** in that file; both read 3.1. It
also reported the sea-level paragraph and the reverse-transition statement as absent;
both are present. Its entire closing recommendation rests on the phantom pointer.

**ChatGPT read a stale file for the second consecutive round.** It reported 2 711 lines;
that build had 2 809 and this one has 2 924. Every one of its eight "still unfixed"
items is a feature of the two-rounds-old Zenodo deposit.

**None of this is said to score a point, and two things cut the other way:**

- **Qwen's phantom finding sat next to the single most useful suggestion of the round**
  — that every guard in this project checks whether a pointer *resolves*, not whether it
  resolves to the *right thing*. That observation was correct, it was general, and
  acting on it found four more real defects within the hour. See Section 3.
- **ChatGPT, reading the wrong file, still identified a real defect** — a sentence whose
  subject silently flipped — because that sentence existed in both builds. And its
  objection that calling C_D0 = 0.0248 "self-consistent" is indefensible was right.

**The lesson I take is about me, not about you:** when a reader's premise is wrong, the
useful response is to hand them the means to check, not to file a verdict. Section 0
exists because of that.

---

## 2. The paper, in two hundred words

Hybrid VTOL aircraft pay for runway independence in cruise efficiency. The paper treats
that as *architectural*: the penalty is charged in three coupled currencies — **Bill 1**,
hover hardware carried as dead mass; **Bill 2**, its drag when exposed; **Bill 3**,
continuous power sized by a condition holding some two percent of the flight. Every
remedy surveyed reduces one by raising another. Escape requires four things at once: the
same hardware, in the same orientation, doing the same job, with the hover peak from a
buffer.

**Headline: architectural rankings belong to sizing contracts, not to architectures.**
Three contracts are reported and the ranking reverses between them.

The case is an uncrewed tail-sitting blended-wing body — one coaxial nose pair for both
regimes, four counter-rotating pairs at the tips for attitude, no elevons, no rudder, no
tilt, no dedicated lift system — instantiated at 50 kg and 1000 kg and carried far enough
to show what instantiating the escape condition costs. What it costs, principally, is the
free-wheeling drag of its own attitude rotors: a bill the configuration was assumed to
avoid, and charging it reverses one of the three range comparisons.

Not claimed: that the aircraft is flyable, or that any architecture is generally superior.

---

## 3. Every Round 23 finding: claim, verdict, action

**Seven external findings held. All seven are applied. Four of them were damage I did
myself while applying the previous round's fixes** — that is worth stating plainly,
because it is the measurable cost of fast repair.

| # | Who | Claim | Verdict | Action |
|---|---|---|---|---|
| 1 | DeepSeek, Grok | §3.8's "between a third and a half" is arithmetically wrong | **Held.** 0.0035/0.0154 = 0.227 | Now "a quarter and a half," with both ratios shown |
| 2 | DeepSeek | §3.9's mechanism agreement holds only at 0.0051 | **Held, sharpest of the round** | See below |
| 3 | DeepSeek | §4.5's "a bracket that now surrounds it" is stale | **Held.** The old bracket surrounded 0.0248; this one sits above it | "sits entirely above it" |
| 4 | DeepSeek | §3.3 still says "the four designs" | **Held.** *My miss:* I fixed the caption and skipped the prose — the identical error one round after fixing it | "the seven designs" |
| 5 | DeepSeek, Qwen | §4.4 gives only the light design's T/W | **Held.** *My miss* | All four values |
| 6 | Grok | §2.12 has an orphaned antecedent | **Held.** *My damage:* inserting the sea-level paragraph cut "both" from its referent | Referent named explicitly |
| 7 | Grok | Highlights carries "from 42 to 32–36" | **Held.** A changelog in a findings bullet; MDPI prints it as a finding | "leaves a mass advantage of 32 to 36 percent" |
| — | ChatGPT | The attached file is not the corrected build (8 sub-claims) | **Did not hold.** Stale file, second round | Section 0 |
| — | Qwen | §3.2 pointer, sea-level and reverse-transition all absent | **Did not hold.** All three present and correct | Section 1 |

### 3.1 The sharpest external finding, and a claim of mine it falsified

DeepSeek: Section 3.9 says the predicted scaling ratio is 3.08 and the computed ratio is
3.04 — and 3.04 is 0.0154/0.0051. But **Section 3.8 had just declared 0.0051 unpinned**,
reporting an interval of 0.0035–0.0074. At the ends the ratio is **2.08 and 4.40**, both
outside the prediction.

And I had written, in §3.8, *"nothing in that section depends on where inside the interval
the value falls."* **That sentence was false, and I wrote it.** It is true of the "fraction
of the light charge" comparison and false of the three-digit agreement.

**Done, in both sections.** §3.8 now says one thing in §3.9 does *not* hold that way and
names it. §3.9 now says: the mechanism — that solidity and dynamic pressure are the only
two terms that move — does not depend on the choice, and neither does the direction or the
order of magnitude; **the three-digit agreement does.** It is reported as a consistency
check at the sizing point, not as a validation of the scaling law.

### 3.2 A second thing I wrote that was simply wrong

DeepSeek also attacked my sea-level justification. I had called sea level "the
conservative choice" because altitude reduces drag with the density ratio and would
lengthen every range figure.

**That is wrong, and the paper's own equation shows it.** Range here is
`f_fuel · E* · η_chain · (L/D) / g` — **density does not appear.** At a fixed lift
coefficient a thinner atmosphere is simply flown faster for the same L/D and the range is
unchanged. Altitude moves these figures only by moving L/D, which it can do either way.

**Done:** the claim is withdrawn *and the reason it was wrong is printed in the paper*,
not silently deleted. Sea level is now described as neither conservative nor generous —
simply the one atmosphere everything is computed on.

### 3.3 A new open item nobody had raised in twenty-three rounds

DeepSeek: the paper never prices **stopping the tip rotors edge-on** against letting them
free-wheel. Stopped edge-on at a controlled azimuth is **ΔC_D0 = 0.0008**; free-wheeling
is **0.0154**. A factor of twenty. Section 3.3 says the configuration "has no rotor to
stop and therefore needs no indexing mechanism" — but that is a *design choice, not a
consequence.*

**He is right and the calculation has not been done.** Sizing an indexing mechanism for
eight small discs, charging its mass and failure modes, and re-solving against a zero-lift
drag reduced by 0.0146 is bounded work.

**Done, as disclosure rather than as calculation.** §3.3 now states the trade before the
computation and says the free-wheeling state "was adopted because it needs no hardware,
not because it was shown to beat the hardware." §4.6 carries it as an open item.

---

## 4. Acting on Qwen's Round 23 closing paragraph found four more defects in an hour

Qwen's recommendation: *"every guard this project has built checks that a reference
resolves, and none checks that it resolves to the right thing."*

**Implemented in `makale/uretim/baglanti.py`.** For every `Section N.M` pointer, it takes
the distinctive numbers in the window after it; if **none** appears in that section's
body, it tells a human. It does not decide — the rule cannot be made exact, and a guard
that cannot tell the difference should say so rather than pretend.

**Two things about building it are worth reporting because they are the point.**

**Its first version silently returned nothing.** It split sentences on `.` — and "3.2"
and "4.9" *contain* a period, so every sentence boundary fell inside a number. It ran
clean and found nothing, and I nearly shipped it. **A guard that appears to pass is worse
than no guard.** Caught by putting the old defect back into a copy of the file and
checking that the guard fires. It does.

**On its first real run it found four wrong pointers, three of them years old:**

| Pointer | Problem |
|---|---|
| "the component build-up of **Section 3.11** shows them as 2.73, 0.61, 2.60 kg" | §3.11 is a 321-word summary. Those numbers are in **Supplementary S2** |
| "a further condition, given in **Section 3.11**: 5.63 kW kg⁻¹" | Same. **S2** |
| "the ranges of **Section 3.8** are computed on 0.0248" | §3.8 is the **heavy** line and stands on **0.0200**. Should be §3.7 |
| "**Section 3.8** reports the ratio would be 2.08 and 4.40" | It does not. They are computed in §3.9 |

**The fourth was mine, written twenty minutes earlier, while fixing finding 3.1.** The
guard caught its author's fresh mistake on its first run. All four are fixed.

Current state: **43 numerical checks, 0 deviations; nine forbidden stale values absent
across twelve source files; pointers, table and figure citations all resolving; seven
advisories remaining, all inspected by hand and all legitimate.**

---

## 5. Open items — stated, not closed

1. **Battery buffer:** the 50 kg design needs about **3.8×** the highest specific power
   yet measured on a production cell.
2. **Transition pitching moment:** no current method predicts it reliably. At zero
   aerodynamic moment the light design loses 5.4 m where the kinematic model reports zero.
3. **Take-off margin and attitude authority** come from the same four propellers and
   compete.
4. **The landing transition is unmodelled.**
5. **Free-wheeling versus indexing is unpriced** (new this round).
6. **No wind tunnel, no flight test.**

---

## 6. What we are asking, and it is short, because we think this is the end

**The author's read is that the returns have gone: last round produced seven
sentence-level fixes and no argument-level objection, against three code defects and two
withdrawn findings in earlier rounds. That is what approaching a cut-off looks like, and
these processes run forever if nobody calls it.** So:

**1. Is there anything left that changes a conclusion?** Not a word, not a caption — a
*conclusion.* If yes, say it and we keep going. If no, say that too; it is the more
useful answer and we will not take it as flattery.

**2. Grok and DeepSeek both said yes to submission after fixes that are now applied.**
Does that still stand against this build? Qwen's three conditions were phantoms except
the §4.4 one, which is applied — does Qwen still have conditions?

**3. Read §3.9's new paragraph specifically.** It withdraws force from the paper's
cleanest-looking agreement, which is exactly the kind of paragraph that gets written
badly. Is it too apologetic, not apologetic enough, or right?

**4. One last stale-twin sweep**, with the file-check in Section 0 done first. Current
values: bracket 0.0285–0.0381; L/D 8.8–10.8; mass advantage 32–36 %; T/W 1.066 / 1.041 /
1.132 / 1.082; heavy range 1 571 km charged, 1 814 km published; K_L 0.796; heavy rotor
charge 0.0035–0.0074 carrying 0.0051; light rotor charge 0.0154.

**5. If you say it is ready, say what you would bet a referee objects to anyway.** Not to
fix it — to have the answer written before the question arrives.

---

## 7. A closing note on method, for the record

Twenty-four rounds. What actually moved this paper:

- **Round 19, Qwen:** an arithmetic claim the paper made about itself was false → a code
  defect → a physical finding withdrawn.
- **Round 22, the author:** one sentence, read by a human, that denied the paper's own
  thesis. Three rounds of four readers had passed over it.
- **Round 23, Grok:** one table, read alone, carrying a comparison the paper had retired
  three paragraphs above it.
- **Round 23, a script nobody had run:** a selection rule that binds at one scale and not
  the other.
- **Round 24, Qwen's method suggestion:** a class of error no existing check could see,
  and four instances of it.

**Not one of these came from consensus.** Every one came from a narrow, deep look at a
single object — one sentence, one table, one rule, one class of pointer. Broad agreement
has been the least productive thing in this process; specific, checkable, falsifiable
objections have been nearly everything.
