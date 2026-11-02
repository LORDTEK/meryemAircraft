"""Supplement S7: how robust the corrected transition result is (transition_dynamics.py, REVISION).

1. Rotation time. The 2 s rotation of S7 is the quick case. The same model with the rotation time t_r stretched to
   20 s: the aircraft leans forward, climbs on full thrust while the horizontal speed builds, and reaches 95 % of the
   30 m/s cruise speed at t_cr, at an altitude h_cr above the entry point.
2. Moment law. The linear law C_m = C_m0 + C_m_alpha alpha (on the MAC, about the CG) with seven pairs of intercept and
   slope: the paper's law (0.056, -0.48); the untwisted planform's direct vortex-lattice fit (0.0578, -0.4953); the
   -9 deg washout planform's own vortex-lattice line (0.0621, -0.5512); and four trim-consistent lines
   0.45 K - K CL_alpha alpha for neutral points from 0.831 to 0.888 m (static margins K of 8.2 to 16.9 % MAC), the
   range of the project's neutral-point estimates. With t_r = 2 s each law is swept from 17.6 to 23.0 N m in steps of
   0.2 N m (and at 20.7 N m); with t_r = 3, 4 and 6 s it is run at 17.6, 19.0, 20.7 and 23.0 N m. Every case with the
   lift model's stall break at 12 deg (as coded) and at 14 deg.
50 kg design (HAFIF), entry climb 5 m/s, bang-bang profile unless stated, run 40 s after the profile.
loss = lowest altitude below entry; fall = largest fall from an earlier high point.
Usage: python transition_robustness.py
"""
import math
import os
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transition_dynamics as td

D2R = math.pi / 180.0
H = td.HAFIF
TRS = (2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 20.0)
LAWS = (("paper law", 0.056, -0.48),
        ("untwisted VLM, direct fit", 0.0578, -0.4953),
        ("-9 deg washout VLM line", 0.0621, -0.5512),
        ("neutral point 0.869 m", 0.063, -0.538),
        ("neutral point 0.888 m", 0.076, -0.687),
        ("neutral point 0.855 m", 0.053, -0.472),
        ("neutral point 0.831 m", 0.037, -0.316))
MS, LTRS, BREAKS = (17.6, 19.0, 20.7, 23.0), (2.0, 3.0, 4.0, 6.0), (12.0, 14.0)
MGRID = tuple(sorted(set([round(17.6 + 0.2 * i, 1) for i in range(28)] + [20.7])))


def moments(tr):
    return MGRID if tr == 2.0 else MS


def one(job):
    if job[0] == "tr":
        _, model, prof, M, tr = job
        return job, td.kos(M_kontrol=M, tr=tr, model=model, profil=prof, **H)
    _, li, M, tr, a = job
    _, c0, s = LAWS[li]
    return job, td.kos(M_kontrol=M, tr=tr, model="dogrusal", cm0=c0, cma=s, astall=a * D2R, **H)


if __name__ == "__main__":
    jobs = [("tr", model, prof, M, tr) for model in ("sifir", "dogrusal") for prof in ("bang", "duz")
            for M in (23.0, 17.6) for tr in TRS]
    jobs += [("law", li, M, tr, a) for li in range(len(LAWS)) for tr in LTRS for M in moments(tr) for a in BREAKS]
    with Pool(4) as p:
        out = dict(p.map(one, jobs))
    th_trim = td.trim_attitude(**H)
    al_trim = math.pi / 2 - th_trim
    qSc = 0.5 * td.RHO * H["Vcr"] ** 2 * H["S"] * H["c_ort"]
    print("50 kg design: trim attitude %.2f deg (incidence %.2f deg at 30 m/s); q S c at 30 m/s %.1f N m"
          % (th_trim / D2R, al_trim / D2R, qSc))
    print("\n1. ROTATION TIME (stall break 12 deg)")
    for model in ("sifir", "dogrusal"):
        for prof in ("bang", "duz"):
            for M in (23.0, 17.6):
                print("  C_m %s, profile %s, M = %.1f N m" % ("= 0" if model == "sifir" else "linear (paper law)",
                                                             "bang-bang" if prof == "bang" else "cubic", M))
                print("  %6s %7s %7s %7s %7s %8s %6s %8s  %s" % ("t_r s", "loss m", "fall m", "t_cr s", "h_cr m",
                                                              "alpha", "sat s", "Mdem", "end"))
                for tr in TRS:
                    r = out[("tr", model, prof, M, tr)]
                    print("  %6.1f %7.2f %7.2f %7s %7s %8.1f %6.2f %8.1f  %s"
                          % (tr, -r["kayip"], r["dusus"], "%.1f" % r["t_cr"] if r["t_cr"] is not None else "never",
                             "%.1f" % r["h_cr"] if r["h_cr"] is not None else "-", r["al_max"], r["doyma"],
                             r["M_ist_max"], "TUMBLES" if r["firladi"] else ("settled" if r["oturdu"] else
                                                                            "NOT settled")))
    print("\n2. MOMENT LAW (largest values over the moments run: 17.6 to 23.0 N m in 0.2 N m steps at t_r 2 s,"
          " 17.6 / 19.0 / 20.7 / 23.0 N m at 3, 4 and 6 s; breaks 12 deg | 14 deg)")
    print("  %-44s %8s %5s | %34s | %34s" % ("law (C_m0, C_m_alpha)", "M_trim", "t_r", "loss / fall / sat / Mdem, 12 deg",
                                            "loss / fall / sat / Mdem, 14 deg"))
    n_t = n = n_u = 0
    worst_M = {}
    for li, (name, c0, s) in enumerate(LAWS):
        for tr in LTRS:
            cells = []
            for a in BREAKS:
                rs = [out[("law", li, M, tr, a)] for M in moments(tr)]
                n += len(rs)
                n_t += sum(r["firladi"] for r in rs)
                n_u += sum((not r["firladi"]) and (not r["oturdu"]) for r in rs)
                worst = max(rs, key=lambda r: -r["kayip"])
                cells.append("%6.2f / %6.2f / %5.2f / %5.1f%s" % (-worst["kayip"], max(r["dusus"] for r in rs),
                                                                max(r["doyma"] for r in rs),
                                                                max(r["M_ist_max"] for r in rs),
                                                                " T" if any(r["firladi"] for r in rs) else "  "))
                if tr == 2.0 and a == 12.0:
                    worst_M[li] = [M for M in moments(tr) if out[("law", li, M, tr, a)] is worst][0]
            label = "%s (%.4g, %.4g)" % (name, c0, s) if tr == LTRS[0] else ""
            trim = "%+8.1f" % (qSc * (c0 + s * al_trim)) if tr == LTRS[0] else ""
            print("  %-44s %8s %5.1f | %34s | %34s" % (label, trim, tr, cells[0], cells[1]))
    print("  M_trim = aerodynamic moment at the cruise trim attitude, N m (+ nose-up); T = a run tumbles")
    print("  largest dip below entry at t_r 2 s, break 12 deg, is at: "
          + "; ".join("%s %.1f N m" % (LAWS[li][0], M) for li, M in sorted(worst_M.items())))
    print("\n  tumbling runs: %d of %d; runs not settled at the end: %d" % (n_t, n, n_u))
