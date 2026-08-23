---
title: Nuclear Weapons, Missiles and Raids
category: mechanics
tags: [nuclear, atomic-bomb, thermonuclear, reactors, missiles, rockets, icbm, raids, fallout, special-projects]
game_version: "1.19"
dlc: [Götterdämmerung]
sources:
  - https://hoi4.paradoxwikis.com/Nuclear_bomb
  - https://hoi4.paradoxwikis.com/Missile
  - https://hoi4.paradoxwikis.com/Raid
---

## Summary

Nuclear bombs require the Atomic Research technology, the Nuclear Reactor and Nuclear Fission Bomb special projects, and at least one built reactor; each reactor then ticks out bombs on a fixed schedule. Delivery is via strategic bombers, land-based rocket sites, or (with Götterdämmerung) missile submarines — the "nuclear trifecta". Missiles are single-use air units launched from rocket sites, submarines or multi-charge large caliber guns, and split into guided, ballistic, nuclear, surface-to-air, and gun-ammunition types. Raids (added in 1.15 with Götterdämmerung) are the prepared-strike interface covering nuclear, air and paratrooper operations, each resolving on a four-tier success ladder.

## Nuclear weapons

### Prerequisites

| Step | What it does |
|---|---|
| **Atomic Research** (Engineering technology) | Prerequisite for the nuclear special projects; gives **+4% research speed** |
| **Nuclear Reactor** (special project) | Unlocks the state-level **Nuclear Reactor** building in the construction screen. Built reactors provide enriched uranium; useless without bomb technology |
| **Nuclear Fission Bomb Project** (special project) | Lets the country produce and stockpile nuclear bombs; grants **one free bomb** on completion for the initial test |
| **Thermonuclear Bomb** (special project, Götterdämmerung) | Unlocks thermonuclear bombs, produced **in parallel** with ordinary nuclear bombs |
| **Nuclear Warheads** (special project, Götterdämmerung) | Unlocks the MRBM and ICBM for nuclear missile strikes |
| **Commercial Nuclear Reactor** (Götterdämmerung) | State-wide industry bonuses |
| **Nuclear Engines** (Götterdämmerung) | Nuclear propulsion for ships |

Research can be accelerated by a theorist with the **Nuclear Scientist** or **Nuclear Enthusiast** trait, and by certain national focuses.

### Bomb production rates

Baseline: each reactor produces **1 bomb per 7 years (2,555 days)** divided by various factors, giving the following per-reactor rates:

| Reactor type | Nuclear bomb | Thermonuclear bomb |
|---|---|---|
| Nuclear reactor | 1 per **852 days** (≈2.34 years) | 1 per **1,278 days** (≈3.5 years) |
| Civilian nuclear reactor | 1 per **852 days** (≈2.34 years) | 1 per **1,278 days** (≈3.5 years) |
| Heavy water nuclear reactor | 1 per **1,278 days** (≈3.5 years) | 1 per **2,555 days** (7 years) |

Production progress is shown in the tooltip of the nuclear weapons stockpile counter on the top bar.

### Delivery methods

Since patch 1.15 (Götterdämmerung), nuclear use runs through the **raids interface** (bottom-right of the screen). Two strike categories:

| Strike type | Delivery unit | Launched from |
|---|---|---|
| Bomber strike | Strategic bomber wing | Air base |
| Missile strike | MRBM or ICBM | Rocket site, or a nuclear missile submarine deployed from a naval base |

All must be within range of the target. A nuclear submarine carrying ICBMs can travel halfway around the world from its home naval base and then launch a further 14,000 km, effectively reaching anywhere. Having all three delivery methods (bombers, terrestrial missiles, submarine missiles) is the **nuclear trifecta**.

### Detonation effects

| Effect | Nuclear bomb | Thermonuclear bomb |
|---|---|---|
| Damage to units | Random **10%–90%** of current strength and organization, **in the target province** | Same roll, applied to units in **every province of the state**, regardless of nationality — severe friendly-fire risk on frontline states |
| Province buildings | All buildings in the target province reduced to **0 HP** | All province buildings in the whole **state** reduced to 0 HP |
| State and shared buildings | Reduced to a **random HP level below** their current undamaged level | All state buildings reduced to **0 HP** |
| Air base | Targeting a province with an air base **destroys all aircraft stationed there** | Same |
| War support | Controller loses up to **20% war support** — proportionately less if the state's largest victory point is smaller than 3, or if undamaged infrastructure is below level 10 | Same |

- The first use, and uses on specific capital cities, generate unique news messages (informational only).
- After the **second** nuclear bomb is dropped on a Japanese core state, **Japan gains a special surrender decision** — provided that, before the second bomb, Japan's navy has fewer than 40 ships and Japan controls neither Okinawa nor Iwo Jima.

### Fallout modifiers

**Nuclear Fallout** — applied to the target state for **365 days**:

| Modifier | Value |
|---|---|
| Divisions speed | −30% |
| Resource gain efficiency | −40% |
| Division defense | −25% |
| Factory repair speed | −40% |
| Free repair | −40% |
| Max entrenchment | −50% |
| Local construction speed | −40% |
| Infrastructure repair speed | −40% |
| Railway repair speed | −40% |

**Intense Nuclear Fallout** — applied to the target state for **730 days**:

| Modifier | Value |
|---|---|
| Divisions speed | −65% |
| Resource gain efficiency | −75% |
| Division defense | −50% |
| Factory repair speed | −75% |
| Free repair | −75% |
| Max entrenchment | −90% |
| Local construction speed | −75% |
| Infrastructure repair speed | −75% |
| Railway repair speed | −75% |

> ⚠️ The Nuclear bomb page and the Raid page state slightly different fallout modifier sets and durations (the Raid page lists 180/365/730-day "Fallout (Atomic)" with −25% army defense, −25% army speed, −50% max entrenchment, −40% factory repair, −40% factory free repair, −40% local resources, scaled by success tier). Both are reproduced — the Raid page's version is what the raid interface applies.

## Missiles

Missiles are single-use air units launched from dedicated bases and destroyed on use — closest analogue is a kamikaze strike. Without Götterdämmerung only **basic guided missiles** can be built. Missiles are tightly tied to **aerodynamics and avionics special projects** for both the missiles and their launch platforms.

### Guided missiles ("flying bombs")

Fly **Strategic Bombing** and *can* be intercepted by fighters and anti-air. Their air defence is 0, so they cannot be disrupted — only shot down. Built with military factories; fired from rocket sites and (Götterdämmerung) missile-launching submarines.

| Equipment | Agility | Strategic bombing | Naval attack | Naval targeting | Speed (km/h) | Range (km) | Reliability | Production cost | Resources per factory | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|
| Basic Guided Missile | 10 | 450 | 1.5 | 0.6 | 640 | 500 | 80% | 36 | 2 Aluminium, 2 Tungsten | Flying Bomb |
| Improved Guided Missile | 10 | 550 | 1.5 | 0.6 | 5760 | 640 | 80% | 36 | 2 Aluminium, 2 Tungsten | Ballistic Missile (**without** Götterdämmerung) |
| Advanced Guided Missile | 10 | 700 | 1.5 | 0.6 | 6500 | 4000 | 80% | 74 | 3 Aluminium, 2 Tungsten | MRBM (**without** Götterdämmerung) |

### Ballistic missiles

Fly the **Barrage** mission — functionally identical to Strategic Bombing but **cannot be intercepted or shot down**. Built with military factories; fired from rocket sites and missile-launching submarines.

| Equipment | Agility | Strategic bombing | Naval attack | Naval targeting | Speed (km/h) | Range (km) | Reliability | Production cost | Resources per factory | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|
| Basic Ballistic Missile | 10 | 550 | 1.5 | 0.6 | 5760 | 640 | 80% | 50 | 2 Aluminium, 2 Tungsten | Ballistic Missile |
| Medium Range Ballistic Missile | 10 | 700 | 1.5 | 0.6 | 6500 | 4000 | 80% | 74 | 3 Aluminium, 2 Tungsten | MRBM |

### Nuclear missiles

Fly the **Nuclear Strike** mission and enable the Nuclear Missile Strike and Thermonuclear Missile Strike raids. **Cannot be thwarted by anti-air** and can be launched from the sea. Fired from rocket sites and nuclear missile submarines.

| Equipment | Agility | Strategic bombing | Naval attack | Naval targeting | Speed (km/h) | Range (km) | Reliability | Production cost | Resources per factory | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|
| Medium Range Nuclear Missile | 10 | 500 | 1.5 | 0.6 | 6500 | 4000 | 80% | 800 | 3 Aluminium, 3 Tungsten, 1 Chromium | Nuclear Warheads |
| Intercontinental Nuclear Missile | 10 | 600 | 1.5 | 0.6 | 8000 | 14000 | 80% | 1200 | 4 Aluminium, 3 Tungsten, 2 Chromium | ICBM |

### Surface-to-air missiles

Fly the **Surface to air** mission, acting like anti-air but with separately produced ammunition. Fired from rocket sites.

| Equipment | Agility | Air attack | Strategic bombing | Naval attack | Naval targeting | Speed (km/h) | Range (km) | Reliability | Production cost | Resources per factory | Prerequisite |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Surface-to-Air Missile I | 10 | 0.25 | 0 | 1.5 | 0.6 | 5760 | 400 | 80% | 30 | 1 Aluminium, 1 Tungsten | Surface to Air Missiles |

Each SAM wing on the Surface to air mission provides **at most 5 air superiority** in its air zone. The actual amount scales with the missiles' air attack (an air attack of 1.0 gives the full 5), and range/air-zone coverage still affects mission efficiency as with aircraft.

### Multi-charge large caliber gun ammunition

Technically classified as missiles. Created **automatically** at a Multi-charge large caliber gun when it is ordered to fire — no production line needed. Flies the **Barrage** mission.

| Equipment | Agility | Strategic bombing | Speed (km/h) | Range (km) | Reliability | Production cost | Prerequisite |
|---|---|---|---|---|---|---|---|
| Multi-Charge Large Caliber Gun (ammo) | 10 | 1000 | 9999 | 600 | 100% | 0 | Multi-charge large caliber gun |

### Launch platforms

| Platform | Capacity | Can launch | Unlocked by | Notes |
|---|---|---|---|---|
| **Rocket site** | **100 missiles per level, max 300 at level 3** | All missile types except gun ammunition | Experimental Rockets technology | State building; **mutually exclusive with the Multi-charge large caliber gun** |
| **Missile-launching submarine** | 1 missile wing, **10 missiles** | Guided and ballistic missiles | Missile Launching Submarine special project *(Götterdämmerung)* | Mobile and potentially invisible. Without Man the Guns it is a dedicated ship type; with Man the Guns any Fleet or Nuclear Submarine with a **Submarine Missile Launcher** module qualifies |
| **Nuclear missile submarine** | 1 missile wing, **10 missiles** | Nuclear missiles | Nuclear Missile Submarine special project *(Götterdämmerung)* | With Man the Guns, any Nuclear Submarine with a **Submarine Nuclear Missile Launcher** module qualifies |
| **Multi-charge large caliber gun** | **1** round | Its own ammunition | Multi-Charge Large Caliber Gun land warfare special project *(Götterdämmerung)* | State building; mutually exclusive with rocket sites |

## Raids

Raids were added in **patch 1.15 with Götterdämmerung**. Three families: Nuclear, Air and Paratrooper. Every raid resolves on a four-tier ladder — **Failure / Limited Success / Success / Critical Success**. Unique (country-specific) raids can be launched **once only**.

### Nuclear raids

| Raid | Prep time | Required equipment | Required special projects | Launched from | Base success |
|---|---|---|---|---|---|
| Nuclear Strike | 30 days | 10 Strategic or Intercontinental Bombers, 1 Nuclear Bomb | Nuclear Fission Bomb Project | Air base | 50% |
| Nuclear Missile Strike | 14 days | 1 Nuclear Missile, 1 Nuclear Bomb | Nuclear Fission Bomb Project, Nuclear Warheads | Rocket site or submarine | 80% |
| Thermonuclear Strike | 30 days | 10 Strategic or Intercontinental Bombers, 1 Thermonuclear Bomb | Thermonuclear Bomb | Air base | 50% |
| Thermonuclear Missile Strike | 14 days | 1 Nuclear Missile, 1 Thermonuclear Bomb | Thermonuclear Bomb, Nuclear Warheads | Rocket site or submarine | 80% |

**Bomber-strike success modifiers** (Nuclear Strike and Thermonuclear Strike):

| Factor | Range |
|---|---|
| Experience | −10% to +10% |
| Air defense | −5% to +5% |
| Air agility | −10% to +10% |
| Reliability | −10% to +10% |
| Air reliability | −10% to +10% |
| Air superiority | −25% to +25% |
| Interception | −25% |
| Static anti-air | −25% |
| Radar coverage | −5% |
| Target information | +20% |

**Missile-strike success modifiers**: only **Target information +20%** (no interception, anti-air or radar penalty).

Outcomes:

| Raid | Failure | Limited Success | Success | Critical Success |
|---|---|---|---|---|
| Nuclear Strike | Lose **75%** of bombers; **−50 political power** | Lose **50%** of bombers; Fallout (Atomic) for **180 days** | Lose **10%** of bombers; Fallout (Atomic) for **365 days** | **No** bomber losses; Fallout (Atomic) for **730 days** |
| Nuclear Missile Strike | Nothing happens | Nothing happens | Fallout (Atomic) for **365 days** | Fallout (Atomic) for **365 days** |
| Thermonuclear Strike | Lose **50%** of bombers; **−50 political power** | Lose **25%** of bombers (no fallout) | Lose **5%** of bombers; Fallout (Thermonuclear) for **730 days** | **No** bomber losses; Fallout (Thermonuclear) for **730 days** |
| Thermonuclear Missile Strike | Nothing happens | Nothing happens | Fallout (Thermonuclear) for **730 days** | Fallout (Thermonuclear) for **730 days** |

**Fallout (Atomic):** −25% army defense, −25% army speed, −50% max entrenchment, −40% factory repair speed, −40% factory free repair speed, −40% local resources.
**Fallout (Thermonuclear):** −50% army defense, −65% army speed, −90% max entrenchment, −75% factory repair speed, −75% factory free repair speed, −75% local resources.

### Generic air raids

| Raid | Prep time | Required equipment | Required special project | Target | Base success | Base critical success |
|---|---|---|---|---|---|---|
| Facility Strike | 90 days | 70 Tactical or Strategic Bombers | — | Enemy facilities | 65% | 15% |
| Lock Bombing Raid | 90 days | 70 Tactical or Strategic Bombers | Air bouncing bomb | Canals | 65% | 15% |
| Dam Busting | 45 days | 70 Strategic Bombers | Air bouncing bomb | Dams | 65% | 15% |
| Oilfield Raid | 90 days | 40 Strategic Bombers | — | Any province with more than 24 Oil | 65% | 15% |
| Mega Gun Emplacement Strike | 90 days | 70 Strategic Bombers with Earthshaker Bomb | Earthshaker Bomb | Multi-charge large caliber gun | 65% | 15% |

Success modifiers (all generic air raids; ranges differ slightly per raid):

| Factor | Facility Strike / Mega Gun | Lock Bombing / Dam Busting / Oilfield |
|---|---|---|
| Experience | −20% to +20% | −10% to +10% |
| Agility | −10% to +10% | −10% to +10% |
| Reliability | −10% to +5% | −10% to +5% (Oilfield: −10% to +10%) |
| Air defense | −5% to +5% | −5% to +5% |
| Air superiority | −10% to +10% | −20% to +20% |
| Static anti-air | −25% | −25% |
| Interception | −20% | −20% |
| Target information | +30% | +30% |

Outcomes:

| Raid | Failure | Limited Success | Success | Critical Success |
|---|---|---|---|---|
| Facility Strike | Lose 70 bombers; facility damaged **0.05 level** | Lose 40 bombers; **0.15 level**; −5% facility repair speed until repaired; **−5% special project progress** | Lose 30 bombers; **0.55 level**; −25% repair speed; **−15% special project progress** | Lose 10 bombers; **0.85 level**; −50% repair speed; **−25% special project progress** |
| Lock Bombing Raid | Lose 85% of bombers; canal damaged **0.1 level** | Lose 45%; **0.2 level** | Lose 15%; **0.8 level**; −35% repair speed until repaired; **+10 air experience** | Lose 5%; **1 level**; −55% repair speed; **+20 air experience** |
| Dam Busting | Lose 65% of bombers | Lose 45%; dam damaged **0.25 level**; "Dam blown" for **60 days** | Lose 15%; dam damaged **1 level**; −0.7 repair speed; "Dam blown" for **180 days**; **+10 air experience** | Lose 5%; dam damaged **1 level**; −0.8 repair speed; "Dam blown" for **360 days**; **+20 air experience** |
| Oilfield Raid | Lose 95% of bombers | Lose 65%; "Refinery lightly damaged" for **90 days** (−25% local oil) | Lose 25%; "Refinery damaged" for **180 days** (−50% local oil); **+10 air experience** | Lose 10%; "Refinery critically damaged" for **360 days** (−75% local oil); **+20 air experience** |
| Mega Gun Emplacement Strike | Lose 70 bombers; gun damaged **0.1 level** | Lose 40 bombers; **0.15 level**; −20% repair speed until repaired | Lose 30 planes; **gun destroyed** | Lose 10 bombers; **gun destroyed** |

**Dam blown** state modifier: strategic deployment disabled, **−50% local supply, −25% local resources, −50% local manpower, −25% army speed** for the controller.

### Unique air raids

Seven unique air raids exist: 1 Austrian, 1 British, 3 German, 1 Chinese, and 1 available to any nation fighting Germany. Each is **one-use only**.

| Raid (country) | Prep | Equipment | Requirements | Target | Base success | Base critical |
|---|---|---|---|---|---|---|
| Reichstag Bombing (Austria) | 30 days | 75 Strategic Bombers | At war with Germany; completed **The Second Brothers War** or **Deal with the German Threat** | Reichstag landmark | 70% | 10% |
| Reichstag Bombing (United Kingdom) | 30 days | 75 Strategic Bombers | At war with Germany | Reichstag landmark | 70% | 10% |
| Big Ben Bombing (Germany) | 30 days | 75 Strategic Bombers | At war with the UK; after a specific event | Big Ben landmark | 70% | 10% |
| Statue of Liberty Bombing (Germany) | 30 days | 75 Strategic Bombers | At war with the USA; completed **Amerikabomber** | Statue of Liberty landmark | 70% | 10% |
| Kremlin Bombing (Germany) | 30 days | 75 Strategic Bombers | At war with the Soviet Union; completed **Strike Eastward** | Kremlin landmark | 70% | 10% |
| Operation Jericho (any nation fighting Germany) | 90 days | 70 Tactical Bombers or Heavy Fighters | Germany controls Picardy and Ile de France; France is democratic and in a faction with the UK; Ile de France resistance > 25 | Picardy | 55% | 15% |
| Leaflet Dropping Over Japan (China) | 90 days | 8 Tactical Bombers or 5 Strategic Bombers | At war with Japan; more than 5% surrender progress | Nagasaki | 65% | 15% |

Landmark-raid success modifiers (all five landmark raids): Experience −5% to +5%; Agility −5% to +5%; Reliability −10% to +5%; Air defense −5% to +5%; Air superiority −10% to +10%; Static anti-air −10%; Interception −20%; Target information +20%.

Outcomes:

| Raid | Failure | Limited Success | Success | Critical Success |
|---|---|---|---|---|
| Reichstag Bombing (Austria) | Lose 10 bombers; −5% war support; landmark damaged 0.05 level | Lose 5 bombers; +2% war support; 0.15 level | Lose 2 bombers; +5% war support; 0.65 level | Lose 1 bomber; +5% war support; **+10% ruling party popularity**; 0.85 level |
| Reichstag Bombing (UK) | Lose 65 bombers; −5% war support; 0.05 level | Lose 50 bombers; +2% war support; 0.15 level; −5% repair speed | Lose 35 bombers; +5% war support; 0.65 level; −15% repair speed | Lose 10 bombers; +5% war support; +10% ruling party popularity; 0.85 level; −25% repair speed; **−5% war support for Germany** |
| Big Ben Bombing (Germany) | Lose 65 bombers; −5% war support; 0.05 level | Lose 50 bombers; +2% war support; 0.15 level; −5% repair speed | Lose 35 bombers; +5% war support; 0.65 level; −15% repair speed | Lose 10 bombers; +5% war support; +10% ruling party popularity; 0.85 level; −25% repair speed; **−5% war support and −5% ruling party popularity for the UK** |
| Statue of Liberty Bombing (Germany) | Lose 65 bombers; −5% war support; 0.05 level | Lose 50 bombers; +2% war support; 0.15 level; −5% repair speed | Lose 35 bombers; +5% war support; 0.65 level; −15% repair speed | Lose 10 bombers; +5% war support; +10% ruling party popularity; 0.85 level; −25% repair speed; **−5% war support and −5% ruling party popularity for the USA** |
| Kremlin Bombing (Germany) | Lose 65 bombers; −5% war support; 0.05 level | Lose 50 bombers; +2% war support; 0.15 level; −5% repair speed | Lose 35 bombers; +5% war support; 0.65 level; −15% repair speed | Lose 10 bombers; +5% war support; +10% ruling party popularity; 0.85 level; −25% repair speed; **−5% war support and −5% ruling party popularity for the Soviet Union** |
| Operation Jericho | Lose 70 planes; **−10% resistance** in Picardy and Ile de France | Lose 40 planes; +10% resistance in Picardy, +5% in Ile de France | Lose 30 planes; +20% resistance in Picardy, +10% in Ile de France | Lose 10 planes; **+40%** resistance in Picardy, **+20%** in Ile de France |
| Leaflet Dropping Over Japan | Lose 90% of bombers; **−25 political power** | Lose 50%; **+20 political power**; Japan gets "Public awareness of war" for 35 days (−5% war support, −0.05 political power) | Lose 30%; **+50 political power**; Japan gets "Public awareness of war worse" for 70 days (−10% war support, −0.05 political power) | **No** bomber losses; **+75 political power**; Japan gets "Public awareness of war worst" for 140 days (−10% war support, −0.1 political power) |

### Paratrooper raids

| Raid | Prep time | Required equipment | Additional requirement | Base success | Base critical success |
|---|---|---|---|---|---|
| Steel Mine Raid | 90 days | 1 Paratrooper division (≥3 battalions), 10 Transport Planes, 200 Support Equipment | — | 60% | 15% |
| Pathfinder Raid | 30 days | 1 Paratrooper division (≥3 battalions), 10 Transport Planes, 200 Support Equipment | Target province must have an ongoing naval invasion at ≥5% preparation | 60% | 15% |
| Eben Emael (Germany) | 30 days | 2 Paratrooper divisions, 5 Transport Planes, 200 Infantry Equipment, 100 Support Equipment | Unlocked by the **Expanding the Luftwaffe** focus | — | — |

Success modifiers for both generic paratrooper raids: Experience −5% to +5%; Organization −5% to +5%; Strength −5% to +5%; **+0.5% per point of Reconnaissance**; Air superiority −25% to 0; Static anti-air −20% to 0; Interception −20% to 0.
- **Steel Mine Raid** additionally: Resistance **0 to +40%** (starting from 20% resistance); **enemy units −50%** (maximum penalty reached at 2 units); Intel **0 to +20%**.
- **Pathfinder Raid** additionally: Resistance **+50% to 0** (starting from 20% resistance); Intel **0 to +20%** (starting from 50% intel).

Outcomes:

| Raid | Failure | Limited Success | Success | Critical Success |
|---|---|---|---|---|
| Steel Mine Raid | **25%** of the province's steel unusable for **30 days** | **25%** for **90 days** | **50%** for **120 days** | **75%** for **180 days** |
| Pathfinder Raid | No buff | Buff for **20 hours** | Buff for **40 hours** | Buff for **60 hours** |
| Eben Emael | Damages **1 level** of land fort | Damages **1 level**; −10% fort repair speed; **−50% fort effectiveness for 180 days** | Damages **4 levels**; −25% fort repair speed; **−75% fort effectiveness and −25% max entrenchment for 180 days** | Damages **6 levels**; −40% fort repair speed; **−50% fort effectiveness and −50% max entrenchment for 180 days** |

**Pathfinder Raid buff:** strategic deployment disabled in the province, **+20 hours of no-supply grace**, **−10% naval invasion penalty**.

## Detecting incoming raids

Air intel governs raid warning: **10% air intel** is the minimum to be told a raid has launched, and every additional percentage point lets a raid be spotted one percentage point earlier in its preparation (50% air intel → detected at 50% preparation). See [Espionage and operations](espionage-and-operations.md).

## Cross-references

- [Espionage and operations](espionage-and-operations.md) — air intel and raid detection; the Soviet Infiltrate Atomic Program operation; the Heavy Water Raid against German nuclear progress.
- [Supply and logistics](supply-and-logistics.md) — supply effects of Dam blown and fallout modifiers.
