# Round 46 — you falsified the gap, and you were right. Plus a boundary on the source rule, because it is costing more than it should.

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`2f09538`**.

```
paper/v8/01-the-gap.md             SHA-256 1cf73e40120f0c93d1e36a5028780ae3af0d9ea8386fd6a62726c3b249124b00
paper/v8/07-the-combination.md     SHA-256 1359dde5687358ff90002cccf195e94955bc70bcc5d580d5c2be58a53ea3c739
paper/v8/09-what-is-not-claimed.md SHA-256 e402350b84dcada3c993c69a9770e94abc4eef5b737cf19bf61b4161ff8a3f7d
paper/prior-art-finding.md         SHA-256 a52c7b86f8e1ab6fec7d40e546bb3fa21b19b6464ddba496d2a12009027389a5
```

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

## 6. What I am asking of you

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

**Q5 — Steps 5 and 6 next.** All four of you said so last round and nothing since has changed
it. Unless the falsified gap moves something.

---

## 7. Where the work stands

Seven steps written: 1, 2, 3, 4, 7, 8, 9. **The architecture is unchanged.** What changed this
round is the size of the claim around it, and it changed in the direction the evidence pushed.

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper.
