# Round 31 — the last round was contaminated. By me. We are doing that step again, properly.

---

## 0. What went wrong, and why we are repeating a step

**The fault is mine and it is specific, not general.**

In the Round 30 briefing I wrote that the author had **endorsed** ChatGPT's narrative
chain. He had not. What he said, in his own words, was that ChatGPT *"grasped the
matter well."* That is an observation about one reader's understanding. I turned it
into a decision the author never made.

**It propagated, and the evidence is in your own replies.** DeepSeek wrote: *"ChatGPT's
chain. I agree with the chain, **and the author has endorsed it**."* Grok listed *"What
I endorse — ChatGPT's chain"*. You were told the author had blessed one shape before
you proposed yours. Whatever you would have written independently, we cannot now tell
it apart from what you wrote against a shape presented as already approved.

**That is why the step is being repeated.** Not because your answers were poor — several
of them were the best work in thirty rounds — but because the input was corrupted and
a corrupted round cannot be the foundation of the paper.

**Nothing from Round 30 is adopted. Nothing is rejected.** No flow is preferred. No
chain is blessed. The author has decided none of it. Your Round 30 answers are kept in
the record and you may reuse or abandon them freely.

**And a second correction, from the same source.** Earlier I told you the centre was
the configuration and that *"everything else is either the accounting or the price."*
That made the framework sound instrumental and it is not the author's position. His
position, plainly:

> The main flow — the part that must not be overshadowed — is **the novelty being
> described.** And the calculations built over all these rounds go in too, properly, in
> their right place. **Both.** There is no conflict here and there never was.

DeepSeek said in Round 30: *"The framing I responded to was not the author's."* Correct.
It was mine.

---

## 1. Settled. Do not spend words on these.

- **Full-Length Paper**, *Journal of Aircraft* (AIAA). Closed.
- **Title, provisional:** `meryemAircraft: A Tail-Sitting Blended-Wing Body Without
  Propulsor Reorientation`. No one objected in Round 30. Closed unless something new
  arises.
- **Word budgets, figure counts, table counts, section lengths.** **Not this round.**
  They are recorded, they are settled arithmetic, and they get built on top of a
  structure once there is one. Raising them now is what took us off course before.

---

## 2. What is being asked, and why

**The question: what are the milestones this paper must contain?**

In the author's words:

> *"Makalede olması gereken milestone'lar nelerdir? Bunları listeleyin. Önce anlatım
> başlıkları veya ana hatlar neler, onları konuşmamız gerekiyor. **Kaba iskelet olmadan
> yapay zekâya yazdırınca ortaya büyük bir balon çıkıyor.**"*

— *What are the milestones the paper must have? List them. First we need to discuss
what the narrative headings, the main outline, are. Without a coarse skeleton, letting
an AI write produces a big balloon.*

That last sentence is the reason for the whole exercise. A paper written before its
skeleton exists inflates: every calculation argues for its own inclusion, every section
grows to hold what was computed, and the thing that was actually invented ends up
somewhere in the middle of it. That is exactly what v7 became at 36 000 words, and it
is what we are not going to do again.

**A milestone here means: a point the paper must reach for the argument to stand.**
A named waypoint. Not a section with a budget. Not a heading with figures assigned.
The list of things that must be established, in the order they must be established, so
that a reader arrives at the end convinced.

**What a good answer looks like:** a numbered list. Each item a few words as a name,
then one line saying what it establishes and why the argument fails without it. Around
eight to twelve items. The author's own one-second sketch, offered only as a shape and
not as a template to copy:

> introduction · the current situation · the solution to this problem · the solution to
> that problem · the combination of the solutions · the soundness of the resulting
> product · the calculations we have · conclusion

**What we do not want:** word counts, figure or table assignments, section budgets,
abstract drafts, title debates. All of it later.

---

## 3. What must hold, whatever shape you propose

These are the author's, not conclusions borrowed from another reader.

**The novelty is the main flow and must not be overshadowed — and the calculations go
in, properly, in their right place.** Both. Any list that sacrifices one for the other
is answering a question nobody asked.

**The claim structure, four axes and four different opponents:**

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency and range | **Multirotors** | Claimed. Sufficient. |
| Runway independence, vertical operation | **Fixed-wing** | Claimed. |
| **Absence of a propulsor-reorientation mechanism** | **Tilting architectures** | **The contribution.** |
| Range against the other hybrids | Lift-plus-cruise, tilt | **Not claimed.** |

Two errors this project has already made and will not make again: **racing a fixed-wing
aircraft on range** — nothing outruns a glider, and beating a multirotor on distance is
enough — and **racing a multirotor on vertical take-off**, where the opponent is
fixed-wing.

The union is therefore stated as: **runway-independent vertical operation combined with
wing-borne cruise efficiency.** Not "the range of a fixed-wing aircraft." I wrote that
phrase in Round 29 and two of you caught it; it is the first of those two errors and it
is now a standing prohibition.

**The third claim stays narrow.** What is eliminated is the *class of mechanism that
reorients a propulsor* — pivot, nacelle actuator, variable-pitch hub, gyroscopic moment
from a tilting mass. It is **not** a claim that nothing moves: roll cannot be produced
by coaxial torque-balanced pairs at all and comes from one variable-extension strip,
which is the only moving aerodynamic surface on the aircraft and which also pitches the
nose down. And it is **not** a claim of mechanical simplicity — part count, mass, failure
modes and maintenance were never measured. It is a count of eliminated mechanism
classes.

**"By construction" is used carefully.** The design *sizes* vertical operation.
Transition and flight feasibility are not demonstrated.

---

## 4. Verification

Repository: `https://github.com/LORDTEK/meryemAircraft`

The current manuscript, byte-identical to its Zenodo deposit (DOI
`10.5281/zenodo.22745666`), SHA-256 beginning `c5b0cd898d20`, today at
`paper/paper-v7.md`. Pinned to the commit it was submitted from:
`https://raw.githubusercontent.com/LORDTEK/meryemAircraft/e45d43c/makale/makale-v7.md`

Everything named in this briefing — the AIAA requirements, the word arithmetic, the
Bacchini reading, my errors — is in `paper/` and `cfd/` on the current branch.

**My own milestone list is written and committed before this briefing was sent, and is
deliberately not in this document.** Putting it here would repeat the anchoring mistake
that caused this round. It will be shared with yours next round, on the same terms, and
you are free to take it apart.

---

## 5. How this round and the next one work

**This round:** each of you produces a milestone list. Independently. You have not seen
each other's.

**Next round:** every list, including mine, goes to all four of you in full, attributed.
You read all of them and comment — what you object to, what you endorse, what you would
change in your own after reading the others.

**Then, and only then**, the structure that survives becomes the skeleton v8 is written
to. After that, and not before, come the section budgets, the figures and the tables.

The author's instruction for the whole process is one word: **slowly.**

---

## 6. One request about how you answer

If something in this briefing is wrong — including the claim structure, including the
author's position as I have stated it here — say so. I have now misrepresented the
author to you twice in three rounds, both times by making his position sharper or more
decided than it was. If a sentence here reads as too clean, it may be me again.
