---
title: Land Doctrine
category: land-warfare
tags: [doctrine, land-doctrine, mastery, army-experience, officer-corps, mobile-warfare, superior-firepower, grand-battleplan, mass-assault, subdoctrine, tactics]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Land_doctrine
---

## Summary

Land doctrine specialises how a nation fights on land. Since patch 1.17 it is **not** a research tree: it is bought from the **Officer Corps** with **Army experience**, and it is split into four mutually exclusive **Grand Doctrines** (Mobile Warfare, Superior Firepower, Grand Battleplan, Mass Assault) plus four **Doctrine Tracks** (Infantry; Artillery & Combat Support; Armor; Operations) from each of which one **Subdoctrine** may be active. Subdoctrine milestones are unlocked by accumulating **Mastery**, which is earned by the relevant unit types fighting (or training, at 10% rate). There are no XP-cost-per-node/research-time values any more — that was the pre-1.17 system.

> ⚠️ The old land doctrine trees (Mobile Warfare / Superior Firepower / Grand Battleplan / Mass Assault as branching research trees with per-node army-XP costs, research days and mutually exclusive branches) were removed in **1.17**. The wiki now documents only the Grand Doctrine + Subdoctrine + Mastery system reproduced below. If a user asks about the old nodes (e.g. "Shock and Awe", "Mass Mobilization", "Superior Firepower path 1 vs 2"), tell them the system was reworked.

## How the system works

- Doctrines are reviewed and unlocked from the **Officer Corps** screen using **Army experience**.
- **Grand Doctrine**: exactly one active at a time. It gives flat bonuses, enables one **Tactic**, and defines the four **track milestones** (one per Doctrine Track) that fire when that track's subdoctrine is fully mastered.
- **Switching Grand Doctrine resets all Mastery in the land folder.** This is the single most expensive decision in the system — commit early.
- **Doctrine Tracks** (Infantry, Artillery & Combat Support, Armor, Operations) each hold one active Subdoctrine. Grand Doctrine does **not** restrict which Subdoctrines are available; any Subdoctrine can be paired with any Grand Doctrine.
- **Mastery** is the currency inside a track. Each milestone costs **100 Mastery, cumulative** (so 100 / 200 / 300 / 400 / 500) unless the subdoctrine's table says otherwise (People's Militia uses 50 / 100 / 200 / 250).
- Mastery is generated when units of the track's type **engage in combat**, or at **10% of that rate while training**.
- If **no Subdoctrine is selected** in a track, up to **200 Mastery** is held in reserve, banked at **25%** of the normal gain rate.
- Completing a track (mastering its subdoctrine) unlocks that Grand Doctrine's **track milestone**. One of the four milestones raises **Brigade Size +1**, and every milestone except Grand Battleplan's Operations milestone enables an extra **Tactic**.

### Mastery gain rates by track

| Doctrine Track | Multiplier | Gains Mastery from |
|---|---|---|
| Infantry | 1.0× | All Infantry & Mot/Mech |
| Artillery & Combat Support | 10.0× | Line Artillery, Support Artillery, Support Companies |
| Armor | 4.0× | Armored Car, Tanks & Armor Variants |
| Operations | 0.7× | All Infantry & Mot/Mech, Line Artillery, Support Artillery, Tanks & Armor Variants |

**Inferred:** the multiplier compensates for how few battalions of that type a typical army fields — Artillery & Combat Support fills fastest per engaged battalion, Operations slowest, so Operations is effectively the "whole-army" track that fills from everything you do.

## Grand Doctrines

Only one may be active. Switching wipes all land Mastery.

| Grand Doctrine | Bonuses | Tactic enabled |
|---|---|---|
| **Mobile Warfare** | Divisions speed: +10%<br>Planning Speed: +20% | Unexpected Thrust |
| **Superior Firepower** | Line Artillery: Soft Attack: +10%<br>Support Companies: Soft Attack: +5% | Overwhelming Fire |
| **Grand Battleplan** | Max planning: +10%<br>Daily Command Power Gain: +0.25 | Well-Planned Attack |
| **Mass Assault** | Non-Combat Out of Supply Penalties: -10%<br>Supply Grace: +48 hours | Relentless Assault |

Flavour intent: Mobile Warfare breaks trench deadlock by aggressive manoeuvre; Superior Firepower sends shells not men; Grand Battleplan wins through meticulous preparation; Mass Assault concentrates numerical superiority.

## Track milestones (fire when a track is fully mastered)

These are the payoffs that differ by Grand Doctrine. Read the row for your Grand Doctrine.

| Grand Doctrine | Infantry milestone | Artillery & Combat Support milestone | Armor milestone | Operations milestone |
|---|---|---|---|---|
| **Mobile Warfare** | Org Loss when Moving: -15%<br>Reinforce Rate: +2%<br>Enables tactic: **Delay** | Org Loss when below 25%: -10%<br>Planning Speed: +10%<br>Enables tactic: **Overwhelming Fire** | **Brigade Size: +1**<br>Enables tactic: **Blitz** | Planning Speed: +20%<br>Regimental Support Companies: Breakthrough: +10%, Organization: +10<br>Enables tactic: **Backhand Blow** |
| **Superior Firepower** | Supply Consumption: -10%<br>Enables tactic: **Elastic Defense** | **Brigade Size: +1**<br>Plan Preparation Decay Rate: -10%<br>Support companies: Organization: +10<br>Enables tactic: **Suppressive Barrage** | Army Recovery Rate: +0.10<br>Regimental Support Companies: Soft Attack: +5%, Hard Attack: +5%<br>Enables tactic: **Delay** | Plan Preparation Decay Rate: -10%<br>Army Recovery Rate: +0.20<br>Enables tactic: **Tactical Withdrawal** |
| **Grand Battleplan** | Max Entrenchment: +5%<br>**Brigade Size: +1**<br>Enables tactic: **Elastic Defense** | Coordination: +10%<br>Regimental Support Companies: Defense: +10%, Entrenchment: +20%<br>Enables tactic: **Overwhelming Fire** | Reinforce Rate: +2%<br>Enables tactic: **Breakthrough** | Maximum Command Power Increase: +30<br>Coordination: +10%<br>_(no tactic — the only milestone that grants none)_ |
| **Mass Assault** | **Brigade Size: +1**<br>Regimental Support Companies: Recovery Rate: +0.10, Supply Use: +0.02<br>Enables tactic: **Mass Charge** | Non-Combat Out of Supply Penalties: -5%<br>Minimum Training Level: -5%<br>Enables tactic: **Elastic Defense** | Reinforce Rate: +2%<br>Enables tactic: **Overwhelming Fire** | Entrenchment Speed: +5%<br>Minimum Training Level: -5%<br>Weekly War Support (Combat Casualties): +0.10%<br>Enables tactic: **Backhand Blow** |

Which track carries the **Brigade Size +1** milestone is the key branching decision:

| Grand Doctrine | Brigade Size +1 comes from |
|---|---|
| Mobile Warfare | Armor track |
| Superior Firepower | Artillery & Combat Support track |
| Grand Battleplan | Infantry track |
| Mass Assault | Infantry track |

## Subdoctrines

One active per track. Base effects apply the moment the subdoctrine is picked; the numbered milestones unlock at cumulative Mastery thresholds.

> Note on notation: the wiki also shows, for percentage modifiers, the resulting absolute value on each equipment tier (e.g. "Breakthrough: 2.2 (+0.2)"). Those per-tier readouts are omitted here — the percentage is the modifier that is actually applied. Percentages apply to **base equipment stats** unless stated as a unit-level or country-level modifier.

### Infantry track

Gains Mastery from all Infantry & Mot/Mech (1.0× rate).

#### Mobile Infantry
Keep pace, avoid positional fighting.
**Base:** Enables tactic: Overwhelming Fire · 1× 50% research bonus for Truck · All Infantry & Mot/Mech: Breakthrough +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Modernized Cavalry | Mounted Infantry: Breakthrough +20% |
| 200 | Infiltration | All Infantry & Mot/Mech: Organization +10, Max speed +5% |
| 300 | First Strike Operations | Motorized & Mechanized Infantry: Organization +20 · Infantry Guns and Rocket Battery: Soft Attack +15% |
| 400 | Delegated Authority | Motorized & Mechanized Infantry: Recovery Rate +0.10, Soft Attack +10% |
| 500 | Maneuver Warfare | Motorized Heavy Weapons Company: Soft Attack +10%, Organization +5 · All Infantry & Mot/Mech: Organization +10, Max speed +20% |

#### Defensive Postures
Stubbornly hold ground, inflict casualties and delay.
**Base:** Mounted Infantry: Supply Use -0.01 · All Infantry & Mot/Mech: Entrenchment +20%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Improvised Fighting Positions | Entrenchment speed +5% · Heavy Weapons Company: Soft Attack +20%, Supply Use -0.01 |
| 200 | Outpost Line | All Infantry & Mot/Mech: Organization +10, Defense +10% |
| 300 | Strongpoint Network | All Infantry & Mot/Mech: Entrenchment +20% |
| 400 | Interlocking Fields of Fire | All Infantry & Mot/Mech: Soft Attack +10% · Infantry Guns and Rocket Battery: Soft Attack +20% |
| 500 | Infantry Engineer Training | Entrenchment speed +15% |

#### Large Unit Tactics
Concentrated operations on a narrow front to create local superiority.
**Base:** All Infantry & Mot/Mech: Supply Use -0.01

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Overnight Entrenchment | Entrenchment speed +10% |
| 200 | Flexible Division Structures | Infantry Unit Design Cost: -100% · Infantry: Combat width 1.7 (-0.3) |
| 300 | Unit Knowledge Sharing | All Infantry & Mot/Mech: Exp. loss -1% |
| 400 | Large Front Offensive | Division Recovery Rate +0.1 · Heavy Weapons Company: Breakthrough +10% · All Infantry & Mot/Mech: Organization +10, Soft Attack +10% · Infantry Guns and Rocket Battery: Soft Attack +10% |
| 500 | Motorization Initiative | All Infantry & Mot/Mech: Breakthrough +10%, Soft Attack +10% · Motorized & Mechanized Infantry: Supply Use -0.02, Reliability +10% |

#### Assault Infantry
Combined arms with organic fire support down to the smallest unit.
**Base:** Support Artillery: Soft Attack +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Low Echelon Fire Support | Support Artillery → Leg Infantry battalions: Soft Attack +20% · Infantry Guns: Soft Attack +20% |
| 200 | Infiltration | Anti-Tank Battery: Hard Attack +10%, Piercing +10% · Anti-Air Battery: Air Attack +10% · Infantry Guns and Rocket Battery: Soft Attack +10% |
| 300 | Infantry Forward Observer Training | Support Anti-Tank: Hard Attack +5%, Organization +20, Piercing +5% · Support Anti-Air: Air Attack +5%, Organization +20 · Support Artillery: Soft Attack +5%, Organization +20 |
| 400 | Recon Pull | Armored Recon Company: Organization +20; and → All Infantry & Mot/Mech battalions: Organization +5, Breakthrough +20% · Motorized Recon Company: Organization +20; and → All Infantry & Mot/Mech battalions: Breakthrough +10%, Organization +5 |
| 500 | Assault Detachments | Light/Medium/Heavy Flame Tank Company → All Infantry & Mot/Mech battalions: Breakthrough +10%, Soft Attack +10% · Support Artillery: Supply Use -0.02 · Infantry Guns and Rocket Battery: Supply Use -0.01 |

#### Mounted Infantry
Modernised cavalry: mounted mobility, dismounted fighting with heavy weapons.
**Base:** Cavalry Unit Design Cost: -100% · Mounted Infantry: Soft Attack +10%, Breakthrough +10%
**Special:** this subdoctrine gains Mastery from a specific set of units — Mounted Infantry and All Infantry & Mot/Mech.

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Dragoon Traditions | Mounted Infantry: Defense +10%, Breakthrough +20% |
| 200 | Regimental Scout Troop | Cavalry Recon Detachment: Soft Attack +20%, Organization +10 · Leg Infantry battalions: Soft Attack +10%, Defense +10%, Organization +5 · Mounted Infantry: Organization +5 |
| 300 | Anti-Mechanized Cavalry Groups | Mounted Infantry: Hard Attack +20%, Piercing +20% |
| 400 | Beasts of War | Cavalry Recon Detachment: Max speed +50% · Mounted Infantry: HP +5%, Max speed +50% (Cavalry 9.6 km/h, Camelry 8.4 km/h, Elephantry 9 km/h) |
| 500 | Limbered Combat Support | Artillery / Anti-Tank / Anti-Air / Rocket Artillery: Max speed +50% (to 6 km/h) |

#### Individual Excellence
"Every Man An Emperor" — individually capable troops.
**Base:** Enables tactic: Infiltration Assault · Logistics Company → Leg infantry battalions: HP +5

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Isolated Combat Elements | Field Hospital / Helicopter Brigade / Helicopter Field Hospital: Trickleback and War Support Protection +5% · Leg Infantry: Supply Use -0.01, Reliability +5% · Infantry Guns and Rocket Battery: Soft Attack +5%, Supply Use -0.01 |
| 200 | Dispersed Element Coordination | Signal Company → All Infantry & Mot/Mech battalions: Defense +10% · Logistics Company → Motorized & Mechanized Infantry battalions: HP +5 · Motorized & Mechanized Infantry: Breakthrough +10%, Reliability +5% |
| 300 | Rigorous Training Regime | Cavalry/Motorized/Armored Recon Companies → All Infantry & Mot/Mech battalions: Soft Attack +10% · Anti-Tank Battery → Leg Infantry battalions: Hard Attack +10% · Infantry in Desert / Jungle / Hills: Movement +10%, Attack +5% |
| 400 | Field Intelligence Gathering | Intelligence gained from Combat: +15% |
| 500 | Integrated Assaults | Heavy Weapons Company: Breakthrough +15% · Motorized Heavy Weapons Company: Breakthrough +15% · All Infantry & Mot/Mech: Breakthrough +10%, Soft Attack +10% · Infantry Guns and Rocket Battery: Breakthrough +15% |

#### Irregulars
Asymmetric infantry warfare — ambush, misdirection, harassment.
**Base:** Irregular Infantry: Defense +10%, Supply Use -0.05 · Militia: Supply Use -0.01, Defense +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Service By Lot | Mobilization Speed +5% |
| 200 | Partisan Regiments | Irregular Infantry: Combat width 1.6 (-0.4) · Militia: Combat width 1.6 (-0.4) · Leg Infantry: Defense +10% |
| 300 | Improvised Officer Groups | Leg Infantry: Organization +10, Breakthrough +10%, Soft Attack +10% |
| 400 | Levée En Masse | Mobilization Speed +5% · Recruitable population +2% |
| 500 | Standardization Efforts | 2× 50% research bonus for Support technology · Leg Infantry: Organization +10, Soft Attack +10% |

#### People's Militia
**Available only with Communism.** State-mobilised popular resistance.
**Base:** Enables tactic: Guerrilla Tactics · Militia: Soft Attack +10%, Defense +20%
**Cheaper milestones:** 50 / 100 / 200 / 250 Mastery, and only four of them.

| Mastery | Milestone | Effects |
|---|---|---|
| 50 | Revolutionary Base Area | Militia: Supply Use -0.02, Defense +10% · Leg Infantry: Organization +5 |
| 100 | Destruction over Land Gains | Militia: Eq. Capture Ratio +1% · Infantry Guns: Soft Attack +15% · Leg Infantry: Recovery Rate +0.10 |
| 200 | Quick Decision Offensive Warfare | Militia: Initiative +1%, Organization +10, Breakthrough +20% |
| 250 | People, not Things | Leg Infantry: HP +15%, Soft Attack +10% |

#### Great War Infantry
Limited-objective attacks followed by rapid entrenchment.
**Base:** Land Fort construction speed +25% · Mounted Infantry: Supply Use -0.02 · Leg Infantry: Defense +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Zig-zag Trenches | Entrenchment speed +5% · Heavy Weapons Company: Defense +10%, Soft Attack +10% · Engineer Company → Leg Infantry battalions: Entrenchment +0.05 |
| 200 | Communication Trenches | Field Hospital: Trickleback and War Support Protection +10% · Leg Infantry: Defense +10% |
| 300 | Creeping Barrages | Support Artillery: Soft Attack +10% · Leg Infantry battalions: Soft Attack +10%, Breakthrough +5% · Infantry Guns and Rocket Battery: Soft Attack +20% |
| 400 | Overhead Cover | Leg Infantry: Organization +5, Defense +5%, Reliability +5% |
| 500 | Redoubt Networks | Entrenchment speed +10% |

### Artillery & Combat Support track

Gains Mastery from Line Artillery, Support Artillery and Support Companies (10.0× rate — the fastest-filling track).

#### Fire Concentration
Centralised control of fire support assets.
**Base:** Enables tactic: Overwhelming Fire · Line Artillery: Organization +5, Defense +5%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Predicted Fire | Line Artillery: Defense +5% |
| 200 | Prepared Gun Pits | Line Artillery: Combat width 2.2 (-0.8) · Rocket Artillery: Combat width 2.2 (-0.8) |
| 300 | Battery Local Security | Infantry Guns and Rocket Battery: Breakthrough +10%, Soft Attack +5% · Support Artillery: Breakthrough +10%, Soft Attack +5% · Line Artillery: Breakthrough +10%, Soft Attack +5% |
| 400 | Centralized Anti-Aircraft Support | Anti-Air Battalions: Air Attack +10% |
| 500 | Flanking Fire Emplacement | Anti-Tank: Hard Attack +10%, Piercing +10% · Artillery: Soft Attack +10% · Rocket Artillery: Soft Attack +10% |

#### Anti-Tank Frontline
Unified anti-tank defence, kill zones, flank protection.
**Base:** Engineer Company → Line Artillery battalions: Entrenchment +0.20

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Pakfront | Anti-Tank: Piercing +10% · Anti-Tank Battery: Hard Attack +20%, Piercing +20% |
| 200 | Emplacement Rotation | Anti-Tank: Organization +10, Defense +20% |
| 300 | Weak-point Studies | Anti-Tank: Soft Attack +20%, Hard Attack +10%, Piercing +10% |
| 400 | Offensive Deployment | Motorized Anti-Tank: Breakthrough +20%, Piercing +20% |
| 500 | Direct Fire Bunker-Busting | Motorized Anti-Tank: Soft Attack +20%, Hard Attack +20% |

#### Flying Batteries
Mobility for supporting arms so they keep pace with motorised advances.
**Base:** 1× 50% research bonus for Rocketry technology · Line Artillery: Soft Attack +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Deployment Drills | Truck-drawn Rocket Artillery / Motorized Rocket Artillery / Motorized Artillery battalions: Organization +10 · Motorized Heavy Weapons Company: Soft Attack +10%, Organization +10 |
| 200 | Counter-battery Tasks | Cavalry Recon Detachment / Motorized Recon Company: Reconnaissance +0.25 · Line Artillery battalions: Soft Attack +5%, Defense +10% |
| 300 | Armored Forward Observer Vehicles | Armored Signal Company → Line Artillery battalions: Supply Use -0.01, Initiative +2% |
| 400 | Fast Unlimbering | Line Artillery: Recovery Rate +0.05, Breakthrough +5% |
| 500 | Widely Dispersed Batteries | Truck-drawn Rocket Artillery / Motorized Rocket Artillery / Motorized Artillery battalions: Organization +10 |

#### Air Cavalry
**Requires the Helicopter Special Project.**
**Base:** 2× 50% research bonus for Helicopters

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Heliborne Observers | Helicopter Recon Company: Organization +10 · Artillery Support & Line battalions: Soft Attack +10% |
| 200 | Service & Support | Helicopter Support Companies: HP +3% |
| 300 | Rescue Liaisons | Helicopter Field Hospital: Trickleback and War Support Protection +5%, Organization +5 · All Infantry & Mot/Mech battalions: HP +5%, Recovery Rate +5% |
| 400 | Transport-Assault | Helicopter Transports: Breakthrough +5%, Organization +10 · Leg Infantry battalions: Max speed +20%, Breakthrough +5% |
| 500 | Intervention Units | Helicopter Brigade: Organization +10 · All Infantry & Mot/Mech battalions: Soft Attack +10% |

#### Mobile Recon & Assault
Recon finds the enemy, mobile heavy weapons smash them.
**Base:** Armored Car: Organization +3 · Light Tank: Organization +5

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Organic Motorized Supply | Motorized Heavy Weapons Company: Soft Attack +10%, Organization +10 · Mobile Battalions & Combat Support: Recovery Rate +0.10, Max speed +10% |
| 200 | Long Range Reconnaissance | Recon: Max speed +15% |
| 300 | Mobile Operational Deployment | Armored Recon Company → Tanks & Armor Variants battalions: Breakthrough +10% · Motorized Artillery: Soft Attack +5% |
| 400 | Fire On The Move | Armored Car: Recovery Rate +0.20, Breakthrough +20% · Self-Propelled Artillery: Soft Attack +10% · Self-Propelled Anti-Air: Soft Attack +5%, Air Attack +15% · Tank Destroyers: Hard Attack +10%, Piercing +3% |
| 500 | Deep Reconnaissance Focus | Armored Recon Company: Breakthrough +10%, Reconnaissance +20% · Recon: Max speed +10% · Tank Destroyer Regimental Support: Breakthrough +20% · Self-Propelled Anti-Air Regimental Support: Breakthrough +20% |

#### Self-propelled Support
Tracked mobility and protection for heavy support weapons.
**Base:** Self-Propelled Artillery: Soft Attack +10% · Self-Propelled Anti-Air: Air Attack +10% · Tank Destroyers: Hard Attack +5%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Mobile Fire Direction Center | Self-Propelled Artillery / Self-Propelled Anti-Air / Tank Destroyers: Organization +10 |
| 200 | Time-On-Target Fire Missions | Recon / Motorized Recon / Armored Recon Companies → Self-Propelled Artillery battalions: Soft Attack +10%, Recovery Rate +10% |
| 300 | All-terrain Mobility | Self-Propelled Artillery / Self-Propelled Anti-Air / Tank Destroyers: Max speed +30% |
| 400 | Multi-role Support Vehicles | Tank Destroyer Regimental Support: Breakthrough +20%, Hard Attack +10%, Organization +10 · Self-Propelled Anti-Air Regimental Support: Breakthrough +20%, Hard Attack +10%, Organization +10 |
| 500 | Shoot & Scoot | Self-Propelled Artillery / Self-Propelled Anti-Air: Recovery Rate +0.15, Soft Attack +5%, Organization +5 · Tank Destroyers: Recovery Rate +0.15, Hard Attack +5%, Organization +5 |

#### Siege Artillery
**Requires the Super-heavy Howitzer Special Project.**
**Base:** Railway Artillery / Super-Heavy Railway Gun: Bombardment +25% · Super-Heavy Artillery battalion → Army battalions: Soft Attack +10%, Defense +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Fortress Busters | Super-Heavy Artillery / Self-Propelled Super-Heavy Artillery: Fort attack +25% |
| 200 | Improved Transport Preparation | Railway Gun / Super-Heavy Railway Gun: Hours between redistribution -50% · Super-Heavy Artillery / SP Super-Heavy Artillery: Plains movement +10% · Line Artillery: Recovery Rate +0.10 |
| 300 | Pre-computed Firing Data | Super-Heavy Artillery / SP Super-Heavy Artillery: Organization +10, Defense +20% |
| 400 | Advanced Fire Correction | Super-Heavy Artillery / SP Super-Heavy Artillery: Urban attack +20% · Heavy Weapons Company: Soft Attack +10% · Artillery Support & Line: Soft Attack +5% · Infantry Guns and Rocket Battery: Soft Attack +10% |
| 500 | Mobile Artillery Command | Railway Gun / Super-Heavy Railway Gun: Max speed +100% · Self-Propelled Super-Heavy Artillery: Organization +10, Max speed +50% · Support Artillery: Organization +10 |

#### Field Engineering
Bridging, mining, demolition — sweat to spare blood.
**Base:** Engineer / Assault Engineer / Pioneer Support Companies: River movement +20%, Forest movement +20%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Rapid Fire Lane Clearance | Engineer Company: Organization +5; → All Infantry & Mot/Mech battalions: Entrenchment +0.10 · Maintenance Company: Organization +5 |
| 200 | Sapper Fieldcraft | Engineer Company: Defense +10%, HP +25% · Maintenance Company: HP +25% |
| 300 | Engineer-dug Gun Emplacements | Engineer Company → Artillery Support & Line battalions: Soft Attack +10%, Defense +10%; → All Infantry & Mot/Mech battalions: Soft Attack +5% · Infantry Guns: Defense +10%, Soft Attack +10% |
| 400 | Smoke Projector Training | Engineer Company: Breakthrough +50% · Maintenance Company: Supply Use -0.01 · Tanks battalions: Reliability +5% |
| 500 | Flames & Satchel Charges | Engineer Company: Soft Attack +5%, Hard Attack +100%, Organization +5 · Maintenance Company: Organization +5 · Heavy Weapons Company: Breakthrough +10%, Organization +5 |

### Armor track

Gains Mastery from Armored Car and Tanks & Armor Variants (4.0× rate).

#### Armored Spearhead
Rapid exploitation of breakthroughs to encircle and destroy.
**Base:** Enables tactic: Breakthrough

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Point of Main Effort | Tanks: Recovery Rate +0.05, Organization +2 |
| 200 | Breakthrough Exploitation | Tanks & Armor Variants: Breakthrough +10% |
| 300 | Local Reserves | Armored Car: Recovery Rate +0.10, Organization +7 · Light Tank: Recovery Rate +0.10, Organization +3 · Self-Propelled Anti-Air Regimental Support: Air Attack +5%, Organization +10 |
| 400 | Strong Point Bypassing | Tanks & Armor Variants: Breakthrough +10% |
| 500 | Flank Protection | Armored Car: Recovery Rate +0.20, Organization +3, Breakthrough +20% · Tanks: Breakthrough +20%, Organization +3 |

#### Armored Infantry Support
Seamless tank-infantry cooperation.
**Base:** Enables tactic: Blitz · 1× 100% research bonus for Heavy Tank models

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Assault Overrun | Medium Tank: Breakthrough +5%, Soft Attack +10% · Heavy Tank: Breakthrough +5%, Soft Attack +10% |
| 200 | Armored Cohorts | Medium Tank: Organization +5 · Heavy Tank: Organization +5 · Tank Destroyer Regimental Support: Organization +5, Piercing +10% |
| 300 | Maintenance Routines | Armored Maintenance Company → Tanks & Armor Variants battalions: HP +0.15 |
| 400 | Fuel Rationing | Heavy Tank: Supply Use -0.08 |
| 500 | Mobile Armored Strongpoints | Heavy Tank: Breakthrough +10% · Heavy SP Anti-Air Support: Air Attack +10%, Organization +5 · All Infantry & Mot/Mech: Breakthrough +5% |

#### Streamlined Deployment
Mass all arms, including tanks, at the decisive point.
**Base:** Tanks & Armor Variants: Soft Attack +10%, Breakthrough +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Army Mechanization Drive | Light Tank Unit Design Cost -50% · Medium Tank Unit Design Cost -50% · Armored Recon Company → Tanks & Armor Variants battalions: Organization +2 |
| 200 | Mechanized Wave | Mechanized: Recovery Rate +0.10, Organization +5 · Tanks & Armor Variants: Recovery Rate +0.05 |
| 300 | Tank Desant | Armored Signal Company → Leg Infantry battalions: Max speed +5% · Armored Recon Company → Leg Infantry battalions: Max speed +5% |
| 400 | Austere Logistics | Tanks & Armor Variants: Supply Use -0.02, Reliability +5% |
| 500 | Continuous Offensives | Tanks & Armor Variants: Recovery Rate +0.05, Breakthrough +10%, Organization +3 |

#### Mobile Defense
Armour occupies defensive terrain fast and counters breakthroughs.
**Base:** Armored Engineer Company → Tanks & Armor Variants battalions: Entrenchment +0.02 · Tanks & Armor Variants: Defense +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Battle Taxis | Mechanized Infantry: Defense +10%, Soft Attack +10% |
| 200 | Advance Under Fire | Light Tank: Recovery Rate +0.20, Breakthrough +10% · Medium Tank: Recovery Rate +0.10, Breakthrough +10% |
| 300 | Tracked Combat Support | Assault Engineer Company: Organization +10 · Armored Engineer Company: Organization +10 · Armored Signal Company: Organization +10 · Self-Propelled Anti-Air Regimental Support: Air Attack +5%, Organization +10 |
| 400 | Combined Anti-armor | Support Anti-Tank → Tanks & Armor Variants battalions: Hard Attack +5%, Piercing +5% · Tank Destroyer Regimental Support: Hard Attack +5%, Organization +5, Piercing +15% |
| 500 | Tank-on-Tank Engagement | Tanks & Armor Variants: Soft Attack +10%, Hard Attack +10%, Piercing +5% |

#### Armored Cavalry
Mechanised forces with fast light tanks and armoured cars probing for weak spots.
**Base:** Armored Car: Organization +5, Defense +10% · Mechanized: Organization +5, Defense +5%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Cruiser Tanks | Light Tank: Breakthrough +5%, Organization +5, Max speed +10% |
| 200 | Motorized Security Forces | Motorized Military Police → Motorized & Mechanized Infantry battalions: Suppression Bonus +5% · Armored Car battalion: Suppression Bonus +20% |
| 300 | Speed as Armour | Light Tank: Breakthrough +5%, Max speed +5% · Armored Car: Breakthrough +10%, Soft Attack +10%, Max speed +5% · Mechanized Infantry: Breakthrough +5%, Max speed +5% |
| 400 | Fighting Reconnaissance | Light Armored Recon Company: Soft Attack +5%, Organization +3 · Armored Recon Company: Soft Attack +5%, Organization +2 · Anti-Tank Battery: Piercing +10% · Motorized Heavy Weapons Company: Recovery Rate +0.10, Soft Attack +5%, Organization +5 |
| 500 | External Stowage | Armored Car: Recovery Rate +0.20, Organization +5, Soft Attack +5% · Light Tank: Recovery Rate +0.15, Soft Attack +5%, Hard Attack +10%, Organization +5 · Mechanized / Motorized Infantry: Recovery Rate +0.10, Organization +5, Soft Attack +5% |

#### Tank Destroyer Force
Defence in depth by ambushing anti-tank units.
**Base:** Tanks & Armor Variants: Defense +10%, Hard Attack +10%, Piercing +10%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Mobile Anti-Tank Reserves | Motorized Anti-Tank: Organization +8, Hard Attack +10%, Piercing +10% |
| 200 | Organic Combat Engineer Platoons | Assault Engineer Company → Tank Destroyers battalions: Reliability +2%, Soft Attack +5%, Hard Attack +10% |
| 300 | Rapid Riposte | Tank Destroyers: Recovery Rate +0.10, Supply Use -0.02 |
| 400 | Independent Counterattacks | Tank Destroyers: Initiative +1%, Organization +6 |
| 500 | Radio-Directed Breakthrough Containment | Armored Signal Company → Tank Destroyers battalions: Hard Attack +10%, Piercing +10% · Tank Destroyer Regimental Support: Hard Attack +10%, Organization +5, Piercing +10% |

### Operations track

Gains Mastery from All Infantry & Mot/Mech, Line Artillery, Support Artillery and Tanks & Armor Variants (0.7× rate — slowest, but fed by nearly everything).

#### Mission-Type Tactics
Auftragstaktik — leaders interpret orders intelligently.
**Base:** Daily Command Power Gain +0.02 · All Infantry & Mot/Mech: Organization +15

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Low-level Delegation | All Infantry & Mot/Mech: Recovery Rate +0.10 · Infantry Guns and Rocket Battery: Soft Attack +5%, Organization +5 |
| 200 | Flexible Command | Org Loss when Moving -15% |
| 300 | Combined Arms Battle Groups | Reinforce Rate +0.20 · Tanks & Armor Variants: Max speed +10% |
| 400 | Offensive Posture | All Infantry & Mot/Mech: Organization +10, Breakthrough +10% |
| 500 | Control Zone Responsibilities | All Infantry & Mot/Mech: Recovery Rate +0.20 · Tanks: Recovery Rate +0.10 |

#### Desperate Defense
**Requires a defensive war.** Total national resistance.
**Base:** Recruitable population +5%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Sabotage Groups | Damage to Enemy Garrisons in our states occupied by the enemy: +25% |
| 200 | Pocket Consolidation | All Infantry & Mot/Mech: Defense +10% |
| 300 | Trench-Huddling | Non-Combat Out of Supply Penalties -20% · All Infantry & Mot/Mech: Entrenchment +10% |
| 400 | Supply Cache Retrieval | Supply Grace +72 hours |
| 500 | Final Offensive | Army: Soft Attack +15% · Infantry Guns and Rocket Battery: Soft Attack +10%, Organization +5 |

#### Infiltration Tactics
Flow around strongpoints, keep momentum, threaten encirclement.
**Base:** Max planning +5% · Enables tactic: Infiltration Assault

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Infiltration Assault | Heavy Weapons Company: Soft Attack +10% · Army: Breakthrough +10%, Organization +5 |
| 200 | Attacks At Night | Land Night Attack +25% |
| 300 | Self-sustaining Infiltration Units | Supply Consumption -10% · Daily Command Power Gain +0.01 · Tanks: Organization +2 · Tanks & Armor Variants: Recovery Rate +0.10 |
| 400 | Terrain and Situation Assessment | Cavalry / Motorized / Armored Recon Companies → Leg Infantry battalions: Soft Attack +10%; Mounted Infantry battalions: Soft Attack +10% · Recon: Reconnaissance +100% |
| 500 | Infiltration in Depth | Org Loss when Moving -20% · Reinforce Rate +2% |

#### Grand Assault
Deliberate, methodical pre-battle planning, then an avalanche.
**Base:** Max planning +10% · Army: Breakthrough +10%, Soft Attack +5%

| Mastery | Milestone | Effects |
|---|---|---|
| 100 | Central Planning | Maximum Command Power Increase +30 · Logistics Company → All Infantry & Mot/Mech battalions: Defense +5% |
| 200 | Diversionary Attacks | Heavy Weapons Company: Soft Attack +10% · Army: Breakthrough +15% |
| 300 | Combined Arms Integration | Air Superiority +5% · Coordination +10% · Anti-Air Battery: Air Attack +10%, Organization +5 · Motorized Heavy Weapons Company: Soft Attack +10%, Organization +5 · Tank Destroyer Regimental Support: Organization +5 |
| 400 | Forward Command Posts | Logistics Company → All Infantry & Mot/Mech battalions: Supply Use -0.01 · Recon: Reconnaissance +10% |
| 500 | C3I | Max planning +10% · All Infantry & Mot/Mech: Organization +8 |

## Choosing a Grand Doctrine — which suits which playstyle

**Inferred** unless a value is quoted from the tables above.

| Grand Doctrine | Core strength | Best for | Weak for |
|---|---|---|---|
| **Mobile Warfare** | +10% division speed, +20% planning speed, Brigade Size +1 on the **Armor** track, Org-loss-when-moving -15% and Reinforce Rate +2% on Infantry, Blitz tactic | Tank-led encirclement play. Germany, Soviet late-game, any nation whose armour actually fights (Armor Mastery accrues at 4.0×). The speed bonus compounds with the Armor milestones' Breakthrough stacking. | Nations that cannot afford tanks — the Brigade Size milestone is locked behind armour combat, so infantry-only countries get very little. |
| **Superior Firepower** | Line Artillery Soft Attack +10% and Support Company Soft Attack +5% baseline; Brigade Size +1 on the **Artillery & Combat Support** track (the 10.0× Mastery track, i.e. the easiest one to master); Army Recovery Rate +0.10/+0.20; Supply Consumption -10% on Infantry | The default "strong divisions" pick. Artillery-heavy infantry or armour-plus-artillery. USA, UK, anyone with the industry for line artillery. Fastest route to Brigade Size +1 because the track gains Mastery at 10.0×. | Very poor-industry nations that cannot field artillery — no artillery battalions means almost no Mastery in the track that carries your Brigade Size bonus. |
| **Grand Battleplan** | Max planning +10%, Daily Command Power +0.25, Maximum Command Power +30, Coordination +10% (twice), Max Entrenchment +5%, Brigade Size +1 on the **Infantry** track | Battle-plan/AI-assisted offensives, wide fronts, low micromanagement. Command-power-hungry countries (lots of army spirits/orders). Infantry-heavy nations get Brigade Size from the track that fills from ordinary infantry combat. | Players who micromanage attacks manually — planning bonus decays and is wasted. It is also the only doctrine whose Operations milestone grants **no tactic**. |
| **Mass Assault** | Out-of-supply penalty -10% (-5% more), Supply Grace +48h (+72h from Desperate Defense), Minimum Training Level -5% twice, Brigade Size +1 on the **Infantry** track, weekly war support from casualties | Huge manpower, poor logistics: Soviet Union, China, any nation fighting deep into low-supply territory or surviving on cheap infantry. Pairs naturally with Irregulars / People's Militia / Desperate Defense. | Small-manpower, high-quality armies — none of the supply/training bonuses compensate for the lack of direct attack modifiers. |

### Subdoctrine picks by playstyle

| Goal | Infantry | Artillery & Combat Support | Armor | Operations |
|---|---|---|---|---|
| Armoured breakthrough | Mobile Infantry | Mobile Recon & Assault or Self-propelled Support | Armored Spearhead or Streamlined Deployment | Mission-Type Tactics |
| Infantry line-holding / defence | Defensive Postures or Great War Infantry | Anti-Tank Frontline | Mobile Defense or Tank Destroyer Force | Desperate Defense (only in a defensive war) |
| Artillery-heavy infantry offensive | Assault Infantry | Fire Concentration | Armored Infantry Support | Grand Assault |
| Cheap mass infantry / minor nation | Irregulars (or People's Militia if communist) | Field Engineering | Armored Cavalry | Infiltration Tactics |
| Cavalry-era or low-industry army | Mounted Infantry | Field Engineering | Armored Cavalry | Infiltration Tactics |
| Late-game / special-project tech | Individual Excellence | Air Cavalry (needs Helicopter project) or Siege Artillery (needs Super-heavy Howitzer project) | Mobile Defense | Grand Assault |
| Narrow-front concentration, cheap templates | Large Unit Tactics (Infantry Unit Design Cost -100%, Infantry combat width 1.7) | Fire Concentration (Line Artillery combat width 2.2) | Streamlined Deployment (Light/Medium Tank Design Cost -50%) | Mission-Type Tactics |

### Practical notes

- **Free-template subdoctrines:** Large Unit Tactics milestone 200 gives *Infantry Unit Design Cost: -100%*, Mounted Infantry's base gives *Cavalry Unit Design Cost: -100%*, Streamlined Deployment milestone 100 gives *Light/Medium Tank Unit Design Cost: -50%*. These remove/reduce the army-XP price of editing templates and are worth taking early if you iterate templates a lot.
- **Combat-width changers:** Fire Concentration 200 (Line Artillery and Rocket Artillery to 2.2), Large Unit Tactics 200 (Infantry to 1.7), Irregulars 200 (Irregular Infantry and Militia to 1.6). Recheck division widths against terrain after unlocking these.
- **Ideology/state gates:** People's Militia requires Communism; Desperate Defense requires being in a defensive war; Air Cavalry requires the Helicopter special project; Siege Artillery requires the Super-heavy Howitzer special project.
- **Do not switch Grand Doctrine mid-war** — all land Mastery is wiped, meaning every subdoctrine milestone must be re-earned.

## See also

- [Special forces doctrine](special-forces-doctrine.md)
- [Tank designer](tank-designer.md)
- [Armor technology](armor-technology.md)
- [Infantry and support company technology](infantry-and-support-technology.md)
- [Artillery technology](artillery-technology.md)
