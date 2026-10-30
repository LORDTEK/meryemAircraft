"""B1 probe: local angle of attack and Re along the tip blade at zero shaft torque (NeuralFoil baseline)."""
import sys, numpy as np
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import tip_propeller as tp
for cl_h in (0.40, 0.55, 0.70, 0.85):
    c, th = tp.hover_tasarla(cl_hedef=cl_h)
    om, T = tp.sifir_tork(c, th)
    out = tp.bemt_sabit(tp.V_SEYIR, om, c, th)
    print(cl_h, "om", round(om), "T", round(T, 3), "dCD0", round(tp.dcd0(T), 5), "n_out", len(out))
    for k, v in enumerate(out):
        if hasattr(v, "__len__") and len(v) > 3:
            print("   item", k, np.round(np.asarray(v)[::4], 2))
