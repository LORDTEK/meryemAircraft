"""Frame term from measured drag of thick sections (revision item 2).

The paper charges the two tip frames (20 mm thick, 2.84 m in all) at a frontal drag coefficient of 0.15,
an assumption; Hoerner's subcritical formula gives 0.42-0.68 for the paper's fairing chord of 31-52 mm
(Supplement S4). This script takes measured zero-incidence drag of thick sections near the frames'
chord Reynolds numbers and closes the paper's loop (as frame_sens.py) for three fairings: the paper's
chord (t/c 0.38-0.65), a streamline strut of t/c 0.29-0.33, and one of t/c 0.25. A longer fairing is
heavier; its extra mass is carried in the loop.

Usage: python frame_fairing.py   (from aero/; or pass the aero dir)
"""
import sys
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import drag_sweep as DS, baseline as BL                    # noqa: E401
from chain_resolve import gorev_ile

T_FRAME, L_FRAME, S_REF = 0.020, 4 * 0.71, 1.9785         # m, m, m2 (as frame_sens.py)
S_FRAME = L_FRAME * T_FRAME / S_REF                       # frontal area / S_ref
NU = 1.46e-5                                              # m2/s, sea level ISA
# Fairing skin for the extra mass of a longer chord: 0.30 kg/m2 (thin glass-epoxy, assumed), perimeter
# about twice the chord, counted from the paper's shortest chord (31 mm) so that the extra mass is not
# understated; the paper's own fairing carries none.
SKIN, C_PAPER = 0.30, 0.031

# (name, chord range m, frontal C_D range, source). Tags: S stated, R read from a plot, D derived.
CASES = [
    ("paper assumption", (0.031, 0.052), (0.15, 0.15), "assumed in the paper"),
    ("paper fairing, t/c 0.38-0.65", (0.031, 0.052), (0.36, 0.60),
     "ellipses: t/c 0.40 at Re 7.8e4, 0.357 (Zahm, Smith & Louden 1929, NACA Rep. 289, Tab. VIII; "
     "NTRS OCR text); 2:1 ellipse at Re 1e5, 0.6 (Delany & Sorensen 1953, NACA TN 3038, Tab. I) [S]"),
    ("streamline strut, t/c 0.29-0.33", (0.060, 0.070), (0.13, 0.15),
     "Warner 1923, NACA TN 167: strut 76-1, t/c 0.286, 0.13 at 30 mph, free ends (p. 2) [S]; "
     "strut 76-2, t/c 0.333, 0.153 at Re 6e4 (Fig. 4) [R]"),
    ("streamline strut, t/c 0.25", (0.080, 0.080), (0.069, 0.087),
     "Zahm, Smith & Hill 1923, NACA Rep. 137, Tab. V: Navy No. 3 (3 x 12 in), 1/32-in gap, 20 mph, "
     "C = 0.0347, C_D = 2C = 0.069, Re_c 1.8e5 [S->D]; upper end +25 %, the gap between Rep. 137 and "
     "Smith 1929, NACA Rep. 311, Tab. VII on the Navy No. 2 strut (0.094 against 0.073) [D]"),
]


def close(F, R, end, eta, dm=0.0):
    """frame_sens.close with an extra fixed mass dm (kg) carried as a fraction of the closed mass."""
    DS.CERCEVE, DS.ROTOR = F, R
    if end == "fav":
        cd0, pay = 0.0073 + F + 0.0015 + R, 1.0
    else:
        cd0, pay = (0.0129 + F + 0.0020 + R) * 1.1, 1.1
    ld_t, carp = DS.zincir(cd0, rotorlu=True, pay=pay)
    mtow = 55.0
    for _ in range(3):                                   # dm / MTOW converges in a few passes
        m = BL.mimariler(f_tampon=0.036)[0]
        m.LD_carpan, m.f_ek = carp, m.f_ek + dm / mtow
        r = BL.boyutlandir(m, ld_t, g=gorev_ile(eta))
        mtow = r["MTOW"]
    return cd0, r["LD"], r["MTOW"], r["menzil"], (F + R) * pay / cd0


def self_test():
    """The paper's row must reproduce frame_sens.py (52.3 kg / 1233 km and 57.5 kg / 927 km), and a larger
    frame drag must raise the closed mass."""
    a = close(0.15 * S_FRAME, 0.0154, "fav", 0.683)
    b = close(0.15 * S_FRAME, 0.0154, "adv", 0.632)
    assert round(a[2], 1) == 52.3 and round(a[3]) == 1233 and round(b[2], 1) == 57.5 and round(b[3]) == 927, (a, b)
    assert close(0.30 * S_FRAME, 0.0154, "fav", 0.683)[2] > a[2] + 0.5, "frame drag ignored"
    print("self-test: the paper's closures reproduced; the frame term moves the closure")


if __name__ == "__main__":
    self_test()
    V = gorev_ile(0.683)["V"]
    print("conditions: V %.1f m/s, nu %.2e m2/s, frames %.3f m thick, %.2f m in all, S_ref %.4f m2 (frontal/S_ref %.5f);"
          % (V, NU, T_FRAME, L_FRAME, S_REF, S_FRAME))
    print("  rotor term 0.0154 (NeuralFoil, the paper's closures); ends fav (eta_p 0.683) and adv (0.632) as frame_sens.py;")
    print("  extra fairing mass %.2f kg/m2 x twice the chord increment over %.0f mm x %.2f m" % (SKIN, 1000 * C_PAPER, L_FRAME))
    print("\n%-34s %-11s %-9s %-11s %-4s %7s %6s %6s %6s %5s" % ("fairing", "chord mm", "Re_c", "C_D front", "end", "CD0", "L/D", "MTOW", "range", "tip%"))
    for name, (c1, c2), (k1, k2), src in CASES:
        dm = 0.0 if name.startswith("paper") else SKIN * 2 * (c2 - C_PAPER) * L_FRAME
        for k in sorted({k1, k2}):
            for end, eta in (("fav", 0.683), ("adv", 0.632)):
                cd0, ld, mt, rg, sh = close(k * S_FRAME, 0.0154, end, eta, dm)
                print("%-34s %4.0f-%-6.0f %3.1e-%-3.1e %-11.3f %-4s %7.4f %6.2f %6.1f %6.0f %4.0f%%"
                      % (name, 1000 * c1, 1000 * c2, V * c1 / NU, V * c2 / NU, k, end, cd0, ld, mt, rg, 100 * sh))
        print("    source: " + src + ("; extra mass %.2f kg" % dm if dm else ""))
