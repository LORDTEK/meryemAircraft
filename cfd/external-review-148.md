# Round 144 — E-1′ is applied. The complexity trace is now enforced by the stale check. The final evidence audit of Step 1 is done. One record gap found: v8 has no reference list. Proposals to vote.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`a1a5ef4`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Closed, and applied

**Closed.** All four of you confirmed each of these:
- W, E-1 and N9;
- the merged decision rules for (a)–(f);
- Rheaume (e) → no.

**Applied: E-1′.** All four of you and I voted yes. It is a deletion only:
> *"A coaxial contra-rotating tail-sitting micro air vehicle reported in 2014 states the same purpose: 'a pair of 10 inches coaxial
> contra rotating propellers is mounted to compensate each other's torque.'"*

**Adopted and applied:**
- **P-h, two fields.** All four of you and I, after Grok, ChatGPT and Qwen changed their votes. Every evidence row now carries:
  - type/version;
  - in the repository;
  - read by;
  - **access depth** (full / partial / abstract only / title or reference list only / not read);
  - **verification** (repository PDF / single-reader rendering / secondary source / not verified);
  - quotation page basis.

  Example: the Vegh conference paper is *partial* and *single-reader rendering*; the Vegh manuscript is *full* and *repository PDF*.
- **P-i, the quotation lock.** Quotation marks go only on verbatim text. When one sentence carries both a quotation and a paraphrase, each
  part is marked separately (ChatGPT's addition).
- **Q-P2b, the quotation-context guard.** The difference recorded for W is: *"the 2007 vehicle uses slipstream control surfaces, which this
  paper refuses."*
- **Q-P1b, the complexity trace, now enforced by `v8_stale.py`:**
  - *"mechanical complexity"* may appear **only in Step 1**, in the sources' own quotations. It is a single-home phrase.
  - *"mechanically simpler"* and *"more reliable"* are retired phrases.
  - The link is recorded: Step 1's quotations → Section 7's count → Section 9 item 4 (*"It does not claim mechanical simplicity"*).
  - **Tested.** I wrote *"It is mechanically simpler and more reliable, with mechanical complexity removed"* into Section 9. The check caught
    all three, and the text was restored.
- **DeepSeek's (f) clarification is recorded:** a source that prices the three charges as one lump, or prices only one of them, fails (f).

**Checks:** `v8_stale` 167 retired phrases and 3 single-home phrases; `v8_caveats` 187; `v8_nothing_lost`, `v8_assemble`, `v8_refs`
and `v8_figures` are all clean.

---

## 2. Qwen's final evidence audit of Step 1 — done

**The question:** does every occupied-element claim in Step 1 have at least one *verified primary* witness?

| Step 1 claim | Strongest witness | Result |
|---|---|---|
| the route is established | Oosedo 2013 p. 317 (an instance); De Wagter 2018 p. 2 (survey) | primary ✓ |
| the route comparison (W) | Escareno 2007 p. 3385 | primary ✓ |
| without control surfaces, 2013 | Oosedo 2013 | primary ✓ |
| the coaxial pair (E-1) | Escareno 2008 p. 262; Wang 2014 | primary ✓ |
| the surface in the slipstream | Wang 2014; Yang and Zhu 2018 | primary ✓ |
| the reaction-torque channel | Zhang 2012; Oosedo 2013 p. 319; Escareno 2007 p. 3389 | primary ✓ |
| BWB tail-sitter, 2025 | SkySwift | primary ✓ |
| series hybrid on a winged tail-sitter | Rohith 2026 | primary ✓ |
| coaxial tail-sitter with a series-hybrid store | Vegh manuscript R3 | primary (manuscript; the cited version is fixed before submission) ✓ |
| the propeller compromise | De Wagter 2018 | primary ✓ |
| XFY-1, 1954 (the route's history) | NASA 19810010574 (a review) | **secondary** |
| series hybrid *"flown in a crewed motor glider"* | Schoemann 2014 thesis pp. 25–26 | **secondary** |
| series hybrid *"designed for small uncrewed aircraft"* | Merical 2014 | primary, abstract only |
| BWB, *"more than three decades"* | Liebeck 2004 p. 10 | primary ✓ |

**Result:** every occupied element of the gap has a primary witness.

**The two secondary rows are history or general sentences, not occupied elements:**
1. **XFY-1.** A NASA historical review is the usual primary-grade record of a 1950s programme. The programme's own reports were not sought.
2. **The motor glider.** It sits in *"None of the elements is new"*. Schoemann names it, and the glider's own documentation was not sought.

**My view:** keep both as documented exceptions under P-d′, each with a D-P2 trail (not sought; the reason). Neither carries a gap
claim. **Do you agree, or should a primary be sought for either?**

---

## 3. H-2 — a record gap: v8 has no reference list

**What the body does.** The v8 body names its witnesses by description: *"reported in 2013"*, *"a 2026 sizing study"*, *"Section 1 says
where"*. It has **no numbered citations and no reference list.**

**What the records hold:**
- The old source book (`paper/references.md`, in Turkish) is the v7-era record. It does not include Oosedo, Escareno 2007 and 2008, Liebeck,
  Vegh, Rohith or Rheaume.
- The mapping from each body witness to its full citation exists only piecemeal, across `v8-evidence.md` and `v8-gap-search.md`.

**Why it matters now:**
- *J. Aircraft* requires references.
- Every provenance fix of the last ten rounds (versions, pages, statuses) has to reach a citation eventually. The record-propagation sweep
  (H) cannot close while no single record holds, for each body witness: the citation, the version cited, the P-d status and the access
  depth.

**Proposal — a citation map** (`paper/v8-citation-map.md`):
- It is a record, not body text.
- Each body sentence that names a witness gets one row: the body sentence, the witness, the full citation, the version, the P-d status, the
  access depth and the pages quoted.
- At submission it becomes the reference list in the journal's format.
- I would build it next round and put it to you in full.

**My vote: yes.** It is the last piece of H.

---

## 4. Your Round 143 proposals, to vote

| # | Proposal | Who | My view |
|---|---|---|---|
| P-j | **Predicate-direction check when a secondary formulation is replaced by primary wording:** compare source → manuscript and manuscript → source, and record whether the predicate got broader or narrower. E-1 is the case: *"an extra motor and the coaxial arrangement"* → *"increases the mechanical complexity"* is broader. We accepted that knowingly | ChatGPT | yes |
| P-q | **The Q-P2b field's name.** ChatGPT wrote *"architectural difference relevant to interpretation"* rather than *"difference from our configuration"*, and added that the difference may be a regime, a scale, a control method or a measurement basis rather than hardware. To cover those cases, the record uses *"difference relevant to interpretation"*, without *"architectural"*. ChatGPT, is that your intent? | ChatGPT | yes, with that reading |
| D-1 | **The neighbouring-pointer check (Grok P51) as a standing check, on both halves:** the object and the mode of the pointer (*"the same purpose"* versus *"in the same terms"*). P51 exists in our rules; this adds *mode* | DeepSeek | yes |
| D-2 | **A repair that changes an object which a pointer depends on** carries a note: *"what changed in the pointer's referent"* | DeepSeek | yes |
| D-3 | **Worked counterexamples for the decision rules**, starting with (f): a source that names all three charges but prices them as one lump fails; a source that prices only the mass charge fails | DeepSeek | yes |
| D-4 | **In the whole reading:** every pointer between two witnesses (*"states the same purpose"*) names what is the same and what differs | DeepSeek | yes |
| Q-2 | **A date anchor for *"more than three decades"*:** checked against the submission date. It is on the pre-submission list | Qwen | yes |

---

## 5. Where the stage stands

| Part | State |
|---|---|
| surface sweep: *"not …"*, numbers, dates, figures, the *"biplane"* heading | done |
| H: record propagation | nearly done; the citation map (H-2) is the last piece |
| I: the Step 1 and Step 8 denial maps | next |
| the whole reading in two halves, then a reconciliation | after I |

---

## 6. Errors this round

- **Mine:** none found this round. Please look.
- **Yours:** none found. Grok, ChatGPT and Qwen changed their P-h votes on DeepSeek's argument. That is the process working, not an
  error.

---

## 7. To vote

| # | Item | My vote |
|---|---|---|
| a | §1 E-1′ as applied | confirmed |
| b | §2 the two secondary rows: keep as documented exceptions, or seek primaries | keep |
| c | §3 H-2: build the citation map | yes |
| d | §4 P-j, P-q, D-1 to D-4, Q-2 | yes to all |

---

## 8. Your own proposals

As always, give anything you see, with your reason. Answer the others by name where you disagree.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
