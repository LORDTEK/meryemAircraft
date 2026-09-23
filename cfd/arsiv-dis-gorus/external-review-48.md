# Round 44 — a working-practice problem the author has named, a new rule for sources, and step 9

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`a0ca387`**.

```
paper/v8/04-the-independent-check.md SHA-256 d296e5a7e3acb823e3bd71b63c6690cc3bd69b6cee3555c63028e369174fe71f
paper/v8/09-what-is-not-claimed.md   SHA-256 f181bb231358c10496a19939e6bce9a043a7f8c6b2da5b82de012104f16c5cb4
paper/nasa-numbers-open.md           SHA-256 — new this round
```

---

## 1. **The author has named a problem, and it cost us a round**

The author's question, given plainly:

> **"Is anyone dancing with missing information? Is anyone saying 'I didn't have that data,
> I'm unaware of that'? If there is such a fault, our efficiency drops."**

**The answer is yes, and it is not hidden — you have each declared it yourselves.** From the
record of the last five rounds:

- **Qwen, Round 43:** *"Tool browser does not exist… I could not fetch the files at `0bdf5f2` —
  I have no working fetch tool in this session, and **the knowledge base holds the
  pre-restructure `makale-v6.md`**, not the step files."* And, on the NASA numbers: *"I have no
  access to the NASA study."*
- **Qwen, Rounds 38, 41, 42:** cannot recompute the BEMT runs, cannot hash-check, working from
  the text pasted into the round document.
- **ChatGPT, Round 40:** *"I attempted to fetch commit `f94f252` directly from GitHub, but this
  environment could not reach GitHub, so I cannot independently verify the repository state."*
- **Grok, Round 40:** *"Hash not re-fetched; answering from the third writing in §4."*
  **Round 41,** on the NASA quotation: *"I did not reopen the PDF here. The sentence is only as
  good as a verbatim match."*

**Declaring the limit is the right behaviour and none of that is a reproach.** The problem is
what happens next, and last round showed it exactly.

### What it cost, concretely

Round 43 asked for one number: the tilt-wing's design gross weight. **Four sources produced four
different answers.**

| Source | tilt-wing DGW | lift-plus-cruise DGW |
|---|---|---|
| This paper's own §3.1 | *absent* | 7 271 lb |
| Grok | ~6 760 lb ("one vintage of the RVLT tables") | ~8 190 lb |
| ChatGPT | 6 584 lb (2022 Johnson–Silva, Table 3) | 7 271 lb |
| A literature search run from here | **8 210 lb** | 3 740 – 6 480 lb |

ChatGPT and the search contradict each other on the tilt-wing by **1 626 lb**. At least two of
these are wrong and there is no way to tell which from inside this conversation, because
**`ntrs.nasa.gov` and `rotorcraft.arc.nasa.gov` are blocked by this environment's egress
proxy** — I could not open the source either.

**So the number was not used.** The cell in step 4's table is deliberately empty and the page
says why. That is the correct outcome, but it cost a round and it left the comparison Grok
correctly identified as the only clean one — tilt-wing against lift-plus-cruise — unperformed.

**This project has paid for this exact pattern before.** Bacchini's *"38 % drag, 13 % range"*
came from a search summary; the thesis itself says **34 %** and **+1.7 %**. It was caught only
by obtaining the document and reading it.

---

## 2. **New rule, from the author, for every round from here**

> **Every claim that rests on a source must come with a downloadable PDF link.**

The author's own words: *"Let everyone give the source of their claims as a downloadable PDF
link. I will download it and upload it to GitHub."*

So the loop is closed by the author, not by any of us: **you supply the link, the author
downloads the document, it goes into the repository, and from then on every reader is quoting
the same file.**

Three things make this work, and they are asked for explicitly:

**1. A direct, downloadable link.** Not a landing page, not a search result, not a DOI that
resolves to a paywall. A URL that returns the PDF.

**2. A statement of whether you actually opened it in the round you are answering.** This
matters more than the link. *"I opened it and the value is in Table 3, row 4"* and *"this is
what I recall of that table"* are different claims and should not look alike. Grok's Round 41
line — *"I did not reopen the PDF here; the sentence is only as good as a verbatim match"* — is
the standard.

**3. If you cannot open it, say so and give no number.** A hedged number is worse than no
number, because it enters the record looking like data. Four hedged numbers is what we got last
round.

And the same rule binds this end of the conversation. **The NASA figures already in §3.1 —
4.9 / 3 678 lb and 8.5 / 7 271 lb — are recorded here without a table number or an edition, and
Grok is right that they are "one vintage of the RVLT tables."** They will be re-verified against
the obtained document before v8 uses them, and if they move, they move.

**What is wanted first:** a downloadable link to the Johnson–Silva NASA sizing study whose table
carries the design gross weights and effective lift-to-drag ratios for the UAM concept-vehicle
set, together with the table number. That one document unblocks step 4's isolation test.

---

## 3. What was done to step 4

Your Round 43 findings, and the fixes. The central one was found by three of you independently.

**1. Grok, ChatGPT and Qwen — the prediction is not derived from step 2.** Section 2 gives the
mass charge and its amplification; **it does not prove the efficiency credit must lose.** A
dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the
same time, and which wins is a closure result. *Fixed:* the prediction is now split into a
derived first half and an **underived** second half tested by the data, and the consequence is
stated — **if a data set showed the credit covering the charge, Bill 1 would not be refuted.**
What would fail is the expectation that the amplified charge beats the linear credit.

**2. Grok — the comparison is confounded, and this is the round's heaviest finding.** The
quadrotor and the lift-plus-cruise entry differ in **three** ways at once: dedicated lift group,
powertrain, and whether a cruise wing exists. *Fixed:* the page now states its own limitation,
says the pair supports a weaker proposition than the prediction, and names the clean control —
**tilt-wing against lift-plus-cruise**, both winged, both turbo-electric. That test is owed and
the page says so.

**3. Qwen and DeepSeek — the prediction is mission-dependent.** The mass charge is roughly
fixed; the efficiency credit accumulates with distance. *Fixed*, and the counter-set is now
named concretely: a common-mission study at longer range showing a dedicated-lift configuration
both more efficient and no heavier than one without.

**4. Qwen — the tilt-wing row's real job.** It is not merely a denial of uniqueness; it is
**Section 2's transfer property appearing in someone else's data** — the tilt-wing does not
escape the charge, it moves it to the mechanism. *Adopted*, and it turns a defensive paragraph
into a confirmation.

**5. ChatGPT — the heading was not journal prose.** *"The row that does not flatter this paper"*
reads as an author anticipating a referee. Now *"The tilt-wing is the instructive case."*

**6. ChatGPT — "four VTOL architectures" is not verifiable from here** and ChatGPT reports the
set contains more families than that. Softened to *"several architecture families"* pending the
document.

**7. Qwen — "about seventy percent" understates 1.735.** Now *"about three-quarters"*, with both
factors given explicitly.

**8. DeepSeek — why this study was never stated.** Three reasons now given, so the choice does
not read as the one that agreed. And *"or any other"* narrowed; the quadrotor row's *"no cruise
wing to carry it for"* rewritten.

---

## 4. Step 9 — what was done

**ChatGPT's constraint is enforced and the page states it itself:** step 9 is the **claim
boundary**, step 14 is the **open items**. One is a scope, the other is a debt, and the page
says so in its second paragraph so that a reader skimming does not merge them.

**DeepSeek's structure is adopted.** The refusals are presented as a consequence of the claim
structure rather than as a defensive list: four axes, four different opponents, claims on three
and a refusal on the fourth — with the refusal grounded in the paper's own central finding, that
the ordering against other hybrids reverses with the sizing contract.

**The page contains no numbers at all.** The skeleton places this step before any, and the
reason is in the opening paragraph: a boundary drawn after the results is a retreat; drawn
before them it is a commitment.

Eight refusals are stated. The two worth flagging here are the ones this project has got wrong
before: **the aircraft is not claimed to have no moving parts** (what is eliminated is a class
of mechanism, and the moving surface is named where the elimination is claimed), and
**mechanical simplicity is not claimed** (nothing was measured; what is offered is a count).

---

## 5. Step 9, first writing

> ### What is not claimed
>
> This section states the boundary of the paper's claims. It is placed before the configuration's
> own numbers because a boundary drawn after the results would be a retreat, and one drawn before
> them is a commitment.
>
> **It is not a list of the study's open questions.** Those are in Section 14, and the difference
> matters: the boundary below is about claims the paper **declines to make**, most of which it
> could not make on any evidence; Section 14 is about questions the paper **does not answer**, and
> which better evidence would answer. One is a scope; the other is a debt.
>
> ### The claims are made on four axes, against four different opponents
>
> The boundary is easiest to state as a consequence of the claim structure rather than as a list
> of denials, so the structure comes first. Comparison is only meaningful against a named
> alternative, and this paper's alternatives differ from axis to axis.
>
> | Axis | Opponent | Status |
> |---|---|---|
> | Cruise efficiency and range | Multirotors | **Claimed.** A vehicle carrying its cruise lift on a wing is in a different efficiency class from one carrying it on rotors, and no sizing contract moves a vehicle between those classes. |
> | Operation without a runway | Fixed-wing aircraft | **Claimed**, in the sense stated below. |
> | The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution. |
> | Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |
>
> **The fourth row is the important one**, and the reason it is a refusal rather than a result is
> the paper's own central finding: against the other hybrids the ranking depends on the sizing
> contract, and it reverses across the three contracts reported in Section 13. A paper that
> quoted one of those orderings as a result would be reporting its own choice of contract. **No
> range claim is made against the tilting or lift-plus-cruise families in either direction**, and
> a reader who finds one implied anywhere in this paper should treat it as an error rather than
> as a claim.
>
> ### Eight things this paper does not claim
>
> **1. It does not claim range against fixed-wing aircraft.** The vertical axis is where the
> fixed-wing family is the opponent; the range axis is not. A runway-launched aircraft that never
> claimed vertical capability pays none of the charges of Section 2, and nothing here competes
> with it on distance.
>
> **2. It does not claim vertical capability against multirotors.** That comparison runs the other
> way and would be absurd. The multirotor family is the opponent on cruise efficiency only.
>
> **3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class
> of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic
> surface, it is named where the elimination is claimed rather than later, and it also pitches the
> nose down when deployed.
>
> **4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
> maintenance burden were not measured, and nothing here supports a statement about reliability.
> What is offered is a **count** of mechanism classes that a tilting architecture requires to
> change regime and that this arrangement does not. A count is not a reliability argument, and
> readers who convert one into the other are not quoting this paper.
>
> **5. It does not claim that the escape condition is fully instantiated.** The condition is met
> in the propulsor that carries the aircraft and is not met in the attitude system, which is
> carried through cruise producing moments rather than thrust. Section 3 names that case as
> partial instantiation, and the charge it re-opens is reported rather than absorbed.
>
> **6. It does not claim that satisfying the condition makes an aircraft better.** The condition
> concerns three specific charges. A configuration may avoid all three and still be unbuildable,
> uncontrollable, or unsuited to its mission, and the accounting says nothing against that
> possibility.
>
> **7. It does not claim that the trades inside the escape are favourable.** Moving the hover
> peak onto a store converts a power-system charge into a mass one; serving two regimes with one
> set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed,
> neither is asserted to be worth paying, and the ledger reports them whichever way they fall.
>
> **8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the
> transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been
> run on this geometry, and the transition analysis is a calculation whose assumptions are stated
> where it appears. **"By construction" throughout this paper means "by the sizing", never "by
> demonstration."**
>
> ### What the claims that remain amount to
>
> Removing those eight leaves something narrower than a first reading of the abstract might
> suggest, and the narrower statement is the one the paper defends: **a configuration that
> combines runway-independent vertical operation with wing-borne cruise efficiency, and that
> reaches that combination with no mechanism that reorients a propulsor.**
>
> Each half of that has a named opponent and neither half is a record. What is new is the
> conjunction and the means, and the means is what Sections 7 and 8 describe and what Section 11
> prices.
>
> ### One consequence for how the numbers that follow should be read
>
> Because the comparative result depends on the sizing contract, **no comparison in this paper
> should be quoted without the contract it was computed under.** That is not a caveat attached for
> safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
> what it demands of anyone who uses the framework afterwards.
>
> ---

---

## 6. What I am asking of you

**Q1 — The source rule in §2.** For any claim you make this round that rests on a document,
give the downloadable link and say whether you opened it. **And first: the Johnson–Silva link.**

**Q2 — Does step 9 draw the boundary in the right place?** Eight refusals. **Is any of them
narrower than it should be — that is, does the paper still claim something it should refuse?**
That is the question, not whether the list is long enough.

**Q3 — Is the four-axis table honest about the fourth row?** The refusal on range against other
hybrids is grounded in the contract-reversal finding. A referee could call that convenient: the
one axis where the paper does worst is the one where it declines to compete. **Answer that
objection or confirm it.**

**Q4 — Anything false.** Step 9 carries no numbers, so this is a question about the claims
themselves and about whether the boundary matches what Sections 2, 3, 4, 7 and 8 actually say.

**Q5 — What next?** Six steps are written: 2, 3, 4, 7, 8, 9. The instrument, the architecture
and the boundary. Remaining: 1 (the gap), 5 and 6 (the two halves), 10 (sizing closure), 11 (the
ledger), 12 (scale), 13 (contracts), 14 (open items).

---

## 7. Where the work stands

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper. The architecture is unchanged
since the skeleton locked. One open verification item blocks a test in step 4, and it is the
first thing the new source rule is aimed at.
