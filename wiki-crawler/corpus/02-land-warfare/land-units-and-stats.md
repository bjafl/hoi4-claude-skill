---
title: Land Units and Stats
category: land-warfare
tags: [land units, battalions, support companies, stats, combat width, organization, armor, piercing, hardness, equipment, railway artillery]
game_version: "1.19"
dlc: [No Step Back, Arms Against Tyranny, By Blood Alone, Waking the Tiger, Together for Victory]
sources:
  - https://hoi4.paradoxwikis.com/Land_units
  - https://hoi4.paradoxwikis.com/Land_units_by_unit
  - https://hoi4.paradoxwikis.com/Land_units_by_year
  - https://hoi4.paradoxwikis.com/Unit
---

## Summary

This file is the numeric reference for every land battalion and support company: what each contributes to a division, what equipment it consumes, and its full stat line at every technology generation. Two views are provided — a **per-battalion base-stat view** (the fixed contribution of the subunit, using first-generation equipment) and a **per-unit-per-year view** (the complete stat line at each tech level). Stats here exclude doctrine technologies, which have no year associated and are largely mutually exclusive.

> ⚠️ Stats for armored vehicles (tanks, tank destroyers, SP artillery, SP anti-air) shown here are the **without No Step Back** values, where armored equipment has predetermined stats and is varianted with army experience. **With No Step Back, armored vehicles get their stats from the tank designer instead**, so the tables below become baselines rather than actual values.

> ⚠️ The wiki flags the per-battalion "Unit types" tables as not fully accurate: they are built from first-generation equipment. Non-combat statistics are defined per battalion and are static; combat statistics are a function of the equipment fielded, then modified by the battalion.

## How subunit stats become division stats

| Combination rule | Stats |
|---|---|
| **Sum** of all battalions and companies | HP, soft attack, hard attack, air attack, defence, breakthrough, recon, suppression, weight, supply use, trickleback, experience-loss, initiative, entrenchment, fuel capacity, fuel usage, manpower, equipment need |
| **Sum** of combat battalions only | Combat width |
| **Average** of all battalions and companies | Organization, recovery rate |
| **Average of line battalions only** | Hardness |
| **Slowest** battalion (support companies that "affect speed" included) | Maximum speed |
| **40% highest + 60% average** | Armor, piercing |
| **Average of combat battalions + sum of support companies** | Terrain modifiers / adjusters |
| **Longest** of any battalion or company | Training time |
| Tracked per equipment type | Reliability |

If a battalion uses several equipment types, its stats are the **sum over all equipment used**. Battalions then apply their own **equipment modifier** on top (e.g. Marines add +30% breakthrough to their infantry equipment; support artillery applies −40% soft/hard/defence/breakthrough to its artillery equipment). **Support Equipment adds nothing to combat stats.**

## Stat glossary

| Stat | Meaning |
|---|---|
| **Maximum speed** | The division moves at its **slowest** battalion's speed. Recon and some other support companies count. |
| **HP (Strength)** | Damage the division can absorb before physical destruction. Combat stats scale proportionally to current HP — at 50% HP a division makes only 50% of its attacks/defences. Infantry and especially Mechanized are the HP sources; tanks and combat-support battalions are fragile. |
| **Organization** | Readiness to fight. At 0 org a division cannot fight. Moving costs **−0.2 org per hour**; org loss also slows movement by up to **−80%**. At 0 org an **attacker** stops attacking and returns to its origin province, losing all movement progress, and cannot attack again until org recovers appreciably; a **defender** flees to the nearest friendly province, and is **destroyed** if it cannot leave. |
| **Recovery rate** | Additional org regeneration on top of the fixed out-of-combat rate. Penalised by lack of supply. |
| **Recon** | Reconnaissance in battle. The side with the recon advantage (divisions + general) is more likely to pick better combat tactics each day. |
| **Suppression** | Ability to suppress resistance during occupation. Summed, but because occupation does not use deployed divisions it behaves in practice like a division average weighted by production cost and manpower. |
| **Weight** | Convoys needed for naval transfer and transport planes needed for paradrop. |
| **Supply use** | Daily supply consumption. Reduced by the Logistics Company. |
| **Reliability** | Resistance to equipment breakdown. Higher reliability = less attrition loss and better equipment recovery in combat. Tracked per equipment type; the Maintenance Company adds a bonus to each. |
| **Trickleback** | Share of combat manpower losses returned to the manpower pool. Mainly the Field Hospital. |
| **Exp. loss** | Experience lost when taking casualties (a larger negative is better). Reduced by the Field Hospital. Extra XP is also lost bringing in reinforcements. |
| **Soft attack** | Attacks per hour against low-hardness targets. |
| **Hard attack** | Attacks per hour against high-hardness (armoured) targets. |
| **Air attack** | Damage against enemy aircraft; reduces the effectiveness of enemy air attacking the division and helps counter air superiority effects. |
| **Defence** | Number of incoming attacks the division can avoid while **defending** a province. |
| **Breakthrough** | Same as defence, but while **attacking**. |
| **Armour** | If the attacker's piercing is below the defender's armour, the attacker makes **up to −50% fewer** soft and hard attacks (the full −50% at under 50% piercing). Having more armour than the enemy's piercing also **increases your own number of attacks** and changes the org-damage die per attack from **1d4 to 1d6**. Armour is a property of equipment, not unit type. |
| **Piercing** | If piercing ≥ enemy armour: no damage penalty and no extra org damage taken. Otherwise: **−20% damage at ≥75% piercing**, **−35% at ≥50%**, **−50% below that**. |
| **Initiative** | Speeds up planning (20% initiative turns 2%/day planning into 2.4%/day) and raises reinforce chance: **each 1% initiative = +0.25% reinforce rate**. |
| **Entrenchment** | Temporary defensive works. Built up daily while stationary and out of combat; **lost entirely when attacking**, except with the probing-attack ability. Affects both attack and defence. |
| **Combat width** | Frontage occupied. Infantry and armoured battalions **2**, artillery battalions **3**, anti-tank and anti-air battalions **1**. Support companies add **0**. Mass Assault land doctrine reduces Infantry battalion width; the Mountaineer special forces doctrine tree (**Arms Against Tyranny**) reduces Mountaineer width. |
| **Hardness** | Share of the division that is protected. Incoming attacks split: `hard attacks × hardness` and `soft attacks × (1 − hardness)`. Infantry 0%, Motorized 20%, Mechanized 60–75%, Medium tanks 90%, Super-heavy tanks 100%. |
| **Fuel capacity** | Most fuel-using units add **96 hours** of their own fuel usage to division capacity. |
| **Fuel usage** | Consumed while moving, in combat, or training. Refuelling requires sufficient supply in the province. Logistics companies lower it. Some support companies require fuel-using equipment but add no fuel usage. |
| **Paradrop** | Boolean: true only if **all line battalions are Paratroopers**. Most support companies can be mixed in freely; some heavy ones cannot paradrop. |
| **Special Forces Cap** | Special forces battalions a country may field are capped relative to its deployed non-special-forces battalions. Divisions cannot be trained, retemplated or edited if that would exceed the cap. |
| **Equipment cost** | Manpower, equipment and training time are summed, except **training time**, which is the **longest** of any battalion or company. |
| **Terrain modifiers** | Averaged across battalions; **additive** for support companies. |

## Battalion base stats (first-generation equipment)

Columns: HP / Org / Recov = recovery / Supp = suppression / Wt = weight / Sup = supply use / W = combat width / MP = manpower / Trn = training days / Equip = equipment required / Mod = the battalion's equipment modifier / then equipment-derived combat stats / Hard% = hardness / FuelCap / FuelUse / Cost = production cost.

### Infantry battalions

| Unit | HP | Org | Recov | Supp | Wt | Sup | W | MP | Trn | Equipment | Mod | Speed | Soft | Hard | Air | Def | Break | Armour | Pierce | Hard% | FuelCap | FuelUse | Cost | Special |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Infantry | +25.0 | 60 | 0.3 | +1.5 | +0.5 | +0.06 | +2.0 | 1000 | 90 | 100 Infantry Equipment | — | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0% | 0 | 0 | +43.0 | — |
| Bicycle | +25.0 | 60 | 0.3 | +2.0 | +0.5 | +0.06 | +2.0 | 1000 | 90 | 100 Infantry Equipment, 10 Support Equipment | +60% Max Speed | 6.4 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0% | 0 | 0 | +83.0 | Altered movement in some terrain |
| Penal Battalion | +15.0 | 70 | 0.4 | +0.5 | +0.5 | +0.05 | +2.0 | 850 | 50 | 85 Infantry Equipment | — | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0% | 0 | 0 | +36.55 | — |
| Irregular Infantry | +30.0 | 45 | 0.2 | +1.5 | +0.5 | +0.04 | +2.0 | 1000 | 30 | 80 Infantry Equipment | −5% Soft attack, −15% Defence | 4.0 | +2.85 | +0.5 | — | +17.0 | +2.0 | — | 1 | 0% | 0 | 0 | +34.4 | — |
| Militia | +25.0 | 50 | 0.3 | +1.5 | +0.5 | +0.06 | +2.0 | 1000 | 80 | 100 Infantry Equipment | — | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0% | 0 | 0 | +43.0 | — |
| Mountaineers | +20.0 | 70 | 0.4 | +1.0 | +0.5 | +0.05 | +2.0 | 1000 | 120 | 140 Infantry Equipment | +30% Breakthrough | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.6 | — | 1 | 0% | 0 | 0 | +60.2 | Various rugged terrain bonuses; special forces |
| Marines | +20.0 | 70 | 0.4 | +1.0 | +0.5 | +0.05 | +2.0 | 1000 | 120 | 150 Infantry Equipment | +30% Breakthrough | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.6 | — | 1 | 0% | 0 | 0 | +64.5 | Various wet terrain bonuses; special forces |
| Marine Commandos | +20.0 | 70 | 0.4 | +1.0 | +0.5 | +0.05 | +2.0 | 1000 | 120 | 150 Infantry Equipment | +30% Breakthrough | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.6 | — | 1 | 0% | 0 | 0 | +64.5 | Various wet terrain bonuses; special forces |
| Paratrooper | +22.0 | 70 | 0.4 | +1.0 | +0.5 | +0.05 | +2.0 | 1000 | 150 | 130 Infantry Equipment | — | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0% | 0 | 0 | +55.9 | Can be paradropped; special forces |
| Rangers | +20.0 | 70 | 0.4 | +1.0 | +0.5 | +0.05 | +2.0 | 1000 | 120 | 140 Infantry Equipment | — | 4.0 | +3.0 | +0.5 | — | +20.0 | +2.6 | — | 1 | 0% | 0 | 0 | +60.2 | Various dense-foliage terrain bonuses; special forces |

Categories: all of the above are `front line, foot infantry, all infantry, all army`. Mountaineers add `special forces, all mountaineers, special forces leg infantry`; Marines and Marine Commandos add `special forces, all marines, special forces leg infantry`; Paratroopers add `special forces, all paratroopers, special forces leg infantry`; Rangers add `special forces, all rangers, special forces leg infantry`; Militia adds `militia`.

### Mobile battalions

| Unit | HP | Org | Recov | Supp | Wt | Sup | W | MP | Trn | Equipment | Mod | Speed | Soft | Hard | Air | Def | Break | Armour | Pierce | Hard% | FuelCap | FuelUse | Cost | Special |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cavalry | +25.0 | 70 | 0.3 | +2.0 | +0.5 | +0.06 | +2.0 | 1000 | 120 | 120 Infantry Equipment | +60% Max Speed | 6.4 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0% | 0 | 0 | +51.6 | Various terrain attack penalties |
| Camelry | +30.0 | 70 | 0.3 | +2.0 | +0.6 | +0.10 | +2.0 | 1000 | 160 | 150 Infantry Equipment | +40% Max Speed | 5.6 | +6.0 | +1.0 | — | +22.0 | +3.0 | — | 4 | 0% | 0 | 0 | +64.5 | Terrain attack penalties; desert bonuses |
| Elephantry | +30.0 | 55 | 0.25 | +2.3 | +1.2 | +0.12 | +2.0 | 1100 | 210 | 260 Infantry Equipment, 30 Artillery | +50% Max Speed, −25% Soft, −15% Hard, +30% Breakthrough | 6 | +23.2 | +2.5 | — | +32.0 | +11.7 | — | 9 | 0% | 0 | 0 | +235.0 | Various terrain modifiers |
| Motorized Infantry | +25.0 | 60 | 0.3 | +2.2 | +0.75 | +0.065 | +2.0 | 1200 | 90 | 100 Infantry Equipment, 35 Motorized (Trucks) | — | 12.0 | +3.0 | +0.5 | — | +20.0 | +7.0 | — | 1 | 10% | 57.6 | 1.20 | +130.5 | Various terrain penalties |
| Mechanized Infantry | +30.0 | 60 | 0.3 | +2.0 | +1.0 | +0.14 | +2.0 | 1200 | 120 | 100 Infantry Equipment, 40 Mechanized | +10% Soft, +400% Hard | 8.0 | +3.3 | +2.5 | — | +46.0 | +8.0 | 10 | 12 | 60% | 115.2 | 2.40 | +363.0 | Various terrain penalties |
| Amtrac Battalion | +30.0 | 60 | 0.3 | +1.0 | +1.0 | +0.18 | +2.0 | 1200 | 120 | 100 Infantry Equipment, 50 Amtrac | +10% Soft, +50% Hard | 7.0 | +3.3 | +0.75 | — | +46.0 | +6.0 | 10 | 12 | 60% | 192.0 | 4.0 | +450.0 | Terrain penalties; wet terrain bonuses |
| Armored Car | +5.0 | 20 | 0.3 | +2.5 | +0.8 | +0.14 | +2.0 | 500 | 180 | 60 Armored Cars | — | 9.0 | +6.0 | +2.0 | — | +2.0 | +12.0 | 3 | 6 | 65% | 38.40 | 0.8 | +210.0 | Terrain penalties and movement bonuses |

> ⚠️ The `Land units` intro text states Mechanized battalions get **+500%** bonus to Weapon Hard Attack, while the Mobile Battalions table states **+400%**. The table value is used above.

### Combat support battalions (line artillery / AT / AA, foot)

| Unit | HP | Org | Recov | Wt | Sup | W | MP | Trn | Equipment | Speed | Soft | Hard | Air | Def | Break | Pierce | Hard% | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anti-Tank | +0.6 | 0 | — | +0.5 | +0.10 | +1.0 | 500 | 120 | 36 Anti-Tank | 4.0 | +4.0 | +20.0 | — | +4.0 | — | 60.0 | 0% | +144.0 |
| Anti-Air | +0.6 | 0 | 0.1 | +0.5 | +0.10 | +1.0 | 500 | 120 | 36 Anti-Air | 4.0 | +3.0 | +7.0 | +19.0 | +4.0 | +1.0 | 25 | 0% | +144.0 |
| Artillery | +0.6 | 0 | 0.1 | +0.5 | +0.21 | +3.0 | 500 | 120 | 24 Artillery | 4.0 | +25.0 | +2.0 | — | +10.0 | +6.0 | 5 | 0% | +84.0 |
| Rocket Artillery | +0.6 | 0 | 0.1 | +0.5 | +0.22 | +3.0 | 500 | 120 | 24 Rocket Artillery | 4.0 | +30.0 | +1.0 | — | +12.0 | +9.0 | 2 | 0% | +96.0 |

All have "various terrain penalties" and fuel capacity/usage 0. Categories: `line artillery, all army` (Anti-Tank and Artillery also `front line` / `artillery`).

### Mobile combat support battalions (motorized artillery / AT / AA)

| Unit | HP | Org | Recov | Wt | Sup | W | MP | Trn | Equipment | Speed | Soft | Hard | Air | Def | Break | Pierce | Hard% | FuelCap | FuelUse | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Motorized Anti-Tank | +0.6 | 0 | — | +0.5 | +0.15 | +1.0 | 500 | 120 | 36 Anti-Tank, 36 Motorized | 12.0 | +4.0 | +20.0 | — | +4.0 | +5.0 | 60.0 | 20% | 57.6 | 1.20 | +234.0 |
| Motorized Anti-Air | +0.6 | 0 | 0.1 | +0.5 | +0.15 | +1.0 | 500 | 120 | 36 Anti-Air, 36 Motorized | 12.0 | +3.0 | +7.0 | +19.0 | +4.0 | +6.0 | 25 | 10% | 57.6 | 1.20 | +234.0 |
| Motorized Artillery | +0.6 | 0 | 0.1 | +0.5 | +0.25 | +3.0 | 500 | 120 | 24 Artillery, 36 Motorized | 12.0 | +25.0 | +2.0 | — | +10.0 | +11.0 | 5 | 10% | 57.6 | 1.20 | +174.0 |
| Truck-drawn Rocket Artillery | +0.6 | 0 | 0.1 | +0.5 | +0.25 | +3.0 | 500 | 120 | 24 Rocket Artillery, 36 Motorized | 12.0 | +30.0 | +1.0 | — | +12.0 | +14.0 | 2 | 10% | 57.6 | 1.2 | +186.0 |
| Motorized Rocket Artillery | +0.6 | 0 | 0.1 | +0.5 | +0.25 | +3.0 | 500 | 120 | 16 Mot. Rocket Artillery, 16 Motorized | 12.0 | +36.0 | +1.0 | — | +15.0 | +17.0 | 2 | 10% | 115.2 | 2.40 | +232 |

Motorized Rocket Artillery is a **distinct unit** from Truck-drawn Rocket Artillery (its icon resembles a Katyusha).

### Armored battalions

Speed entries of the form `a/b/c` are the successive tech generations of that chassis.

| Unit | HP | Org | Recov | Supp | Wt | Sup | W | MP | Trn | Equipment | Mod | Speed | Soft | Hard | Def | Break | Armour | Pierce | Hard% | FuelCap | FuelUse | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light Tank | +2.0 | 10 | 0.3 | 2.5 | +1.0 | +0.22 | +2.0 | 500 | 180 | 60 Light Tanks | +15% Breakthrough | 10/12/14 | +13 | +4 | +4 | +29.9 | 10 | 10 | 80% | 115.2 | 2.4 | +480 |
| Medium Tank | +2.0 | 10 | 0.3 | 2.5 | +1.25 | +0.25 | +2.0 | 500 | 180 | 50 Medium Tanks | +15% Breakthrough | 8/9/10 | +19 | +14 | +5 | +41.4 | 60 | 61 | 90% | 172.8 | 3.6 | +600 |
| Heavy Tank | +2.0 | 10 | 0.3 | 2.5 | +1.5 | +0.32 | +2.0 | 500 | 180 | 40 Heavy Tanks | +15% Breakthrough | 5/6/6 | +15 | +12 | +6 | +41.4 | 70 | 35 | 95% | 211.2 | 4.4 | +1000 |
| Modern Tank | +2.0 | 10 | 0.3 | 2.5 | +1.5 | +0.25 | +2.0 | 500 | 180 | 50 Modern Tanks | +15% Breakthrough | 10 | +40 | +32 | +10 | +96.6 | 130 | 131 | 98% | 240 | 5 | +1400 |
| Amphibious Tank Battalion | +2.0 | 10 | 0.3 | — | +1.0 | +0.20 | +2.0 | 500 | 180 | 50 Amphibious Tanks | — | 7 | +13 | +4 | +4 | +26 | 20 | 10 | 80% | 192 | 4 | +500 |
| Light Amphibious Tank Battalion | +2.0 | 10 | 0.3 | — | +1.0 | +0.20 | +2.0 | 500 | 180 | 50 Light Amphibious Tanks | — | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer |
| Medium Amphibious Tank Battalion | +2.0 | 10 | 0.3 | — | +1.0 | +0.20 | +2.0 | 500 | 180 | 50 Medium Amphibious Tanks | — | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer |
| Heavy Amphibious Tank Battalion | +2.0 | 10 | 0.3 | — | +1.0 | +0.20 | +2.0 | 500 | 180 | 50 Heavy Amphibious Tanks | — | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer | Tank designer |

The Light / Medium / Heavy Amphibious Tank Battalions are **unavailable without No Step Back**, and with NSB their combat stats come from the tank designer.

### Armored combat support battalions (tank destroyers, SP artillery, SP AA)

| Unit | HP | Org | Recov | Supp | Wt | Sup | W | MP | Trn | Equipment | Mod | Speed | Soft | Hard | Air | Def | Break | Armour | Pierce | Hard% | FuelCap | FuelUse | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light Tank Destroyer | +0.6 | 0 | 0.3 | 1.0 | +1.0 | +0.20 | +2.0 | 500 | 180 | 40 Light Tank Destroyer | −42% Breakthrough, +15% Piercing | 10/12/14 | +6.0 | +10.0 | — | +4.0 | +0.5 | 10 | 57.5 | 80% | 57.6 | 1.20 | +320.0 |
| Medium Tank Destroyer | +0.6 | 0 | 0.3 | 1.25 | +1.25 | +0.22 | +2.0 | 500 | 180 | 40 Medium Tank Destroyer | −25% Breakthrough, +15% Piercing | 8/9/10 | +5.0 | +20.0 | — | +5.0 | +0.9 | 60 | 101.2 | 90% | 86.4 | 1.80 | +480.0 |
| Heavy Tank Destroyer | +0.6 | 0 | 0.3 | 1.25 | +1.5 | +0.30 | +2.0 | 500 | 180 | 40 Heavy Tank Destroyer | −25% Breakthrough, +15% Piercing | 5/6/6 | +6.0 | +25.0 | — | +4.0 | +0.7 | 70 | 110.4 | 95% | 105.6 | 2.20 | +1000.0 |
| Modern Tank Destroyer | +0.6 | 0 | 0.3 | 1.25 | +1.5 | +0.25 | +2.0 | 500 | 180 | 40 Modern Tank Destroyer | −25% Breakthrough, +15% Piercing | 10 | +10.0 | +42.0 | — | +8.0 | +1.5 | 130 | 189.7 | 98% | 120.00 | 2.50 | +1120.0 |
| Light SP Artillery | +0.6 | 0 | 0.1 | 1.25 | +1.0 | +0.42 | +2.0 | 500 | 180 | 40 Light SP Artillery | −42% Breakthrough, +15% Soft | 10/12/14 | +39.1 | +0.5 | — | +4.0 | +1.1 | 5 | 4 | 50% | 57.6 | 1.20 | +320.0 |
| Medium SP Artillery | +0.6 | 0 | 0.1 | 1.5 | +1.25 | +0.46 | +2.0 | 500 | 180 | 40 Medium SP Artillery | −25% Breakthrough, +15% Soft | 8/9/10 | +48.3 | +1.0 | — | +5.0 | +2.2 | 45 | 5 | 65% | 86.4 | 1.80 | +480.0 |
| Heavy SP Artillery | +0.6 | 0 | 0.1 | 1.5 | +1.5 | +0.60 | +2.0 | 500 | 180 | 40 Heavy SP Artillery | −25% Breakthrough, +15% Soft | 5/6/6 | +63.2 | +1.0 | — | +4.0 | +1.5 | 45 | 8 | 80% | 105.5 | 2.20 | +1000.0 |
| Modern SP Artillery | +0.6 | 0 | 0.1 | 1.5 | +1.5 | +0.50 | +2.0 | 500 | 180 | 40 Modern SP Artillery | −25% Breakthrough, +15% Soft | 10 | +92.0 | +3.0 | — | +8.0 | +3.0 | 90 | 10 | 85% | 120.00 | 2.50 | +1120.0 |
| Light SP Anti-Air | +0.6 | 0 | 0.1 | 0.75 | +1.0 | +0.10 | +2.0 | 500 | 180 | 40 Light SP Anti-Air | −55% Breakthrough, +15% Air | 10/12/14 | +2.0 | +1.0 | +17.2 | +2.0 | +0.9 | 5 | 5 | 50% | 28.8 | 0.60 | +400.0 |
| Medium SP Anti-Air | +0.6 | 0 | 0.1 | 0.8 | +1.25 | +0.10 | +2.0 | 500 | 180 | 40 Medium SP Anti-Air | −53% Breakthrough, +15% Air | 8/9/10 | +4.5 | +3.0 | +25.3 | +2.5 | +1.1 | 45 | 40 | 65% | 43.2 | 0.90 | +480.0 |
| Heavy SP Anti-Air | +0.6 | 0 | 0.1 | 0.75 | +1.5 | +0.10 | +2.0 | 500 | 180 | 40 Heavy SP Anti-Air | −35% Breakthrough, +15% Air | 5/6/6 | +4.5 | +4.0 | +19.5 | +2.0 | +1.3 | 45 | 25 | 80% | 52.8 | 1.10 | +1000.0 |
| Modern SP Anti-Air | +0.6 | 0 | 0.1 | 2.0 | +1.5 | +0.10 | +2.0 | 500 | 180 | 40 Modern SP Anti-Air | −53% Breakthrough, +15% Air | 10 | +9.0 | +7.5 | +57.5 | +4.0 | +1.8 | 90 | 100 | 85% | 60.00 | 1.25 | +1120.0 |

> ⚠️ Combat-width conflict: the `Land units` unit-type table lists **+2.0** width for every armored combat support battalion, while `Land units by unit` lists **3** for SP Artillery and **1** for SP Anti-Air. Treat the by-unit values as the likelier current ones and verify in game.

## Support companies

Support companies have **no combat width**, do **not** affect division speed and **can** be paradropped, unless the Special column says otherwise. Each can be taken only once per division, and several **block** other support companies.

| Unit | HP | Org | Recov | Wt | Sup | MP | Trn | Equipment | Equipment modifier | Speed | Soft | Hard | Air | Def | Break | Armour | Pierce | FuelCap | FuelUse | Cost | Special effects |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Support Anti-Tank | +0.2 | 0 | −0.1 | +0.1 | +0.08 | 300 | 120 | 24 Anti-Tank | −50% Soft/Hard/Defence/Breakthrough, −15% Piercing | — | +2.0 | +10.0 | — | +2.0 | — | — | 51.0 | 0 | 0 | +96.0 | — |
| Support Anti-Air | +0.2 | 0 | −0.1 | +0.1 | +0.10 | 300 | 120 | 20 Anti-Air | −40% Soft/Hard/Defence/Breakthrough, −20% Air Attack | — | +1.8 | +4.2 | +15.2 | +2.4 | +0.6 | — | 25 | 0 | 0 | +80.0 | — |
| Support Artillery | +0.2 | 0 | 0.1 | +0.1 | +0.16 | 300 | 120 | 12 Artillery | −40% Soft/Hard/Defence/Breakthrough | — | +15.0 | +1.2 | — | +6.0 | +3.6 | — | 5 | 0 | 0 | +42.0 | — |
| Support Rocket Artillery | +0.2 | 0 | 0.1 | +0.1 | +0.16 | 300 | 120 | 12 Rocket Artillery | −50% Soft/Hard/Defence/Breakthrough | — | +15.0 | +0.5 | — | +6.0 | +4.5 | — | 2 | 0 | 0 | +48.0 | — |
| Super-Heavy Artillery | +0.2 | 0 | 0.1 | +0.1 | +0.25 | 1000 | 180 | 3 Super-Heavy Howitzer | — | 4.0 | +35.0 | +4.0 | — | +12.0 | +12.0 | — | 7 | 12 | 0.25 | +135.0 | Cannot paradrop; **speed affects division** |
| Self-Propelled Super-Heavy Artillery | +0.2 | 0 | 0.1 | +0.1 | +0.35 | 1000 | 180 | 3 Self-Propelled Super-Heavy Howitzer | — | — | +44.0 | +6.0 | — | +14.0 | +14.0 | 6 | 9 | 86.4 | 1.8 | +195.0 | Cannot paradrop; **speed affects division** |
| Cavalry Recon Company | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 500 | 120 | 40 Infantry Equipment, 10 Support Equipment | −90% Soft & Hard, −50% Defence & Breakthrough, +60% Max Speed | 6.4 | +0.3 | +0.05 | — | +10.0 | +1.0 | — | 1 | 0 | 0 | +57.2 | **+1 Recon**; speed affects division; terrain movement bonuses; blocks other recon; **+10% All Artillery Soft Attack** |
| Recon Rangers | +2.0 | 30 | 0.3 | +0.1 | +0.06 | 500 | 120 | 40 Infantry Equipment, 15 Support Equipment | +60% Max Speed | 6.4 | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0 | 0 | +77.2 | **+1 Recon**; speed affects division; terrain movement & attack bonuses; blocks other recon |
| Long Range Patrol Company | +10 | 60 | 0.3 | +0.3 | +0.04 | 500 | 120 | 40 Infantry Equipment, 10 Support Equipment | +10% Soft, +30% Breakthrough, +60% Max Speed | 6.4 | +3.3 | +0.5 | — | +20.0 | +2.6 | — | 1 | 0 | 0 | +57.2 | **+2 Recon**; +5% Equipment Capture Ratio; speed affects division; terrain movement & attack bonuses; snow bonuses; blocks other recon; **+2% Leg Infantry Initiative** |
| Motorized Recon Company | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 500 | 120 | 40 Infantry Equipment, 10 Support Equipment, 20 Motorized | −90% Soft & Hard, −9% Defence, −50% Breakthrough | 12.0 | +0.3 | +0.05 | — | +20.0 | +3.5 | — | 1 | 57.6 | 1.2 | +107.2 | **+1.5 Recon**; speed affects division; terrain movement bonuses; blocks other recon; **+10% All Artillery Soft Attack** |
| Armoured Car Recon Company | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 500 | 120 | 24 Armoured Cars | −50% Soft & Hard & Defence, −20% Breakthrough | 9.0 | +3.0 | +1.0 | — | +1.0 | +9.6 | 3 | 6 | 38.40 | 0.8 | +96.0 | **+2 Recon**; speed affects division; terrain movement bonuses; blocks other recon; **+10% All Artillery Soft Attack** |
| Light Tank Recon Company | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 500 | 120 | 24 Light Tanks | −60% Soft/Hard/Defence/Breakthrough/Armor | — | +1.3 | +0.4 | — | +2.0 | +13.0 | 10 | 10 | 92 | 2.4 | +192 | **+1 Recon**; speed affects division; terrain movement bonuses; **cannot paradrop**; blocks other recon; **+10% Tanks & Armor Variants Hard Attack** |
| Airborne Light Armour | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 500 | 120 | 24 Light Tanks | −50% Defence & Armor, −25% Soft/Hard/Breakthrough | — | +6.0 | +3.0 | — | +2.0 | +13.5 | 2.5 | 15 | 92 | 1.0 | +168 | **+1 Recon**; speed affects division; terrain movement bonuses; blocks other recon |
| Helicopter Recon | +2.0 | 20 | 0.3 | +0.1 | +0.07 | 500 | 120 | 20 Infantry Equipment, 10 Support Equipment, 20 Helicopter | — | — | +3.0 | +0.5 | — | +26 | +10 | 4 | 11 | 86.4 | 1.8 | +228.6 | **+2 Recon**; terrain movement bonuses; **cannot paradrop**; blocks other recon and Helicopter Brigade; **+10% All Artillery Soft Attack** |
| Helicopter Brigade | +2.0 | 20 | 0.3 | +0.1 | +0.07 | 500 | 120 | 15 Support Equipment, 15 Helicopter | −100% Fuel Use | 10.0 | — | — | — | +6 | +8 | 4 | 11 | 0 | 0 | +195.0 | **+1 Recon**; +10% Manpower trickleback; −5% Experience loss from casualties; −5% Supply Consumption; cannot paradrop; blocks other helicopter companies; **+3% All Infantry HP** |
| Engineer Company | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 300 | 120 | 10 Infantry Equipment, 30 Support Equipment | −50% Soft, +10% Defence, +50% Breakthrough | — | +1.5 | +0.5 | — | +22.0 | +3.0 | — | 1 | 0 | 0 | +124.0 | **+2 Max Entrenchment**; various terrain bonuses; blocks other engineers; **+0.2 Leg Infantry Max Entrenchment** |
| Armored Engineer Company | +2.0 | 20 | 0.3 | +0.1 | +0.035 | 300 | 120 | 30 Armored Support Equipment, 15 Support Equipment | −50% Soft, +15% Defence, +100% Breakthrough | — | +3.0 | +2.0 | — | +11.5 | +6.0 | 12.0 | 5.0 | 86.4 | 1.8 | +485.0 | **+3 Max Entrenchment**; terrain bonuses; cannot paradrop; blocks other engineers; **+0.05 Tanks & Armor Variants Breakthrough**; **+0.2 All Infantry Max Entrenchment** |
| Assault Engineer Company | +2.0 | 20 | 0.3 | +0.1 | +0.025 | 300 | 120 | 20 Armored Support Equipment, 20 Support Equipment | −50% Soft, +10% Defence, +150% Breakthrough | — | +3.0 | +2.0 | — | +11.0 | +7.5 | 12.0 | 5.0 | 86.4 | 1.8 | +385.0 | **+2 Max Entrenchment**; terrain bonuses; cannot paradrop; blocks other engineers; **+10% Leg Infantry Breakthrough** |
| Pioneers | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 300 | 120 | 10 Infantry Equipment, 40 Support Equipment | +10% Defence, +50% Breakthrough, −50% Soft | — | +1.5 | +0.5 | — | +22.0 | +3.0 | — | 1 | 0 | 0 | +164.3 | **+2.5 Max Entrenchment**; wet terrain bonuses; blocks other engineers; **+15% All Marines Breakthrough** |
| Jungle Pioneers | +1.0 | 30 | 0.3 | +0.1 | +0.1 | 500 | 120 | 10 Infantry Equipment, 40 Support Equipment | +30% Breakthrough, +5% Defence | — | +3.0 | +0.5 | — | +21.0 | +2.6 | — | 1 | 0 | 0 | +164.3 | **+2 Max Entrenchment**; **+300% Hot acclimatization gain rate**; terrain bonuses; blocks other engineers |
| Field Hospital | +2.0 | 20 | 0.3 | +0.1 | +0.05 | 500 | 120 | 20 Motorized, 30 Support Equipment | −100% Fuel Use | — | — | — | — | — | +5.0 | — | — | 0 | 0 | +170.0 | **+20% Manpower trickleback**; **−15% Experience loss from casualties**; blocks Helicopter Med-Evac; **+10% All Infantry HP** |
| Helicopter Med-Evac | +2.0 | 20 | 0.3 | +0.1 | +0.07 | 500 | 120 | 15 Motorized, 30 Support Equipment, 15 Helicopter | — | — | — | — | — | +6.0 | +13.0 | 4 | 11 | 144.0 | 3.0 | +292.5 | **+25% Manpower trickleback**; −10% Experience loss from casualties; blocks Field Hospital and Helicopter Brigade; +5% All Infantry HP; +10% All Infantry Recovery Rate |
| Logistics Company | +1.0 | 10 | 0.3 | +0.1 | — | 500 | 120 | 10 Motorized, 20 Support Equipment | −100% Fuel Use | — | — | — | — | — | +5.0 | — | — | 0 | 0 | +105.0 | **−10% Supply Consumption**; **−5% Fuel Consumption**; blocks Helicopter Transports |
| Helicopter Transports | +1.0 | 12 | 0.3 | +0.1 | — | 500 | 120 | 10 Motorized, 20 Support Equipment, 10 Helicopter | −100% Fuel Use | — | — | — | — | +6.0 | +13.0 | 4 | 11 | 0 | 0 | +195.0 | **−10% Supply Consumption**; terrain movement bonuses; blocks Logistics Company and Helicopter Brigade |
| Maintenance Company | +1.0 | 20 | 0.3 | +0.1 | +0.03 | 500 | 120 | 25 Support Equipment | — | — | — | — | — | — | — | — | — | 0 | 0 | +100.0 | **+5% Reliability**; **+5% Equipment Capture Ratio**; blocks Armored Maintenance Company |
| Armored Maintenance Company | +1.0 | 20 | 0.3 | +0.1 | +0.035 | 500 | 120 | 20 Armored Support Equipment, 15 Support Equipment | — | — | +6.0 | +2.0 | — | +10.0 | +3.0 | 12.0 | 5.0 | 86.4 | 1.8 | +365.0 | **+2% Reliability**; **+10% Equipment Capture Ratio**; **+10% Equipment Recovery**; cannot paradrop; blocks Maintenance Company; +0.1 Tanks & Armor Variants HP |
| Military Police | +1.0 | 0 | 0.3 | +0.1 | +0.02 | 500 | 180 | 40 Infantry Equipment, 10 Support Equipment | — | — | +3.0 | +0.5 | — | +20.0 | +2.0 | — | 1 | 0 | 0 | +50.2 | **+20% Suppression**; blocks Motorized Military Police; **+20% All Infantry Recovery Rate** |
| Motorized Military Police | +2.0 | 10 | 0.3 | +0.1 | +0.03 | 500 | 200 | 20 Infantry Equipment, 5 Support Equipment, 20 Military Motorcycle | — | — | +3.0 | +0.5 | — | +20.0 | +3.0 | — | 1 | 24.0 | 0.5 | +51.6 | **+30% Suppression**; **+1 Recon**; cannot paradrop; blocks Military Police; +20% All Infantry Recovery Rate; +20% Mot. & Mech. Infantry Suppression |
| Signal Company | +1.0 | 20 | 0.3 | +0.1 | +0.02 | 500 | 120 | 10 Motorized, 20 Support Equipment | −100% Fuel Use | — | — | — | — | — | +5.0 | — | — | 0 | 0 | +98.0 | **+10% Initiative**; blocks Armored Signal Company |
| Armored Signal Company | +1.0 | 20 | 0.3 | +0.1 | +0.035 | 500 | 120 | 20 Armored Support Equipment, 15 Support Equipment | — | — | +6.0 | +2.0 | — | +10.0 | +3.0 | 12.0 | 5.0 | 86.4 | 1.8 | +365.0 | **+12% Initiative**; cannot paradrop; blocks Signal Company; **+5% Tanks & Armor Variants Breakthrough** |
| Super Heavy Tank | +2.0 | 10 | 0.3 | +1.0 | +0.40 | 500 | 180 | 20 Super Heavy Tanks | — | 4.0 | +38.0 | +45.0 | — | +10.0 | +74.0 | 145 | 146 | 480.00 | 10.00 | +2000 | Suppression 2.5; **speed affects division**; terrain penalties; **fort attack bonus**; cannot paradrop |
| Super Heavy SP Artillery | +0.6 | 0 | 0.1 | +1.75 | +0.80 | 500 | 180 | 20 SH SP Artillery | −25% Breakthrough | 4.0 | +85.0 | +3.0 | — | +7.0 | +2.625 | 100 | 9 | 240.00 | 5.00 | +2000 | Suppression 1.25; speed affects division; terrain penalties; cannot paradrop; **unaffected by support company bonuses** |
| Super Heavy Tank Destroyer | +0.6 | 0 | 0.3 | +1.75 | +0.40 | 500 | 180 | 20 SH Tank Destroyer | −25% Breakthrough | 4.0 | +12.0 | +70.0 | — | +7.0 | +1.35 | 145 | 170 | 240.00 | 5.00 | +2000 | Suppression 1.25; speed affects division; terrain penalties; cannot paradrop; unaffected by support company bonuses |
| Super Heavy SP Anti-Air | +0.6 | 0 | 0.1 | +1.75 | +0.10 | 500 | 180 | 20 SH SP Anti-Air | −35% Breakthrough | 4.0 | +11.5 | +9.0 | +50.0 (air) | +3.5 | +2.275 | 100 | 98 | 120.00 | 2.50 | +2000 | Suppression 0.75; speed affects division; terrain penalties; cannot paradrop; unaffected by support company bonuses |
| Land Cruiser | +15.0 | 60 | 0.3 | +2.0 | +0.6 | 1000 | 250 | 1 Land Cruiser | — | 5.0 | +80.0 | +65.0 | +32.0 (air) | +35.0 | +120.0 | 180 | 160 | 672.00 | 14.00 | +300 | Suppression 4; **speed affects division**; terrain penalties; **fort attack bonus**; cannot paradrop |
| Light Flame Tank Company | +2.0 | 20 | 0.3 | +0.1 | +0.02 | 300 | 120 | 15 Light Flame Tanks | −75% Hard/Defence/Armour, −50% Soft/Breakthrough | Tank designer | — | — | — | — | — | — | — | — | — | — | **Requires No Step Back.** Speed affects division; terrain attack bonuses; fort movement bonus; cannot paradrop; blocks other flame tank companies; **+5% All Infantry Breakthrough** |
| Medium Flame Tank Company | +2.0 | 20 | 0.3 | +0.1 | +0.025 | 300 | 120 | 15 Medium Flame Tanks | −70% Hard/Defence/Armour, −45% Soft/Breakthrough | Tank designer | — | — | — | — | — | — | — | — | — | — | **Requires No Step Back.** Same specials as Light Flame Tank Company |
| Heavy Flame Tank Company | +2.0 | 20 | 0.3 | +0.1 | +0.03 | 300 | 120 | 15 Heavy Flame Tanks | −62.5% Hard/Defence/Armour, −40% Soft/Breakthrough | Tank designer | — | — | — | — | — | — | — | — | — | — | **Requires No Step Back.** Same specials as Light Flame Tank Company |
| Assault Battalion (Blackshirt) | +40.0 | 10 | 0.2 | +0.4 | +0.06 | 1000 | 120 | 100 Infantry Equipment, 10 Support Equipment | +10% Soft, +30% Breakthrough | — | +3.3 | +0.5 | — | +22.0 | +2.6 | — | 1 | 0 | 0 | +83.0 | Suppression 1.5; **unaffected by support company bonuses** |
| Winter Logistics Company | +2.0 | 45 | 0.3 | +0.1 | +0.05 | 500 | 120 | 40 Infantry Equipment, 10 Support Equipment | −50% Breakthrough/Soft/Hard/Armor | — | +1.5 | +0.25 | — | +20.0 | +1.0 | — | 1 | 0 | 0 | +57.2 | **+300% Cold acclimatization gain rate**; various snow bonuses |
| Sturmtruppe Battalion | +20.0 | 70 | 0.4 | +0.5 | +0.05 | 1000 | 120 | 150 Infantry Equipment, 10 Support Equipment | +10% Soft attack | — | +3.3 | +0.5 | — | +20.0 | +2.6 | — | 1 | 0 | 0 | +104.5 | Suppression 1; **fort and urban attack bonuses**; unaffected by support company bonuses |

**Recon company values at a glance:** Cavalry +1, Motorized +1.5, Armoured Car +2, Light Tank +1, Recon Rangers +1, Long Range Patrol +2, Helicopter Recon +2, Airborne Light Armour +1, Motorized Military Police +1.

**Entrenchment at a glance:** Engineer +2, Armored Engineer +3, Assault Engineer +2, Pioneers +2.5, Jungle Pioneers +2.

## Full stats by unit and technology year

Only years that bring an upgrade are listed. Doctrine technologies are **not** included (they have no year and are largely mutually exclusive). **Total cost** = production cost + (1.5/8) × resource cost, derived from the import rate (8) and the cost ratio between military (7200) and civilian (10800) factories.

Common column order: Year / Prod. cost / Res. cost / Total cost / Manpower / Train time (days) / Supply / Weight / Width / Speed / Org. / Recovery / HP / Hardness / Soft attack / Hard attack / Air attack / Defense / Breakthrough / Armor / Piercing.

### Infantry afoot

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1918 | 40 | 80 | 55 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 3.0 | 0.5 | — | 21.0 | 2.1 | — | 1.0 |
| 1936 | 50 | 100 | 68 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 6.0 | 1.0 | — | 23.1 | 3.2 | — | 4.0 |
| 1938 | 50 | 100 | 68 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 6.3 | 1.0 | — | 24.2 | 3.3 | — | 4.0 |
| 1939 | 60 | 180 | 93 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 9.5 | 1.5 | — | 30.8 | 4.4 | — | 5.0 |
| 1940 | 60 | 180 | 93 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 9.9 | 1.5 | — | 32.2 | 4.6 | — | 5.0 |
| 1942 | 70 | 280 | 122 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 13.2 | 2.5 | — | 40.8 | 6.0 | — | 20.0 |
| 1943 | 70 | 280 | 122 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 13.2 | 3.0 | — | 40.8 | 6.0 | — | 30.0 |
| 1944 | 70 | 280 | 122 | 1000 | 90 | 0.07 | 0.5 | 2 | 4.0 | 60 | 0.3 | 25.0 | 0% | 13.8 | 3.0 | — | 40.8 | 6.0 | — | 30.0 |

### Bicycle Infantry

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 90 | 220 | 131 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 6.0 | 1.0 | — | 23.1 | 3.2 | — | 4.0 |
| 1938 | 90 | 220 | 131 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 6.3 | 1.0 | — | 24.2 | 3.3 | — | 4.0 |
| 1939 | 100 | 300 | 156 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 9.5 | 1.5 | — | 30.8 | 4.4 | — | 5.0 |
| 1940 | 100 | 300 | 156 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 9.9 | 1.5 | — | 32.2 | 4.6 | — | 5.0 |
| 1942 | 110 | 400 | 185 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 13.2 | 2.5 | — | 40.8 | 6.0 | — | 20.0 |
| 1943 | 110 | 400 | 185 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 13.2 | 3.0 | — | 40.8 | 6.0 | — | 30.0 |
| 1944 | 110 | 400 | 185 | 1000 | 90 | 0.07 | 0.5 | 2 | 6.4 | 60 | 0.3 | 25.0 | 0% | 13.8 | 3.0 | — | 40.8 | 6.0 | — | 30.0 |

### Motorized Infantry

There is only **one** motorized equipment (trucks, from 1936); all stat differences come from the infantry equipment generation issued to the battalion.

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 175 | 475 | 264 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 10% | 6.0 | 1.0 | — | 23.1 | 3.2 | — | 4.0 |
| 1938 | 175 | 475 | 264 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 10% | 6.3 | 1.0 | — | 24.2 | 3.3 | — | 4.0 |
| 1939 | 185 | 555 | 289 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 10% | 9.5 | 1.5 | — | 30.8 | 4.4 | — | 5.0 |
| 1940 | 185 | 555 | 289 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 20% | 9.9 | 1.5 | — | 32.2 | 4.6 | — | 5.0 |
| 1942 | 195 | 655 | 317 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 20% | 13.2 | 2.5 | — | 40.8 | 6.0 | — | 20.0 |
| 1943 | 195 | 655 | 317 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 20% | 13.2 | 3.0 | — | 40.8 | 6.0 | — | 30.0 |
| 1944 | 195 | 655 | 317 | 1200 | 90 | 0.11 | 0.8 | 2 | 12.0 | 60 | 0.3 | 25.0 | 20% | 14.4 | 3.0 | — | 40.8 | 6.0 | — | 30.0 |

### Mechanized Infantry

Unlike motorized, there are three mechanized equipment generations. (The wiki notes it is unknown whether the infantry equipment issued further modifies these values.)

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1940 | 460 | 1780 | 793 | 1200 | 120 | 0.18 | 1.0 | 2 | 8.0 | 60 | 0.3 | 30.0 | 60% | 10.8 | 7.5 | — | 62.1 | 9.2 | 10.0 | 16.0 |
| 1942 | 570 | 2780 | 1091 | 1200 | 120 | 0.18 | 1.0 | 2 | 10.0 | 60 | 0.3 | 30.0 | 72% | 14.4 | 10.5 | — | 76.8 | 12.0 | 15.0 | 52.0 |
| 1943 | 570 | 2780 | 1091 | 1200 | 120 | 0.18 | 1.0 | 2 | 10.0 | 60 | 0.3 | 30.0 | 72% | 14.4 | 11.0 | — | 76.8 | 12.0 | 15.0 | 78.0 |
| 1944 | 670 | 4480 | 1510 | 1200 | 120 | 0.18 | 1.0 | 2 | 12.0 | 60 | 0.3 | 30.0 | 84% | 17.4 | 11.3 | — | 81.6 | 13.2 | 20.0 | 93.0 |

### Marines

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 75 | 150 | 103 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 70 | 0.4 | 20.0 | 0% | 6.0 | 1.0 | — | 22.7 | 4.0 | — | 4.0 |
| 1938 | 75 | 150 | 103 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 70 | 0.4 | 20.0 | 0% | 6.3 | 1.0 | — | 23.3 | 4.1 | — | 4.0 |
| 1939 | 90 | 270 | 140 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 75 | 0.4 | 20.0 | 0% | 9.9 | 1.5 | — | 29.7 | 5.4 | — | 5.0 |
| 1940 | 90 | 270 | 140 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 80 | 0.4 | 20.0 | 0% | 10.3 | 1.5 | — | 31.9 | 5.6 | — | 5.0 |
| 1942 | 105 | 420 | 183 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 80 | 0.4 | 20.0 | 0% | 13.8 | 2.5 | — | 39.8 | 7.1 | — | 20.0 |
| 1943 | 105 | 420 | 183 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 85 | 0.4 | 20.0 | 0% | 13.8 | 3.0 | — | 39.8 | 7.1 | — | 30.0 |
| 1944 | 105 | 420 | 183 | 1000 | 120 | 0.06 | 0.5 | 2 | 4.0 | 90 | 0.4 | 20.0 | 0% | 15.0 | 3.0 | — | 39.8 | 7.1 | — | 30.0 |

### Mountaineers

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 70 | 140 | 96 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 70 | 0.4 | 20.0 | 0% | 6.0 | 1.0 | — | 22.7 | 4.0 | — | 4.0 |
| 1938 | 70 | 140 | 96 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 70 | 0.4 | 20.0 | 0% | 6.3 | 1.0 | — | 23.3 | 4.1 | — | 4.0 |
| 1939 | 84 | 252 | 131 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 75 | 0.4 | 20.0 | 0% | 9.9 | 1.5 | — | 29.7 | 5.4 | — | 5.0 |
| 1940 | 84 | 252 | 131 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 80 | 0.4 | 20.0 | 0% | 10.3 | 1.5 | — | 31.9 | 5.6 | — | 5.0 |
| 1942 | 98 | 392 | 171 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 80 | 0.4 | 20.0 | 0% | 13.8 | 2.5 | — | 39.8 | 7.1 | — | 20.0 |
| 1943 | 98 | 392 | 171 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 85 | 0.4 | 20.0 | 0% | 13.8 | 3.0 | — | 39.8 | 7.1 | — | 30.0 |
| 1944 | 98 | 392 | 171 | 1000 | 120 | 0.07 | 0.5 | 2 | 4.0 | 90 | 0.4 | 20.0 | 0% | 15.0 | 3.0 | — | 39.8 | 7.1 | — | 30.0 |

### Paratroopers

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 65 | 130 | 89 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 70 | 0.4 | 22.0 | 0% | 6.0 | 1.0 | — | 22.7 | 3.1 | — | 4.0 |
| 1938 | 65 | 130 | 89 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 70 | 0.4 | 22.0 | 0% | 6.3 | 1.0 | — | 23.3 | 3.2 | — | 4.0 |
| 1939 | 78 | 234 | 121 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 75 | 0.4 | 22.0 | 0% | 9.9 | 1.5 | — | 29.7 | 4.2 | — | 5.0 |
| 1940 | 78 | 234 | 121 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 80 | 0.4 | 22.0 | 0% | 10.3 | 1.5 | — | 31.9 | 4.4 | — | 5.0 |
| 1942 | 91 | 364 | 159 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 80 | 0.4 | 22.0 | 0% | 13.8 | 2.5 | — | 39.8 | 5.6 | — | 20.0 |
| 1943 | 91 | 364 | 159 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 85 | 0.4 | 22.0 | 0% | 13.8 | 3.0 | — | 39.8 | 5.6 | — | 30.0 |
| 1944 | 91 | 364 | 159 | 1000 | 150 | 0.06 | 0.5 | 2 | 4.0 | 90 | 0.4 | 22.0 | 0% | 15.0 | 3.0 | — | 39.8 | 5.6 | — | 30.0 |

### Cavalry (Horses) — and Camels, which share identical values

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1918 | 48 | 96 | 66 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 3.0 | 0.5 | — | 20.4 | 2.0 | — | 1.0 |
| 1936 | 60 | 120 | 82 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 6.0 | 1.0 | — | 22.4 | 3.1 | — | 4.0 |
| 1938 | 60 | 120 | 82 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 6.3 | 1.0 | — | 22.9 | 3.1 | — | 4.0 |
| 1939 | 72 | 216 | 112 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 9.5 | 1.5 | — | 29.1 | 4.2 | — | 5.0 |
| 1940 | 72 | 216 | 112 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 9.9 | 1.5 | — | 29.7 | 4.2 | — | 5.0 |
| 1942 | 84 | 336 | 146 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 13.2 | 2.0 | — | 36.7 | 5.4 | — | 10.0 |
| 1944 | 84 | 336 | 146 | 1000 | 120 | 0.12 | 0.5 | 2 | 6.4 | 70 | 0.3 | 25.0 | 0% | 14.4 | 2.0 | — | 36.7 | 5.4 | — | 10.0 |

> The `Land units by unit` Camels table is numerically identical to Horses. The battalion-level table gives Camelry different base values (HP +30.0, supply +0.10, weight +0.6, +40% max speed → 5.6 km/h, 150 infantry equipment, soft +6.0, hard +1.0, defence +22.0, breakthrough +3.0, piercing 4, cost +64.5) plus desert bonuses.

### Towed / Motorized Artillery

Both share the table below; the differences are:

| Type | Speed | Supply consumption | Extra cost | Hardness |
|---|---|---|---|---|
| Towed artillery | 4 km/h | 0.3 | — | 0% |
| Motorized artillery | 12 km/h | 0.2 | 50 trucks | 10% |

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1918 | 126 | 378 | 196 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 25.0 | 2.0 | 10.0 | 6.0 | 5.0 |
| 1936 | 126 | 378 | 196 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 27.5 | 2.0 | 10.0 | 6.0 | 5.0 |
| 1939 | 144 | 432 | 225 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 33.0 | 2.0 | 15.0 | 7.0 | 5.0 |
| 1940 | 144 | 432 | 225 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 36.0 | 2.0 | 15.0 | 7.0 | 5.0 |
| 1941 | 144 | 432 | 225 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 39.0 | 2.0 | 15.0 | 7.0 | 5.0 |
| 1942 | 162 | 648 | 283 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 44.2 | 2.0 | 18.0 | 8.0 | 5.0 |
| 1943 | 162 | 648 | 283 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 47.6 | 2.0 | 18.0 | 8.0 | 5.0 |

### Support Artillery

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1918 | 42 | 126 | 65 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 15.0 | 1.2 | 6.0 | 3.6 | 5.0 |
| 1936 | 42 | 126 | 65 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 17.5 | 1.2 | 6.0 | 3.6 | 5.0 |
| 1939 | 48 | 144 | 75 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 21.0 | 1.2 | 9.0 | 4.2 | 5.0 |
| 1940 | 48 | 144 | 75 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 24.0 | 1.2 | 9.0 | 4.2 | 5.0 |
| 1941 | 48 | 144 | 75 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 27.0 | 1.2 | 9.0 | 4.2 | 5.0 |
| 1942 | 54 | 216 | 94 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 30.6 | 1.2 | 10.8 | 4.8 | 5.0 |
| 1943 | 54 | 216 | 94 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 34.0 | 1.2 | 10.8 | 4.8 | 5.0 |

### Rocket Artillery (horse / truck-drawn)

Horse-drawn: 4 km/h, supply 0.3, hardness 0%. Truck-drawn: 12 km/h, supply 0.2, hardness 10%, plus 50 trucks.

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1940 | 144 | 432 | 225 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 30.0 | 1.0 | 12.0 | 9.0 | 2.0 |
| 1941 | 144 | 432 | 225 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 34.5 | 1.0 | 12.0 | 9.0 | 2.0 |
| 1942 | 144 | 432 | 225 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 39.0 | 1.0 | 12.0 | 9.0 | 2.0 |
| 1943 | 180 | 540 | 281 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 49.4 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1944 | 180 | 540 | 281 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 51.3 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1945 | 180 | 540 | 281 | 500 | 120 | 0.20 | 0.5 | 3 | 0 | 0.1 | 0.6 | 0% | 53.2 | 1.0 | 15.0 | 12.0 | 2.0 |

### Support Rocket Artillery

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1940 | 96 | 288 | 150 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 15.0 | 0.5 | 6.0 | 4.5 | 2.0 |
| 1941 | 96 | 288 | 150 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 19.5 | 0.5 | 6.0 | 4.5 | 2.0 |
| 1942 | 96 | 288 | 150 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 24.0 | 0.5 | 6.0 | 4.5 | 2.0 |
| 1943 | 120 | 360 | 187 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 30.4 | 0.5 | 7.5 | 6.0 | 2.0 |
| 1944 | 120 | 360 | 187 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 32.3 | 0.5 | 7.5 | 6.0 | 2.0 |
| 1945 | 120 | 360 | 187 | 300 | 120 | 0.16 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 34.2 | 0.5 | 7.5 | 6.0 | 2.0 |

### Motorized Rocket Artillery (Katyusha-type; distinct from truck-drawn)

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1939 | 277 | 832 | 433 | 500 | 120 | 0.28 | 0.5 | 3 | 12.0 | 0 | 0.1 | 0.6 | 10% | 36.0 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1941 | 277 | 832 | 433 | 500 | 120 | 0.28 | 0.5 | 3 | 12.0 | 0 | 0.1 | 0.6 | 10% | 41.4 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1942 | 277 | 832 | 433 | 500 | 120 | 0.28 | 0.5 | 3 | 12.0 | 0 | 0.1 | 0.6 | 10% | 46.8 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1943 | 277 | 832 | 433 | 500 | 120 | 0.28 | 0.5 | 3 | 12.0 | 0 | 0.1 | 0.6 | 10% | 57.6 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1944 | 277 | 832 | 433 | 500 | 120 | 0.28 | 0.5 | 3 | 12.0 | 0 | 0.1 | 0.6 | 10% | 59.4 | 1.0 | 15.0 | 12.0 | 2.0 |
| 1945 | 277 | 832 | 433 | 500 | 120 | 0.28 | 0.5 | 3 | 12.0 | 0 | 0.1 | 0.6 | 10% | 61.2 | 1.0 | 15.0 | 12.0 | 2.0 |

### Self-propelled artillery

| Unit | Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light SP Artillery | 1934 | 288 | 1152 | 504 | 500 | 180 | 0.40 | 1.0 | 3 | 10.0 | 0 | 0.1 | 0.6 | 50% | 34.0 | 0.5 | 4.0 | 2.0 | 5.0 | 4.0 |
| Light SP Artillery | 1936 | 324 | 1620 | 627 | 500 | 180 | 0.40 | 1.0 | 3 | 12.0 | 0 | 0.1 | 0.6 | 50% | 42.0 | 1.0 | 5.0 | 2.5 | 10.0 | 4.0 |
| Light SP Artillery | 1941 | 360 | 2520 | 832 | 500 | 180 | 0.40 | 1.0 | 3 | 14.0 | 0 | 0.1 | 0.6 | 50% | 46.0 | 1.5 | 7.0 | 3.5 | 25.0 | 4.0 |
| Medium SP Artillery | 1939 | 432 | 2592 | 918 | 500 | 180 | 0.44 | 1.2 | 3 | 8.0 | 0 | 0.1 | 0.6 | 65% | 42.0 | 1.0 | 5.0 | 3.0 | 45.0 | 5.0 |
| Medium SP Artillery | 1941 | 468 | 3276 | 1082 | 500 | 180 | 0.44 | 1.2 | 3 | 9.0 | 0 | 0.1 | 0.6 | 65% | 50.0 | 1.5 | 6.0 | 3.0 | 50.0 | 5.0 |
| Medium SP Artillery | 1943 | 504 | 4536 | 1354 | 500 | 180 | 0.44 | 1.2 | 3 | 10.0 | 0 | 0.1 | 0.6 | 65% | 55.0 | 2.0 | 7.0 | 4.0 | 58.0 | 5.0 |
| Heavy SP Artillery | 1934 | 600 | 4200 | 1387 | 500 | 180 | 0.60 | 1.5 | 3 | 5.0 | 0 | 0.1 | 0.6 | 80% | 55.0 | 1.0 | 4.0 | 2.0 | 45.0 | 8.0 |
| Heavy SP Artillery | 1941 | 648 | 5184 | 1620 | 500 | 180 | 0.60 | 1.5 | 3 | 6.0 | 0 | 0.1 | 0.6 | 80% | 74.0 | 2.0 | 6.0 | 3.0 | 68.0 | 8.0 |
| Heavy SP Artillery | 1943 | 720 | 6480 | 1935 | 500 | 180 | 0.60 | 1.5 | 3 | 6.0 | 0 | 0.1 | 0.6 | 80% | 80.0 | 2.5 | 7.0 | 3.5 | 90.0 | 8.0 |
| Super Heavy SP Artillery | 1943 | 1200 | 10800 | 3225 | 500 | 180 | 0.80 | 1.8 | 3 | 3.5 | 0 | 0.1 | 0.6 | 90% | 85.0 | 3.0 | 7.0 | 3.5 | 100.0 | 9.0 |
| Modern SP Artillery | 1945 | 1120 | 8960 | 2800 | 500 | 180 | 0.50 | 1.5 | 3 | 10.0 | 0 | 0.1 | 0.6 | 85% | 80.0 | 3.0 | 8.0 | 4.0 | 90.0 | 10.0 |

### Armored Car

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 240 | – | 240 | 500 | 180 | 0.14 | 0.8 | 2 | 9.0 | 10 | 0.3 | 2.0 | 65% | 6.0 | 2.0 | 2.0 | 12.0 | 3.0 | 6.0 |
| 1940 | 360 | 2 Steel | ? | 500 | 180 | 0.14 | 0.8 | 2 | 12.0 | 10 | 0.3 | 2.0 | 65% | 13.0 | 4.0 | 3.0 | 16.0 | 10.0 | 8.0 |
| 1941 | 480 | 2 Steel, 1 Tungsten | ? | 500 | 180 | 0.14 | 0.8 | 2 | 15.0 | 10 | 0.3 | 2.0 | 70% | 16.0 | 8.0 | 5.0 | 28.0 | 20.0 | 36.0 |
| 1942 | 540 | 2 Steel, 1 Tungsten | ? | 500 | 180 | 0.14 | 0.8 | 2 | 16.0 | 10 | 0.3 | 2.0 | 70% | 12.0 | 14.0 | 6.0 | 28.0 | 20.0 | 62.0 |

### Tanks

| Unit | Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light Tank | 1918 | 420 | 1260 | 656 | 500 | 180 | 0.20 | 1.0 | 2 | 6.0 | 10 | 0.3 | 2.0 | 80% | 8.0 | 4.0 | 4.0 | 18.0 | 5.0 | 15.0 |
| Light Tank | 1934 | 480 | 1440 | 750 | 500 | 180 | 0.20 | 1.0 | 2 | 10.0 | 10 | 0.3 | 2.0 | 80% | 13.0 | 4.0 | 4.0 | 26.0 | 10.0 | 10.0 |
| Light Tank | 1936 | 540 | 2160 | 945 | 500 | 180 | 0.20 | 1.0 | 2 | 12.0 | 10 | 0.3 | 2.0 | 80% | 16.0 | 6.0 | 5.0 | 36.0 | 15.0 | 30.0 |
| Light Tank | 1941 | 600 | 3600 | 1275 | 500 | 180 | 0.20 | 1.0 | 2 | 14.0 | 10 | 0.3 | 2.0 | 80% | 22.0 | 9.0 | 6.0 | 46.0 | 30.0 | 50.0 |
| Medium Tank | 1939 | 600 | 3000 | 1162 | 500 | 180 | 0.22 | 1.2 | 2 | 8.0 | 10 | 0.3 | 2.0 | 90% | 19.0 | 14.0 | 5.0 | 36.0 | 60.0 | 61.0 |
| Medium Tank | 1941 | 650 | 3900 | 1381 | 500 | 180 | 0.22 | 1.2 | 2 | 9.0 | 10 | 0.3 | 2.0 | 90% | 25.0 | 19.0 | 7.0 | 51.0 | 80.0 | 81.0 |
| Medium Tank | 1943 | 700 | 5600 | 1750 | 500 | 180 | 0.22 | 1.2 | 2 | 10.0 | 10 | 0.3 | 2.0 | 90% | 32.0 | 24.0 | 9.0 | 66.0 | 90.0 | 91.0 |
| Heavy Tank | 1934 | 1000 | 7000 | 2312 | 500 | 180 | 0.30 | 1.5 | 2 | 5.0 | 10 | 0.3 | 2.0 | 95% | 15.0 | 12.0 | 6.0 | 36.0 | 70.0 | 35.0 |
| Heavy Tank | 1941 | 1080 | 7560 | 2497 | 500 | 180 | 0.30 | 1.5 | 2 | 6.0 | 10 | 0.3 | 2.0 | 95% | 27.0 | 30.0 | 8.0 | 52.0 | 110.0 | 111.0 |
| Heavy Tank | 1943 | 1200 | 9600 | 3000 | 500 | 180 | 0.30 | 1.5 | 2 | 6.0 | 10 | 0.3 | 2.0 | 95% | 35.0 | 40.0 | 9.0 | 67.0 | 130.0 | 131.0 |
| Super-Heavy Tank | 1943 | 1500 | 13500 | 4031 | 500 | 180 | 0.40 | 1.8 | 2 | 3.5 | 10 | 0.3 | 2.0 | 99% | 38.0 | 45.0 | 10.0 | 74.0 | 145.0 | 146.0 |
| Modern Tank | 1945 | 1400 | 11200 | 3500 | 500 | 180 | 0.25 | 1.5 | 2 | 10.0 | 10 | 0.3 | 2.0 | 98% | 40.0 | 32.0 | 10.0 | 84.0 | 130.0 | 131.0 |

### Anti-Air (horse / motorized line battalion)

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 120 | 240 | 165 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.1 | 0.6 | 0% | 3.0 | 7.0 | 19.0 | 4.0 | 1.0 | 25.0 |
| 1939 | 120 | 240 | 165 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.1 | 0.6 | 0% | 3.0 | 7.0 | 20.9 | 4.0 | 1.0 | 25.0 |
| 1940 | 150 | 300 | 206 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.1 | 0.6 | 0% | 3.5 | 11.0 | 27.5 | 4.0 | 1.0 | 60.0 |
| 1941 | 150 | 300 | 206 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.1 | 0.6 | 0% | 3.5 | 11.0 | 30.0 | 4.0 | 1.0 | 60.0 |
| 1942 | 150 | 300 | 206 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.1 | 0.6 | 0% | 3.5 | 11.0 | 32.5 | 4.0 | 1.0 | 60.0 |
| 1943 | 180 | 540 | 281 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.1 | 0.6 | 0% | 4.0 | 15.0 | 41.6 | 4.0 | 1.0 | 88.0 |

### Support Anti-Air

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 80 | 160 | 110 | 300 | 120 | 0.10 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 1.8 | 4.2 | 15.2 | 2.4 | 0.6 | 25.0 |
| 1939 | 80 | 160 | 110 | 300 | 120 | 0.10 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 1.8 | 4.2 | 17.1 | 2.4 | 0.6 | 25.0 |
| 1940 | 100 | 200 | 137 | 300 | 120 | 0.10 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.1 | 6.6 | 22.5 | 2.4 | 0.6 | 60.0 |
| 1941 | 100 | 200 | 137 | 300 | 120 | 0.10 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.1 | 6.6 | 25.0 | 2.4 | 0.6 | 60.0 |
| 1942 | 100 | 200 | 137 | 300 | 120 | 0.10 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.1 | 6.6 | 27.5 | 2.4 | 0.6 | 60.0 |
| 1943 | 120 | 360 | 187 | 300 | 120 | 0.10 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.4 | 9.0 | 35.2 | 2.4 | 0.6 | 88.0 |

### Self-propelled anti-air

| Unit | Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Air | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light SP AA | 1934 | 150 | 450 | 234 | 500 | 180 | 0.10 | 1.0 | 1 | 10.0 | 0 | 0.1 | 0.6 | 50% | 3.0 | 1.0 | 15.0 | 2.0 | 2.0 | 5.0 | 5.0 |
| Light SP AA | 1936 | 165 | 660 | 288 | 500 | 180 | 0.10 | 1.0 | 1 | 12.0 | 0 | 0.1 | 0.6 | 50% | 4.5 | 1.5 | 17.0 | 2.5 | 2.5 | 10.0 | 20.0 |
| Light SP AA | 1941 | 180 | 1080 | 382 | 500 | 180 | 0.10 | 1.0 | 1 | 14.0 | 0 | 0.1 | 0.6 | 50% | 6.8 | 4.0 | 32.0 | 3.5 | 3.5 | 25.0 | 35.0 |
| Medium SP AA | 1939 | 144 | 720 | 279 | 500 | 180 | 0.10 | 1.2 | 1 | 8.0 | 0 | 0.1 | 0.6 | 65% | 6.8 | 3.0 | 22.0 | 2.5 | 2.5 | 45.0 | 40.0 |
| Medium SP AA | 1941 | 156 | 936 | 331 | 500 | 180 | 0.10 | 1.2 | 1 | 9.0 | 0 | 0.1 | 0.6 | 65% | 9.0 | 4.5 | 32.0 | 3.0 | 3.0 | 50.0 | 60.0 |
| Medium SP AA | 1943 | 168 | 1344 | 420 | 500 | 180 | 0.10 | 1.2 | 1 | 10.0 | 0 | 0.1 | 0.6 | 65% | 11.2 | 6.0 | 43.0 | 3.5 | 3.5 | 58.0 | 70.0 |
| Heavy SP AA | 1934 | 200 | 1400 | 462 | 500 | 180 | 0.10 | 1.5 | 1 | 5.0 | 0 | 0.1 | 0.6 | 80% | 6.8 | 4.0 | 17.0 | 2.0 | 2.0 | 45.0 | 25.0 |
| Heavy SP AA | 1941 | 216 | 1512 | 499 | 500 | 180 | 0.10 | 1.5 | 1 | 6.0 | 0 | 0.1 | 0.6 | 80% | 9.0 | 4.5 | 33.0 | 3.0 | 3.0 | 68.0 | 60.0 |
| Heavy SP AA | 1943 | 240 | 1920 | 600 | 500 | 180 | 0.10 | 1.5 | 1 | 6.0 | 0 | 0.1 | 0.6 | 80% | 11.2 | 6.0 | 44.0 | 3.5 | 3.5 | 90.0 | 88.0 |
| Super Heavy SP AA | 1943 | 400 | 3600 | 1075 | 500 | 180 | 0.10 | 1.8 | 1 | 3.5 | 0 | 0.1 | 0.6 | 90% | 17.2 | 9.0 | 50.0 | 3.5 | 3.5 | 100.0 | 98.0 |
| Modern SP AA | 1945 | 336 | 2688 | 840 | 500 | 180 | 0.10 | 1.5 | 1 | 10.0 | 0 | 0.1 | 0.6 | 85% | 13.5 | 7.5 | 50.0 | 4.0 | 4.0 | 90.0 | 100.0 |

### Anti-Tank (horse / motorized line battalion)

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Def | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 144 | 576 | 252 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.0 | 0.6 | 0% | 4.0 | 15.0 | 4.0 | 75.0 |
| 1939 | 144 | 576 | 252 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.0 | 0.6 | 0% | 4.0 | 16.5 | 4.0 | 90.0 |
| 1940 | 180 | 720 | 315 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.0 | 0.6 | 0% | 4.0 | 24.2 | 4.0 | 105.6 |
| 1941 | 180 | 720 | 315 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.0 | 0.6 | 0% | 4.0 | 26.4 | 4.0 | 114.4 |
| 1942 | 180 | 720 | 315 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.0 | 0.6 | 0% | 4.0 | 28.6 | 4.0 | 123.2 |
| 1943 | 216 | 1080 | 418 | 500 | 120 | 0.10 | 0.5 | 1 | 0 | 0.0 | 0.6 | 0% | 4.0 | 39.0 | 4.0 | 151.2 |

### Support Anti-Tank

| Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Org | Rec | HP | Hard% | Soft | Hard | Def | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1936 | 96 | 384 | 168 | 300 | 120 | 0.08 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.0 | 7.5 | 2.0 | 63.8 |
| 1939 | 96 | 384 | 168 | 300 | 120 | 0.08 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.0 | 9.0 | 2.0 | 78.8 |
| 1940 | 120 | 480 | 210 | 300 | 120 | 0.08 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.0 | 13.2 | 2.0 | 92.4 |
| 1941 | 120 | 480 | 210 | 300 | 120 | 0.08 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.0 | 15.4 | 2.0 | 101.2 |
| 1942 | 120 | 480 | 210 | 300 | 120 | 0.08 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.0 | 17.6 | 2.0 | 110.0 |
| 1943 | 144 | 720 | 279 | 300 | 120 | 0.08 | 0.1 | 0 | 0 | 0.1 | 0.2 | 0% | 2.0 | 24.0 | 2.0 | 135.0 |

### Tank destroyers

| Unit | Year | Prod | Res | Total | MP | Trn | Supply | Wt | W | Speed | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Armor | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light TD | 1934 | 240 | 1200 | 465 | 500 | 180 | 0.20 | 1.0 | 2 | 10.0 | 0 | 0.3 | 0.6 | 80% | 6.0 | 10.0 | 4.0 | 1.0 | 10.0 | 50.0 |
| Light TD | 1936 | 270 | 1620 | 573 | 500 | 180 | 0.20 | 1.0 | 2 | 12.0 | 0 | 0.3 | 0.6 | 80% | 6.0 | 16.0 | 5.0 | 1.3 | 15.0 | 77.0 |
| Light TD | 1941 | 300 | 2400 | 750 | 500 | 180 | 0.20 | 1.0 | 2 | 14.0 | 0 | 0.3 | 0.6 | 80% | 8.0 | 24.0 | 7.0 | 1.8 | 30.0 | 99.0 |
| Medium TD | 1939 | 288 | 2016 | 666 | 500 | 180 | 0.22 | 1.2 | 2 | 8.0 | 0 | 0.3 | 0.6 | 90% | 5.0 | 20.0 | 5.0 | 1.3 | 60.0 | 88.0 |
| Medium TD | 1941 | 312 | 2496 | 780 | 500 | 180 | 0.22 | 1.2 | 2 | 9.0 | 0 | 0.3 | 0.6 | 90% | 6.0 | 26.0 | 6.0 | 1.5 | 80.0 | 110.0 |
| Medium TD | 1943 | 336 | 3360 | 966 | 500 | 180 | 0.22 | 1.2 | 2 | 10.0 | 0 | 0.3 | 0.6 | 90% | 8.0 | 32.0 | 7.0 | 1.8 | 90.0 | 120.0 |
| Heavy TD | 1934 | 500 | 3500 | 1156 | 500 | 180 | 0.30 | 1.5 | 2 | 5.0 | 0 | 0.3 | 0.6 | 95% | 6.0 | 25.0 | 4.0 | 1.0 | 70.0 | 96.0 |
| Heavy TD | 1941 | 540 | 4320 | 1350 | 500 | 180 | 0.30 | 1.5 | 2 | 6.0 | 0 | 0.3 | 0.6 | 95% | 8.0 | 42.0 | 6.0 | 1.5 | 110.0 | 140.0 |
| Heavy TD | 1943 | 600 | 6000 | 1725 | 500 | 180 | 0.30 | 1.5 | 2 | 6.0 | 0 | 0.3 | 0.6 | 95% | 10.0 | 60.0 | 7.0 | 1.8 | 130.0 | 160.0 |
| Super Heavy TD | 1943 | 700 | 6300 | 1881 | 500 | 180 | 0.40 | 1.8 | 2 | 3.5 | 0 | 0.3 | 0.6 | 99% | 12.0 | 70.0 | 7.0 | 1.8 | 145.0 | 170.0 |
| Modern TD | 1945 | 672 | 5376 | 1680 | 500 | 180 | 0.25 | 1.5 | 2 | 10.0 | 0 | 0.3 | 0.6 | 98% | 10.0 | 42.0 | 8.0 | 2.0 | 130.0 | 165.0 |

### Non-combat support companies by year

| Unit | Year | Prod | Res | Total | MP | Trn | Supply | Wt | Speed | Org | Rec | HP | Hard% | Soft | Hard | Def | Break | Pierce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Engineer Company | 1936 | 125 | 370 | 194 | 300 | 120 | 0.02 | 0.1 | 4.0 | 20 | 0.3 | 2.0 | 0% | 3.0 | 1.0 | 24.2 | 4.5 | 4.0 |
| Engineer Company | 1939 | 126 | 378 | 196 | 300 | 120 | 0.02 | 0.1 | 4.0 | 20 | 0.3 | 2.0 | 0% | 4.5 | 1.5 | 30.8 | 6.0 | 5.0 |
| Engineer Company | 1942 | 127 | 388 | 199 | 300 | 120 | 0.02 | 0.1 | 4.0 | 20 | 0.3 | 2.0 | 0% | 6.0 | 2.0 | 37.4 | 7.5 | 10.0 |
| Engineer Company | 1945 | 127 | 388 | 199 | 300 | 120 | 0.02 | 0.1 | 4.0 | 20 | 0.3 | 2.0 | 0% | 6.0 | 2.0 | 37.4 | 7.5 | 10.0 |
| Field Hospital | 1936–1945 | 170 | 510 | 265 | 500 | 120 | 0.05 | 0.1 | 12.0 | 20 | 0.3 | 2.0 | 10% | — | — | — | — | — |
| Logistics Company | 1936–1945 | 105 | 315 | 164 | 500 | 120 | — | 0.1 | 12.0 | 10 | 0.3 | 1.0 | 10% | — | — | — | — | — |
| Maintenance Company | 1936–1945 | 100 | 300 | 156 | 500 | 120 | 0.03 | 0.1 | — | 20 | 0.3 | 1.0 | 0% | — | — | — | — | — |
| Military Police | 1936 | 60 | 160 | 90 | 500 | 180 | 0.02 | 0.1 | 4.0 | 0 | 0.3 | 1.0 | 0% | 6.0 | 1.0 | 22.0 | 3.0 | 4.0 |
| Military Police | 1939 | 64 | 192 | 100 | 500 | 180 | 0.02 | 0.1 | 4.0 | 0 | 0.3 | 1.0 | 0% | 9.0 | 1.5 | 28.0 | 4.0 | 5.0 |
| Military Police | 1942 | 68 | 232 | 111 | 500 | 180 | 0.02 | 0.1 | 4.0 | 0 | 0.3 | 1.0 | 0% | 12.0 | 2.0 | 34.0 | 5.0 | 10.0 |
| Military Police | 1945 | 68 | 232 | 111 | 500 | 180 | 0.02 | 0.1 | 4.0 | 0 | 0.3 | 1.0 | 0% | 12.0 | 2.0 | 34.0 | 5.0 | 10.0 |
| Recon Company | 1936 | 60 | 160 | 90 | 500 | 120 | 0.02 | 0.1 | — | 20 | 0.3 | 2.0 | 0% | 0.6 | 0.1 | 11.0 | 1.5 | 4.0 |
| Recon Company | 1939 | 64 | 192 | 100 | 500 | 120 | 0.02 | 0.1 | — | 20 | 0.3 | 2.0 | 0% | 0.9 | 0.1 | 14.0 | 2.0 | 5.0 |
| Recon Company | 1942 | 68 | 232 | 111 | 500 | 120 | 0.02 | 0.1 | — | 20 | 0.3 | 2.0 | 0% | 1.2 | 0.2 | 17.0 | 2.5 | 10.0 |
| Recon Company | 1945 | 68 | 232 | 111 | 500 | 120 | 0.02 | 0.1 | — | 20 | 0.3 | 2.0 | 0% | 1.2 | 0.2 | 17.0 | 2.5 | 10.0 |
| Signal Company | 1936–1945 | 105 | 315 | 164 | 500 | 120 | 0.02 | 0.1 | 12.0 | 20 | 0.3 | 1.0 | 10% | — | — | — | — | — |

The Recon Company row is generic; `~/common/units/recon.txt` defines four distinct recon companies — **mounted, motorized, armored_car and light_tank** — each with its own recon value and its own equipment requirement (see the support company table above).

## Year availability index

Which units first exist at each equipment generation (from `Land units by year`):

| Year | Units available/updated |
|---|---|
| **1918** | Artillery, Cavalry, Infantry, Light Tank, Support Artillery |
| **1934** | + Heavy SP Anti-Air, Heavy SP Artillery, Heavy Tank, Heavy Tank Destroyer, Light SP Anti-Air, Light SP Artillery, Light Tank Destroyer |
| **1936** | + Bicycle, Motorized Infantry, Marines, Mountaineers, Paratroopers, Camels, Anti-Air, Support Anti-Air, Anti-Tank, Support Anti-Tank, Armored Car, Engineer/Field Hospital/Logistics/Maintenance/Military Police/Recon/Signal companies |
| **1938** | Infantry-equipment refresh (infantry, bicycle, motorized, cavalry, marines, mountaineers, paratroopers) |
| **1939** | + Medium Tank, Medium Tank Destroyer, Medium SP Anti-Air, Medium SP Artillery, Motorized Rocket Artillery |
| **1940** | + Mechanized Infantry, Rocket Artillery, Support Rocket Artillery |
| **1941** | Broad upgrade tier for tanks, SP artillery, SP AA, tank destroyers, artillery, AT |
| **1942** | Infantry/AT/AA refresh |
| **1943** | + Super-Heavy Tank, Super Heavy Tank Destroyer, Super Heavy SP Artillery, Super Heavy SP Anti-Air |
| **1944** | Final infantry-equipment and rocket tier |
| **1945** | + Modern Tank, Modern Tank Destroyer, Modern SP Artillery, Modern SP Anti-Air |

## Railway artillery

Railway artillery behaves unlike any other land unit.

- **Production:** like ships, the equipment and the unit are the same thing. Each piece produced is automatically deployed in the national capital.
- **Movement:** land movement is **only along railway lines**. It can cross water by moving manually to a railway-connected port and embarking to another port. Embarked railway artillery **ignores naval access-level settings**, so routes must be managed by hand to avoid unwanted sea zones.
- **Command:** cannot be assigned to commanders. Like air wings it can be assigned to follow land units, and it can be put into control groups.
- **Combat:** it does not attack directly. It applies a **debuff to nearby enemy units in combat**, similar to shore bombardment. Recent movement reduces its bombardment bonus for **24 hours**, recovering over time. If several railway guns are in range of one battle, **only the one with the greatest bombardment** participates.
- **Supply:** affects both its movement speed (down to **−80%** in low supply) and its bombardment. Supply for railway artillery **cannot be motorized at unit or army level** — supply hubs must be motorized manually.
- **Vulnerability:** damaged by air missions targeting railways. **100%** of Logistics Strike damage and **20%** of Strategic Bombing damage in the state spills over onto railway artillery there. Damaged guns are repaired with civilian factories and appear in the construction queue.
- **Capture:** **20% chance** of capture when overrun (raised by a higher Equipment Capture Ratio on the overrunning unit). On capitulation or annexation, **50%** of the pieces transfer to the new owner.

| Unit | HP | Weight | Supply | Speed | Bombardment | Range | Enemy fort effectiveness | Enemy entrenchment effectiveness | Enemy suppression | Manpower | Equipment | Production cost | Resources per factory |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Railway Gun | 2000 | 1 | 0.2 | 5 km/h | 25.0 | 240 km | −33.325% | −20% | +10% | 1000 | 1 Railway Gun | 800.0 | 4 Steel, 2 Tungsten, 2 Chromium |
| Super-Heavy Railway Gun | 3500 | 1 | 0.5 | 3 km/h | 40.0 | 360 km | −53.32% | −32% | +16% | 1500 | 1 Super-Heavy Railway Gun | 1600.0 | 8 Steel, 4 Tungsten, 4 Chromium |

## Related files

- [division-designer.md](division-designer.md) — how these subunits combine into a division
- [land-combat.md](land-combat.md) — how attack/defence/armour/piercing resolve into damage
- [combat-tactics.md](combat-tactics.md) — how recon and initiative feed the tactic system
- [historical-divisions.md](historical-divisions.md) — reference templates
