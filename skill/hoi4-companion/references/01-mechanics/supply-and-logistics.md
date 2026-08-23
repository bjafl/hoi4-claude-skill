---
title: Supply and Logistics
category: mechanics
tags: [supply, logistics, railways, supply-hubs, trucks, trains, ports, convoys, attrition, air-supply, terrain, weather]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Logistics
  - https://hoi4.paradoxwikis.com/Terrain
  - https://hoi4.paradoxwikis.com/Weather
  - https://hoi4.paradoxwikis.com/Land_units
  - https://hoi4.paradoxwikis.com/Support_companies_technology
---

## Summary

Supply is not a stockpiled resource: the supply level of a province is a *support capacity* that limits how many battalions can operate there at full effectiveness. Supply reaching a province comes from three stacked sources — **state supply** (drawn first), **hub supply** (drawn second) and **aerial supply** (drawn last). Divisions that cannot meet their demand suffer escalating penalties to speed, organisation, attack, defence and eventually equipment attrition. The system in this file is the post-1.11 (Barbarossa) logistics model; railways, supply hubs and trains are base-game features since 1.11 even though they were introduced alongside No Step Back.

## Supply map mode (F4) colour key

| Colour | Meaning |
|---|---|
| Bright/light blue | Large amount of available supply |
| Dark blue | Small amount of available supply |
| Purple | Small or no available supply, but no units in the province are suffering low-supply effects |
| Yellow | Insufficient supply for the units present, but still a reasonable partial supply level |
| Bright red | Insufficient supply and units are taking significant supply penalties |

Tooltip behaviour in supply map mode:
- **Unit** — its supply draw and where the supply comes from.
- **Supply hub / port** — supply requested of the hub, and the highlighted railway path back to the capital. Hold **Shift** to display the hub's current range (range varies with weather).
- **Province** — total and available supply. Hold **Ctrl** for a breakdown of hub-supply sources.

## Hub supply

Hub supply comes from supply hubs and from ports (ports act as supply hubs). Three things matter: the hub's **total throughput capacity**, its **range**, and the fact that a province receives supply from *every* hub in range.

### Total hub throughput

Throughput is set by the level of the **railway connection from the hub back to the capital**, and for sea links by the levels of the **departure and arrival ports**. The connection is rated at the *weakest* link along the whole chain.

Railway connection throughput:

| Railway level | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Supply throughput | 15 | 20 | 25 | 30 | 35 |

Port-to-port (convoy) connection throughput:

| Port level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Supply throughput | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |

- Rail: base 15 at level 1, **+5 per further level**, capped at 35.
- Port: base 8 at level 1, **+3 per further level**, capped at 35.
- Weakest-link examples: three rail stretches at levels 2, 2, 1 → the connection counts as level 1 = 15 supply. A level 3 rail feeding a level 6 port that ships to a level 5 port → counts as a level 5 port connection = 20 supply.
- **Rivers count as level 1 rail connections.**
- If the convoy route feeding a port is being raided, the supply delivered is reduced until the route's capacity recovers.
- **Capital hub exception:** base capacity 5, then supplemented by the country's total civilian factories, military factories and naval dockyards.

### Hub range

Range is a per-province falloff driven mainly by **distance in provinces** from the hub, modified by the rail-connection level, infrastructure level, terrain and weather. Falloff grows sharply with each extra province, so extending range by one more province often costs a lot.

Four ways to improve hub supply reach (all four stack):
1. Motorise the hub (or the army).
2. Raise the rail-connection level to the hub.
3. Raise the infrastructure level of the state supply flows *out of*.
4. Build a new supply hub or port.

An un-motorised hub in a level-1-infrastructure state on a level-1 rail connection has the shortest possible range; a fully motorised hub with level 5 infrastructure and a level 5 rail connection has the longest.

### Motorisation (trucks)

| Motorisation level | Icon | Trucks required per hub |
|---|---|---|
| Not motorised | Horse | 0 |
| Motorised | 1 truck | 40 |
| Fully motorised | 2 trucks | 80 |

- Green truck icon(s) = the hub was motorised directly; grey truck(s) = motorised indirectly by a nearby army's motorisation setting.
- Trucks assigned to supply motorisation **consume no fuel and no manpower**.
- They **do take attrition**, increased by bad terrain and weather (see truck attrition factors below), and can be destroyed by enemy aircraft on the **Logistical Strike** mission.
- Motorisation can be set at **army level**, which auto-applies the chosen level to every hub the army draws from. Less micromanagement, but truck demand fluctuates as the army moves.
- If fewer trucks are available than assigned, the benefit is reduced **in proportion to the shortfall**.

### Railways

Construction cost per province tile, per level:

| Railway level | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| CIC cost | 300 | 430 | 560 | 690 | 820 |

- Formula: **300 CIC + 130 CIC per existing railway level**, max level 5.
- Total to go from nothing to level 5 in one province: **2800 CIC** (300+430+560+690+820), before construction-speed and infrastructure modifiers.
- Build methods: select a hub and click the middle (top) of the three icons — each click queues one more railway level along the whole connection to the capital; or use the production interface's **Railways** button and click the white number in a black circle on a rail link (each click adds one level).
- Higher rail level also speeds **strategic redeployment**.

### Building new hubs and ports

| Building | Cost | Notes |
|---|---|---|
| Naval base (port), level 1 | 5,000 CIC | +1,000 CIC per subsequent level |
| Supply hub (inland) | 20,000 CIC | Modified by construction-speed / infrastructure bonuses |
| Infrastructure, per level | 6,000 CIC | Four levels in one state cost more than a whole new supply hub |

- Both ports and supply hubs can be built in **allied and subject territory**.
- A port needs no rail link if it can trace convoys/ports/railways back to the capital.
- An inland hub needs a rail or river connection to the capital. **River connection is instant** if the hub's province borders a river that also touches the capital, or another hub/port on the same river.
- To rail-connect a new hub: construction interface → Railways → click a province with a capital-connected railway, then click the new hub's province. The new line inherits that railway's level; adjust with the +/- buttons in the construction list, or left-click (raise) / right-click (lower) the small number under the crossed-hammers icon on the map before it is built.
- Railways may be built in controlled, allied or subject territory at any time — no need to wait for the hub.

### Infrastructure and supply flow

- Each infrastructure level reduces hub-supply falloff, to a **maximum reduction of 0.3 at level 5 infrastructure**.
- The infrastructure that counts is that of the state the supply is flowing **out of**, not into. Supply crossing from a level-5 state into a bordering level-1 state flows as level 5; supply moving within the level-1 state flows as level 1.

### Trains

- Rail connections need **trains** the way convoy routes need convoys; the requirement scales with the supply drawn through each hub. Per-hub requirement is in the hub tooltip; the national total is in the logistics tooltip (crate icon with a percentage, top of screen).
- Too few trains → **reduced hub supply** delivered to divisions.
- Trains take **no attrition** but can be destroyed by enemy **Logistical Strike** air missions.

| Train model | Production cost | Notes |
|---|---|---|
| Train (base model) | 70 MIC | Starting model |
| Austerity train (unarmoured) | 50 MIC | Same job, cheaper |
| Armoured train | 105 MIC | Much more resistant to Logistics Strike; used automatically before other train types when available |

### Capturing rail and hubs

| Situation | Days before captured railway is usable |
|---|---|
| Non-core territory | 10 days |
| Core state | 5 days |
| Civil war | 0 (no cooldown) |

- Every province on the line must finish its conversion before a captured hub becomes functional.
- **Supply hubs themselves have no conversion time** — only the rail does.
- Rail can also need repair if damaged by strategic bombing or enemy scorched earth.

## State supply

State supply is a fixed pool per state, distributed **evenly to all units in the state** (land, air and naval) and drawn **before** hub or air supply. It comes from four sources: victory points, infrastructure, population, and a fixed "base supply" value some states have.

**Victory points:** a state containing any VP gets **0.2** supply, plus **0.05 per point of total VP value** in that state. (A state with a 1-point VP and a 5-point VP → 0.2 + 6×0.05 = 0.5.)

| Total VP value in state | 50 | 20 | 15 | 10 | 5 | 3 | 1 |
|---|---|---|---|---|---|---|---|
| State supply | 2.70 | 1.20 | 0.95 | 0.70 | 0.45 | 0.35 | 0.25 |

**Infrastructure:** **0.3 supply per level**, only while undamaged; damaged infrastructure gives proportionally less until repaired.

| Infrastructure level | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| State supply | 1.50 | 1.20 | 0.90 | 0.60 | 0.30 |

**Population:** diminishing scale, from **0.01 supply per province** in a 30,000-person state to **4.25 supply per province** in a 23.6 M state. Per million inhabitants this slides from **0.3 supply/million** in sparse states down to **0.18 supply/million** in very dense states (e.g. Chinese states).

Units drawing hub supply **still also draw state supply** — state supply is applied first regardless. So units outside hub range must share the state pool with units that are inside hub range.

The supply map-mode heat map shades a province using the *whole state's* remaining state supply, so moving more units into any province of the state lowers the effective supply everywhere in it.

### Contested states

If two warring countries each hold part of a state, state supply is split: the population and infrastructure components are divided by the **share of provinces owned**, while VP-derived supply goes entirely to whoever controls the province containing each victory point.

## Aerial supply

- Provided by **transport aircraft** flying the **Air Supply** mission; available anywhere in the air zone, regardless of the wing's actual range.
- Drawn **last** — only if state + hub supply cannot cover a unit's demand.
- **0.01 supply per plane** at 100% mission efficiency, fully supplied, in good weather.
- Mission efficiency (weather, squadron supply state, range-vs-air-zone-size) scales the supply delivered. A wing covering a larger fraction of the air zone delivers more.
- Transport wings on Air Supply can themselves only draw **state and hub** supply — they cannot feed on their own air supply.
- Air supply **does not restore fuel** to ground units.

## Supply consumption per battalion

Base supply use added to a division by each battalion / support company (before Logistics Company, terrain, weather and commander modifiers).

### Infantry battalions

| Battalion | Supply use |
|---|---|
| Infantry | 0.06 |
| Bicycle | 0.06 |
| Penal Battalion | 0.05 |
| Irregular Infantry | 0.04 |
| Militia | 0.06 |
| Mountaineers | 0.05 |
| Marines | 0.05 |
| Marine Commandos | 0.05 |
| Paratrooper | 0.05 |
| Rangers | 0.05 |
| Assault Battalion | 0.06 |
| Sturmtruppe Battalion | 0.05 |

### Mobile / mechanised battalions

| Battalion | Supply use |
|---|---|
| Cavalry | 0.06 |
| Camelry | 0.10 |
| Elephantry | 0.12 |
| Motorized Infantry | 0.065 |
| Mechanized Infantry | 0.14 |
| Amtrac Battalion | 0.18 |
| Armored Car | 0.14 |

### Line artillery / AT / AA

| Battalion | Supply use |
|---|---|
| Anti-Tank | 0.10 |
| Anti-Air | 0.10 |
| Artillery | 0.21 |
| Rocket Artillery | 0.22 |
| Motorized Anti-Tank | 0.15 |
| Motorized Anti-Air | 0.15 |
| Motorized Artillery | 0.25 |
| Truck-drawn Rocket Artillery | 0.25 |
| Motorized Rocket Artillery | 0.25 |

### Armour

| Battalion | Supply use |
|---|---|
| Light Tank | 0.22 |
| Medium Tank | 0.25 |
| Heavy Tank | 0.32 |
| Modern Tank | 0.25 |
| Super Heavy Tank | 0.40 |
| Land Cruiser | 0.6 |
| Amphibious Tank Battalion (any weight class) | 0.20 |
| Light Tank Destroyer | 0.20 |
| Medium Tank Destroyer | 0.22 |
| Heavy Tank Destroyer | 0.30 |
| Modern Tank Destroyer | 0.25 |
| Super Heavy Tank Destroyer | 0.40 |
| Light SP Artillery | 0.42 |
| Medium SP Artillery | 0.46 |
| Heavy SP Artillery | 0.60 |
| Modern SP Artillery | 0.50 |
| Super Heavy SP Artillery | 0.80 |
| Light / Medium / Heavy / Modern SP Anti-Air | 0.10 each |
| Super Heavy SP Anti-Air | 0.10 |

### Support companies

| Support company | Supply use | Supply-relevant effects |
|---|---|---|
| Logistics Company | 0 (no supply cost listed) | −10% division supply consumption, −5% division fuel consumption; blocks Helicopter Transports |
| Helicopter Transports | 0 (no supply cost listed) | −10% division supply consumption, terrain movement bonuses; blocks Logistics Company and Helicopter Brigade |
| Winter Logistics Company | 0.05 | +300% cold acclimatization gain, various snow bonuses |
| Helicopter Brigade | 0.07 | −5% supply consumption, +10% manpower trickleback, −5% XP loss from casualties |
| Support Anti-Tank | 0.08 | |
| Support Anti-Air | 0.10 | |
| Support Artillery | 0.16 | |
| Support Rocket Artillery | 0.16 | |
| Super-Heavy Artillery | 0.25 | |
| Self-Propelled Super-Heavy Artillery | 0.35 | |
| Cavalry Recon Company | 0.02 | |
| Recon Rangers | 0.06 | |
| Long Range Patrol Company | 0.04 | |
| Motorized Recon Company | 0.02 | |
| Armoured Car Recon Company | 0.02 | |
| Light Tank Recon Company | 0.02 | |
| Airborne Light Armour | 0.02 | |
| Helicopter Recon | 0.07 | |
| Engineer Company | 0.02 | |
| Armored Engineer Company | 0.035 | |
| Assault Engineer Company | 0.025 | |
| Pioneers | 0.02 | |
| Jungle Pioneers | 0.1 | |
| Field Hospital | 0.05 | |
| Helicopter Med-Evac | 0.07 | |
| Maintenance Company | 0.03 | |
| Armored Maintenance Company | 0.035 | |
| Military Police | 0.02 | |
| Motorized Military Police | 0.03 | |
| Signal Company | 0.02 | |
| Armored Signal Company | 0.035 | |
| Light Flame Tank Company | 0.02 | |
| Medium Flame Tank Company | 0.025 | |
| Heavy Flame Tank Company | 0.03 | |

## Logistics Company

Support company whose whole purpose is cutting the division's supply draw. Counts as a **motorized technology** for MIO and technology-bonus purposes.

| Base stats (Logistics Company) | Value |
|---|---|
| Manpower | 500 |
| Organization | 10 |
| Recovery rate | 0.30 |
| HP | 1.0 |
| Weight | 0.1 |
| Training time | 120 |
| Division supply usage | −10% |
| Division fuel usage | −5% |

Technology line:

| Technology | Year | Base research time | Prerequisites | Effect |
|---|---|---|---|---|
| Logistics Company I | 1936 | 137 days | Support Equipment, Truck | Enables Logistics Company (−10% supply usage, −5% fuel usage) |
| Helicopter Transport Company | 1938 | 220 days | Helicopter, Logistics Company I | Enables Helicopter Transports (−10% supply usage; +5% movement in Forest, Hills, Mountain, Plains, Jungle, Marsh, Desert and across Rivers) |
| Logistics Company II | 1939 | 165 days | Logistics Company I | Logistics Company: −10% supply usage, −5% fuel usage. Helicopter Transports: −12% supply usage |
| Logistics Company III | 1942 | 220 days | Logistics Company II | Logistics Company: −10% supply usage, −5% fuel usage. Helicopter Transports and Helicopter Brigade: −12% supply usage |
| Logistics Company IV | 1945 | 220 days | Logistics Company III | Logistics Company: −10% supply usage, −5% fuel usage. Helicopter Transports: −15% supply usage |

**Inferred:** with all four Logistics Company technologies the company reaches roughly −40% division supply usage and −20% division fuel usage (the upgrades are stated as repeated −10%/−5% steps; the wiki does not state whether they add or compound).

## Terrain effects on supply

**Supply flow penalty factor** is a *direct* subtraction from the hub-supply amount flowing into a province, added on top of other falloff — not a percentage. Urban terrain is the only terrain that *improves* flow (negative penalty). **Truck attrition factor** multiplies attrition on trucks motorising hubs in that terrain.

| Terrain | Supply flow penalty factor | Truck attrition factor | Movement cost | Attrition (equipment loss) |
|---|---|---|---|---|
| Plains | 0 | 0 | — | — |
| Forest | 0.08 | 0.2 | +50% | — |
| Hills | 0.1 | 0.2 | +50% | — |
| Mountain | 0.12 | 1.0 | +100% | +30% |
| Desert | 0.14 | 0.5 | +5% | +15% |
| Jungle | 0.16 | 3.0 | +50% | +20% |
| Marsh | 0.16 | 4.0 | +100% | +35% |
| Urban | **−0.2** (improves flow) | 0 | +20% | — |

Full terrain table (combat width, attack modifiers, fort levels, temperature bias) is in [Land combat](../02-land-warfare/land-combat.md).

## Weather effects on supply

Two distinct weather effects:
- **Supply Factor** — reduces the *flow* of supply from a hub into a province (effectively shrinking hub range).
- **Supply Consumption Factor** — increases the *draw* of a division.

These stack: e.g. Deep Snow ground condition plus a Blizzard weather event compounds both.

### Temperature modifiers

| Condition | Temperature (°C) | Supply Factor | Supply Consumption Factor | Truck attrition factor | Other |
|---|---|---|---|---|---|
| Extremely cold | −100 to −12 | −15% | — | 100% | +20% winter attrition, −20% attack, −30% breakthrough, −5% org regain, −60% entrenchment speed |
| Very cold | −12 to −4 | — | — | — | +10% winter attrition, −10% attack, −15% breakthrough, −30% entrenchment speed |
| Very hot | 20 to 28 | −5% | — | — | +10% heat attrition, −5% org regain |
| Extremely hot | 28 to 100 | — | **+50%** | 10% | +20% heat attrition, −10% attack, −10% org regain |

### State-level weather events

| Weather | Supply Factor | Supply Consumption Factor | Truck attrition factor | Org regain | Org loss when moving |
|---|---|---|---|---|---|
| Rain | — | −5% | — | — | — |
| Storm | −5% | −15% | — | 10% | 10% |
| Snow | — | −10% | — | 30% | — |
| Blizzard | −25% | +15% | 100% | −10% | 25% |
| Sandstorm | −15% | — | 300% | −20% | 25% |

### Province-level ground conditions

| Condition | Supply Factor | Truck attrition factor | Attrition | Division speed | Org loss when moving |
|---|---|---|---|---|---|
| Snow (ground) | −20% | 50% | — | −20% | 10% |
| Deep Snow | −40% | 100% | — | −50% | 25% |
| Mud | −15% | **500%** | +70% | −50% | 25% |
| Flooded | −40% | 300% | — | −50% | 25% |

Higher **infrastructure reduces mud growth in a province by up to −80%**.

## Effects of insufficient supply

### Land units

A division's supply level moves gradually toward what the province can support — it does not snap. Moving from a 100%-supplied province into a 50%-supplied one leaves the division at 100% for the first hour, then it decays.

Characteristics degraded as supply falls (severity scales with how bad the shortfall is):

| Affected stat | Note |
|---|---|
| Speed | |
| Max organization | |
| Organization regain speed | |
| Attack | Max penalty **−20% when attacking**, **−50% when defending** |
| Breakthrough | Applies to attacking units |
| Defense | Applies to defending units |
| Attrition | Begins once supply drops to **35% or below**, and worsens as supply falls further |

There can be a delay between reaching a low-supply state and the full penalty applying.

Reinforcement rules:
- **Manpower** reinforcements arrive as long as the division has a continuous friendly path (provinces/ports/convoys) to the capital, but arrive very slowly at low supply.
- **Equipment** resupply speed is *not* affected by supply state — but constant supply attrition can stop a division ever reaching full equipment.
- A division **cut off from the capital receives neither manpower nor equipment**, even if fully supplied by a victory point or by air supply.
- **Fuel**: slows like manpower when undersupplied, but **stops entirely** below a threshold. Air supply does not restore fuel, so an air-supplied but hub/state-starved division can still run dry.

### Stored supply / supply grace

- "Supply grace" and "stored supply" are the same thing: supply held above 100% while sitting in a fully supplied province.
- **Base stored supply is 150%.**
- Typically enough to operate at full efficiency for **2–3 days** in an unsupplied province before dropping below 100%.
- Special forces technologies extend supply grace; **Marine divisions led by a general with the Amphibious trait** get further extension. The extension is described in hours but is only indicative, because drain rate varies.
- Visible near the bottom of the division tooltip in the Army UI.

### Air units

- An air wing's supply is the supply level of the province containing its **airbase**.
- Below 100% supply the wing suffers a **mission-efficiency malus**; below a further threshold it also loses fuel, cutting efficiency again.

### Naval units

- Undersupply directly hurts **spotting efficiency** and **repair speed**, and slows fuel intake (which then hurts combat performance).
- Ships draw on the **full potential supply of their hub**, not limited by what the province can support, so naval undersupply is far rarer than land or air undersupply.

## Allies and supply

- By default allies may draw from each other's supply hubs in both directions.
- Fighting on **allied territory you cannot use the state supply system** — only hub (and air) supply. Host-country divisions on the same tile will therefore usually be better supplied.
- Supply for allies can be toggled off per hub: click the hub, then click the blue flag above-left of the hub symbol. The AI never does this.

## Cross-references

- [Land combat](../02-land-warfare/land-combat.md) — full terrain and weather tables, state categories, building slots.
- [Manpower and experience](manpower-and-experience.md) — attrition and accident formulas.
