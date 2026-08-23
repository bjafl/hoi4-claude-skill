---
title: Production and Equipment
category: mechanics
tags: [production, factories, efficiency, equipment, variants, licensing, conversion, lend-lease, stockpile]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Production
  - https://hoi4.paradoxwikis.com/Equipment
  - https://hoi4.paradoxwikis.com/Variant
  - https://hoi4.paradoxwikis.com/Diplomacy
---

## Summary

Military factories and naval dockyards turn industrial capacity and strategic resources into equipment on production lines. Military factories are scaled by production efficiency (which grows over time on an unchanged line); dockyards are not. Equipment is stockpiled and drawn on by divisions and air wings. This file covers factory output numbers, efficiency growth and retention, equipment conversion and ship refits, licensed production, variants and upgrades, resource shortages, lend-lease, and the land/armor equipment stat tables.

## Factories

| Factory type | Base output | Powered output (with coal) | Used for | Affected by production efficiency? |
|---|---|---|---|---|
| Civilian factory | 4 industrial capacity/day | 5 | Construction and repair, buying resources by trade, consumer goods, equipment licenses, the international market (Arms Against Tyranny), intelligence agencies and upgrades (La Résistance) | No |
| Military factory | 3.5 production cost/day | 4.5 | Land and air equipment, including infantry, artillery, tanks, air wings, railway equipment | Yes |
| Naval dockyard | 2 production cost/day | 2.5 | Ships, submarines, convoys, floating harbours | No |

Military factory daily output = `powered output × production efficiency × (1 + sum of factory output modifiers)`. The efficiency multiplier and the factory-output modifier are applied independently.

Worked example: a powered military factory at 50% efficiency, with Export Focus (+10% factory output) and −21.8% factory output from low stability, produces `4.5 × 0.5 × (1 + 0.10 − 0.218) = 1.9845` production cost per day.

Military factory and dockyard output are mainly driven by production technologies and industry technologies; civilian factory output is mainly driven by construction technologies and economy laws.

## Production lines

- Each production line makes a single equipment type at a time, using military factories (land/air) or dockyards (naval).
- **Up to 150 factories per production line.** A country can run several lines producing the same item.
- Dockyard-per-line caps: **5** for capital ships, **10** for screen ships and submarines, **15** for convoys, **5** for floating harbours (No Step Back).
- Military-factory-per-line caps for special land equipment: **5** each for railway guns and super-heavy railway guns (No Step Back), super-heavy howitzers and self-propelled super-heavy howitzers (Götterdämmerung), and land cruisers (Götterdämmerung).

Production line UI elements: item name and queue position; the MIO producing it (Arms Against Tyranny; without it, the design company); production efficiency; factory count; delete line; move line up/down the priority queue (drag-and-drop works); toggle equipment conversion mode; specialized role (e.g. tank destroyer); the MIO/design company used for the variant (an up arrow means a newer MIO version can be applied); target of production (reinforcements, upgrading fielded units, or stockpile) with the needed/stocked count; and resources consumed, red when short.

## Production efficiency

- Applies only to military factories, per production line.
- **Base (starting) efficiency: 10%** without modifiers. **Cap: 50%** without modifiers. Both are raised by industry technology, research and national focuses.
- Daily growth: `0.001 × cap² / current efficiency` (all values in the same units).
  - Minimum base growth ≈ **0.05%/day** (near a 50% cap); maximum **1%/day** (100% cap, 10% current efficiency).
- Relative time in days to reach a given efficiency: `t = 500 × (efficiency / cap)²`.
  - Going from 25% of cap to 75% of cap takes `500·0.75² − 500·0.25² = 250` days.
  - A fully-supplied line takes **at most 500 days** to reach its cap, a shortfall of at most 166.6 factory-days of output relative to a factory running at cap.
- Efficiency is tracked **per factory**. Adding new factories to an existing line gives only the *new* factories minimum efficiency; the existing ones keep theirs.
- When military factories are lost or damaged, the loss comes **off the bottom of the production list**, and those factories lose their efficiency. Keep high-priority, high-efficiency lines high in the list.
- Some equipment is exempt from passive efficiency growth — most notably **railway guns** (No Step Back). Their lines can only be improved by raising base production efficiency.

### Production efficiency retention (switching a line)

Switching a line's equipment cancels the current item's progress and cuts efficiency. Base retention depends on how far the switch goes:

| Retained | Kind of switch | Example |
|---|---|---|
| 90% | Different variant of the same model — including switching between license production and own production of the same equipment type | Panzer III Ausf. F → Ausf. G; Italian Fighter II C.202 Folgore → German Fighter II FW190 |
| 70% | Different model on the same chassis | Panzer III → StuG III (medium tank 1 → medium tank destroyer 1) |
| 30% | Direct upgrade or downgrade of the same equipment type | Panzer III → Panzer IV (medium tank 1 → medium tank 2) |
| 20% | Indirect upgrade or downgrade of the same equipment type | Panzer III → Panther (medium tank 1 → medium tank 3) |
| 10% | Anything else | Infantry Equipment 1 → Towed Artillery 1 |

Retention bonuses come from Dispersed industry I–V (+10% each) and Flexible line (+20%) — up to +70% — plus some national spirits and unique political advisors. **Changing variant always loses 10% regardless of bonuses.**

The bonus is applied to the *loss*, not added to the retention:

```
New efficiency = CPE × ( RET + (1 − RET) × BON )
Real efficiency = max( New efficiency, base production efficiency )
```
where CPE = current production efficiency, RET = base retention from the table, BON = retention bonus.

Example: 10% base retention means a 90% loss; a +10% retention bonus removes 10% of that 90% = 9%, giving 19% effective retention. The bonus is worth more the lower the base retention.

Switching a line **back** to its previous equipment does not restore lost efficiency — retention is computed purely from the difference between the current and the target equipment.

### Ships

Dockyards have no production efficiency: each produces a flat 2 production cost/day (2.5 powered) modified only by dockyard output modifiers. Changing a dockyard line loses all progress on the incomplete ship but the dockyards run at full rate on the new item immediately.

Ship **repair** also consumes dockyards: each dockyard repairs at most one ship at a time, the maximum number of repairing dockyards is set in the production screen, and repairing dockyards are removed from active production lines until finished.

## Equipment conversion

A production line can be switched to *convert* obsolete or foreign (captured, lend-leased, license-built or purchased) equipment of the same chassis, via the button at the bottom-left of the line's box. Conversion:
- Can be toggled at any time and **costs no production efficiency**.
- Reverts automatically to production from raw materials when the input stock runs out.
- Consumes strategic resources **only to the extent the new design needs them and the old one did not**.
- Is generally faster than building from scratch, and is sped up further by the equipment conversion technologies.

To convert, the existing design must be marked **decommissioned** (automatic for foreign equipment) and share the **same chassis** as the target (a 1934 light tank cannot become a 1936 light tank).

| Conversion target | Converts domestic designs | Converts foreign designs |
|---|---|---|
| Domestic design, same model¹ | Yes | No |
| Foreign license, same model | No | Only with tank (No Step Back) / ship / aircraft (By Blood Alone) designers², and only same national origin |
| Domestic design, different model | Yes | Yes |
| Foreign license, different model | Yes | Yes |

¹ A "model" means Tank/TD/SPA/SPAA, or Fighter/CAS/etc. — the aircraft grouping exists only with By Blood Alone; without it every plane is a separate chassis.
² Same national origin only.

**Conversion cost:** `(base_chassis_cost × (0.9 − tech) + new_module_cost) × prod_modifiers + dismantle_costs`
- The base chassis cost is not shown on the research or production screens (those include modules); it appears in the designer's production-cost tooltip.
- Production modifiers come from armour types and modules.
- Dismantle cost is paid whenever a module changes from the old design, **including moving a module between slots**.

### Conversion speed bonuses

Conversion speed bonuses (equipment conversion technologies, focuses such as Salvaged and Retooled) increase the *savings* from conversion, not the whole cost.

Example: an aircraft with a full cost of 30 whose conversion cost is 20 has savings of 10. A +40% conversion bonus raises the savings to 14, so the conversion costs `30 − 10 × 1.4 = 16`. With both conversion bonuses researched: `30 − 10 × (1 + 0.4 + 0.4) = 12`.

Building a bare-bones design and then converting it to the full design is often only a few percent more expensive in total production cost but can halve the strategic-resource cost. With extra conversion bonuses it can be outright cheaper.

> ⚠️ The wiki notes the UI wrongly highlights conversion-speed bonuses when refitting ships; those bonuses are **not** applied to refits.

### Ship refits

Ships are refitted individually from the task force panel, and consume significant dockyard time (engines and armour especially). A refit can be cancelled safely until it is 20% complete; after that, cancelling requires scuttling the ship. To refit a foreign ship taken in a peace conference, create a new design from the design tab of the ship's info panel — this sometimes fails to produce a valid refit target.

**Refit cost:** `old_design_cost × (0.2 + newly_added_module_prod_modifiers) + (module_upgrade_cost if available, else new_module_cost) × prod_modifiers + dismantle_costs`. Carrier conversions use the same formula.
- Module upgrade costs generally exist only when moving between tiers within the same module category (e.g. anti-air 1 → 2/3/4). They are usually cheaper than a new module, but for light cruiser batteries, heavy cruiser batteries and engines they can be two or three times more expensive. Engine upgrade costs apply only within the same engine category — so converting a cruiser/heavy-ship engine to a carrier engine avoids them, while staying in the same category and changing tier does not.
- Dismantle costs apply mainly to armour modules and (in small amounts) torpedo launchers. Removing battleship or battlecruiser armour to build a carrier makes such carrier conversions **more expensive than building a new carrier**.

Ship refitting speed bonuses (e.g. the Naval Refit Yards officer corps spirit, focuses like Expand the Repair Yards) act as extra dockyard output applied only during refits, so they matter less the more dockyard output the country already has.

## Resources in production

- Each nation may use a share of the strategic resources on its territory for production; the rest is reserved for export. The split is set by **trade law** (Closed Economy = 100% domestic, 0% exported). Overlords can access puppet resources beyond what trade laws would give.
- **Resources cannot be stockpiled.** They flow straight into production and any surplus is wasted. Only **fuel refined from oil** can be stockpiled.
- Excavation technologies: +10% resource gain efficiency each, five levels, **+50%** total, on extracted resources only (not synthetic refinery output or imports).
- Infrastructure: **+15% extracted resources per level in that state**, five levels, **+75%** total. A High Capacity Electrical Grid (state-level) adds **+10% resources gained per infrastructure**.
- **+20%** resource extraction in a state that contains a Supply Hub or Naval Base connected to the capital by rail or sea. Most states have this at game start.

### Resource shortage penalty

Missing resources apply an efficiency penalty to the **lowest-priority** production lines, up to −100%. The penalty is **−5% per missing unit of each resource type**, applied per factory, and the highest applicable penalty is used for a given factory.

Worked example: with 2 steel and 0 aluminium available, adding an 11-factory Support Equipment line (2 steel + 1 aluminium each):
- Factory 1: −5% (missing 1 aluminium).
- Factory 2: −10% (missing 2 steel and 1 aluminium).
- Each further factory: another −10% (2 more steel), so the last factories hit −100% and produce nothing.
- The line displays the average, −50%. The penalty stacks **multiplicatively** with other modifiers.

Some national spirits, focuses and advisors reduce these penalties. Note that production efficiency growth is **not** affected by resource shortages, so it can be worth starting a line under-supplied (output loss is smallest at low efficiency) and using the civilian factories elsewhere.

### Ways to get more resources

Trade for them; resource prospecting decisions and national focuses; build infrastructure in resource states; build a supply hub or naval base in a resource state that lacks one and connect it to the capital; build synthetic refineries; change trade law to keep more domestically; research excavation technologies; conquer resource states; gain resource rights via peace conferences or unique decisions.

### Ways to use fewer resources

- Lower-tier equipment, components and chassis usually cost fewer resources.
- Aircraft designs with **Non-Strategic Material Usage** need less aluminium.
- Omitting resource-costing modules (Squeeze-Bore Adaptor, Flight Deck Armor, Self Sealing Fuel Tanks) cuts costs.
- Build a bare-bones tank/aircraft and convert it to the full design — conversion only charges resources for the *difference*.
- Build ships without expensive modules and refit them afterwards: a cruiser built with no armour and refitted to Cruiser Armor IV pays the chromium only during the refit, not throughout production.
- Some MIO bonuses reduce resource requirements. The **Vertical Integration** and **Permanent Industrial Revolution** MIO policies reduce resource requirements for all MIO equipment; Vertical Integration also increases the penalty for lacking resources.

## Stockpiles

Land divisions and air wings are not built as units — factories produce individual pieces of equipment which then fill divisions and wings. Unlike resources, **equipment is stockpiled**; stockpiles are viewed in the Logistics tab. A production line can be directed at reinforcements, at upgrading fielded units, or at the stockpile.

### Equipment used by land units

| Equipment | Used by |
|---|---|
| Amphibious Mechanized (Amtrac) | Amtrac battalion |
| Amphibious Tank | Amphibious tank |
| Anti-Air | Anti-air, Motorized anti-air, Support Anti-air |
| Anti-Tank | Anti-tank, Motorized anti-tank, Support Anti-tank |
| Armored Car | Armored car, Armored car recon (La Résistance) |
| Artillery | Artillery, Motorized artillery, Support Artillery |
| Heavy Amphibious Tank | Heavy amphibious tank (No Step Back) |
| Heavy Flame Tank | Heavy flame tank (No Step Back) |
| Heavy SP Anti-Air / Heavy SP Artillery / Heavy Tank / Heavy Tank Destroyer | Corresponding heavy armour battalions |
| Infantry Equipment | Infantry, Bicycle battalion, Penal Battalion, Militia, Irregular Infantry, Marines, Marine Commandos (Arms Against Tyranny), Mountaineers, Paratroopers, Cavalry, Camelry (By Blood Alone), Motorized, Mechanized, Amtrac battalion, Engineer company, Pioneers (AAT), Jungle Pioneers (Trial of Allegiance or Götterdämmerung), Cavalry recon, Motorized recon, Recon Rangers (AAT), Long range patrol (AAT), Military police, Assault battalion (BBA), Winter Logistics (AAT) |
| Light Amphibious Tank / Light Flame Tank | Corresponding battalions (No Step Back) |
| Light SP Anti-Air / Light SP Artillery / Light Tank Destroyer | Corresponding light armour battalions |
| Light Tank | Light tank, Armored recon, Airborne light armor (AAT) |
| Mechanized | Mechanized |
| Medium Amphibious Tank / Medium Flame Tank | Corresponding battalions (No Step Back) |
| Medium SP Anti-Air / Medium SP Artillery / Medium Tank / Medium Tank Destroyer | Corresponding medium armour battalions |
| Modern SP Anti-Air / Modern SP Artillery / Modern Tank / Modern Tank Destroyer | Corresponding modern armour battalions |
| Trucks | Motorized, Motorized anti-air/anti-tank/artillery, Motorized Rocket Artillery, Truck-Drawn Rocket Artillery, Motorized recon, Field hospital, Logistics company, Signal company |
| Motorized Rocket Artillery | Motorized Rocket Artillery |
| Rocket Artillery | Rocket Artillery, Support Rocket Artillery, Truck-Drawn Rocket Artillery |
| Super Heavy SP Anti-Air / SP Artillery / Tank / Tank Destroyer | Corresponding super-heavy battalions |
| Support Equipment | Bicycle battalion, Engineer company, Pioneers (AAT), Jungle Pioneers (ToA/Gött), Cavalry recon, Motorized recon, Recon Rangers (AAT), Long range patrol (AAT), Military police, Maintenance company, Field hospital, Logistics company, Signal company, Assault battalion (BBA), Winter Logistics (AAT) |

## Equipment: archetypes, types, variants

- **Archetype** — the general class a unit asks for. A division needing 100 medium tanks accepts any mix of Panzer III, Panzer IV, Panther or foreign medium tank variants. Different archetypes (light vs. medium tanks) are never interchangeable.
- **Type** — a specific researched item within an archetype (Infantry Equipment 1, Infantry Equipment 2...). Types form the basis of the variants a country creates.
- **Parent** — the type unlocked by the previous technology in the same archetype chain (Infantry Equipment 1 is the parent of Infantry Equipment 2). Parentage determines production efficiency retention.
- **Family** — types sharing mechanical parts, making transitions easier. Each tank type plus the armoured vehicles built on it form a family.
- **Variant** — the concrete, country-specific class. Researching a technology automatically creates a base variant using whatever design company the country has at that moment (the company need not be hired when research starts; only when it completes). Variants can also be licensed from other countries.
- **Designer** — a design company's bonuses attach to all variants of an equipment type unlocked while that company is employed.

### Variant statistics

Additive and averaged-additive module stats are added to the equipment type's stats. Multiplicative module stats, designer stats and upgrade stats **stack additively with each other** and are then applied as a single factor.

Example: Japan with Mitsubishi (+20% agility, +10% speed) completes the 1940 fighter type (agility 65). The resulting Ki-43 Hayabusa has `65 × 1.20 = 78` agility. Adding five Engine upgrade points (5 × 5% agility) gives `65 × 1.45 = 94.25` agility on the Ki-43 Hayabusa Kai A.

### Equipment upgrades (when the designers are disabled)

Where the tank/ship/plane designer DLC is not active, equipment is customised with **upgrades** bought with experience.

- Each upgrade can be taken up to **5 times**, at any time.
- **Land equipment: first upgrade level costs 10 experience. Air and naval equipment: 25 experience. Each subsequent level costs 5 more.**
- Upgrades often trade one stat for another (complexity reduces reliability, weight reduces speed). Maintenance support companies raise equipment reliability in a division.

**Land upgrades**

| Upgrade | Applies to | Bonus | Penalty |
|---|---|---|---|
| Armor | all armor, armored cars, mechanized | +5% Armor | −2% Speed, −5% Reliability |
| Engine | all armor, mechanized | +4% Speed | – |
| Engine | armored cars | +2% Speed | – |
| Reliability | all armor, armored cars, mechanized | +10% Reliability | – |
| Main Gun | tanks, armored cars | +3% Soft Attack, +10% Hard Attack, +5% Piercing | −2% Speed, −5% Reliability |
| Production Cost | mechanized | −10% Production Cost | −4% Reliability |
| Anti-Air Armament | self-propelled AA | +15% Air Attack | −2% Speed, −5% Reliability |
| Anti-Tank Armament | tank destroyers | +10% Soft Attack, +10% Hard Attack, +5% Piercing | −2% Speed, −5% Reliability |
| Artillery Armament | self-propelled artillery | +3% Soft Attack | −2% Speed, −5% Reliability |

**Naval upgrades**

| Upgrade | Applies to | Bonus | Penalty |
|---|---|---|---|
| Gun | CL, CA, torpedo cruiser, heavy ships | +4% Light Attack, +5% Light Piercing, +4% Heavy Attack, +5% Heavy Piercing | −1% Max Speed, −0.5% Reliability |
| Torpedo | torpedo cruiser, DD | +7.5% Torpedo Attack | −1% Max Speed, −1% Max Range |
| Armor | CA, heavy ships | +5% Armor | −1% Speed |
| Engine | CV, heavy ships, CL, CA, torpedo cruiser | +3% Speed, +5% Max Range | −0.5% Reliability |
| Engine | DD | +3% Speed, +5% Max Range | – |
| Reliability | CV, heavy ships, SS, CL, CA, torpedo cruiser | +1.5% Reliability | −4% Max Range |
| Anti-Air | CL, DD | +5% Anti-air | −1% Max Speed |
| ASW | DD | +4% Sub Detection, +4% Depth Charge | −1% Torpedo Attack |
| Torpedo | SS | +4% Torpedo Attack | −2% Max Speed |
| Stealth | SS | −5% Sub Visibility | −2% Max Speed |
| Engine | SS | +5% Max Speed, +5% Max Range | +5% Sub Visibility, −0.5% Reliability |
| Deck Space | CV | +7.5% Deck Space | −5% Armor |
| Armor | CV | +10% Armor, +1% HP | −4% Deck Space |

**Air upgrades**

| Upgrade | Applies to | Bonus | Penalty |
|---|---|---|---|
| Weapons | (jet/heavy) fighter, rocket interceptor | +10% Air Attack | −1% Speed, −10% Reliability, −5% Agility |
| Weapons | carrier fighter | +10% Air Attack | −1% Speed, −10% Reliability, −15% Agility |
| Range | all non-carrier types | +10% Range | −10% Reliability |
| Range | all carrier types | +15% Range | −10% Reliability |
| Engine | all | +2% Speed, +5% Agility | – |
| Reliability | all | +10% Reliability | – |
| Attack | naval bomber | +5% Naval Attack | −10% Reliability |
| Attack | carrier naval bomber | +5% Naval Attack | −15% Reliability |
| Bombing | (jet) strategic bomber | +5% Bombing | −10% Reliability, −5% Range |
| Bombing | (jet) tactical bomber | +2% Bombing, +2% Ground Attack | −10% Reliability, −5% Agility |
| Attack | (carrier) CAS | +2% Air Attack, +5% Ground Attack | −10% Reliability, −5% Agility |
| Armor | scout plane | +5% Air Defense | −5% Range |

With the designer DLCs active, modules replace upgrades: hulls, chassis and airframes are researched individually and provide module slots, and variants are assembled from researched modules at a cost of navy / army / air experience.

## Production licenses

- Base cost: **1 civilian factory** for a license on 1936-or-earlier technology, **+1 civilian factory per technology year beyond 1936**. Towed Artillery (1936) = 1 factory; Improved Artillery (1939) = 4 factories; Advanced Artillery (1942) = 7 factories.
- The civilian factories go to the licensing country while the license is active.
- A license **cannot be cancelled for 30 days**.
- A license grants **+20% research speed** on the technology that unlocks the domestic version. For designer equipment, only the base chassis/hull/airframe technology gets the bonus.
- AI willingness to license depends on relations and how modern the technology is; national focuses may grant licenses directly.

Production penalties for building foreign equipment, applied **multiplicatively** to factory or dockyard output:

| Situation | Penalty |
|---|---|
| Licensed equipment from a faction member | −25% |
| Licensed equipment from a non-faction member | −35% |
| No license for the foreign equipment | −50% |
| Foreign equipment is ahead of time | additional −5% per year ahead, max −20% |

Focus bonuses can offset these (License German Equipment, Befriend Japan); Hungary's **Extensive Licensing Program** can make licensed production faster than domestic.

Other licensing rules:
- Creating a variant of licensed equipment costs **2× the experience** of a domestic variant.
- Design company and MIO bonuses on the original equipment **do not** transfer with the license. Country-wide bonuses from national spirits, political advisors and Air Production that affect production cost **do** transfer.
- With Arms Against Tyranny, **MIOs cannot be assigned to foreign-equipment production lines**, so they neither apply their bonuses nor gather funds/experience from them.

> ⚠️ As of v1.16.9 the wiki reports a bug where component modules of licensed **ship** designs can be used on domestic hulls without the required technology, triggered by loading a save while the license is active. Similar bugs are unofficially reported for tank (No Step Back) and aircraft (By Blood Alone) designs.

## Lend-lease

- **Start Lend Lease** sends any equipment to a non-enemy country that is currently at war. You may send a single shipment of a fixed amount, or a recurring monthly amount **or** a percentage of monthly production (not both at once).
- Shipments occur **once per month**. Past and present shipments appear in the Lend-Lease tooltip at the top of the Recruit/Deploy window.
- Requirements: the **receiving** country must have enough convoys, unless there is an unobstructed land path; a world tension threshold must be met.
- Lend-lease can be modified or cancelled at any time by clicking the Lend Lease action.
- **Request lend lease** asks another country to send specific equipment archetypes; the selection screen shows their stockpile and production rates. You must be at war and the target must accept.
- Lend-lease routes are drawn on the map like trade and market delivery routes.
- Some ideas modify the **lend lease tension limit** (e.g. Autarky, +20%).

## International market (requires Arms Against Tyranny)

Equipment can also be bought and sold for industrial capacity. See [Trade, resources and the international market](trade-resources-and-market.md).

---

## Land equipment statistics

Column order: Speed (km/h) | Soft attack | Hard attack | Air attack | Defense | Breakthrough | Armor | Piercing | Hardness | Fuel usage | Reliability | Production cost | then resources per factory (Steel / Tungsten / Chromium / Aluminium / Rubber). Blank = zero or not applicable.

| Type | Equipment | Speed | Soft att | Hard att | Air att | Def | Break | Armor | Pierc | Hardness | Fuel use | Reliab | Cost | Steel | Tung | Chrom | Alum | Rubber |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Infantry Eq. | Basic Eq. | 4 | 3 | 0.5 | – | 20 | 2 | – | 1 | – | – | 90% | 0.43 | 2 | – | – | – | – |
| Infantry Eq. | Weapons I | 4 | 6 | 1 | – | 22 | 3 | – | 4 | – | – | 90% | 0.5 | 2 | – | – | – | – |
| Infantry Eq. | Weapons II | 4 | 9 | 1.5 | – | 28 | 4 | – | 5 | – | – | 90% | 0.58 | 3 | – | – | – | – |
| Infantry Eq. | Weapons III | 4 | 12 | 2 | – | 34 | 5 | – | 10 | – | – | 80% | 0.69 | 4 | – | – | – | – |
| Motorized | Truck | 12 | – | – | – | – | 5 | – | – | 10% | 1.2 | 80% | 2.5 | 1 | – | – | – | 1 |
| Motorized | Armor Car 1 | 9 | 6 | 2 | – | 2 | 12 | 3 | 6 | 65% | 0.8 | 80% | 4 | 2 | – | – | – | – |
| Motorized | Armor Car 2 | 12 | 13 | 4 | – | 3 | 16 | 10 | 8 | 65% | 1.8 | 80% | 6 | 2 | – | – | – | – |
| Motorized | Armor Car 3 | 15 | 16 | 8 | – | 5 | 28 | 20 | 36 | 70% | 1.8 | 80% | 8 | 2 | 1 | – | – | – |
| Motorized | Armor Car Anti-Tank | 16 | 12 | 14 | – | 6 | 28 | 20 | 62 | 70% | 1.8 | 80% | 9 | 2 | 1 | – | – | – |
| Mot. R. Artillery | Mot. Rocket Artillery | – | 36 | 1 | – | 15 | 12 | – | 2 | – | 1.2 | 80% | 12 | 1 | 2 | – | – | 1 |
| Mechanized | Mechanized I | 8 | – | – | – | 26 | 6 | 10 | 11 | 60% | 2.4 | 80% | 8 | 2 | – | – | – | 1 |
| Mechanized | Mechanized II | 10 | – | – | – | 30 | 8 | 15 | 16 | 70% | 2.4 | 80% | 10 | 3 | – | – | – | 1 |
| Mechanized | Mechanized III | 12 | – | – | – | 34 | 10 | 20 | 21 | 75% | 2.4 | 80% | 12 | 4 | – | – | – | 1 |
| Amph. Mechanized | Amphibious Mechanized 1 | 7 | – | – | – | 26 | 4 | 10 | 11 | 60% | 4 | 80% | 8 | 2 | – | – | – | 1 |
| Amph. Mechanized | Amphibious Mechanized 2 | 10 | – | – | – | 30 | 5 | 15 | 16 | 70% | 4 | 80% | 10 | 3 | – | – | – | 1 |
| Artillery | Artillery | – | 25 | 2 | – | 10 | 6 | – | 5 | – | – | 80% | 3.5 | 2 | 1 | – | – | – |
| Artillery | Improved Artillery | – | 30 | 2 | – | 15 | 7 | – | 5 | – | – | 80% | 4 | 2 | 1 | – | – | – |
| Artillery | Advanced Artillery | – | 34 | 2 | – | 18 | 8 | – | 5 | – | – | 80% | 4.5 | 3 | 1 | – | – | – |
| Rocket Artillery | Rocket Artillery | – | 30 | 1 | – | 12 | 9 | – | 2 | – | – | 80% | 4 | 1 | 2 | – | – | – |
| Rocket Artillery | Advanced Rocket Artillery | – | 38 | 1 | – | 15 | 12 | – | 2 | – | – | 80% | 5 | 1 | 2 | – | – | – |
| Anti-Tank | Anti-Tank | – | 4 | 20 | – | 4 | – | – | 60 | 10% | – | 80% | 4 | 2 | 2 | – | – | – |
| Anti-Tank | Improved Anti-Tank | – | 4 | 22 | – | 4 | – | – | 90 | 10% | – | 80% | 5 | 2 | 2 | 1 | – | – |
| Anti-Tank | Advanced Anti-Tank | – | 4 | 30 | – | 4 | – | – | 125 | 10% | – | 80% | 6 | 3 | 2 | 1 | – | – |
| Anti-Air | Anti-Air | – | 3 | 7 | 19 | 4 | 1 | – | 25 | – | – | 80% | 4 | 2 | – | – | – | – |
| Anti-Air | Improved Anti-Air | – | 3.5 | 11 | 25 | 4 | 1 | – | 60 | – | – | 80% | 5 | 2 | – | – | – | – |
| Anti-Air | Advanced Anti-Air | – | 4 | 15 | 32 | 4 | 1 | – | 88 | – | – | 80% | 6 | 3 | – | – | – | – |
| Support Eq. | Support Equipment | – | – | – | – | – | – | – | – | – | – | 80% | 4 | 2 | – | – | 1 | – |

## Armor equipment statistics

Excludes armour designed with the No Step Back tank designer. Same column order, plus the equipment each item can be converted from.

| Type | Equipment | Speed | Soft att | Hard att | Air att | Def | Break | Armor | Pierc | Hardness | Fuel use | Reliab | Cost | Steel | Tung | Chrom | Convertible from |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light Tank | Great War Tank | 6 | 8 | 4 | – | 4 | 18 | 5 | 15 | 80% | 1.0 | 80% | 7 | 1 | – | – | – |
| Light Tank | L. Tank I | 10 | 13 | 4 | – | 4 | 26 | 10 | 10 | 80% | 2.4 | 80% | 8 | 2 | – | – | – |
| Light Tank | L. Tank II | 12 | 16 | 6 | – | 5 | 36 | 15 | 30 | 80% | 2.4 | 80% | 9 | 3 | – | – | – |
| Light Tank | L. Tank III | 14 | 22 | 9 | – | 6 | 46 | 30 | 50 | 80% | 2.4 | 80% | 10 | 4 | – | – | – |
| Light SP Artillery | L. SPG I | 10 | 34 | 0.5 | – | 4 | 2 | 5 | 4 | 50% | 1.2 | 80% | 8 | 2 | 1 | – | L. Tank I |
| Light SP Artillery | L. SPG II | 12 | 42 | 1 | – | 5 | 2.5 | 10 | 0 | 50% | 1.2 | 80% | 9 | 3 | 1 | – | L. Tank I, L. Tank II |
| Light SP Artillery | L. SPG III | 14 | 46 | 1.5 | – | 7 | 3.5 | 25 | 0 | 50% | 1.2 | 80% | 10 | 4 | 1 | – | L. Tank II, L. Tank III |
| L. Tank Destroyer | L. TD I | 10 | 6 | 10 | – | 4 | 1 | 10 | 50 | 80% | 1.2 | 80% | 8 | 2 | 2 | – | L. Tank I |
| L. Tank Destroyer | L. TD II | 12 | 6 | 16 | – | 5 | 1.3 | 15 | 77 | 80% | 1.2 | 80% | 9 | 3 | 2 | – | L. Tank I, L. Tank II |
| L. Tank Destroyer | L. TD III | 14 | 8 | 24 | – | 7 | 1.8 | 30 | 99 | 80% | 1.2 | 80% | 10 | 4 | 2 | – | L. Tank II, L. Tank III |
| Light SP Anti-Air | L. AA I | 10 | 2 | 1 | 15 | 2 | 2 | 5 | 5 | 50% | 0.6 | 80% | 10 | 2 | – | – | L. Tank I |
| Light SP Anti-Air | L. AA II | 12 | 3 | 1.5 | 17 | 2.5 | 2.5 | 10 | 20 | 50% | 0.6 | 80% | 11 | 3 | – | – | L. Tank I, L. Tank II |
| Light SP Anti-Air | L. AA III | 14 | 4.5 | 4 | 32 | 3.5 | 3.5 | 25 | 35 | 50% | 0.6 | 80% | 12 | 4 | – | – | L. Tank II, L. Tank III |
| Medium Tank | M. Tank I | 8 | 19 | 14 | – | 5 | 36 | 60 | 61 | 90% | 3.6 | 80% | 12 | 2 | 2 | – | – |
| Medium Tank | M. Tank II | 9 | 25 | 19 | – | 7 | 51 | 80 | 81 | 85% | 3.6 | 80% | 13 | 3 | 2 | – | – |
| Medium Tank | M. Tank III | 10 | 32 | 24 | – | 9 | 66 | 90 | 91 | 85% | 3.6 | 80% | 14 | 4 | 2 | – | – |
| M. SP Artillery | M. SPG I | 8 | 42 | 1 | – | 5 | 3 | 45 | 5 | 65% | 1.8 | 80% | 12 | 2 | 3 | – | M. Tank I, M. Tank II |
| M. SP Artillery | M. SPG II | 9 | 50 | 1.5 | – | 6 | 3 | 50 | 0 | 65% | 1.8 | 80% | 13 | 3 | 3 | – | M. Tank I, M. Tank II |
| M. SP Artillery | M. SPG III | 10 | 55 | 2 | – | 7 | 4 | 58 | 0 | 65% | 1.8 | 80% | 14 | 4 | 3 | – | M. Tank II, M. Tank III |
| M. Tank Destroyer | M. TD I | 8 | 5 | 20 | – | 5 | 1.3 | 60 | 88 | 90% | 1.8 | 80% | 12 | 2 | 4 | – | M. Tank I |
| M. Tank Destroyer | M. TD II | 9 | 6 | 26 | – | 6 | 1.5 | 80 | 110 | 85% | 1.8 | 80% | 13 | 3 | 4 | – | M. Tank I, M. Tank II |
| M. Tank Destroyer | M. TD III | 10 | 8 | 32 | – | 7 | 1.8 | 90 | 120 | 85% | 1.8 | 80% | 14 | 4 | 4 | – | M. Tank II, M. Tank III |
| M. SP Anti-Air | M. AA I | 8 | 4.5 | 3 | 22 | 2.5 | 2.5 | 45 | 40 | 65% | 0.9 | 80% | 12 | 2 | 2 | – | M. Tank I, M. Tank II |
| M. SP Anti-Air | M. AA II | 9 | 6 | 4.5 | 32 | 3 | 3 | 50 | 60 | 65% | 0.9 | 80% | 13 | 3 | 2 | – | M. Tank I, M. Tank II |
| M. SP Anti-Air | M. AA III | 10 | 7.5 | 6 | 43 | 3.5 | 3.5 | 58 | 70 | 65% | 0.9 | 80% | 14 | 4 | 2 | – | M. Tank II, M. Tank III |
| Heavy Tank | H. Tank I | 5 | 15 | 12 | – | 6 | 36 | 70 | 35 | 95% | 4.4 | 80% | 25 | 3 | – | 3 | – |
| Heavy Tank | H. Tank II | 6 | 27 | 30 | – | 8 | 52 | 110 | 111 | 95% | 4.4 | 80% | 27 | 3 | – | 3 | – |
| Heavy Tank | H. Tank III | 6 | 35 | 40 | – | 9 | 67 | 130 | 131 | 95% | 4.4 | 80% | 30 | 4 | – | 3 | – |
| Heavy SP Artillery | H. SPG I | 5 | 55 | 1 | – | 4 | 2 | 45 | 8 | 80% | 2.2 | 80% | 25 | 3 | – | 3 | H. Tank I |
| Heavy SP Artillery | H. SPG II | 6 | 74 | 2 | – | 6 | 3 | 68 | 0 | 80% | 2.2 | 80% | 27 | 4 | – | 3 | H. Tank I, H. Tank II |
| Heavy SP Artillery | H. SPG III | 6 | 80 | 2.5 | – | 7 | 3.5 | 90 | 0 | 80% | 2.2 | 80% | 30 | 5 | – | 3 | H. Tank II, H. Tank III |
| H. Tank Destroyer | H. TD I | 5 | 6 | 25 | – | 4 | 1 | 70 | 96 | 95% | 2.2 | 80% | 25 | 3 | – | 3 | H. Tank I |
| H. Tank Destroyer | H. TD II | 6 | 8 | 42 | – | 6 | 1.5 | 110 | 140 | 95% | 2.2 | 80% | 27 | 4 | – | 3 | H. Tank I, H. Tank II |
| H. Tank Destroyer | H. TD III | 6 | 10 | 60 | – | 7 | 1.8 | 130 | 160 | 95% | 2.2 | 80% | 30 | 4 | – | 4 | H. Tank II, H. Tank III |
| Heavy SP Anti-Air | H. AA I | 5 | 4.5 | 4 | 17 | 2 | 2 | 45 | 25 | 80% | 1.1 | 80% | 25 | 3 | – | 3 | H. Tank I |
| Heavy SP Anti-Air | H. AA II | 6 | 6 | 4.5 | 33 | 3 | 3 | 68 | 60 | 80% | 1.1 | 80% | 27 | 3 | – | 3 | H. Tank I, H. Tank II |
| Heavy SP Anti-Air | H. AA III | 6 | 7.5 | 6 | 44 | 3.5 | 3.5 | 90 | 88 | 80% | 1.1 | 80% | 30 | 4 | – | 3 | H. Tank II, H. Tank III |
| Super Heavy Tank | SH. Tank | 4 | 38 | 45 | – | 10 | 74 | 145 | 146 | 99% | 10.0 | 80% | 100 | 3 | – | 4 | – |
| SH. SP Artillery | SH. SPG | 4 | 85 | 3 | – | 7 | 3.5 | 100 | 9 | 90% | 5.0 | 80% | 100 | 3 | – | 4 | SH. Tank |
| SH. Tank Destroyer | SH. TD | 4 | 12 | 70 | – | 7 | 1.8 | 145 | 170 | 99% | 5.0 | 80% | 100 | 3 | – | 4 | SH. Tank |
| SH. SP Anti-Air | SH. AA | 4 | 11.5 | 9 | 50 | 3.5 | 3.5 | 100 | 98 | 90% | 2.5 | 80% | 100 | 3 | – | 4 | SH. Tank |
| Modern Tank | Mod. Tank | 10 | 40 | 32 | – | 10 | 84 | 130 | 131 | 98% | 5.0 | 80% | 28 | 3 | – | 4 | – |
| Modern SP Artillery | Modern SPG | 10 | 80 | 3 | – | 8 | 4 | 90 | 10 | 85% | 2.5 | 80% | 28 | 3 | – | 4 | Mod. Tank |
| Modern Tank Destroyer | Modern TD | 10 | 10 | 42 | – | 8 | 2 | 130 | 165 | 98% | 2.5 | 80% | 28 | 3 | – | 4 | Mod. Tank |
| Modern SP Anti-Air | Modern AA | 10 | 9 | 7.5 | 50 | 4 | 4 | 90 | 100 | 85% | 1.25 | 80% | 28 | 3 | – | 4 | Mod. Tank |
| Amphibious Tank | Amphibious Tank 1 | 7 | 13 | 4 | – | 4 | 26 | 20 | 10 | 80% | 4 | 80% | 10 | 2 | – | – | L. Tank II |
| Amphibious Tank | Amphibious Tank 2 | 8 | 19 | 14 | – | 5 | 36 | 80 | 61 | 90% | 4 | 80% | 13 | 2 | 2 | – | M. Tank I |

No armour equipment in the table uses aluminium or rubber.

## Equipment statistic definitions

**Army values** — Recovery Rate (hourly organisation regained out of combat); Defense (attacks avoided while defending); Breakthrough (attacks avoided while attacking); Hardness (share of the division that is armoured — reduces soft attacks taken and increases hard attacks taken); Soft attack (vs. low-hardness targets); Hard attack (vs. high-hardness targets); Reconnaissance (better tactic selection); Entrenchment; Initiative (faster reinforcement and planning); Trickleback (share of combat losses returned to the manpower pool); Supply use and Supply Usage modifier; Suppression and Suppression Bonus; Exp. Loss (experience lost when replacing casualties); Eq. Capture Ratio; Fuel Capacity.

**Navy values** — Surface detection; Sub detection; Surface Visibility; Sub Visibility; Light Attack and Light Piercing; Heavy Attack and Heavy Piercing; Torpedo attack; Depth charges; Anti-air; Max Speed; Max Range (distance from the nearest friendly naval base); Minelaying; Minesweeping.

**Air values** — Range; Air Defense (hits a plane survives); Air Attack; Agility; Strategic Bombing; Air Superiority; Naval Attack; Naval Targeting; Ground Attack.

**Common values** — Organization; HP (strength); Max Speed; Armor (higher than enemy piercing reduces damage taken and grants more attacks); Piercing (equal or greater than target armour does more damage); Reliability (lower = more breakdowns and accidents; support companies can add a reliability bonus); Weight (transports needed for shipping and invasions); Fuel Usage.

**Special values** — Deck size (planes a carrier holds); Hot/Cold acclimatization gain factor; Production Cost (factory output needed per unit).

See also: [Research and technology](research-and-technology.md), [Construction and buildings](construction-and-buildings.md), [Trade, resources and the international market](trade-resources-and-market.md), [Military industrial organizations](military-industrial-organizations.md).
