---
title: Land Combat
category: land-warfare
tags: [land battle, combat width, reinforcement, damage, organization, entrenchment, encirclement, planning bonus, stacking penalty, terrain, weather, night, river, fort]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Land_battle
  - https://hoi4.paradoxwikis.com/Terrain
  - https://hoi4.paradoxwikis.com/Weather
---

## Summary

A land battle occurs in the **defender's province** when attacking divisions try to move in. It resolves in **one-hour turns**: divisions roll attacks against automatically-selected enemy divisions, each hit rolling dice for HP and organization damage. The battle ends when one side has no frontline divisions able to keep fighting; if the attacker wins, defenders retreat to another province, or **shatter** if they have nowhere to go. This file covers width, reinforcement, the exact damage formula, targeting, and every combat modifier.

## Combat width and terrain frontage

The concentration of force each side can bring is limited by the battle's **combat width**, set by the **terrain of the province being attacked**. Each additional province the attackers come from ("flanking") adds extra width. **Paradrops and naval invasions each add another flanking direction.**

| Terrain | Base combat width | + per extra attack direction | Movement cost | Attrition (equipment loss) | Attacker attack adjuster | Enemy air superiority reduction | Max fort level | Sickness | Supply flow penalty | Truck attrition | Temperature bias |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Plains | 70 | +35 | — | — | — | — | 5 | — | — | — | — |
| Desert | 70 | +35 | +5% | +15% | — | — | 4 | yes | 0.14 | 0.5 | — |
| Hills | 70 | +35 | +50% | — | −25% | −5% | 5 | — | 0.1 | 0.2 | −3 °C |
| Forest | 60 | +30 | +50% | — | −15% | −10% | 4 | — | 0.08 | 0.2 | −1 °C |
| Jungle | 60 | +30 | +50% | +20% | −30% | −25% | 3 | yes | 0.16 | 3.0 | +5 °C |
| Marsh | 50 | +25 | +100% | +35% | −40% | — | 3 | yes | 0.16 | 4.0 | — |
| Mountain | 50 | +25 | +100% | +30% | −50% | −10% | 4 | — | 0.12 | 1.0 | −7 °C |
| Urban | 80 | +40 | +20% | — | −30% | −50% | 5 | — | −0.2 | — | +3 °C |

"Sickness": army leaders may temporarily become **Sick** when at least 75% of the units they command are in that terrain. Terrain attrition applies only while at war.

### Division combat width

| Battalion type | Width |
|---|---|
| Infantry, armoured, cavalry, motorized, mechanized, tank destroyers | 2 |
| Artillery, rocket artillery (incl. motorized and self-propelled) | 3 |
| Anti-tank and anti-air (incl. motorized) | 1 |
| Support companies | 0 |

Width reductions:

| Source | Effect |
|---|---|
| **Vast Offensives** or **Human Wave Offensive** (mutually exclusive Mass Assault branches) | −0.4 width on ordinary infantry battalions → **25% more infantry battalions** fit in the same frontage |
| **Holding the Line** (Mountaineers special forces doctrine) | −0.2 width on mountaineer battalions |

### Over-width penalty and the join rule

```
combat width penalty = -100% × (total_width − battle_width) / battle_width
```

At the start of a battle and on every reinforcement, divisions are added from reserve **unless** the combat width is already filled **or** the resulting width penalty would exceed **−33%**.

- **80-width Urban battle:** 106 total width is allowed (penalty −32.5%); 107 is not (−33.75%).
- **70-width Plains battle:** with 10-width divisions the 8th stays in reserve because the width is already **filled** at 70 — even though the penalty would only be about −14.29%.

Design divisions whose width divides the terrain width you intend to fight in. Frontage Reduction effects let more divisions (or slightly bigger ones) fit.

## Reserves and reinforcement

Divisions that do not fit at the start, or that arrive later, go to **reserve**. In reserve they:

- deal and take **no damage**;
- **do not** regain organization;
- **do not** build entrenchment or planning bonus;
- **do** still contribute recon and anti-air.

**Base chance to join from reserve: 2% per hour** — a mean waiting time of about 35 hours. Improved by:

- **Radio** technology
- division speed
- doctrine technologies
- a **Signal Company** (initiative: **each 1% initiative = +0.25% reinforce rate**; a level-1 signal company's +10%/+20% initiative also speeds planning from 2%/day to 2.4%/day at 20%)

**Defender tactics.** Feed reserves early enough that they can actually reinforce before the line collapses. When fighting at full width with fresh reserves, pull very low-org defenders out **one at a time** to a province behind the line so they recover and reserves can slot in; otherwise every frontline division hits 0 org simultaneously and the reserves never get their chance.

**Attacker tactics.** Do not attack with more divisions than the width supports — the surplus sits in reserve instead of recovering org and accumulating planning bonus. When you *do* have width free and reserves available and the defender is already fully engaged, it is often better to **cancel the attack and re-attack** so all your units join immediately rather than trickling in at 2%/hour.

## Attack rolls and damage

### Attacks

Against a given target, the attacker's soft and hard attack combine by the target's **hardness**:

```
effective attacks ∝ soft_attack × (1 − hardness) + hard_attack × hardness
```

A 0% hardness target receives all soft attacks and no hard attacks; a 25% hardness target receives 25% of hard attacks and 75% of soft attacks.

### Defences

The target has a number of defences that partly protect it: **Defence** when it is on the defending side, **Breakthrough** when it is on the attacking side.

### The hourly resolution

```
number of attacks  = round( hardness-modified attack / 10 )
number of defences = round( defence / 10 )
```

Both reset every hour.

Each attack is a hit or a miss. **After each attack the defender removes one defence, if any remain.**

| Situation | Hit chance |
|---|---|
| Defender still has defences left | **10%** |
| Defender has no defences left | **40%** |

An attack point that lands after enemy defence is exhausted is therefore worth **four times** one that does not.

### Damage per hit

| Damage type | Die | Base multiplier |
|---|---|---|
| HP (strength) | **1d2** | **×0.06** |
| Organization | **1d4** | **×0.053** |

```
damage per hit = die_roll × base_multiplier × tactic attack modifier × armor reduction
```

Other modifiers change the **number of attacks** (and so the number of hits), not the damage per hit.

**Armour bonus:** when an armoured unit attacks a target with **insufficient piercing**, the organization die grows from **1d4 to 1d6** — average org damage per hit rises from 2.5 to 3.5, a **+40%** increase.

**HP scaling:** as a unit loses HP its damage output scales down, **rounded to multiples of 10%** (at 90–99.99% strength the output is scaled to 90%). Damage taken during a battle does **not** change the unit's other stats until the battle ends.

### Worked example (from the wiki)

Armoured division with 1000 soft attack vs an infantry division with 500 defence:

- 100 attacks total; **50 attacks against defence at 10%**, **50 against no defence at 40%**.
- Expected hits: `50×0.1 + 50×0.4 = 25`.
- Expected org die (unpierced armour, 1d6): **3.5**.
- Armoured division slightly under full HP → **90%** damage scaling.
- Org damage per hour: `25 × 3.5 × 0.90 × 0.053 = 4.17375`.
- Against a 50–60 org infantry division, the combat resolves in roughly **half a day**.

### Armour and piercing effects

| Comparison | Effect |
|---|---|
| Attacker piercing ≥ defender armour | No penalty; no extra org damage taken |
| Attacker piercing ≥ 75% of defender armour | **−20% damage** |
| Attacker piercing ≥ 50% of defender armour | **−35% damage** |
| Attacker piercing < 50% of defender armour | **−50% damage** |

Having more armour than the enemy's piercing also **increases your own number of attacks** and upgrades your org die to 1d6.

## Targeting and coordination

Each division has an **Engagement Width equal to twice its own combat width**, used to build a target list. Enemy divisions are added in **random order**, rejecting any that would push the list over the engagement width. If **no** enemy division fits, one is chosen at random. If some fit and some do not, only those that fit are eligible.

*Example:* a 36-width division has 72 engagement width. It can engage five 14-width divisions (70 ≤ 72), but only four of five 15-width divisions (75 > 72).

Attacks split into **uncoordinated** and **coordinated** parts:

```
coordinated share = 35% + Coordination × (1 + Initiative)
```

- **Uncoordinated attacks** are spread across all targets in the engagement width in proportion to their width.
- **Coordinated attacks** all go to one **priority target**, greatly raising the chance of breaking through its defences.
- **Initiative** is a division stat, mainly from **Signal companies**.
- **Coordination** is a global stat, mainly from **Radio** and **RADAR** technologies, plus some land doctrines and officer corps spirits.

**Priority target selection** weighs:

1. how the target's hardness affects the attacker's effective attack count, **with a slight bias toward hard attacks**;
2. **avoiding armoured targets** — if the target's armour exceeds the attacker's piercing, its rating is **halved**;
3. **favouring low organization**, via `100% − (org ratio / 4)`.

*Worked example:* a 36-width division with 1000 attacks facing five 14-width divisions with 200 defence each, no coordination modifiers. 650 attacks go to the split (130 each), and 350 go to the best target. The four secondary targets each face 130 attacks vs 200 defence; the priority target faces 480 vs 200. Add a second identical attacker and the secondaries face 260 vs 200 while the priority target faces 960 vs 200.

## Collateral damage

```
collateral damage = 0.1 × soft attack × (number of attacks) × damage dealing factor
```

- **Infrastructure** in the state is **always** damaged.
- **Fortifications** in the province are damaged with a **5% probability** per instance.
- **Close air support attacks cause no collateral damage.**
- The **Siege Artillery** ability **doubles both the probability and the damage** against land forts.
- Infrastructure damage is further scaled per the construction damage/repair rules.

## Combat factors

All factors **stack multiplicatively**. The final multiplier is **floored at 1%** if the product would be lower. The wiki notes this list is not exhaustive.

| Factor | Effect |
|---|---|
| **Terrain** | Attacker attack and breakthrough penalties in rough terrain, up to **−50%** (worse for heavy units). See the terrain table above. |
| **River crossing** | **−30%** (small river) or **−60%** (large river) to attacker attack and breakthrough |
| **Night** | **−50% land attack for both sides**; offset by Land Night Attack bonuses |
| **Fort** | **−15%** to attacker attack and breakthrough **per fort level**. Each extra attacking direction cancels one fort level — **but never the last level** |
| **Encirclement** | **−30% for the defender** when all surrounding land provinces are enemy-controlled (islands excluded) |
| **Enemy air superiority** | up to **−35%** for whichever side faces hostile air superiority |
| **Low supply** | Attacker: up to **−25% attack / −65% defence**. Defender: up to **−35% attack / −15% defence** |
| **Exceeding combat width** | **−1% per extra percent of width**, capped at **−33%** |
| **Stacking penalty** | **−2% per division over the stacking limit**. The limit is **5, plus 3 per flanking direction** |
| **In multiple combats** | **−50%** for a division fighting in more than one battle (e.g. attacking while being attacked) |
| **Paradrop penalty** | **−30%** for **48 hours** after being paradropped |
| **Amphibious penalty** | **−50%** |
| **Commander skill** | **+2.5% per skill point** to both attack and defence |
| **Planning bonus** | up to **+30%** for the attacker; doctrine can raise it to **+110% or more** |
| **Entrenchment** | **+2% for the defender per point built** |
| **Air support** | Attack and defence bonus, on top of the direct damage support planes deal |
| **Country bonus** | Various national modifiers |
| **Division experience** | Green **−25%**, Trained **0%**, Regular **+25%**, Seasoned **+50%**, Veteran **+75%** |
| **Intel advantage** | up to **+15%** from army intel advantage (starts at 5, maxes at 50 intel advantage) |
| **Tactics** | e.g. **+20%** from Breakthrough — see [combat-tactics.md](combat-tactics.md) |

**Stacking example (wiki):** experience +75%, entrenchment +40%, terrain +20%, country +40%, commander skill +35% → `1.75 × 1.4 × 1.2 × 1.4 × 1.35 = 5.56` = **+456%** to base stats.

### Entrenchment and dig-in

- Divisions build entrenchment **daily while stationary and not in combat**.
- Entrenchment gives **+2% defence per point** and is described as a force multiplier when defending.
- **All entrenchment is lost when a division attacks** — the sole exception is the **probing attack** command-power ability.
- Entrenchment level is shown in the army selection panel.
- Sources of extra max entrenchment: Engineer +2, Armored Engineer +3, Assault Engineer +2, Pioneers +2.5, Jungle Pioneers +2 (see [land-units-and-stats.md](land-units-and-stats.md)).
- Entrenchment **speed** is modified by weather: Extremely cold **−60%**, Very cold **−30%**, Snow **+5%**, Deep Snow **+15%**, Flooded **−20%**.

### Planning bonus

- Accumulates while a battle plan is drawn and not executed, up to **+30%** base, raised to **+110% or more** by land doctrine.
- Planning progresses at a base **2%/day**, scaled by **initiative** (20% initiative → 2.4%/day).
- Divisions sitting in **reserve during a battle do not accumulate planning bonus** — another reason not to over-commit to a battle.

### Encirclement

- A defender whose surrounding land provinces are **all** enemy-controlled takes a **−30%** penalty (islands are excluded from the check).
- A defeated defender with **nowhere to retreat is destroyed (shatters)** rather than retreating.
- A division that loses all organization while defending flees to the nearest friendly province; if it cannot leave the province, it is destroyed.

## Terrain features

Terrain features apply on top of base terrain and stack **multiplicatively** with it. Unlike base terrain modifiers, features **only affect the attacker**, because they depend on the specific path taken and the defender may face attacks from several directions. Attack adjusters modify the attacker's soft and hard attack; defence adjusters modify the attacker's breakthrough.

| Feature | Effect |
|---|---|
| **Small river** | −30% attack and defence, −25% movement |
| **Large river** | −60% attack and defence, −50% movement |
| **Amphibious landing** | −50% attack and defence |
| **Fort** | −15% attack and defence **per level**, up to **−150% at level 10** |

- The **river** adjuster applies whenever the path intersects a river. An active river modifier also **enables certain combat tactics**.
- The **amphibious** penalty applies when attacking a land province from a sea province. It sits on top of an additional scaling modifier of **−80% attacker soft and hard attack and +50% attacker breakthrough**, which **decays over the course of the combat**; both the modifiers and their decay rate are affected by transport technologies. Naval invasion movement speed is fixed at **3.557 km/h**, adjustable by division terrain modifiers.
- The **fort** adjuster applies to land forts from **all** directions, but **not to naval invasions**. Each extra attacking direction reduces the effective fort level by 1 (worth +15%). **Coastal forts** reduce attack for naval invasions and for attacks across straits.

### Paths and movement cost

A path between two adjacent provinces is the straight line between their centres, traced on a pixel grid — so **diagonal paths are noticeably longer** than north–south or east–west ones. The terrain **along the path** (not just the endpoints) sets the movement cost, and can mix terrains: two coastal mountain provinces across a fjord might give a path 40% mountain / 60% ocean, costing +40% instead of +100%. Amphibious landing path cost is fixed at **24 pixels = 170.736 km**.

### Unit-specific terrain adjusters

- The division's net adjuster is the **average of its combat battalions plus the sum of its support companies**. Divisions short of manpower get proportionately smaller bonuses *and* penalties.
- For **regular terrain**: the attack value modifies the attacker's soft attack, hard attack and breakthrough; the defence value modifies the defender's soft attack, hard attack and defence.
- For **rivers**: attack value modifies the attacker's soft and hard attack; defence value modifies the attacker's **breakthrough**. Defenders get no river adjusters.
- For **forts**: attack value modifies attacker soft/hard attack; defence value modifies attacker breakthrough **and defender defence**.
- For **amphibious**: attack value modifies attacker soft attack, hard attack and breakthrough; the defence value does nothing. Defenders get no amphibious adjusters.
- Unit adjusters apply **additively onto the base feature penalty**, effectively negating it. **Amphibious and fort attack adjusters are capped by the base penalty** and cannot turn into net bonuses; **river adjusters can** exceed it. Fort **defence** modifiers have no cap for defenders.

## Night and weather

### Night

The game simulates a full day–night cycle per province every hour, roughly 12h/12h averaged over the year, with far more variation near the poles.

| Nighttime effect | Value |
|---|---|
| Land attack | **−50%** |
| Air detection | −20% |
| Naval hit chance | −25% |
| Carrier traffic | −100% |
| Bombing targeting | −50% |
| Naval retreat speed | +10% |
| Close air support damage | ×0.1 |

**Land Night Attack** bonuses (e.g. **Night Assault Tactics**, Night Vision technologies) **negate the base penalty** rather than simply adding attack at night — an important distinction when several sources stack.

### Temperature modifiers

| Modifier | Range (°C) | Heat attrition | Winter attrition | Division attack | Division breakthrough | Org regain | Entrenchment speed | Supply consumption | Supply factor | Truck attrition | Daily hot acclim. | Daily cold acclim. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Extremely cold** | −100 to −12 | — | +20% | **−20%** | **−30%** | −5% | −60% | — | −15% | 100% | — | +0.2% |
| **Very cold** | −12 to −4 | — | +10% | −10% | −15% | — | −30% | — | — | — | — | +0.1% |
| **Very hot** | 20 to 28 | +10% | — | — | — | −5% | — | — | −5% | — | +0.2% | — |
| **Extremely hot** | 28 to 100 | +20% | — | −10% | — | −10% | — | +50% | — | 10% | +0.4% | — |

Weather attrition applies **only if the controller is at war**.

**Terrain temperature bias:** Mountain −7 °C, Hills −3 °C, Forest −1 °C, Urban +3 °C, Jungle +5 °C. Province temperature changes at most **6 °C per update tick** and is smoothed between neighbours. Strategic regions define allowed temperature ranges per day of year.

**Acclimatization** reduces these negative effects by up to **50%**. Units gain hot acclimatization in Very/Extremely hot provinces and cold acclimatization in Extremely cold, Very cold, Snow, Blizzard and Deep Snow provinces. Acclimatization gain is **×3 in combat**, and boosted by the **Adaptable** commander trait or the **Shared Instructors** special forces doctrine. It decays when unused, and **×2 as fast** when a cold-acclimatized unit sits in a hot province or vice versa. Winter attrition can be reduced by a commander with **Winter Specialist** (earned by long service in cold weather); there is no heat equivalent, though **South Africa** has a unique **Desert Equipment** focus reducing heat attrition.

### Province-level weather modifiers (ground combat)

| Modifier | Attrition | Division attack | Division breakthrough | Division defence | Division speed | Attacking division speed | Entrenchment speed | Org regain | Org loss moving | Supply factor | Truck attrition | Daily cold acclim. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Snow (ground)** | — | −20% | −15% | — | −20% | −25% | +5% | — | +10% | −20% | 50% | +0.1% |
| **Deep Snow** | — | −40% | −30% | — | −50% | −50% | +15% | −5% | +25% | −40% | 100% | +5% |
| **Mud** | +70% | −40% | — | — | −50% | — | — | — | +25% | −15% | 500% | — |
| **Flooded** | — | — | — | **+50%** | −50% | — | −20% | — | +25% | −40% | 300% | — |

Snow and Deep Snow debuffs **stack on top of** Extremely cold / Very cold. Mud especially punishes motorized supply (500% truck attrition).

### State-level weather events

| Event | Air accidents | Air detection | Air mission eff. | Carrier traffic | Naval detection | Naval hit | Naval retreat spd | Naval speed | Naval strike | Positioning | Casualties on sink | Naval attrition | Ground bombing targeting | Org loss moving | Supply consumption | Org regain | Supply factor | Truck attrition | Attacking div. speed | Daily cold acclim. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Rain** | +10% | −10% | −10% | — | −10% | −5% | +5% | −5% | −20% | — | — | — | 5% | — | −5% | — | — | — | — | — |
| **Storm** | +30% | −20% | −30% | −80% | −20% | −20% | +10% | −10% | −40% | −10% | — | — | −50% | 10% | −15% | 10% | −5% | — | — | — |
| **Snow** | +10% | −15% | −10% | — | −15% | −5% | +5% | −5% | −30% | −10% | — | — | 10% | — | −10% | 30% | — | — | — | +0.1% |
| **Blizzard** | +30% | −30% | −30% | −100% | −30% | −10% | +15% | −10% | −40% | −20% | — | — | −70% | 25% | 15% | −10% | −25% | 100% | −25% | +0.2% |
| **Sandstorm** | +60% | −90% | −50% | — | — | — | — | — | −90% | — | — | — | −100% | 25% | — | −20% | −15% | 300% | — | — |
| **Shark Infested Waters** | — | — | — | — | — | — | — | — | — | — | +60% | — | — | — | — | — | — | — | — | — |
| **Arctic Water** | — | — | — | — | — | — | −5% | — | — | −20% | +20% | +10% | — | — | — | — | — | — | — | — |

### Terrain effect on weather likelihood

| Weather | Mountain | Plains | Marsh | Desert | Jungle | Urban |
|---|---|---|---|---|---|---|
| Mud | −30% | +50% | +90% | +10% | +20% | — |
| Rain | — | — | — | — | +20% | — |
| Storm | — | — | — | — | +20% | — |
| Snow | +80% | — | — | −100% | — | −40% |
| Blizzard | +80% | — | — | −100% | — | −40% |
| Sandstorm | −100% | — | — | +80% | — | — |

**Mud formation:** the game tracks collected water per province from rain, storms and snowmelt. Snow melts at ≥0 °C (melt rate rises linearly to a cap at 12 °C); collected water evaporates from ≥2 °C (rate rises linearly to a cap at 38 °C); mud **freezes and is negated at ≤−1 °C**. Snow can only fall at ≤1 °C, with snowfall rate rising linearly to a cap at −4 °C. Higher **infrastructure reduces mud growth by up to −80%**. Classic mud seasons: spring and late autumn in the western Soviet Union and north-eastern USA; wet mild winters in northern France and southern UK.

## After the battle

### Equipment and manpower losses

The ratio of **HP lost** is converted into equipment and manpower losses with a factor of **70%**. A division's stats are locked for the duration of the combat (provided the template is unchanged) and only update afterwards.

### Equipment capture

The winner captures part of the enemy's lost equipment through **Equipment Capture Ratio (ECR)**, default **0%**. Sources: **Maintenance companies**, the **Scavenger** general trait, and various national spirits.

Each division's share of the enemy's losses is proportional to its **manpower × ECR**, and it recovers that share **times its own ECR**.

*Example:* winner has division A with 10 000 manpower and 5% ECR and division B with 20 000 manpower and 10% ECR. Weighted shares are 20% and 80%. A recovers `20% × 5% = 1%` of the enemy's lost equipment; B recovers `80% × 10% = 8%`.

### Equipment recovery

```
recovery ratio per division = reliability² × 40%
```

Applied to that division's own lost equipment, including shot-down air support planes. With many divisions the **total can exceed 100%**: 15 divisions attacking successfully with 90%-reliability infantry equipment recover `0.9² × 40% × 15 = 486%` of what they lost.

## Related files

- [combat-tactics.md](combat-tactics.md) — the daily tactic system that modifies these numbers
- [division-designer.md](division-designer.md) — how to build for width, org and armour
- [land-units-and-stats.md](land-units-and-stats.md) — per-battalion attack, defence, armour and piercing values
- [land-warfare-overview.md](land-warfare-overview.md) — command groups, invasions, border wars
