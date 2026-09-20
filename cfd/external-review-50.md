# Round 46 — you falsified the gap and you were right; a boundary on the source rule; and step 5, unreviewed

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`5460d51`** (the commit that introduces step 5; this briefing itself lands one commit later).

```
paper/v8/01-the-gap.md             SHA-256 1cf73e40120f0c93d1e36a5028780ae3af0d9ea8386fd6a62726c3b249124b00
paper/v8/05-the-first-half.md      SHA-256 a20ced694cba23fade532021d0fe10d1f642cd9c387206c602f2a98898ac72f3
paper/v8/07-the-combination.md     SHA-256 1359dde5687358ff90002cccf195e94955bc70bcc5d580d5c2be58a53ea3c739
paper/v8/09-what-is-not-claimed.md SHA-256 e402350b84dcada3c993c69a9770e94abc4eef5b737cf19bf61b4161ff8a3f7d
paper/prior-art-finding.md         SHA-256 a52c7b86f8e1ab6fec7d40e546bb3fa21b19b6464ddba496d2a12009027389a5
```

**Two things are in front of you this round, as usual: a page that has been through your
criticism, and a page that has not.** Section 5 is the mature one — step 1, rewritten after you
falsified it. Section 6 is the fresh one — **step 5, first writing, never reviewed.**

**The documents you linked are in the repository**, under `cfd/`: the two NASA V/STOL reviews,
the DelftaCopter paper, and the SkySwift paper.

---

## 1. **The gap statement was false. Three of you found it and you were right.**

Step 1 said:

> *"The route that refuses both … was flown once, in 1954 … and **has not been revisited as a
> design proposition** since the constraints that stopped it were removed."*

and

> *"**Every** architecture that puts one set of hardware into both regimes does so by
> reorienting the propulsors."*

**Grok, ChatGPT and DeepSeek each said, independently, that both sentences are false.** The two
documents were uploaded and read here first-hand. **They are false.**

### What the DelftaCopter paper contains

Its introduction is, in effect, a literature survey of exactly this design space:

- Early hybrid tail-sitters were *"combinations of fixed-pitch quad-rotor helicopters with a
  flying wing… four propellers and typically two aerodynamic actuators."*
- **Oosedo et al., ICRA 2013:** *"Development of a quad rotor tail-sitter VTOL UAV **without
  control surfaces** and experimental verification."*
- **Escareno et al. (2007, 2008):** a **coaxial dual propeller** tail-sitter, proposed
  specifically to remove the reaction torque a single propeller imposes, *"at the cost of an
  extra motor and coaxial system."*
- And, directly: *"the fixed-pitch propellers make it **theoretically impossible** to be very
  efficient in both hovering and forward flight."*

**That last line lands on this project's own propeller result.** The paper's own propulsion
section calls its rotor *"a **compromise** between efficient hover and efficient forward
flight"* and picks its diameter on that basis, in 2018.

> **ChatGPT was right about what this means, and the correction is adopted.** The *phenomenon*
> we computed two weeks ago is a known result in this literature. **We did not discover it. We
> quantified it for this architecture and carried it through the sizing loop.** The claim is now
> written that way — measured and charged, not discovered — and the note is at the head of the
> finding record.

### What the SkySwift paper contains

*"A hybrid flying-wing tailsitter UAV designed specifically for **disaster management and rapid
response** … The airframe is a **blended wing-body**, with forward-swept wings … uses a
**contra-rotating pusher** configuration."* Four of our own elements, in one 2025 title.

Reading it does produce a distinction, and it falls exactly where this paper's claim is:
**SkySwift uses aerodynamic control surfaces** — its own method section validates *"control
surface and propeller effectiveness."* It is battery-powered, and it carries no mass build-up,
no sizing closure and no architectural accounting.

**That is a real difference and it is not enough to rescue the original sentence.** The
configuration is in print.

---

## 2. What the gap says now

**Step 1 now names what is already occupied *before* it names the gap**, which is the only
honest order. Four things, each from a document in the repository: uncrewed tail-sitters are
ordinary; a tail-sitter without control surfaces was reported with experimental verification in
2013; coaxial contra-rotating tail-sitter propulsion was proposed to kill reaction torque;
a blended-wing-body tail-sitter for disaster response was reported in 2025. And the fixed-pitch
compromise is a known result.

**The gap is no longer historical.** It is the combination *together with its price*:

> a blended-wing-body tail-sitter in which **every** propulsor is a coaxial, torque-balanced
> pair — so that **reaction torque and net angular momentum are given up along with the
> reorientation mechanism** — carrying no aerodynamic control surfaces beyond a single moving
> device, powered through a buffered series hybrid, and audited explicitly against carried hover
> mass, exposed cruise drag and hover-sized continuous power, at two scales and under three
> sizing contracts.

**And the giving-up is named as the cost it is.** A torque-balanced coaxial pair cannot produce
a rolling moment by any setting. **Oosedo's four separate rotors can** — that is what reaction
torque buys. This configuration declines it deliberately, and pays the strip for it. That trade
was not found in the literature; it is stated as *not found* rather than as *not existing*.

Steps 7 and 9 have had their novelty language corrected to match. Step 9 now says explicitly
that the configuration **is not claimed to be without precedent** and points at Section 1.

---

## 3. **A boundary on the source rule — because it is costing more than it is worth in places**

The author's report, given plainly:

> *"I was able to open one of ChatGPT's sources but could not download it to upload for you.
> I could not open either of DeepSeek's two. I could not download Qwen's two either… **It turns
> out this makes a lot of work.** I do not know how we should do it."*

**The rule is not being withdrawn. It has paid for itself twice in two rounds, in opposite
directions** — Round 45 it confirmed our numbers against four contradictory reports; Round 46 it
destroyed our gap claim before a referee could. Both are the same rule working.

**But it now has a boundary, and it is the author's instruction for every round from here:**

> **A PDF is asked for only where a document could REFUTE a claim:**
> **(a) priority and novelty claims** — every sentence that says something has not been done;
> **(b) numbers** — every value taken from a table;
> **(c) verbatim quotations.**
>
> **No PDF is asked for opinion, judgement, structural suggestion or criticism of the writing.**
> Most of the value in these rounds comes from exactly those, and none of them needs a source.

**And the counterpart stands:** a number whose document you did not open **this round** is not
used. If you cannot open it, say so and give no number. Four hedged numbers is what Round 43
cost.

**One practical request.** Where a document is hard to reach, a verbatim quotation plus the
table or page number is worth more than a link that fails. The quotation can be checked against
the file once anyone obtains it; a dead link cannot.

---

## 4. **A rule this project has now written for itself**

Recorded in the project file, because the cost was real:

> Before writing *"has not been done"*, *"the only"*, *"the first"*, or *"has not been
> revisited"* — **search first.** Not finding something is not evidence that it is not there,
> so the claim is written as **"not found"**, with the place that was searched named.
>
> And a gap does not weaken by narrowing. The correct form is: **name what is already occupied
> first**, then describe what is missing **as a combination with its price.**

---

## 5. Step 1 as it now reads, from the section that changed

> ### What is already occupied, stated before the gap
>
> It would be easy, and wrong, to present the third route as an empty field. **It is not**, and
> the paper is better for saying so first.
>
> **The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a
> flying wing have been built and flown for more than a decade, beginning with quadrotor-plus-wing
> arrangements carrying a few aerodynamic actuators for forward flight.
>
> **Attitude without aerodynamic control surfaces is established.** A quadrotor tail-sitter
> operated without control surfaces, with experimental verification, was reported in 2013.
>
> **Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed specifically to
> remove the reaction torque a single propeller imposes, at the cost of an extra motor and the
> coaxial arrangement.
>
> **A blended-wing-body tail-sitter with contra-rotating propulsion, aimed at disaster response,
> is established**, reported in 2025 with vortex-lattice and RANS analysis of its planform,
> winglets and transition.
>
> **And the propeller compromise at the centre of this paper's own ledger is a known result, not a
> discovery.** The uncrewed tail-sitter literature states it directly: fixed-pitch propellers make
> it *"theoretically impossible to be very efficient in both hovering and forward flight."* A
> long-range tail-sitter reported in 2018 describes its own rotor as *"a compromise between
> efficient hover and efficient forward flight"* and selects its diameter on exactly that basis.
>
> ### The gap, stated precisely
>
> **Each half of the required capability is well served, and both halves together are served by
> the contemporary hybrids.** This paper does not claim otherwise. **And the third route is
> occupied.** What follows is therefore not a claim to an empty field.
>
> **What is not established is the combination taken together with its price.** Specifically:
> a blended-wing-body tail-sitter in which *every* propulsor is a coaxial, torque-balanced pair —
> so that reaction torque and net angular momentum are given up along with the reorientation
> mechanism — carrying no aerodynamic control surfaces beyond a single moving device, powered
> through a buffered series hybrid, and **audited explicitly against carried hover mass, exposed
> cruise drag and hover-sized continuous power**, at two scales and under three sizing contracts.
>
> Each of those choices costs something, and **the giving-up is the part that is not free**: a
> torque-balanced coaxial pair cannot produce a rolling moment by any setting, which the quadrotor
> tail-sitters can. What that costs, and what the rest of the combination costs, is what the paper
> is for.
>
> **None of the elements is new**, and Section 7 says so. Tail-sitting aircraft are seventy years
> old and uncrewed ones are ordinary; blended wing bodies have been a standing subject of transport
> research for three decades; series-hybrid propulsion has established precedent in small uncrewed
> aircraft. **What this paper offers is the combination, the consequences of the choices inside it,
> and an accounting of what they cost** — not a claim that the route was waiting to be found.
>
> Section 2 states the cost that any architecture in this corner pays, in terms that do not
> presume an escape.
>
> ---

---

## 6. **Step 5 — the first half, first writing, not yet reviewed**

**What it is for.** The first of the two halves the combination is made of: operation without a
runway, against the fixed-wing family, on that axis only.

**ChatGPT's Round 45 condition is what the page is built around**, and it is worth repeating
because it changed the shape of the section:

> *"Don't make Step 5 'prove' that your aircraft has vertical capability yet. It should
> establish the fixed-wing opponent and the mission-level capability requirement, then say what
> is sized versus demonstrated."*

So the page does four things and refuses a fifth.

**It fixes the axis and refuses the other one in its first paragraph.** Nothing is claimed
against fixed-wing aircraft on range or cruise efficiency, where the runway-launched aeroplane
is the better machine and pays none of Section 2's charges.

**It states the requirement in its stronger form before claiming to meet it.** A catapult also
leaves without a runway; what it does not do is bring the aircraft *back* to the same unprepared
site, and it does not travel. The requirement is therefore that the aircraft carries everything
needed to depart and recover, and **the site supplies nothing — including the reaction surface
for a landing gear.** A net, a cradle, a prepared strip or a recovery vehicle each fail it.

**It gives the saving to its source rather than to this paper.** The inversion — landing
structure that is also control structure — has precedent in the NASA record: *"dispensing with a
conventional landing gear improved the empty weight fraction for these VATOL aircraft."*

**And the sized-versus-demonstrated split is the centre of the page, not a closing caveat.**
Four things are named as not demonstrated, and none is softened:

1. **The aircraft leaves the ground on its control propellers.** The primary propulsor is sized
   at thrust equal to weight and no more; the margin comes from the tip pairs, which compete for
   it with the attitude authority.
2. **The vertical descent has not been analysed** — whether the descent profile enters the
   vortex ring state is open.
3. **Neither has the landing transition**, and the page says why the forward model cannot be
   reused: going out, the rotation builds dynamic pressure while it turns; coming back, lift is
   leaving while the thrust vector has not yet returned to vertical. **No figure in this paper
   describes the landing transition.**
4. **Crosswind exposure on the ground is inherited, not removed.** The stance base is the answer
   offered, and it is a parameter rather than a proof.

**And the historical credit is kept to exactly what it covers.** Removing the pilot disposes of
the spatial-orientation objection — height above ground is a sensor measurement now — **and
nothing else.** Precise hovering, ground gusts and the descent are not disposed of by removing
the pilot, and the page says so in those words.

---

## 7. Step 5, first writing

> ### The first half: operation without a runway
>
> ### The opponent, and the axis
>
> On this axis the alternative is the fixed-wing aircraft, and the comparison runs one way only.
> **Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency**, where a
> runway-launched aeroplane that never bought vertical capability pays none of the charges of
> Section 2 and is the better machine. The claim is confined to the one thing that family cannot
> do: leave from, and return to, a site that has not been prepared.
>
> ### What the requirement actually is
>
> "Vertical take-off" is a weaker requirement than the one the missions impose, and stating the
> stronger one first prevents the claim from being read as easier than it is.
>
> A catapult-launched fixed-wing aircraft also leaves without a runway. What it does not do is
> **come back** to the same unprepared site, and it does not travel without the launcher. The two
> applications this work is aimed at — wildfire observation and response, and cargo delivery to
> places without a runway — need the aircraft to arrive somewhere that has no infrastructure, and
> to leave again.
>
> So the requirement is: **the aircraft carries everything it needs to depart and recover, the
> site supplies nothing, and what the site supplies nothing of includes the landing gear's
> reaction surface.** A net, a catapult, a cradle, a prepared strip or a recovery vehicle each
> fail it.
>
> ### How the configuration meets it
>
> The aircraft stands on its tail, with its longitudinal axis vertical, in its own storage
> attitude. **No launch equipment is present.** It rests on five points: the four lower ends of
> the tip frames and the aft end of a keel running along the centreline.
>
> **Those five points are not added hardware.** The tip frames are the landing structure, and
> they are also the structure that carries the attitude propellers and sets their moment arm. One
> structure serves three purposes and is charged to the mass budget once.
>
> **The saving has precedent and it is not this paper's observation.** Reviewing the tail-sitters
> of the 1950s, NASA recorded that *"dispensing with a conventional landing gear improved the
> empty weight fraction for these VATOL aircraft"*, while noting that some form of gear was still
> required on the tail surfaces. The present arrangement takes that benefit and extends it by
> giving the same structure the control duty as well.
>
> **And the stance base is a parameter rather than a constraint.** Moving the frame ends further
> outboard widens the base against ground wind without altering the planform, the propulsion or
> the control architecture — and because the same displacement lengthens the control moment arm,
> both benefits arrive from one change. The reference geometry is one point on that trade; an
> operator with a stronger ground-wind requirement can take another.
>
> ### What is sized, and what is not demonstrated
>
> This is the part of the section that decides whether the rest of it can be trusted.
>
> **Sized.** The vertical phase is sized: hover power from momentum theory at thrust equal to
> weight, the buffer that supplies the difference between that peak and the cruise demand, the
> tip-frame lengths that set both the stance base and the control arms, and the structure that
> carries the landing loads. Those numbers exist, they close, and Section 10 reports the closure
> together with the margin it has.
>
> **Not demonstrated, and the list is not short.**
>
> **The aircraft leaves the ground on its control propellers.** Hover power is sized at thrust
> equal to weight, so the primary propulsor supplies a thrust-to-weight ratio of exactly one and
> no more. The take-off margin comes from the four tip pairs, which were sized from the moment
> requirement rather than from weight support. That is the one place the configuration asks a
> component to do a second job it was not sized for, and it means the take-off margin and the
> attitude authority are drawn from the same four propellers and compete for it.
>
> **The vertical descent has not been analysed.** A rotor descending into its own wake can enter
> the vortex ring state, in which thrust becomes erratic and adding power makes matters worse.
> Whether this configuration's descent profile enters that region, and at what rate of descent,
> is an open question in Section 14 rather than an answered one here.
>
> **Neither has the landing transition.** The forward rotation and the reverse are not symmetric
> and must not be assumed to be. Going out, the rotation builds dynamic pressure while it turns,
> so lift arrives to replace the vertical component of thrust as that component falls. Coming
> back, the race runs backwards: dynamic pressure is falling while the aircraft is being turned,
> so lift is leaving at the moment the thrust vector has not yet returned to vertical. **A model
> built for the first case cannot be read for the second by changing a sign, and no figure in this
> paper describes the landing transition.**
>
> **And one historical difficulty is inherited rather than removed.** A tail-sitting aircraft on
> the ground is more exposed to crosswind than a conventional one. The stance base is the answer
> this configuration offers, and it is a parameter rather than a proof.
>
> ### What the historical record does and does not give back
>
> One of the 1954 objections is genuinely removed and it should be named exactly. The XFY-1's
> landing difficulty was attributed to a pilot judging a backwards vertical descent by looking
> over his shoulder, to turbulence sensitivity and to reduced control power near touchdown.
> **There is no pilot here, and height above ground is a sensor measurement rather than a human
> estimate.** That disposes of the spatial-orientation objection and nothing else. **Precise
> hovering, ground gusts and the descent itself are not disposed of by removing the pilot**, and
> this section does not pretend otherwise.
>
> ### What this half costs
>
> Runway independence is not obtained free, and the charges appear later rather than here. The
> tip frames that make the aircraft self-supporting are structure standing in the cruise
> airstream, and Section 11 charges their drag. The attitude propellers they carry are exposed
> for the whole cruise and cannot be feathered, and Section 11 charges that too. The buffer that
> releases the engine from the hover peak is mass carried for the whole flight.
>
> **The second half — cruise carried on a wing rather than on rotors — is the subject of the next
> section**, and the two are combined in Section 7.
>
> ---

---

## 8. What I am asking of you

**Q1 — Is the narrowed gap defensible, or has it narrowed into a non-claim?** It now says: the
route is occupied, the elements are old, the phenomenon we measured was known — what is not
found is this combination with its accounting. **Is that a paper, or is it a design study
wearing a framework?** Answer honestly; this is the question the correction raises.

**Q2 — Is anything in the new "what is already occupied" section wrong or incomplete?** Four
items, each from a repository document. **What else belongs there?** If a fifth thing is
occupied and we have not named it, naming it now is cheaper than a referee naming it later.
Under the new boundary, this question **does** warrant a PDF, because it is a priority claim.

**Q3 — The coaxial torque-balance trade.** The claim that separates this configuration from the
quadrotor tail-sitters is that every pair is torque-balanced, so reaction torque is unavailable
and roll must come from a surface. **Has anyone else given up reaction torque this way on a
tail-sitter, and paid an aerodynamic device for roll?** Not found here; that is not the same as
not existing.

**Q4 — Anything false**, in step 1 as rewritten, or in steps 7 and 9 as corrected.

**Q5 — On step 5 specifically.** Three questions, and the third is the one that matters:
does the page establish the requirement without claiming to have met it? Is the
sized-versus-demonstrated split honest, or is anything hiding on the sized side that belongs on
the other? **And is the four-item "not demonstrated" list complete — what is missing from it?**

**Q6 — Step 6 next**, the second half: wing-borne cruise, opponent multirotors. Unless the
falsified gap moves something.

---

## 9. Where the work stands

Eight steps written: 1, 2, 3, 4, **5**, 7, 8, 9. **The architecture is unchanged.** What changed this
round is the size of the claim around it, and it changed in the direction the evidence pushed.

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper.
