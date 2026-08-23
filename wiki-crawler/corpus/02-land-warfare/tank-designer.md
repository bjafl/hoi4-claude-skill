---
title: Tank Designer
category: land-warfare
tags: [tank-designer, tanks, armor, chassis, modules, variants, land-cruiser, no-step-back, production-cost, reliability]
game_version: "1.19"
dlc: [No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Tank_designer
  - https://hoi4.paradoxwikis.com/Armor_technology
  - https://hoi4.paradoxwikis.com/Military_industrial_organization
---

## Summary

The tank designer (**requires No Step Back**) replaces fixed tank equipment with modular designs: pick a chassis, then an engine, suspension, armor type, turret, main gun, and up to four special modules, plus separately-levelled engine and armor upgrades. The chosen **role** (tank / tank destroyer / artillery / anti-air / flame / amphibious) further modifies the finished stats. Chassis, engine and armor modules come from the **armor technology** tree; main guns come from **artillery technology**; radios and other support modules come from the common trees (engineering, etc.).

## Design rules

- Every design **must** have an engine type, a suspension, an armor type and a turret module to be valid. Defaults: **Gasoline Engine**, **Bogie Suspension**, **Riveted Armor**.
- The **chassis type sets the maximum turret size**, and the **turret sets the maximum armament size**. Smaller weapons can always be mounted.
- A **fixed superstructure** mounts a gun one size class larger than the equivalent turret, gives +20% reliability and +3 defense, but costs **-25% breakthrough** and **cannot mount anti-air guns** (it cannot elevate or track aircraft).
- All tank chassis have **four special module slots**, which may be left empty.
- **Secondary turret limits by chassis:** Light 1 · Medium 2 · Heavy and Super-Heavy 4 · Amphibious and Modern **none**.
- Only **one radio** module per chassis. Tank Unique Special Modules are limited to **one of each**; ordinary Tank Special Modules may be stacked freely (within the 4 slots).
- Mounting an **anti-air gun** or a **rocket launcher** disqualifies the design from being a "tank" — it can only be an anti-air / artillery variant.
- Land Cruiser chassis use an entirely separate module set (see below) and feed the Land Cruiser support company.
- Non-tracked suspensions are **light chassis only**.

## Chassis

### Tank chassis

| Chassis | Type | Year | Max Speed | Armor | Hardness | Reliability | Production Cost | Resources / factory | Service Manpower | Unlocked by |
|---|---|---|---|---|---|---|---|---|---|---|
| Inter-War Light Tank Chassis | Light | 1922 | 5.1 km/h | 10 | 80% | 80% | 2 | 1 Steel | 2 | Inter-War Tank Development |
| Basic Light Tank Chassis | Light | 1934 | 6.3 km/h | 15 | 80% | 95% | 2.35 | 1 Steel | 2 | Basic Light Tank Chassis |
| Improved Light Tank Chassis | Light | 1936 | 7.4 km/h | 20 | 80% | 110% | 2.7 | 1 Steel | 2 | Improved Light Tank Chassis |
| Advanced Light Tank Chassis | Light | 1942 | 8.6 km/h | 25 | 80% | 130% | 3 | 2 Steel | 2 | Advanced Light Tank Chassis |
| Inter-War Medium Tank Chassis | Medium | 1922 | 5.1 km/h | 20 | 85% | 75% | 3.5 | 1 Steel | 2 | Inter-War Tank Development |
| Basic Medium Tank Chassis | Medium | 1938 | 6.3 km/h | 30 | 85% | 80% | 3.75 | 1 Steel | 2 | Basic Medium Tank Chassis |
| Improved Medium Tank Chassis | Medium | 1940 | 7.4 km/h | 40 | 85% | 100% | 4 | 1 Steel | 2 | Improved Medium Tank Chassis |
| Advanced Medium Tank Chassis | Medium | 1943 | 7.4 km/h | 50 | 85% | 120% | 4.25 | 2 Steel | 2 | Advanced Medium Tank Chassis |
| Inter-War Heavy Tank Chassis | Heavy | 1922 | 4 km/h | 35 | 95% | 75% | 9 | 1 Steel | 2 | Inter-War Tank Development |
| Basic Heavy Tank Chassis | Heavy | 1934 | 6.3 km/h | 55 | 95% | 80% | 10 | 1 Steel | 2 | Basic Heavy Tank Chassis |
| Improved Heavy Tank Chassis | Heavy | 1940 | 6.3 km/h | 60 | 95% | 110% | 11 | 1 Steel, 1 Chromium | 2 | Improved Heavy Tank Chassis |
| Advanced Heavy Tank Chassis | Heavy | 1943 | 6.3 km/h | 75 | 95% | 120% | 12 | 2 Steel, 1 Chromium | 2 | Advanced Heavy Tank Chassis |
| Modern Tank Chassis | Modern | 1945 | 8.6 km/h | 65 | 95% | 120% | 6 | 2 Steel, 1 Chromium | 2 | Modern Tank Chassis |
| Super-Heavy Tank Chassis | Super-Heavy | 1943 | 4.9 km/h | 90 | 100% | 100% | 28 | 3 Steel, 2 Chromium | 2 | Super-Heavy Tank Chassis |
| Amphibious Tank Chassis | Amphibious | 1938 | 6.3 km/h | 15 | 85% | 110% | 4.5 | 1 Steel | 2 | Amphibious Tank Chassis |

Note the Modern Tank Chassis: **65 armor, 8.6 km/h and only 6 production cost** — dramatically cheaper per point of armor than heavy chassis, but it cannot mount secondary turrets.

### Land Cruiser chassis

Feeds the **Land Cruiser** support company.

| Chassis | Type | Year | Max Speed | Armor | Reliability | Production Cost | Resources / factory | Service Manpower | Unlocked by |
|---|---|---|---|---|---|---|---|---|---|
| Land Cruiser Chassis | Land Cruiser | 1943 | 5 km/h | 150 | 100% | 330 | 8 Steel, 4 Chromium | 30 | Land Cruiser |

## Engine

### Engine types

| Module | Max Speed | Breakthrough | Defense | Reliability | Fuel Usage | Production Cost | Design Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| **Gasoline Engine** (default) | +0.5 km/h, +15% | – | – | – | 2 | 1 | Default (else 6 army XP) | – |
| **Diesel Engine** | – | – | – | **+25%** | 2 | 1 | 6 army XP | – |
| **Petrol-Electric Engine** | – | +2, +15% | +2, +15% | **-50%** | 2 | 2, +15% | 6 army XP | – |
| **Gas Turbine** | +0.5 km/h, **+25%** | – | – | -10% | 4 | 3 | 6 army XP | Jet Engine |

### Engine upgrade levels

Levels 0–20, each level identical and stacking:

| Per level | Value |
|---|---|
| Max Speed | +0.1 km/h |
| Fuel Usage | +0.05 |
| Reliability | -1.5% |
| Production Cost | +0.1 |
| Design Cost | +1 army XP |

| Levels available | Requires |
|---|---|
| 0–4 | – |
| 5–9 | Basic Engine |
| 10–14 | Improved Engine |
| 15–17 | Advanced Engine |
| 18–20 | Modern Engine |

## Suspension

### Tracked (all chassis)

| Module | Max Speed | Breakthrough | Reliability | Production Cost | Design Cost |
|---|---|---|---|---|---|
| **Bogie Suspension** (default) | – | – | – | – | Default (else 6 army XP) |
| **Christie Suspension** | +20% | – | – | 1 | 6 army XP |
| **Interleaved Roadwheels** | – | +4 | – | 2 | 6 army XP |
| **Torsion Bar** | – | – | +15% | 1 | 6 army XP |

### Non-tracked (light chassis only)

| Module | Hardness | Reliability | Production Cost | Design Cost | Prerequisite |
|---|---|---|---|---|---|
| **Half-track Suspension** | -30% | -10% | -5% | 6 army XP | Mechanized Equipment I |
| **Wheeled Suspension** | -40% | -20% | -10% | 6 army XP | Early Truck |

## Armor

### Armor types

| Module | Armor | Breakthrough | Defense | Hardness | Production Cost | Resources | Design Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| **Riveted Armor** (default) | – | 2 | 2 | – | **-20%** | – | Default (else 8 army XP) | – |
| **Cast Armor** | +30% | 3 | 3 | +2% | **+20%** | – | 8 army XP | – |
| **Welded Armor** | +30% | 4 | 4 | – | – | 1 Chromium | 8 army XP | Basic Armor Protection |
| **Makeshift Armor** | – | 0 | 1 | -30% | **-30%** | – | 8 army XP | Norway only, via Rikstanken |

### Armor upgrade levels

Levels 0–20, each level identical and stacking:

| Per level | Value |
|---|---|
| Breakthrough | +1.2 |
| Armor | +2.5 |
| Max Speed | -0.1 km/h |
| Reliability | -1.5% |
| Production Cost | +0.2 |
| Design Cost | +1 army XP |

| Levels available | Requires | Resource note |
|---|---|---|
| 0–4 | – | – |
| 5–9 | Basic Armor Protection | +1 Steel at level 5 and above |
| 10–14 | Improved Armor Protection | +1 Steel |
| 15–17 | Advanced Armor Protection | +1 Steel |
| 18–20 | Modern Armor Protection | +1 Steel |

## Turret

Turrets are the main source of breakthrough (they represent visibility, crew workspace and workload).

| Module | Allowed chassis | Role restriction | Max armament | Max Speed | Soft Atk | Hard Atk | Breakthrough | Defense | Reliability | Prod. Cost | Design Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Light Fixed Superstructure | Light, Medium, Heavy, Super-Heavy | no Anti-air | Medium | – | – | – | **-25%** | 3 | +20% | 1 | 2 army XP |
| Light One Man Turret | Light, Medium, Heavy, Super-Heavy | – | Small | – | – | – | 7 | – | – | 1 | 2 army XP |
| Light Two Man Turret | Light, Medium, Heavy, Super-Heavy | – | Small | – | – | – | 10 | – | – | 1.25 | 2 army XP |
| Light Three Man Turret | Light, Medium, Heavy, Super-Heavy | – | Small | -0.1 km/h | – | – | 14 | – | – | 1.5 | 2 army XP |
| Medium Fixed Superstructure | Medium, Heavy, Super-Heavy | no Anti-air | Heavy | – | – | – | **-25%** | 3 | +20% | 1.5 | 2 army XP |
| Medium One Man Turret | Medium, Heavy, Super-Heavy | – | Medium | – | -5% | -5% | 8 | – | – | 1.25 | 2 army XP |
| Medium Two Man Turret | Medium, Heavy, Super-Heavy | – | Medium | – | – | – | 16 | – | – | 1.75 | 2 army XP |
| Medium Three Man Turret | Medium, Heavy, Super-Heavy | – | Medium | -0.2 km/h | – | – | 24 | – | – | 2.25 | 2 army XP |
| Heavy Fixed Superstructure | Heavy, Super-Heavy | no Anti-air | Super-Heavy | – | – | – | **-25%** | 3 | +20% | 5 | 2 army XP |
| Heavy Two Man Turret | Heavy, Super-Heavy | – | Heavy | – | – | – | 18 | – | – | 5 | 2 army XP |
| Heavy Three Man Turret | Heavy, Super-Heavy | – | Heavy | -0.2 km/h | – | – | 22 | – | – | 5.5 | 2 army XP |
| Super-Heavy Three Man Turret | Super-Heavy | – | Super-Heavy | -0.2 km/h | – | -10% | 24 | – | -10% | 10, +50% | 2 army XP |
| Super-Heavy Four Man Turret | Super-Heavy | – | Super-Heavy | -0.5 km/h | – | – | 35 | – | -25% | 12, +50% | 2 army XP |
| Modern Turret | Modern | – | Heavy | – | – | – | 24 | – | – | 8 | 2 army XP |
| Improvised Turret | Light | – | Small | – | – | – | 1 | – | -25% | 0.1 | 2 army XP |

## Weapons

### Small armaments (any chassis with a large enough turret)

| Module | Role restriction | Size | Brk | Soft Atk | Hard Atk | Air Atk | Max Speed | Piercing | Reliability | Prod. Cost | Resources | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heavy Machine Gun | – | Small | – | 8 | 2 | – | – | 6 | – | 0.5 | – | Basic Infantry equipment |
| Automatic Cannon | – | Small | – | 15 | 5 | – | -0.1 | 20 | -10% | 1.5 | – | Towed Anti-Air |
| Improved Automatic Cannon | – | Small | – | 20 | 7 | – | -0.1 | 35 | -10% | 2 | – | Improved Anti-Air |
| Basic Anti-Air Gun | Anti-air only (no Tank) | Small | – | 6 | 2 | 18 | – | 10 | -10% | 2 | – | Towed Anti-Air |
| Improved Anti-Air Gun | Anti-air only (no Tank) | Small | – | 8 | 5 | 32 | – | 18 | -10% | 3 | 2 Steel, 1 Tungsten | Improved Anti-Air |
| Advanced Anti-Air Gun | Anti-air only (no Tank) | Medium | – | 10 | 5 | 46 | – | 24 | -10% | 4 | 3 Steel, 1 Tungsten | Advanced Anti-Air |
| Small Cannon | – | Small | – | 10 | 6 | – | -0.1 | 25 | -10% | 1.5 | – | Towed Artillery |
| Improved Small Cannon | – | Small | – | 15 | 15 | – | -0.1 | 50 | -10% | 3 | – | Inter-War Artillery |
| Medium Cannon | TD; not Light Tank | Medium | +2 | 20 | 15 | – | -0.2 | 60 | -15% | 3 | 1 Steel, 1 Tungsten | Improved Artillery |
| Improved Medium Cannon | TD; not Light Tank | Medium | +4 | 32 | 20 | – | -0.3 | 90 | -15% | 4 | 2 Steel, 1 Tungsten, 1 Chromium | Advanced Artillery **or** Improved Anti-Tank Upgrade I |
| Close Support Gun | Artillery | Small | – | 22 | 5 | – | -0.2 | 10 | -10% | 4 | 1 Steel | Inter-War Artillery |
| Medium Howitzer | Artillery; not Light Tank | Medium | -2 | 35 | 1 | – | -0.3 | 20 | -20% | 4 | 2 Steel, 1 Tungsten | Improved Artillery |
| Improved Medium Howitzer | Artillery; not Light Tank | Medium | -2 | 45 | 2 | – | -0.4 | 30 | -20% | 5.5 | 3 Steel, 1 Tungsten, 1 Chromium | Improved Artillery Upgrade II |
| Rocket Launcher | Artillery only (no Tank) | Medium | -4 | 25 | 1 | – | -0.1 | 2 | -10% | 4 | 1 Steel, 2 Tungsten | Towed Rocket Artillery |
| Improved Rocket Launcher | Artillery only (no Tank) | Medium | -4 | 35 | 1 | – | -0.2 | 2 | -10% | 5 | 1 Steel, 2 Tungsten | Advanced Rocket Artillery |
| Basic High-Velocity Cannon | Tank destroyer | Small | – | 10 | 26 | – | -0.1 | 68 | -5% | 3 | 2 Steel, 2 Tungsten | Towed Anti-Tank |
| Improved High-Velocity Cannon | TD; not Light Tank | Medium | – | 20 | 35 | – | -0.3 | 125 | -17.5% | 5 | 2 Steel, 2 Tungsten, 1 Chromium | Improved Anti-Tank Upgrade II |
| Advanced High-Velocity Cannon | TD; not Medium Tank | Heavy | – | 25 | 45 | – | -0.4 | 200 | -20% | 7 | 3 Steel, 2 Tungsten, 1 Chromium | Advanced Anti-Tank |
| Basic Heavy Cannon | TD; not Medium Tank | Heavy | – | 20 | 20 | – | -0.3 | 90 | -25% | 6 | 2 Steel, 1 Tungsten, 1 Chromium | Towed Anti-Air **or** Towed Anti-Tank |
| Improved Heavy Cannon | TD; not Medium Tank | Heavy | – | 25 | 35 | – | -0.4 | 125 | -25% | 7 | 2 Steel, 2 Tungsten, 1 Chromium | Improved Anti-Air Upgrade I **or** Improved Anti-Tank |
| Advanced Heavy Cannon | TD; not Medium Tank | Heavy | – | 30 | 40 | – | -0.5 | 170 | -30% | 8 | 3 Steel, 3 Tungsten, 1 Chromium | Advanced Anti-Air **or** Advanced Anti-Tank |
| Heavy Howitzer | Artillery; not Medium Tank | Heavy | -4 | 55 | 2 | – | -0.5 | 60 | -30% | 7 | 3 Steel, 1 Tungsten, 1 Chromium | Advanced Artillery Upgrade |
| Super-Heavy Cannon | TD; not Heavy/Modern Tank | Super-heavy | – | 35 | 45 | – | -0.6 | 225 | -35% | 12.5 | 5 Tungsten, 2 Chromium | Super-Heavy Tank Chassis |

### Flamethrowers (light, medium or heavy chassis only)

| Module | Role | Size | Breakthrough | Soft Attack | Reliability | Prod. Cost | Design Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|
| Flamethrower | Flame | Small | – | 5 | -5% | 0.5 | 1 army XP | Flamethrower Tank |
| Advanced Flamethrower | Flame | Small | +6 | 12 | -5% | 1.2 | 1 army XP | Advanced Flamethrower |

## Tank auxiliary modules (4 slots)

### Secondary turrets

Limits: Light 1 · Medium 2 · Heavy/Super-Heavy 4 · Amphibious and Modern **cannot mount any**.

| Module | Breakthrough | Soft Attack | Hard Attack | Reliability | Prod. Cost | Design Cost | Prerequisite |
|---|---|---|---|---|---|---|---|
| Heavy Machine Gun | – | 4 | – | – | 1.5 | 1 army XP | Basic Infantry equipment |
| Small Cannon | 2 | 5 | 3 | -10% | 3 | 1 army XP | Towed Artillery |

### Radios (one per chassis)

| Module | Defense | Breakthrough | Prod. Cost | Design Cost | Prerequisite |
|---|---|---|---|---|---|
| Basic Radio | +20% | +15% | 0.5 | 1 army XP | Radio |
| Improved Radio | +40% | +25% | 1.5 | 1 army XP | Improved Radio |
| Advanced Radio | +60% | +40% | 2.5 | 1 army XP | Advanced Radio |

### Tank special modules (stackable)

| Module | Soft Atk | Defense | Breakthrough | Fuel Capacity | Max Speed | Reliability | Prod. Cost | Design Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|
| Additional Machineguns | 1 | 2 | – | – | – | – | 0.5 | 1 army XP | Basic Infantry equipment |
| Extra Ammunition Storage | – | 4 | 2 | – | – | -10% | – | 1 army XP | – |
| Fuel Drum | – | – | – | +100 | -0.2 km/h | – | 1 | 3 army XP | – |
| Smoke Launchers | – | 2 | 1 | – | – | – | 0.5 | 1 army XP | – |

### Tank unique special modules (max one of each)

| Module | Allowed chassis | Role | Defense | Piercing | Armor | Breakthrough | Entrench. | Reliability | Prod. Cost | Resources | Design Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amphibious Drive | Light, Medium, Heavy | Amphibious only | – | – | – | – | – | -15% | 2, +10% | – | 1 army XP | Amphibious Drive |
| Armor Skirts | L, M, H, SH, Modern | – | – | – | 3 | 3 | – | – | 0.5 | – | 1 army XP | Improved Armor Protection |
| Auto Loader | L, M, H, SH, Modern | – | 4 | – | – | 4 | – | – | 1.5 | – | 1 army XP | Advanced Artillery Upgrade / Advanced Anti-Air / Advanced Anti-Tank |
| Dozer Blade | L, M, H, SH, Modern | – | – | – | – | – | 1 | – | 1 | – | 1 army XP | Engineer Company II |
| Easy Maintenance | L, M, H, SH, Modern | – | – | – | – | – | – | **+10%** | **-7.5%** | – | **30 army XP** | Maintenance Company II |
| Squeeze-bore Adaptor | L, M, H, SH, Modern | – | – | **+10%** | – | – | – | – | – | +1 Tungsten | 1 army XP | Anti-Tank Upgrade |
| Sloped Armor | L, M, H, SH, Modern | – | – | – | **+25%** | – | – | – | +10% | – | **10 army XP** | – |
| Stabilizer | L, M, H, SH, Modern | – | – | – | – | 5 | – | – | 2 | – | 1 army XP | Improved Computing Machine |
| Wet Ammunition Storage | L, M, H, SH, Modern | – | – | – | – | – | – | **+15%** | 1 | – | 1 army XP | – |

## Land Cruiser modules

Land Cruisers use a wholly separate module set on the Land Cruiser Chassis.

### Main armament

| Module | Brk | Soft Atk | Hard Atk | Air Atk | Max Speed | Piercing | Reliability | Prod. Cost | Resources | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|
| Heavy Anti-Air Platform | 20 | 20 | 10 | 80 | – | 50 | -5% | 10.0 | 5 Steel, 3 Tungsten | Advanced Anti-Air |
| Heavy Naval Guns | 40 | 60 | 55 | – | -0.6 km/h | 240 | -20% | 20.0 | 7 Tungsten, 4 Chromium | – |
| Super-Heavy Railway Gun | 30 | 80 | 8 | – | -0.5 km/h | 80 | -15% | 16.0 | 5 Steel, 5 Tungsten, 3 Chromium | Super-Heavy Railway Gun |
| High-Impact Obliterator Cannon | 25 | 35 | 75 | – | -0.4 km/h | 280 | -10% | 15.0 | 4 Steel, 7 Tungsten, 3 Chromium | High-Impact Obliterator Cannon |

### Secondary armament

| Module | Brk | Soft Atk | Hard Atk | Extra Collateral | Air Atk | Max Speed | Piercing | Reliability | Prod. Cost | Resources | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Heavy Anti-Air Battery | 10 | 14 | 7 | – | 60 | – | 40 | – | 7.0 | 4 Steel, 2 Tungsten | Improved Anti-Air |
| Medium Naval Guns | 25 | 42 | 52 | – | – | -0.4 km/h | 230 | -10% | 16.0 | 6 Tungsten, 3 Chromium | – |
| Hull-Mounted Railway Gun | 15 | 70 | 5 | – | – | -0.4 km/h | 70 | -10% | 14.0 | 4 Steel, 3 Tungsten, 2 Chromium | Railway Gun |
| Heavy High-Velocity Cannon | 15 | 30 | 55 | – | – | -0.3 km/h | 250 | -5% | 12.0 | 4 Steel, 4 Tungsten, 2 Chromium | Advanced Anti-Tank |
| Super-Heavy Howitzer | 20 | 65 | 4 | 500 | – | -0.4 km/h | 65 | -10% | 12.0 | 4 Steel, 3 Tungsten, 2 Chromium | – |

### Additional armament

| Module | Brk | Soft Atk | Hard Atk | Extra Collateral | Air Atk | Max Speed | Piercing | Reliability | Prod. Cost | Resources | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Flamethrower Turret | 8 | 8 | – | – | – | – | – | -5% | 1.0 | 1 Steel | Flamethrower Tank |
| Light Anti-Air Battery | – | 10 | 5 | – | 46 | – | 30 | – | 4.0 | 3 Steel, 1 Tungsten | Towed Anti-Air |
| Medium Cannon Turret | 8 | 32 | 20 | – | – | -0.2 km/h | 90 | -5% | 4.0 | 2 Steel, 1 Tungsten, 1 Chromium | Improved Artillery |
| High-Velocity Cannon Turret | 4 | 25 | 45 | – | – | -0.3 km/h | 200 | -5% | 7.0 | 3 Steel, 2 Tungsten, 1 Chromium | Towed Anti-Tank |
| Assault Gun | 16 | 55 | 2 | 250 | – | -0.3 km/h | 40 | -10% | 8.0 | 3 Steel, 1 Tungsten, 1 Chromium | Improved Artillery |
| Rocket Launcher | 4 | 35 | 1 | – | – | -0.2 km/h | 2 | -5% | 5.0 | 1 Steel, 2 Tungsten | Towed Rocket Artillery |

### Land Cruiser special features

**Aerial deployment**

| Module | Defense | Recon | Air Attack | Fuel Usage | Prod. Cost | Prerequisite |
|---|---|---|---|---|---|---|
| Aircraft Catapult | 1 | 5 | 2 | 2 | 6 | – |
| Helipad | 1 | 8 | 2 | 1 | 4 | Helicopter |

**Structural features**

| Module | Defense | Brk | Soft Atk | Max Speed | Armor | Fuel Usage | Fuel Capacity | Reliability | Prod. Cost | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|
| Bunker Emplacement | 10 | 10 | 10 | – | 8 | 1 | – | – | 8 | Improved Land Forts |
| Internal Ammunition Compartments | 4 | 2 | – | – | – | – | – | -5% | – | – |
| Internal Fuel Tanks | – | – | – | -0.2 km/h | – | – | 150 | – | 2 | – |
| Stabilizers | – | 6 | – | – | – | – | – | – | 3 | Improved Computing Machine |
| Wet Ammunition Storage | – | – | – | – | – | – | – | +15% | 2 | – |

**External features**

| Module | Defense | Breakthrough | Air Attack | Prod. Cost | Prerequisite |
|---|---|---|---|---|---|
| Armored Skirts | 6 | 6 | – | 8 | Advanced Armor Protection |
| Radar | +10% | – | +50% | 10 | Radar |
| Smoke Generators | 2 | 3 | – | 2 | – |

**Radio systems**

| Module | Defense | Breakthrough | Prod. Cost | Prerequisite |
|---|---|---|---|---|
| Basic Radio | +20% | +15% | 2 | Radio |
| Improved Radio | +40% | +25% | 4 | Improved Radio |
| Advanced Radio | +60% | +40% | 6 | Advanced Radio |
| Command Center | +75% | +50% | 8 | Armored Signal Company |

## Tank roles

Setting the role changes the design's stats even if nothing else changes — two identical designs, one flagged Medium Tank and one Medium Tank Destroyer, will differ (the TD gets more hard attack and piercing). Role also determines which battalion or support company the design can fill.

| Role | Battalion | Supply Use | Soft Atk | Hard Atk | Piercing | Armor | Breakthrough | Defense | Suppression |
|---|---|---|---|---|---|---|---|---|---|
| Tank | Light / Medium / Heavy / Modern tank | – | – | – | – | – | – | – | – |
| Amphibious Tank | Amphibious tank | – | – | – | – | – | – | – | – |
| Amphibious Tank | Light amphibious tank | -0.02 | – | – | – | – | -15% | – | -250% |
| Amphibious Tank | Medium amphibious tank | -0.05 | – | – | – | – | -15% | – | -250% |
| Amphibious Tank | Heavy amphibious tank | -0.12 | – | – | – | – | -15% | – | -250% |
| Tank Destroyer | Light Tank Destroyer | -0.02 | – | +30% | +30% | – | -57% | – | -150% |
| Tank Destroyer | Medium Tank Destroyer | -0.03 | – | +30% | +30% | – | -40% | – | -125% |
| Tank Destroyer | Heavy Tank Destroyer | -0.02 | – | +30% | +30% | – | -40% | – | -125% |
| Tank Destroyer | Super Heavy Tank Destroyer | – | – | +30% | +30% | – | -25% | – | -125% |
| Tank Destroyer | Modern Tank Destroyer | – | – | +30% | +30% | – | -40% | – | -125% |
| Artillery | Light SP Artillery | +0.2 | +35% | – | – | – | -57% | – | -125% |
| Artillery | Medium SP Artillery | +0.21 | +35% | – | – | – | -40% | – | -100% |
| Artillery | Heavy SP Artillery | +0.28 | +35% | – | – | – | -40% | – | -100% |
| Artillery | Super Heavy SP Artillery | +0.4 | +35% | – | – | – | -25% | – | -125% |
| Artillery | Modern SP Artillery | +0.25 | +35% | – | – | – | -40% | – | -100% |
| Anti-Air | Light SP Anti-Air | -0.12 | – | – | – | – | -70% | – | -175% |
| Anti-Air | Medium SP Anti-Air | -0.15 | – | – | – | – | -68% | – | -170% |
| Anti-Air | Heavy SP Anti-Air | -0.22 | – | – | – | – | -50% | – | -175% |
| Anti-Air | Super Heavy SP Anti-Air | -0.3 | – | – | – | – | -35% | – | -175% |
| Anti-Air | Modern SP Anti-Air | -0.15 | – | – | – | – | -68% | – | -50% |
| Flame | Light flame tank | -0.2 | -75% | -75% | – | -75% | -90% | -75% | -250% |
| Flame | Medium flame tank | -0.22 | -70% | -70% | – | -70% | -85% | -70% | -250% |
| Flame | Heavy flame tank | -0.29 | -62.5% | -62.5% | – | -62.5% | -77.5% | -62.5% | -250% |

## Reliability and production-cost trade-offs

Reliability drives equipment attrition and breakdowns; production cost drives how many tanks you get per factory-day. The designer is mostly a contest between the two.

**Things that cost reliability:**
- Every engine upgrade level: -1.5% (up to -30% at level 20)
- Every armor upgrade level: -1.5% (up to -30% at level 20)
- Most guns: -5% to -35% (Super-Heavy Cannon is the worst at -35%; heavy cannons -25% to -30%; howitzers -20% to -30%)
- Wheeled suspension -20%, half-track -10%
- Extra Ammunition Storage -10%, Amphibious Drive -15%
- Super-Heavy turrets -10% / -25%, Improvised Turret -25%

**Things that give reliability back:**
- **Diesel Engine +25%** — the single biggest source, and it costs nothing but 1 production cost and a design-cost swap
- **Torsion Bar suspension +15%**
- **Wet Ammunition Storage +15%** (1 prod. cost, 1 slot)
- **Easy Maintenance +10% AND -7.5% production cost** — strictly good, but costs **30 army XP** and needs Maintenance Company II
- Any **fixed superstructure +20%** (at -25% breakthrough)
- The chassis itself: reliability rises with chassis tier (e.g. Advanced Light 130%, Advanced Heavy 120%)

**Things that cut production cost:**
- **Riveted Armor -20%** (default; gives up 30% armor)
- **Makeshift Armor -30%** (Norway only; -30% hardness)
- **Easy Maintenance -7.5%**
- Wheeled -10% / half-track -5% suspension (light chassis only, at heavy hardness cost)

**Things that add production cost sharply:**
- Cast Armor +20%, Sloped Armor +10%, Petrol-Electric +15%, Amphibious Drive +10%, Super-Heavy turrets +50%
- Big guns: Super-Heavy Cannon 12.5, Advanced Heavy Cannon 8, Advanced High-Velocity Cannon 7, Heavy Howitzer 7
- Heavy chassis themselves: Basic Heavy 10, Advanced Heavy 12, Super-Heavy 28 (vs Modern 6)

**Rules of thumb (Inferred):**
- Always take **Diesel Engine** unless you specifically need Gas Turbine speed; +25% reliability free is what pays for gun and upgrade-level reliability losses.
- **Sloped Armor (+25% armor for +10% cost)** is the most efficient armor in the game per production point; take it on anything meant to survive.
- **Easy Maintenance** pays for itself twice (reliability up, cost down) — the 30 army XP is worth it on your one main-line tank design.
- Armor upgrade levels are worth taking only up to the point where you out-armor the enemy's piercing; every level past that is wasted cost, speed and reliability.
- Watch **Chromium and Tungsten**: welded armor, all high-velocity/heavy cannons and improved medium cannons need them. A resource-poor nation is pushed toward Cast/Riveted armor and Medium Cannons.

## Designer companies

With **Arms Against Tyranny**, design companies are replaced by **Military Industrial Organizations (MIOs)**. A tank-category MIO assigned as the **designer** of a tank variant applies its trait bonuses to that equipment. Relevant tank MIO archetypes: **Standardized Production, Infantry Tank Designer, Assault Guns Manufacturer, Fast Tank Designer, Medium Tank Designer, Heavy Tank Designer, Tank Refurbishment Plant, Light Armored Manufacturer**. Tank-only traits include Armor Welding Specialists (+5% armor), Casting Specialists (+2% hardness), Factory Applied Camouflage (+2% defense and breakthrough, medium/heavy specialists), and Cutting Corners (-10% production cost at -5% reliability/soft/hard attack/armor).

Full mechanics, trait tree, funds, size and policy rules: see [Military Industrial Organizations](../01-mechanics/military-industrial-organizations.md). Without Arms Against Tyranny the older single-slot **Tank Manufacturer** design-company idea applies instead.

## Worked example designs

**Inferred** — these are role templates built from the module tables above, not designs quoted by the wiki. Adjust armor/engine levels to your tech and to enemy piercing.

### 1. Cheap 1936–1939 light tank (early-war spam / cavalry filler)
- Chassis: **Basic** or **Improved Light Tank Chassis**
- Engine: **Diesel** (+25% reliability)
- Suspension: **Christie** (+20% speed) or **Torsion Bar** if reliability is short
- Armor: **Riveted** (-20% production cost)
- Turret: **Light One Man Turret** (cheapest breakthrough at 1 cost)
- Gun: **Small Cannon** or **Automatic Cannon**
- Modules: Additional Machineguns, Basic Radio when available
- Upgrades: engine 2–4, armor 0–2
- **Why:** the point is cost. Riveted + one-man turret + small gun keeps it near 5 production cost, so you can field armour at all in 1937–1939 against unarmoured infantry.

### 2. Main-line medium breakthrough tank (1940–1943 workhorse)
- Chassis: **Improved Medium Tank Chassis** (1940), later **Advanced Medium** (1943)
- Engine: **Diesel**, upgraded to keep ~7–8 km/h after armor levels
- Suspension: **Christie** (speed) or **Interleaved Roadwheels** (+4 breakthrough)
- Armor: **Welded** (+30% armor, +4 breakthrough/defense) if Chromium allows, otherwise **Cast**
- Turret: **Medium Three Man Turret** (+24 breakthrough)
- Gun: **Improved Medium Cannon** (32 soft / 20 hard / 90 piercing)
- Modules: **Sloped Armor**, **Easy Maintenance**, **Improved/Advanced Radio**, **Wet Ammunition Storage** (or Extra Ammunition Storage if you can spare reliability)
- Upgrades: armor to whatever beats enemy piercing (typically 5–10), engine to hold speed
- **Why:** this is the standard "does everything" tank. High breakthrough from the three-man turret, enough piercing to hurt enemy mediums, sloped armor for cheap protection, Easy Maintenance to offset upgrade-level reliability loss.

### 3. Heavy breakthrough tank (fortified fronts, low-numbers armies)
- Chassis: **Improved** or **Advanced Heavy Tank Chassis**
- Engine: **Diesel** with high engine levels (heavies are slow)
- Suspension: **Torsion Bar** (+15% reliability — heavies have miserable reliability)
- Armor: **Welded**
- Turret: **Heavy Three Man Turret** (+22 breakthrough, Heavy-size gun)
- Gun: **Improved Heavy Cannon** or **Advanced High-Velocity Cannon**
- Modules: **Sloped Armor**, **Armor Skirts**, **Easy Maintenance**, **Advanced Radio**
- Upgrades: armor high (10–15), engine enough to stay above ~4 km/h with your division
- **Why:** heavies exist to be unpierceable. Stack armor type + sloped + skirts + upgrade levels; accept the production cost (11–12 base chassis) and the low speed.

### 4. Cheap armor-only "space" tank (division armor/hardness filler)
- Chassis: cheapest **Light** chassis available
- Engine: **Diesel**
- Suspension: **Bogie** (free)
- Armor: **Riveted**
- Turret: **Light Fixed Superstructure** (+20% reliability, +3 defense) — accept -25% breakthrough
- Gun: **Heavy Machine Gun** (0.5 cost)
- Modules: none, or Wet Ammunition Storage
- Upgrades: armor only, a few levels
- **Why:** one battalion of this in an infantry division raises the whole division's armor and hardness for minimal industry. Breakthrough is irrelevant here.

### 5. Medium tank destroyer (anti-armor)
- Chassis: **Improved / Advanced Medium Tank Chassis**
- Role: **Tank Destroyer** (+30% hard attack, +30% piercing, -40% breakthrough)
- Engine: **Diesel**
- Suspension: **Torsion Bar**
- Armor: **Riveted** (cost) or **Welded** (survivability)
- Turret: **Medium Fixed Superstructure** (mounts a Heavy-size gun on a medium chassis, +20% reliability)
- Gun: **Improved High-Velocity Cannon** (125 piercing) or **Advanced High-Velocity Cannon** (200 piercing) via the superstructure
- Modules: **Squeeze-bore Adaptor** (+10% piercing), **Auto Loader**, **Radio**, **Easy Maintenance**
- **Why:** the superstructure is what makes TDs work — it upsizes the gun, adds reliability, and the -25% breakthrough hurts a role that already has -40% breakthrough anyway.

### 6. Self-propelled artillery (soft attack)
- Chassis: **Improved Medium Tank Chassis** (cheap per gun) — Light SP Artillery is even cheaper but takes -57% breakthrough
- Role: **Artillery** (+35% soft attack)
- Engine: **Diesel**
- Suspension: **Bogie**
- Armor: **Riveted**
- Turret: **Medium Fixed Superstructure** (to fit a Heavy Howitzer) or Medium Three Man Turret for the Improved Medium Howitzer
- Gun: **Improved Medium Howitzer** (45 soft) or **Heavy Howitzer** (55 soft, needs Heavy-size mount)
- Modules: **Easy Maintenance**, Radio
- **Why:** soft attack per production point. Note SP Artillery is the only role with a **positive** supply-use penalty (+0.21 on medium), so do not spam it in low-supply theatres.

### 7. Self-propelled anti-air
- Chassis: cheapest **Light** or **Medium** chassis
- Role: **Anti-Air**
- Engine: **Diesel**; Suspension: **Bogie**; Armor: **Riveted**
- Turret: a real turret (**never** a fixed superstructure — superstructures cannot mount AA guns)
- Gun: **Improved** or **Advanced Anti-Air Gun** (32 / 46 air attack)
- Modules: minimal — this design exists for air attack and hardness, not combat stats
- **Why:** cheap air defence for armoured divisions plus a hardness bump. Advanced AA Gun is Medium-size, so it needs a medium turret.

### 8. Flame tank support company
- Chassis: cheapest **Light** chassis (Light flame tank has the harshest role penalties but the lowest cost)
- Role: **Flame**
- Engine: **Diesel**; Armor: **Riveted**; Turret: **Light One Man Turret**
- Gun: **Advanced Flamethrower** if researched (+6 breakthrough, 12 soft) else Flamethrower
- **Why:** the flame tank company's value is its terrain/fort bonuses, not its own stats — the role strips 62.5–90% of everything. Build it as cheaply as possible.

### 9. Amphibious tank (naval invasion support)
- Chassis: **Amphibious Tank Chassis** (or Light/Medium chassis + **Amphibious Drive** module)
- Role: **Amphibious Tank**
- Engine: **Diesel**; Suspension: **Torsion Bar** (the drive costs -15% reliability)
- Armor: **Riveted** or **Cast**
- Turret: light/medium turret; Gun: **Small Cannon** / **Medium Cannon**
- **Why:** amphibious tanks and the Amtrac are what let armour land in the first wave. Remember they count against the **special forces cap** — see [Special forces doctrine](special-forces-doctrine.md).

## See also

- [Armor technology](armor-technology.md) — which chassis, engine and armor levels you can research and when
- [Artillery technology](artillery-technology.md) — where the gun modules come from
- [Land doctrine](land-doctrine.md) — Armor track subdoctrines that buff these designs
- [Military Industrial Organizations](../01-mechanics/military-industrial-organizations.md)
