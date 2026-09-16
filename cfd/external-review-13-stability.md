# Round 8 — we took two of your suggestions, and both changed numbers

Two of you proposed work that needed no new CFD: **a credible panel/VLM
static trim analysis**, and **formalising the framework plus testing it
once against a literature benchmark**. Both are done. Both changed
something, and one of them exposed an error of ours.

We also still owe you a journal decision. You split three ways last round
and we would like to close it.

---

# 1. The static trim check — and an error we found inside it

One of you objected to our sentence that the tight condition at the end of
the rotation was "the ordinary trim question of a tailless aircraft". The
objection was that this aircraft has no elevons, no reflex is specified,
and the centre of gravity we had quoted was at 57 percent of root chord —
so "ordinary" was asserted, not shown. That was fair, so we showed it.

## 1.1 What the vortex-lattice solution gives

Neutral point at 0.859 m from the root leading edge — **34.3 percent of
mean aerodynamic chord**, an entirely conventional value for a swept
planform. Converged: 0.8611 → 0.8591 → 0.8589 m over a threefold grid
refinement, 0.26 percent.

## 1.2 The error was ours, and it was in the centre of gravity

Our first pass with that neutral point gave a static margin of 47 percent
of mean aerodynamic chord and a cruise trim requirement of C_m = 0.240 —
against 23 N m of tip-propeller authority and roughly 150 N m needed. That
looked like a fatal finding.

It was our own mistake. The 57 percent centre of gravity came from our
inertia model, where we had placed fuel, payload and engine along the root
chord **by hand, without checking where the internal volume actually is.**
We then measured it. Because of the sweep, the outboard sections lie well
aft of the root trailing edge, and:

- the internal volume's absolute centroid is at **78.3 percent** of root chord;
- the structural centroid is at **99 percent**.

Distributing the movable items in proportion to available volume — which is
what a real internal arrangement must do — gives a centre of gravity at
**80 percent** of root chord.

## 1.3 The corrected picture

| | hand-placed (wrong) | volume-weighted |
|---|---:|---:|
| Centre of gravity | 57 % root chord | **80 %** |
| Static margin | +47 % MAC (absurd) | **+12.4 % MAC** |
| Cruise trim coefficient needed | 0.240 | **0.063** |
| I_yy, light design | 7.04 kg m² | **9.81 kg m²** |

Twelve percent sits in the middle of the usual tailless band of five to
fifteen. **The configuration is statically stable in pitch, and it owes
that to the sweep**, which carries the neutral point aft faster than it
carries the volume.

The trim requirement of 0.063 is above what reflexed sections typically
deliver (0.02–0.05), but of the same order. Moving the centre of gravity
aft to 83 percent — a three-centimetre change in internal arrangement —
gives 0.040 and a static margin of 7.8 percent, both conventional.

## 1.4 What this adds, and what it costs

**It adds a constraint the study did not have**: the centre of gravity must
lie between roughly 80 and 85 percent of root chord. Not demanding, since
the volume centroid is at 78.3, but not free either — fuel, payload and
engine cannot be placed forward for convenience.

**It costs rotational margin.** The corrected inertia is 39 percent higher,
so the numbers we gave you last round were optimistic:

| | required, bang-bang | required, smooth | available | margin, bang-bang | margin, smooth |
|---|---:|---:|---:|---:|---:|
| Light, t_r = 2 s | 15.4 N m | 23.1 N m | 23.0 N m | **1.49 ×** | **0.99 ×** |
| Heavy, t_r = 5.1 s | 605 N m | 907 N m | 952 N m | **1.57 ×** | **1.05 ×** |

Both designs now sit essentially at unity on a smoothly commanded rotation.
The shortest smooth rotations the tip propellers can force are 2.01 s and
4.98 s against reference times of 2 and 5.1. **The transition times are not
free parameters; they follow from the tip-propeller moment.** We have
written that as a finding rather than adjusting the times again.

**Question 1.** Is the volume-weighted placement a defensible way to fix a
centre of gravity in a configuration study, or does it need to be an
explicit design choice with its own justification? And is a static margin
of 12.4 percent with a trim requirement of 0.063 something you would accept
as "shown", or does it still need the camber distribution defined?

---

# 2. The framework, formalised and tested

The other suggestion was to make the framework more mathematical and to test
it once against published work. Section 3.7 is new.

**Formal statement.** The three charges are written as dimensionless
fractions of the quantity each degrades: carried hover mass over take-off
mass; the fractional loss of lift-to-drag ratio against a clean airframe;
and the propulsion mass attributable to installing continuous power above
the cruise requirement. Each is zero for an aircraft that does not hover and
measurable for one that does. The claim is that they cannot be minimised
independently, and the transfer table of Section 3.4 shows which move trades
which for which.

**The test.** If the three are genuinely separate currencies, an architecture
can be best in one and worst in another — specifically, the architecture with
the highest cruise lift-to-drag ratio need not be the lightest. A
single-metric comparison would not anticipate that.

The NASA sizing study we already cite reports exactly this: the
lift-plus-cruise concepts are the heaviest of four examined *and* have the
highest cruise efficiency of the group, with the weight attributed to
hardware carried for hover. Our own comparison in Section 5.5 reproduces the
same structure on a different architecture set: the tilting layout has the
best lift-to-drag ratio, 13.44 against 12.00, and is twenty percent heavier
than the tail-sitter.

Two independent studies, different architecture sets, same structure.

We also wrote what the framework does *not* claim: it predicts no magnitudes
for an architecture that has not been sized.

**Question 2.** Is that a real test or are we congratulating ourselves for a
restatement? This is the "is it a framework or a relabelling" question one of
you raised, and we would rather you answered it than us.

---

# 3. The journal — please close this

Last round you split three ways: Aerospace Science and Technology first, or
Journal of Aircraft first, or Drones first.

**The author's own preference is Drones**, and the paper now differs from
what you judged: it has a converged static-stability result, a formalised and
externally tested framework, a stated centre-of-gravity constraint, and
tighter, more honest rotational margins.

**Question 3.** With that in front of you, is Drones the right first
submission, or does the added stability analysis change the calculation
toward Aerospace Science and Technology? If you still disagree with each
other, please say which of your reasons you would abandon first.

---

# 4. Standing question

Nothing about our Q1 assessment has changed from your last answers, and we
are not asking you to repeat them. But if either of the two new pieces of work
above moves your estimate — in either direction — we would like to know, and
particularly if it moves it **down**. The static-stability result closed one
gap and opened a constraint; the rotational margins got worse, not better. If
the net is negative in your reading, say so.
