# -*- coding: utf-8 -*-
"""Adim 4 yeniden kurma denemesi (Tur 75): etiketli taslak -> taslak metni, iz tablosu, denetim.
Her cumle: (etiket, metin, kaynak cumle numaralari, [R icin yuklem defteri]).
Kaynak numaralari: 04-snapshot.md govdesinin cumle sirasi (1..51)."""
import re, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "build"))
from v8_caveats import duz, liste

B = []
def blok(ad): B.append((ad, []))
def c(tag, text, src, ledger=None): B[-1][1].append((tag, text, src, ledger))

blok("B1 — why the check, and its reach")
c("D", "An accounting proposed by the same people who then use it invites one obvious objection: that the charges were chosen because a particular aircraft happens not to pay them.", [1])
c("R", "The objection arises at the title, not at the ledger, so it is answered here — before any configuration is described — by testing a prediction the accounting makes against numbers this work did not produce.", [2],
  "Source: '…described — and it is answered in the only way that settles anything, by testing…'. The exclusivity claim ('the only way that settles anything') is dropped. Narrower.")
c("P", "**What follows is not a test of the whole framework.** It checks one falsifiable consequence on one independent data set.", [3])

blok("B2 — the prediction, stated before the data")
c("P", "**The prediction has two halves, and only the first is a derivation.**", [5])
c("D", "> **First half, derived from Section 2.** A configuration carrying a dedicated lift system pays for it in gross weight, and the payment is amplified: additional empty mass enters through a multiplier that grows as the empty-mass fraction rises, and the same increment is charged again in hover.", [6])
c("P", "> **Second half, not derived.** That the cruise efficiency the arrangement buys does not cover that payment. Section 2 predicts the charge and the amplification; **it does not prove that the credit must lose.** A dedicated lift system raises the empty-mass fraction and may lower the energy fraction at the same time, and which wins is a closure result rather than a consequence of the accounting.", [7, 8])
c("D", "The check tests the second half on independent data, with the first half supplying the reason to expect the outcome: the weight charge is amplified by a multiplier, while the efficiency credit enters linearly through the cruise lift-to-drag ratio.", [9])
c("D", "**If some data set showed the credit covering the charge, Bill 1 would not be refuted** — the mass would still have been paid. What would be refuted is the expectation that the amplified charge outweighs the linear credit.", [11, 12])
c("P", "**The prediction is also mission-dependent**, and the page would be weaker for hiding it. The mass charge of carried lift hardware is roughly fixed; the efficiency credit accumulates with distance. A long enough mission is where the credit is most likely to cover the charge, and the mission used below is short. **The counter-set is therefore a common-mission sizing study at longer range in which a dedicated-lift configuration is both more efficient and no heavier than one without.** None is known to the authors.", [13, 14, 15, 16])

blok("B3 — the data")
c("R", "The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes **five VTOL architecture families** — nine designs in all — against a single mission with common tools and common assumptions; it does not use the three-bill accounting of Section 2 or any framework derived from it.", [17, 18],
  "Source 17 + 18 joined. Every predicate kept: own purposes; no relationship; five families; nine designs; single mission; common tools and assumptions; does not use the accounting or any framework derived from it. Dropped only 'most in two propulsion variants' (a detail, no predicate). Not broader.")
c("D", "It is used for three reasons, stated so that the choice is not merely the one that agreed: it holds the mission fixed across architecture families, it applies one set of tools to all of them, and it reports both quantities this prediction needs.", [19])
c("D", "The mission is 1 200 lb of payload over 75 nautical miles. Three of the nine designs matter here.", [20, 21])
c("D", "The turboshaft quadrotor reaches an effective lift-to-drag ratio of 4.9 at a design gross weight of 3 678 lb, with no dedicated lift group: its rotors serve both regimes.", [22])
c("D", "**The turbo-electric lift-plus-cruise design reaches 8.5 at 7 271 lb and carries a dedicated lift group — eight lift motors beside its cruise motor. The turbo-electric tilt-wing reaches 8.6 at 6 584 lb with none: eight proprotors, reoriented.**", [23, 24])

blok("B4 — the result")
c("R", "**The primary comparison is the lift-plus-cruise design against the tilt-wing**, because they isolate the charge: they share the mission, the payload, the turbo-electric propulsion architecture and the presence of a cruising wing.", [25, 26],
  "Source 25 ('the last two designs', 'because they isolate the charge') + 26 joined; 'the last two designs' named. Same predicates. Not broader.")
c("P", "**They are not identical in every other respect** — one stops its lift rotors in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting wing — **but the difference the comparison turns on is that one carries a dedicated lift group through cruise and the other does not.** The comparison is the closest the published set comes to isolating that charge; it is not a controlled experiment.", [27])
c("D", "**The tilt-wing is 1.2 % better in effective cruise efficiency and 9.4 % lighter.** The dedicated lift group buys no cruise-efficiency advantage at all here — it is marginally behind — and the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net difference between two architectures, not the measured mass of a lift group**, and the published weight breakdown is what makes it informative rather than merely large.", [28, 29])
c("R", "**The published weight breakdown shows the transfer property of Section 2 — the mechanism giving part of the structural saving back — inside a breakdown this work did not produce**: its three reported categories account for 580 lb of the 679 lb empty-weight difference, and the remaining 99 lb lies in categories it does not break out (Supplement S4).", [30, "S4"],
  "Source 30: '…although the categories it reports do not account for the whole difference (Supplement S4)'. S4: 'Those three categories account for 580 lb of the 679; the remaining 99 lb lies in empty-weight categories the published table does not break out'. The body gains the three numbers (Grok: local evidence). Objects: 679 lb = empty-weight difference, lift-plus-cruise minus tilt-wing; 580 lb = structure, propulsion and battery together; 99 lb = unallocated. 687 lb (design gross weight) is a different object and is not merged. Not broader.")
c("D", "**And the source states the second half of the prediction in its own words.** Discussing why the all-electric lift-plus-cruise design is the heaviest in the set, the study writes that the high cruise efficiency of the lift-plus-cruise type reduces battery weight compared with the quadrotor, *\"but not enough to counter the increase in structure and propulsion weight.\"* That is the efficiency credit conceded and found insufficient, by the authors of the data rather than by the authors of the prediction.", [31])
c("P", "**The quadrotor is reported for scale, and the isolation test above is what carries the prediction**: against it the lift-plus-cruise design changes three things at once, and the contrast is in Supplement S4.", [32])
c("P", "**The framework does not predict any of these numbers**; without the input fractions it predicts no magnitudes. What it predicts is that the amplified weight charge survives the efficiency credit, and on the isolated pair it does so with the credit reduced to nothing.", [33, 34])

blok("B5 — the tilt-wing entry")
c("D", "**The architecture proposed later in this paper is not the only way to avoid the first charge.** The tilting family avoids it too — it carries no dedicated lift group, it is the lighter of the two matched designs, and an independent set says so. The margin in cruise efficiency is one tenth and nothing is claimed from its direction.", [36, 37])
c("D", "**The tilt-wing is the transfer property of Section 2 appearing in someone else's data.** It does not escape the accounting by avoiding the mass charge; it *moves* the charge — to the mechanism that reorients its propulsors, with the actuation, the gyroscopic coupling and the transition control problem that Section 2 assigns to that family.", [38])
c("D", "What separates the tilting family from the configuration described later is not this axis; it is what each pays, and a sizing study does not settle that.", [40])

blok("B6 — what the check establishes")
c("D", "It establishes that one prediction of the accounting holds on data produced elsewhere, for purposes unrelated to this argument. That is the whole of it.", [41, 42])
c("P", "**It does not establish that the accounting is complete**, that the three charges are the only costs an architecture pays, or that avoiding them makes an aircraft better. The accounting says an architecture that avoids the three is cheaper in those three currencies and nothing more.", [43, 44])
c("D", "**It does not establish anything about the configuration this paper proposes**, which has not yet been described, and which is not in the study used here. A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where the answer is not uniformly favourable.", [46, 47])
c("R", "**An instrument whose first use is to measure the thing its authors are advocating should be shown working on something else first**, and that is why this section comes before the aircraft.", [48, 49],
  "Source 48–49: 'What the check is for is narrower and comes earlier: an instrument … first. That is what this section does, and it is the reason it appears here rather than after the aircraft.' Same predicate. Not broader.")
c("D", "**The instrument is now fixed, and it is not modified again.** **Everything that follows is measured with it rather than added to it.** The next two sections describe the two capabilities the mission asks for, one at a time and each against the family that structurally lacks it, before Section 7 asks whether one aircraft can hold both.", [50, 51])

if __name__ == "__main__":
    kok = os.path.join(os.path.dirname(__file__), "..", "..", "..")
    src = [l.split("\t") for l in open(os.path.join(os.path.dirname(__file__), "04-source-sentences.tsv"), encoding="utf-8").read().splitlines()]
    govde = ["## An independent quantitative check", ""]
    for ad, cs in B:
        par = []
        for tag, t, s, led in cs:
            if t.startswith(">"):
                if par: govde.append(" ".join(par)); govde.append(""); par = []
                govde.append(t); govde.append("")
            else:
                par.append(t)
        if par: govde.append(" ".join(par)); govde.append("")
    metin = "\n".join(govde).rstrip() + "\n"
    open(os.path.join(os.path.dirname(__file__), "04-draft.md"), "w", encoding="utf-8").write(metin)
    d = duz(metin)
    eksik = [q for a, q, _ in liste() if a == 4 for p in [duz(x).strip(" .,") for x in q.split("…") if duz(x).strip(" .,")] if p not in d]
    kullanilan = {x for _, cs in B for _, _, s, _ in cs for x in s if isinstance(x, int)}
    print("taslak kelime:", len(metin.split()), "| eksik korunan:", eksik or "yok")
    print("kaynakta olup taslakta karsiligi olmayan (S4'e):", [int(i) for i, _, _ in src if int(i) not in kullanilan])
    say = {}
    for _, cs in B:
        for tag, t, s, led in cs:
            say[tag] = say.get(tag, 0) + len(t.split())
    print("etiket kelime:", say)
