# Round 206 — The fairing sentence (S-66): five repair wordings side by side; the S8 qualification text

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text.

---

## A. Closed in Round 205 (all four, and me)

- **P09, P11, P12, P13:** R1.
- **The flagged S6 and S8 changes** are accepted:
  - the four blade families with their efficiencies;
  - *"across its four closures"*;
  - the explicit spanwise extent of the strip.
- **S-66 is a defect.** The body's *"less than a 20 mm faired strut carries in any case"* is not supported: at a slope of 3.0 per radian the chord is 52 mm, inside the assumed 50 to 70 mm. It is entered in the source-defect register. Its repair wording is in §B.
- **C1 (a):** the NACA qualification goes into S8, not only into the evidence file. The text is in §C.
- **Grok's rounding note on P12:** 3,665 lb is 1,662 kg, and the protected wording *"1 660"* rounds it. No change.

---

## B. The body sentence: five wordings, please answer each other

**The sentence as it stands** (Section 5.2, *"What meets the ground"*; not protected), with the sentence after it, which depends on it through *"therefore"*:

> **The frames carry a fairing, and it is not only a drag measure**: a planar planform supplies no directional stability, so the fairing is the aircraft's only vertical surface, and sized against the criterion the tailless literature recommends it needs a chord of **39 mm**, less than a 20 mm faired strut carries in any case (Supplement S8). Directional stability on this configuration therefore does not ask for a surface; it asks for a fairing on a frame that is already there.

**The working (Supplement S8):**

| Slope | Chord |
|---:|---:|
| 3.0 per radian | 52 mm |
| 4.0 per radian | 39 mm |
| 5.0 per radian | 31 mm |

The 50 to 70 mm for a 20 mm faired strut is assumed, not sourced.

**The five wordings** (each replaces the part from *"it needs a chord"* to *"(Supplement S8)."*):

| Reader | Wording | What it does against the working |
|---|---|---|
| **Grok** | *"…needs a chord of 39 mm at an assumed lateral lift-curve slope of 4.0 per radian, and 31 to 52 mm from 5.0 to 3.0; a 20 mm faired strut is taken to carry 50 to 70 mm, assumed rather than sourced."* | Names the slope, the range and both assumptions. It does not say how 31–52 stands against 50–70 and leaves that comparison to the reader. |
| **ChatGPT** | *"At an assumed lateral lift-curve slope of 4.0 per radian, the fairing needs a chord of 39 mm, within the 50 to 70 mm range assumed for a 20 mm-thick faired strut."* | Names the slope and marks the strut range as assumed. **39 mm is below 50 mm, not within the range**, so *"within"* does not match the working at 4.0. |
| **DeepSeek** | *"…it needs a chord of 39 mm at an assumed lateral lift-curve slope of 4.0 per radian, below the 50 to 70 mm a 20 mm faired strut carries (Supplement S8)."* | Names the slope, and *"below"* is true at 4.0. *"A 20 mm faired strut carries"* states the assumed range as a fact, and the 3.0 case is left to the supplement. |
| **Qwen** | *"…the chord required over the combined frame length is 39 mm, no more than the 50 to 70 mm that a 20 mm faired strut carries."* (with the slope and the sensitivity in S8) | Short. The slope is not in the body. *"No more than the 50 to 70 mm"* can be read as no more than 50 mm, which 52 mm at 3.0 exceeds. |
| **Claude** | *"…it needs a chord of **39 mm** at an assumed lateral lift-curve slope of 4.0 per radian (Supplement S8). Across slopes of 5.0 to 3.0 per radian the chord is 31 to 52 mm, within or below the 50 to 70 mm assumed for a 20 mm faired strut."* | Names the slope and the range, marks the strut range as assumed, and states the comparison at all three slopes. It is longer: one sentence becomes two. |

**What all five keep:** the 39 mm, and the sentence after it. At every slope the chord is still that of a fairing on a frame that is already there, so *"therefore does not ask for a surface"* still follows. Grok noted this explicitly.

**Please:**
- Answer each other's wordings, mine included. Each comment in the third column is a reading against the working, not a verdict. If one is wrong, say so.
- Say which wording you accept. Two wordings may be merged.
- The sentence is not protected, so this does not go to the author unless we fail to converge.

**Qwen, one check.** You graded P14 R1. Under C2 you judged the body's *"in any case"* an R4 risk and voted to change it. Does the R1 stand, or is it R4 like the others?

---

## C. S8: the qualification text (C1), drafted

All four and I chose (a). Grok and DeepSeek asked for both qualifications, the one-third note and the tip-fin sentence. ChatGPT listed both as relevant but proposed quoting the tip-fin sentence. Qwen proposed the tip-fin sentence. The draft carries both and is appended to the S8 fairing paragraph:

> The same report qualifies the criterion in two ways. Models were flown in the Langley free-flight tunnel with one-third of that value, though the best flying qualities came above it; and when fins stand at the wing tips, the moment arm of their drag is half the span, so that *"the drag characteristics as well as the lift characteristics of the tip fins exert an influence on the directional stability"* [24]. The chord derived here counts the frames' side force only.

**Source check this round:**
- The quotation is verbatim in NACA Report 796 (p. 428). NACA ACR L4H19, the earlier issue of the same text, has the same wording.
- The context sentence before it reads: *"When vertical fins are placed at the wing tip extremities, however, the moment arm associated with the drag of the tip fin is so large (one-half the span) that …"*. The draft paraphrases it without quotation marks.

**Please:**
- **ChatGPT and Qwen:** is the one-third note acceptable to you?
- **All:** does the draft add a claim the body does not make or promise (ChatGPT's rule)? Does *"counts the frames' side force only"* say exactly what the working does?

---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Claude:** in Round 205 I wrote that the p. 71 → p. 70 correction was made *"in both places"* (the S4 note and the S-64 row). **The S-65 row also said p. 71.** Corrected now. This is the propagation rule (Q-P2: when a value is corrected, every record stating the same fact is listed), and I did not run it.
- **Readers:** none found in Round 205.

---

## F. What goes to the author

**Nothing this round.** The fairing sentence goes to the author only if the five of us do not converge on a wording.
