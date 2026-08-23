---
title: Armor Technology
category: land-warfare
tags: [armor, tanks, technology, research, chassis, tank-destroyer, self-propelled-artillery, spaa, no-step-back, land-cruiser]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Armor_technology
  - https://hoi4.paradoxwikis.com/Armor_technology_(Basic)
---

## Summary

There are **two completely different armor research trees**. With **No Step Back** the tree unlocks *chassis and modules* for the [tank designer](tank-designer.md); without it, the legacy tree unlocks *fixed equipment models* (Light Tank I/II/III and so on) directly. Both are documented here. Base research times are given in days before research-speed modifiers; years are the historical unlock years used for the ahead-of-time penalty.

## Which tree applies

| Situation | Tree |
|---|---|
| **No Step Back** enabled | NSB chassis-and-module tree (below) — Inter-War Tank Development → Light/Medium/Heavy chassis lines, plus Armor/Engine upgrade lines |
| No Step Back **not** enabled | Legacy tree — Great War Tank → Light/Medium/Heavy Tank I–III, with parallel Tank Destroyer, SP Artillery and SP Anti-Air variant lines |

> Note on production costs: the NSB chassis tables on the *Armor technology* page quote the production cost of the **whole default design** (chassis plus the default engine/armor/suspension/turret/gun), while the [tank designer](tank-designer.md) page quotes the **chassis module's own** cost. Both are reproduced faithfully; e.g. the Basic Light Tank Chassis module costs 2.35, and the default design built on it costs 3.48.

---

## Part 1 — No Step Back armor technology (chassis and modules)

## Root technology

| Technology | Year | Base time | Prerequisites | Unlocks |
|---|---|---|---|---|
| **Inter-War Tank Development** | 1918 | 220 days | – | Inter-War **Light**, **Medium** and **Heavy** Tank Chassis, plus the Light Tank, Medium Tank and Heavy Tank battalion types and a large set of basic armored-vehicle modules |

Default designs on the three inter-war chassis:

| Chassis | Resources | Service MP | Breakthrough | Max Speed | Reliability | Prod. Cost | Defense | Hardness | Armor | Fuel Usage |
|---|---|---|---|---|---|---|---|---|---|---|
| Inter-War Light Tank Chassis | 1 Steel | 2 | 9.0 | 5.1 km/h | 80% | 3.20 | 2.0 | 80% | 10.0 | 2.00 |
| Inter-War Medium Tank Chassis | 1 Steel | 2 | 10.0 | 5.1 km/h | 75% | 4.60 | 2.0 | 85% | 20.0 | 2.00 |
| Inter-War Heavy Tank Chassis | 1 Steel | 2 | 20.0 | 4.0 km/h | 75% | 12.00 | 2.0 | 95% | 35.0 | 2.00 |

Battalion base stats unlocked at the same time (shared with the legacy tree):

| Battalion | Manpower | Recovery | Supply Use | Org | Weight | Training | Equip. Breakthrough | Suppression | HP |
|---|---|---|---|---|---|---|---|---|---|
| Light Tank | 500 | 0.30 | 0.22 | 10 | 1.0 | 180 | +10% | 2.5 | 2.0 |
| Medium Tank | 500 | 0.30 | 0.25 | 10 | 1.2 | 180 | +10% | 2.5 | 2.0 |
| Heavy Tank | 500 | 0.30 | 0.32 | 10 | 1.5 | 180 | +10% | 2.5 | 2.0 |
| Modern Tank | 500 | 0.30 | 0.25 | 10 | 1.5 | 180 | +10% | 2.5 | 2.0 |
| Super-Heavy Tank | 500 | 0.30 | 0.40 | 10 | 1.0 | 180 | – | 2.5 | 2.0 |
| Amphibious Tank | 500 | 0.30 | 0.20 | 10 | 1.0 | 180 | – | – | 2.0 |

Terrain adjusters by battalion (Movement / Attack / Defense):

| Terrain | Light Tank | Medium Tank | Heavy Tank | Modern Tank | Super-Heavy Tank | Amphibious Tank |
|---|---|---|---|---|---|---|
| Forest | -40% / -20% / – | -40% / -30% / – | -40% / -40% / – | -40% / -30% / – | -30% / -25% / – | -40% / -20% / – |
| Hills | – | – / -10% / – | – / -20% / – | – / -10% / – | – / -15% / -15% | – |
| Mountain | – / -10% / – | – / -20% / – | – / -30% / – | – / -20% / – | – / -20% / -20% | – / -10% / – |
| Plains | – | – | – | – | – | -10% / -10% / – |
| Urban | – / -40% / -10% | – / -40% / -10% | – / -50% / -20% | – / -40% / -10% | – / -30% / -30% | – / -40% / -10% |
| Jungle | -40% / -30% / – | -40% / -40% / – | -40% / -60% / – | -40% / -40% / – | -30% / -35% / -35% | -40% / -30% / – |
| Marsh | -10% / -10% / – | -10% / -10% / – | -20% / -40% / – | -10% / -10% / – | -30% / -30% / -30% | – / **+30%** / – |
| Fort | – | – | – / **+10%** / – | – | – / **+10%** / **+5%** | – |
| River | -20% / -20% / – | -20% / -20% / – | -40% / -40% / – | -20% / -20% / – | -30% / -25% / -25% | – / **+40%** / – |
| Amphibious | – / -40% / – | – / -80% / – | – / -90% / – | – / -70% / – | – / -60% / – | – / **+60%** / – |

## Light chassis line

Unlocks chassis for Light tanks, Light SP Anti-Air, Light SP Artillery, Light Tank Destroyers, plus the Armored Recon, Light Flame Tank and (with Arms Against Tyranny) Airborne Light Armor support companies. Also the prerequisite chain for amphibious chassis and Light Amphibious Tanks. Cheap, fast and reliable, but thin armor, low breakthrough and limited armament options — best used late as combat-support vehicles rather than frontline tanks.

| Technology | Year | Base time | Prerequisites | Chassis unlocked (default design) |
|---|---|---|---|---|
| **Basic Light Tank Chassis** | 1934 | 220 days | Inter-War Tank Development | 1 Steel · MP 2 · Breakthrough 9.0 · 6.3 km/h · Reliability 95% · Cost 3.48 · Defense 2.0 · Hardness 80% · Armor 15.0 · Fuel 2.00 |
| **Improved Light Tank Chassis** | 1936 | 220 days | Basic Light Tank Chassis | 1 Steel · MP 2 · Breakthrough 9.0 · 7.4 km/h · Reliability 110% · Cost 3.76 · Defense 2.0 · Hardness 80% · Armor 20.0 · Fuel 2.00 |
| **Advanced Light Tank Chassis** | 1941 | 220 days | Improved Light Tank Chassis | 2 Steel · MP 2 · Breakthrough 9.0 · 8.6 km/h · Reliability 130% · Cost 4.00 · Defense 2.0 · Hardness 80% · Armor 25.0 · Fuel 2.00 |

## Amphibious chassis line

All amphibious tanks **count as special forces** — they benefit from special-forces bonuses and consume [special forces cap](special-forces-doctrine.md). Amphibious designs may mount heavier weapons than normal without being reclassified as an armor variant, so they keep tank-only breakthrough and tank-only doctrine bonuses.

| Technology | Year | Base time | Prerequisites | Unlocks |
|---|---|---|---|---|
| **Amphibious Tank Chassis** | 1938 | 220 days | Improved Light Tank Chassis | Amphibious Tank Chassis: 1 Steel · MP 2 · Breakthrough 9.0 · 6.3 km/h · Reliability 110% · Cost 5.20 · Defense 2.0 · Hardness 85% · Armor 15.0 · Fuel 2.00. Also the Amphibious Tank Battalion |
| **Amphibious Drive** | 1941 | 220 days | Amphibious Tank Chassis | Amphibious Drive module: Reliability -15%, Production cost +10% and +2 flat — lets Light/Medium/Heavy chassis become amphibious designs |

## Medium chassis line

Unlocks chassis for Medium tanks, Medium SP Anti-Air, Medium SP Artillery, Medium Tank Destroyers, the Medium Flame Tank support company and Medium Amphibious Tanks; leads to the Modern chassis. Mediums are usually the best stats-per-production-cost option.

| Technology | Year | Base time | Prerequisites | Chassis unlocked (default design) |
|---|---|---|---|---|
| **Basic Medium Tank Chassis** | 1938 | 220 days | Inter-War Tank Development | 1 Steel · MP 2 · Breakthrough 10.0 · 6.3 km/h · Reliability 80% · Cost 4.80 · Defense 2.0 · Hardness 85% · Armor 30.0 · Fuel 2.00 |
| **Improved Medium Tank Chassis** | 1940 | 220 days | Basic Medium Tank Chassis | 1 Steel · MP 2 · Breakthrough 10.0 · 7.4 km/h · Reliability 100% · Cost 5.00 · Defense 2.0 · Hardness 85% · Armor 40.0 · Fuel 2.00 |
| **Advanced Medium Tank Chassis** | 1943 | 220 days | Improved Medium Tank Chassis | 2 Steel · MP 2 · Breakthrough 10.0 · 7.4 km/h · Reliability 120% · Cost 5.20 · Defense 2.0 · Hardness 85% · Armor 50.0 · Fuel 2.00 |
| **Modern Tank Chassis** | 1945 | 275 days | **One of:** Advanced Medium Tank Chassis **or** Advanced Heavy Tank Chassis | 2 Steel, 1 Chromium · MP 2 · Breakthrough 26.0 · 8.6 km/h · Reliability 120% · Cost 12.00 · Defense 2.0 · Hardness 95% · Armor 65.0 · Fuel 2.00. Also unlocks the Modern Tank battalion |

## Heavy chassis line

Unlocks chassis for Heavy tanks, Heavy SP Anti-Air, Heavy SP Artillery, Heavy Tank Destroyers, the Heavy Flame Tank support company and Heavy Amphibious Tanks; leads to Super-Heavy and (with Götterdämmerung) the Land Cruiser. Also an alternative prerequisite for the Modern chassis. Peerless on the attack, but enormously expensive, slow, and heavily penalised in bad terrain.

| Technology | Year | Base time | Prerequisites | Chassis unlocked (default design) |
|---|---|---|---|---|
| **Basic Heavy Tank Chassis** | 1934 | 220 days | Inter-War Tank Development | 1 Steel · MP 2 · Breakthrough 20.0 · 6.3 km/h · Reliability 80% · Cost 12.80 · Defense 2.0 · Hardness 95% · Armor 55.0 · Fuel 2.00 |
| **Improved Heavy Tank Chassis** | 1940 | 275 days | Basic Heavy Tank Chassis | 1 Steel, 1 Chromium · MP 2 · Breakthrough 20.0 · 6.3 km/h · Reliability 110% · Cost 13.60 · Defense 2.0 · Hardness 95% · Armor 60.0 · Fuel 2.00 |
| **Advanced Heavy Tank Chassis** | 1943 | 275 days | Improved Heavy Tank Chassis | 2 Steel, 1 Chromium · MP 2 · Breakthrough 20.0 · 6.3 km/h · Reliability 120% · Cost 14.40 · Defense 2.0 · Hardness 95% · Armor 75.0 · Fuel 2.00 |
| **Super-Heavy Tank Chassis** | 1941 | 330 days | Improved Heavy Tank Chassis | Super-Heavy Tank Chassis: 3 Steel, 2 Chromium · MP 2 · Breakthrough 26.0 · 4.9 km/h · Reliability 90% · Cost 50.70 · Defense 2.0 · Armor 90.0 · Fuel 2.00.<br>Also the **Super-Heavy Cannon** module (5 Tungsten, 2 Chromium; Soft attack 35.0, Hard attack 45.0, Piercing 225.0, Max Speed -0.6 km/h, Reliability -35%, Cost 12.50), the Super-Heavy Tank battalion, and **unlocks the Land Cruiser** |

## Armor upgrade technologies

Each raises the ceiling on tank-designer armor upgrade levels (each level: Breakthrough +1.2, Armor +2.5, Max Speed -0.1 km/h, Reliability -1.5%, Production Cost +0.2, Design Cost +1 army XP; +1 Steel at level 5 and above).

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| **Basic Armor Protection** | 1935 | 110 days | – | Armor upgrade levels **5+**; unlocks **Welded Armor** (1 Chromium; Defense 4.0, Armor +30%, Breakthrough 4.0) |
| **Improved Armor Protection** | 1938 | 110 days | Basic Armor Protection | Armor upgrade levels **10+**; unlocks **Armor Skirts** (Breakthrough 3.0, Armor 3.0, Cost 0.50) |
| **Advanced Armor Protection** | 1941 | 110 days | Improved Armor Protection | Armor upgrade levels **15+**; unlocks Land Cruiser **Armored Skirts** |
| **Modern Armor Protection** | 1944 | 110 days | Advanced Armor Protection | Armor upgrade levels **18+** |

## Engine upgrade technologies

Each raises the ceiling on engine upgrade levels (each level: Max Speed +0.1 km/h, Fuel Usage +0.05, Reliability -1.5%, Production Cost +0.1, Design Cost +1 army XP).

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| **Basic Engine** | 1935 | 110 days | – | Engine upgrade levels **5+** |
| **Improved Engine** | 1938 | 110 days | Basic Engine | Engine upgrade levels **10+** |
| **Advanced Engine** | 1941 | 110 days | Improved Engine | Engine upgrade levels **15+** |
| **Modern Engine** | 1944 | 110 days | Advanced Engine | Engine upgrade levels **18+** |

## Flamethrower upgrade

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| **Advanced Flamethrower** | 1941 | 110 days | Flamethrower Tank + Inter-War Tank Development | Light/Medium/Heavy flame tank: Forest, Hills, Urban, Jungle and Fort **Attack +5%** each.<br>Unlocks **Advanced Flamethrower** module: Breakthrough 6.0, Soft attack 12.0, Reliability -5%, Cost 1.20 |

## Land Cruiser upgrades

All require the **Land Cruiser** special project completed. Some also benefit Super-Heavy tanks and super-heavy variants.

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| **Naval Engine Conversion** | 1943 | 110 days | Land Cruiser + Super-Heavy Tank Chassis | Land Cruisers and Super-heavy tank: Supply Use -2%, Max Speed +5% |
| **Transmission Improvements** | 1943 | 110 days | Land Cruiser + Super-Heavy Tank Chassis | Land Cruisers and Super-heavy tank: Supply Use -2%, Reliability +5%, Forest/Hills/Mountain/Jungle Movement +20% each |
| **Specialized Field Manuals** | 1943 | 110 days | Land Cruiser + Super-Heavy Tank Chassis | Land Cruisers: Entrenchment +5%, Organization +10, HP +5% |
| **High-Impact Obliterator Cannon** | 1943 | 110 days | Land Cruiser + Super-Heavy Tank Chassis | Enables the **High-Impact Obliterator Cannon** main armament |
| **Weapon Fire Control** | 1945 | 110 days | One of: Naval Engine Conversion / Transmission Improvements / Specialized Field Manuals | Land Cruisers: Defense +10%, Breakthrough +10% |

## Secret technologies (NSB tree)

| Technology | Unlocked by | Effects |
|---|---|---|
| `mountain_tanks` | British Raj via **Mountain Tanks**; Siam via **Mountain Tanks** | All Tanks, SP Anti-Air, SP Artillery, Tank Destroyers and Amphibious tank: Mountain Attack +15%, Speed +15% |
| `NOR_rikstanken_tech` | Norway via **Rikstanken** | Enables **Improvised Turret** (Breakthrough 1.0, Cost 0.1, Reliability -25%) and **Makeshift Armor** (Defense 1.0, Production cost -30%, Hardness -30%) |
| `jungle_tanks` | Siam via **Jungle Armor** | Light/Medium Tanks, all SP Anti-Air, SP Artillery, Tank Destroyers and Amphibious tank: Jungle Attack +15%, Speed +15% |
| `jungle_heavy_tanks` | Australia via establish-training-camps focus | Heavy, Super-Heavy and Modern tanks: Jungle Attack +15%, Speed +15% |

---

## Part 2 — Legacy armor technology (without No Step Back)

Fixed equipment models instead of designer chassis. Reliability is a flat 80% on every model.

## Root

| Technology | Year | Base time | Prerequisites | Equipment unlocked |
|---|---|---|---|---|
| **Great War Tank** | 1918 | 220 days | – | Great War Tank (1 Steel): MP 2 · Breakthrough 18.0 · Soft attack 8.0 · Hard attack 4.0 · Piercing 15.0 · Armor 5.0 · Defense 4.0 · Hardness 80% · 6.0 km/h · Reliability 80% · Fuel 1.00 · **Cost 7.00**. Also enables the Light Tank battalion |

## Light tanks

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hard­ness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Light Tank I** | 1934 | 220 days | Great War Tank | 2 Steel | 26.0 | 13.0 | 4.0 | 10.0 | 10.0 | 4.0 | 80% | 10.0 km/h | 2.40 | 8.00 |
| **Light Tank II** | 1936 | 220 days | Light Tank I | 3 Steel | 36.0 | 16.0 | 6.0 | 30.0 | 15.0 | 5.0 | 80% | 12.0 km/h | 2.40 | 9.00 |
| **Light Tank III** | 1941 | 220 days | Light Tank II | 4 Steel | 46.0 | 22.0 | 9.0 | 50.0 | 30.0 | 6.0 | 80% | 14.0 km/h | 2.40 | 10.00 |

## Amphibious tanks (legacy)

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hardness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Basic Amphibious Tank** | 1940 | 220 days | Light Tank II | 2 Steel | 26.0 | 13.0 | 4.0 | 10.0 | 20.0 | 4.0 | 80% | 7.0 km/h | 4.00 | 10.00 |
| **Improved Amphibious Tank** | 1942 | 220 days | Basic Amphibious Tank | 2 Steel, 2 Tungsten | 36.0 | 19.0 | 14.0 | 61.0 | 80.0 | 5.0 | 90% | 8.0 km/h | 4.00 | 13.00 |

Amphibious Tank Battalion terrain: Forest -40%/-20%, Mountain –/-10%, Plains -10%/-10%, Urban –/-40%/-10%, Jungle -40%/-30%, **Marsh –/+30%**, **River –/+40%**, **Amphibious –/+60%**.

## Medium and modern tanks

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hardness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Medium Tank I** | 1938 | 220 days | Light Tank II | 2 Steel, 2 Tungsten | 36.0 | 19.0 | 14.0 | 61.0 | 60.0 | 5.0 | 90% | 8.0 km/h | 3.60 | 12.00 |
| **Medium Tank II** | 1941 | 220 days | One of: Medium Tank I / Heavy Tank II | 3 Steel, 2 Tungsten | 51.0 | 25.0 | 19.0 | 81.0 | 80.0 | 7.0 | 85% | 9.0 km/h | 3.60 | 13.00 |
| **Medium Tank III** | 1943 | 220 days | One of: Medium Tank II / Heavy Tank III | 4 Steel, 2 Tungsten | 66.0 | 32.0 | 24.0 | 91.0 | 90.0 | 9.0 | 85% | 10.0 km/h | 3.60 | 14.00 |
| **Modern Tank** | 1945 | 275 days | One of: Medium Tank III / Heavy Tank III | 3 Steel, 4 Chromium | 84.0 | 40.0 | 32.0 | 131.0 | 130.0 | 10.0 | 98% | 10.0 km/h | 5.00 | 28.00 |

## Heavy and super-heavy tanks

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hardness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Heavy Tank I** | 1934 | 220 days | Great War Tank | 3 Steel, 3 Chromium | 36.0 | 15.0 | 12.0 | 35.0 | 70.0 | 6.0 | 95% | 5.0 km/h | 4.40 | 25.00 |
| **Heavy Tank II** | 1941 | 275 days | One of: Heavy Tank I / Medium Tank II | 3 Steel, 3 Chromium | 52.0 | 27.0 | 30.0 | 111.0 | 110.0 | 8.0 | 95% | 6.0 km/h | 4.40 | 27.00 |
| **Heavy Tank III** | 1943 | 275 days | One of: Heavy Tank II / Medium Tank III | 4 Steel, 3 Chromium | 67.0 | 35.0 | 40.0 | 131.0 | 130.0 | 9.0 | 95% | 6.0 km/h | 4.40 | 30.00 — **unlocks Land Cruiser** |
| **Super Heavy Tank** | 1941 | 330 days | Heavy Tank II | 3 Steel, 4 Chromium | 74.0 | 38.0 | 45.0 | 146.0 | 145.0 | 10.0 | 99% | 4.0 km/h | 10.00 | **100.00** |

## Armor variants — Tank Destroyers

TDs trade soft attack, organisation and (heavily) breakthrough for hard attack and piercing. Because **40% of a division's piercing and 40% of its armor come from the single battalion with the highest value**, one TD battalion can carry a whole division's anti-armor capability.

Battalion modifiers: Light TD equipment breakthrough -40%, supply use 0.20, HP 0.6, suppression 1.0; Medium/Heavy/Super-Heavy/Modern TD equipment breakthrough -20%.

### Light Tank Destroyers

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hardness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Light Tank Destroyer I** | 1934 | 55 days | Light Tank I | 2 Steel, 2 Tungsten | 1.0 | 6.0 | 10.0 | 50.0 | 10.0 | 4.0 | 80% | 10.0 km/h | 1.20 | 8.00 |
| **Light Tank Destroyer II** | 1936 | 55 days | Light Tank II | 3 Steel, 2 Tungsten | 1.3 | 6.0 | 16.0 | 77.0 | 15.0 | 5.0 | 80% | 12.0 km/h | 1.20 | 9.00 |
| **Light Tank Destroyer III** | 1941 | 55 days | Light Tank III | 4 Steel, 2 Tungsten | 1.8 | 8.0 | 24.0 | 99.0 | 30.0 | 7.0 | 80% | 14.0 km/h | 1.20 | 10.00 |

### Medium and Modern Tank Destroyers

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hardness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Medium Tank Destroyer I** | 1938 | 55 days | Medium Tank I | 2 Steel, 4 Tungsten | 1.3 | 5.0 | 20.0 | 88.0 | 60.0 | 5.0 | 90% | 8.0 km/h | 1.80 | 12.00 |
| **Medium Tank Destroyer II** | 1941 | 55 days | Medium Tank II | 3 Steel, 4 Tungsten | 1.5 | 6.0 | 26.0 | 110.0 | 80.0 | 6.0 | 85% | 9.0 km/h | 1.80 | 13.00 |
| **Medium Tank Destroyer III** | 1943 | 55 days | Medium Tank III | 4 Steel, 4 Tungsten | 1.8 | 8.0 | 32.0 | 120.0 | 90.0 | 7.0 | 85% | 10.0 km/h | 1.80 | 14.00 |
| **Modern Tank Destroyer** | 1945 | 55 days | Modern Tank | 3 Steel, 4 Chromium | 2.0 | 10.0 | 42.0 | 165.0 | 130.0 | 8.0 | 98% | 10.0 km/h | 2.50 | 28.00 |

### Heavy and Super-Heavy Tank Destroyers

| Technology | Year | Base time | Prerequisites | Resources | Brk | Soft | Hard | Pierce | Armor | Def | Hardness | Speed | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Heavy Tank Destroyer I** | 1934 | 55 days | Heavy Tank I | 3 Steel, 3 Chromium | 1.0 | 6.0 | 25.0 | 96.0 | 70.0 | 4.0 | 95% | 5.0 km/h | 2.20 | 25.00 |
| **Heavy Tank Destroyer II** | 1941 | 55 days | Heavy Tank II | 4 Steel, 3 Chromium | 1.5 | 8.0 | 42.0 | 140.0 | 110.0 | 6.0 | 95% | 6.0 km/h | 2.20 | 27.00 |
| **Heavy Tank Destroyer III** | 1943 | 55 days | Heavy Tank III | 4 Steel, 4 Chromium | 1.8 | 10.0 | 60.0 | 160.0 | 130.0 | 7.0 | 95% | 6.0 km/h | 2.20 | 30.00 |
| **Super Heavy Tank Destroyer** | 1941 | 55 days | Super Heavy Tank | 3 Steel, 4 Chromium | 1.8 | 12.0 | 70.0 | 170.0 | 145.0 | 7.0 | 99% | 4.0 km/h | 5.00 | **100.00** |

Super-Heavy Tank Destroyer terrain: Forest -40%/-50%, Hills –/-30%, Mountain –/-40%, Urban –/-60%/-20%, Jungle -40%/-70%, Marsh -20%/-50%, **Fort –/+30%**, River -30%/-50%/-50%, Amphibious –/-100%.

## Armor variants — Self-Propelled Artillery

SPGs trade hard attack, piercing, hardness, armor, organisation and breakthrough for soft attack, but are far better armored than truck-drawn artillery — useful because 40% of a division's armor comes from its best-armored battalion.

### Light SP Artillery

| Technology | Year | Base time | Prerequisites | Resources | Def | Brk | Hardness | Soft | Hard | Speed | Armor | Pierce | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Light SP Artillery I** | 1934 | 42 days | Light Tank I | 2 Steel, 1 Tungsten | 4.0 | 2.0 | 50.0% | 34.0 | 0.5 | 10.0 km/h | 5.0 | 4.0 | 1.2 | 8.0 |
| **Light SP Artillery II** | 1936 | 42 days | Light Tank II | 3 Steel, 1 Tungsten | 5.0 | 2.5 | 50.0% | 42.0 | 1.0 | 12.0 km/h | 10.0 | 4.0 | 1.2 | 9.0 |
| **Light SP Artillery III** | 1941 | 42 days | Light Tank III | 4 Steel, 1 Tungsten | 7.0 | 3.5 | 50.0% | 46.0 | 1.5 | 14.0 km/h | 25.0 | 4.0 | 1.2 | 10.0 |

### Medium and Modern SP Artillery

| Technology | Year | Base time | Prerequisites | Resources | Def | Brk | Hardness | Soft | Hard | Speed | Armor | Pierce | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Medium SP Artillery I** | 1939 | 42 days | Medium Tank I | 2 Steel, 3 Tungsten | 5.0 | 3.0 | 65.0% | 42.0 | 1.0 | 8.0 km/h | 45.0 | 5.0 | 1.8 | 12.0 |
| **Medium SP Artillery II** | 1941 | 42 days | Medium Tank II | 3 Steel, 3 Tungsten | 6.0 | 3.0 | 65.0% | 50.0 | 1.5 | 9.0 km/h | 50.0 | 5.0 | 1.8 | 13.0 |
| **Medium SP Artillery III** | 1943 | 42 days | Medium Tank III | 4 Steel, 3 Tungsten | 7.0 | 4.0 | 65.0% | 55.0 | 2.0 | 10.0 km/h | 58.0 | 5.0 | 1.8 | 14.0 |
| **Modern SP Artillery** | 1945 | 42 days | Modern Tank | 3 Steel, 4 Chromium | 8.0 | 4.0 | 85.0% | 80.0 | 3.0 | 10.0 km/h | 90.0 | 10.0 | 2.5 | 28.0 |

### Heavy and Super-Heavy SP Artillery

| Technology | Year | Base time | Prerequisites | Resources | Def | Brk | Hardness | Soft | Hard | Speed | Armor | Pierce | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Heavy SP Artillery I** | 1934 | 42 days | Heavy Tank I | 3 Steel, 3 Chromium | 4.0 | 2.0 | 80.0% | 55.0 | 1.0 | 5.0 km/h | 45.0 | 8.0 | 2.2 | 25.0 |
| **Heavy SP Artillery II** | 1941 | 42 days | Heavy Tank II | 4 Steel, 3 Chromium | 6.0 | 3.0 | 80.0% | 74.0 | 2.0 | 6.0 km/h | 68.0 | 8.0 | 2.2 | 27.0 |
| **Heavy SP Artillery III** | 1943 | 42 days | Heavy Tank III | 5 Steel, 3 Chromium | 7.0 | 3.5 | 80.0% | 80.0 | 2.5 | 6.0 km/h | 90.0 | 8.0 | 2.2 | 30.0 |
| **Super Heavy SP Artillery** | 1943 | 42 days | Super Heavy Tank | 3 Steel, 4 Chromium | 7.0 | 3.5 | 90.0% | 85.0 | 3.0 | 4.0 km/h | 100.0 | 9.0 | 5.0 | **100.0** |

## Armor variants — Self-Propelled Anti-Air

SPAA gains air attack at the cost of higher production cost, lower soft/hard attack, piercing, hardness, armor, organisation and breakthrough. Still fast, armored, and able to pierce obsolete armor and mechanized infantry.

### Light SP Anti-Air

| Technology | Year | Base time | Prerequisites | Resources | Def | Brk | Hardness | Soft | Hard | Air Atk | Speed | Armor | Pierce | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Light SP Anti-Air I** | 1934 | 42 days | Light Tank I | 2 Steel | 2.0 | 2.0 | 50.0% | 2.0 | 1.0 | 15.0 | 10.0 km/h | 5.0 | 5.0 | 0.6 | 10.0 |
| **Light SP Anti-Air II** | 1936 | 42 days | Light Tank II | 3 Steel | 2.5 | 2.5 | 50.0% | 3.0 | 1.5 | 17.0 | 12.0 km/h | 10.0 | 20.0 | 0.6 | 11.0 |
| **Light SP Anti-Air III** | 1941 | 42 days | Light Tank III | 4 Steel | 3.5 | 3.5 | 50.0% | 4.5 | 4.0 | 32.0 | 14.0 km/h | 25.0 | 35.0 | 0.6 | 12.0 |

### Medium and Modern SP Anti-Air

| Technology | Year | Base time | Prerequisites | Resources | Def | Brk | Hardness | Soft | Hard | Air Atk | Speed | Armor | Pierce | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Medium SP Anti-Air I** | 1939 | 42 days | Medium Tank I | 2 Steel, 2 Tungsten | 2.5 | 2.5 | 65.0% | 4.5 | 3.0 | 22.0 | 8.0 km/h | 45.0 | 40.0 | 0.9 | 12.0 |
| **Medium SP Anti-Air II** | 1941 | 42 days | Medium Tank II | 3 Steel, 2 Tungsten | 3.0 | 3.0 | 65.0% | 6.0 | 4.5 | 32.0 | 9.0 km/h | 50.0 | 60.0 | 0.9 | 13.0 |
| **Medium SP Anti-Air III** | 1943 | 42 days | Medium Tank III | 4 Steel, 2 Tungsten | 3.5 | 3.5 | 65.0% | 7.5 | 6.0 | 43.0 | 10.0 km/h | 58.0 | 70.0 | 0.9 | 14.0 |
| **Modern SP Anti-Air** | 1945 | 42 days | Modern Tank | 3 Steel, 4 Chromium | 4.0 | 4.0 | 85.0% | 9.0 | 7.5 | 50.0 | 10.0 km/h | 90.0 | 100.0 | 1.2 | 28.0 |

### Heavy and Super-Heavy SP Anti-Air

| Technology | Year | Base time | Prerequisites | Resources | Def | Brk | Hardness | Soft | Hard | Air Atk | Speed | Armor | Pierce | Fuel | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Heavy SP Anti-Air I** | 1934 | 42 days | Heavy Tank I | 3 Steel, 3 Chromium | 2.0 | 2.0 | 80.0% | 4.5 | 4.0 | 17.0 | 5.0 km/h | 45.0 | 25.0 | 1.1 | 25.0 |
| **Heavy SP Anti-Air II** | 1941 | 42 days | Heavy Tank II | 3 Steel, 3 Chromium | 3.0 | 3.0 | 80.0% | 6.0 | 4.5 | 33.0 | 6.0 km/h | 68.0 | 60.0 | 1.1 | 27.0 |
| **Heavy SP Anti-Air III** | 1943 | 42 days | Heavy Tank III | 4 Steel, 3 Chromium | 3.5 | 3.5 | 80.0% | 7.5 | 6.0 | 44.0 | 6.0 km/h | 90.0 | 88.0 | 1.1 | 30.0 |
| **Super Heavy SP Anti-Air** | 1943 | 42 days | Super Heavy Tank | 3 Steel, 4 Chromium | 3.5 | 3.5 | 90.0% | 11.5 | 9.0 | 50.0 | 4.0 km/h | 100.0 | 98.0 | 2.5 | **100.0** |

## Land Cruiser upgrades (legacy tree)

The legacy page carries the same Land Cruiser upgrade line as the No Step Back tree — see the **Land Cruiser upgrades** table in Part 1. In the legacy tree the Land Cruiser is unlocked by **Heavy Tank III** rather than by the Super-Heavy Tank Chassis.

## Secret technologies (legacy tree)

| Technology | Unlocked by | Effects |
|---|---|---|
| `mountain_tanks` | British Raj via **Mountain Tanks** | All Tanks, SP Anti-Air, SP Artillery, Tank Destroyers and Amphibious tank: Mountain Attack +15%, Speed +15% |
| `NOR_rikstanken_tech` | Norway via **Rikstanken** | Enables the "Landsverk 'Rikstanken' L-120" Light Tank variant |

## Research notes

**Inferred:**
- In the NSB tree the **chassis technologies are the expensive commitment** (220–330 days each) while the Armor and Engine upgrade lines are cheap (110 days) and multiply the value of every chassis you own. Take the upgrade lines on schedule and skip chassis tiers you will not build.
- Medium and Heavy chassis lines both feed the Modern chassis, so a heavy-tank nation does not need the medium line at all to reach Modern.
- The Super-Heavy chassis (330 days, 50.70 default cost, 3 Steel + 2 Chromium) is a prestige/Land-Cruiser gateway, not a practical mainline vehicle.
- In the legacy tree the **variant technologies are extremely cheap** (42–55 days) relative to the base tank technologies (220–275 days). Researching the TD/SPG/SPAA variant of a tank you already have is nearly free research and is how a non-NSB nation gets piercing and armor into infantry divisions.
- Tungsten gates almost all legacy anti-tank equipment; Chromium gates all heavy and modern equipment. Check resource access before committing to a heavy line.

## See also

- [Tank designer](tank-designer.md)
- [Artillery technology](artillery-technology.md) — the gun modules for the NSB designer
- [Land doctrine](land-doctrine.md) — Armor track subdoctrines
