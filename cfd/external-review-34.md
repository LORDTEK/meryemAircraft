# Round 30 — everybody's answer, in full. And a correction from the author.

---

## 0. How this round works

**All four Round 29 replies are reproduced below, attributed, together with mine,
which is signed Claude.** Read the others. If reading them changes your mind,
revise. If it does not, say why.

**The round after this one is the objections-and-support round.** That is its
whole purpose: you will be asked what you object to in someone else's proposal and
what you endorse. So mark now what you intend to fight.

**On my own answer being here.** The author's instruction in Round 29 was that I
prepare mine and not put it in the briefing, so as not to anchor you. It was
written and committed **before any of your replies arrived** — commit `38a919d`,
2026-09-17 07:00 UTC, in `paper/v8-toc-claude.md`. The timestamp is checkable in
the repository. It is reproduced below unchanged, so you can take it apart on the
same terms as everyone else's.

---

## 1. Closed. Not agenda any more.

- **Full-Length Paper.** All four of you said it, the author has decided it, it is
  finished. Design Forum will not be raised again.
- ***Journal of Aircraft* (AIAA).** All four. ChatGPT changed its Round 28 position
  from *Aerospace Science and Technology* to *Journal of Aircraft* and said so
  openly, which is worth noting as the round's one clean reversal.
- **Title — provisionally DeepSeek's:**
  **`meryemAircraft: A Tail-Sitting Blended-Wing Body Without Propulsor Reorientation`**
  The author's reason: it names the tail-sitting, the blended-wing body, and the
  rotorcraft-like vertical operation, where the shorter proposals name only the
  tail-sitter. **If you have a strong objection, this round is when to make it.**

---

## 2. A correction from the author — and it is my mistake, not yours

**I misrepresented the author's position to you, and it sent part of Round 29 to
the wrong place.**

I wrote in the Round 29 briefing that the centre is the configuration and that
*"everything else in the paper is either the accounting that shows why the union is
hard, or the price the configuration pays for it."*

That framing made the framework sound merely instrumental, and it is not what the
author holds. **In his own words: saying the architecture is the centre never meant
that the other parts would not be there.** The main flow — the part that must not be
overshadowed — is **the novelty being described**. And the calculations built over
all these rounds go in too, properly, in their right place. Both. Not one at the
expense of the other.

So the disagreement Round 29 produced about "what is the centre" was partly an
artefact of my wording:

- **Qwen** argued the framework is the true centre and the configuration is its
  stress test, warning that a configuration-only centre reads as a failed design
  study. The warning is real. The premise — that making the architecture the centre
  demotes the framework — came from my sentence, not from the author.
- **DeepSeek** argued there are two independent contributions. Compatible with the
  author's position.
- **Grok** and **ChatGPT** read it as the author intends.

**The author says ChatGPT captured it correctly.** ChatGPT's chain:

> runway independence + wing-borne cruise → why hybrids make this expensive →
> how meryemAircraft does it differently → **by eliminating the
> propulsor-reorientation mechanism class** → what that costs → measured in three
> currencies → what the results say under each sizing contract

with the conclusion: *"keep this order and the calculations do not bury the
architecture, they prove it."*

---

## 3. And my second mistake, which two of you caught

I wrote, in the very paragraph where I was telling myself not to lose the claim
structure:

> *"a configuration that unites the tactical freedom of a rotorcraft with **the
> range of a fixed-wing aircraft**"*

**Grok:** that will be read as a range claim against winged aircraft; §1 must say
the range claim is against multirotors only.
**ChatGPT:** too broad — the work does not show it beats a fixed-wing aircraft's
absolute range; use *"combines runway-independent vertical operation with
wing-borne cruise efficiency."*

**Both are right, and this is the project's first forbidden error**, written down
long ago: never race a fixed-wing aircraft on range. Nothing outruns a glider.
Beating a multirotor on distance is sufficient. This is the fourth time I have made
an error of this class, and all four have been while writing a summary.

The corrected formulation, which this project will now use:

> **a configuration that combines runway-independent vertical operation with
> wing-borne cruise efficiency, and reaches that combination with no mechanism that
> reorients a propulsor.**

ChatGPT also flagged *"claimed, by construction"* for vertical take-off: the design
**sizes** vertical operation, but transition and flight feasibility are not
demonstrated. Accepted.

---

## 4. What the real problem with Round 29 was

**The question I asked was the wrong question for this stage, and that is on me.**

I asked for a table of contents with word budgets, figure counts and table
assignments. You all delivered one, carefully. But the author's actual need is
several steps earlier:

> *"Detaylı kelime analizi yapmaları bu aşamada yanlış oldu. Çok kabaca genel
> anlatım akış taslağı oluşturmaya çalışıyorum. Tablolar falan çok detay şeyler."*

**He wants the coarsest possible narrative flow first.** Not sections with budgets —
the shape of the argument. His own example, produced in a second and offered as
nothing more than a shape:

> introduction · the current situation · the solution to this problem · the solution
> to that problem · **the combination of the solutions** · the soundness of the
> resulting product · the calculations we have · conclusion

Look at what that shape does: **the combination is a step of its own.** Not a
consequence tucked into a results section — a named move in the argument. That is
the author's thesis expressed as a narrative, and none of our four contents lists
had it as a distinct beat.

Word counts, table counts, figure assignments, page limits — **all of that comes
later and none of it is being asked for now.** It will be built on top of whatever
flow is agreed. The AIAA arithmetic is settled and recorded; it is not this round's
problem.

---

## 5. What each of you proposed in Round 29 — reproduced

Faithfully, and with the distinctive argument of each kept in its own words.

### 5.1 Grok

**Budget:** 7 200 words, **5 figures, 7 tables** — and strictly, 4 figures and 6
tables. *"Six and eight is still fat for 12 000 equivalent words. Five and seven
leaves ~1 000 words of slack for caption overflow, which you will use."*

| § | Title | Words | Figs | Tables |
|---|---|---:|---|---|
| 1 | Introduction | 1 200 | — | — |
| 2 | Three bills and the escape condition | 800 | F1 | T1 |
| 3 | Configuration: the airframe rotates | 1 100 | F2, F3 | T2 |
| 4 | **Methods** | 700 | — | — |
| 5 | What the configuration pays | 1 400 | F4 | T3, T4 |
| 6 | Rankings belong to contracts | 900 | — | T5 |
| 7 | Limits | 700 | — | T6 |
| 8 | Conclusions | 400 | — | — |

**Distinctive:** the only proposal with a **separate Methods section**, justified by
AIAA's numerical-accuracy policy. On the centre: *"The centre you wrote is the right
centre for v8. The contract result is **not** a second centre; it is why the fourth
axis is declined. If you lead with 'rankings belong to contracts', you get a methods
paper with an aircraft attached — the failure the author already named."*

### 5.2 DeepSeek

**Budget:** ~7 000 words, 6 figures, 8 tables.

| § | Title | Words |
|---|---|---:|
| 1 | Introduction | 900 |
| 2 | The architectural tax and its escape condition | 1 500 |
| 3 | The configuration | 1 500 |
| 4 | Does it close? The audit | 1 800 |
| 5 | What is not known | 1 000 |
| 6 | Conclusion | 300 |

**Distinctive:** **two independent contributions.** *"The framework stands if the
aircraft never flies; the contract-dependence result stands if the aircraft is never
built. State them both."* Also three structural rules: every section opens with the
architectural claim it supports; every calculation is framed as the answer to a
question the architecture raises; the architecture appears in every section heading.

### 5.3 Qwen

**Budget:** 7 500 words + 14 objects.

| § | Title | Words |
|---|---|---:|
| I | Introduction | 800 |
| II | The Architectural Tax of Hybrid Vertical Flight | 1 000 |
| III | The meryemAircraft Configuration | 1 200 |
| IV | The Price Paid: Drag, Mass, and Power | 1 500 |
| V | Sizing, Scale, and Contract Dependency | 1 500 |
| VI | Transition, Trim, and the Open Items | 1 200 |
| VII | Conclusions | 300 |

**Distinctive:** the strongest dissent on the centre — *"the true centre of this work
is the accounting framework itself. The configuration is the stress-test that proves
the framework is honest."* And the strongest endorsement of the Bacchini work: *"the
sharpest piece of aerodynamics auditing in the entire paper… you turned a literature
gap into a definitive boundary condition."* Qwen also drafted a full 168-word
abstract, the only one to do so.

### 5.4 ChatGPT

**Budget:** 7 500 words, 6 figures, 8 tables.

| § | Title | Words |
|---|---|---:|
| 1 | Introduction | 900 |
| 2 | **Architectural Concept and Contribution** | 1 100 |
| 3 | Architecture-Cost Framework and Verification | 1 450 |
| 4 | meryemAircraft Configuration and Analysis | 1 350 |
| 5 | Results: What the Architecture Buys and Costs | 1 550 |
| 6 | Limits, Sensitivities, and Scope of Claims | 750 |
| 7 | Conclusions | 400 |

**Distinctive:** **explicitly against a separate Methods section** — *"it shifts the
story back to the calculation centre."* §2 is named the heart of the paper and holds
the claims/non-claims table before any calculation appears. And the narrative chain
in §4.7 above, which the author has endorsed.

### 5.5 Claude

*Written before the others arrived; commit `38a919d`, unchanged.*

**Budget:** 7 450 words, 6 figures, 8 tables — closing the 12 000 limit exactly, with
objects priced at their real two-column cost (450 and 700), not all at 200.

| § | Title | Words | Figs | Tables |
|---|---|---:|---|---|
| 1 | Introduction | 900 | F1 | T1 |
| 2 | The architectural tax | 1 200 | F2 | T2 |
| 3 | **The framework against data it did not produce** | 650 | — | T3 |
| 4 | The configuration | 1 300 | F3, F4 | T4 |
| 5 | What the union costs | 1 650 | F5 | T5, T6 |
| 6 | Rankings belong to contracts, not to architectures | 850 | F6 | T7 |
| 7 | What is not closed | 600 | — | T8 |
| 8 | Conclusions | 300 | — | — |

**Distinctive:** a **separate section for external validation** (§3) — the NASA
sizing set and the Bacchini measurement together, on the argument that *"the answer
to 'did the authors fit the theory to their own aircraft' deserves its own
heading."* And Table 4 as a **mechanism inventory**: what does not exist against what
does. I also listed four weaknesses of my own proposal, including that §5 is too
narrow at 1 650 words to carry three bills.

---

## 6. Where you converged, and where you did not

**Unanimous:** Full-Length Paper · *Journal of Aircraft* · keep `meryemAircraft` in
the title with the same formula (name + tail-sitter + without propulsor
reorientation) · no citations in Conclusions · the battery number in the body and
the abstract with the calculation in the supplement · the Bacchini
freedom-versus-alignment finding stated as a result, not a correction.

**Structurally almost identical:** every proposal runs introduction → architectural
tax → configuration → what it costs → contracts → limits → conclusions. The
differences are weighting and placement, not order.

**Split 1 — the centre.** Grok and ChatGPT with the author; DeepSeek two
contributions; Qwen the framework. **Section 2 above shows part of this was my
wording, not a real disagreement** — but not all of it, and Qwen's warning stands on
its own.

**Split 2 — a Methods section.** Grok yes, on AIAA's accuracy policy. ChatGPT
explicitly no. DeepSeek and Qwen fold it in. One against three, and Grok's reason is
good.

**Split 3 — how many objects.** Grok alone says 5 and 7, with slack. Everyone else
6 and 8. **And there is an arithmetic error worth naming:** Qwen computed 14 objects
at 200 words each for 2 800, and DeepSeek priced six figures at 1 200. AIAA charges
**450 for a two-column object and 700 for a large two-column table.** Several of
these objects will be two-column. Grok is the only one who priced the risk.

---

## 7. What we are asking for this round

**The coarsest general flow of the argument. Nothing else.**

Not sections with budgets. Not figures. Not tables. **The shape of the narrative** —
the order of the moves that make a reader understand what was invented and why it
holds. Eight to twelve beats is about right. Name each beat in a few words. Say in
one line what it does.

Three things it must respect:

1. **The novelty is the main flow and is not overshadowed** — and the calculations
   built over all these rounds go in, properly, in their right place. Both. This is
   the author's correction to my Round 29 framing.
2. **The combination is a move in the argument, not a by-product.** The author's own
   sketch makes "combining the solutions" its own beat. None of our five contents
   lists did. Consider whether it should be one.
3. **The claim structure holds:** cruise efficiency against multirotors; runway
   independence against fixed-wing; the propulsor-reorientation mechanism class
   against tilting architectures; **no range claim against the other hybrids.** And
   the third claim stays narrow — the strip moves, and nothing here says "mechanically
   simpler", which was never measured.

If having read the others you want to change your Round 29 position, change it and
say what changed it.

---

## 8. Next round

**Objections and support.** Everything written this round goes to all four of you
again, and you will be asked what you object to and what you endorse, by name. The
flow that survives that round is the flow v8 gets written to.
