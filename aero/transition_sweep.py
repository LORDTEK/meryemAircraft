"""Supplement S7: control-moment threshold of the transition with the linear borrowed C_m, swept in 0.2 N m steps.
theta_end is the body angle when the run ends at 4 t_r (90 deg = cruise attitude).
Usage: python transition_sweep.py   (from aero/; or pass the aero dir)"""
import sys
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import transition_dynamics as td

print("linear C_m = 0.056 - 0.48 alpha, light 50 kg design, t_r = 2 s, entry climb 5 m/s")
print("%8s %10s %10s %12s %10s" % ("M N m", "completes", "loss m", "saturation s", "theta_end"))
Ms = [round(17.6 + 0.2 * i, 1) for i in range(16)] + [20.7]
for M in sorted(set(Ms)):
    r = td.kos(M_kontrol=M, tr=2.0, model="dogrusal", **td.HAFIF)
    print("%8.1f %10s %10.2f %12.2f %10.1f" % (M, r["ulasti"] and not r["firladi"], r["kayip"], r["doyma"], r["theta_son"]))
