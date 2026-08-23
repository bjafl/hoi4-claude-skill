---
title: Ship Designer
category: naval-warfare
tags: [ship-designer, naval, hulls, modules, engines, armor, weapons, torpedoes, submarines, carriers, battleships, destroyers, cruisers]
game_version: "1.19"
dlc: [Man the Guns]
sources:
  - https://hoi4.paradoxwikis.com/Ship_designer
  - https://hoi4.paradoxwikis.com/Ship
  - https://hoi4.paradoxwikis.com/List_of_default_ship_variants
  - https://hoi4.paradoxwikis.com/Historical_ship_variants
---

## Summary

The ship designer (**requires Man the Guns**) allows custom naval equipment designs by selecting a hull type and equipping it with modules (engines, armor, weapons, radars, torpedoes, etc.). Hull types are unlocked through naval technology and set base stats; modules are chosen from restricted slot pools to build complete ship variants with distinct roles and combat stats. Five capital ship types (battleships, heavy cruisers, battlecruisers, super-heavy battleships, large cruisers) and five screen types (destroyers, light cruisers, torpedo cruisers, carriers, escort carriers, submarines) can be designed, each with different armor/speed/firepower tradeoffs.

## Hull types

Hulls are the foundational component that determine the ship type, cost, manpower, fuel consumption, and available module slots. Each hull gen represents a tech unlock.

### Destroyer hulls

| Hull | Year | Max Speed (kn) | Max Range (km) | HP | Reliability | Supply Use | Manpower | Fuel Usage | Modules (fixed / custom) | Production Cost | Steel per dockyard |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Early Destroyer | 1922 | 32 | 1500 | 25 | 80% | 0.04 | 250 | 0 | 6 / 2 | 400 | 2 |
| 1936 Destroyer | 1936 | 32 | 1800 | 40 | 85% | 0.04 | 325 | 0 | 6 / 2 | 500 | 2 |
| 1940 Destroyer | 1940 | 32 | 2000 | 50 | 90% | 0.04 | 400 | 0 | 6 / 3 | 550 | 3 |
| 1944 Destroyer | 1944 | 32 | 2500 | 60 | 92% | 0.04 | 500 | 0 | 6 / 4 | 600 | 4 Steel, 1 Chromium |

### Cruiser hulls (light and heavy)

| Hull | Year | Max Speed (kn) | Max Range (km) | HP | Reliability | Supply Use | Manpower | Fuel Usage | Modules (fixed / custom) | Production Cost | Steel per dockyard |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Early Cruiser | 1922 | 27 | 2500 | 100 | 80% | 0.16 | 600 | 20 | 7 / 3 | 1800 | 1 |
| 1936 Cruiser | 1936 | 30 | 3000 | 110 | 85% | 0.16 | 800 | 20 | 7 / 4 | 1900 | 2 |
| 1940 Cruiser | 1940 | 32 | 4000 | 120 | 90% | 0.16 | 1200 | 20 | 7 / 5 | 2000 | 2 |
| 1944 Cruiser | 1944 | 33 | 4500 | 130 | 95% | 0.16 | 1400 | 20 | 7 / 5 | 2100 | 3 |
| Torpedo Cruiser | 1936 | 30 | 4000 | 140 | 90% | 0.16 | 960 | 20 | 7 / 5 | 1700 | 3 |
| Panzerschiff | 1933 | 23 | 7500 | 220 | 80% | 0.4 | 1800 | 20 | 7 / 4 | 3500 | 4 |
| Coastal Defense Ship | 1936 | 20 | 1500 | 100 | 80% | 0.16 | 1800 | 20 | 7 / 4 | 3500 | 3 |

### Battleship hulls

| Hull | Year | Max Speed (kn) | Max Range (km) | HP | Reliability | Supply Use | Manpower | Fuel Usage | Modules (fixed / custom) | Production Cost | Steel per dockyard |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Pre-Dreadnought | 1905 | 18 | 2250 | 300 | 65% | 0.8 | 3200 | 67 | 7 / 3 | 2600 | 1 Steel, 1 Chromium |
| Early Heavy Ship | 1922 | 20 | 3000 | 350 | 80% | 0.8 | 4000 | 67 | 7 / 4 | 2800 | 1 Steel, 1 Chromium |
| 1936 Heavy Ship | 1936 | 24 | 3500 | 370 | 85% | 0.8 | 5200 | 67 | 7 / 4 | 3000 | 1 Steel, 1 Chromium |
| 1940 Heavy Ship | 1940 | 25 | 4000 | 400 | 90% | 0.8 | 6000 | 67 | 7 / 5 | 3200 | 1 Steel, 1 Chromium |
| 1944 Heavy Ship | 1944 | 26 | 4500 | 450 | 95% | 0.8 | 6000 | 67 | 7 / 5 | 3400 | 1 Steel, 1 Chromium |
| Super Heavy Battleship | 1943 | 24 | 4500 | 700 | 80% | 0.8 | 9000 | 75 | 7 / 7 | 5500 | 1 Steel, 1 Chromium |
| Modern Battleship | 1945 | 30 | 5000 | 525 | 95% | 0.8 | 6000 | 80 | 7 / 5 | 4000 | 6 Steel, 2 Tungsten, 3 Chromium |

### Carrier hulls

| Hull | Year | Max Speed (kn) | Max Range (km) | HP | Reliability | Supply Use | Manpower | Fuel Usage | Modules (fixed / custom) | Production Cost | Steel per dockyard |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Converted Cruiser | 1936 | 22.5 | 4000 | 125 | 65% | 1.2 | 1000 | 87 | 7 / 0 | 2700 | 3 Steel, 1 Chromium |
| Converted Battleship | 1940 | 25 | 4000 | 325 | 65% | 1.2 | 5000 | 87 | 7 / 1 | 2700 | 4 Steel, 1 Chromium |
| 1936 Carrier | 1936 | 26 | 3000 | 250 | 70% | 1.2 | 4500 | 87 | 7 / 2 | 2094 | 3 Steel, 1 Chromium |
| 1940 Carrier | 1940 | 26 | 4000 | 325 | 75% | 1.2 | 5000 | 87 | 7 / 3 | 2600 | 4 Steel, 1 Chromium |
| 1944 Carrier | 1944 | 26 | 5000 | 350 | 80% | 1.2 | 5500 | 87 | 7 / 4 | 3250 | 4 Steel, 2 Chromium |
| Ice Carrier | 1943 | 18 | 7000 | 350 | 80% | 1.2 | 6000 | 95 | 7 / 4 | 4500 | 5 Steel, 2 Chromium |
| Modern Carrier | 1945 | 30 | 7500 | 400 | 85% | 1.2 | 6500 | 90 | 7 / 4 | 4250 | 5 Steel, 3 Chromium |

### Submarine hulls

| Hull | Year | Max Speed (kn) | Max Range (km) | HP | Reliability | Supply Use | Manpower | Fuel Usage | Sub Visibility | Modules (fixed / custom) | Production Cost | Steel per dockyard |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Early Submarine | 1922 | 13 | 2000 | 10 | 60% | 0.04 | 200 | 1 | 25 | 2 / 1 | 320 | 1 |
| 1936 Submarine | 1936 | 17 | 2500 | 20 | 70% | 0.04 | 200 | 1 | 22 | 2 / 1 | 350 | 2 |
| 1940 Submarine | 1940 | 18 | 3000 | 30 | 75% | 0.04 | 200 | 1 | 20 | 2 / 3 | 420 | 2 |
| 1944 Submarine | 1944 | 18 | 3500 | 35 | 80% | 0.04 | 200 | 1 | 15 | 2 / 3 | 550 | 3 Steel, 1 Chromium |
| Midget Submarine | 1938 | 8.3 | 400 | 5 | 65% | 0.04 | 100 | 1 | 15 | 2 / 0 | 150 | 1 |
| Cruiser Submarine | 1936 | 16 | 5000 | 30 | 75% | 0.04 | 200 | 1 | 20 | 2 / 3 | 490 | 2 |
| Fleet Submarine | 1943 | 18 | 6500 | 40 | 75% | 0.04 | 200 | 1 | 18 | 2 / 3 | 650 | 3 |
| Nuclear Submarine | 1950 | 20 | 10000 | 50 | 75% | 0.04 | 400 | 1 | 16 | 2 / 4 | 1150 | 3 Steel, 2 Chromium |

Note: Early Submarine, 1936, and Cruiser submarine have Fuel Usage 1; others similarly shown. Fleet and Nuclear Submarines require [Götterdämmerung] DLC.

### Convoy hull

| Hull | Max Speed (kn) | Surface Detection | Surface Visibility | Light Attack | Light Piercing | Anti-Air | HP | Reliability | Production Cost | Steel per dockyard |
|---|---|---|---|---|---|---|---|---|---|---|
| Convoy | 12 | 10 | 14 | 0.25 | 1 | 0.1 | 60 | 80% | 70 | 1 |

Convoys are auto-managed and cannot be customized with modules.

## Engines

Each hull type uses engine modules matched to size. Engine choice drives max speed and fuel consumption; higher engine tiers unlock with research.

### Destroyer engines

| Module | Max Speed | Fuel Usage | Production Cost | Prerequisite |
|---|---|---|---|---|
| Light Engine I | +10% | 7 | +12.5% | Early Destroyer |
| Light Engine II | +15% | 8 | +15% | 1936 Destroyer |
| Light Engine III | +20% | 10 | +17.5% | 1940 Destroyer |
| Light Engine IV | +25% | 10 | +20% | 1944 Destroyer |

### Cruiser engines

| Module | Max Speed | Fuel Usage | Production Cost | Prerequisite |
|---|---|---|---|---|
| Cruiser Engine I | +20% | 12 | +15% | Early Cruiser |
| Cruiser Engine II | +30% | 16 | +17.5% | 1936 Cruiser |
| Cruiser Engine III | +35% | 20 | +20% | 1940 Cruiser |
| Cruiser Engine IV | +40% | 24 | +22.5% | 1944 Cruiser |

### Heavy ship engines

| Module | Max Speed | Fuel Usage | Production Cost | Prerequisite |
|---|---|---|---|---|
| Heavy Engine I | +20% | 20 | +17.5% | Early Heavy Ship |
| Heavy Engine II | +35% | 25 | +20% | 1936 Heavy Ship |
| Heavy Engine III | +45% | 30 | +22.5% | 1940 Heavy Ship |
| Heavy Engine IV | +55% | 35 | +25% | 1944 Heavy Ship |
| Nuclear Heavy Ship Reactor | +60%, +100% range | -100% fuel | +25% | Modern Battleship + [Götterdämmerung] Nuclear Engines |

### Carrier engines

| Module | Max Speed | Fuel Usage | Production Cost | Prerequisite |
|---|---|---|---|---|
| Carrier Engine I | +30% | 12 | +10% | Deck Conversions |
| Carrier Engine II | +40% | 16 | +12.5% | 1936 Carrier |
| Carrier Engine III | +50% | 20 | +15% | 1940 Carrier |
| Carrier Engine IV | +60% | 24 | +17.5% | 1944 Carrier |
| Nuclear Carrier Reactor | +60%, +100% range | -100% fuel | +25% | Modern Carrier + [Götterdämmerung] Nuclear Engines |

### Submarine engines

| Module | Max Speed | Sub Visibility | Fuel Usage | Production Cost | Prerequisite |
|---|---|---|---|---|---|
| Submarine Engine I | +10% | — | 7 | +10% | Early Submarine |
| Submarine Engine II | +10% | — | 8 | +12.5% | 1936 Submarine |
| Submarine Engine III | +15% | –5% | 10 | +15% | 1940 Submarine |
| Submarine Engine IV | +20% | –10% | 10 | +20% | 1944 Submarine |
| Air-Independent Propulsion | +15%, –66% range | –15% | 60 | +25% | [Götterdämmerung] Air-Independent Propulsion |
| AIP-Diesel Combination Engine | +15%, –33% range | –17% | 45 | +30% | [Götterdämmerung] AIP-Diesel Combination Engines |
| High Speed Walter Engines | +35% | –20% | 30 | +35% | [Götterdämmerung] High-Speed Walter Engines |
| Nuclear Submarine Reactor | +10%, no fuel cost | — | -100% fuel | +25% | [Götterdämmerung] Nuclear Engines |

## Armor

Armor modules reduce incoming damage and affect HP, max speed, and cost. Armor types are not interchangeable between cruisers and battleships — cruiser armor and battleship armor use different module pools.

### Cruiser armor

| Module | Max Speed | HP | Armor | Incoming Torpedo Crit Chance | Torpedo Damage Reduction | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| Cruiser Armor I | -5% | — | 6 | — | — | +10% | — | Early Cruiser |
| Cruiser Armor II | -7.5% | +5% | 8 | — | — | +15% | 1 | Basic Cruiser Armor Scheme |
| Cruiser Armor III | -10% | +10% | 10 | — | — | +20% | 1 Steel, 1 Chromium | Inclined Belt Armor Scheme |
| Cruiser Armor IV | -12.5% | +15% | 12 | — | — | +25% | 2 Steel, 1 Chromium | All-or-Nothing Armor Scheme |

### Battleship armor (capital ships)

| Module | Max Speed | HP | Armor | Incoming Torpedo Crit Chance | Torpedo Damage Reduction | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| Battleship Armor I | — | +5% | 30 | –10% | +10% | +12.5% | 1 | Early Heavy Ship |
| Battleship Armor II | -5% | +10% | 36 | –15% | +15% | +15% | 1 | Inclined Belt Armor Scheme |
| Battleship Armor III | -10% | +15% | 40 | –20% | +20% | +17.5% | 2 Steel, 1 Chromium | All-or-Nothing Armor Scheme |

### Battlecruiser armor

| Module | Max Speed | HP | Armor | Torpedo Damage Reduction | Supply Use | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|---|
| Battlecruiser Armor I | +5% | +5% | 22 | +10% | –0.32 | +10% | Early Heavy Ship |
| Battlecruiser Armor II | — | +10% | 28 | +15% | –0.32 | +12.5% | Inclined Belt Armor Scheme |
| Battlecruiser Armor III | -10% | +15% | 34 | +20% | –0.32 | +12.5% | All-or-Nothing Armor Scheme |

### Super-Heavy armor

| Module | Max Speed | HP | Armor | Incoming Torpedo Crit Chance | Torpedo Damage Reduction | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| Super-Heavy Armor | -12% | +10% | 55 | –25% | +25% | +25% | 2 Steel, 1 Chromium | Super Heavy Battleship hull |

### Carrier deck armor

| Module | Max Speed | HP | Armor | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|
| Flight Deck Armor | -5% | +25 | 5 | +10% | 1 | Deck Conversions |

Ice Carrier runway reinforcements: Pykrete Runway Reinforcements (-10% speed, +30 HP, 2 armor, +10% cost, 2 steel), Steel-Reinforced Pykrete Runway (-15% speed, +35 HP, 4 armor, +15% cost, 2 steel), Ice-Composite Runway (-15% speed, –15% weather penalty, +40 HP, 6 armor, +20% cost, 3 steel).

## Guns and armament

### Rapid-fire guns (light battery)

Light guns are mounted on destroyers and light cruisers; they target the first non-empty row in naval battle.

| Module | Light Attack | Light Piercing | Anti-Air | Max Speed | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|
| Light Battery I (85mm) | 1 | 1 | — | -1% | 90 | Naval Gunnery |
| Light Battery II (105mm) | 1.5 | 2 | — | -2% | 120 | Basic Light Battery |
| Light Battery III (127mm) | 2 | 2.5 | — | -3% | 150 | Improved Light Battery |
| Light Battery IV (130mm) | 3 | 2.5 | — | -4% | 175 | Advanced Light Battery |
| Dual-Purpose Main Battery I (100mm) | 1 | 0.5 | 1 | -1% | 100 | Naval Gunnery |
| Dual-Purpose Main Battery II (113mm) | 1.5 | 1 | 2 | -2% | 130 | Basic Dual-Purpose Battery |
| Dual-Purpose Main Battery III (127mm) | 2 | 1.7 | 3 | -3% | 160 | Improved Dual-Purpose Battery |
| Dual-Purpose Main Battery IV (127mm RF) | 2.5 | 1.7 | 4 | -4% | 185 | Advanced Dual-Purpose Battery |

### Medium batteries (light cruiser armament)

Medium guns mount on light cruisers; they add breakthrough and gun HP bonuses. All require a cruiser hull without a heavy cruiser battery mounted.

| Module | Light Attack | Light Piercing | HP | Max Speed | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|---|
| Light Cruiser Battery I (14.5cm) | 4 | 5.5 | +20 | -3% | 300 | — | Naval Gunnery |
| Light Cruiser Battery II (15cm) | 5 | 7 | +20 | -4% | 350 | — | Basic Medium Battery |
| Light Cruiser Battery III (15.5cm) | 6 | 8 | +20 | -5% | 375 | 1 | Improved Medium Battery |
| Light Cruiser Battery IV (15.5cm Auto-Loading) | 7.5 | 9 | +20 | -6% | 425 | 1 | Advanced Medium Battery |
| Light Cruiser Battery Auto-Loading (152mm RF DP) | 7.5 | 8 | +20 | -6% | 450 | — | Advanced Medium Dual-Purpose Battery |

### Heavy cruiser batteries

Heavy guns mount on heavy cruisers; they block light cruiser batteries and rapid-fire guns from being mounted. Heavy-only mountings can upgrade to heavy cruiser battery roles.

| Module | Heavy Attack | Heavy Piercing | HP | Max Speed | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|---|
| Heavy Cruiser Battery I (17cm) | 6 | 22 | +40% | -4% | 650 | 1 | Naval Gunnery |
| Heavy Cruiser Battery II (19cm) | 8 | 25 | +40% | -6% | 700 | 1 | Basic Medium Battery |
| Heavy Cruiser Battery III (20.3cm) | 10 | 29 | +40% | -7% | 725 | 2 | Improved Medium Battery |
| Heavy Cruiser Battery IV (20.3cm Auto-Loading) | 12 | 34 | +40% | -8% | 800 | 2 | Advanced Medium Battery |

### Heavy gun batteries (battleships and large cruisers)

Heavy batteries mount on battleships, Panzerschiff, and Coastal Defense Ship hulls; they provide major firepower for capital ships.

| Module | Heavy Attack | Heavy Piercing | Max Speed | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|
| Heavy Battery I (28cm) | 14 | 31 | -5% | 1550 | 1 | Naval Gunnery |
| Heavy Battery II (30.5cm) | 18 | 36 | -6% | 1650 | 1 | Basic Heavy Battery |
| Heavy Battery III (38cm) | 22 | 40 | -7% | 1750 | 1 | Improved Heavy Battery |
| Heavy Battery IV (40.6cm) | 26 | 45 | -8% | 1850 | 1 Steel, 1 Chromium | Advanced Heavy Battery |
| Super-Heavy Battery (46cm) | 27 | 45 | -8% | 2000 | 1 Steel, 1 Chromium | Basic Heavy Battery (Super Heavy Battleship only) |

### Secondary batteries

Secondary batteries add light attack to capital ships (cruisers, battleships, carriers); they are secondary damage sources alongside main guns.

| Module | Light Attack | Light Piercing | Anti-Air | Max Speed | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|
| Secondary Battery I (75mm) | 3 | 5.5 | — | -2% | 180 | Naval Gunnery |
| Secondary Battery II (120mm) | 4 | 7 | — | -3% | 240 | Basic Medium Battery |
| Dual-Purpose Secondary Battery I (100mm) | 2 | 3 | 1 | -1% | 180 | Basic Dual-Purpose Battery |
| Dual-Purpose Secondary Battery II (113mm) | 3 | 4 | 2 | -1% | 240 | Basic Dual-Purpose Battery |
| Dual-Purpose Secondary Battery III (127mm) | 4 | 7 | 2.5 | -3% | 300 | Improved Dual-Purpose Battery |
| Dual-Purpose Secondary Battery IV (127mm RF) | 4.5 | 7 | 3 | -3% | 360 | Advanced Dual-Purpose Battery |

### Anti-air guns

All destroyer, cruiser, battleship, and carrier hulls can mount anti-air guns, which improve air defense against aircraft.

| Module | Anti-Air | Max Speed | Production Cost | Prerequisite |
|---|---|---|---|---|
| Anti-Air I (.50 cal MG) | 2.5 | -0.5% | 80 | Towed Artillery |
| Anti-Air II (20mm) | 3.5 | -0.5% | 110 | Towed Anti-Air |
| Anti-Air III (37mm) | 4.5 | -0.5% | 140 | Improved Anti-Air |
| Anti-Air IV (40mm Quad) | 5.5 | -0.5% | 170 | Advanced Anti-Air |

## Torpedoes and depth charges

### Ship torpedo launchers (surface ships)

Destroyers, cruisers, and Pre-Dreadnought battleships can mount torpedo launchers; they provide torpedo attack and hit chance bonuses.

| Module | Torpedo Attack | Torpedo Hit Chance | Max Speed | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|
| Torpedo Launcher I (3x 450mm) | 18 | — | -1% | 90 | Basic Torpedo |
| Torpedo Launcher II (4x 450mm) | 24 | +1% | -2% | 120 | Improved Ship Torpedo Launcher |
| Torpedo Launcher III (3x 533mm) | 30 | +1.5% | -3% | 150 | Advanced Ship Torpedo Launcher |
| Torpedo Launcher IV (4x 533mm) | 36 | +2% | -4% | 180 | Modern Ship Torpedo Launcher |

### Submarine torpedo tubes

All submarine hulls can mount torpedo tubes for their primary armament.

| Module | Torpedo Attack | Torpedo Hit Chance | Max Speed | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|
| Torpedo Tubes I (4x 450mm) | 14 | — | -1% | 80 | Early Submarine |
| Torpedo Tubes II (6x 450mm) | 18 | +1% | -2% | 100 | 1936 Submarine |
| Torpedo Tubes III (4x 533mm) | 22 | +1.5% | -3% | 120 | 1940 Submarine |
| Torpedo Tubes IV (6x 533mm) | 28 | +2% | -4% | 140 | 1944 Submarine |
| Nuclear Torpedo | 44 | +5%, -15% reliability | -5% | 520 | [Götterdämmerung] Nuclear Torpedo |

### Depth charges

Destroyers, cruisers and anti-submarine variants mount depth charges to counter enemy submarines. Depth charge value directly opposes submarine threat.

| Module | Depth Charges | Max Speed | Production Cost | Prerequisite |
|---|---|---|---|---|---|
| Depth Charge I (Rails) | 8 | -1% | 90 | Basic Depth Charges |
| Depth Charge II (Thrower) | 13 | -1% | 120 | Depth Charge Thrower |
| Depth Charge III (Anti-submarine Mortar) | 17 | -2% | 150 | Depth Charge Mortar |
| Depth Charge IV (Advanced Anti-submarine Mortar) | 22 | -2% | 180 | Improved Depth Charge Mortar |

## Detection and fire control

### Radar

Radar modules improve surface and submarine detection, boosting naval battle accuracy.

| Module | Surface Detection | Sub Detection | Light Battery Hit Chance | Heavy Battery Hit Chance | Anti-Air | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| Radar I (Decimetric Naval Search) | 5 | — | — | — | — | 100 | Radar |
| Radar II (Improved Decimetric) | 7 | 2 | +2.5% | +2.5% | +5% | 130 | Cavity Magnatron |
| Radar III (Centimetric Gunnery) | 12 | 6 | +5% | +5% | +7.5% | 160 | Phased Array |
| Radar IV (Integrated Fire Control) | 18 | 14 | +10% | +10% | +10% | 190 | Monopulse Radar |

### Sonar (destroyer/cruiser only)

Sonar modules improve submarine detection when mounted on destroyers and cruisers.

| Module | Sub Detection | Production Cost | Prerequisite |
|---|---|---|---|---|
| Hydrophones | 8 | 40 | Passive Sonar |
| Active Sonar | 12 | 60 | Active Sonar |
| Advanced Sonar | 16 | 80 | Advanced Sonar |
| Modern Sonar | 20 | 100 | Modern Sonar |

### Fire control systems (battleships and cruisers)

Fire control upgrades improve accuracy of light and heavy batteries.

| Module | Light Battery Hit Chance | Heavy Battery Hit Chance | Anti-Air | Production Cost | Prerequisite |
|---|---|---|---|---|---|---|
| Fire Control 0 (Central Rangefinding) | +2.5% | +2.5% | — | 60 | Electronic Mechanical Engineering |
| Fire Control I (Director Fire) | +5% | +5% | +10% | 135 | Basic Fire Control System |
| Fire Control II (Mechanical Rangekeeper) | +7.5% | +7.5% | +15% | 165 | Improved Fire Control System |
| Fire Control III (Ballistic Computer) | +10% | +10% | +20% | 225 | Advanced Fire Control System |

## Submarine specialty modules

### Snorkels (submerged diesel operation)

Snorkels allow submarines to run diesel engines while submerged, improving sub visibility but enabling faster movement while hidden.

| Module | Sub Visibility | Production Cost | Prerequisite |
|---|---|---|---|---|
| Basic Schnorkel | -7% | 50 | Basic Submarine Snorkel |
| Improved Schnorkel | -13% | 70 | Improved Submarine Snorkel |

### Anechoic tiles

Anechoic coatings reduce submarine detection at the cost of production time.

| Module | Sub Visibility | Production Cost | Rubber per dockyard | Prerequisite |
|---|---|---|---|---|
| Anechoic Tiles | -20% | +25% | 2 | Anechoic Tiles |

### Mine warfare and auxiliary

| Module | Effect | Eligible | Production Cost | Prerequisite |
|---|---|---|---|---|---|
| Minelaying Rails | +1 minelaying | All Destroyer / Cruiser | 90, -2% speed | Contact Mine |
| Minelaying Tubes | +1 minelaying | All Submarine | 90 | Minelaying Submarine |
| Minesweeping Gear | +1 minesweeping | All Destroyer | 30, -2% speed | Contact Mine |
| Floatplane Catapult | +7 surface detection, +2.5 sub detection | Cruiser / Battleship / Cruiser Sub | 150, -1% speed | Early Cruiser |
| Improved Floatplane Catapult | +10 surface detection, +3.5 sub detection | Cruiser / Battleship / Cruiser Sub | 170, -1% speed | Improved Airplane Catapult |

### Carrier hangar modules

| Module | Manpower | Deck Size | Max Speed | Production Cost | Steel per dockyard | Prerequisite |
|---|---|---|---|---|---|---|
| Hangar Space | 500 | +20 | -5% | 1500 | 1 | Deck Conversions |
| Floating Airfield Runway | 800 | +30 | -10% | 2000 | 2 | [Götterdämmerung] Ice Aircraft Carrier |

### Special submarine modules

| Module | Effect | Eligible | Production Cost | Prerequisite |
|---|---|---|---|---|---|
| Submarine Missile Launcher | +1500 production cost, -10% reliability | Fleet Submarine / Nuclear Submarine | 1500 | Missile Launching Submarine |
| Submarine Nuclear Missile Launcher | +20% sub visibility, -15% reliability | Nuclear Submarine only | 2000 | Nuclear Missile Submarine |
| Deck Gun | +5% sub visibility, +20% raiding efficiency | Cruiser Sub | 110 | Raiding Protocol special project |
| Fuel Tank | +1000 km range | Cruiser Sub / Fleet Sub / Nuclear Sub | +5% cost | Raiding Protocol special project |

## Worked example designs

These designs are built from the default ship variants shown in the wiki, demonstrating how modules combine into functional fleet units.

### Destroyer I (screen ship, early war)

| Component | Selection |
|---|---|
| **Hull** | Early Destroyer |
| **Engine** | Light Engine I (+10% speed) |
| **Gun** | Light Battery I (85mm, 1 light attack/piercing) |
| **Torpedo** | Torpedo Launcher I (18 torpedo attack) |
| **Anti-Air** | Anti-Air I (2.5 anti-air) |
| **Depth Charge** | Depth Charge I (8 depth charge) |
| **Fire Control** | Fire Control 0 (+2.5% accuracy) |

**Stats:** 34.95 kn max speed, 1500 km range, 25 HP, 80% reliability, 1 light piercing, 18 torpedo attack, 9 depth charges, 900 production cost. **Role:** Fast screen for early war, torpedo threat, basic anti-sub capability.

### Light Cruiser III (screen ship, mid-war)

| Component | Selection |
|---|---|
| **Hull** | 1940 Cruiser |
| **Engine** | Cruiser Engine III (+35% speed) |
| **Light Gun** | Light Cruiser Battery III (15.5cm, 6 light attack/8 piercing) |
| **Torpedo** | Torpedo Launcher III (30 torpedo attack) |
| **Anti-Air** | Anti-Air III (4.5 anti-air) |
| **Depth Charge** | Depth Charge III (17 depth charge) |
| **Secondary** | Light Cruiser Battery III (duplicate) |
| **Fire Control** | Fire Control 0 (+2.5% accuracy) |

**Stats:** 39.93 kn, 4000 km range, 160 HP, 90% reliability, 12 light attack, 8 light piercing, 32 torpedo attack, 6 depth charges, 3490 production cost. **Role:** Versatile mid-war screen; high speed and torpedo threat make it excellent for raiding and fleet actions.

### Battleship III (capital ship, late war)

| Component | Selection |
|---|---|
| **Hull** | 1940 Heavy Ship |
| **Engine** | Heavy Engine III (+45% speed) |
| **Main Gun** | Heavy Battery III (38cm, 22 heavy attack/40 piercing) |
| **Secondary** | Secondary Battery II (120mm, 4 light attack/7 piercing) |
| **Anti-Air** | Anti-Air IV + Anti-Air IV + Anti-Air IV (stacked for 16.5 total) |
| **Armor** | Battleship Armor III (40 armor, –20% torpedo crit, +20% torpedo damage reduction) |
| **Fire Control** | Fire Control 0 (+2.5% accuracy) |

**Stats:** 30.5 kn, 5000 km range, 575 HP, 90% reliability, 40 armor, 8 light attack, 44 heavy attack, 40 heavy piercing, 16.5 anti-air, 14041.25 production cost. **Role:** Late-war battleline; massive firepower and armor, slower speed managed by battleship role.

### Heavy Cruiser IV (capital ship support, late war)

| Component | Selection |
|---|---|
| **Hull** | 1944 Cruiser |
| **Engine** | Cruiser Engine II (+30% speed) |
| **Main Gun** | Heavy Cruiser Battery IV (20.3cm auto-loading, 12 heavy attack/34 piercing) |
| **Secondary** | Dual-Purpose Secondary Battery III (127mm, 4 light attack/7 piercing/2.5 anti-air) + Dual-Purpose Secondary Battery III |
| **Anti-Air** | Anti-Air IV (5.5) |
| **Fire Control** | Fire Control 0 (+2.5% accuracy) |

**Stats:** 34.5 kn, 5000 km range, 405 HP, 92% reliability, 13 armor, 11 light attack, 24 heavy attack, 34 heavy piercing, 21.5 anti-air, 6910 production cost. **Role:** Late-war heavy cruiser; combines serious firepower with speed for capital ship support and independent raiding.

### Submarine IV (convoy raider, late war)

| Component | Selection |
|---|---|
| **Hull** | 1944 Submarine |
| **Engine** | Submarine Engine IV (+20% speed) |
| **Torpedo** | Torpedo Tubes IV (6x 533mm, 28 torpedo attack) |
| **Torpedo (secondary)** | Torpedo Tubes II (6x 450mm, 18 torpedo attack — stacked) |

**Stats:** 21.2 kn, 3500 km range, 35 HP, 80% reliability, 10 sub visibility, 56 torpedo attack (from stacked tubes), 690 production cost. **Role:** Late-war convoy raider; high torpedo count overwhelms unescorted merchant traffic. Sub visibility and cost remain optimal for commerce war.

## Design principles

- **Screen vs capital:** Destroyers and light cruisers cost 500–2100 production per unit and can be fielded in numbers; cruisers trade speed for gun size; submarines trade speed for invisibility and range.
- **Armor tradeoff:** Increasing armor tier (Cruiser Armor I → IV) raises cost and reduces speed, but gains 2 armor per tier. Each tier also requires research (Basic/Inclined/All-or-Nothing Armor Scheme).
- **Torpedo versatility:** Nearly every non-battleship hull can mount torps; each tier (I–IV) boosts attack 6–30 points. Late-war submarines with stacked torpedo tubes (50+ attack) are lethal to capital ships.
- **Engine and fuel:** Base engine speed varies by hull size; engine modules add percentage bonuses (destroyers +10–25%, cruisers +20–40%, battleships +20–55%). Fuel usage scales with engine tier and is the primary supply constraint for task forces.
- **Fire control and radar:** Fire control adds accuracy (battleships and cruisers only); radar adds detection, which is crucial for naval engagements. A 1944 Battleship with Radar IV can detect enemies at 18+5=23 distance before being seen.
- **Reliability:** Early hulls (pre-1936) default to 65–80%; each armor/engine upgrade, and certain gun mounts, reduce reliability. Maintenance and officer skills can offset.

See also: [Naval doctrine](naval-doctrine.md), [Naval technology](naval-technology.md), [Naval support technology](naval-support-technology.md).
