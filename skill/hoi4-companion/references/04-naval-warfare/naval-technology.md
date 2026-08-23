---
title: Naval Technology
category: naval-warfare
tags: [naval, ships, destroyer, cruiser, battleship, carrier, submarine, man-the-guns, mtg, hull, module]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Naval_technology
  - https://hoi4.paradoxwikis.com/Naval_technology_(Basic)
---

## Summary

There are **two completely different naval technology trees** depending on whether **Man the Guns** is enabled. With it, the tree is a modular hull-and-module system where players design custom ships by combining hull types with modules (engines, armor, weapons, electronics). Without it, the legacy tree unlocks fixed equipment models directly (Destroyer I/II/III and so on). Both trees are documented here. All naval technologies generate naval engineering breakthrough progress while being researched (Patch 1.15+).

## Which tree applies

| Situation | Tree |
|---|---|
| **Man the Guns** enabled | Modular hull-and-module tree (below) — Destroyers, Cruisers, Battleships, Carriers, Submarines each with 4 hull generations (Early/1936/1940/1944) plus separate module technologies (armor schemes, engines, sonar, depth charges) |
| Man the Guns **not** enabled | Legacy tree — Fixed equipment designs: Destroyer I–IV, Light/Heavy Cruiser I–IV, Battlecruiser I–II, Battleship I–IV, Carrier I–IV, Submarine I–IV, plus Transports |

---

## Part 1 — Man the Guns naval technology (modular hulls and modules)

Ships have mandatory module slots (always-required mountings: engine, battery gun for most classes) plus optional front/middle/rear slots for customization. The number and type of optional slots varies by hull and generation.

### Destroyers

#### Destroyer Hulls

| Technology | Year | Base time | Prerequisites | Default design hull |
|---|---|---|---|---|
| **Early Destroyer** | 1922 | 165 days | – | 2 Steel · Service manpower 250 · Surface detection 20.0 · Sub detection 2.5 · Surface visibility 10.0 · Depth charges 1.0 · Max speed 32.0 kn · Max range 1500 km · HP 25.0 · Reliability 80.0% · Fuel usage 0.0 · Production cost 400 |
| **1936 Destroyer** | 1936 | 165 days | Early Destroyer | 2 Steel · Service manpower 325 · Surface detection 20.0 · Sub detection 3.0 · Surface visibility 10.0 · Depth charges 1.0 · Max speed 32.0 kn · Max range 1800 km · HP 40.0 · Reliability 85.0% · Fuel usage 0.0 · Production cost 500 |
| **1940 Destroyer** | 1940 | 165 days | 1936 Destroyer | 3 Steel · Service manpower 400 · Surface detection 20.0 · Sub detection 3.5 · Surface visibility 10.0 · Depth charges 1.0 · Max speed 32.0 kn · Max range 2000 km · HP 50.0 · Reliability 90.0% · Fuel usage 0.0 · Production cost 550 |
| **1944 Destroyer** | 1944 | 165 days | 1940 Destroyer | 4 Steel, 1 Chromium · Service manpower 500 · Surface detection 20.0 · Sub detection 4.0 · Surface visibility 10.0 · Depth charges 1.0 · Max speed 32.0 kn · Max range 2500 km · HP 60.0 · Reliability 92.0% · Fuel usage 0.0 · Production cost 600 |

#### Destroyer Modules

| Technology | Year | Base time | Prerequisites | Unlocks |
|---|---|---|---|---|
| **Basic Depth Charges** | 1922 | 165 days | Early Destroyer | Depth Charge Rails: Depth charges 8.0, Max speed -1%, Cost 90 |
| **Depth Charge Thrower** | 1936 | 165 days | Basic Depth Charges | Depth Charge Thrower: Depth charges 13.0, Max speed -1%, Cost 120 |
| **Depth Charge Mortar** | 1940 | 165 days | Depth Charge Thrower | Anti-submarine Mortar: Depth charges 17.0, Max speed -2%, Cost 150 |
| **Improved Depth Charge Mortar** | 1944 | 165 days | Depth Charge Mortar | Advanced Anti-submarine Mortar: Depth charges 22.0, Max speed -2%, Cost 180 |
| **Smoke Generators** | 1922 | 82 days | Early Destroyer | Global stats: Fleet speed while retreating +20% |
| **Passive Sonar** | 1922 | 165 days | Early Destroyer | Hydrophones: Sub detection 8.0, Cost 40 |
| **Active Sonar** | 1936 | 165 days | Passive Sonar | Active Sonar module: Sub detection 12.0, Cost 60 |

### Cruisers

#### Cruiser Hulls

| Technology | Year | Base time | Prerequisites | Default design hull |
|---|---|---|---|---|
| **Early Cruiser** | 1922 | 165 days | – | 1 Steel · Service manpower 600 · Surface detection 20.0 · Sub detection 1.0 · Surface visibility 15 · Max speed 27.0 kn · Max range 2500 km · HP 100 · Reliability 80.0% · Fuel usage 20.0 · Production cost 1800 |
| **1936 Cruiser** | 1936 | 165 days | Early Cruiser | 2 Steel · Service manpower 800 · Surface detection 20.0 · Sub detection 1.5 · Surface visibility 15 · Max speed 30.0 kn · Max range 3000 km · HP 110 · Reliability 85.0% · Fuel usage 20.0 · Production cost 1900 |
| **1940 Cruiser** | 1940 | 165 days | 1936 Cruiser | 2 Steel · Service manpower 1200 · Surface detection 20.0 · Sub detection 2.0 · Surface visibility 15 · Max speed 32.0 kn · Max range 4000 km · HP 120 · Reliability 90.0% · Fuel usage 20.0 · Production cost 2000 |
| **1944 Cruiser** | 1944 | 165 days | 1940 Cruiser | 3 Steel · Service manpower 1400 · Surface detection 20.0 · Sub detection 2.5 · Surface visibility 15 · Max speed 33.0 kn · Max range 4500 km · HP 130 · Reliability 95.0% · Fuel usage 20.0 · Production cost 2100 |

#### Cruiser Modules

| Technology | Year | Base time | Prerequisites | Unlocks |
|---|---|---|---|---|
| **Improved Airplane Catapult** | 1936 | 82 days | Early Cruiser | Improved Floatplane Catapult: Surface detection 10.0, Sub detection 3.5, Max speed -1%, Cost 170 |

### Cruiser & Battleship Armor

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| **Basic Cruiser Armor Scheme** | 1936 | 55 days | – | Cruiser Armor II module: 100mm Belt/30mm Deck, Max speed -7.5%, HP +5%, Armor 8.0, Cost +15% |
| **Inclined Belt Armor Scheme** | 1936 | 137 days | Basic Cruiser Armor Scheme | Battleship Armor II: 350mm Belt/150mm Deck, Max speed -5%, Torpedo damage reduction 0.1, Incoming torpedo critical chance -15%, HP +10%, Armor 36.0, Cost +20%. Battlecruiser Armor II: 305mm Belt/100mm Deck, Torpedo damage reduction 0.1, Incoming torpedo critical chance -10%, HP +10%, Armor 28.0, Cost +12.5%. Cruiser Armor III: 120mm Belt/50mm Deck, Max speed -10.0%, HP +10%, Armor 10.0, Cost +20% |
| **All-or-Nothing Armor Scheme** | 1936 | 137 days | Inclined Belt Armor Scheme | Battleship Armor III: 380mm Belt/155mm Deck, Max speed -10%, Torpedo damage reduction 0.2, Incoming torpedo critical chance -20%, HP +15%, Armor 40.0, Cost +17.5%. Battlecruiser Armor III: 330mm Belt/130mm Deck, Max speed -10%, Torpedo damage reduction 0.2, Incoming torpedo critical chance -15%, HP +15%, Armor 34.0, Cost +12.5%. Cruiser Armor IV: 150mm Belt/60mm Deck, Max speed -12.5%, HP +15%, Armor 12.0, Cost +25% |

### Battleships

| Technology | Year | Base time | Prerequisites | Default design hull |
|---|---|---|---|---|
| **Early Heavy Ship** | 1922 | 192 days | – | 1 Steel, 1 Chromium · Service manpower 4000 · Surface detection 20.0 · Sub detection 1.0 · Surface visibility 20.0 · Max speed 20.0 kn · Max range 3000 km · HP 350.0 · Armor 0.0 · Reliability 80.0% · Fuel usage 67.0 · Production cost 2800. Unlocks Battleship Armor I (200mm Belt/40mm Deck, Torpedo reduction 0.1, Incoming torpedo crit -10%, HP +5%, Armor 30.0) and Battlecruiser Armor I (150mm Belt/25mm Deck, Max speed +5%, Torpedo reduction 0.1, HP +5%, Armor 22.0) |
| **1936 Heavy Ship** | 1936 | 165 days | Early Heavy Ship | 1 Steel, 1 Chromium · Service manpower 5200 · Surface detection 20.0 · Sub detection 1.0 · Surface visibility 20.0 · Max speed 24.0 kn · Max range 3500 km · HP 370.0 · Armor 0.0 · Reliability 85.0% · Fuel usage 67.0 · Production cost 3000 |
| **1940 Heavy Ship** | 1940 | 165 days | 1936 Heavy Ship | 1 Steel, 1 Chromium · Service manpower 6000 · Surface detection 20.0 · Sub detection 1.0 · Surface visibility 20.0 · Max speed 25.0 kn · Max range 4000 km · HP 400 · Armor 0 · Reliability 90.0% · Fuel usage 67.0 · Production cost 3200 |
| **1944 Heavy Ship** | 1944 | 165 days | 1940 Heavy Ship | 1 Steel, 1 Chromium · Service manpower 6000 · Surface detection 20.0 · Sub detection 1.0 · Surface visibility 20.0 · Max speed 26.0 kn · Max range 4500 km · HP 450.0 · Armor 0.0 · Reliability 95.0% · Fuel usage 67.0 · Production cost 3400 |

### Carriers

#### Carrier Hulls

| Technology | Year | Base time | Prerequisites | Default design hull |
|---|---|---|---|---|
| **Deck Conversions** | 1922 | 192 days | – | Converted Battleship: 4 Steel, 1 Chromium, Service manpower 5000, Surface detection 26.0, Sub detection 5.0, Surface visibility 30.0, Max speed 25.0 kn, Max range 4000 km, HP 325.0, Reliability 65.0%, Fuel usage 87.0, Cost 2700. Converted Cruiser: 3 Steel, 1 Chromium, Service manpower 1000, Surface detection 26.0, Sub detection 5.0, Surface visibility 30.0, Max speed 22.5 kn, Max range 4000 km, HP 125.0, Reliability 65.0%, Fuel usage 87.0, Cost 2700. Unlocks Deck Armor (90mm, Max speed -5%, HP 25, Armor 5.0, Cost +10%), Hangar Space (Max speed -5%, Deck Size 20, Cost 1500) |
| **1936 Carrier** | 1936 | 165 days | Deck Conversions | 3 Steel, 1 Chromium · Service manpower 4500 · Surface detection 26.0 · Sub detection 5.0 · Surface visibility 30.0 · Max speed 26.0 kn · Max range 3000 km · HP 250.0 · Reliability 70.0% · Fuel usage 87.0 · Production cost 2094 |
| **1940 Carrier** | 1940 | 165 days | 1936 Carrier | 4 Steel, 1 Chromium · Service manpower 5000 · Surface detection 26.0 · Sub detection 5.0 · Surface visibility 30.0 · Max speed 26.0 kn · Max range 4000 km · HP 325.0 · Reliability 75.0% · Fuel usage 87.0 · Production cost 2600 |
| **1944 Carrier** | 1944 | 165 days | 1940 Carrier | 4 Steel, 2 Chromium · Service manpower 5500 · Surface detection 26.0 · Sub detection 5.0 · Surface visibility 30.0 · Max speed 26.0 kn · Max range 5000 km · HP 350.0 · Reliability 80.0% · Fuel usage 87.0 · Production cost 3250 |

#### Carrier Modules

| Technology | Year | Base time | Prerequisites | Unlocks |
|---|---|---|---|---|
| **Refined Pykrete** | 1942 | 110 days | Ice Carrier | Steel-Reinforced Pykrete Runway: 2 Steel, Max Speed -15%, Weather Penalty -10%, HP 35.0, Armor 4.0, Cost +15% |
| **Ice Composite Runways** | 1945 | 110 days | Refined Pykrete | Ice-Composite Runway: 3 Steel, Max Speed -15%, Weather Penalty -15%, HP 40.0, Armor 6.0, Cost +20% |

### Submarines

#### Submarine Hulls

| Technology | Year | Base time | Prerequisites | Default design hull |
|---|---|---|---|---|
| **Early Submarine** | 1922 | 165 days | Basic Torpedo | 1 Steel · Service manpower 200 · Surface detection 20.0 · Surface visibility 1.0 · Sub visibility 25.0 · Max speed 13.0 kn · Max range 2500 km · HP 10.0 · Reliability 60.0% · Fuel usage 1.0 · Production cost 320. Unlocks Torpedo Tubes I (4x 450mm, Torpedo attack 13.0, Max speed -1%, Cost 80) |
| **1936 Submarine** | 1936 | 165 days | Early Submarine | 2 Steel · Service manpower 200 · Surface detection 20.0 · Surface visibility 1.0 · Sub visibility 22.0 · Max speed 17.0 kn · Max range 4000 km · HP 20.0 · Reliability 70.0% · Fuel usage 1.0 · Production cost 350. Unlocks Torpedo Tubes II (6x 450mm, Torpedo attack 17.0, Max speed -2%, Torpedo hit chance +0.5%, Cost 100) |
| **1940 Submarine** | 1940 | 220 days | 1936 Submarine | 2 Steel · Service manpower 200 · Surface detection 20.0 · Surface visibility 1.0 · Sub visibility 20.0 · Max speed 18.0 kn · Max range 5000 km · HP 30.0 · Reliability 75.0% · Fuel usage 1.0 · Production cost 420. Unlocks Torpedo Tubes III (4x 533mm, Torpedo attack 20.0, Max speed -3%, Torpedo hit chance +1.0%, Cost 120) |
| **1944 Submarine** | 1944 | 220 days | 1940 Submarine | 3 Steel, 1 Chromium · Service manpower 200 · Surface detection 20.0 · Surface visibility 1.0 · Sub visibility 15.0 · Max speed 18.0 kn · Max range 6000 km · HP 35.0 · Reliability 80.0% · Fuel usage 1.0 · Production cost 550. Unlocks Torpedo Tubes IV (6x 533mm, Torpedo attack 25.0, Max speed -4%, Torpedo hit chance +1.5%, Cost 140) |

#### Submarine Modules

| Technology | Year | Base time | Prerequisites | Unlocks |
|---|---|---|---|---|
| **Basic Submarine Snorkel** | 1940 | 110 days | 1940 Submarine | Basic Snorkel module: Sub visibility -7%, Cost 50 |
| **Improved Submarine Snorkel** | 1944 | 220 days | Basic Submarine Snorkel | Improved Snorkel module: Sub visibility -13%, Cost 70 |
| **AIP-Diesel Combination Engines** | 1940 | 220 days | Air-Independent Propulsion | AIP-Diesel Combination Engine module: Sub visibility -17%, Max speed +15%, Max range -33%, Fuel usage 45.0, Cost +30% |
| **High-Speed Walter Engines** | 1944 | 220 days | AIP-Diesel Combination Engines | High Speed Walter Engines module: Sub visibility -20%, Max speed +35%, Fuel usage 30.0, Cost +35% |

### Secret Technologies (Man the Guns)

| Technology | Unlocked by | Effects |
|---|---|---|
| **Panzerschiff** | German Reich (starts with), East Germany (starts with), Argentina (via Recover The Ship focus) | Enables Panzerschiff hull |
| **Pre-Dreadnought Ships** | German Reich (starts with), Greece (starts with), Italy (via Bring Back Old Glories focus) | Enables Pre-Dreadnought hull |
| **Coastal Defense Ships** | Yugoslavia, Turkey, Sweden, Japan, Italy, Netherlands, Greece, Finland (start with); many nations via national focuses or decisions | Enables Coastal Defense Ship hull |

---

## Part 2 — Legacy naval technology (without Man the Guns)

Fixed equipment designs. All designs have fixed stats; players do not combine modules.

### Destroyers

| Technology | Year | Base time | Prerequisites | Resources | Light Atk | Light Pierce | Torpedo Atk | Depth Charges | Anti-Air | Max Speed | Max Range | HP | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Destroyer I** | 1922 | 165 days | – | 2 Steel | 1.0 | 1.0 | 18.0 | 9.0 | 2.5 | 31.9 kn | 1500 km | 25.0 | 80.0% | 14.0 | 911.25 |
| **Destroyer II** | 1936 | 220 days | Destroyer I | 2 Steel | 1.5 | 2.0 | 24.0 | 14.0 | 3.5 | 32.8 kn | 1800 km | 40.0 | 85.0% | 8.0 | 1184.50 |
| **Destroyer III** | 1940 | 220 days | Destroyer II | 3 Steel | 2.0 | 2.5 | 30.0 | 18.0 | 4.5 | 33.4 kn | 2000 km | 50.0 | 90.0% | 10.0 | 1351.25 |
| **Destroyer IV** | 1944 | 220 days | Destroyer III | 4 Steel, 1 Chromium | 3.0 | 2.5 | 36.0 | 23.0 | 10.5 | 34.3 kn | 2500 km | 60.0 | 92.0% | 10.0 | 1518.00 |

### Light Cruisers

| Technology | Year | Base time | Prerequisites | Resources | Light Atk | Light Pierce | Torpedo Atk | Anti-Air | Max Speed | Max Range | HP | Armor | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Light Cruiser I** | 1922 | 165 days | – | 2 Steel | 8.0 | 5.5 | 20.0 | 5.0 | 32.4 kn | 2500 km | 120.0 | 5.0 | 80.0% | 32.0 | 3116.50 |
| **Light Cruiser II** | 1936 | 220 days | Light Cruiser I or Heavy Cruiser II | 3 Steel | 10.0 | 7.0 | 26.0 | 9.0 | 35.7 kn | 3000 km | 140.0 | 6.0 | 85.0% | 36.0 | 3301.75 |
| **Light Cruiser III** | 1940 | 220 days | Light Cruiser II or Heavy Cruiser III | 3 Steel | 12.0 | 8.0 | 32.0 | 9.0 | 35.0 kn | 4000 km | 160.0 | 7.0 | 90.0% | 40.0 | 3528.00 |
| **Light Cruiser IV** | 1944 | 220 days | Light Cruiser III or Heavy Cruiser IV | 4 Steel, 1 Chromium | 15.0 | 9.0 | 38.0 | 11.0 | 33.0 kn | 4500 km | 180.0 | 8.0 | 92.0% | 40.0 | 4116.00 |

### Heavy Cruisers

| Technology | Year | Base time | Prerequisites | Resources | Light Atk | Light Pierce | Heavy Atk | Heavy Pierce | Anti-Air | Max Speed | Max Range | HP | Armor | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Heavy Cruiser I** | 1922 | 165 days | – | 3 Steel | 6.0 | 5.5 | 12.0 | 22.0 | 9.0 | 28.8 kn | 3000 km | 270.0 | 9.0 | 80.0% | 45.0 | 4830.00 |
| **Heavy Cruiser II** | 1936 | 220 days | Heavy Cruiser I or Light Cruiser II | 4 Steel | 7.0 | 6.2 | 16.0 | 25.0 | 9.0 | 33.6 kn | 4000 km | 315.0 | 11.0 | 85.0% | 36.0 | 5593.00 |
| **Heavy Cruiser III** | 1940 | 220 days | Heavy Cruiser II or Light Cruiser III | 4 Steel | 7.0 | 6.2 | 20.0 | 29.0 | 16.5 | 32.8 kn | 4500 km | 360.0 | 12.0 | 90.0% | 36.0 | 6392.00 |
| **Heavy Cruiser IV** | 1944 | 220 days | Heavy Cruiser III or Light Cruiser IV | 5 Steel, 1 Chromium | 11.0 | 6.5 | 24.0 | 34.0 | 21.5 | 34.4 kn | 5000 km | 405.0 | 13.0 | 92.0% | 36.0 | 7461.25 |

### Battlecruisers

| Technology | Year | Base time | Prerequisites | Resources | Light Atk | Light Pierce | Heavy Atk | Heavy Pierce | Anti-Air | Max Speed | Max Range | Torpedo Reduction | Incoming Torpedo Crit | HP | Armor | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Battlecruiser I** | 1922 | 165 days | – | 3 Steel, 1 Chromium | 6.0 | 5.5 | 28.0 | 31.0 | 8.0 | 30.2 kn | 3000 km | 0.1 | -10% | 367.5 | 22.0 | 80.0% | 87.0 | 7994.25 |
| **Battlecruiser II** | 1940 | 220 days | Battlecruiser I or Battleship III | 4 Steel, 1 Chromium | 6.0 | 5.5 | 32.0 | 33.5 | 14.5 | 32.0 kn | 5000 km | 0.1 | -10% | 440.0 | 58.0 | 90.0% | 87.0 | 10491.00 |

### Battleships

| Technology | Year | Base time | Prerequisites | Resources | Light Atk | Light Pierce | Heavy Atk | Heavy Pierce | Anti-Air | Max Speed | Max Range | Torpedo Reduction | Incoming Torpedo Crit | HP | Armor | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Battleship I** | 1922 | 165 days | – | 3 Steel, 1 Chromium | 7.0 | 6.2 | 28.0 | 31.0 | 7.5 | 21.7 kn | 3000 km | 0.1 | -10% | 367.5 | 30.0 | 80.0% | 87.0 | 12246.00 |
| **Battleship II** | 1936 | 220 days | Battleship I | 4 Steel, 1 Chromium | 7.0 | 6.2 | 36.0 | 36.0 | 13.5 | 26.7 kn | 4000 km | 0.1 | -15% | 495.0 | 36.0 | 85.0% | 92.0 | 12960.00 |
| **Battleship III** | 1940 | 220 days | Battleship II or Battlecruiser II | 4 Steel, 2 Chromium | 8.0 | 7.0 | 44.0 | 40.0 | 16.5 | 28.3 kn | 5000 km | 0.2 | -20% | 575.0 | 40.0 | 90.0% | 97.0 | 13650.00 |
| **Battleship IV** | 1944 | 220 days | Battleship III | 5 Steel, 3 Chromium | 9.0 | 7.0 | 52.0 | 45.0 | 21.5 | 31.5 kn | 6000 km | 0.2 | -20% | 632.5 | 80.0 | 92.0% | 102.0 | 15489.75 |
| **Super-Heavy Battleship II** | 1944 | 220 days | Super Heavy Battleship tech + Battleship II | 5 Steel, 3 Chromium | 9.0 | 4.0 | 54.0 | 45.0 | 22.5 | 29.4 kn | 4500 km | 0.2 | -25% | 880.0 | 58.0 | 90.0% | 128.0 | 27435.00 |

### Carriers

| Technology | Year | Base time | Prerequisites | Resources | Light Atk | Light Pierce | Anti-Air | Max Speed | Max Range | Deck Size | HP | Armor | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Carrier I** | 1922 | 165 days | – | 3 Steel, 1 Chromium | 3.0 | 5.5 | 13.0 | 29.8 kn | 3000 km | 8 | 250.0 | 7.0 | 70.0% | 99.0 | 7964.00 |
| **Carrier II** | 1936 | 220 days | Carrier I | 4 Steel, 1 Chromium | 3.0 | 5.5 | 13.0 | 30.4 kn | 4000 km | 10 | 325.0 | 9.0 | 80.0% | 99.0 | 8822.00 |
| **Carrier III** | 1940 | 220 days | Carrier II | 4 Steel, 2 Chromium | 3.0 | 5.5 | 13.5 | 30.3 kn | 5000 km | 14 | 350.0 | 11.0 | 85.0% | 99.0 | 11110.00 |
| **Carrier IV** | 1944 | 220 days | Carrier III | 5 Steel, 2 Chromium | 3.0 | 5.5 | 15.5 | 32.0 kn | 6000 km | 16 | 350.0 | 13.0 | 90.0% | 99.0 | 11935.00 |

### Submarines

| Technology | Year | Base time | Prerequisites | Resources | Torpedo Atk | Max Speed | Max Range | Sub Visibility | HP | Reliability | Fuel Usage | Production Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Submarine I** | 1922 | 165 days | – | 1 Steel | 15.0 | 13.5 kn | 2000 km | 30.0 | 10.0 | 60.0% | 8.0 | 363.00 |
| **Submarine II** | 1936 | 220 days | Submarine I | 2 Steel | 26.0 | 17.5 kn | 2500 km | 25.0 | 20.0 | 70.0% | 8.0 | 451.00 |
| **Submarine III** | 1940 | 220 days | Submarine II | 2 Steel | 42.0 | 18.3 kn | 3000 km | 15.0 | 30.0 | 75.0% | 8.0 | 583.00 |
| **Submarine IV** | 1944 | 220 days | Submarine III | 3 Steel, 1 Chromium | 54.0 | 18.1 kn | 3500 km | 10.0 | 35.0 | 80.0% | 8.0 | 660.00 |

### Transports

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| **Transport Ship** | 1922 | 165 days | – | Troop convoy requirements -33%, Naval invasion capacity +10 |
| **Landing Craft** | 1940 | 220 days | Transport Ship | Invasion preparation time -25%, Invasion defense +15%, Naval invasion capacity +20 |
| **Advanced Landing Craft** | 1944 | 220 days | Landing Craft | Invasion defense +50%, Naval invasion capacity +100, Amphibious invasion preparation speed +25% |
| **Multi-Product Supply Ship** | 1938 | 220 days | Underway Replenishment + Transport Ship | Underway Replenishment Range +25%, Underway Replenishment Convoy Usage -20% |
| **Standardized Tenshioned Replenishment Alongside Method** | 1943 | 275 days | Multi-Product Supply Ship | Underway Replenishment Range +25%, Underway Replenishment Convoy Usage -20% |

### Secret Technologies (Legacy)

| Technology | Unlocked by | Effects |
|---|---|---|
| **Panzerschiff** | German Reich (starts with), East Germany (starts with), Argentina (via Recover The Ship focus) | Enables Panzerschiff hull |
| **Pre-Dreadnought Ships** | German Reich (starts with), Greece (starts with), Italy (via Bring Back Old Glories focus) | Enables Pre-Dreadnought hull |
| **Coastal Defense Ships** | Yugoslavia, Turkey, Sweden, Japan, Italy, Netherlands, Greece, Finland (start with); many nations via national focuses or decisions | Enables Coastal Defense Ship hull |

## Research notes

**Inferred:**
- In the Man the Guns tree, **hull technologies are the expensive bottleneck** (165–192 days each), while most modules are cheap (42–110 days). Prioritize the hull generation(s) you will build.
- **Engine modules unlock as bonus effects** of hull technologies; they provide Max Speed bonuses (10–45% depending on technology and hull type). Research high-speed modules for cruisers and submarines, which benefit from mobility.
- **Armor modules are separate technologies** (Basic Cruiser Armor Scheme onwards) and trade Max Speed for durability. Decide the speed-armor tradeoff per ship class.
- In the legacy tree, all designs are fixed. **Battleships and Battlecruisers are extremely expensive** (12,000–27,000 production cost) and slow — valuable for heavy firepower but not for fleet speed. Submarines and carriers offer alternative strategic effects without the cost.
- **Chromium gates heavy and late-generation ships** (1944 hulls, Super-Heavy Battleship). Verify resource access before committing to a battleship program.
- Sonar and depth-charge technologies matter in convoy raiding: passive sonar (1922) is free detection; active sonar (1936) improves it; depth-charge mortars (1940/1944) increase kill chance.

## See also

- [Ship designer](../04-naval-warfare/ship-designer.md)
- [Naval doctrine](../04-naval-warfare/naval-doctrine.md)
- [Naval support technology](../04-naval-warfare/naval-support-technology.md)
