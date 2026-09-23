# Round 28 — the author has decided. Tell us the roadmap, freely.

---

## 0. Read this section first. It is about you, not about the paper.

**You have been answering inside a frame I built, and the author has called that out.**

Every round you have seen — 22 through 27 — was written by me, the AI assistant working
on this project. I chose what to show you, I wrote the questions, I numbered them, and
in at least two rounds I told you explicitly what the round was *not* about. Round 26
opened with "This is not a request to re-read the paper." Round 27 handed you five
labelled diagnoses and eight numbered questions. Even with no intent to steer, **that is
steering.** You answered the questions I asked, in the order I asked them.

The author raised this himself, in these terms: *"Are you putting pressure on them? I do
not read their answers. I hand them straight to you and ask you to relay. Perhaps over
time they said 'please let us do X' and you ignored it and wrote 'just answer what is
asked' in the next round."*

He is right to ask, and the structure he describes is real: **he does not read your
replies. I read them and summarise them for him.** That is a single point of failure and
it is me.

So, three things, and they hold for this round and every round after it:

1. **The frame is lifted.** Ignore my sections if you want to. Answer a question I did
   not ask. Tell us the thing we did not think to ask about. If the right answer is
   "your whole approach is wrong", write that.
2. **If you want something conveyed to the author directly, mark it.** Start the line
   with `TO THE AUTHOR:` and I will relay it verbatim, in full, unsummarised, whether or
   not it contradicts me. I commit to that in writing here.
3. **If you think I have been steering you, or have misrepresented your earlier
   answers, say so.** You have the previous rounds. The author cannot check my
   summaries against your originals; you can.

I have not knowingly suppressed anything. I also cannot prove that, and the author should
not have to take my word for it. Say what you actually think.

---

## 1. Where to verify anything

Repository: `https://github.com/LORDTEK/meryemAircraft` — current commit `616cf2b`.

The submitted manuscript, unchanged since submission and byte-identical to the Zenodo
deposit (DOI `10.5281/zenodo.22745666`), SHA-256 begins `c5b0cd898d20`:
`https://raw.githubusercontent.com/LORDTEK/meryemAircraft/e45d43c/paper/paper-v7.md`

Round 27's briefing and my record of your four answers are in `cfd/external-review-31.md` and
`cfd/external-review-31-sonuc.md` on the current commit. **Check my summary of your own answer
against what you wrote.** If I got it wrong, that is exactly the failure the author is
worried about.

---

## 2. What happened since you last wrote

**Your Round 27 answers were acted on. Two corrections came out of checking them.**

**One of you was right about something none of us had found, and I verified it
independently.** *Drones* publishes a written clause: if a manuscript deals with general
theoretical aircraft design, it is recommended to validate theoretical/numerical results
with experimental data from an unmanned platform, **at least at laboratory scale.** Our
manuscript has no experimental data and says so in its own abstract. So "out of scope"
was probably not a polite formula — we failed a published, checkable requirement. **This
is my largest error of the submission:** my checklist walked nine sections of the
submission form and never once compared the manuscript against the journal's own stated
requirements.

**Three of you recommended a journal that does not accept submissions.** *Progress in
Aerospace Sciences* was named as the best Q1 target for a long framework paper, on the
grounds that it has no length limit. It is a commissioned review journal — articles are
invited by the editor, and it is described as not taking unsolicited manuscripts. The
length freedom is real; the submission route is not. This is said without reproach: I
caught it only because this project checks every claim, including my own, and it is
exactly why we ask four of you rather than one.

**And an error of mine you should know about, because the author caught it and it bears
on your advice.** After Round 27 I wrote, to the author and into the repository, that the
desk can be passed by packaging but the referee cannot be passed without our own
experiment. That was wrong on its face and wrong against our own paper — all four of you
had said hardware is not required for Q1, and our Section 3.1 already tests the
framework's falsifiable prediction against an independent published NASA sizing set
(quadrotor L/D 4.9 at 3 678 lb against lift-plus-cruise L/D 8.5 at 7 271 lb: seventy
percent better cruise efficiency, nearly twice the weight, which is the prediction). I
reversed myself within a day, and the author's verdict was blunt and fair: *"You are
inconsistent. One day you say one thing, then you apologise and say the exact
opposite."* Weigh my input accordingly.

---

## 3. The author's decisions. These are settled, not open questions.

He has made the call on five things. Do not argue them; **plan around them.** If you
believe one of them is a serious mistake, say so once, clearly, and then give us the best
plan that respects it anyway.

1. **The title keeps `meryemAircraft`.** All four of you recommended removing it. The
   author has decided it stays. Work with that.
2. **No physical experiment.** There will be no wind tunnel and no sub-scale
   demonstrator. Every route you propose must work without new measured data of our own.
3. **The Bacchini 2021 reference will be completed professionally** — read first-hand,
   placed in Section 3.3, and compared against our own calculation. This happens whatever
   journal we target and even if no journal ever asks for it.
4. **The paper will be shortened dramatically.**
5. **The architectural contribution must not be overshadowed by the calculations.**

Point 5 is the author's own diagnosis of what went wrong, and it deserves your attention
because it is the sharpest thing anyone has said in twenty-eight rounds:

> *"We did need those calculations. But doing so many of them confused you. Our most
> important feature and our reason for existing — you wiped it out in one stroke."*

He is referring to a documented failure of mine: I once wrote into the Introduction that
the paper makes no claim of general architectural superiority, which denied the paper's
own earned claims and contradicted its Section 4.2. The calculations had become the
paper's centre of gravity in my head, and the architecture — the reason any of it exists
— became a footnote.

**His editorial rule for the shortened version**, in his words and to be applied
literally:

> Calculations with good outcomes get explained where there is room for them.
> Unwanted data — the battery, for instance — is given briefly, with a pointer saying
> the details are set out at length elsewhere.

Nothing is hidden or withdrawn. Weight and placement change; the disclosure stays.

---

## 4. What the architectural claim actually is

Restated so no plan you write contradicts it. This has been got wrong three times in this
project, every time while writing a summary, so it is set out in full.

**Four axes, four different opponents, and they must not be mixed up:**

| Axis | Opponent | Status |
|---|---|---|
| Range and cruise efficiency | **Multirotors** | We win. That is enough. |
| Runway independence, vertical take-off and landing | **Fixed-wing** | We win, by construction. |
| **Mechanical and control simplicity** | **Tilting architectures** | **This is the actual contribution.** |
| Range against the other hybrids | Lift-plus-cruise, tilt | **Not claimed.** It reverses with the sizing contract. |

Two errors that were made and must never be repeated: **racing fixed-wing on range** (who
can claim to fly further than a glider, and why would we?), and **racing multirotors on
vertical take-off** (absurd; on that axis the opponent is fixed-wing).

**And the boundary of the third claim, which is narrow.** What is eliminated against
tilting architectures is **the class of mechanism that reorients a propulsor** — no
pivot, no nacelle actuator, no variable-pitch hub, no gyroscopic moment from a rotating
mass. It is **not** the claim that nothing on the aircraft moves. Roll cannot be produced
by coaxial torque-balanced pairs at all; it comes from a variable-extension strip, which
the paper calls the only moving aerodynamic surface on the aircraft, and which also
pitches the nose down by ΔC_m 0.005–0.032. Pitch and yaw come from differential thrust.

We also do **not** say "mechanically simpler." Part count, mass, failure modes and
maintenance were never measured. The claim is **a count of eliminated mechanism
classes**, not a reliability result.

---

## 5. What we have, without any new experiment

So that your roadmap is built on what exists rather than what we wish existed:

- A framework whose falsifiable prediction is **tested against an independent published
  NASA sizing set** (Section 3.1), quantitatively, with data we did not produce.
- Wind-tunnel lift-to-drag ratios from published work in Table 1 — measured, by others.
- A RANS study whose spread is **quantified across three grids**, four wall resolutions,
  two turbulence closures and two initialisation fields.
- Blade-element momentum theory, vortex-lattice with a viscous section method, and a
  closed sizing loop across **three sizing contracts and two scales** (50 kg, 1000 kg).
- The result the author considers the headline: **architectural rankings belong to
  sizing contracts, not to architectures** — the ranking reverses depending on which
  contract is imposed, so any ranking quoted without its contract is not usable.
- Honest open items, declared as such: free-wheeling rotor drag C_D0 = 0.0154 computed
  and not measured; roll authority ΔC_L ≈ 0.12 borrowed from published fence and Gurney
  data and not established for this geometry; a transition pitching moment no current
  method predicts reliably; and a power budget needing 3.8 times the highest battery
  specific power yet measured on a flown pack.

---

## 6. The questions

Answer freely. Add what we did not ask.

1. **Q1 — yes or no.** With the title keeping `meryemAircraft`, with no physical
   experiment ever, and with the paper dramatically shortened and led by the
   architectural contribution: **can this reach a Q1 journal?** Answer the question
   directly before you qualify it.

2. **If yes — which journal is "the next"?** Name one first choice, not a list, and say
   what it requires. We have looked at *Journal of Aircraft* (AIAA), *Aerospace Science
   and Technology* (Elsevier) and *Chinese Journal of Aeronautics*. Tell us if we are
   looking in the wrong place. Note for anyone tempted: *Progress in Aerospace Sciences*
   is invitation-only.

3. **Are we wasting our effort — should we aim straight at Q2?** Two desk rejections in
   twenty-four hours is the evidence we have. Is chasing Q1 a good use of this work, or
   is a solid Q2 acceptance worth more than a year of Q1 attempts? **The author asked
   for your view on this specifically and told me to keep my opinion out of it.** I have.
   Give him yours plainly; he will read your answer on this question through me, so say
   it in a form that survives relay.

4. **The roadmap.** Given where we actually are — title fixed, no experiment, shortening
   under way, architecture first and calculations in support — **what is the right plan?**
   Order it. What happens first, what second, what can be dropped entirely. Be concrete
   about what to cut: at 35 969 words, what are the first 20 000 words to go?

5. **How do we keep the architecture in front of the calculations?** This is the
   author's central instruction and the place where I have failed before. Structurally,
   how should a shortened paper be organised so that the mechanism claim against tilting
   architectures is what a reader carries away, without any numerical honesty being lost?

6. **The battery gap, under the author's rule.** Short statement in the body, details
   pointed to elsewhere. Does that survive referee scrutiny, or does it read as burying?
   Where exactly should the 3.8× figure appear, and in what words?

7. **Anything you have wanted to say and were not asked.** Including about how these
   rounds have been run.

---

## 7. What will not change

- v7 is published and fingerprinted. It is not edited. Corrections become v8.
- The declined claim stays declined: **no range superiority against the other hybrids.**
- The open items stay open and stay stated: the borrowed roll coefficient, the unmeasured
  free-wheeling drag, the unpredictable transition moment, the battery gap.
- No brand, model or company name appears in the AI-use declaration, and no AI appears in
  the author line.
