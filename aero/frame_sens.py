"""B1/B5 sensitivity: frame term (Hoerner subcritical, frontal Cd 0.42-0.68) and rotor term
(Run B) propagated through the paper's own closure loop. Usage: python frame_sens.py   (from aero/; or pass the aero dir)"""
import sys
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import drag_sweep as DS, baseline as BL
from chain_resolve import gorev_ile
S_FRAME = 4 * 0.71 * 0.020 / 1.9785          # frontal area / S_ref
def close(F, R, end, eta):
    DS.CERCEVE, DS.ROTOR = F, R
    if end == "fav":
        cd0, pay = 0.0073 + F + 0.0015 + R, 1.0
    else:
        cd0, pay = (0.0129 + F + 0.0020 + R) * 1.1, 1.1
    ld_t, carp = DS.zincir(cd0, rotorlu=True, pay=pay)
    m = BL.mimariler(f_tampon=0.036)[0]; m.LD_carpan = carp
    r = BL.boyutlandir(m, ld_t, g=gorev_ile(eta))
    share = (F + R) * pay / cd0
    return cd0, r["LD"], r["MTOW"], r["menzil"], share
print("%-26s %-4s %5s %7s %6s %6s %7s %6s" % ("case", "end", "eta", "CD0", "L/D", "MTOW", "range", "tip%"))
for name, cdf, R in (("paper (Cd 0.15, NF rotor)", 0.15, 0.0154),
                     ("Hoerner Cd 0.42, NF rotor", 0.42, 0.0154),
                     ("Hoerner Cd 0.68, NF rotor", 0.68, 0.0154),
                     ("Cd 0.15, Sheldahl rotor", 0.15, 0.0104),
                     ("Hoerner 0.42, Sheldahl", 0.42, 0.0104),
                     ("Hoerner 0.68, Sheldahl", 0.68, 0.0104)):
    F = cdf * S_FRAME
    for end, eta in (("fav", 0.683), ("adv", 0.632)):
        cd0, ld, mt, rg, sh = close(F, R, end, eta)
        print("%-26s %-4s %5.3f %7.4f %6.2f %6.1f %7.0f %5.0f%%" % (name, end, eta, cd0, ld, mt, rg, 100 * sh))
