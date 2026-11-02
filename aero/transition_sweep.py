"""Supplement S7: the transition with the linear borrowed C_m, swept in 0.2 N m steps of control moment.
Corrected model (transition_dynamics.py, REVISION): 50 kg design, t_r = 2 s, bang-bang profile, entry climb 5 m/s,
run 40 s after the profile. loss = lowest altitude below entry; fall = largest fall from an earlier high point;
theta_end against the trim attitude of 83.34 deg.
Usage: python transition_sweep.py   (from aero/; or pass the aero dir)"""
import sys
from multiprocessing import Pool

if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import transition_dynamics as td


def one(M):
    return M, td.kos(M_kontrol=M, tr=2.0, model="dogrusal", **td.HAFIF)


if __name__ == "__main__":
    print("linear C_m = 0.056 - 0.48 alpha, light 50 kg design, t_r = 2 s, entry climb 5 m/s, stall break 12 deg")
    print("%8s %9s %8s %8s %13s %10s %10s" % ("M N m", "settled", "loss m", "fall m", "saturation s", "alpha max",
                                               "theta_end"))
    Ms = sorted(set([round(17.6 + 0.2 * i, 1) for i in range(28)] + [20.7]))
    with Pool(4) as p:
        for M, r in p.map(one, Ms):
            print("%8.1f %9s %8.2f %8.2f %13.2f %10.1f %10.1f"
                  % (M, r["oturdu"] and not r["firladi"], -r["kayip"], r["dusus"], r["doyma"], r["al_max"],
                     r["theta_son"]))
