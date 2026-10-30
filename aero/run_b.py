"""B1 Run B: same zero-shaft-torque blade-element solver and frozen tip-blade geometry
(design c_l = 0.68, the design behind the paper's 0.0154), section polar swapped from
NeuralFoil to Sheldahl & Klimas SAND80-2114 Table 2, NACA 0012, Re = 8e4 block
(Eppler synthesis, not measurement; report p. 16, read from the scan).
Symmetric section: cl(-a) = -cl(a), cd(-a) = cd(a). Beyond 16 deg: held at the 16 deg row.
Usage: python run_b.py   (from aero/; or pass a directory containing tip_propeller.py)
"""
import sys, numpy as np
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import tip_propeller as tp

A  = np.arange(0, 17, dtype=float)
CL = np.array([0, .11, .22, .33, .44, .55, .6384, .7227, .6930, -.0010, .0413,
               .0911, .1430, .1966, .2504, .3043, .3582])
CD = np.array([.0133, .0134, .0138, .0145, .0155, .0170, .0189, .0204, .0222,
               .0600, .0600, .1170, .1340, .1520, .1710, .1900, .2100])

def sheldahl(alfa_deg, Re):
    a = np.abs(np.asarray(alfa_deg, dtype=float))
    s = np.sign(alfa_deg)
    return s * np.interp(a, A, CL), np.interp(a, A, CD)

nf_force = tp.kesit_kuvvet
c, th = tp.hover_tasarla(cl_hedef=0.68)          # geometry frozen with the baseline polar
om_a, T_a = tp.sifir_tork(c, th)
alfa_a = tp.bemt_sabit(tp.V_SEYIR, om_a, c, th)[2]
tp.kesit_kuvvet = sheldahl                         # Run B: only the section source changes
om_b, T_b = tp.sifir_tork(c, th)
alfa_b = tp.bemt_sabit(tp.V_SEYIR, om_b, c, th)[2] if om_b else None
print("Run A (NeuralFoil):     omega %.0f rad/s  axial %.3f N  dCD0(8 discs) %.5f" % (om_a, T_a, tp.dcd0(T_a)))
print("  alpha range %.1f .. %.1f deg" % (alfa_a.min(), alfa_a.max()))
if om_b:
    print("Run B (Sheldahl 8e4):   omega %.0f rad/s  axial %.3f N  dCD0(8 discs) %.5f" % (om_b, T_b, tp.dcd0(T_b)))
    print("  alpha range %.1f .. %.1f deg; stations beyond 16 deg: %d" % (alfa_b.min(), alfa_b.max(), int((np.abs(alfa_b) > 16).sum())))
else:
    print("Run B: no zero-torque root found")
