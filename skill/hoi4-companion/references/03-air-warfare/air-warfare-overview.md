---
title: Air Warfare Overview
category: mechanics
tags: [air, air-base, air-wing, mission-efficiency, air-superiority, detection, missions, rebasing, aces]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Air_warfare
  - https://hoi4.paradoxwikis.com/Air_missions
---

## Summary

Air warfare deploys air wings from air bases into **strategic regions**, where they fly missions against enemy aircraft, land units, ships, supply and buildings. It is the only warfare type that touches all three combat domains plus the strategic layer. The two numbers that govern everything are **mission efficiency** (what fraction of a wing actually flies) and **air superiority** (who dominates the region).

---

## Deployment

Air warfare is managed in the **Strategic Air** map mode. Almost all air operations work at the scale of a strategic region, not a province.

### Air bases

- Air bases are **state-wide buildings** built/repaired in the Construction screen, but they physically sit in one fixed province of the state. **Whoever controls that province controls the base.**
- When a base is captured, stationed planes automatically relocate to another available base — they are not lost. If no base is available they are lost.
- Air bases can be damaged by strategic bombing, which reduces capacity until repaired.

#### Capacity

| Item | Value |
|---|---|
| Capacity per air base level | 200 planes |
| Maximum air base level | 10 |
| Maximum planes per land base | 2000 |
| Carrier capacity | equal to the carrier's **deck space** stat |
| Overcrowding penalty | −2% per 1% over capacity |
| Penalty at 50% over capacity | −100% (no planes can fly at all) |

- All plane types, including carrier-capable models, may sit at a land air base.
- Capacity is **shared between allies**. The base tooltip lists total planes present and which countries/plane types are there. Allied wings can silently overcrowd your base.
- Overcrowding is the single most common cause of a red mission-efficiency icon. Rebase off a full base immediately.

#### Carrier fleets as air bases

- Carriers are floating air bases; capacity = deck size. Most carriers accept only **carrier-capable** aircraft; **ice carriers** accept all types.
- Planes on a carrier automatically join naval battles when not assigned to a mission and/or when the carrier's task force is on a mission.
- Air wings on carriers that are **on hold** (no naval mission) and outside port can fly ordinary air missions. Uses: CAS for an amphibious invasion beyond land-base range, exercising green wings so they fight better in naval battles, hunting unescorted enemy patrol bombers from outside their range.
- Carrier overcrowding applies the same penalty as land bases, but it is reduced by the **Massed Strikes** naval doctrine, and in naval battles it can be offset by >100% sortie efficiency.

### Air wings

| Item | Value |
|---|---|
| Land-based wing size | 100 planes |
| Carrier-based wing size | 10 planes |
| Time for a new wing to arrive at its base | 2 days |
| Land↔carrier rebase penalty | 48 hours with no reinforcement |

- A wing is created from the air base screen and needs both sufficient **planes in stockpile** and sufficient **service manpower**.
- All planes in a wing must be the same type / capable of the same missions — no mixing fighters with bombers. **Different models of the same type may be mixed** (e.g. 1936 and 1940 fighters in one wing).
- **Reinforcement level** is the wing's current planes vs. full strength. Below it, planes are drawn from the stockpile; if the stockpile is empty, reinforcement waits on new production.
- Wings can be **split**, **merged**, or **reorganized** (the reorganize tool gives fine control over moving planes between two or more wings of the same type) in the air base view.
- A new wing can be assigned a region and missions immediately, but will not fly until the planes arrive.
- **Rebasing** time depends on distance to the new base and the **speed of the slowest aircraft model** in the wing.
- Disbanding a wing returns all its planes to the equipment stockpile.

---

## Mission efficiency

Mission efficiency is the percentage of a wing's planes that actually carry out the assigned mission. It is shown per-region in the strategic air view and per-wing in the air base view.

| Icon colour | Meaning |
|---|---|
| Red | efficiency < 50% |
| Yellow | 50% ≤ efficiency < 100% |
| Green | efficiency = 100% |
| Clock overlay | wing recently arrived; efficiency is still building up |

**Per-wing effects:**

- **Range shortfall** — if the wing's range does not cover the whole strategic region, it takes a penalty proportional to the uncovered provinces.
- **Airbase overcrowding** — large penalty (see table above).
- **Bad weather** — reduces efficiency.
- **Lack of fuel** — reduces efficiency.
- **Newly arrived in region** — temporary, decaying penalty.

**Per-region effects:**

- Region efficiency is the **weighted average** of the efficiency of all wings operating there.
- **More Ground Crews** (toggled in the strategic air map mode) gives **+10% mission efficiency**, applied **multiplicatively**.

Missions are flown regardless of weather, but bad weather cuts detection and efficiency and raises take-off/landing accident risk. Sandstorms and blizzards are the worst; putting wings on standby during them is often correct.

### The other "mission efficiency" modifiers

Separate from the above, there are modifiers named **Air Superiority Mission Efficiency**, **Interception Mission Efficiency**, **Air Support Mission Efficiency** and **Naval Mission Efficiency**. These do **not** change how many planes fly; they improve these stats for planes on that mission type:

- Agility
- Air Attack
- Air Defense
- Naval Agility
- Naval Attack

> ⚠️ **Escort Efficiency** belongs to the same modifier family but **has no effect in game**. Do not pick doctrine nodes for it alone.

Note the trap: **Air Support Mission Efficiency does not boost Ground Attack**, so it does *not* increase the damage CAS deals to land units.

---

## Air superiority

Air superiority is the degree of dominance over the enemy air force in a strategic region. It is generated only by planes **actively flying their mission**.

**Air power of a wing = number of planes × superiority power × mission efficiency.**

| Aircraft type | Superiority power |
|---|---|
| Heavy Fighter | 1.25 |
| Fighter, Carrier Fighter, Jet Fighter, CAS, Carrier CAS, NAV, Carrier NAV, TAC, Jet TAC | 1.00 |
| Strategic Bomber, Jet Strategic Bomber | 0.01 |

Region superiority compares your air power (plus allies') against the enemy's, expressed as a percentage.

| Colour | Air superiority % | Meaning |
|---|---|---|
| Red | < 40% | enemy holds air superiority |
| Yellow | 40% – 60% | contested region |
| Green | > 60% | you (or allies) hold air superiority |

The ratio is **non-linear with heavy diminishing returns**: at 4000 allied vs. 500 enemy planes, adding 1000 more allied planes raises superiority by only **1.3 percentage points**.

### Things that subtract air power

- **Anti-air buildings**: each level (max level 5 per state) gives **−5 air power to the opposing side**, up to **−25**.
- **Rocket sites on Surface to Air missions** (requires Götterdämmerung) add **5 × air attack of the missile wing** air power per missile wing, theoretical max 15 per site. In practice only **Surface-to-Air Missile I** exists, with 0.25 Air Attack → **+1.25 superiority per active missile wing, max +3.75 per rocket site**, before their reduced mission efficiency from short range.

### Effects of air superiority

| Effect | Value |
|---|---|
| Enemy land combat **defense and breakthrough** | −0.7% per point of superiority advantage, max **−35%** at 100% |
| Enemy **movement speed** | up to **−30%** at 100% superiority (unmodified) |
| Sea zone **surface and sub detection** | up to **+25%** |

- Example: at 60% air superiority the enemy takes −7% defense and breakthrough.
- Air doctrines multiply the final air support penalty by (1 + doctrine bonus). E.g. a −10% penalty with +30% air superiority bonus from the full **Battlefield Support** line becomes −10% × 1.30 = **−13%**.
- **Divisional anti-air** (line AA, Support Anti-air, other sources) reduces penalties from hostile air superiority down to a floor of **0.25×** their unmodified value. The effect is **not linear** — it tapers off with more AA.

### Air superiority and raids/special missions

| Operation | Air superiority effect |
|---|---|
| Paradrop | requires **at least 70% air superiority**, otherwise impossible |
| Most aerial raids | −10% success at 0% superiority → +10% at 100% |
| Lock bombing, dam busting, oilfield raids | −20% at 0% → +20% at 100% |
| Nuclear strike, thermonuclear strike, mine sabotage, pathfinder raids | −25% at 0% → +25% at 100% |
| Raid intel | air superiority contributes up to **50%** of intel on success chance |

---

## Detection

Detection determines what percentage of enemy planes in a region are visible. **Friendly planes that can attack are capped at 3× the number of detected enemy planes**, so detection is what lets a big air force actually be used.

**Additive sources:**

| Source | Maximum |
|---|---|
| Occupying land in the strategic region | +10% (whole region controlled) |
| Radar coverage | +50% at full coverage |
| Own planes operating in the region | +80% at 3000 planes (non-fighters count at only 50% efficiency) |

**Then reduced by:**

| Source | Effect |
|---|---|
| Night-time | −20% detection |
| Bad weather | up to −90% detection |

**Situational visibility modifiers on the enemy side:**

- If the enemy has both ground-mission planes and superiority/escort fighters, the **fighters are always fully visible** (they need not be the same country as the bombers).
- Regular bombers on strategic bombing and carrier-based bombers reduce their visibility via the **Strategic bombing visibility** modifier (e.g. from the **Infiltration Bombing** doctrine).
- Planes on **close air support are 2× as visible** (capped at 100%).
- Planes on **port strike are 10× as visible** (capped at 100%).

Wings sortie in **descending order of air attack and agility**, so your best wings get the limited slots when enemy visibility is low.

See [Air combat](air-combat.md) for how detection feeds into damage and disruption.

---

## Mission types

Each mission lists which plane types can fly it.

### Pilot exercises
**Available for:** all planes **except** rocket interceptors, transport planes and scout planes.
Gains wing experience and country **air experience**. Consumes fuel and raises accident risk. **Enabling pilot exercises disables all other missions.** Shift-click the button to exercise only until fully trained, then stop automatically (a distinct icon shows this is set).

### Air superiority / escort
**Available for:** Fighter, Heavy Fighter, Jet Fighter.
Fights and **disrupts** all enemy wings in the region. Doubles as the **escort** mission: it reduces the disruption enemy fighters inflict on your own bombers in the region.

### Interception
**Available for:** Fighter, Heavy Fighter, Jet Fighter, Rocket Interceptor.
Only engages when enemy **bombers, transport planes or scout planes** are detected. Will fight the escorting fighters too, but **contributes nothing to that region's air superiority**. Lower losses than air superiority — the fallback when you cannot win the superiority contest.

### Close air support (CAS)
**Available for:** CAS, Tactical Bomber, Jet Tactical Bomber.
Joins land combats anywhere in range within the region. Gives an attack bonus to friendly divisions and directly damages enemy organisation and strength.

- **Target priority** = excess wing range (in map pixels) + total number of divisions on both sides of the battle. Battles close to the air base and with more divisions are preferred.
- **Planes per battle cap** = 3 × the enemy's used combat width frontage, then modified by the province terrain's "enemy air superiority" column.
  - Example: a Forest province (−10%) against one enemy division of combat width 20 allows 3 × 20 × 0.9 = **54 CAS planes**.
- A wing larger than one battle's cap **splits across several battles**; several wings can fill one battle. **There is no need to match wing size to combat width.**

**Attack bonus to friendly land units:** base **+25%**, scaled linearly by planes present ÷ maximum allowed. With 27 of 54 planes → +12.5%. With 48 of 54 → +22.22%.

**Damage to enemy divisions:** attacking planes make `ground attack × number of planes` attacks against one randomly selected enemy division. Aces increase the number of attacks; weather decreases it (multiplicative). Attacks resolve like land combat but **ignore defense, hardness and armor**. Damage is scaled by **0.035 to organisation and 0.035 to strength** (versus 0.053 org / 0.06 strength in normal land combat).

**Counters:** generals/field marshals with **Camouflage Expert** and Concealment-specialist military high command reduce incoming CAS damage.

**Divisional AA against CAS:** anti-air is averaged over all divisions on the enemy side including reserves.
- Damage reduction caps at **75%**, already reached at **4.3 average anti-air attack**.
- Divisional AA has a **7% chance per attack** to shoot planes down; when it fires it kills up to **0.5% × (air attack)** of the attacking planes, rolled randomly up to that cap (≈ half on average), but **always at least one plane**.
- **No plane attribute affects AA effectiveness.**
- Worked example: four divisions with 1936 Support Anti-air (15.2 air attack) and four with none → average 15.2×4/8 = **7.6**. Against 91 CAS planes every 8 hours the long-run loss is 7% × 7.6 × (0.5%/2) × 91 = **0.12103 planes per attack**.

**Air experience:** every plane that joins a battle produces **0.0005 air experience**.

### Strategic bombing
**Available for:** Strategic Bomber, Jet Strategic Bomber, Tactical Bomber, Jet Tactical Bomber.
Damages enemy buildings, industry and infrastructure. Target type (air bases, radar, forts, infrastructure, industry, etc.) can be prioritised per region.

- Roughly **120 damage per attack cycle ≈ 0.3 buildings destroyed**, distributed among all targeted buildings in the region regardless of how many wings are present.
- Damage varies greatly day to day (deliberate inaccuracy simulation).
- Bombers get shot at by **state anti-air**.

**Attacker notes:** strategic bombers are extremely expensive and need large numbers to matter — weigh the factory opportunity cost. Only **heavy fighters** have the range to escort deep, but they lose to light fighters.

**Defender notes:**
- **Anti-air buildings** both shoot bombers down and **absorb bombs** that would otherwise hit factories, refineries, resources and naval facilities.
- Intercept with fighters; **heavy fighters** are better against bombers. Bombers are slow and unagile, so **guns** are the best weapon on defensive fighters.
- **Construction Repair** continuous focus speeds building repair.
- **Dispersed Industry** technologies reduce factory bombing vulnerability.
- Assess results in the region's air combat screen (buildings bombed, % of bombers disrupted).

### Naval strike
**Available for:** Naval Bomber, CAS, Tactical Bomber, Jet Tactical Bomber.
Attacks enemy ships both inside and outside naval battles; mechanics are identical in both cases. Base **4% chance to detect an enemy fleet**, modified by other variables. Wings may be hit by naval anti-air.

- **Outside** naval battles, naval strikes never attack resource/supply convoys, though they do attack **troop convoys**. Convoys auto-repair between battles and most aircraft cannot sink one in a single pass — generally only 1940-tech planes can.
- **Combined with a surface/submarine attack**, resource and supply convoys become valid targets and do not repair until the battle ends, so far more aircraft types can sink them.

### Kamikaze strike
**Available for:** Fighter (must be unlocked by country rule).
Identical to naval strike but with **increased effectiveness and increased losses**. Unlocked by:
- Japan: **Warrior Spirit**
- Italy: **By Blood Alone** or **Il Vento Aureo**
- Generic focus tree countries: **Ideological Fanaticism**

### Port strike
**Available for:** Naval Bomber, CAS, Tactical Bomber, Jet Tactical Bomber.
Attacks enemy ships sitting in a naval base. Naval bases are on land provinces, so the region must cover land. The naval base itself is damaged on a successful attack; **empty bases cannot be attacked**. The "Port strikes" modifier (e.g. from the **Base Strike** naval doctrine) modifies the **naval strike attack** stat. Wings may be hit by state anti-air — and port strikers are **10× as visible** to enemy fighters.

### Logistics strike
**Available for:** CAS, Tactical Bomber, Jet Tactical Bomber.
Attacks enemy trucks, trains and railways.

### Air supply
**Available for:** Transport plane.
Each transport plane delivers up to **0.01 supply**, so a full 100-plane wing delivers up to **1.0 supply** under optimal conditions. Modified by wing experience, supply already present in the source province and at the transport wing's air base, and mission efficiency — a supply shortage at the source, lack of air superiority, or insufficient range to cover the whole target region all reduce delivery. Supply is added to the state supply of states in the target air region. **More Ground Crews** adds **+10%**. Costs **0.05 command power per plane** while active (command points are used automatically). Transports can be shot down by enemy interceptors and by anti-air.

### Naval minelaying
**Available for:** Naval Bomber, Tactical Bomber, Jet Tactical Bomber, Strategic Bomber, Jet Strategic Bomber.
Requires the **Aerial Minelaying** technology. Only assignable **during wartime**. Wings lay mines until the region reaches **1000 mines** (full saturation). Rate depends on plane count and type. Hovering a region in strategic air or navy map mode shows mines laid and enemy ships damaged/sunk.

**Minelaying efficiency by type (without By Blood Alone):**

| Plane type | Efficiency |
|---|---|
| Naval Bomber | 5% |
| Tactical Bomber | 8% |
| Jet Tactical Bomber | 8% |
| Strategic Bomber | 13% |
| Jet Strategic Bomber | 13% |

With **By Blood Alone**, efficiency instead comes from the design's **Minelaying** stat.

### Naval minesweeping
**Available for:** Naval Bomber, Tactical Bomber, Jet Tactical Bomber.
Requires the **Aerial Minesweeping** technology. Wartime only. Wings clear mines until the region is clear.

**Minesweeping efficiency by type (without By Blood Alone):**

| Plane type | Efficiency |
|---|---|
| Naval Bomber | 10% |
| Tactical Bomber | 15% |
| Jet Tactical Bomber | 15% |

With **By Blood Alone**, efficiency comes from the design's **Minesweeping** stat.

### Air recon
**Available for:** Scout Planes.
Adds intel on countries in the target air zone, on top of all other intel sources; visible in the Intel Ledger. Scout planes **do contribute to air superiority** in the zone even though they never engage. This is detectable by the enemy: a zone reporting no fighters or bombers but non-zero enemy superiority implies active scout planes.

### Naval patrol
**Available for:** Naval Bombers and Scout Planes.
Patrols a sea zone without engaging. Gives friendly **ships on patrol mission in the same zone** a bonus to spotting enemies; more air wings gives a bigger bonus. **If no ships are on patrol there, the mission does nothing.**

---

## Multiple missions on one wing

A wing with several missions selected flies **exactly one mission type per mission opportunity** — the first one in priority order (left-to-right in the air UI) whose condition is true. Mission-specific efficiency bonuses apply only for the mission actually flown.

To fly several missions at once, **split into several smaller wings**, one per mission.

Read this table top-down and stop at the first true condition:

| Mission | Condition |
|---|---|
| Pilot Exercises | Always executes |
| Air Superiority | Always executes |
| Close Air Support | Ground battles are in progress |
| Interception | Enemy bombers are detected in an assigned air zone |
| Strategic Bombing | At least one undamaged building, including state buildings in partially covered states |
| Naval Strike | Enemy ships are detected |
| Kamikaze Strike | Enemy ships are detected |
| Port Strike | Enemy task force in port |
| Logistics Strike | Enemy divisions or air wings are receiving supply from a supply node |
| Air Supply | At least one friendly division with non-zero supply consumption is present |
| Naval Minelaying | Always executes |
| Naval Minesweeping | Always executes |
| Air Recon | Always executes |

**Key consequence:** if a mission marked "Always executes" is selected, **no lower-priority mission on that wing will ever fly**. Never put Air Superiority on the same wing as anything you actually want flown.

---

## Aces

Air combat can generate aces. **A wing may hold at most one assigned ace.**

| Skill level | Chance | Fighter ace | (Strategic) Bomber ace | Support ace (CAS, TAC, NAV) |
|---|---|---|---|---|
| "Good" | 0.9 | Air Attack +3%, Speed +3%, Agility +5% | Strategic Bombing +5%, Range +3% | Naval Targeting +5%, Ground attack factor +3%, Agility +5% |
| "Unique" | 0.4 | Air Attack +6%, Speed +5%, Agility +10% | Strategic Bombing +10%, Range +6% | Naval Targeting +10%, Ground attack factor +5%, Agility +10% |
| "Genius" | 0.05 | Air Attack +10%, Speed +8%, Agility +15% | Strategic Bombing +15%, Range +10% | Naval Targeting +15%, Ground attack factor +8%, Agility +15% |

Ace effects are **scaled inversely by wing size relative to 100 planes**, up to a maximum of **50× at 2 planes**. This is the basis of "ace stacking" with tiny wings.

**Ace generation.** After a sortie, a wing can roll for an ace if it: dealt damage to enemy wings in air-to-air combat; dealt more points of damage to a ship than it lost in the attack; or successfully damaged an enemy structure. Each time, the chance is **1% + 0.005% per plane in the wing, rolled twice**.

| Wing size | Overall ace chance per qualifying sortie |
|---|---|
| 100 planes (full land wing) | 2.9775% |
| 10 planes (full carrier wing) | ≈ 2.0890% |

If a wing that already has a living ace generates another, the new ace goes to **reserve**.

**Ace death.** An ace can die whenever the wing loses at least one plane in a sortie. Chance = **0.5% + 0.001% per plane lost in that sortie**. A dead ace stays nominally assigned (coffin icon) and gives **no bonuses**; it is auto-unassigned only when the same wing generates a new ace. Living reserve aces must be **manually assigned** to a wing holding a dead ace.

---

## Strategy: fixing low mission efficiency

Deploying more planes offsets low efficiency only up to a point. Better options: base closer to the region's centre, or use longer-ranged designs.

If you control **no air base inside the region you are attacking**, you are at a heavy disadvantage against a defender who does. Options:

- Use **tactical bombers instead of CAS** (longer range) and **heavy fighters** for escort range.
- **Capture an enemy air base fast**; even building a fresh level-1 base in a newly captured state without one is often worth it, since that lets you station 200 planes inside the region.
- **Strategically bomb enemy air bases** to cut their capacity and force *their* overcrowding — only effective if their bases are already near full.
- Anchor a **carrier fleet** off the coast: it provides in-region basing, protects invasion convoys, and adds shore bombardment.
- Give up the superiority contest and fly **interception only**. Fighters then take off only when they detect targets, taking far fewer losses — at the cost of conceding the enemy their air superiority land-combat bonus.

---

## See also

- [Air combat](air-combat.md) — combat resolution, damage formulas, anti-air interaction
- [Aircraft designer](aircraft-designer.md) — designing planes (requires By Blood Alone)
- [Air technology](air-technology.md) — airframe and module research
- [Air doctrine](air-doctrine.md) — doctrine branches and modifiers
