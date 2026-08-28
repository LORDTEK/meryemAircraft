# -*- coding: utf-8 -*-
"""Sekil basliklari — makaleye giren tek yer. Sekil dosyalari ile eslesir."""

FIGS = [
 ("1",  "sekil01-iki-aile.png",
  "Two configuration families and the limit of each. Fixed-wing aircraft occupy the "
  "efficient-cruise corner and are bounded by ground infrastructure; rotary-wing "
  "aircraft occupy the runway-independent corner and are bounded by installed power. "
  "Seventy years of hybrid development has been an attempt to reach the corner that "
  "neither family occupies."),

 ("2",  "sekil02-zaman-cizelgesi.png",
  "Seventy years of attempts to merge the two families, with the recorded reason each "
  "programme ended. The two entries of 1954 and the reason the XFY-1 programme stopped "
  "are taken from [1] and [2]; the remaining entries carry no numerical claim."),

 ("3",  "sekil03-uc-fatura.png",
  "The three bills of the architectural tax and the moves that convert one into "
  "another. Every architectural remedy surveyed in Table 1 reduces one bill by "
  "increasing another. The measured instance quoted at the foot of the figure is "
  "derived in Section 3.5 from [3]."),

 ("4",  "sekil04-uc-gorunus.png",
  "The light reference design, 50 kg, in three orthogonal views: (a) planform, "
  "(b) front view, (c) side view showing the aerofoil section and the tip frames. "
  "Rendered from the parametric geometry model; the scale bar applies to all three "
  "views."),

 ("5",  "sekil05-serbest-gorunus.png",
  "General view of the same geometry. The single coaxial pair at the nose, the four "
  "small coaxial pairs at the ends of the tip frames, and the absence of any control "
  "surface are all visible."),

 ("6",  "sekil06-dagilimlar.png",
  "Spanwise distributions of the planform. (a) Leading-edge sweep falls from 45° at "
  "the root to 38.3° at the crop station while the trailing edge is held constant at "
  "25°; (b) thickness-to-chord ratio; (c) chord. These are one coupled distribution "
  "rather than three independent choices."),

 ("7",  "sekil07-moment-kollari.png",
  "Propeller placement and moment arms, front view. Every thrust vector is parallel "
  "to the body x axis. Pitch and yaw follow directly from differential thrust; the "
  "rolling moment is identically zero at every thrust setting, which is the gap the "
  "strip of Figure 8 exists to close."),

 ("8",  "sekil08-kanatcik-iz.png",
  "The roll strip against the main-propeller slipstream, viewed from below. The "
  "inboard 46 % of the strip lies inside the slipstream, where the dynamic pressure "
  "is set by disc loading and is therefore available at zero airspeed; the outboard "
  "54 % lies outside it and works against the freestream in cruise."),

 ("9",  "sekil09-ucus-profili.png",
  "The five phases of the flight profile, drawn from the parametric geometry model. "
  "The rotation in phase 3 is treated in Sections 7.3 and 7.4."),

 ("10", ["sekil10a-gecis-donus-suresi.png","sekil10b-tirmanarak-giris.png"],
  "Transition altitude loss. (a) Both reference designs against rotation time at four "
  "thrust-to-weight ratios: a slower rotation loses less altitude, not more. (b) The "
  "light design at T/W = 1.2 entering the rotation with an upward velocity w₀; an "
  "entry climb of 5 m s⁻¹ removes the loss at every rotation time considered."),

 ("11", "sekil11-iki-olcek.png",
  "The two reference designs at a common scale: 50 kg and 1000 kg, twenty times apart "
  "in mass and 3.35 times in span. Disc loading, energy-buffer mass fraction and "
  "tip-frame drag fraction are preserved across that range; transition time is not, and "
  "neither is the ratio of propeller diameter to span, which rises from 0.35 to 0.47 "
  "because holding the disc loading makes the propeller grow faster than the airframe."),

 ("12", "sekil12-menzil-LD.png",
  "Range against cruise lift-to-drag ratio for (a) a battery-electric and (b) a "
  "series-hybrid energy system. Filled markers are L/D values measured in wind-tunnel "
  "tests of one airframe [3]; open markers are the calculated reference designs of "
  "this study."),
]

# Sekil hangi bolumun sonuna yerlesecek — metindeki ilk atifa gore
YERLESIM = {
 "01-introduction":       ["1"],
 "02-background":         ["2"],
 "03-architectural-tax":  ["3","12"],
 "04-configuration":      ["4","5","6","7","8"],
 "06-reference-designs":  ["11"],
 "07-transition":         ["9","10"],
}
