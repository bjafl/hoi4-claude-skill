---
title: Construction and Buildings
category: mechanics
tags: [construction, buildings, infrastructure, factories, building-slots, repair, landmarks, consumer-goods]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Construction
---

## Summary

Buildings are built with civilian factories, each contributing 4 industrial capacity per day (5 when powered by coal). Buildings are either **state** buildings (unlimited by slots), **shared** buildings (competing for a limited number of state building slots, max 25), or **province** buildings. Construction speed is multiplied by the state's infrastructure level and by construction-speed modifiers. This file lists every building with its cost, level cap, bombing vulnerability and effects, plus slot categories, consumer goods, repair and landmarks.

## Cost model

- Cost is given in **construction points** (the same unit as production cost). One civilian factory contributes **4 per day base, 5 when powered by coal**, before modifiers.
- Building time in days = `cost / (factories × 5 × infrastructure modifier × (1 + construction speed bonus))`.
- **At most 15 civilian factories** can be assigned to a single construction line.
- Control of a state's resources or buildings requires controlling provinces worth at least **50% of the state's victory points**, even if that excludes the province holding the building icon. Air bases appear but are unusable unless you also control the air base's province.

## State buildings

Built at state level, not limited by shared building slots.

| Building | Cost | Max level | Strat. bombing damage factor | Effects (local unless noted) |
|---|---|---|---|---|
| Infrastructure | 6000 | 5 | 100% | **Per level:** global fuel capacity +1500; province supply +0.3; division speed +5%; division recovery rate +10%; non-railway strategic redeployment speed +1 km/h; available resources +15% (multiplicative with other bonuses); construction speed +20% (multiplicative). **At level 5:** growth of mud −80% |
| Air base | 1250 | 10 | 50% | Bases and repairs air units. **Each level hosts 200 aircraft** (level 10 = 2000) |
| Anti-air | 2500 | 5 | 10% | Per level: building bomb vulnerability −12%; enemy air superiority in the strategic region −5% |
| Radar station | 3375 | 1–6, set by radar technologies | 50% | Detects enemy forces, especially incoming aircraft; also helps detect ships at sea and raises intel on other nations |
| Dam | 20000 (**cannot be built manually**) | 1 | 0% (immune to normal strategic bombing) | Max factories in state +15%; available resources +10%; construction speed +15%; enables the enemy Dam Busting Raid |

Radar station level cap: 1 with Radio Detection, 2 with Cavity Magnatron, 4 with Centimetric Radar, 5 with Phased Array, 6 with Monopulse Radar.

## Shared buildings

Also state-level, but they compete for a limited pool of **shared building slots**.

Many shared buildings can be strategically bombed; **a single point of damage immediately disables the effects of the building's first level**. This is devastating for expensive one-level buildings such as Stronghold Network, Nuclear reactor and Civilian nuclear reactor.

| Building | Base cost | Max level | Strat. bombing damage factor | Effects |
|---|---|---|---|---|
| Civilian factory | 10800 | 20 | 100% | Base output 4/day (5 powered). Used for construction, consumer goods, trade, the international market, and intelligence agencies/upgrades |
| Military factory | 7200 | 20 | 100% | Base output 3.5/day (4.5 powered), modified by factory output and production efficiency |
| Naval dockyard | 6400 | 20 | 100% | Produces and repairs ships. Base output 2/day (2.5 powered), modified by dockyard output |
| Stronghold Network | 20000 | 1 | 100% | Local supply +10%; state max land fort level +2; state land fort construction speed +10%; state max coastal fort level +2; state coastal fort construction speed +10%; enemy division attrition in state +10%. All effects removed the instant it takes any bombing damage |
| Synthetic refinery | 14500 | 3 | 100% | Produces 48–168 fuel and 1–5 rubber per day, depending on synthetic oil technologies |
| Fuel silo | `5000 − 500 × current level` | 3 | 100% | +100,000 fuel storage per silo level |
| Multi-charge large caliber gun | 20000 | 1 | 0% (bombing-immune) | Automatically produces Multi-Charge Large Caliber Gun Ammunition; enables the enemy Mega Gun Emplacement Strike. Mutually exclusive with Rocket site |
| Rocket site | 6400 | 3 | 100% | Stores and launches missiles; rocket site capacity +100 per level. Mutually exclusive with Multi-charge large caliber gun. Unlocked by Experimental Rockets |
| Nuclear reactor | 30000 | 1 | 100% | 1 nuclear bomb per 852 days, 1 thermonuclear bomb per 1278 days. Mutually exclusive with other reactors. All effects removed on any bombing damage |
| Heavy water nuclear reactor | 25000 | 1 | 100% | 1 nuclear bomb per 1278 days, 1 thermonuclear bomb per 2555 days. Mutually exclusive with other reactors |
| Civilian nuclear reactor | 35000 | 1 | 100% | Max factories in state +15%; local available resources +10%; local construction speed +15%; 1 nuclear bomb per 852 days, 1 thermonuclear per 1278 days. Mutually exclusive with other reactors |
| Reinforced Electrical Grid | 12000 | 1 | 100% | Reduces state factory energy consumption by **−7.50% per level of infrastructure**. Mutually exclusive with High Capacity Electrical Grid |
| High Capacity Electrical Grid | 12000 | 1 | 100% | Increases resource gain by **+10.00% per level of infrastructure**. Mutually exclusive with Reinforced Electrical Grid |

Notes: Germany can raise synthetic refinery output by 1 after Industrial Expansion, or by 2 after Establish Buna-Werke. British Raj can raise it by 1 by appointing William Rhodes Davis as political advisor.

### Deconstructing

Shared buildings can be deconstructed from the state tab: hover the building icon and press the X in its lower-right corner. **In wartime each state can deconstruct only one building per 30 days.**

### Building slots by state category

Each state's category sets its base shared-slot count. Technologies (Concentrated/Dispersed industry, +20% each level) give percentage bonuses; national focuses can add flat slots. **Total slots are capped at 25.**

| Category | Slots | Source-file name | Example state |
|---|---|---|---|
| Megalopolis Region | 12 | megalopolis | Greater London Area |
| Metropolis Region | 10 | metropolis | New England |
| Dense Urban Region | 8 | large_city | Southern Ontario |
| Urban Region | 6 | city | Svealand |
| Sparse Urban Region | 5 | large_town | Nebraska |
| Developed Rural Region | 4 | town | Sardinia |
| Rural Region | 2 | rural | Madagascar |
| Pastoral Region | 1 | pastoral | Hejaz |
| Small Island | 1 | small_island | Iwo Jima |
| Enclave | 0 | enclave | Gibraltar |
| Tiny Island | 0 | tiny_island | Midway Island |
| Wasteland | 0 | wasteland | Libyan Desert |

Once a state's infrastructure reaches level 5, the decision **"Region-wide Industrial Integration"** adds one building slot for **100 political power**. It can be taken only once per state.

## Province buildings

Built per province. They benefit whoever controls **that province**, regardless of who controls the rest of the state.

| Building | Cost | Max level | Strat. bombing damage factor | Effects |
|---|---|---|---|---|
| Naval base | `5000 + 1000 × current level` | 10 | 100% | Stations fleets; sends/receives supply and resources by convoy. Each level raises supply capacity, supply throughput and local ship repair capacity. A connected naval base gives +20% resource output in its state |
| Land fort | `500 + 500 × current level` | 3–10, by terrain and fortification engineering technologies | 100% | **−15% attack per fort level** against the attacker in land combat. Attacking from multiple directions reduces fort effects |
| Coastal fort | `500 + 500 × current level` | 3–10, by terrain and fortification engineering technologies | 100% | **−15% attack per level** against naval invasions and strait-crossing attacks |
| Railway | `170 + 130 × current level` | 5 | 100% | Carries supply from the capital to cities, ports and supply hubs; speeds up strategic redeployment |
| Supply hub | 20000 | 1 | 10% | Distributes supply from railways. A connected supply hub gives +20% resource output in its state |
| Canal Locks | 2000 (**cannot be built manually**) | 1 | 0% (bombing-immune) | Enables the enemy Lock Bombing Raid |

Cost examples: a level-1 naval base costs 5000, level 2 costs 6000, up to level 10 at 14000. Land fort level 1 costs 500, level 2 costs 1000, level 3 costs 1500. Railway level 1 costs 170, level 2 costs 300, level 5 costs 690.

### Experimental facilities (requires Götterdämmerung)

Limited to **one per state**. They consume **3 supply** while active and cannot be placed where supply is insufficient. Cost rises with each facility of the same type you control, and is **not** reduced by the infrastructure construction speed bonus.

| Facility | Cost | Max level | Bombing | Effects |
|---|---|---|---|---|
| Naval Engineering Facility | `12000 + 5000 × facilities of this type controlled` | 1 | 0% (bombing-immune) | Employs a Naval Engineering scientist; enables the enemy Facility Strike |
| Nuclear Research Facility | `15000 + 5000 × facilities of this type controlled` | 1 | 0% | Employs a Nuclear Research scientist; enables the enemy Facility Strike |
| Aerodynamics and Avionics Facility | `12000 + 5000 × facilities of this type controlled` | 1 | 0% | Employs an Aerodynamics and Avionics scientist; enables the enemy Facility Strike |
| Land Warfare Facility | `12000 + 5000 × facilities of this type controlled` | 1 | 0% | Employs a Land Warfare scientist; enables the enemy Facility Strike |

See [Special projects and scientists](special-projects-and-scientists.md).

## Strategic locations

Certain provinces/states carry a strategic location that raises a building cap.

| Name | Effect |
|---|---|
| Natural Harbor | Naval base capacity +2 |
| Defensive Chokepoint | Land fort capacity +2 |
| Defensible Coastline | Coastal fort capacity +2 |
| Favorable Approach | Air base capacity +2 (state scope) |

## Landmarks

Landmarks are real-world monuments. **Their modifiers benefit only the owner, not an occupier**, and they cannot be damaged by regular strategic bombing.

| Landmark | State (ID) | Province ID | 1936 owner | Country modifiers | DLC |
|---|---|---|---|---|---|
| Big Ben | Greater London Area (126) | 6103 | United Kingdom | Political power gain +3% | Götterdämmerung |
| Cristo Redentor | Rio de Janeiro (500) | 10980 | Second Brazilian Republic | Stability +5.00% | Götterdämmerung |
| The Colosseum | Lazio (2) | 9904 | Italy | War support +5.00% | Götterdämmerung |
| The Eiffel Tower | Ile de France (16) | 9523 | France | Stability +5.00% | Götterdämmerung |
| The Hagia Sofia | Istanbul (797) | 9833 | Turkey | Stability +5.00% | Graveyard of Empires |
| The Hofburg Palace | Niederösterreich (4) | 11666 | Austria | Stability +5.00% | Götterdämmerung |
| The Kremlin | Moscow (219) | 6380 | Soviet Union | Daily command power gain multiplier +10% | Götterdämmerung |
| The Reichstag | Brandenburg (64) | 6521 | German Reich | Stability +5.00% | Götterdämmerung |
| The Sa'dabad Complex | Tehran (266) | 10837 | Iran | Stability +5.00% | Graveyard of Empires |
| The Statue of Liberty | New York (358) | 3878 | United States | Political power gain +2%, Stability +5.00% | Götterdämmerung |
| The Taj Mahal | Rajasthan (433) | 4915 | British Raj | Stability +5.00% | Graveyard of Empires |
| Volkshalle | Brandenburg (64) | 6521 | German Reich | Stability +5.00%, War support +5.00% | Götterdämmerung |
| The Forbidden City | Beiping (608) | 9843 | Hebei-Chahar | Surrender limit +5.00% | No Compromise, No Surrender |
| The Nanjing Presidential Palace | Nanjing (1035) | 11913 | China | Political power gain +5% | No Compromise, No Surrender |
| The Imperial Palace | Kanto (282) | 1182 | Japan | Political power gain +5% | No Compromise, No Surrender |
| The National Diet Building | Kanto (282) | 1182 | Japan | Political power gain +5%, Stability +5.00% | No Compromise, No Surrender |
| The Hakkō Ichiu Monument | Minami Kyūshū (1018) | 1020 | Japan | War support +5.00%, justify war goal time −10.0% | No Compromise, No Surrender |
| The Great Wall | Hebei-Chahar (1039) 1590; East Hebei (609) 3900; Ningxia (616) 8127; Liaoning (716) 11808; Jiuquan (756) 2028 | see left | Hebei-Chahar, Japan, Ningxia Ma, Manchukuo, Gansu Ma | Entrenchment speed +15.0%, max entrenchment +10.0% | No Compromise, No Surrender |
| The Prague Castle | Bohemia (9) | 11542 | Czechoslovakia | Political power gain +2%, daily command power gain multiplier +5% | Peace for Our Time |
| The Bojnice Castle | Western Slovakia (70) | 3484 | Czechoslovakia | Stability +5.00% | Peace for Our Time |

- **Volkshalle** replaces the Reichstag via one of four focuses: The Triumphant Will, Hegemony over Europe, Restore the Holy Roman Empire, or European Confederation.
- **The National Diet Building** replaces The Imperial Palace via the Revoke the Peace Preservation Law focus.
- **The Hakkō Ichiu Monument** is added via Hakko Ichiu or Ichioku Isshin.
- **The Great Wall** appears in several map locations but the landmark entities themselves grant nothing — the bonuses come from a province modifier, so **occupiers also benefit**.

## Civilian factories and consumer goods

All civilian factories not tied up in consumer goods can build/repair, trade, spend on the international market, or fund decisions and intelligence agency investments.

Consumer goods take a **percentage of the country's total factories** — civilian factories + military factories + factories received through trade, but **not naval dockyards**. Damaged factories still count. The resulting number of civilian factories is **rounded down**.

### Consumer goods by economy law

| Economy law | Consumer goods |
|---|---|
| Undisturbed Isolation (US only, at start) | +50% |
| Civilian Economy | +35% |
| Isolation (US only, 1939 start) | +35% |
| Early Mobilization | +30% |
| Partial Mobilization | +25% |
| War Economy | +20% |
| Total Mobilization | +10% |
| Collectivized Society (Regional Defense Council of Aragón only, from All Must Bear the Torch) | +15% |

Universal reduction: **−1% per 10% of stability above 50%**, i.e. **−5% at 100% stability**.

### Country-specific consumer goods modifiers

| Value | Sources |
|---|---|
| −20% | Germany: Rebuild the Nation (365 days) |
| −15% | Communist China: Permit Opium Trade. Chinese warlords: Embrace the Opium Trade |
| −10% | Australia: Invest in Victory. China: Grain Tax. Warlords: War Taxes. Greece: Schachtplan (at start). Nationalist Spain: National Recovery (from Spanish Austerity). Turkey: İnanç Vergısı |
| −9% | Anarchist Spain: Anarchist Society (Communal Autarky) |
| −8% | Canada: War Bonds (If Day). South Africa: Cheap Labor (Outlaw Strikes) |
| −7% | Bulgaria: Government Reforms (Corporatism). Turkey: Etatism; Reappropriated Exploitive Finance (Scraping Our Debts) |
| −6% | Bulgaria: Our Duty in the Balkans (Free Balkan States, 5 guarantees). Anarchist Spain: Anarchist Society (Agrarian Collectivization) |
| −5% | Albania and Greece and Romania and Yugoslavia: Balkan Trade Union Secretariat (Bulgarian focus, same faction). Australia: Invest in Victory. Bulgaria: Tobacco Exports; Government Reforms (Collectivization of the Countryside / Agrarian Cooperative Movement); Balkan Trade Union Secretariat; Our Duty in the Balkans (4 guarantees); Foreign Industry. Warlords: Land Value Tax. Czechoslovakia: Arms Exports; Extensive Arms Exports. France: Devalue the Franc. Greece: Command Economy; Collectivized Agriculture; Metaxism; Schachtplan (Bolster the Schachtplan); Farmer-Focused Culture. Germany: Mefo Bills (at start); Prepare for the Next Blockade. Hungary: Intervention. Republican Spain: Seized Gold Reserves; Wealth Redistribution; Class War; Appropriate Church Riches; Relocate the Gold Reserves; Provide for the People. Romania: Agrarian Reform. Turkey: Privatized Infrastructure; Funkplan; Turkish Bolshevism; The Central Balkan Bank of Athens. United Kingdom: British Austerity; For the Good of the Revolution. United States: Accumulated Wealth Tax Act. Nationalist Spain: Regional Agrarian Commissions; National Recovery. Netherlands: Friesland Agricultural Impetus. New Zealand: Wairarapa Sheep Farms. South Africa: Gold Exports. Soviet Union and Yugoslavia: Yugoslavian Economic Aid. Yugoslavia: Foreign Capital |
| −4% | Bulgaria: Our Duty in the Balkans (3 guarantees) |
| −3% | Bulgaria: Our Duty in the Balkans (2 guarantees). Greece / Romania / Turkey / Yugoslavia: The Balkan Central Bank. Anarchist Spain: Anarchist Society (Shared Burdens). South Africa: Cheap Labor (Work for All Poor) |
| −2% | British Raj: Princely State Donations. Bulgaria: National Industry (Utmost Optimization); Our Duty in the Balkans (1 guarantee); Government Reforms (Industrial Autarky). Canada: War Bonds. New Zealand: First Labor Government. Portugal: Hydroelectric Power; Estado Novo (Strengthen the Regime) |
| −1% | Bulgaria: Our Duty in the Balkans. Portugal: Estado Novo; National Gold Reserves |
| +2% | New Zealand: Waitangi Tribunal |
| +3% | Romania: Royal Household Accounts (event) |
| +4% | Bulgaria: National Industry (Invigorate National Industry) |
| +5% | Australia: Great Depression. France: Matignon Agreements. British Raj: Famine (event). China: Low Inflation (at start). Greece: Foreign Monopolies (Encourage Tourism / Mobilize Our Economy); Small Debt Repayment. Japan: Zaibatsus (at start) |
| +8% | Bulgaria: National Industry (Increase Industry Investments) |
| +10% | Canada: Great Depression (Canada Wheat Board). China: Moderate Inflation. Greece: Foreign Monopolies (Expand Our Tobacco Industry / Increase Our Mining Operations). Spain: Recovering From Civil War |
| +15% | Australia: Great Depression. China: Heavy Inflation. Greece: Debt to the I.F.C (at start); Foreign Monopolies (Exporting More Luxury Commodities / Greek Autarky); Large Debt Repayment. Romania: King Carol Emptied Accounts |
| +17.5% | United States: Slow Economic Growth |
| +20% | Australia: Great Depression (at start). China: Hyper Inflation. Greece: Foreign Monopolies (at start). Romania: Supplementary Budget (event) |
| +25% | Canada: Great Depression (at start). China: Economic Collapse. Romania: Embezzlement Scandal (event). United States: Slow Recovery |
| +30% | United States: The Great Depression (at start) |

South Africa can reach −3% consumer goods on Total Mobilization with its spirits, but gains no extra factories from doing so.

**Example:** Early Mobilization (30%), no other modifiers, a country with 50 military factories, 50 civilian factories and 20 naval dockyards. Total counted factories = 100, so 30 civilian factories go to consumer goods, leaving 15 free.

### Consumer Goods Factories Factor (CGFF)

CGFF is a **multiplicative** modifier on the law's consumer goods figure, available to some countries (notably Germany):

```
Total consumer goods = consumer goods from economy law × (1 + CGFF)
```

Early Mobilization (30%) with +10% CGFF gives 30% × 1.1 = **33%**, not 40%. With −10% CGFF: 30% × 0.9 = **27%**, not 20%. Multiple CGFF sources stack **multiplicatively**, so several small positive sources hurt more than one large one, while one large negative source helps more than several small ones.

## Construction speed modifiers

Base civilian factory output in construction is **4 per day** (5 powered).

| Value | Universal source | Country-specific examples |
|---|---|---|
| +15% | Free Trade trade law | – |
| +10% | Export Focus trade law; Construction I; Construction II; Construction III; Construction IV; Construction V | New Zealand: The Worker's Party; In the Darkness. Soviet Union: Worker's Culture |
| +5% | Limited Exports trade law | – |
| −10% | Service by Requirement conscription law | – |
| −30% | All Adults Serve conscription law | – |
| −40% | Scraping the Barrel conscription law | – |

Building-specific modifiers come mainly from political advisors: **Captain of Industry, Fortification Engineer, Quartermaster General, War Industrialist**, plus assorted national spirits from focuses and events.

Construction speed modifiers overall range from **−70% to +65%**.

## Infrastructure and construction speed

State construction speed is multiplied by:

```
1 + ( state infrastructure × INFRA_MAX_CONSTRUCTION_COST_EFFECT / max infrastructure level )
```

`INFRA_MAX_CONSTRUCTION_COST_EFFECT` defaults to 1 (`common/defines/00_defines.lua`) and max infrastructure level defaults to 5 (`common/buildings/00_buildings.txt`), so each level is **+20%**:

| Infrastructure level | Construction speed multiplier |
|---|---|
| 0 | 1.0× |
| 1 | 1.2× |
| 2 | 1.4× |
| 3 | 1.6× |
| 4 | 1.8× |
| 5 | 2.0× |

This multiplier is applied **after** technology, advisor and national spirit bonuses, which makes one level of infrastructure a stronger bonus than, for example, a War Industrialist. Filling all slots in one state at a time — starting with high-infrastructure states — is the most efficient build order, at the cost of concentrating industry where bombing hurts most.

### Infrastructure and organization recovery

| Infrastructure level | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| Organization recovery rate | +25% | +15% | +5% | −5% | −15% |

### When infrastructure pays for itself

Minimum total construction value that must be built in a state to justify raising infrastructure to a given level:

| Target infrastructure level | Minimum construction cost to justify | In military factories | In civilian factories |
|---|---|---|---|
| 1 | 36000 | 5 | 3.333 |
| 2 | 42000 | 5.833 | 3.889 |
| 3 | 48000 | 6.667 | 4.444 |
| 4 | 54000 | 7.5 | 5 |
| 5 | 60000 | 8.333 | 5.556 |

Modified by construction speed: `modified cost = required cost × construction speed modifier`.

| Construction speed | Modifier |
|---|---|
| −30% | 0.7 |
| −20% | 0.8 |
| −10% | 0.9 |
| 0% | 1 |
| +10% | 1.1 |
| +20% | 1.2 |
| +30% | 1.3 |

Higher construction speed (always good in itself) makes the infrastructure boost relatively less worthwhile.

### Civilian factory payback

```
Payback time (days) = 10800 / ( infrastructure modifier × 5 × (1 + construction speed bonus) × (1 − consumer goods % / 100) )
```

Payback table for a state with 4 infrastructure (1.8× modifier):

| Economy law | Min construction speed (−70%) | 0% | Max (+65%) |
|---|---|---|---|
| Undisturbed Isolation | 4444 | 1333 | 1159 |
| Isolation | 3077 | 1231 | 985 |
| Civilian Economy | 2286 | 1143 | 847 |
| Early Mobilization | 1524 | 1067 | 688 |
| Partial Mobilization | 1250 | 1000 | 606 |
| War Economy | 1232 | 942 | 571 |
| Total Mobilization | 1111 | 889 | 539 |

Minimum construction speed ranges from −70% (Undisturbed Isolation) to −20% (Partial Mobilization); maximum from +15% (Undisturbed Isolation) to +65% (Partial Mobilization). Values rounded up to whole days.

Optimal moment to stop building civilian factories and start building military factories, to maximise equipment by a target date:

```
Switch time = target time − (2 / ln 2) × payback time
```

For a payback time of 800 days and a target of January 1944, switch in September 1937.

Build time for a new civilian factory:

```
Build time = 10800 / ( #factories × 5 × infrastructure modifier × (1 + speed bonus/100) )
```

## Factory conversion

| Conversion | Base cost |
|---|---|
| Civilian factory → military factory | 4000 |
| Military factory → civilian factory | 9000 |

Base costs are modified by economy laws and can be further modified by national spirits and political advisors. Convert by clicking the state and hovering the factory, or via the convert button in the construction tab; conversions then queue like any other project.

## Damage and repair

- **Each building level has 100 HP.**
- Damage sources: port strikes (naval bases), land combat (infrastructure, forts), resistance (factories), strategic bombing, scripted events (e.g. the Soviet decision to move factories to the Urals). Nuclear bombs can destroy multiple or all levels at once.
- Damage from land combat and strategic bombing is scaled by the building's **damage factor** (air base and radar 0.5, anti-air 0.1, everything else 1) **and by the squared ratio of undamaged levels to maximum level**.
  - A level-3 anti-air building (max 5) with one level partly damaged takes only `(2/5)² × 0.1 = 1.6%` of incoming bombing damage.
  - A single military factory in a state takes `(1/20)² = 0.25%`; 15 military factories take `(15/20)² = 56.25%`. High-level factories and infrastructure take damage far faster.
- **Anti-air** gives damage resistance against bomber attacks (port strikes and strategic bombing), scaling with state anti-air level and anti-air technologies. **Dispersed Industry** gives an alternative resistance for factories only; the two do **not** stack — the larger of the two is used for factories.
- Damaged buildings appear in the construction list. Factories assigned to a repair line get **+200% speed** plus any factory repair speed bonuses (construction technologies, the Construction Repair continuous focus, infrastructure levels). Even with **no** factories assigned, the repair line runs at speed 1.
- Daily repair progress = `median(1%, speed / building cost × 100%, 100%)`, rounded to the nearest whole percent. With no factories assigned, repairs still advance 1%/day. Assigning only a few factories to an expensive building may also yield only 1%/day, wasting their output.

See also: [Production and equipment](production-and-equipment.md), [Trade, resources and the international market](trade-resources-and-market.md), [Research and technology](research-and-technology.md).
