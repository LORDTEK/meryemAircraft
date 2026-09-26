#!/usr/bin/env python3
"""v8 Sekil 3 TASLAGI (Tur 101): etkin kaldirma/surukleme L/De = WV/P, tek birimde.

Sayilar YALNIZ dogrulanmis kaynaklardan:
  bu yapilandirma: Adim 10 kapanislari A-D, L/De = (L/D) * eta_p = 5.56 / 6.00 / 6.84 / 7.39 (Adim 6 tablosu)
  yayimlanmis: Johnson & Silva 2022, Tablo 3 (PDF s. 70), `paper/v8-evidence.md`
Etiketler v8_stale.py emekli listesine ve korunan cumlelere karsi taranir (CLAUDE.md 3.1, Tur 68 kurali).
Bu bir taslaktir; okuyucu oyu ve yazar karari olmadan govdeye girmez.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(KOK, "figures", "output", "v8-draft-f3-effective-LD.png")

BU = [("A", 5.56), ("B", 6.00), ("C", 6.84), ("D", 7.39)]
YAYIN = [  # (etiket, aile, L/De)
    ("Quadrotor, turboshaft", "Multirotor", 4.9),
    ("Quadrotor, electric", "Multirotor", 5.8),
    ("Single main rotor, turboshaft", "Helicopter", 5.4),
    ("Single main rotor, electric", "Helicopter", 6.0),
    ("Side-by-side, turboshaft", "Helicopter", 5.9),
    ("Side-by-side, electric", "Helicopter", 7.2),
    ("Lift+cruise, turbo-electric", "Hybrid", 8.5),
    ("Lift+cruise, electric", "Hybrid", 7.9),
    ("Tilt-wing, turbo-electric", "Hybrid", 8.6),
]
RENK = {"Multirotor": "#8A5A2B", "Helicopter": "#5B6770", "Hybrid": "#3E6B4E"}

fig, ax = plt.subplots(figsize=(7.0, 3.6))
ax.axvspan(BU[0][1], BU[-1][1], color="#2F6F8F", alpha=0.13, lw=0)
for ad, v in BU:
    ax.axvline(v, color="#2F6F8F", lw=1.0, ls=":")
    ax.text(v, len(YAYIN) - 0.35, ad, ha="center", va="bottom", fontsize=8.5, color="#2F6F8F")
# Aciklama sekil altyazisinda (AIAA: 20-25 kelime).
for i, (ad, aile, v) in enumerate(YAYIN):
    y = len(YAYIN) - 1 - i
    ax.plot([v], [y], "o", ms=6, color=RENK[aile])
ax.set_xlim(4.5, 9.0)
ax.set_ylim(-0.7, len(YAYIN) + 0.2)
ax.set_yticks([len(YAYIN) - 1 - i for i in range(len(YAYIN))])
ax.set_yticklabels([ad for ad, _, _ in YAYIN], fontsize=8.5)
for t, (_, aile, _) in zip(ax.get_yticklabels(), YAYIN):
    t.set_color(RENK[aile])
ax.tick_params(axis="y", length=0)
ax.set_xlabel("Effective lift-to-drag ratio  L/De = WV/P")
for s in ("left", "right", "top"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, dpi=300)
print("yazildi:", os.path.relpath(OUT, KOK))
