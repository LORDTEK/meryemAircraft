# Round 17 — what moved, and the one question

**Version check before you read.** Open `makale-v5.md` and confirm all four:

| Marker | Current value |
|---|---|
| Sections | five; §2 is *Materials and Methods* |
| §3.3 rotor drag | **0.0153**, not 0.0085 |
| §3.6 contract 1 | B is **+21.1 %** against A, not −14.4 % |
| Abstract mass claim | **thirty-seven to forty-two percent** |

If you see 0.0085, or −14.4 %, or nine sections, you have an old copy. Say so and stop.

---

## What changed since you last read it

Four of your findings were verified against the files and acted on. Two of them
broke a claim.

**1. The headline rotor drag came from a propeller the aircraft cannot use.**
The free-wheeling figure was 0.0085, taken from the design with the lowest drag
of four. That design has a hover figure of merit of 0.27; the hover power the
whole paper descends from assumes **0.599**. Quoting it charged the
configuration for a component it had already ruled out.

Recomputed. The figure of merit is flat at 0.63–0.65 from section c_l 0.55 to
0.68, then collapses to 0.35 by 0.70 — so 0.599 falls inside the collapse and no
design in the family sits on it. Every design that *meets* the hover
requirement lies at c_l ≤ 0.68, and the least draggy of those gives
**ΔC_D0 = 0.0153**. Three and a half times the tip frames.

**2. That broke the drag bound, and the drag bound was load-bearing.**
The zero-lift build-up had no rotor row at all. With one:

| | lower | upper |
|---|---:|---:|
| as published | 0.0131 | 0.0210 |
| with rotors | 0.0216 | **0.0380** |

Assumed C_D0 = 0.0248. It used to sit **above** the bracket — three sections
called it conservative. It now sits **inside** it, optimistic by up to 53 %.

**3. So §3.6 was re-sized, and one ranking reversed.**
Architecture A was charged 1/1.12 for exposed hardware — tip frames only.
Architecture B was charged 13/17, which comes from a *measured* configuration
and already contains its lift-rotor drag. The comparison was asymmetric. The
drag book-keeping reproduces the published 1.12 to three digits, which is the
chain check; adding the rotor term gives **1/1.58**, cruise L/D 12.00 → **8.49**,
MTOW 50.0 → **54.5 kg**.

| Contract | B against A, as published | B against A, rotors charged |
|---|---:|---:|
| Fixed fuel fraction | −14.4 % | **+21.1 %** |
| Fixed fuel mass | −36.5 % | −5.4 % |
| Fixed MTOW and payload | −72.6 % | −44.9 % |

Under equal fuel fractions the lift-plus-cruise layout now flies further. A's
cruise efficiency fell below B's: 0.632 of clean against 0.765. The mass
advantage survives at **37 % rather than 42 %**. The tilting layout now leads
under all three.

The asymmetry is real and runs against this configuration: B's lift discs are
horizontal in cruise and can be stopped blades-aligned; A's are fixed-pitch
tractors that cannot be turned out of the flow at all.

**4. A second correction pushes the other way and is larger.**
Applying the measured pack's buffer fraction to *all three* architectures — not
just A — the layout that suffers is B. Its hover power per unit mass is the
highest, and the buffer feeds back through hover power:

| Buffer fraction | A | B | C |
|---|---:|---:|---:|
| 4 % | 54.5 kg | 86.0 kg | 60.3 kg |
| 16 % | 106.2 kg | 369 kg | 130.6 kg |
| 20 % | 165.8 kg | **does not close** | 234.1 kg |

B's entries past 12 % are not masses — they lie on a curve going vertical, and B
stops closing between 18 and 20 %. The reportable statement is qualitative.
An earlier version said the measured pack cut A's margin from 42 % to 20 %;
that was wrong in this paper's own favour — it grew A on the measured pack while
holding B at a mass sized on the assumed one. Corrected.

**5. Two smaller things, both found by chasing a reviewer's point.**
The neutral point was quoted as 0.859 m (untwisted planform) while the
sensitivity study used 0.867 m (twisted to trim). Chasing that found something
worse: across eight equally defensible solver choices the neutral point spans
0.858–0.867 m, a scatter of **1.3 % MAC — five times the grid sensitivity**, and
never measured before. In exact linear theory none of those choices can move it.
The static-margin figures are now quoted to one decimal for that reason, and the
neutral-point column of the loading-shape sensitivity is flagged as sitting
inside its own method's noise floor.

Also: a dead roadmap sentence from the IMRaD move — *"Section 1 reviews seventy
years of attempts…"* — was still in §1, self-referential and false. Deleted.

---

## The question

**Is there a reason not to run the RANS-versus-VLM loading comparison next?**

That is the plan. The setup exists: 1.67 M cells, 12.3 s/step on four cores,
~4 000 steps for a converged lifting solution, and the trimmed geometry needs a
new mesh. Call it fourteen hours plus meshing. What it would deliver is the one
missing input: §3.10 already measures the *sensitivity* to a spanwise
redistribution — 0.15 % MAC of neutral-point movement and 0.38° of trim-twist
movement per degree — and a RANS solution would supply the redistribution itself.

Before spending it, three checks:

1. **Is fourteen hours the right price for that answer**, given that §3.6 has
   just moved on drag rather than on loading? If the answer is no, name the
   calculation you would run instead and what result would count against the
   paper.

2. **The neutral-point scatter above is 1.3 % MAC.** A RANS comparison would be
   read against a VLM baseline carrying that scatter. Does that make the
   comparison worth less than it looks, and if so what would fix it — a tighter
   VLM protocol first, or a different comparison quantity?

3. **The 0.0153 is a lower bound at Mach 0.77**, which is marginal for the
   incompressible section data underneath it. Is the honest move to report it as
   a bound, or to redo the blade-element run with a compressibility correction
   before anything else is built on it?

Answer whichever you can check. If you cannot open the file, say so rather than
describing it.
