# Rheaume & Lents 2016 — body text (for the round file)

**Source:** J. M. Rheaume and C. Lents, *Energy Storage for Commercial Hybrid Electric Aircraft*, SAE Technical Paper 2016-01-2014,
2016, doi:10.4271/2016-01-2014. File: `references/Rheaume-Lents-2016_SAE-2016-01-2014_energy-storage-hybrid-electric-aircraft.pdf`
(5 pages). **Extracted with `pdftotext`; paragraph breaks restored by hand from the page layout; the three tables are images in the PDF
and were transcribed by hand.** Reference list, contact details and disclaimer omitted.

#### Abstract

Energy storage options for a hybrid electric commercial single aisle aircraft were investigated. The propulsion system features twin Geared Turbofan™ engines in which each low speed spool is assisted by a 2,500 HP electric motor during takeoff and climb. During cruise, the aircraft is powered solely by the turbine engines which are sized for efficient operation during this mission phase. A survey of state of the art energy storage options was conducted. Battery, supercapacitor, and flywheel metrics were collected from the literature including Specific Energy (Wh/kg), Volumetric Energy Density (Wh/L), Specific Power (W/kg), Cost ($/kWh), and Number of Cycles. Energy storage in fuels was also considered along with various converters sized to produce a targeted quantity of electric power. The fuel and converters include fuel cells (both proton exchange membrane and solid oxide operating on hydrogen or on jet fuel) and a turbogenerator (jet fuel or LNG). The various energy storage options were compared across a range of stored energy on the basis of weight. The selection of a lightweight energy storage technology depends on power and quantity of energy storage. A turbogenerator auxiliary power unit has the best energy and power density for the application. The fuel cells tend to be heavy options due to low specific power. PEM fuel cells operating on compressed or liquid hydrogen are lighter weight than SOFCs, however, PEMFCs are comparable to batteries at the energy storage design point of 1500 kWh. Applications requiring low detectability and long duration favor PEM fuel cells.

#### Introduction

A hybrid electric aircraft propulsion system for a commercial single aisle aircraft motivates this investigation of energy storage. The hybrid architecture consists of twin Geared Turbofan™ engines assisted by 2,500 HP electric motors during takeoff and climb. The motors provide power to the low speed spools of each engine allowing the core to be downsized. (See Figure 1.) During cruise, the aircraft is powered solely by the turbine engines which are sized for efficient operation during this mission phase. As fuel mass decreases during cruise, excess power can be allocated to recharging energy storage by taking power off the low spool motor-generator. Earlier efforts indicated that 1500 kWh of energy is necessary to boost the fan during takeoff and climb [1].

The automotive industry has pioneered hybrid electric vehicle development. Several vehicles are available for sale from numerous manufacturers. The aerospace industry has not followed the automotive trend largely due to integration challenges, a long and costly product development cycle that includes airworthiness certification, and the weight of the additional motor, drive and energy storage systems.

Numerous prior studies exist on vehicular energy storage [2, 3, 4, 5, 6, 7]. This paper builds on previous work by reviewing and comparing state of the art energy storage methods as they relate to a commercial single aisle hybrid electric aircraft. Conventional technologies such as batteries, capacitors, and flywheels were considered. In addition, energy conversion devices such as fuel cells (both proton exchange membrane and solid oxide) and a turbogenerator (turbine directly coupled with an electric generator) were explored.

Metrics of state of the art energy storage technologies are tabulated for comparison. These metrics include: Specific Energy (Wh/kg), Volumetric Energy Density (Wh/L), Specific Power (W/kg), Cost ($/kWh), and Number of Cycles. On account of the importance of weight for aircraft applications, various energy storage technologies are compared for energy storage on a mass basis.

In the following, energy storage is examined from the point of view of hybrid propulsion of a commercial single aisle aircraft with focus on performance metrics that enable a hybrid electric aircraft architecture.

#### Methods

A literature survey was conducted in order to harvest metrics for comparison. These metrics were tabulated and used to estimate the weight of energy storage systems over a range of stored energy. Projections of future energy storage parameters were made for batteries and similarly compared. The design point is a 1,500 kWh energy storage system that delivers 5,000 HP for a commercial aircraft with a maximum takeoff gross weight of 62,000 kg.

Table 1. Energy Storage Performance Parameters *(an image in the PDF; transcribed by hand, bracketed numbers are the paper's reference numbers)*

| Technology | Specific Energy (Wh/kg) | Volumetric Energy Density (Wh/L) | Specific Power (W/kg) | Cost ($/kWh) | Cycles |
|---|---|---|---|---|---|
| Lead-Acid Battery | 20-50 [8] | 50-100 [8] | 150-300 [8] | 50-310 [9] | 1200-1800 [10] |
| Ni-Cd Battery | 40-60 [8] | 75-150 [8] | 150-200 [8] | 300 [8], 400-2400 [9] | 2000 [14] 3000 [10] |
| Ni-MH Battery | 60-100 [8] | 100-250 [8] | 250-1000 [14] | 300-500 [8] | 300 [10], 1000 [14] |
| Lithium-Ion Battery | 150-200 [11] | 200-300 [8] | 1800 [12] | 200-700 [8], 600-2500 [13] | 3000 [10] |
| Lithium-Polymer Battery | 130-200 [14] | 250 [15] | 3000 [12] | 333-500 [12] | >1000 [14] |
| Lithium-Air Battery | 400-800 [16] | 180-250 [15,16] | "Poor" [16] | n/a | 10 [16] |
| Lithium-Sulfur Battery | 200-700 [11] | 180-250 [15,16] | 750 [16] | n/a | 100 [14,16] |
| Sodium Sulfur Battery | 90–250 [14] | 167 [17] | 50 [14] | 180-500 [9] | >2500 [14] |
| Zinc-Air Battery | 200-300 [18] | 500 [13] | 70 [18] | 10-60 [13] | 100-300 [13] |
| Super-Capacitor | 1-10 [14] | 10 [8] | 500-10k [8], 10k-100k [14] | 20k [8] | >500k [14] |
| Fly-wheel | 10, 50-400 | 200 | 200-400 | 200-500, 400-800 | No limits |

*References cited in the table, from the paper's list: [8] Srinivasan 2006 (book); [12] Shukla & Kumar 2013, J. Phys. Chem. Lett.; [14] Chin 2011, NPS Masters thesis.*

The weight of energy converters was calculated from their specific power, and fuel was added to meet energy storage requirements. In contrast, battery weight was estimated solely on the basis of specific energy. Specific power is also likely to be a significant driver of weight but has not been considered in this analysis.

*[Figure 1, Parallel Hybrid Electric Geared Turbofan™ Architecture, and Figure 2, Energy Storage Weight, are figures and are not reproduced.]*

#### Results and Discussion

Values of energy storage parameters appear in Table 1 for conventional energy storage systems and in Table 2 for energy conversion systems (fuel cells, turbogenerator). An effort was made to select recent values in the appropriate size range.

Table 1 lists various types of batteries (loosely organized by technological maturity) followed by capacitors and flywheels. The best metrics in each category for each battery type were selected. Such batteries are not commercially available since they are usually optimized either for specific energy or specific power. The best metrics were selected in order to provide the best possible comparison with energy conversion devices. Multiple ranges of values and their sources were cited in the cases in which ranges differed. Cost information labelled as “n/a” applies to technologies in development (e.g. Li-S).

Table 2. Energy Converter Performance Parameters. All values exclude fuel and storage tank weights. *(image; transcribed)*

| Technology | Specific Power (W/kg) |
|---|---|
| PEMFC System with Fuel Processor | 140 [8] |
| PEMFC Stack plus BOP and excluding Fuel Processor | 500 |
| PEMFC Stack | >1000 [19,20] |
| SOFC System plus BOP including Fuel Processor (without Desulfurizer) | 100 |
| SOFC Stack | 500 |
| Gas Turbine-Driven Generator | 3,300 |

Lithium-air and lithium-sulfur batteries are attractive for high specific energy, however, these batteries are not widely available in the marketplace. Lithium polymer batteries exhibit attractive volumetric energy density as well as high specific power. The lithium chemistries tend to be more expensive than other options while offering high energy density. Supercapacitors exhibit low specific energy but outstanding specific power at high cost suggesting that this technology is more appropriate in a hybrid energy storage approach (e.g. supercapacitors and batteries). Flywheels exhibit attractive metrics, however, packaging remains challenging.

Energy converters (Table 2) rely on chemical energy storage, and their value proposition lies in the weight and efficiency of conversion. Fuel cells and a turbogenerator were considered.

Fuel cells were examined due to their high efficiency. The performance metrics of a fuel cell power system are dependent on the system size since efficiency varies with load. Generally no fuel cell power systems are available in the 5,000 HP class, so conservative values representative of automotive applications were chosen or estimated.

The specific power of fuel cell stacks and balance of plant (BOP) excluding fuel and tank weight were broken out separately in order to better understand the contribution of the stacks to the system weight.

Fuel processors that convert hydrocarbon fuels to a hydrogen-rich stream were included in the fuel cell system weight in order to make a direct comparison of the conversion of chemical energy to electricity. A likely fuel processor technology for aviation applications is partial oxidation due to low weight, however, autothermal reforming is more efficient than partial oxidation, and it is lighter weight than steam reforming.

For the fuel cell systems, the fuel is assumed to be desulfurized on account of the large weight penalty that a desulfurizer imposes; it has the potential to cut the specific power in half depending on the technology selected. Even with the advantage of desulfurized fuel, fuel cells exhibit lower specific power than a gas turbine-driven generator by a wide margin. The specific power of the turbogenerator in Table 2 was selected by identifying the specific powers of the turbine and generator (non-cryo-cooled) and combining them into one metric by taking the inverse of the sum of their reciprocals.

Competing engine technologies such as reciprocating engines and Wankel engines were not considered due to low specific power and consequently a dearth of commercial products available for aviation in the 5,000 HP class.

Turbogenerators are the lowest weight solution at the present time for the specified mission. The choice of liquid natural gas as fuel does not carry a significant weight penalty, however, it does increase system and logistical complexity.

For batteries, several energy storage densities are shown (200, 300, 500, and 1000 W-hr/kg). The current state of the art in commercially available lithium ion batteries is approximately 200 W-hr/kg. The higher battery energy densities allow one to set future targets for battery energy storage. The battery chemistry is not specified. No penalties for battery self-discharge and inefficiency of charging and discharging are applied in Fig. 2. In addition, the battery discharge rate metrics are not considered here.

The efficiency of conversion is also of interest. Fuel cells running on hydrogen exhibit over 50% efficiency, however, the fuel processing dramatically reduces the system efficiency. Partial oxidation is the lightest fuel conversion technology albeit the least efficient. The efficiency of a fuel cell power system with partial oxidation is on par with that of the lighter weight turbogenerator. When considering the fuel required to transport the energy converter, the turbogenerator exhibits favorable fuel consumption characteristics.

Figure 2 shows the weights of PEM fuel cells, turbogenerators, and batteries to deliver 5000 HP power over a range of stored energy including the design point of 1500 kWh. The PEM fuel cells operate on hydrogen in either compressed or liquid form. Not shown is the SOFC; the weight of a system that processes logistics fuel is several tens of thousands of kg excluding the desulfurizer. The weight of the ceramic stacks, their housing, the reformer, and nickel superalloy ducting combine for a massive and expensive system.

In Figure 2, power converters that operate on fuels other than Jet-A include the weight of the tank. For example, the turbogenerator that operates on Jet-A includes fuel weight but not tank weight because fuel tanks are already onboard, however, the turbogenerator operating on LNG includes fuel and tank weights. Similarly, the PEM fuel cell systems include the weight of the hydrogen fuel and tank because this fuel is not otherwise on the aircraft. The base PEM weight is the same for both cases, but compressed hydrogen storage is heavier than liquid.

Table 3. Energy to Transport Energy Storage System Mass throughout Mission. *(image; transcribed)*

| Energy Storage Technology | Transport Energy (kWh) | Fuel (lbm) |
|---|---|---|
| SOFC + Jet-A (S-free) | 6,067 | 1,121 |
| PEMFC + Comp H2 | 1,409 | 260 |
| PEMFC + LH2 | 1,232 | 228 |
| Battery 200 | 1,437 | 266 |
| Battery 300 | 958 | 177 |
| Battery 500 | 575 | 106 |
| Battery 1000 | 287 | 53 |
| GT-APU + LNG | 242 | 45 |
| GT-APU + Jet-A | 189 | 35 |

Despite consideration under ideal conditions, batteries are heavier than turbogenerators at the design point. For batteries to compete favorably for the intended application to assist takeoff and climb, a specific energy in excess of 1000 W-hr/kg is required. This value may further increase due to discharge losses, performance degradation, etc.

State-of-the-art batteries may find niche applications with small quantities of stored energy. The all electric Airbus E-Fan 2.0 training aircraft has 60 kW total propulsive power and can fly for an hour on a charge of lithium polymer batteries [21]. Reduced maintenance costs may result from the electric drivetrain.

Batteries have an inherent drawback: the weight of batteries remains unchanged throughout the flight envelope whereas jet fuel decreases in weight. Fuel must be expended to transport battery weight. Similarly, the weight of fuel cell and turbogenerator systems must be transported throughout the mission requiring additional energy, however, the fuel weight is significant. Table 3 quantifies the energy required to transport the various energy storage devices (and fuel other than -Jet-A when applicable) throughout a mission of 900 nm length (approx. 1.8 hr long) in which they provide 1525 kWh stored energy. The lower heating value of Jet-A fuel (42.9 MJ/kg) was used to calculate an equivalent fuel quantity. The fuel weight penalty that was used was derived from Pratt & Whitney aircraft and engine models.

Fuel for the turbogenerator and fuel cells was assumed to be completely consumed during takeoff and climb (no reserves). In reality, some reserves would be required in the event of an aborted landing to come around and to climb. In addition, fuel was assumed to be consumed at a constant rate during these mission phases. In reality, fuel consumption varies with power from a high during takeoff and tapering off during climb. The first assumption understates the energy required to transport fuel whereas the second one overstates it. Nevertheless, the conclusions are unlikely to change: batteries and fuel cells require large increases in specific energy in order to be competitive with the turbogenerators for this application. A factor 5 increase over the present state of the art specific energy will begin to make batteries competitive with present heat engines at the design point noting that specific power is a significant driver of battery weight but was not considered in this analysis. Until then, the transport of battery weight is prohibitively energy-intensive.

The turbogenerators (labelled as GT-APU) require the least weight to transport. They have high specific power and in contrast to batteries; the turbogenerators lose their fuel weight early in the flight. In the case of Jet-A fuel, no additional tank weight is required whereas LNG requires an additional tank. The SOFC utilizes Jet-A so no additional tank is required, however, at least an order of magnitude improvement in specific power (mass reduction) is necessary in order to be viable. The PEM fuel cell systems require almost as much energy to transport during the mission as they provide.

Factors other than fuel burn and specific energy may lead to the selection of different energy storage methods For example, if low noise and low IR signature are desired criteria, then a PEM fuel cell competes favorably against the turbogenerator. The PEM fuel cell is preferred over present batteries for stored energy greater than 1300 kWh for the given power rate provided that liquid hydrogen is available. The infrastructure to generate and distribute the hydrogen must also be considered. Similarly, recharging batteries must be taken into account (during descent, on ground, etc).

#### Summary/Conclusions

At the current state of the art, turbogenerators are the most promising technology for supplementary electricity aboard commercial hybrid electric aircraft. Batteries begin to be competitive with turbogenerators at 1000 W-hr/kg on the basis of specific energy, however, non-ideal performance may require even higher specific energy. This analysis of battery weight did not include specific power which may also significantly impact battery weight. A turbogenerator operating on jet fuel or LNG is the best option from the point of view of weight for larger energy storage quantities. Fuel cells are outperformed by batteries and turbogenerators except for applications requiring > 1300 kWh where noise and detectability are valued and liquid hydrogen is available.