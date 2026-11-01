"""Airframe mass from the bottom up (revision item 4b): is the paper's airframe fraction of 0.30 optimistic?

The paper holds the airframe at 0.30 of takeoff mass, a construction constant. The closure is strongly
leveraged by it (0.35 gives +25 to 28 percent takeoff mass), so this script estimates the airframe from
its parts for the paper's planform (planform.py) and the four closed masses:

  1. Wing-box bending material at an ultimate load factor (limit 3.8 or 5, factor 1.5): spar caps sized
     by the root-to-tip bending moment of an elliptic lift distribution over the local box height. This
     is printed to show that, on a thick blended body of this size, bending does not size the structure.
  2. Minimum-gauge sandwich skin over the wetted area, as a range of layups (faces of one carbon or glass
     ply, a foam core, adhesive), plus spars, ribs and bulkheads as a fraction of the skin.
  3. Concentrated items: nose-pair mount, engine and generator mounts and tank support, tip frames with
     fairings, tail-sitting landing feet.
  4. An assembly factor for joints, fasteners, adhesive, paint and hatches. The upper end is Sagitta's:
     30 kg assembled airframe target against 19.46 kg of finite-element-sized structure (Gramueller et
     al., DLRK 2015, pp. 6 and 13), a factor of 1.54.

Every input is a stated assumption or a cited value; the output is a low-to-high band, not a point.
Usage: python airframe_estimate.py   (from aero/; or pass the aero dir)
"""
import math
import sys

if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import planform as PF                                       # noqa: E402

G = 9.81
CLOSED = {"A": 57.5, "B": 55.8, "C": 53.5, "D": 52.3}     # the paper's closures, kg

# Material and layup assumptions (low, high)
SIGMA_CAP = 500e6            # Pa, design allowable of a unidirectional CFRP spar cap (compression)
RHO_CFRP = 1550.0            # kg/m3
FACE = (0.155, 0.333)        # kg/m2 per face: one 93 g/m2 carbon ply / one 200 g/m2 carbon ply, fibre 60 % by mass
CORE = (0.10, 0.15)          # kg/m2: Rohacell 51 foam, 2 mm / 3 mm
GLUE = (0.05, 0.12)          # kg/m2 of film adhesive and filler
STRUCT_OVER_SKIN = (0.30, 0.50)   # spars, ribs and bulkheads as a fraction of the skin mass
NOSE_MOUNT = (0.5, 1.0)      # kg: mount and bulkhead for the 1.2 m coaxial pair (about 560 N at takeoff)
INTERNAL_MOUNTS = (0.3, 0.6) # kg: engine and generator mounts, fuel-tank support
FRAMES = (0.4, 0.7)          # kg: two tip frames, 2.84 m of 20 mm carbon tube and fairing
LANDING_FEET = (0.5, 1.5)    # kg: tail-sitting landing feet with load spreading
ASSEMBLY = (1.20, 1.54)      # joints, fasteners, adhesive, paint, hatches; 1.54 is Sagitta's (see above)


def geometry():
    st, half, _ = PF.istasyonlar(n=120)
    area = 2 * sum(0.5 * (a[2] + b[2]) * (b[0] - a[0]) for a, b in zip(st[:-1], st[1:]))
    # wetted area of a thick wing, S_wet = S (1.977 + 0.52 t/c), applied strip by strip (Raymer, Eq. 7.12)
    wet = 2 * sum(0.5 * (a[2] + b[2]) * (b[0] - a[0]) * (1.977 + 0.52 * 0.5 * (a[3] + b[3]))
                  for a, b in zip(st[:-1], st[1:]))
    return st, half, area, wet


def cap_mass(mtow, n_ult, st, half):
    """Spar-cap mass for bending: two caps, box height 0.8 of the local thickness, elliptic lift."""
    L_half = n_ult * mtow * G / 2.0
    q0 = 4.0 * L_half / (math.pi * half)                    # elliptic peak load per span, N/m
    ys = [s[0] for s in st]
    m = 0.0
    for i in range(len(st) - 1):
        y = 0.5 * (ys[i] + ys[i + 1])
        dy = ys[i + 1] - ys[i]
        # bending moment at y from the elliptic load outboard of y (numerical integral)
        M, k, n = 0.0, 0, 200
        for k in range(n):
            eta = y + (half - y) * (k + 0.5) / n
            q = q0 * math.sqrt(max(0.0, 1 - (eta / half) ** 2))
            M += q * (eta - y) * (half - y) / n
        chord = 0.5 * (st[i][2] + st[i + 1][2])
        tc = 0.5 * (st[i][3] + st[i + 1][3])
        h = 0.8 * tc * chord
        area_cap = M / (SIGMA_CAP * h)
        m += 2 * area_cap * RHO_CFRP * dy
    return 2 * m                                            # both halves


def main():
    st, half, area, wet = geometry()
    print("conditions: planform.py (span %.3f m, area %.4f m2, root t/c %.2f, tip t/c %.2f); wetted area %.2f m2"
          % (2 * half, area, st[0][3], st[-1][3], wet))
    print("  closed masses (the paper): " + ", ".join("%s %.1f kg" % kv for kv in CLOSED.items()))
    print("\n1. bending material (spar caps, %.0f MPa allowable):" % (SIGMA_CAP / 1e6))
    for n_lim in (3.8, 5.0):
        print("   limit %.1f g, ultimate %.2f g: %.3f kg at 57.5 kg" % (n_lim, 1.5 * n_lim, cap_mass(57.5, 1.5 * n_lim, st, half)))
    skin = [wet * (2 * FACE[i] + CORE[i] + GLUE[i]) for i in (0, 1)]
    inner = [skin[i] * STRUCT_OVER_SKIN[i] for i in (0, 1)]
    point = [NOSE_MOUNT[i] + INTERNAL_MOUNTS[i] + FRAMES[i] + LANDING_FEET[i] for i in (0, 1)]
    print("\n2. skin %.2f-%.2f kg (%.2f-%.2f kg/m2 sandwich); spars, ribs, bulkheads %.2f-%.2f kg"
          % (skin[0], skin[1], skin[0] / wet, skin[1] / wet, inner[0], inner[1]))
    print("3. nose mount, internal mounts, tip frames, landing feet: %.2f-%.2f kg" % tuple(point))
    for i, tag in ((0, "low"), (1, "high")):
        caps = cap_mass(57.5, 1.5 * (3.8 if i == 0 else 5.0), st, half)
        prim = skin[i] + inner[i] + point[i] + caps
        tot = prim * ASSEMBLY[i]
        fr = ", ".join("%s %.3f" % (k, tot / m) for k, m in CLOSED.items())
        print("4. %-4s: primary %.2f kg x assembly %.2f = %.2f kg -> fraction %s" % (tag, prim, ASSEMBLY[i], tot, fr))
    print("\nthe paper holds 0.300; reported in-class values 0.28-0.44 (revision note R-5); one production tail-sitter, 0.30")


if __name__ == "__main__":
    main()
