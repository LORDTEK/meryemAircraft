# Round 23 — the full record. What was claimed, by whom, whether it was true, and what was done.

**Read it whole, then in parts.** This is the longest of these documents because it
is the first one that tries to be a complete account rather than a status report.
The author asked for it in those words: *who claimed what, were they right, was it
worth anything, what was done about it, and how did the paper get here.*

**You have one file: `makale-v6.md`, the main text, 33500 words — and it is
the corrected build, rebuilt after every item in Section 3 below was applied.** You
do not have the supplementary document (six files, 32 400 words), the figures, or
the code. The main text carries **figure citations but no figure captions**, and it
carries **all 22 table captions**. Where something below depends on a figure you
cannot see, the figure is described.

---

## 0. Credit, and it is not close

**Qwen has spent more thinking on this paper than any other reader, across four
rounds, and it shows in the kind of error it finds.** This is said plainly because
it should be said.

Round 19: Qwen objected that Section 3.9's *explanation* of the scale behaviour was
arithmetically false. It was. Chasing it found a code defect — a chord limit written
in absolute metres and applied to a rotor three times the radius it was chosen for —
that had manufactured a physical finding all four readers had then flagged as a
submission blocker. **The finding was withdrawn. That one objection changed the
paper more than any other single sentence written by anyone.**

Round 20: Qwen noticed the dual-use statement still said "near 1800 km" after the
heavy range moved. Trivial-looking. Fixing it exposed four mandatory declaration
blocks missing from the built PDF entirely.

Round 22, the round just closed: Qwen was the only reader to name the *class* the
round's errors belonged to — "labels and pointers that no longer match their
referent," living in the connective tissue rather than in the results — and to
propose the mechanical check that would catch them. **That check has now been built
and is in the repository.** See Section 4. Qwen also caught a one-kilometre
self-inconsistency inside a sentence whose entire purpose was to assert that two
numbers agreed.

The pattern worth copying: **check an arithmetic or internal-consistency claim the
paper makes about itself; if it fails, do not accept the replacement without
measuring it.**

---

## 1. The paper, in two hundred words

Hybrid VTOL aircraft pay for runway independence in cruise efficiency. The paper
treats that as *architectural* and builds an accounting framework: the penalty is
charged in three coupled currencies — **Bill 1**, hover hardware carried as dead
mass; **Bill 2**, its drag when exposed; **Bill 3**, continuous power sized by a
condition holding some two percent of the flight. Every remedy surveyed reduces one
by raising another. Escape requires four things at once: the same hardware, in the
same orientation, doing the same job, with the hover peak from a buffer.

**Headline: architectural rankings belong to sizing contracts, not to
architectures.** Three contracts are reported and the ranking reverses between them.

The case is an uncrewed tail-sitting blended-wing body — one coaxial nose pair for
both regimes, four counter-rotating pairs at the tips for attitude, no elevons, no
rudder, no tilt, no dedicated lift system — instantiated at 50 kg and 1000 kg and
carried far enough to show what instantiating the escape condition costs. What it
costs, principally, is the free-wheeling drag of its own attitude rotors: a bill the
configuration was assumed to avoid, and charging it reverses one of the three range
comparisons.

Not claimed: that the aircraft is flyable, or that any architecture is generally
superior to any other.

---

## 2. How the paper got here — the whole arc, briefly

Twenty-two rounds. The turns that changed the paper rather than tidied it:

| Round | What changed, and who caused it |
|---|---|
| early | Framework built; three bills; four-part escape condition |
| 14–16 | Three sizing contracts introduced. **The ranking reverses between them — this became the headline** |
| 17 | Section 5.5's table found to be a *source's* table with the column headings changed. The single-file builder was written so a hand-assembled document could never drift again |
| 19 | **Qwen:** Section 3.9's mechanism is arithmetically false → chord-clip code defect → the "heavy design cannot hover" finding **withdrawn** |
| 20 | **Qwen:** stale dual-use range → four mandatory declaration blocks found missing from the built PDF |
| 21 | First end-to-end reading by anyone. Bibliography verified against the deposit, 51/51 |
| — | **v6 deposited on Zenodo.** DOI 10.5281/zenodo.22144194 |
| 22 | **The author**, against the model: a scope sentence inserted into the Introduction denied the paper's own earned claims. See Section 3.1 |
| 22 | **ChatGPT:** figures print out of order in the Word file → renumbering → a figure that contradicted the paragraph above it |
| 23 | **This round.** Eighteen corrections, below |

Two findings recur often enough to be the project's characteristic failure mode:

1. **A corrected number leaves an uncorrected twin somewhere else.** Three times now.
2. **A label, pointer or count stops matching its referent and no number-checking
   pass notices**, because nothing arithmetic is wrong.

---

## 3. Round 22 in full: every claim, whether it held, and what was done

Four readers. **Sixteen distinct claims.** Twelve held, four did not. Every one that
held has been acted on.

### 3.1 The claim that mattered most came from the author, not from any reader

While tightening the Introduction I inserted *"No claim of general architectural
superiority is made."* The author objected: *we have an architectural superiority
claim — it is why this configuration exists. It needs no runway and it goes far
beyond a multirotor.*

**He was right.** The sentence denied the two claims the paper earns while
disclaiming a third it never made, and it contradicted Section 4.2 of the same
document. **No reader caught this in three rounds of reading the same Introduction.**

**Done:** the passage now separates three claims by status — escapes the runway
requirement (sound); cruises on a wing, which a multirotor does not (sound); a
ranking against the other hybrids (*not* claimed, because Section 3.6 shows it
reverses with the contract). All four readers then attacked the repair, correctly —
see 3.2.

### 3.2 All four readers, independently: the 4.9 versus 8.8–10.8 comparison is not fair

**Held, unanimously, and it was the most valuable consensus of the round.** The
repair quoted a turboshaft quadrotor's *effective* L/D of 4.9 against this
configuration's *aerodynamic* 8.8–10.8. Different kinds of number: one a system-level
figure of merit, the other a force ratio, from different studies at different
fidelities and masses. DeepSeek and Grok said cut the numbers from the Introduction;
ChatGPT said reword the claim; Qwen said the comparison is legitimate but the label
is missing.

**Done, taking all four:** the claim is now stated structurally — *lift in cruise is
carried by a surface rather than by rotors, and that is a structural difference
rather than a margin* — the numbers are kept but explicitly labelled as different
kinds and offered "for scale rather than as a measured margin," and **Qwen's
criterion is now written into the paper**: the line between claim 2 and claim 3
tracks *whether the competitor has a cruising wing at all.*

### 3.3 DeepSeek, Grok and Qwen, independently: the section pointer is wrong

**Held.** Two places — the Introduction and Section 4.2 — pointed the NASA sizing set
to **Section 3.2**. Section 3.2 is *Bill 1 — mass* and contains neither the number
4.9 nor the word quadrotor; the set is in **3.1**. Three readers, same catch,
independently.

**Done:** both fixed, and a guard now resolves every section pointer in the document
(Section 4).

### 3.4 Grok alone: Table 8 still compares two different drag bases

**Held, and this was the most serious single finding of the round.** Three paragraphs
above Table 8, the paper retires a 37 % mass advantage because it compared *"this
configuration with its rotors charged, at 54.5 kg, against a lift-plus-cruise layout
at 86.0 kg sized on the uncharged drag — on two different aerodynamic bases."* **Table
8's own 4 % row is 54.5 / 86.0 / 60.3.** The same pairing, one table lower, still
live — and Tables 7 and 10 are built from the same run.

**Verified by re-running the sizing script.** Its output is explicit: in the
"new drag" block A moves from 50.0 to 54.5 kg while B stays at 86.0 and C at 60.3.
The new drag is applied to A only. Grok is exactly right. **Three readers missed it.**

**Done:** Tables 7, 8 and 10 now carry captions stating the mixed basis and naming
Table 9 — the bracket sweep, which re-solves all three on a common basis — as the
reportable form. The qualitative conclusion drawn from Table 8 is explicitly
restricted to a direction rather than a margin, with the reason it survives the basis
change stated (B's hover power per unit mass is the highest of the three, and that
ordering does not depend on the drag assumption).

### 3.5 DeepSeek and Qwen: two caption counts do not match their tables

**Held, both.** Table 1's caption said "four configurations"; the table has **three**
rows. Table 4's caption said "four designs"; the table has **seven**. Both were
written by the model in one pass the round before. The prose carried the same wrong
counts.

**Done:** caption and prose corrected in both; Table 4's caption now also says that
shaft speed and tip Mach were not recorded for the two designs added by the later
solver-stability sweep, which is why two rows show a dash.

### 3.6 DeepSeek, ChatGPT and Grok: Table 18 presents the coarse-mesh answer as the result

**Held.** Table 18 gives K_L = 0.787 with no qualifier; Table 19, two paragraphs
later, shows the converged value is 0.796 and that the coarse mesh *"was smoothing
the loading and making the agreement look better than it is."*

**Done:** Table 18's caption now says "on the initial 192 000-cell mesh" and names
0.796 as the converged value in the caption itself.

### 3.7 Qwen: a self-check that fails its own stated value by one kilometre

**Held.** Table 14's note asserted it reproduces *"the 13.6 and 1 814 km of the table
above"* — while Table 14's own published row read 1 813.

**Done:** 1 814 is the authoritative value (Table 13 carries it and the numerical
guard re-derives it), so Table 14's row was corrected. Small, but it sat inside a
sentence whose only job was to assert two numbers agreed.

### 3.8 DeepSeek: the Conclusion's thrust-to-weight range covers one design only

**Held.** Section 5 said *"between 1.066 and 1.132"* — the light design's span. The
heavy design is 1.041 to 1.082.

**Done:** all four values now stated.

### 3.9 Qwen: Section 3.3 says something false about its own document

**Held.** Section 3.3 said the margin narrows *"by an amount this paper has not
re-sized."* Section 3.6 re-sizes exactly that margin and reports it.

**Done:** now reads "by an amount Section 3.6 re-sizes."

### 3.10 ChatGPT: a sentence contradicts itself mid-clause

**Held — and ChatGPT found it while reading the wrong file.** *"Against tilt it no
longer leads at all: with the rotor term charged it leads under all three rules."*
The subject silently flips.

**Done:** both subjects named explicitly.

### 3.11 DeepSeek: three gaps a reviewer will find

**All three held.**

- **Sea-level cruise is assumed and never justified.** A 1600 km mission at sea level
  is unusual and the paper had no answer prepared. **Done:** a paragraph now states
  that it is the *conservative* choice (altitude would lengthen every range figure),
  that it matches the intended missions — wildfire observation and cargo to sites
  without a runway, both flown low — and that it keeps hover and cruise on one
  atmosphere so the ratio between them is not also carrying a density change.
- **The reverse transition is assumed and never analysed.** Six subsections treat the
  forward transition; the reverse got a clause. **Done:** the paper now states plainly
  that the two are *not* symmetric — the forward rotation builds dynamic pressure
  while it turns, so lift arrives as the vertical thrust component departs, and the
  reverse runs that race backwards — that no figure here describes the landing
  transition, and that none should be inferred from the take-off one. Added to the
  open-items section as well.
- **Tip-pair disc loading not stated.** **Done:** 26.3 kg m⁻², computed and added to
  Table 11.

### 3.12 ChatGPT: "0.0248 is self-consistent rather than optimistic"

**Held**, though ChatGPT reached it from the wrong file. Section 3.10 computes the
bracket at 0.0285–0.0381 and the assumption lies below both ends, so calling it
self-consistent is no longer defensible.

**Done:** the claim is withdrawn in the assumptions list — *"it is an assumption and
an optimistic one, not a self-consistent choice"* — and the reason is stated there.

### 3.13 The four claims that did NOT hold — all from ChatGPT, all the same root

ChatGPT's headline finding was *"the file you were given is not the corrected build."*
**It is false, and so are its four supporting claims.** Checked directly against the
file:

| ChatGPT claimed | Actual |
|---|---|
| The old "No claim of general architectural superiority" sentence is still there | **Absent.** The three-claim passage is present |
| Only Table 1 and Table 4 have captions | **All 22 captions present** |
| Raw LaTeX still passes through unrendered | **Zero occurrences of `$$`** |
| §3.10 and §4.5 carry the old bracket 0.0216–0.0380 | **The string "0.0216" does not occur anywhere in the file** |

It also reported 2 711 lines; the file has 2 809. **ChatGPT was reading the deposited
Zenodo v6, not the attached file** — or reconstructing from the previous round. Grok
independently reported the exact word count of the attached file, and DeepSeek's and
Qwen's findings match it line for line, so three of four read the correct document.

**This is recorded without prejudice.** ChatGPT still found a real defect nobody else
found (3.10) and was independently right about 3.12. **A reader working from a stale
copy can still be right; but a confident claim about what a file contains is checkable,
and should be checked before it is led with.**

### 3.14 What the readers could not have found, and the code did

Chasing 3.4 into the scripts turned up **an error no reader had access to**, and it
runs against the paper's own convenience.

Section 3.8 carries a heavy-line rotor drag charge of **0.0051**. Re-running the
script showed its stated selection rule — *among blade designs meeting the hover
figure-of-merit requirement, take the least draggy* — selects **0.00446**, and that
0.0051 belongs to a design **not in the swept list at all**.

Widening the sweep exposed the real problem, which is worse than a wrong number.
**In the light line the rule binds:** the figure of merit collapses from 0.633 to
0.350 above a target section lift coefficient of 0.68, so the cliff selects the
design and the 0.0154 of Section 3.3 is pinned by physics. **In the heavy line there
is no cliff** — the figure of merit is still 0.657 at a target of 0.85 — so the same
rule selects whichever design sits at the end of whatever range happens to be swept.

Applying the rule literally would have returned **0.0035**, the lowest charge, which
is **the end favourable to this configuration.** That is precisely why it was not
done silently.

**Done:** Section 3.8 now reports the charge as **bounded by 0.0035 and 0.0074, not
pinned within that interval by any criterion this study applies**, states that 0.0051
is the interior value the sizing was run at rather than a minimum, and notes that the
charge stays between a third and a half of the light design's at every point in the
interval — which is all Section 3.9 needs. The numerical guard now re-derives both
ends and asserts the carried value lies between them; it never checked this quantity
before.

---

## 4. What was built so this class of error cannot recur silently

Qwen's Round 22 closing paragraph proposed the check. It now exists:
`makale/uretim/baglanti.py`, the connective-tissue guard. It verifies that

- every `Section N.M` reference resolves to a heading that exists;
- every `Table N` and `Figure N` citation resolves to a definition, and every
  definition is cited;
- and it lists every caption whose number-word disagrees with its table's row count,
  **as an advisory rather than a failure** — because "one uncrewed airframe" and
  "eight tip discs" are legitimate numbers that count nothing, and a guard that
  cannot tell the difference should say so instead of pretending.

Run against the pre-correction document, it flags 3.3, 3.5 and the figure ordering.
It cannot flag 3.1 — a scope sentence that denies the paper's thesis is not a
mechanical defect, and no script will ever catch it. A person did.

The numerical guard now runs **43 checks** including the heavy-rotor interval, plus
a forbidden-value list of nine superseded numbers across twelve source files.

---

## 5. Open items — unchanged, none closed this round

1. **The battery buffer.** The 50 kg design needs a specific power about **3.8 times**
   the highest rate yet measured on a production cell. The paper says so. The aircraft
   is not shown to be flyable and does not claim to be.
2. **The transition rests on a pitching-moment coefficient no current method predicts
   reliably.** At zero aerodynamic pitching moment the light design loses 5.4 m where
   the kinematic model reports zero; with a borrowed moment the spread is wide enough
   that no number from it is reportable.
3. **Take-off margin and attitude authority are drawn from the same four propellers
   and cannot both be had in full.**
4. **The landing transition is unmodelled** — newly stated this round rather than
   newly true.
5. **No wind tunnel, no flight test.**

---

## 6. What we want from this round

**1. Read the repairs, not the paper you remember.** Eighteen corrections landed in
Sections 1, 2.3, 2.12, 3.3, 3.6, 3.8, 3.10, 3.16, 4.2, 4.6 and 5. Several were
written fast. **Attack the new prose specifically** — the three-claim passage, the
sea-level justification, the heavy-rotor interval paragraph, and the mixed-basis
captions on Tables 7, 8 and 10.

**2. Is the heavy-rotor interval the right call?** We could have reported 0.0035 and
been consistent with our own rule. We reported an interval and kept the higher
interior value instead. Tell us if that reads as over-caution, or as the only honest
option, or as a third thing.

**3. Is Table 8 now adequately handled, or does it need to come out?** Labelling a
table as resting on a retired basis is not the same as fixing it. Recomputing the
buffer sweep on the common basis is possible but touches the sizing chain. Grok found
the defect; all four should now say whether the label suffices for submission.

**4. Stale twins, again.** Two were found this round after twenty-one rounds of
looking. The corrected values are: bracket 0.0285–0.0381; L/D 8.8–10.8; mass advantage
32–36 %; T/W 1.066 / 1.041 / 1.132 / 1.082; heavy range 1 571 km charged and 1 814 km
published; K_L 0.796; heavy rotor charge 0.0035–0.0074 carrying 0.0051. **Search for
older values of any of these.**

**5. Is it ready for *Drones*?** None of you said yes last round; all four gave a
must-fix list, and all four lists have now been worked. Say yes or say what is left.

**6. What have twenty-three rounds collectively missed?** The last two rounds'
sharpest findings came from a reader working alone on one table (Grok), from a human
reading a single sentence (the author), and from a script nobody had run (3.14). None
came from consensus.
