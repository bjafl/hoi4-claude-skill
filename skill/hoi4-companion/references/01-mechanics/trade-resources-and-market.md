---
title: Trade, Resources and the International Market
category: mechanics
tags: [trade, resources, strategic-resources, trade-laws, convoys, international-market, fuel, refineries]
game_version: "1.19"
dlc: [Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Trade
  - https://hoi4.paradoxwikis.com/International_market
  - https://hoi4.paradoxwikis.com/Fuel
  - https://hoi4.paradoxwikis.com/Ideas
---

## Summary

Strategic resources are extracted from states, split between domestic production and the export market by the country's trade law, and bought by other countries with civilian factories (8 units per factory at base rates). Resources cannot be stockpiled — only fuel can. The international market (requires Arms Against Tyranny) is a separate system in which finished equipment is bought and sold for Economic Capacity Surplus. This file covers all seven strategic resources, trade laws, trade influence, convoy routing, the market, and fuel production/storage/consumption.

## Strategic resources

The game now has **seven** strategic resources — the six classic ones plus **coal**, which powers factories rather than being consumed by equipment.

| Resource | Purpose | Used by |
|---|---|---|
| Oil | Vehicle fuel | Not consumed in manufacturing; refined into **fuel** used by ships, aircraft and ground vehicles |
| Aluminium | Specialized vehicles and aircraft | Aircraft; Support Equipment |
| Rubber | Most vehicles | Aircraft; Motorized/Mechanized |
| Tungsten | Anti-tank munitions, machine tools, specialized parts | Artillery and Anti-Tank level III–IV; armored cars; medium, heavy and super-heavy tank weapons; small anti-tank and anti-air tank weapons; Squeeze-Bore Adapter; rocket aircraft; railway guns |
| Steel | Primary metal for military machinery | Infantry weapons and Support Equipment; artillery, anti-air, anti-tank; floating harbors; ships; tanks, motorized/mechanized, armored cars; trains; railway guns |
| Chromium | Advanced engines and heavy armour | Improved Heavy, Advanced Heavy, Super-Heavy and Modern tank chassis; welded armor; high-tier medium tank weapons; Anti-Tank level II–III; large ships (carrier, battleship, super-heavy battleship, battlecruiser); level IV small ships (destroyer, light cruiser, heavy cruiser, submarine); Cruiser Armor III–IV; jet aircraft; railway guns |
| Coal | Powers factories for higher output | When powered: civilian factory output 4 → 5; military factory output 3.5 → 4.5; naval dockyard output 2 → 2.5 |

**Resources cannot be stockpiled.** They flow directly into production and any excess is wasted. Only fuel refined from oil is stockpiled.

### Increasing resource output

| Source | Effect |
|---|---|
| Excavation I–V (industry technology) | +10% resource gain efficiency each, **+50%** total, on extracted resources only |
| Infrastructure | **+15% per level** to a state's extracted resources; five levels = **+75%** |
| High Capacity Electrical Grid (state building, 12000) | **+10% resources gained per level of infrastructure** |
| Supply hub or naval base in the state, connected to the capital by rail or sea | **+20%** resource extraction in that state. Most states have this at game start |
| Synthetic refinery | Produces rubber (1–5 per refinery, from rubber processing technologies) and fuel |
| Trade law | Determines what share of extraction is diverted to the export market |
| Other | Resource prospecting decisions, national focuses, conquest, peace-conference resource rights |

Bonuses apply to **extracted** resources only — not synthetic refinery output and not imports.

### Resource shortage penalty

Missing resources penalise the lowest-priority production lines: **−5% per missing unit of each resource type**, applied per factory, up to −100%; the highest applicable penalty is used for each factory, and the line displays the average. It stacks multiplicatively with other modifiers. Production efficiency growth is **not** affected by resource shortage. See [Production and equipment](production-and-equipment.md#resource-shortage-penalty) for the worked example.

## Trade laws

Trade law sets the share of domestic extraction exported to the market (unavailable domestically, whether or not anyone buys it) and gives economic bonuses. Changing trade law costs **150 political power** when prerequisites are met.

**Export Focus** is the default and the starting law for most countries. Germany, Italy, the United States, China and Japan start on Limited Exports or Free Trade; **Communist China** is the only country starting on Closed Economy.

| Modifier | Free Trade | Export Focus | Limited Exports | Closed Economy |
|---|---|---|---|---|
| Resources to market | +80% | +50% | +25% | 0% |
| Factory output | +15% | +10% | +5% | – |
| Dockyard output | +15% | +10% | +5% | – |
| Construction speed | +15% | +10% | +5% | – |
| Research speed | +10% | +5% | +1% | – |
| Civilian intel to others | +40% | +20% | +10% | – |
| Navy intel to others | +20% | +10% | +5% | – |
| Base construction line speed boost | +5% | +10% | −5% | −10% |

**Prerequisites**
- *Free Trade*: as Spain with La Résistance, must not have completed All Must Bear the Torch.
- *Export Focus*: as China, must not have the Nine Power Treaty national spirit; as Spain with La Résistance, must not have completed All Must Bear the Torch.
- *Limited Exports*: if the ruling party is Democratic — at war, and an enemy has more than 20% of your total factories. If not Democratic — have Partial Mobilization, War Economy or Total Mobilization. British Raj with Graveyard of Empires must have completed Raise Import Duties. China: no Nine Power Treaty spirit. Spain with La Résistance: not completed All Must Bear the Torch.
- *Closed Economy*: at war; **and** ruling party is Fascist or Communist, or has completed The State General Mobilization Law, or has War Economy / Total Mobilization / National Defense State. Soviet Union must not have signed the Molotov-Ribbentrop Pact. China: no Nine Power Treaty spirit.

### Special trade laws

| Modifier | Embargoed Economy (Poland) | Autarky (Germany) | Special Economic Zones (British Raj) |
|---|---|---|---|
| Resources to market | +25% | +15% | +90% |
| Factory output | – | +5% (upgraded: +20%) | – |
| Dockyard output | – | +5% (upgraded: +20%) | – |
| Construction speed | – | +5% / +10% (upgraded: +20%) | – |
| Research speed | – | +5% (upgraded: +15% to Industry) | – |
| Civilian intel to others | +40% | – | +80% |
| Navy intel to others | +40% | – | +30% |
| Base construction line speed boost | +15% | – | – |
| Consumer goods factories | +5% | – | – |
| Agency upgrade time | +15% | – | – |
| Lend lease tension limit | – | +20% | – |
| Faction trade deal opinion factor | – | +25% / +50% | – |
| Trade extra resource per factory | – | – | +1 |

> ⚠️ The wiki's special trade law table has a broken column layout (four header columns but five values in several rows), so the split of Autarky's base versus upgraded values above is a best reading; verify in-game.

- **Embargoed Economy** — Poland only. Can be removed manually only if at war, or after Integrate Gdańsk Industries or Expand the Gdynia Seaport, or if it owns neither Danzig (85) nor Gdynia (807), or owns any coastal state other than those two.
- **Autarky** — Germany only, from Autarky Efforts; upgraded by Autarky Achieved.
- **Special Economic Zones** — British Raj or its successors, from the Special Economic Zones focus. Switching away leaves it in the list with an always-false prerequisite: it is permanently lost.

## Buying resources

- A trade deal can be struck with any non-hostile country you have **at least 0 trade influence** with, have trade access to, and that has goods available for export. **The exporter does not approve or get notified.**
- The importer spends **at least 1 civilian factory**. Each civilian factory buys **up to 8 units** of a resource. Even if the exporter has fewer than 8 left, the whole factory is still spent.
- The civilian factories spent go to the **exporter** while the deal runs: they count for construction, for focus requirements that need N factories, for special-project and espionage spending, and can even be used to buy resources from third countries.
- Trade deals are **automatically voided** if the importer no longer has enough free civilian factories.
- If a resource has no buyer it is simply not extracted and stays on the market as untapped capacity.

### Resources per civilian factory by relationship

| Relationship | Resources per civilian factory |
|---|---|
| Ordinary trade partner | 8 |
| Independent subjects (Dominion, Satellite) | 10–16 |
| Closely aligned subjects (Collaboration Government, Reichskommissariat) | up to 80 |

Certain national focuses grant laws or spirits that directly modify resources bought per factory — Germany's **Increased Trade**, Belgium's **Port of Antwerp**, British Raj's **Special Economic Zones** (+1 per factory).

Overlords can additionally access their puppets' resources beyond what the puppets' trade laws would allow.

## Trade influence

When demand for an exporter's resources exceeds supply, importers' shares are decided by their relative **trade influence** with that exporter. If everyone has equal influence, shares are equal. Priority access share = a country's influence divided by the total influence competing for that resource.

Example: importer A has 120 influence and importer B has 80 → A gets priority access to up to 60%, B to 40%. Add importer C with 200 → shares become A 30%, B 20%, C 50%.

**At 0 trade influence a country can no longer import from that exporter** — usually the result of an embargo.

| Source | Trade influence |
|---|---|
| Base value, all countries | 150 |
| Overlord towards its puppet | +400 |
| Opinion of the importer in the exporting country | −100 to +100, scaling with opinion |
| Distance between capitals | −0.02 per 7.114 km |
| Existing active trade deals | +2 per month, max +50 |
| Support for the importer's ruling ideology in the exporting country | up to +50 at 100% support |
| "Anti-monopoly" factor: exporter already sells ≥50% of its available resources to this importer | −100 |
| Operatives on the Control Trade mission | +0.5/day, with a stacking 0.5× multiplier for each operative beyond the first, max +50 |

In practice trade influence rarely matters in the first few years; later it becomes a way to deny neutral countries' resources to enemies.

## Transporting traded goods

**Land trade has priority.** A land route is used if it can be traced through non-hostile states between the two capitals **and** the capital-to-capital distance is below:

```
sqrt( ln( 2 + states in country A + states in country B ) ) × 1000 × 7.114 km
```

Example: Tannu Tuva ↔ Luxembourg is 9917 km apart, over the limit of `sqrt(ln 4) × 7114 = 8376 km`, so land trade is impossible.

Otherwise a **naval route** is chosen. Candidate ports are found by expanding outward from each capital, traversing only states controlled by the exporter, importer, their overlords, or (for governments in exile) their host countries. Only the largest valid naval base in each state counts, and the search expands until at least ten port states are found or no more land-reachable states remain. Ports with no allowed naval-access path are excluded.

The chosen pair maximises:

```
F × ( max(0, T − Σ_regions P·A) + 10 × (L_S + L_D) )
```
- `T` = total provinces on the map
- `F` = 2 if at least one of the two ports is controlled by the **exporter**, else 1
- `regions` = sea zones the route passes through; `P` = provinces in that sea zone
- `A` = 1 normally, **100** if the sea region is set to *avoid*, **1000** if set to *blocked*
- `L_S`, `L_D` = source and destination naval base levels

Example: the Soviet Union (10 in-range ports from Moscow) and Japan (7 from Tokyo) give 70 candidate routes. The chosen route Northeast Siberia → Hiroshima scores `2 × (13257 − (68+52+25+17) + 10 × (10+1)) = 26410`. Setting the Black Sea and Barents Sea to blocked and the Coast of Japan to restricted would instead route Vladivostok → the port north of Kyoto, which crosses only one sea zone and is easier to defend.

The same routing rules apply to **internal resource transfers within a country**, except the source is the resource state rather than a foreign capital, and the land distance limit does not apply.

**Overseas trade consumes the importer's convoys**, which enemy submarines and surface raiders can sink. Convoy routes are visible in the resource map mode. Countries that cannot protect shipping should trade with nearby partners, or manipulate naval access levels to force convoys through defensible sea zones.

## International market (requires Arms Against Tyranny)

The international market trades **finished equipment** (the resource trade above is separate). Open it with the Market Tab (hotkey **E**), between Research and Trade.

### Economic Capacity Surplus (ECS)

ECS is the market currency. Buyers allocate civilian factories to a purchase; that output becomes ECS for the seller.

For the seller, ECS acts as **extra civilian factory output for construction**: it creates a temporary construction boost on each construction line, starting at the top of the queue, up to the country's **maximum construction line speed boost per line**. Default is **+25% construction speed**, modified by trade law's base construction line speed boost, giving typical caps of **+22.5% on Closed Economy** to **+27.5% on Export Focus**. ECS drains as construction consumes it; at 0 the boost turns off.

### Market access

- A mutual agreement letting two countries see and bid on each other's sale offers.
- Negotiated in the diplomacy menu ("Negotiate market access"); automated by default, can be set to manual in market settings.
- AI willingness is driven mainly by **opinion and ideology**. Countries at war with each other, or under an embargo, have no market access.
- **Guaranteed** between faction members, and between subjects and their overlords.
- If access becomes impossible (war declaration or embargo), **all active contracts are cancelled**.

### Buying

- Fill in a **Purchase Draft**: quantity, payment terms, delivery terms.
- Each assigned civilian factory generates ECS to pay for the order; more factories = fewer deliveries needed. **Maximum 15 civilian factories per contract.**
- Deliveries have weight and need **convoys**; faster delivery of more equipment needs more convoys.
- The seller must accept. AI acceptance uses similar criteria to market access, prefers **shorter contracts**, and factors in the buyer's trade influence.
- Once accepted, the buyer's factories start generating ECS for the seller and equipment arrives in batches **every 30 days**. Equipment can be lost if convoys are sunk.
- Active import routes are drawn on the map like resource trade and lend-lease routes. Ongoing purchases can be reviewed and cancelled from the International Market screen.

### Selling

- Only equipment currently **in stockpile** can be offered, up to the amount held. Submitting an offer removes the equipment from the stockpile; cancelling the offer returns it.
- A sell offer has three parts: the equipment, the amount, and the price tier.

| Price tier | Buyer pays |
|---|---|
| Low | 1.5× production cost in ECS (−25%) |
| Normal | **2× production cost** in ECS |
| High | 2.5× production cost in ECS (+25%) |

- All countries with market access see the offer. A submitted purchase request reserves the corresponding equipment until accepted or denied.
- Purchase requests must be reviewed manually by default; the Market Options menu can switch to automatic acceptance.
- Sell offers can be edited (amount and price) or removed at any time from the Sell Equipment page; changes do not affect purchases already in progress.

### Subsidies

Subsidies are near-free ECS granted by certain national focuses, decisions and events. Each has an ECS value.

- Usually restricted to a specific equipment type (light tanks, fighters, towed artillery...) and often to purchases from a specific country, typically a major such as the German Reich, the Soviet Union or the United States.
- Applying a subsidy to a purchase **increases the ECS paid to the seller by +100%**: each civilian factory on the order compensates the seller for two factories' worth of ECS per day. The subsidy drains as it pays out that extra ECS, then disappears.

## Fuel

### Production

| Source | Fuel per day |
|---|---|
| Base country production | 48 |
| Each unit of oil | 48 |
| Synthetic refinery | 48 baseline, up to **168** with fuel and oil refining technologies |

- Fuel refining technologies raise the yield: Fuel refining I–V give **+20% fuel gain per oil each (+100% total)** and **+10% fuel gain from refineries each (+50% total)**; Oil processing → Modern oil processing give **+50% fuel gain from refineries each (+200% total)**.
- **Economy laws below War Economy reduce fuel production from oil.** Synthetic refinery output is **not** affected by economy laws.
- Synthetic refineries also produce **1–5 rubber** each, depending on rubber processing technologies (base 1, +1 per rubber processing level).
- The Synthetic refinery building costs **14500**, max 3 per state, unlocked by **Synthetic oil experiments**.

### Storage

| Source | Fuel capacity |
|---|---|
| Base, every country | 50,000 |
| Each level of infrastructure, across all states | +1,500 |
| Each fuel silo level | +100,000 |

- Fuel silo cost: `5000 − 500 × current level`, max 3 levels, unlocked by **Fuel storage** (industry technology, 110 days, 1936). Silos are vulnerable to bombing and capture.
- Some economy laws (e.g. Civilian Economy) reduce fuel storage capacity.
- Countries **start with 25% of their fuel capacity filled**.
- On **capitulation, 50%** of the fuel stockpile is captured by enemies; on **annexation, 25%** transfers to the annexing country.

Fuel priority between army, navy and air force is set in the Fuel Prioritization section near the bottom of the Logistics window.

### Army fuel consumption

- Land units consume fuel if any combat battalion uses fuel-consuming equipment (trucks, half-tracks, tanks, self-propelled guns). Some support companies (motorized recon, Airborne light armor) also cause consumption. Fuel-using divisions are marked with an oil barrel in the unit panel.
- **Effective use per day = 12× the fuel usage shown in the division's stats.**

| Situation | Multiplier |
|---|---|
| Standing idle | 0× |
| Strategic redeployment | 0× |
| Naval transfer | 0× |
| Fighting and moving at once (e.g. attacking) | 2× |

- Each division holds an internal reserve worth **4 days of continuous use**, extendable with modules such as Fuel Drums.
- Penalties start at **25% of reserve capacity** and peak at 0%. At 0% fuel: movement **0.4× speed**, and combat stats of all fuel-consuming equipment **×0.1**. Training divisions earn **0× experience** (including army experience) while out of fuel.
- Out-of-combat units refuel at up to **2× consumption**, provided supply is available in their province. Fuel flow shrinks as the supply zone is overloaded and stops entirely at **50% overload** — a supply zone giving 20 supply to units needing 30 delivers no fuel at all.

### Aircraft fuel consumption

- All aircraft use fuel on missions, except **rocket interceptors** (not oil-based). Usage depends on airframe and engine module.
- **Effective use per plane per day = 8.4× the nominal fuel usage** shown in the wing's details. Day-only or night-only operation reduces it proportionally.

| Mission | Multiplier |
|---|---|
| Interception | 0.2× |
| Kamikaze | 0.75× |
| Port strike | 1.2× |
| Logistics strike | 1.2× |
| Training | 0.6× |

- Out of fuel: **0.25× mission efficiency**.

### Naval fuel consumption

- **Effective use per day = 2.4× the nominal fuel usage** shown in the ship's stats. Ships are the heaviest fuel users.

| Situation | Multiplier |
|---|---|
| In combat | 2× |
| Holding position (including idle naval-invasion-support and strike-force task forces) | 0× |
| In port | 0× |
| Training (actively training ship) | 0.6× |
| Training (escort accompanying but not training) | 0.15× |

- Ships refuel near naval bases at **2× consumption**, multiplied by the supplying naval base's supply status.
- Out of fuel: up to **−75% speed**, **0% range**, **−50% attack**. Submarines out of fuel: up to **−80% torpedo attack**.

See also: [Production and equipment](production-and-equipment.md), [Construction and buildings](construction-and-buildings.md), [Research and technology](research-and-technology.md).
