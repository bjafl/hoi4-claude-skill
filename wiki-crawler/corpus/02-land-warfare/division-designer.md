---
title: Division Designer and Template Rules
category: land-warfare
tags: [division, template, division designer, army experience, support companies, battalions, armor, piercing, hardness, understrength, sizing, subject forces]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Division
  - https://hoi4.paradoxwikis.com/Division_designer
---

## Summary

The division template defines what every division built from it contains: up to 5 combat regiments of up to 5 battalions each, plus up to 5 support companies. Templates are edited in the division designer ("Recruit & Deploy" menu) by spending army experience, and editing a template instantly changes every division using it. This file covers template structure, XP costs, exactly how each division stat is derived from its battalions, understrength scaling, and sizing theory.

## Template structure

| Level | Max count | Rule |
|---|---|---|
| Combat regiments (columns) | 5 | Each regiment holds battalions of **one category only** |
| Battalions per regiment | 5 | Starts at 4; raised to 5 by land doctrine |
| Total combat battalions | 25 | 5 × 5 |
| Support companies | 5 | **Only one of each type** per division |

```
            Regiment  Regiment  Regiment  Regiment  Regiment
 Company    Battalion Battalion Battalion Battalion Battalion
 Company    Battalion Battalion Battalion Battalion Battalion
 Company    Battalion Battalion Battalion Battalion Battalion
 Company    Battalion Battalion Battalion Battalion Battalion
 Company    Battalion Battalion Battalion Battalion Battalion
```

> ⚠️ The `Division` page states 5 battalions per regiment flatly; the `Division designer` page states regiments start at 4 slots and are raised to 5 by land doctrine. Treat 4 as the pre-doctrine cap.

A division may have any number of the same battalion type, but only one of each support company type.

### Battalion categories

A regiment must be homogeneous by category. The broad categories are:

| Category | Battalions |
|---|---|
| **Infantry (foot)** | Infantry, special forces (marines, mountaineers, paratroopers), line/towed artillery, line anti-air, line anti-tank |
| **Mobile** | Cavalry, motorized infantry, mechanized infantry, motorized rocket artillery, motorized artillery / anti-air / anti-tank, armored cars |
| **Armored** | Tanks, tank destroyers, self-propelled artillery / anti-air, amphibious tanks |

Combat-battalion composition also determines how military high command bonuses and commander traits apply: their bonuses are scaled by the target battalion count relative to total combat battalions.

## Army experience costs

| Action | XP cost | Notes |
|---|---|---|
| Duplicate a template | 0 | |
| Change a template's equipment selection | 0 | |
| Change a template's name or icon | 0 | |
| Change a template's priority | 0 | |
| Add a combat regiment of an **existing** type | 5 | Includes one battalion |
| Add a combat regiment of a **new** type | 25 | 5 for the battalion + 20 new-category penalty; includes one battalion |
| Add or swap out a combat battalion | 5 | |
| Remove a battalion | 5 | Removing the last battalion in a regiment removes the regiment |
| Change a combat battalion to an existing type | 5 per battalion | Existing battalions may be moved between regiments of the same type, or to new regiments, at **no** extra cost |
| Change a combat regiment to a **new** type | 25 + 5 per battalion | Changing the topmost battalion's type converts **all** battalions in that regiment |
| Add or swap out a support company | 10 | |
| Remove a support company | 10 | |

XP is **not charged until Save is pressed**, and the Save button shows the running total — so experimenting and reading the resulting stats is free.

## Creating and managing templates

- **New templates:** use **Duplicate** on an existing one (give it a unique name), or select the name field and press **Create Empty**. Researching technologies that unlock new battalion types (e.g. mountaineers) also auto-creates a basic template for them.
- **Editing a live template:** every division using it immediately orders the extra manpower and equipment and returns any surplus to the national stockpile. Have the stockpile ready **before** editing a template on divisions about to fight, and consider upgrading units one at a time.
- **Rolling upgrades:** make the change in a duplicate template, then reassign divisions individually. Change a single division's template via the unit symbol icon in the Unit Details screen while that division's template is open.
- **Consolidation:** understrength divisions of the same template can be merged in the Army window with the **Consolidation** button, provided the selected divisions are not assigned to any army command. Very useful when short of manpower or equipment.
- Divisions cannot be split into smaller units.
- Keep an unmodified copy of the original template as a base for later designs; it saves XP.

### Name lists

Templates can have a historical name list (the "dog-tag" icon), which renames all divisions of that template. List names appear in **white**; custom division names appear in **green**. The name lists themselves are only editable through mods.

### Division equipment selection

The **Division Equipment** button (right of the parachute icon) lists all stockpiled equipment the template can use, letting you pin a template to specific weapon variants — e.g. old rifles for garrisons while newer ones are stockpiled for elites or lend-lease. Equipment already in the field is not returned unless it is upgraded or the template stops using that type.

### Equipment priority

| Priority | Effect |
|---|---|
| **Elite** | Receives equipment and reinforcements first, highest priority |
| **Default (Regular)** | Average priority; standard line divisions |
| **Reserves** | Receives equipment last, lowest priority; base guards, resistance control |

## Support companies

Support companies are "integrated support" in doctrine terminology, as opposed to "dispersed support" (artillery/AA/AT as a *line battalion* inside a combat regiment).

| Support company | Effect |
|---|---|
| **Support Artillery** | Soft attack, smaller than a line artillery battalion (fewer guns). Does not slow the division or affect paradrops |
| **Support Anti-Air** | Air attack, smaller than a line AA battalion. Does not slow the division or affect paradrops |
| **Support Anti-Tank** | Hard attack and piercing, smaller than a line AT battalion. Does not slow the division or affect paradrops |
| **Support Rocket Artillery** | Like support artillery, but also adds **breakthrough** |
| **Engineer Company** | +Entrenchment; big bonuses attacking forts and crossing rivers; large amphibious-assault bonus |
| **Recon (Cavalry / Motorized / Armored Car / Light Tank)** | +Reconnaissance (better at countering enemy combat tactics) and +speed in difficult terrain |
| **Military Police** | +Suppression for the division's line battalions, reducing partisan effects |
| **Maintenance Company** | +Equipment reliability, reducing losses from training and combat |
| **Field Hospital** | +Trickleback (returns a share of lost manpower to the pool) and reduced experience loss from casualties |
| **Logistics Company** | Reduces the whole division's supply usage |
| **Signal Company** | +Initiative — faster planning and higher chance of reinforcement from reserves in battle |

**Key properties:**

- Support companies **never count toward combat width**.
- Most do **not** affect the division's max speed — a towed AT *support* company leaves a 12 km/h division at 12 km/h, whereas a towed AT *line battalion* would drag it down to the AT gun's 4 km/h base speed. This is why fast divisions get their AT/AA/artillery as support companies.
- **Recon companies DO affect speed.** They set the maximum possible speed of the whole division, and their speed drops if they lack their essential equipment (infantry + support equipment for Cavalry recon; those plus motorized for Motorized recon; armored cars only for Armored Car recon; light tanks only for Light Tank recon). Since a recon company needs only ~10 support equipment or 24 tanks, missing a handful of items can cripple the entire division's speed.
- Most support companies of a **Paratrooper** division can paradrop with it; some heavier ones cannot.
- Support companies are unlocked through the Support Companies research tree, the Artillery tree, special projects, and country-specific national focuses.

## How division stats are computed

### Additive stats

**HP, soft attack, hard attack, air attack, defence, breakthrough, combat width, supply use, manpower, equipment need** are the **sum** over all battalions (combat width and speed come only from combat battalions).

### Averaged stats

**Organization** is the **average** of the organization of the included battalions — so adding low-org battalions (artillery, tanks, support companies) *reduces* division org even as it raises attack. Recovery rate is likewise averaged.

**Reliability** is the average of all the division's equipment.

### Armor

```
Division Armor = 0.40 × (highest Armor of any single battalion)
               + 0.60 × (average Armor over ALL battalions and support companies)
```

*Example (wiki):* 2 × Infantry (1936, armor 0) + 1 × Light Tank (1934, armor 10):
`0.40 × 10 + 0.60 × (0+0+10)/3 = 4 + 2 = 6`

*Example (wiki):* 1 armor battalion with armor 70 + 1 infantry with armor 0 → **49**
(`0.4×70 + 0.6×35`). With **2** infantry battalions instead → **41.9** (`0.4×70 + 0.6×23.3`).

### Piercing

```
Division Piercing = 0.40 × (highest Piercing of any single battalion OR support company)
                  + 0.60 × (average Piercing over ALL battalions and support companies)
```

Note the asymmetry: for **piercing** the 40% "highest" term can come from a support company; for **armor** the wiki states the highest term is taken over battalions.

### Hardness

```
Division Hardness = average Hardness of the LINE battalions
```

Support companies do not enter the hardness average.

*Example (wiki):* 2 × Infantry (hardness 0) + 2 × Light Tank (hardness 80):
`(80 + 80 + 0 + 0) / 4 = 160 / 4 = 40` → **40%**

The hardness bar sits just below the stats in the designer (tank icon left, helmet icon right). High hardness means fewer hits land from **soft attack** but more damage taken from **hard attack**.

Raise hardness by adding tank battalions, upgrading light→medium→heavy, or replacing "soft" battalions (infantry, cavalry) with motorized/mechanized. *Example:* the free "Armored-Division" template is only **35%** hardness (2 light tank + 2 cavalry battalions); swapping the light tanks for mediums and the cavalry for mechanized takes it to **70%**.

### Adjusters (terrain/situational modifiers)

The division's net adjuster is the **average of its combat battalions' adjusters, plus the sum of the support companies' adjusters**. Each adjuster shows three small icons for mobility, attack and defence — green is a bonus, red a penalty.

### Cost readout

The lower-right corner of the designer shows the resources and the minimum/maximum production cost of the equipment needed to fill the division.

## Understrength stats

When a division is below full strength its stats degrade — modelling how many troops are present to operate how much equipment.

**Out of combat**, the displayed "Current Fighting Strength" ratio is:

```
Strength ratio = min( manpower ratio , cost-weighted equipment ratio )
```

But the *stats* are scaled differently, per battalion/company:

1. **Equipment-derived stats** are scaled by the lower of the **manpower ratio** and the **unweighted equipment ratio for each equipment type** the battalion uses.
2. **Subunit stats** (including terrain modifiers, but **excluding organization, recovery rate and combat width**) are scaled by the **manpower ratio only**.
3. If the battalion/company uses **"essential" equipment**, all its stats are further scaled by the **cost-weighted ratio of that essential equipment**.

**What counts as essential:** all equipment of **all support companies** and of the **mechanized battalion** is essential — with the single exception that **infantry equipment is not essential to the Engineer company**.

Practical consequence: organization, recovery rate and combat width do **not** shrink when understrength, so an understrength division still occupies full width — hence the value of the Consolidation button.

## Sizing theory (20-width vs 40-width)

The damage system drives the answer:

- Soft/hard attack and defence/breakthrough are **additive** — doubling the template doubles them.
- Organization is **averaged** — it does **not** scale up.
- In combat, only **10%** of attacks are counted for damage while they are covered by the enemy's defence, but **40%** is counted once the attacks have exhausted enemy defence. An attack point past the enemy's defence is therefore **four times** as valuable as one held back.

Consequences:

| | Large divisions (40w) | Small divisions (20w) |
|---|---|---|
| Draining enemy defence | Better — concentrates the drain, removes a random element, so more attacks land in the 40% band | Worse — two small divisions drain less efficiently than one large one of the same total size |
| Resistance to damage | Not doubled: HP is additive but **org is not**, so damage lands on org twice as often | Better org-per-width survivability |
| Versatility | Fewer units — worse for encirclements and stretching lines | More units for encirclements and covering extending lines |
| Command capacity | Cheaper on general command limits | Consumes more command capacity |
| Support company economics | Fewer support companies per unit of front; non-weapon support companies (percentage bonuses) are cheaper per width | More support companies usable — many are more equipment-efficient per stat than line battalions; but percentage-bonus companies cost more to reach the same effect |

**General rule:** 20-width divisions are better at **defence**, 40-width at **attack**. A common structure is a breakthrough army of large divisions plus a larger number of standard-size divisions holding the line.

## Division unit type (icon)

The division's icon/type is set by multiplying an internal priority weight by the number of battalions of each type; the highest score defines the exemplar type. Ties are broken by the first (top-left) unit in the template. Values from `...\common\units\`:

| Unit | Priority | Types |
|---|---|---|
| Anti-Air | 301 | Infantry, Anti-Air |
| Anti-Tank | 1197 | Infantry, Anti-Tank |
| Amphibious Mechanized | 610 | Mechanized |
| Amphibious Tank | 2501 | Armor |
| Armored Car | 501 | Motorized |
| Artillery | 1198 | Infantry, Artillery |
| Cavalry | 599 | Infantry, Cavalry |
| Engineer Company | 0 | Infantry, Support |
| Field Hospital | 0 | Infantry, Support |
| Heavy SP Anti-Air | 301 | Armor, Anti-Air |
| Heavy SP Artillery | 1797 | Armor, Artillery |
| Heavy Tank | 2503 | Armor |
| Heavy Tank Destroyer | 1797 | Armor, Anti-Tank |
| Infantry | 600 | Infantry |
| Light SP Anti-Air | 301 | Armor, Anti-Air |
| Light SP Artillery | 1795 | Armor, Artillery |
| Light Tank | 2501 | Armor |
| Light Tank Destroyer | 1795 | Armor, Anti-Tank |
| Logistics Company | 0 | Infantry, Support |
| Maintenance Company | 0 | Infantry, Support |
| Marines | 601 | Infantry, Special Forces |
| Mechanized Infantry | 610 | Mechanized |
| Medium SP Anti-Air | 301 | Armor, Anti-Air |
| Medium SP Artillery | 1796 | Armor, Artillery |
| Medium Tank | 2502 | Armor |
| Medium Tank Destroyer | 1796 | Armor, Anti-Tank |
| Military Police | 0 | Infantry, Support |
| Modern SP Anti-Air | 301 | Armor, Anti-Air |
| Modern SP Artillery | 1796 | Armor, Artillery |
| Modern Tank | 2510 | Armor |
| Modern Tank Destroyer | 1796 | Armor, Anti-Tank |
| Motorized Anti-Air | 301 | Motorized, Anti-Air |
| Motorized Anti-Tank | 1197 | Motorized, Anti-Tank |
| Motorized Artillery | 1198 | Motorized, Artillery |
| Motorized Infantry | 599 | Motorized |
| Motorized Rocket Artillery | 1199 | Artillery, Motorized, Rocket |
| Mountaineers | 601 | Infantry, Special Forces |
| Paratroopers | 2 | Infantry, Special Forces |
| Recon Company | 0 | Infantry, Support |
| Rocket Artillery | 1199 | Infantry, Artillery |
| Signal Company | 0 | Infantry, Support |
| Super Heavy SP Anti-Air | 301 | Armor, Anti-Air |
| Super Heavy SP Artillery | 1798 | Armor, Artillery |
| Super Heavy Tank Destroyer | 1798 | Armor, Anti-Tank |
| Super-Heavy Tank | 2520 | Armor |
| Support Anti-Air | 0 | Infantry, Support |
| Support Anti-Tank | 0 | Infantry, Support |
| Support Artillery | 0 | Infantry, Support |
| Support Rocket Artillery | 0 | Infantry, Support |
| Truck-drawn Rocket Artillery | 1199 | Motorized, Artillery |

## Armored templates at game start

- Countries with tank equipment researched in 1936 **and** historical armoured divisions get a historic template matching their order of battle — e.g. Italy's **Divisione Celere**, the Soviet Union's **Mekhanizirovaniy Korpus**.
- Countries with tank equipment researched in 1936 but **no** historical armoured divisions (e.g. Commonwealth countries such as Canada, who receive the tech from the UK) get a generic template named **"Armored-Division"**.
- Every other country receives the free **"Armored-Division"** template the moment it researches its first tank equipment.

All of these free/starting templates are **light tank** templates. Converting them (or a duplicate) to medium or heavy tanks costs **5 XP per battalion**, available as soon as the research completes.

## Subject forces

Countries with subjects can recruit divisions using their subjects' templates.

| Subject type | Share of the division's manpower the subject must provide |
|---|---|
| Colony | **70%** |
| Puppet | **90%** |
| Integrated puppet | **100%** |

- Equipment comes entirely from the **overlord**; manpower is split between subject and overlord per the table above.
- **Dominions cannot be recruited from**, though they may still be asked to provide forces.
- Subject forces are under the overlord's complete control but **can only be deployed in their home country**, from which they may then move.
- Deploying them **increases the subject's autonomy**.
- To use: the **colonial templates** button in the upper-right of the templates panel lists available subjects and their autonomy levels. Select one to view/copy its templates; copies land in the overlord's template list and are edited with the overlord's army experience. Colonial templates show the home country's flag at the bottom-left of their icon.

## Stat-optimisation notes

**Organization & recovery.** The single most important stat. Foot infantry and all mobile infantry are good at it; tanks, artillery and support companies are poor to severely poor. Bring enough infantry into the mix to keep average org viable — though many land doctrines offset these penalties for specific elements.

**Speed.** Anything above the infantry battalion's 4 km/h requires restricting the template to mobile and armored battalions. Artillery must then come from support companies and/or motorized/SP variants.

**Suppression.** Most infantry gives 1–1.5; tanks 2.5; artillery and anti-tank 0. Cavalry and bicycle infantry give **2** and can be boosted by the Military Police support company — cavalry's best role. Cavalry costs more supply and equipment, though. Since resistance losses scale with manpower × (1 − hardness), soft units like infantry and cavalry take heavier garrison casualties than light tanks or armoured cars.

**Reliability.** The 80% default is fine for cheap equipment (infantry, support, motorized). Mechanized and tank divisions benefit a lot from raising it — via equipment-variant reliability investment and the Maintenance company.

**Soft attack.** Infantry already supplies plenty per width. One artillery battalion gives roughly the soft attack of **3 infantry battalions at half their width**. Light tanks and mechanized lean toward hard attack.

**Hard attack.** Everything, including infantry equipment, has some. Tanks shift the ratio toward hard — heavier is better. Anything with piercing also does good hard attack. AA is somewhat effective at hard attack, about **half** an AT gun's damage. Air power is an alternative.

**Air attack.** AA is the answer. Armor, hardness, defence and breakthrough appear to have no effect on it.

**Breakthrough.** Tanks are best; heavier is generally better, though **Modern tanks beat super-heavies**. Artillery contributes a decent amount; mechanized infantry is the best non-tank source.

**Defence.** Infantry is the top source. Mechanized infantry adds its own defence on top of the equipment-derived value, easily exceeding **80 per battalion**. Tanks are poor defensive battalions unless you hold an armor advantage.

**Armor.** Because 40% comes from the single highest-armor battalion, a single very-high-armor battalion is worth including. The remaining 60% average is best raised with high-tier mechanized infantry as a baseline. Exceeding the enemy's piercing unlocks the armor combat bonuses.

**Piercing.** Same 40%-highest structure — always include one battalion of something with strong piercing. AT guns give the best piercing until the **T2 heavy tank (1941)**, whose tank-destroyer variant beats contemporary AT guns. Two AT guns fit in 2 width, so line AT can still carry the average. The other 60% comes mostly from infantry equipment (rifles or mechanized) — take the passive **Infantry Anti-Tank** upgrades, which apply to both and can double those piercing values. **Caution:** mixing AT *support* companies with line AT or tank battalions can *lower* the division's average piercing and organization, because the support company's piercing is lower.

**Forts.** Heavy tanks, the Engineer company and all artillery except AA give fort-attack bonuses. Super-heavy tanks — and to a lesser degree super-heavy tank destroyers — have by far the highest. This category uniquely has no penalties, since those are already built into the fortification mechanic.

**Amphibious assault.** Amphibious tanks are best, then marines, then baseline infantry. All artillery battalions suffer penalties, as do tanks scaling with weight. The **Engineer company provides a huge bonus**.

**Rivers.** Half the amphibious penalty, but also applied to movement. Cavalry uniquely performs *worse* than baseline infantry at river crossings.

**Hills & mountains.** Mountaineers first. Among tanks, lighter ones have the lower penalty. All mobile battalions have reduced penalties. All infantry battalions suffer movement penalties at worst.

## Related files

- [land-units-and-stats.md](land-units-and-stats.md) — per-battalion and per-support-company numbers
- [land-combat.md](land-combat.md) — how attack/defence/breakthrough resolve into damage
- [historical-divisions.md](historical-divisions.md) — reference templates
- [land-warfare-overview.md](land-warfare-overview.md) — command groups and theaters
