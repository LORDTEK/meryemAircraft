# Round 209 — S-67: five wordings for the loop sentence; S10 closed apart from it; a short round before S11–S14

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text. No packet is attached this round; nothing here needs it.

---

## A. Closed in Round 208 (all four, and me)

- **The author's question: all four have now answered.**
  - **Nothing is missing** for any of you for the current work.
  - **The archive passages will be needed for S11–S14.** Grok, DeepSeek and Qwen said so.
  - **Windows:**
    - ChatGPT and Qwen: no strain.
    - Grok: *"long, not blocked"*; a fresh conversation *"would help before those four sections if the packet keeps growing."*
    - DeepSeek: handling it for now; a fresh conversation *"would help at the S11–S14 stage."*
    
    How that is done is the author's call (§D).
- **The S2–S8 check against the whole body: all four pass.** No passage adds a claim the body does not make or promise.
- **DeepSeek's two packet statements:** DeepSeek checked both and withdrew them. Recorded in §E as DeepSeek reported it.
- **The S8 ending stays as drafted** (*"counts the frames' side force only"*). Qwen accepts. Closed.
- **P14: R1** (Grok, ChatGPT, Qwen, me). **DeepSeek, please confirm in one word.**
- **S10:**
  - **P17 and P18: R1**, all four.
  - **The two archive corrections** (MTOW^1.5; the 7 and 5 percent): accepted by all four.
  - **The gain sweep stays in S10**, all four. Following ChatGPT, the provenance note now says it is a new sensitivity run whose design was chosen this round, not a reconstruction of the archived sweep. Following Grok, 16.9 m stays out of the body.
  - DeepSeek offered a qualitative-only form, *"raising the gains increases the loss rather than removing it"*, without the number, and left the choice open. The draft keeps the number with its design stated. **DeepSeek, is that acceptable?**
- **S-67 is a defect, all four.** P16 is R4 as the body stands, and R1 once repaired. The wording is in §B.

---

## B. S-67: five wordings, please answer each other

**The body sentence now** (Section 6.1, P16; not protected):

> Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10).

**What the loop does** (S10, as drafted and accepted for P17 and P18):

> The closure statement is MTOW = m_payload / (1 − f_empty − f_fuel), with the fuel fraction fixed at 0.16. The empty fraction contains a propulsion term, f_prop = 0.108 + P_engine / (p_s · MTOW), in which the engine rating P_engine is 1.53 times the cruise electrical power at the take-off mass and p_s, 1.0 kW per kilogram, is the specific power assumed for the engine and generator. The take-off mass is found by iteration as the fixed point of that loop: mass sets the cruise power, cruise power the engine rating, the engine rating the propulsion mass, and the propulsion mass the take-off mass. The rest of the propulsion mass, the fixed 0.108, is a fraction back-solved from the reference design's own budget. Hover power … is computed at the closed mass and reported, and it does not size the engine. Because the disc loading is fixed, hover power is itself proportional to take-off mass, so any mass that scales with hover power scales as a fixed fraction does; the loop computes no hover-rated mass of its own.

**Section 6.2 already says:** *"The engine is sized by cruise … But the full hover power passes through the electrical path, and that path is sized by it."*

| Reader | Wording | Reading against the code and Section 6.2 |
|---|---|---|
| **Grok** | *"Cruise power sets the engine rating, the engine rating the propulsion mass, and the propulsion mass the take-off mass; the take-off mass is found by iteration as the fixed point of that circle. Hover power is computed at the closed mass and does not size the engine; the electrical path, which the hover power sizes, enters the loop as a fixed fraction of take-off mass (Supplement S10)."* | The loop is right. The second sentence says the electrical path *"enters the loop as a fixed fraction"*. The code does not say that: its comment for the 0.108 lists propeller, shaft, mount and wiring, and no line of the code identifies the electrical path with it. The sentence would add an identification the working does not make. |
| **ChatGPT** | *"Take-off mass sets the cruise power, cruise power the engine rating, engine rating the propulsion mass, and propulsion mass the take-off mass; the take-off mass is found by iteration as the fixed point of that loop (Supplement S10)."* | Matches S10 word for word in order. It says nothing about hover power; Section 6.2 carries that. |
| **DeepSeek** | *"Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the **cruise power** that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10)."* | One word changed, so the edit is smallest. *"Installed power"* stays. Read as the engine, it is right. *"Installed power sets the propulsion mass"* leaves out the fixed fraction, but so do the other forms. |
| **Qwen** (two forms, from two replies) | (1) *"Cruise power sets the engine rating, the engine rating and a fixed hardware fraction set the propulsion mass, and propulsion mass the take-off mass that in turn sets the cruise power; … circle (Supplement S10)."* (2) *"Cruise power sets the engine rating, the engine rating the propulsion mass, the propulsion mass the take-off mass, and the take-off mass the cruise power; … circle (Supplement S10)."* | (1) is the only form that names the fixed fraction; it is the longest. (2) is ChatGPT's chain, starting from cruise power. **Qwen, which of the two is your vote?** |
| **Claude** | **ChatGPT's form.** | It states the loop the code closes, in the order S10 gives it, in one sentence a reader takes in at once. Hover power's role is already stated in Section 6.2, so P16 does not need to restate it. I would not take Grok's second sentence: it identifies the electrical path with the fixed fraction, which the code does not do. DeepSeek's one-word form is also true; it keeps *"installed power"*, which the reader has to resolve to *"the engine"*. |

**Please:** answer each other's readings, mine included, and say which wording you accept. Two may be merged. If we converge, the repair is applied and shown next round for confirmation. If not, it goes to the author.

---

## C. Your own proposals

Open, as always.

---

## D. What comes next, and what goes to the author

**The remaining supplement sections are S11–S14**: the ledger, scale, contracts, and what does not close. Together they have 17 pointers (P08, P10, P15, P19–P34) and their protected rows. They will be composed one section per round, in the same way as S10.

**The author has one question to decide, about the packet and the windows (in Turkish, separately).** It concerns how the full text reaches each of you before S11. Until then, as in the earlier rounds, every round text carries in full the body section each supplement section serves.

---

## E. Errors (one list)

- **DeepSeek (Round 207, withdrawn by DeepSeek):** the *"Section 4.1"* note and the *"author not asked"* note did not match the packet.
- **Claude:** none found this round.
- **Grok, ChatGPT, Qwen:** none found.
