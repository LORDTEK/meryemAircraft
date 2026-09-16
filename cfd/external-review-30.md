# Round 26 — suggested reviewers. A short, specific question, not a full review.

---

## 0. What this round is, and what it is not

**The manuscript is submitted.** *Drones* (MDPI), Article, Drone Design and Development
section. Everything you reviewed in Round 25 went in unchanged. **This is not a request to
re-read the paper.**

One field is left: **suggested reviewers.** MDPI asks for three to five, with name, email
and affiliation, and screens them for conflict of interest. We want your judgement on the
slate before it is entered, because a bad slate has two failure modes and both are quiet:
a reviewer who cannot judge the paper, or a reviewer whose own work the paper reinterprets.

**The file, if you want it** — this is the submitted manuscript, which carries the Round 25
corrections you asked for:
`https://raw.githubusercontent.com/LORDTEK/meryemAircraft/e45d43c/paper/paper-v7.md`
— SHA-256 `c5b0cd898d20…`, 3 077 lines. The bibliography is at the end.
*(The `535401f/paper-v6.md` link from Round 25 still resolves but is the build from before
those corrections. Use the one above.)*

---

## 1. What the paper is, in five lines

An accounting framework for the cruise-efficiency penalty of hybrid VTOL aircraft, charged
in three coupled currencies, plus an uncrewed tail-sitting blended-wing-body as the case
that instantiates its escape condition. **Three architectural claims**: no runway
(against runway-dependent fixed-wing), wing-borne cruise (against multirotors), and
**no propulsor-reorientation mechanism** (against tilting layouts — the airframe rotates,
the propulsors do not). **One claim declined**: a range ranking against the other hybrids,
because it reverses with the sizing contract.

Methods a reviewer must be able to judge: **blade-element momentum theory** (the
free-wheeling rotor drag), **vortex-lattice with a viscous section method** (span
efficiency, neutral point), **RANS with a three-level grid study** (the loading-shape
check), and **a closed sizing loop** across three contracts and two scales.

---

## 2. The slate we have built, from the paper's own bibliography

Every candidate below is cited in the paper. Affiliations were checked against the
published papers and public profiles; **we have not verified current email addresses and
will take those from the papers themselves**, which are open access in five of the six
cases.

### A. Bacchini & Cestino — Politecnico di Torino, Dept. of Mechanical and Aerospace Eng.
*Electric VTOL Configurations Comparison*, Aerospace 2019, 6(3), 26. Bacchini's doctoral
thesis is our reference [3].

**Why:** this is the closest published work to ours — a like-for-like comparison of eVTOL
configurations — and they are the only people who compare architectures the way we do.

**Why this is also the riskiest name on the list, and the reason we are asking you:**
**our paper leans on their data more than on anyone else's.** The wind-tunnel
lift-to-drag ratios in our Table 1 are theirs. The 13/17 cruise penalty we charge the
lift-plus-cruise layout is theirs. And **we reinterpret it**: we argue that charging that
ratio to one architecture while charging our own only its frames was asymmetric, and we
rebuild the comparison. That is a correction to how *their* number was being used —
by us — but a reviewer may read it as a correction to *them*.

Citing someone is not a conflict of interest under MDPI's rules. But is it wise?

### B. Ugwueze, Statheros, Horri (Coventry), Bromfield (Birmingham), Simo (UCLan)
*An Efficient and Robust Sizing Method for eVTOL Aircraft Configurations in Conceptual
Design*, Aerospace 2023, 10(3), 311.

**Why:** they built a sizing method for exactly the problem our Section 3.6 solves, and
they would be the readers most able to say whether our three-contract result is correct,
trivial, or already known. **This is the single most competent audience for our headline
claim.** Five authors, so several independent choices.

### C. Panagiotou & Yakinthos — Aristotle University of Thessaloniki, UAV Integrated
Research Center / Lab of Fluid Mechanics and Turbomachinery
*Quasi-3D Aerodynamic Analysis Method for Blended-Wing-Body UAV Configurations*,
Aerospace 2021, 8(1), 13.

**Why:** BWB UAV aerodynamics with low-fidelity methods, which is our Section 3.10
exactly — panel/vortex-lattice methods used for a BWB UAV, with the question of how far
they can be trusted. They have an active group and a continuing publication record on
this airframe class.

### D. Lampropoulos, Vouros, Templalexis, Lekas — Hellenic Air Force Academy
*On the Aerodynamic Performance of a Blended-Wing-Body, Low-Mach Number Unmanned Aerial
Vehicle*, Fluids 2025, 10(3), 54.

**Why:** the most recent BWB UAV aerodynamic study in our bibliography, at our Mach
number and our scale, using a panel method and an optimisation loop — the same tools and
the same regime.

### E. Wang & Zhou — Northwestern Polytechnical University, College of Aeronautics
*Aerodynamic Design, Analysis and Validation of a Small Blended-Wing-Body Unmanned Aerial
Vehicle*, Aerospace 2022, 9(1), 36.

**Why:** they designed a small BWB UAV **and wind-tunnel tested it.** We have no
experimental validation and say so throughout; a reviewer who has done the measurement we
did not do is the right person to say whether our bounds are honest or whether we are
claiming more than calculation supports.

### F. Li, Zhou, Wen (Hong Kong Polytechnic), Low (NTU Singapore), Chen
*Transition Optimization for a VTOL Tail-sitter UAV*, IEEE/ASME Trans. Mechatronics 2020,
25(5), 2534–2545.

**Why:** tail-sitter transition, which is our Sections 3.12–3.17 and our largest open
item. They optimised the manoeuvre we only bound.

### G. Reserve — Şugar Gabor, Koreanschi, Botez — LARCASE, ÉTS Montréal
*A New Non-Linear Vortex Lattice Method*, Chinese Journal of Aeronautics 2016.

**Why held in reserve:** the most technically contested part of our paper is Section
3.10, where a RANS/vortex-lattice loading comparison runs **opposite in direction** to the
published comparison we cite, and we report that rather than reconcile it. This group
builds non-linear vortex-lattice methods and would be the sharpest possible reader of
that section. Whether that is desirable or suicidal is a judgement we would like yours on.

---

## 3. What we are asking you

**1. Which three to five, and in what order?** MDPI takes three to five. We are inclined
toward **B, C, E and F** — sizing, BWB aerodynamics, an experimentalist, and a
tail-sitter specialist — as the combination that covers all four methods a reviewer must
judge. Argue against it.

**2. Bacchini & Cestino: suggest, or not?** They are the closest match and the paper
reinterprets their data. Two readings: *(a)* the person whose data you used is the person
best placed to check you used it correctly, and suggesting them signals confidence; *(b)*
asking someone to review a paper that says their number was applied asymmetrically is
inviting a defensive review. **Which reading is right?** We cannot tell, and it is the
question we most want answered.

**3. Is there a competence gap in the slate?** The four methods are blade-element momentum
theory, vortex-lattice plus viscous sections, RANS with a grid study, and closed-loop
sizing. **B** covers sizing, **C/D/E** cover the aerodynamics, **F** covers transition.
**Nobody on this list is primarily a propulsion or rotor-aerodynamics person**, and the
free-wheeling rotor drag — 0.0154, the largest single entry in our ledger and the number
that reverses one of our comparisons — rests on blade-element momentum theory. **Should we
add a propeller/rotor specialist, and from where?** Our bibliography is thin there.

**4. Should we name anyone in "excluded reviewers"?** We have no grounds we know of. Is
leaving it blank ever read as naive?

**5. One thing we will not do, for the record:** we will not suggest anyone we have a
personal or institutional connection to, anyone from our own country's aerospace
community whom we know, or anyone we have corresponded with. The authors are independent
researchers with no institutional affiliation, which makes the conflict surface small —
but it also means we have no informal read on any of these people. **That is exactly why
we are asking.**

---

## 4. What the paper says about itself, so you can judge reviewer fit honestly

The paper states that it is not shown to be flyable; that it has no wind-tunnel
measurement and no flight test; that the mass budget closes only on a battery specific
power about 3.8 times the highest yet measured on a flown pack; that the transition
pitching moment is blocked on measurement; that the roll strip's actuation is unsized; and
that the landing transition is unmodelled. **A reviewer who rejects it on those grounds
will be rejecting it for something the paper announces.** The question is whether the
framework and the architectural claims survive that, and a good slate is one that can
judge the framework rather than only the aircraft.

---

## 5. Keep it short

This is a narrow question and a short answer is the useful kind. Name your three to five,
say why, and answer question 2. If you think the whole slate is wrong, say that instead.
