"""Supplement S10, Table S6a: the range ratio is the (L/D)e ratio times the fuel-fraction ratio, per contract;
checked against contracts.py, with the break-even ratio 0.16/(0.16 - df_e) of contract 3.
Usage: python breakeven_check.py   (from aero/; or pass the aero dir)"""
import sys
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import contracts as C
from closure import CD0, ETA_P
for k, dk, ek in C.KAPANISLAR:
    ldt, ref, out = C.kos(CD0[dk], ETA_P[ek])
    A1, B1 = out[(1, 0)], out[(1, 1)]
    r = (B1["LD"] * 0.80) / (A1["LD"] * ETA_P[ek])          # effective L/D ratio
    rows = []
    for s in (1, 2, 3):
        a, b = out[(s, 0)], out[(s, 1)]
        meas = b["menzil"] / a["menzil"]
        ff_a = 0.16 if s == 1 else (0.16 * ref["MTOW"] / a["MTOW"])
        ff_b = 0.16 if s == 1 else (0.16 * ref["MTOW"] / b["MTOW"] if s == 2 else 1 - b["f_bos"] - 13.0 / ref["MTOW"])
        rows.append((s, meas, r * ff_b / ff_a))
    df = B1 and (out[(3, 1)]["f_bos"] - out[(3, 0)]["f_bos"])
    print(k, "r=%.3f" % r, " ".join("s%d meas %.4f pred %.4f" % x for x in rows),
          " df_e(s3)=%.4f shift_pred=%.1f shift_meas=%.1f break_even_r=%.3f" % (df, 100 * r * df / 0.16, 100 * (rows[0][1] - rows[2][1]), 0.16 / (0.16 - df)))
