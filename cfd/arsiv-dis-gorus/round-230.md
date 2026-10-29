# Round 230 — Where is v9 ready to be published, at the venue that does the authors the most credit?

**Readers:** all channels. This round opens a new stage: choosing the venue. This text was prepared by the Claude session that works in the repository. It states only facts with their basis. The Claude session's own view goes beside everyone's in the next round, under the standing rule.

**This round carries the whole paper.** Section 5 below is the full text of the v9 paper as deposited on Zenodo: all 27 pages, extracted from the PDF with its layout kept, so tables keep their columns. The two figures are images; their captions are in the text. The PDF's SHA-256 is `f264782f8c13104de2723cb987de5289418ae8fcf0760a98a72020177ea7de82`. The supplement is not included; it is in the Zenodo record. Nobody should judge a venue's fit without reading the paper.

**The author's decision:** the paper's content will not change any more. This round is only about where to publish it. Changes to the template, format or length layout required by a venue are allowed; changes to content are not.

**The author's question, in full:** *Where is this work, published as v9 on Zenodo (https://zenodo.org/records/23754355) and the product of a great deal of effort, ready to be published so that it brings the authors the most credit?*

---

## 1. What the work is (facts for the venue question)

**The record.** Zenodo v9 is a new version under the concept DOI 10.5281/zenodo.22144194; the version DOI is 10.5281/zenodo.23754355, resource type Publication / Preprint, licence CC BY 4.0.
- The Claude session could not open the Zenodo page from its environment (the network proxy refused it, HTTP 403). The paper below is the deposited PDF, which the author supplied directly.

**Title:** *meryemAircraft: A Blended-Wing-Body Tail-Sitter with Body-Fixed Coaxial Propulsors.*

**Files deposited (per the authors' upload notes):**
- the paper (preprint, without vitae);
- the supplement (Table S0 and Sections S1–S11);
- the LaTeX sources;
- the analysis code at a recorded commit of https://github.com/LORDTEK/meryemAircraft;
- the record of the blind re-implementation: frozen text with SHA-256, the pre-run declaration, the list of the 58 compared values with their status, prompt, scripts, outputs, and the diff of every change after the freeze;
- the additional checks.

**Abstract (as in the paper; Section 5 has the whole text):**

> Hybrid vertical-takeoff aircraft change between hover and cruise by carrying two propulsor sets or reorienting one. meryemAircraft, a 50 kg tail-sitting blended-wing body for a 13 kg payload, does neither: its fixed-pitch coaxial pairs keep one body-relative orientation while the whole airframe rotates, so it carries none of the mechanism classes a tilting architecture uses to change regime. It is priced in three costs of hover: carried hover mass, exposed cruise drag and continuous power sized to the hover peak. On a buffered series hybrid, the nose pair, which supplies hover and cruise thrust, incurs none of them; the attitude-control tip pairs and frames stay in the cruise flow, taking 50 to 80 percent of zero-lift drag across the drag sources examined. With the assumed frame drag the sizing loop closes at 52.3 to 57.5 kg, at an effective lift-to-drag ratio 13 to 51 percent above a published turboshaft quadrotor's; across those sources the envelope, not a confidence interval, is 50.7 to 66.1 kg and 699 to 1,401 km. The range margin of a lift-plus-cruise layout over this aircraft shifts by 67 to 77 percentage points across three sizing contracts, so the ranking depends on the contract. No store reported as built delivers the required specific power; hover heading authority, the transition and landing remain open.

**Nature of the work:**
- An analytical conceptual-design study of one configuration.
- No aircraft built, no flight test, no wind tunnel; computational methods only (vortex-lattice, blade-element momentum with NeuralFoil polars, a 3-DOF transition model, a sizing loop).
- The contribution is the architecture. The accounting and the sizing contracts are its instruments.
- 27 pages in `elsarticle` preprint format (about 9,000 words by text extraction, references included), 6 tables, 2 figures, 28 references, with a separate supplement.
- The transition is computed but not settled. On the vortex-lattice pitching moment, the rotation completes at the sizing figure of merit read as the pair's own value (20.7 N·m), and fails from about 19 N·m (Sec. 4.3).
- One independent check of reproducibility: two blind re-implementations from the frozen text.

**The authors:**
- Three independent researchers with no institutional affiliation and no funding. The cost of publication therefore matters.
- The corresponding author is Meryem Gülmen.
- The authors hold Turkish patent application TR 2026/014570 (filed 26 August 2026) on the aircraft and the roll strip. The paper declares it.

**Submission history (all desk decisions; no reviewer has read the work):**

| Date | Venue | Outcome, as recorded |
|---|---|---|
| 2026-09-14 | *Drones* (MDPI) | Found out of scope and transferred to *Aerospace* without review. The *Drones* scope page, which was not read before submitting, asks that general theoretical aircraft-design papers be validated with experimental data from at least a laboratory-scale uncrewed platform. |
| 2026-09-15 | *Aerospace* (MDPI) | Desk-rejected the same day ("discipline, novelty and general significance"). The text then had a 35,827-word body. |
| 2026-10-02 → 10-14 | *Journal of Aircraft* (AIAA), Full Paper, v8 | Desk-rejected by the Associate Editor: *"The paper does not provide any developments that are of archival nature."* |

The present v9 is shorter and restructured around the architecture. It was prepared in *Aerospace Science and Technology*'s template (Elsevier), and an AST submission version with vitae and photographs exists. **It has not been submitted anywhere.** AST is a candidate like any other.

**Standing rules that bind any answer:**
- **The venue rule.** Before a venue is named as a target, its aims, scope and special requirements are read in full and compared with the paper item by item. *Drones* was submitted to without reading its scope page; that cost one rejection.
- **The source rule.** Any statement about a venue that could be wrong needs a link opened in this round, and the quoted sentence where the claim rests on one. This covers scope, preprint policy, AI policy, length limits, fees, indexing, quartile, impact factor and deadlines. A figure you did not open this round is not given. A hedged number is worse than none, because it enters the record as data.

---

## 2. Questions

**Q1. Venues.** Name up to five venues, journals or conferences, ranked by the credit they would bring the authors. Limit yourself to venues where v9, with its content unchanged (no experiment, no new analysis, no rewriting; template and format only), has a realistic chance of being sent to review and accepted. For each, give:
- (a) the aims-and-scope page, with a link and the sentence that admits an analytical conceptual-design study of one configuration without experiments, or the sentence that excludes it;
- (b) the preprint policy, with a link and a quotation. v9 and its predecessors are public on Zenodo under CC BY 4.0;
- (c) the policy on generative-AI use, with a link and a quotation. AI tools were used for text, literature search, review and analysis code, and the paper says so;
- (d) the length or page limits, against v9's 27 pages and separate supplement;
- (e) the indexing and quartile or impact figure, with the source page and its year;
- (f) the publication cost for authors without funding: APC or a subscription route;
- (g) for conferences, the next deadline, with a link, and whether a conference paper can later be extended into a journal paper at the same publisher;
- (h) what the venue would require of the files: template, reference style, highlights, graphical abstract, page or word count. Content stays as it is; if the venue would require a content change, say so, because that removes it from the list;
- (i) the desk-rejection risk in the light of the two recorded reasons: "experimental validation" and "no developments of archival nature". Say what in v9 now answers them, or does not.

**Q2. "Ready".** Is v9, as it is, ready for the venue you rank first? The content is fixed. Name anything in the submission package (cover letter framing, article type, suggested reviewers, choice of section or special issue) that would most raise its chance of being sent to review, and say why.

**Q3. Credit against acceptance.** Where the most prestigious venue and the most likely venue differ, which would you advise for these authors at this point, and why? Is there a sequence, for example a conference first and then a journal? If you propose one, give the venue rules that allow it, with links.

**Q4. Venues to avoid.** Name any venue a reader might propose that you would advise against for this paper, with the reason and a link: scope, predatory practice, preprint conflict, or AI policy.

**Q5. Open proposals,** each with its reason.

Each channel's answers go side by side to every channel next round. Answer each other's reasons by name there.

---

## 3. Answer format

Give your channel name first. Answer Q1 as one block per venue, (a)–(i), each with its link. Then answer Q2–Q5. Mark every item you did not open this round as "not opened", and give no number for it.

## 4. What goes to the author after this round

- The venues on which the channels converge, with each one's requirements as quoted, so that the author can decide.
- Where the channels diverge, the reasons side by side.
- Any venue requirement that the fixed content of v9 cannot meet, so that venue drops out.

---

## 5. The paper: full text of v9 as deposited (extracted from the PDF, layout kept)

```text
meryemAircraft: A Blended-Wing-Body Tail-Sitter
        with Body-Fixed Coaxial Propulsors
            Meryem Gülmena,∗, Berke Gülmena , Ömer Gülmena
             a
                 Independent Researcher, Merkez, 06560, Ankara, Türkiye

Abstract
Hybrid vertical-takeoff aircraft change between hover and cruise by carrying
two propulsor sets or reorienting one. meryemAircraft, a 50 kg tail-sitting
blended-wing body for a 13 kg payload, does neither: its fixed-pitch coaxial
pairs keep one body-relative orientation while the whole airframe rotates, so
it carries none of the mechanism classes a tilting architecture uses to change
regime. It is priced in three costs of hover: carried hover mass, exposed
cruise drag and continuous power sized to the hover peak. On a buffered
series hybrid, the nose pair, which supplies hover and cruise thrust, incurs
none of them; the attitude-control tip pairs and frames stay in the cruise flow,
taking 50 to 80 percent of zero-lift drag across the drag sources examined.
With the assumed frame drag the sizing loop closes at 52.3 to 57.5 kg, at
an effective lift-to-drag ratio 13 to 51 percent above a published turboshaft
quadrotor’s; across those sources the envelope, not a confidence interval, is
50.7 to 66.1 kg and 699 to 1,401 km. The range margin of a lift-plus-cruise
layout over this aircraft shifts by 67 to 77 percentage points across three
sizing contracts, so the ranking depends on the contract. No store reported
as built delivers the required specific power; hover heading authority, the
transition and landing remain open.
Keywords: hybrid VTOL, tail-sitter, blended wing body, airframe rotation,
aircraft sizing, sizing contracts

  ∗
   Corresponding author.
   Email addresses: meryemgulmen@outlook.com (Meryem Gülmen),
berkegulmen@outlook.com (Berke Gülmen), gulmen@outlook.com (Ömer Gülmen)

1. Introduction
1.1. Two configuration families and the corner between them
    Fixed-wing aircraft carry payload over distance efficiently because a wing
sustains them without continuously spending power on lift; their limit is in-
frastructural, a runway, a catapult, or an equivalent installation. Rotorcraft
remove that requirement and can take off, hover and land at confined sites,
but with no wing every second of flight is bought with installed power, so
range and endurance stay modest; multirotors suit short-range missions and
vectored-thrust aircraft long-range ones [1]. Missions such as wildfire obser-
vation and cargo delivery to sites without a runway need both capabilities at
once.
    Hybrid vertical-takeoff (VTOL) aircraft occupy that corner today by two
routes: lift-plus-cruise aircraft carry two sets of propulsors and switch be-
tween them, and tilting aircraft carry one set and reorient it. A third route
keeps one set of propulsors in one orientation and rotates the whole airframe
instead: the tail-sitter. The Convair XFY-1 flew it in 1954 and completed
six transitions to conventional flight before testing was curtailed by engine
and gearbox reliability problems [2]; uncrewed tail-sitters, enabled by electric
drive on each rotor, sensor-based attitude reference and onboard computa-
tion, have revisited the route for more than a decade [3, 4].
    All three routes have been studied, at different levels of evidence (Table 1).
What remains unsettled is the price each pays for hover, and how that price
should be counted when architectures are compared.

1.2. What is already established
    Table 1 summarizes the closest prior work. Uncrewed tail-sitters have
flown with a main rotor under cyclic and collective pitch [3] and with four
rotors and no control surfaces [4]; attitude control without aerodynamic sur-
faces has been demonstrated on a quadrotor tail-sitter [4]; coaxial contra-
rotating propulsion has been used on tail-sitters to cancel reaction torque [5,
6], and the differential speed of a coaxial pair has been used as a con-
trol channel about the propeller axis [7]. A blended-wing-body tail-sitter
with contra-rotating propulsion for disaster response has been analyzed with
vortex-lattice and RANS methods [8], and buffered series-hybrid power has
been sized for winged tail-sitters [9, 10]. The compromise at the centre of
this paper’s drag and efficiency results is also known: fixed-pitch propellers
cannot be very efficient in both hover and forward flight [3].

Table 1: Closest prior work. Entries restate what each reference reports; “not stated”
means the reference, as cited here, does not report it.
Ref.        Airframe            Propulsors          Reported conversion and              Power /
                                                    hover-control mechanisms             evidence
[2]         Crewed              One turboprop       Not stated                           Flown; six
            tail-sitter, 1954                                                            transitions
[3]         Delta biplane       Main rotor;         Airframe rotates about 90◦ ;         Flown
            tail-sitter         wingtip rotors      main-rotor cyclic and collective
                                                    pitch; wingtip rotors and
                                                    ailerons balance main-rotor
                                                    torque
[4]         Quadrotor           Four rotors         Differential rotor thrust and        Hover,
            tail-sitter                             torque; no control surfaces          transition and
                                                                                         level flight,
                                                                                         experimentally
                                                                                         verified
[11]        Tail-sitter         Not stated          Differential rotor speed; elevator   Transition
                                                    and ailerons in propeller wash       control study
[5]         Convertible         Coaxial             Counter-rotation cancels             Hover control
            mini-UAV            contra-rotating     reaction torque; other channels      model
                                                    not stated
[6]         Tail-sitter MAV     Coaxial pair        Elevon and rudder in slipstream      Hover attitude
                                                                                         control
[12]        Flying-wing         Two                 Differential thrust about the        Hover and
            tail-sitter         counter-rotating    source’s xb axis; elevons for the    vertical flight
                                propellers          other two axes
[7]         Tail-sitter         Coaxial             Coaxial layout: differential         Lift-system
            (several layouts)   contra-rotating     motor speed; stabilizer and          design
                                                    rudder
[8]         Blended-wing-       Contra-rotating     Control surfaces and propeller       VLM and
            body tail-sitter    pusher              effectiveness discussed; control     RANS analysis
                                                    allocation and blade pitch not
                                                    stated
[9]         100 kg winged       Four, six or        Not stated                           Sized: engine
            biplane             eight rotors;                                            for cruise, boost
            tail-sitter         fixed-pitch rotor                                        battery for
                                model                                                    VTOL
[10]        Coaxial             Coaxial             Not stated                           Sized: fuel cell
            tail-sitter with                                                             charging a
            fuselage and                                                                 battery
            tails
This work   Blended-wing-       Five coaxial        Airframe rotation; differential      Sized;
            body tail-sitter    pairs, fixed        thrust of coaxial pairs,             accounting and
                                pitch and fixed     torque-balanced in cruise; one       contracts
                                mounting            lower-surface strip

1.3. Gap and contribution
    The individual elements are not new: tail-sitting aircraft are seventy
years old [2], blended wing bodies have been studied for transport for three
decades [13], and series-hybrid propulsion has been designed for small un-
crewed aircraft [14]. Among the references summarized in Table 1, none
reports the complete combination analysed here: a wing-dominant tail-sitter
whose propulsors keep one body-relative orientation and a fixed blade pitch,
with coaxial pairs torque-balanced in cruise and hover attitude assigned to
their differential thrust and to one lower-surface strip. The closest reported
airframe and propulsor arrangement is that of [8], whose description does
not specify its mounting, blade pitch or control allocation in enough detail
to tell whether it shares this arrangement. The sizing studies closest to this
work [9, 10] size particular hybrid tail-sitters for mass, aerodynamics and
power; they do not separate the price of hover into accounts defined before
the configuration is chosen, and they do not compare architectures under
more than one sizing contract.
    The contribution of this paper is that architecture, meryemAircraft. It
carries none of the mechanism classes that tilting architectures use to change
regime (Sec. 3); doing without them is paid for in exposed drag and in in-
stalled power, and the paper prices that payment. To do so it divides the
price of hover into three accounts (carried hover mass, exposed cruise drag,
and continuous power sized to the hover peak; Sec. 2), closes the aircraft on
a buffered series hybrid, and compares it with a lift-plus-cruise layout under
three sizing contracts, the rules that fix what a comparison holds equal. The
accounts and the contracts are instruments: they locate where the archi-
tecture pays, and they show that its range ranking against the competitor
depends on the contract within the range model used (Sec. 4).
    The study is analytical; no aircraft has been built or flown. Section 2
states the accounting and the sizing contracts, Section 3 the configuration and
methods, Section 4 the closures, the cost ledger and the contract-dependent
rankings, and Section 5 the limits of the results.

2. Analytical framework and sizing contracts
2.1. Three costs of hover
    On a one-hour mission, takeoff, the two transitions and landing occupy
about a minute, roughly two percent of the flight. Hardware or capacity

provided for that minute is carried for the remaining fifty-nine. This duty-
cycle mismatch cannot be removed by improving the hardware, because it is
a property of the mission, and it gives rise to three distinct costs, each paid
in its own unit.

Bill 1: carried hover mass. A dedicated lift subsystem (rotors, motors, mounts,
wiring and structural reinforcement for the vertical phase) produces no re-
quired lift or thrust in cruise and is carried anyway. Its cost is amplified
twice. Through the closure
                                        mpayload
                        MTOW =                         ,                    (1)
                                    1 − fempty − ffuel
with fempty and ffuel the empty and fuel fractions of takeoff mass, added empty
mass passes through a multiplier that grows as the denominator shrinks, and
the hover power it requires grows as W 3/2 at fixed disc area, and in proportion
to W at fixed disc loading, as held in the sizing loop (Sec. 4.2).

Bill 2: exposed cruise drag. Hover hardware left in the airstream after the
vertical phase (stopped or free-wheeling rotors, the structures that carry
them, and their interference with the wing) adds cruise drag. Wind-tunnel
work on hybrid airframes found the difference between propellers aligned with
the flow and no propellers modest, but the drag of the motors significant [15].
A quadplane study measured more drag in the hybrid regime than in either
pure mode, and separately found that a simulation neglecting rotor–structure
interaction predicted more lift and less drag than was measured [16]. Because
Bill 2 is paid per unit time in cruise, it grows with the quantity the aircraft
exists to maximize.

Bill 3: power sized to the hover peak. A VTOL aircraft must install enough
power to hover. From momentum theory for hover and the drag polar for
cruise (Supplement S1),
                                    s
                           Phover     DL L/D ηp
                                  =             ,                       (2)
                          Pcruise      2ρ V ηh

where DL is disc loading and ηh , ηp are hover and cruise propulsive efficien-
cies. The ratio depends on the configuration and its operating points, not
on how long the hover lasts; a disc loading of 100 N m−2 , L/D = 15 and
V = 30 m s−1 give a ratio between three and four. Bill 3 is the continuous

power plant (engine or equivalent) installed to that peak: it is sized by a con-
dition that lasts a minute and is carried for an hour. The electrical path that
delivers the peak (machines, power electronics, wiring) is a separate item of
the ledger in Sec. 4.3.
2.2. Remedies move cost; they do not remove it
    The three bills are distinct accounting quantities, not assumed indepen-
dent physical causes, and each known partial remedy reduces one of them by
paying in another or in a cost outside the three (Table 2).

Table 2: Known partial remedies and the costs they move. “Outside” marks a cost this
accounting does not track but lists.
 Remedy                                    Reduces                   Pays in
 Distributed electric lift rotors          Bill 3 (the cruise en-    Bills 1 and 2 (many
                                           gine no longer sizes to   rotors and mounts,
                                           hover)                    carried and exposed)
 Folding or retracting lift rotors         Bill 2                    Bill 1 (mechanism,
                                                                     actuation, locking);
                                                                     outside: a new failure
                                                                     mode
 Tilt-rotor, tilt-wing, tilt-nacelle       Bill 1 (one propul-       Mass of pivot and ac-
                                           sion group for both       tuators; Bill 3 un-
                                           regimes)                  less a store supplies
                                                                     the hover peak; out-
                                                                     side: gyroscopic cou-
                                                                     pling, transition con-
                                                                     trol
 Variable-pitch or feathering propulsors   Bills 1 and 3             Mass of pitch hub
                                                                     and actuation; out-
                                                                     side: a new failure
                                                                     mode
 Higher disc loading                       Bills 1 and 2             Bill 3 (hover
                                                                              √      power
                                                                     rises as DL)
 Lower disc loading                        Bill 3                    Bills 1 and 2 (larger
                                                                     structure and ex-
                                                                     posed area)

   The accounting is falsifiable: a counter-example is a remedy that reduces
one bill, leaves the other two no worse than in the architecture it modifies,
and whose own cost is absent or demonstrably smaller in the same unit.
Costs outside the three bills do not refute the accounting, but they are listed
rather than ignored.

2.3. The escape condition
    Inverting Table 2 gives the condition under which none of the three bills
is incurred. It is stated here, before any configuration is examined, so that
the standard is not taken from the aircraft it will be used to measure:

      An architecture incurs none of the three bills if the propulsors
      that carry the weight, held in one orientation relative to the air-
      frame, produce both the hover thrust and the cruise thrust, and
      if the difference between the hover peak and the cruise demand
      is supplied from an energy store rather than from installed con-
      tinuous power.

    An architecture fails the condition if it carries through cruise a propul-
sor that produces no cruise thrust, if it reorients a propulsor relative to the
airframe to change regime, or if its installed continuous power is sized by
hover; if it meets the condition only in part, the part that fails reopens the
corresponding bill. The condition does not mean that an architecture costs
nothing, and it does not claim that the trades it permits are favourable (Sup-
plement S2). It permits an energy store, itself mass carried for a brief duty
(the same principle, a continuous plant sized for cruise with the peak drawn
from a store, has been studied for winged tail-sitters [9] and for a single-aisle
airliner [17]); an electrical path that must still be rated to the hover peak;
the rotation of the airframe through ninety degrees, with the control author-
ity that requires; hardware installed for the vertical phase that serves both
regimes, which is outside Bill 1 but not free; and the efficiency lost when
one fixed geometry serves two operating points. Attitude hardware used in
both regimes does not stop the weight-carrying propulsors from meeting the
condition, but if it stays in the cruise flow without producing cruise thrust
it reopens Bill 2, and the instantiation is then partial. Section 4 prices each
of these where it falls.

2.4. A consistency check against published NASA sizing results
    An accounting proposed by the people who then apply it invites the
objection that the bills were chosen to suit a particular aircraft. One conse-
quence is therefore compared, before the aircraft is introduced, with a sizing
study produced independently: NASA’s set of urban-air-mobility concept
vehicles, sized with common tools to one mission of 1,200 lb payload over
75 nmi [18]. The prediction is that a dedicated lift group is paid for in gross

weight through the multiplier of Eq. (1), and that the cruise-efficiency credit
it buys does not cover that payment on a short mission.
     The closest isolation of Bill 1 in that set is the turbo-electric pair: a
lift-plus-cruise design with eight lift motors and a cruise motor, and a tilt-
wing with eight reoriented proprotors. They share the mission, payload,
propulsion architecture and a cruising wing. The tilt-wing is 9.4 percent
lighter (6,584 against 7,271 lb) at an effective lift-to-drag ratio 1.2 percent
higher (8.6 against 8.5). The published weight breakdown shows the transfer
of Table 2: of the 679 lb empty-weight difference, structure accounts for 716 lb
against the lift-plus-cruise design, the tilt-wing’s heavier propulsion returns
146 lb, the lift-plus-cruise design’s battery is 10 lb heavier, and 99 lb lies in
categories the source does not break out (Supplement S3). This is a category-
level consistency check on independent data, not a controlled experiment, and
the accounting predicts the direction, not the magnitudes. A quantitative fit
of Eq. (2) across all nine vehicles of the set was attempted and is too weak
to use (R2 = 0.69); it is reported in Supplement S3 as a negative result.

2.5. Sizing contracts
    Where one architecture pays less of one bill and more of another, a ranking
between them depends on how the bills are weighed, and a sizing contract is
such a weighing: it fixes what is held equal between the architectures. Range
in a sizing loop is R = ffuel E ∗ ηchain ηp (L/D)/g, with ηchain the fuel-to-shaft
efficiency and ηp (L/D) the effective lift-to-drag ratio, and three contracts
that differ only in the fuel fraction are used in Sec. 4:
  (a) fixed fuel fraction, ffuel = 0.16 of each architecture’s own takeoff mass;
  (b) fixed fuel mass, equal to the fuel this configuration carries;
  (c) fixed takeoff mass and payload, so that every kilogram of architecture-
       specific hardware is a kilogram of fuel not carried.
These are three different questions, not three estimates of one answer. Be-
cause E ∗ and ηchain are common, the range ratio of an architecture X to a
reference factors into an aerodynamic term and a contract term,

                    RX        ffuel,X                  (L/D)e,X
                         = re           ,       re =              ,           (3)
                    Rref      ffuel,ref                (L/D)e,ref

and the contract fixes only the second factor: it is 1 under (a), the inverse
ratio of takeoff masses under (b), and 1 − ∆fempty /ffuel under (c), where
∆fempty is the empty-mass fraction that X carries in excess of the reference

at the common takeoff mass. Under (a), Bill 1 does not enter the range
ratio at all; it appears only in takeoff mass. Under (c), X ranks ahead only
if re > ffuel /(ffuel − ∆fempty ), and the ranking moves from (a) to (c) by
100 re ∆fempty /ffuel percentage points, toward the lighter architecture. The
shift grows as the fuel fraction falls, so a small fuel fraction, as on a short
mission, weighs carried hover mass most heavily. These relations are conse-
quences of the range model used here and hold within it; they are not offered
as a general law of aircraft sizing.

3. Configuration and analysis methods
3.1. Configuration
    meryemAircraft is a tailless blended-wing body in which the whole air-
frame is the wing (Fig. 1). Leading-edge sweep falls from 45◦ at the root to
38.3◦ at the tip with the trailing edge held at 25◦ ; for the 50 kg reference
design the span is 3.453 m, the wing area 1.979 m2 and the aspect ratio 6.03.
Sweep places the outboard sections behind the centre of gravity, so that the
pitching moment comes from the lift distribution itself.
    The aircraft changes regime by rotating the airframe. It stands on its
tail with the longitudinal axis vertical, rests on five points (the lower ends
of four tip frames and the aft end of a centreline keel), takes off and hovers
in that attitude, and pitches the whole body through about ninety degrees
into wing-borne cruise. The propulsors keep one orientation relative to the
airframe throughout; what changes is the orientation of the airframe relative
to the flight path. The tip frames are at once the landing structure, the
mounts of the attitude rotors, the source of their moment arms and, through
their fairing, the aircraft’s only vertical surface, and they are charged to
the mass budget once. Dispensing with conventional landing gear improved
the empty-weight fraction of the 1950s tail-sitters [19]; the frame ends can
be moved outboard to widen the stance against ground wind, which also
lengthens the control arms.

Propulsion. Five stations carry ten rotors; each station is a coaxial counter-
rotating pair. One pair at the nose, 1.20 m in diameter, produces all propul-
sive thrust in both regimes; four pairs of 0.20 m sit at the ends of the tip
frames, which extend 0.71 m above and below the plane of the wing at each
tip. Every rotor has fixed pitch and its own electric machine; shaft speed

Figure 1: Three views of the 50 kg reference design.

is commanded, blade geometry and orientation are not. At equal counter-
rotating speeds the pairs produce no net reaction torque and nominally no
net angular momentum, so rotating the airframe induces no gyroscopic mo-
ment; each pair is torque-balanced at the cruise condition, which leaves a
small residual in hover (Sec. 5).
Power path. The power plant is a series hybrid: fuel to engine, engine to
generator, generator to the machines at the rotors. Because no rotor is
mechanically connected to the engine, the engine is sized by cruise, and the
difference between the hover peak and the cruise demand is supplied by a
battery buffer used only in the vertical phases.
Control. Body-axis names are used throughout; the longitudinal axis is the
roll axis in both regimes, so a moment about it appears as a heading change
in hover and as bank in cruise. Pitch and yaw come from differential thrust
of the tip pairs, at arms of 0.71 m (pitch) and 1.726 m (yaw, the semi-
span) (Fig. 2); the same differential thrust is assigned to rotate the airframe
through transition. Since every thrust vector is parallel to the roll axis,
no combination of thrust settings produces a roll moment. The reaction-
torque channel of the coaxial pairs could [7], but this configuration operates
every pair torque-balanced and assigns roll to a single modulated strip on
the lower surface, about 46 percent of which is estimated to lie in the nose-
pair slipstream and so to work at zero airspeed; the slipstream boundary is
not derived (Supplement S6). In hover the thrust axis has no aerodynamic
damping, and the strip’s own normal force in the nose-pair slipstream gives
0.6 to 1.4 N m about it. No handling-qualities standard consulted here states
a hover heading requirement for this class; as stated screens, a 90◦ rest-to-rest
heading turn in 10 s needs 1.6 N m and a heading rate of 20◦ s−1 reached in
1.5 s needs 5.8 N m. Moments of 6 to 12 N m would require a lift increment
of 0.1 to 0.2 on the half wing in the slipstream, which is assumed and not
predicted for this geometry. The strip’s hover heading authority is therefore
not established here. The reaction-torque channel this configuration declines
has the magnitude to cover the screens: a torque imbalance of one nose rotor
of 10 percent gives 2.5 to 2.7 N m, above the first, and of 30 percent 7.5 to
8.2 N m, above both; its cost in power and in the other axes is not computed
(Supplement S6). Directional stability comes from the fairing on the tip
frames, which needs a chord of 31 to 52 mm for lateral lift-curve slopes of
5.0 to 3.0 per radian [20]; attitude is to be closed by a flight computer whose
control loop is not designed here (Sec. 5).

 Figure 2: Control moment arms of the tip pairs: 0.71 m in pitch and 1.726 m in yaw.

Mechanism classes. Table 3 counts the mechanism classes that other hybrid
architectures use to change regime or to remove a rotor from one regime’s
flow. Beyond the rotation of the rotors, the only part of this aircraft that
changes configuration is the strip, deployable in two halves (one for roll,
both as a speed brake); the actuator inventory is the propulsion machines
plus the strip. A fixed structure is inherently less complex than a moving
mechanism, and this aircraft carries none of the mechanism classes of Table 3;
it is therefore mechanically simpler than a tilting architecture, though not
one in which nothing moves. No comparison of part count, mass or reliability
is made.

3.2. Analysis methods
Aerodynamics. The cruise drag polar is CD = CD0 + CL2 /(πAR e) with span
efficiency e = 0.817 from a vortex-lattice solution of the trimmed planform
(AeroSandbox 4.2.10 [21]). The zero-lift drag is a component build-up brack-
eted between 0.0285 and 0.0381 (Supplement S8): the bracket’s two ends
differ in the clean-surface and hub terms, and the adverse end carries a ten
percent margin on every item. Rotor–structure and rotor–wing interference
are not modelled; the upper end of the bracket is the only provision for

Table 3: Mechanism classes that change regime or remove a rotor from one regime’s flow.
 Mechanism class                         Required by                           Present here
 Pivot or tilting joint                  Tilting architectures                 No
 Nacelle or rotor-group actuator         Tilting architectures                 No
 Variable-pitch hub                      Rotors trimmed across two operat-     No
                                         ing points, or feathered
 Dedicated lift rotors                   Lift-plus-cruise architectures        No
 Rotor stowing, indexing or stop-        Removal of lift rotors from the       Noa
 ping mechanism                          cruise flow
        a
            The tip pairs free-wheel in cruise; a brake or lock would add this class.

them. The predictions of these methods diverge above about ten degrees
of incidence [22, 23], which does not affect the cruise point but bounds the
transition analysis.

Propellers. Nose and tip rotors are analysed by blade-element momentum
theory with section polars from NeuralFoil 0.3.3 [24]; the tip-rotor section is
a NACA 0012, chosen for the analysis rather than taken from a measured
blade. Four nose-blade families (two and three blades, design section lift
coefficients 0.55 and 0.70) meet the hover figure-of-merit requirement and
give cruise propeller efficiencies of 0.632 to 0.683; the blade family is a design
variable this study does not fix. The free-wheeling tip rotors, at zero shaft
torque, are charged as a drag term computed on section polars at a Reynolds
number of about 8 × 104 , a regime in which section drag is hard to predict
and which has not been measured for this configuration.

Sizing loop. Takeoff mass sets the cruise power, cruise power the engine rat-
ing, the engine rating the propulsion mass, and the propulsion mass the take-
off mass; the closed mass is the fixed point of Eq. (1), with a fuel fraction of
0.16, a 13 kg payload, wing loading 25.3 kg m−2 , disc loading 44.2 kg m−2 ,
airframe and avionics fractions of 0.30 and 0.08, and a battery buffer of 3.6
percent of takeoff mass. Hover power follows from momentum theory with
a figure of merit of 0.599; because disc loading is held fixed, disc area and
hover power scale in proportion to takeoff mass. Hover power does not size
the engine. All constants and relations needed to reproduce the closures, in-
cluding the fuel energy and the fuel-to-shaft chain, are listed in Supplement
Table S2a. Four closures span the drag bracket and the blade-family range.

Transition. The rotation into cruise is analysed in a three-degree-of-freedom
model in which a proportional–derivative controller drives the body angle
along a reference profile with the control moment limited to the 23 N m
available from the tip pairs, a rotation time of 2 s and an entry climb of
5 m s−1 ; the aerodynamic pitching moment is set to zero so that no favourable
moment is borrowed (Supplement S7).

Reproducibility. The code, inputs and scripts that produce every table are de-
posited with a DOI (Data availability). As a check that the text is sufficient,
the closures were re-implemented twice from the manuscript and supplement
of this version alone, frozen before the run, without access to the code, by two
separate generative AI assistants, each instructed to mark every input it had
to assume or back-solve. No input of Table S2a was back-solved; the one ex-
ception is the specific power of the bench-average store of Table 6, which one
re-implementation back-solved from the two masses at that store, and those
two values are not counted. Of the 58 tabulated values compared (Table 4,
Table 6 and Supplement Table S4a), that re-implementation reproduced ev-
ery counted value within 0.15 percent; the other reproduced 56 within 0.5
percent and those two within 0.72 percent, because Table 6 gave the store
as 1.5 rather than the 1.49 kW/kg used. That label, and the statement that
the empty fraction includes the buffer, which one re-implementation had to
infer, were corrected after the run. The frozen text, the list of compared val-
ues with their status, both re-implementations and a record of every change
made to the text after the freeze, none of which alters a compared value, are
deposited with the data (Data availability). This is a check of reproducibility,
not an external validation.

4. Results
4.1. Cruise efficiency
    At the cruise condition (30 m s−1 , CL = 0.450, 1.49 times the stall speed)
the aerodynamic lift-to-drag ratio is 8.79 at the adverse end of the drag
bracket and 10.82 at the favourable end, with the tip frames and free-wheeling
tip rotors already charged. Multiplied by the cruise propeller efficiency of the
four admissible blade families, 0.632 to 0.683, this gives an effective lift-to-
drag ratio (L/D)e = (L/D) ηp of 5.56 to 7.39 (Table 4). The first spread is
uncertainty; the second is a design variable this study does not fix. Across
the computed fixed-pitch blade families, the nose propeller efficiency is what

limits the cruise figure: at an assumed 0.85, not a computed value, the same
airframe would reach 7.47 to 9.20.
     The NASA sizing set of Sec. 2.4 gives effective lift-to-drag ratios for two
quadrotors and two helicopter types on a common mission [18]. Against
the turboshaft quadrotor (4.9) the effective lift-to-drag ratio of the present
configuration is 13 to 51 percent higher at every corner; closing that margin
would require a propeller efficiency of 0.557. Against the all-electric quadro-
tor (5.8) it ranges from 4 percent behind to 27 percent ahead. Against the
helicopters (5.4 to 7.2) the result is mixed. These corners carry the frame
drag of Table 4; across the drag sources of Supplement Table S4a the effective
lift-to-drag ratio spans 4.19 to 8.40, from 14 percent behind to 71 percent
ahead of the turboshaft quadrotor and from 28 percent behind to 45 percent
ahead of the all-electric one. These are figures from independently produced
analyses in a common definition, not a controlled comparison: the NASA
rotorcraft are 1,660 to 3,275 kg against 50 kg here, a scale that favours them;
they are quoted at best-range speed and this configuration at its cruise point
of 1.49 times stall, faster than its lift-to-drag optimum at 1.14 to 1.23 times
stall (Supplement S5); and they are sized at 5,000 ft and ISA+20◦ C against
sea level here, a mismatch whose direction has not been computed.

4.2. Sizing closure
     All four closures converge (Table 4); takeoff mass is the output and the
13 kg payload is fixed. The blade family that is best before the loop re-
mains best after it. Run on the reference design’s own assumed inputs, the
same loop reproduces that design within 1.5 percent in mass and exactly in
lift-to-drag ratio (Supplement S7). Closing the loop establishes that the con-
figuration is arithmetically self-consistent on the declared package; it does
not establish that the package exists (Sec. 4.6). Across the rotor-section and
frame-drag sources examined (Supplement Table S4a), the closures span 50.7
to 66.1 kg and 699 to 1,401 km, the envelope row of Table 4. Read as a mis-
sion, the four closures carry the 13 kg payload for 927 to 1,233 km at 30 m s−1 ,
which is 8.6 to 11.4 h of flight on the 0.16 fuel fraction with no reserve; at a
radius of 50 km, 7.7 to 10.5 h of that is on station, as an observation mission
such as wildfire monitoring would use it. These are sea-level values of the
model. At 2,000 m the computed nose-propeller efficiency falls by about 2
percent and the hover power at the rotor shaft rises by about 10 percent
(Supplement S7); the altitude penalty falls on the fixed-pitch propeller and
on the store, not on the airframe.

Table 4: Effective lift-to-drag ratio and the four closures of the sizing loop (50 kg reference
geometry, closed takeoff masses 52.3 to 57.5 kg, 13 kg payload, fuel fraction 0.16). Masses
and ranges hold only for a buffer delivering the specific power these closures imply (Sec. 4.6,
Table 6); ranges are modelled at sea level, not demonstrated.
                    CD0           ηp       L/D     (L/D)e    MTOW fempty Phover Peng          Range
                                                                kg         kW kW                km
A                 0.0381       0.632       8.79       5.56      57.5   0.614   12.53   5.17     927
B                 0.0381       0.683       8.79       6.00      55.8   0.607   12.17   4.65    1002
C                 0.0285       0.632      10.82       6.84      53.5   0.597   11.66   3.91    1141
D                 0.0285       0.683      10.82       7.39      52.3   0.592   11.40   3.54    1233
Envelopea 0.0235–0.0548 0.632–0.683 6.63–12.30 4.19–8.40 50.7–66.1       —       —      — 699–1401

fempty : empty fraction, including the 3.6 percent buffer; Phover : rotor-shaft hover power;
Peng : engine shaft rating. Ranges scale linearly with the fuel-to-shaft energy product of
   Table S2a. a Extremes over the rotor-section and frame-drag sources examined in
Supplement Table S4a: an envelope of those sources, not a confidence interval and not a
                                      further closure.

4.3. Where the three bills fall
Bill 2. In the drag build-up, the hardware the vertical phase leaves in the
cruise flow (the tip frames and the free-wheeling tip rotors) is 69 percent of
the zero-lift drag at the favourable end of the bracket and 57 percent at the
adverse end (50 to 69 percent across the two rotor sources with the frames
at 0.15, and 50 to 80 percent across all the drag sources of Supplement Table
S4a); the rotor term alone is 0.0154 at the favourable end. This is an estimate
resting on computed section polars at a Reynolds number of about 8 × 104 ,
not a measurement. Stopping the tip rotors offers no reduction: with the
rotor axis parallel to the cruise flow, a stopped fixed-pitch blade presents
the same projected area at any azimuth, and an edge-on state would require
feathering. Without the tip frames and rotors, the lift-to-drag ratio would
be 20.55 and 15.24; the configuration retains 52.6 and 57.7 percent of it.
Because range at fixed fuel fraction, propeller efficiency and chain efficiency
is proportional to the lift-to-drag ratio, the tip hardware costs 42.3 to 47.4
percent of the range the same airframe would reach without it; this prices the
drag and describes no other aircraft, since without the tip pairs the airframe
cannot hover. The tip discs are not reduced to cut this drag. With the
linear vortex-lattice pitching moment, the rotation completes at 23.0 N m,
the moment from the reference design’s assumed 16.2 N and 335 W per tip
pair; at 20.7 N m, the moment at the sizing figure of merit of 0.599 read as
the pair’s own value, it still completes, saturating for 0.57 s; it fails from
about 19 N m, so that margin is about 9 percent (Supplement S7). The same

pairs supply the takeoff margin.

Fixed-pitch efficiency. The cruise propeller efficiencies of 0.683 and 0.632
are 14.6 and 21.0 percent below the 0.80 the reference design assumed. No
variable-pitch counterfactual was computed, so the gap is not attributed to
the absence of a variable-pitch hub.

Bill 1. There is no dedicated lift group, so Bill 1 as defined is not incurred.
The energy buffer is a separate carried mass, 3.6 percent of takeoff mass (1.9
to 2.1 kg), carried for the whole flight to serve a demand that lasts about
a minute of it: the architecture converts power into mass, a cost the escape
condition permits but does not price. The buffer fraction is an input, not
a result; the deficit it must cover per kilogram of takeoff mass varies by 12
percent across the closures.

Bill 3. The engine is sized by cruise, 3.54 to 5.17 kW of shaft rating against
a hover demand of 11.4 to 12.5 kW at the rotor shaft. Bill 3, as defined in
Sec. 2.1, is therefore not incurred on the power plant. The electrical path
(machines, power electronics, wiring) still carries the full hover power and
must be rated to it; its mass is carried in the fixed propulsion fraction at the
reference design’s specific powers rather than re-rated in the loop, and its
heat rejection is not sized (Supplement S8).
    Between the 50 kg and 1,000 kg reference designs the rotor drag term falls
to 0.29 to 0.65 of its light-design value while the Bill 3 power ratio changes
by 5 to 14 percent, so within this model the two are not one quantity under
two names (Supplement S9).

4.4. Transition
    A point-mass model with the body angle driven kinematically loses no
altitude in a rotation entered in a 5 m s−1 climb. With rotational dynamics
and a finite control moment, and with the aerodynamic pitching moment set
to zero, the 50 kg design loses 5.4 to 6.6 m across three reference profiles
without saturating the control moment; raising the controller gains increases
the loss rather than removing it (16.9 m at sixteen-fold proportional and
four-fold derivative gain), again without saturation. A prediction would re-
quire the aerodynamic pitching moment through 18 to 22 degrees of inci-
dence, where the methods used here diverge; with a borrowed moment, some
models complete the rotation, some saturate the tip pairs and some tumble.

The transition is therefore computed but not settled; the profiles, gains and
borrowed-moment cases are defined in Supplement S7.

4.5. Rankings under three sizing contracts
     Two competitors are built on the same planform, mission (13 kg payload
at 30 m s−1 ), wing and disc loadings and energy chain, and carry the same
buffered series hybrid, so that Bill 3 is held common and the comparison
measures mass and drag. The lift-plus-cruise layout adds a lift group of
10 percent of takeoff mass and uses a lift-to-drag ratio transferred from a
wind-tunnel campaign on another airframe [15]; the tilting layout adds a
mechanism of 5 percent and is given no cruise penalty at all, which makes
it a bound rather than a design. Both are given a propeller efficiency of
0.80 against this configuration’s computed 0.632 to 0.683. None of these
competitor figures is measured.
     Under a fixed fuel fraction, this configuration closes 27 to 30 percent
lighter than the lift-plus-cruise layout, which cruises at a lift-to-drag ratio
of 11.66 to 15.72. The lift-plus-cruise layout’s range advantage is 55 to 84
percent under the fixed fuel fraction, 28 to 54 percent under fixed fuel mass,
and between −13 and +7 percent under fixed takeoff mass (Table 5). The
shift from the first contract to the third is 67 to 77 percentage points at ev-
ery closure and always toward the lighter aircraft, as the accounting predicts.
Under the third contract the sign changes inside the envelope: this configu-
ration leads at the two closures with the higher-efficiency blade family and
trails at the other two. Both statements are Eq. (3) evaluated at the closures:
the lift-plus-cruise layout has re = 1.55 to 1.84 and ∆fempty = 0.064 to 0.072,
which give the tabulated shifts to rounding, and its break-even ratio under
the third contract, 1.66 to 1.82, exceeds its re at exactly the two closures
where this configuration leads (Supplement S10). The agreement is an im-
plementation check of the loop against its own range model, not independent
evidence.
     The sign under a fixed takeoff mass is decided by quantities assumed
for the competitor rather than measured: with a lift group of 5 percent the
lift-plus-cruise layout leads under all three contracts, with 15 percent this
configuration leads under a fixed takeoff mass at every closure, and with
a common propeller efficiency this configuration leads under a fixed takeoff
mass at every closure (Supplement S10). Under the nominal assumptions
the shift is 67 to 77 percentage points at every closure; its direction, toward
the lighter aircraft, holds in every tested alternative, while its size does not

Table 5: Range of the lift-plus-cruise layout relative to this configuration (positive: lift-
plus-cruise ahead) under three sizing contracts, and its sensitivity to the competitor as-
sumptions. Shift: change from the first contract to the third.
Case           Fixed fuel fraction Fixed fuel mass Fixed takeoff mass                  Shift
Closure A                 +67.8%           +40.2%                +1.1%          66.8 points
Closure B                 +55.3%           +27.5%               −13.0%          68.3 points
Closure C                 +83.9%           +53.5%                +7.3%          76.6 points
Closure D                 +70.2%           +40.1%                −6.5%          76.7 points
Lift group          +55 to +84%      +47 to +76%          +36 to +65%       14 to 24 points
5% of take-
off mass
Lift group          +55 to +84%       +8 to +31%          −62 to −50% 117 to 134 points
15% of take-
off mass
Common              +33 to +45%       +6 to +17%          −33 to −25%       65 to 72 points
propeller
efficiency

(14 to 134 points). Which architecture ranks first under a given contract is
a statement about the contract and the competitor’s assumed masses and
propeller efficiency. Against the tilting bound, which pays no cruise penalty,
the tilting layout is 93 to 141 percent ahead under every contract; that margin
is the room a real tilting aircraft’s nacelle, pivot and rotor penalties would
have to fill, and no ranking is claimed against it. Without the common buffer,
with engines rated to hover, the lift-plus-cruise layout does not close under
the first or third contract.

4.6. Energy store
    At the closed masses the buffer must deliver 4.7 to 5.2 kW per kilogram of
buffer in hover and 5.5 to 6.1 kW/kg at takeoff with the tip pairs at full thrust.
For a battery pack flown in a 210 kg-class electric VTOL aircraft [25], the
13.5 kg test pack delivered 1.49 kW/kg on average over a four-minute bench
discharge at 10.68C; the test pack is rated at 0.724 kW/kg at its validated
continuous current of 110 A, and the onboard four-pack system is listed at
0.892 kW/kg at a continuous current of 4 × 110 A that is computed rather
than flown. The takeoff demand is 3.7 to 4.1 times the bench average and
6.2 to 6.8 times the listed continuous figure. A NASA-funded design study
assumes 4 kW/kg [26]. Re-closing the loop with the buffer derived from

the demand at a given specific power gives the takeoff masses of Table 6.
None of the stores reported as built in the sources consulted delivers the
required specific power. A case that “does not close” has no fixed point of
Eq. (1) (Supplement S7). Sized by power, the store also holds the energy of a
vertical event only if its specific energy is at least its specific power times the
event’s duration: 39 to 51 Wh/kg for 30 s at the hover and takeoff demands,
78 to 102 Wh/kg for 60 s. The cited test pack delivered 103 Wh/kg in its
bench discharge (1,394 Wh from 13.5 kg in 249 s), at about a quarter of the
specific power required here. The conditions under which the closures hold
are collected in Supplement Table S8a.

Table 6: Sizing loop re-closed with the buffer derived at a given specific power (all other
inputs as in Table 4).
 Buffer specific power          Takeoff mass     Buffer fraction   Change in takeoff mass
 5.5 to 6.1 kW/kg (im-        52.3 to 57.5 kg              3.6%                        —
 plied by Table 4)
 4 kW/kg (design-study        56.6 to 61.2 kg       5.0 to 5.5%           +6.5 to +8.2%
 assumption [26])
 1.49 kW/kg (bench aver-     94.6 to 101.2 kg     13.4 to 14.7%             +76 to +81%
 age [25])
 0.892 kW/kg (listed con-       about 335 kg         22 to 25%           +480 to +540%
 tinuous [25])
 0.724 kW/kg (test-pack        does not close                —                         —
 continuous [25])

5. Discussion
5.1. What generalizes
    Two results belong to the framework rather than to this aircraft, although
they are tested here only on this design and one NASA pair. First, the
accounting: the price of hover can be stated in three distinct costs before
any configuration is chosen, each remedy catalogued in Table 2 moves cost
between them or outside them, and the escape condition tests an architecture
against all three at once. Second, the dependence of rankings on the sizing
contract: when two architectures pay different bills, the ordering of their
ranges moves by tens of percentage points between reasonable contracts and
can change sign, so a range comparison is complete only with its contract and
its competitor assumptions stated. A third property concerns the method

rather than the aircraft: the text states every input needed to reproduce the
tables, and two blind re-implementations of the frozen text reproduced them
(Sec. 3.2).
    The configuration result is narrower. meryemAircraft meets the escape
condition in the propulsor that carries it and fails it in the attitude system:
the tip rotors that provide pitch and yaw, and the frames that carry them,
stay in the cruise flow without producing cruise thrust and together account
for 57 to 69 percent of the zero-lift drag with the baseline rotor source and the
frame drag assumed here, 50 to 69 percent across the two rotor sources, and
50 to 80 percent across the drag sources examined (Supplement Table S4a).
The accounting thus shows where the configuration should be improved next,
in the drag of the attitude system, rather than certifying it.

5.2. Limitations
    The results rest on analysis; no aircraft has been built or flown and no
wind tunnel has been run on this geometry. The limitations below are the
ones that would most change the numbers or the feasibility; the full list,
with what each bears on and what would settle it, is in Supplement S11, and
each headline claim is set against its evidence and what would refute it in
Supplement Table S0.
    • Energy store. The required buffer specific power is 3.7 to 4.1 times the
      bench average of the cited battery; re-closed at that bench average the
      package becomes 76 to 81 percent heavier, and at the listed continuous
      figure 5.8 to 6.4 times as heavy (Table 6). Sized by power, the store
      holds about a minute of vertical flight only if it keeps, at four times the
      bench rate, the specific energy the cited pack delivered at the bench
      rate; no reserve is included.
    • Transition and landing. The rotation into cruise is computed with the
      aerodynamic pitching moment set to zero and is not settled; the landing
      transition is not the takeoff run backwards and has not been analysed
      (Supplement S4), and the vortex ring state in the vertical descent has
      not been assessed.
    • Control. Attitude control is sized but not closed as a loop. Declining
      the reaction-torque channel has a cost in authority and response that
      is not computed; each pair is torque-balanced in cruise, leaving a small
      hover residual whose absorption is not shown; the tip pairs supply both
      the takeoff margin and the attitude authority; rejection of wind gusts in
      hover, where the vertical wing presents its full area, is not analysed; and

     the strip’s computed hover authority about the thrust axis falls below
     both stated heading screens, so hover heading control is not established
     (Sec. 3.1).
   • Drag. The tip-rotor term rests on computed section polars near a
     Reynolds number of 8×104 and falls from 0.0154 to 0.0104 with a second
     section source [27]; the frames are charged at a frontal drag coefficient
     of 0.15 where a subcritical estimate gives 0.42 to 0.68 [28]. Across
     these sources the closures span 699 to 1,401 km (Table 4, envelope
     row). Rotor–structure and rotor–wing interference are not modelled.
   • Mass and power. The airframe fraction of 0.30 is a construction con-
     stant, not a structural sizing; the hover-rated electrical path is carried
     in a fixed fraction at assumed specific powers and its heat rejection
     is not sized; engine installation is absent; and the engine thermal effi-
     ciency of 0.28 inside the range figures is optimistic for an engine of 3.5
     to 5.2 kW.
   • Scope. All numbers are at sea level; only the 50 kg design is closed,
     and the 1,000 kg reference design is used only for the scale comparison.
     With a 13 kg payload, the missions the design serves are observation
     and small cargo; it is not sized for fire suppression.

6. Conclusions
    meryemAircraft changes between hover and cruise by rotating the whole
airframe, with fixed-pitch coaxial pairs that keep one body-relative orienta-
tion, and so carries none of the mechanism classes a tilting architecture uses
to change regime; in that sense it is mechanically simpler, though not an
aircraft in which nothing moves. Priced in three costs of hover, carried hover
mass, exposed cruise drag and power sized to the hover peak, the architecture
meets the escape condition in the nose pair that carries it and pays in the
attitude system: the tip rotors and the frames that carry them, kept in the
cruise flow, account for 50 to 80 percent of the zero-lift drag across the drag
sources examined, which is where the configuration should be improved. A
50 kg design closes consistently at 52.3 to 57.5 kg, with an envelope of 50.7
to 66.1 kg and 699 to 1,401 km across those sources, and its range ranking
against a lift-plus-cruise layout shifts by 67 to 77 percentage points across
three sizing contracts, changing sign under one of them for the competitor
assumptions used. The package depends on an energy store whose required
specific power has not been demonstrated; the strip’s hover heading authority

is not established; and the transition and landing remain to be shown.

Declaration of competing interest
    The authors are the inventors and applicants of Turkish patent applica-
tion TR 2026/014570 (filed 26 August 2026 with the Turkish Patent and
Trademark Office), which concerns the tail-sitting blended-wing-body air-
craft and the roll-control strip described in this paper. The authors declare
no other competing interests.

Funding
   This research did not receive any specific grant from funding agencies in
the public, commercial, or not-for-profit sectors.

Data availability
    The analysis code (archived from https://github.com/LORDTEK/merye
mAircraft), the manuscript sources, the scripts of the drag-source and tran-
sition checks, and the frozen text, compared-value list, prompt, scripts and
outputs of the re-implementation described in Sec. 3.2 are openly available
on Zenodo (https://doi.org/10.5281/zenodo.23754355).

Declaration of generative AI and AI-assisted technologies in the
manuscript preparation process
    The concept, architecture, design and solution approach of this work are
the authors’ own. During the preparation of this work the authors used
generative AI assistants as tools: to draft and revise the English text, to
search and check the literature, to review the manuscript, and to write and
check analysis code. Two of these assistants were also used, as described
in Sec. 3.2, to re-implement the sizing closures from the manuscript text as
a reproducibility check. After using these tools the authors reviewed and
edited the content as needed and take full responsibility for the content of
the published article.

References
[1] Bacchini, A., and Cestino, E., “Electric VTOL Configurations Compar-
    ison,” Aerospace, Vol. 6, No. 3, 2019, Paper 26. https://doi.org/10
    .3390/aerospace6030026
[2] Anderson, S. B., “Historical Overview of V/STOL Aircraft Technology,”
    NASA TM-81280, March 1981.
[3] De Wagter, C., Ruijsink, R., Smeur, E., van Hecke, K., van Tienen, F.,
    van der Horst, E., and Remes, B., “Design, Control, and Visual Nav-
    igation of the DelftaCopter VTOL Tail-Sitter UAV,” Journal of Field
    Robotics, Vol. 35, No. 6, 2018, pp. 937–960. https://doi.org/10.100
    2/rob.21789
[4] Oosedo, A., Abiko, S., Konno, A., Koizumi, T., Furui, T., and
    Uchiyama, M., “Development of a Quad Rotor Tail-Sitter VTOL UAV
    without Control Surfaces and Experimental Verification,” 2013 IEEE
    International Conference on Robotics and Automation (ICRA), IEEE,
    Karlsruhe, Germany, 2013, pp. 317–322. https://doi.org/10.1109/
    ICRA.2013.6630594
[5] Escareño, J., Sanchez, A., Garcia, O., and Lozano, R., “Modeling and
    Global Control of the Longitudinal Dynamics of a Coaxial Convertible
    Mini-UAV in Hover Mode,” Journal of Intelligent and Robotic Systems,
    Vol. 54, Nos. 1–3, 2009, pp. 261–273. https://doi.org/10.1007/s108
    46-008-9265-y
[6] Wang, J., Song, B., and Wang, L., “L1 Adaptive Attitude Controller for
    a Tail-Sitter MAV in Hover Flight,” 29th Congress of the International
    Council of the Aeronautical Sciences, St. Petersburg, Russia, 2014, Pa-
    per ICAS 2014-0529.
[7] Zhang, D., Chen, Z., and Lv, J., “Lift System Design of Tail-Sitter
    Unmanned Aerial Vehicle,” Intelligent Control and Automation, Vol. 3,
    No. 4, 2012, pp. 285–290. https://doi.org/10.4236/ica.2012.34033
[8] Pathak, S., “Design of Flying Wing Tail Sitter Contra-Rotating Propeller
    VTOL Sky Swift V1.0 UAV,” Journal of Informatics Education and
    Research, Vol. 5, No. 2, 2025, pp. 6268–6278. https://doi.org/10.5
    2783/jier.v5i2.3173

 [9] Rohith, S. K., Sridharan, A., and Govindarajan, B., “Hybrid Powertrain
     Systems for 100 kg Multicopters and Tailsitters,” Journal of Aircraft,
     Vol. 63, No. 2, 2026, pp. 575–591. https://doi.org/10.2514/1.C038
     443

[10] Vegh, J. M., “Hybrid-Electric Design Studies for a Long-Endurance Tail-
     sitter Concept,” AIAA Paper 2025-1436, Jan. 2025. https://doi.org/
     10.2514/6.2025-1436; correction notice https://doi.org/10.2514/
     6.2025-1436.c1

[11] Escareño, J., Stone, R. H., Sanchez, A., and Lozano, R., “Modeling and
     Control Strategy for the Transition of a Convertible Tail-Sitter UAV,”
     Proceedings of the European Control Conference 2007, Kos, Greece,
     2007, pp. 3385–3390. https://doi.org/10.23919/ECC.2007.7068919

[12] Yang, Y., Zhu, J., Zhang, X., and Wang, X., “Active Disturbance
     Rejection Control of a Flying-Wing Tailsitter in Hover Flight,” 2018
     IEEE/RSJ International Conference on Intelligent Robots and Sys-
     tems (IROS), IEEE, Madrid, Spain, 2018, pp. 6390–6396. https:
     //doi.org/10.1109/IROS.2018.8594470

[13] Liebeck, R. H., “Design of the Blended Wing Body Subsonic Transport,”
     Journal of Aircraft, Vol. 41, No. 1, 2004, pp. 10–25. https://doi.org/
     10.2514/1.9084

[14] Merical, K., Beechner, T., and Yelvington, P., “Hybrid-Electric, Heavy-
     Fuel Propulsion System for Small Unmanned Aircraft,” SAE Interna-
     tional Journal of Aerospace, Vol. 7, No. 1, 2014, pp. 126–134. https:
     //doi.org/10.4271/2014-01-2222

[15] Bacchini, A., “Electric VTOL Preliminary Design and Wind Tunnel
     Tests,” Ph.D. Dissertation, Dept. of Mechanical and Aerospace Engi-
     neering, Politecnico di Torino, Turin, Italy, 2020.

[16] Mathur, A., and Atkins, E., “Wind Tunnel Testing and Aerody-
     namic Characterization of a QuadPlane Uncrewed Aircraft System,”
     arXiv:2301.12316v1, Jan. 2023. https://doi.org/10.48550/arXiv
     .2301.12316

[17] Rheaume, J. M., and Lents, C., “Energy Storage for Commercial Hybrid
     Electric Aircraft,” SAE Technical Paper 2016-01-2014, 2016. https:
     //doi.org/10.4271/2016-01-2014

[18] Johnson, W., and Silva, C., “NASA Concept Vehicles and the Engineer-
     ing of Advanced Air Mobility Aircraft,” The Aeronautical Journal, Vol.
     126, No. 1295, 2022, pp. 59–91. https://doi.org/10.1017/aer.2021
     .92

[19] Nelms, W. P., and Anderson, S. B., “V/STOL Concepts in the United
     States: Past, Present, and Future,” NASA TM-85938, April 1984.

[20] Donlan, C. J. (compiler), “An Interim Report on the Stability and Con-
     trol of Tailless Airplanes,” NACA Report 796, 1944.

[21] Sharpe, P. D., “AeroSandbox: A Differentiable Framework for Aircraft
     Design Optimization,” S.M. Thesis, Dept. of Aeronautics and Astronau-
     tics, Massachusetts Institute of Technology, Cambridge, MA, 2021.

[22] Panagiotou, P., Dimopoulos, T., Dimitriou, S., and Yakinthos, K.,
     “Quasi-3D Aerodynamic Analysis Method for Blended-Wing-Body UAV
     Configurations,” Aerospace, Vol. 8, No. 1, 2021, Paper 13. https:
     //doi.org/10.3390/aerospace8010013

[23] Wang, K., and Zhou, Z., “Aerodynamic Design, Analysis and Validation
     of a Small Blended-Wing-Body Unmanned Aerial Vehicle,” Aerospace,
     Vol. 9, No. 1, 2022, Paper 36. https://doi.org/10.3390/aerospace9
     010036

[24] Sharpe, P. D., and Hansman, R. J., “NeuralFoil: An Airfoil Aero-
     dynamics Analysis Tool Using Physics-Informed Machine Learning,”
     arXiv:2503.16323, 2025. https://doi.org/10.48550/arXiv.2503.
     16323

[25] Yu, S., Jung, Y.-J., Cho, B.-D., and Lee, G.-S., “Design, Fabrication, and
     In-Flight Demonstration of a 24S NCM Battery System for an eVTOL
     Aircraft,” Batteries, Vol. 12, No. 9, 2026, Paper 317. https://doi.or
     g/10.3390/batteries12090317

[26] Barrett, S. R. H., Brown, A., and Gomez-Vega, N., “Silent, Solid-State
     Propulsion for Advanced Air Mobility Vehicles,” NASA Innovative Ad-
     vanced Concepts Phase I Final Report, Massachusetts Institute of Tech-
     nology, Cambridge, MA, 2023.

[27] Sheldahl, R. E., and Klimas, P. C., “Aerodynamic Characteristics of
     Seven Symmetrical Airfoil Sections Through 180-Degree Angle of At-
     tack for Use in Aerodynamic Analysis of Vertical Axis Wind Turbines,”
     SAND80-2114, Sandia National Laboratories, Albuquerque, NM, 1981.
     https://doi.org/10.2172/6548367

[28] Hoerner, S. F., Fluid-Dynamic Drag, published by the author, Midland
     Park, NJ, 1965.
```
