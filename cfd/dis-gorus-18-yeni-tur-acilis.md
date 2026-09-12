# YZ'lerin YENİ sohbetlerine verilecek açılış metni (12.09.2026)

Kullanıcı bunu `makale/makale-v5.md` ile birlikte yükleyecek. Sıfırdan
başlayan bir sohbet olduğu için metin kendi kendine yetiyor.

---

## Reviewing meryemAircraft v5 — what we need from you

Attached is v5 of a configuration-study paper we intend to submit to **Drones**
(MDPI). You are one of four independent reviewers working on it in parallel; we
do not share your answers with each other before you answer.

### What the paper is

The primary contribution is a **framework**, not an aircraft. It argues that
hybrid VTOL aircraft pay for vertical capability in three currencies — carried
hover mass, exposed cruise drag, and continuous power sized by the hover peak —
that every known architectural remedy *transfers* the penalty between them
rather than removing it, and that there is an explicit escape condition: the tax
is charged whenever hover and cruise are served by hardware that is not the same
hardware, doing the same job, in the same orientation.

**meryemAircraft** is the case study that instantiates that condition: a
propeller-driven tail-sitting blended-wing body, one coaxial pair at the nose for
all thrust, four small coaxial pairs on tip frames for moments only, no elevons,
no rudder, no tilting or retraction mechanism, no dedicated lift system. The one
moving aerodynamic surface is a variable-extension strip on the lower surface,
which exists because propellers cannot produce a rolling moment.

### Where it stands

Body 17,900 words, 51 references, six supplementary files carrying the
derivations. Everything computable has been computed; nothing has been measured.
There is no wind tunnel and no flight test, and the paper says so in its first
limitation.

Four things changed in the last round and you should know them, because three of
them went **against** us and we kept them:

1. **Reflex sections do not trim this aircraft, and this is now measured rather
   than assumed.** Nine reflexed and low-moment sections have been tested in
   tunnels that measure pitching moment. Exactly one is positive (NACA 2R212,
   +0.004); the rest lie between zero and −0.03. Reflex as actually built is a
   device for *removing* negative pitching moment, not for producing positive
   moment. We need +0.056. Nine degrees of tip washout supplies it instead, at
   4.3 % of cruise efficiency.
2. **The span efficiency assumption was optimistic.** We computed the Oswald
   efficiency of the trimmed wing station by station (viscous section solver at
   each strip's own local lift coefficient): **0.817 against the 0.85 assumed**,
   worth 1.4 % of the ranges quoted.
3. **The battery buffer is the paper's most exposed number, and it got worse.**
   Bill 3 is avoided by a buffer implying 4.61 kW/kg. A 24S NCM pack that was
   built and *flown* in an eVTOL measures 724–892 W/kg continuous and ~1.5 kW/kg
   at its thermal limit. The light design's mass budget does not close at any
   measured specific power.
4. **The transition pitching moment is not computed, and we now argue it cannot
   reliably be** — three methods of three fidelities fail above ~10° incidence on
   this class of configuration, the highest of them against wind-tunnel
   measurement.

### What we want from you

**Please do not summarise the paper back to us.** We want the four things below,
in this order of usefulness.

**1. Where is it wrong?** Not "where is it weak" — we know where it is weak,
Section 8 lists it. Where is a number, a derivation, or an inference actually
wrong? We have been caught three times this way already and each time it improved
the paper.

**2. What would a Drones referee reject it for?** Be specific about which
sentence triggers the rejection. We would rather delete a claim than defend one.

**3. Two remaining source requests.** These are narrow:
   - A measured C_lα or side-force derivative for a **thin symmetric fin of a few
     tens of millimetres chord at Re ≈ 10⁵.** Our tip-frame fairing is 39 mm and
     we assumed 4.0 per radian; low-Reynolds compilations say that is optimistic
     but give us no number.
   - A wind-tunnel measurement of a **two-sided spoiler or strip** — equal
     projection above and below one wing half. NACA TR-796 (1944) called
     one-sided projection's pitching moment "prohibitive" and proposed the
     two-sided arrangement, noting the data were then insufficient. Has anyone
     measured it since? (NACA TR-1034 does **not** answer this; it measures
     symmetric left/right deployment as a speed brake. We checked.)

**4. Is 17,900 words the right length, and is the split right?** The body carries
results and measured evidence; six supplementary files carry derivations, the
full limitations enumeration, and the comparative sizing. Tell us if anything in
the supplementary needs to be in the body, or the reverse.

### One request about method

If you give us a source, please give us **the sentence you are relying on**, not
just the citation. Twice in the last round we were sent a source that said the
opposite of what it was offered for, and we only caught it by opening the PDF. We
would rather have three sources you have actually read than thirty you have not.
