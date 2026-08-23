---
title: Laws, Advisors and National Spirits
category: mechanics
tags: [ideas, laws, conscription, trade law, economy law, advisors, high command, theorist, design companies, national spirit]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Ideas
  - https://hoi4.paradoxwikis.com/National_spirit
---

## Summary

Ideas are everything a country buys with political power: the three law slots (conscription, trade, economy), political advisors, design companies/industrial concerns, and military staff (theorist, chiefs, high command). A country holds exactly one law of each type; laws cost **150 PP** to switch (conscription costs 150 PP *per level of difference*) and are gated by war support, ruling ideology and war status. National spirits are non-purchasable ideas granted by focuses and events.

## Idea categories

| Category | What it affects | Slots |
|---|---|---|
| Conscription law | Recruitable manpower, factory/dockyard output, construction speed, training time | 1 |
| Trade law | Resources sent to market, factory/dockyard output, construction speed, research speed | 1 |
| Economy law | Consumer goods, factory construction/conversion, manpower, fuel | 1 |
| Political advisors | Broad bonuses; used to shift party popularity | up to 3 |
| Research/production companies | Research time reductions and equipment bonuses | 1 tank + 1 naval + 1 air + 1 materiel + 1 industrial concern |
| Military staff | Army/navy/air bonuses | 1 theorist, 1 chief of army, 1 chief of navy, 1 chief of air, 3 high command |

## Conscription laws

Cost: **150 PP per level of difference** between old and new law. With No Step Back, fascist countries get a sizable discount through the **State Serves the Military** officer corps spirit. Raising up to **Extensive Conscription** is essentially free of economic penalties; **Service by Requirement** and above start hurting the economy.

**Volunteer Only** is the default and most countries' starting law; Germany, France, Italy, the United States and Japan start elsewhere (Limited Conscription or Disarmed Nation).

| Modifier | Disarmed Nation | Volunteer Only | Limited Conscription | Extensive Conscription | Service by Requirement | All Adults Serve | Scraping the Barrel |
|---|---|---|---|---|---|---|---|
| Recruitable Population | 1.0% | 1.5% | 2.5% | 5.0% | 10.0% | 20.0% | 25.0% |
| Factory Output | – | – | – | – | −10% | −30% | −40% |
| Dockyard Output | – | – | – | – | −10% | −30% | −40% |
| Construction Speed | – | – | – | – | −10% | −30% | −40% |
| Training Time | – | – | – | +10% | +20% | +30% | +50% |

### Conscription law requirements

| Law | Requirements |
|---|---|
| Disarmed Nation | – (cannot be selected voluntarily; imposed) |
| Volunteer Only | Economy law is not Undisturbed Isolation or Isolation. Hungary: must not have the Treaty of Trianon spirit |
| Limited Conscription | Economy law is not Undisturbed Isolation or Isolation; more than 10% war support |
| Extensive Conscription | More than 20% war support, **and** one of: ruling party is Fascist; ruling party is Communist; or (at war **and** an enemy has an estimated army strength ratio of 50%+ compared to this country) |
| Service by Requirement | One of: ruling party is Fascist or Communist; or (at war **and** enemy army strength ratio 60%+). Plus one of: more than 60% war support, or more than 0% surrender progress |
| All Adults Serve | At war; enemy army strength ratio 70%+; plus one of: more than 70% war support, or more than 0% surrender progress |
| Scraping the Barrel | At war; enemy army strength ratio 100%+; plus one of: more than 85% war support, or more than 25% surrender progress |

Country-specific extra gates that apply from Limited Conscription upward: **Australia** must have completed *Citizen Military Forces* (and *Fight Work or Perish* from Extensive upward); **British Raj** must be fully independent; **Bulgaria** must not have the *Army Restrictions* spirit; **Dominion of Canada** needs *Commit to the War* (plus *If Day* for Extensive, and *Compromise With Quebec* or *Forced Quebec Conscription* from Service by Requirement upward); **Hungary** must not have *Treaty of Trianon*; **Spain** must not have completed *All Must Bear the Torch*.

### Special conscription laws

The Chitet has two states: the first column applies at war, the second at peace.

| Modifier | The Chitet (at war) | The Chitet (at peace) | Swiss Citizen Militias | Expanded Swiss Citizen Militias |
|---|---|---|---|---|
| Recruitable Population | 4.50% | 0.50% | 10.0% | 20.0% |
| Factory Output | −5% | +5% | – | – |
| Dockyard Output | −5% | +5% | – | – |
| Construction Speed | −5% | +5% | – | – |
| AI Modifier: Desired Divisions Factor | – | – | 100% | 200% |

- **The Chitet** — Ethiopia only (requires By Blood Alone). Penalties and manpower reserves increase automatically at war; can raise the National Levy at war; at peace it switches to the secondary (peace) effects. Removed only by completing *Expand the Mehal Sefari*.
- **Swiss Citizen Militias / Expanded Swiss Citizen Militias** — Switzerland only (requires By Blood Alone). Cannot train regular forces outside the militias and cannot edit existing templates outside the Military Readiness decisions; militia organization is initially capped. After the focus *Armed Neutrality* the militias can be expanded, improved and deployed via the *Deploy Citizen Militias* decision — deployment stacks economic penalties over time that reset on recall. Removed only by completing one of *Professionalize Militias*, *Join the Alliance*, *Join France*, *Jump into Action*.

## Trade laws

Cost **150 PP**. The trade law sets how much of the resources in controlled provinces is exported to the market — only the remainder is usable for own production. Freer trade gives more factory output, construction speed and research speed but leaks more intel.

**Export Focus** is the default; Germany, Italy, the United States, China and Japan start on Limited Exports or Free Trade. **Communist China** is the only country starting on Closed Economy.

| Modifier | Free Trade | Export Focus | Limited Exports | Closed Economy |
|---|---|---|---|---|
| Resources to Market | +80% | +50% | +25% | 0% |
| Factory output | +15% | +10% | +5% | – |
| Dockyard output | +15% | +10% | +5% | – |
| Construction Speed | +15% | +10% | +5% | – |
| Research Speed | +10% | +5% | +1% | – |
| Civilian Intel to Others | +40% | +20% | +10% | – |
| Navy Intel to Others | +20% | +10% | +5% | – |
| Base construction line speed boost | +5% | +10% | −5% | −10% |

### Trade law requirements

| Law | Requirements |
|---|---|
| Free Trade | – (Spain with La Résistance: must not have completed *All Must Bear the Torch*) |
| Export Focus | – (China: must not have the *Nine Power Treaty* spirit; Spain as above) |
| Limited Exports | If ruling party is Democratic: at war **and** an enemy holds more than 20% of this country's factory count. If not Democratic: economy law is Partial Mobilization, War Economy or Total Mobilization. British Raj with Graveyard of Empires: *Raise Import Duties* completed |
| Closed Economy | At war, **and** either ruling party is Fascist/Communist, or *The State General Mobilization Law* is completed; economy law is War Economy, Total Mobilization or National Defense State. Soviet Union: must not have signed the Molotov–Ribbentrop Pact |

### Special trade laws

Autarky has two levels: the base version from *Autarky Efforts* and the upgraded version from *Autarky Achieved*.

| Modifier | Embargoed Economy | Autarky | Autarky (Achieved) | Special Economic Zones |
|---|---|---|---|---|
| Resources to Market | +25% | +15% | +15% | +90% |
| Factory output | – | – | +5% | +20% |
| Dockyard output | – | – | +5% | +20% |
| Construction Speed | – | +5% | +10% | +20% |
| Research Speed | – | +5% | +5% | +15% to Industry |
| Civilian Intel to Others | +40% | – | – | +80% |
| Navy Intel to Others | +40% | – | – | +30% |
| Base construction line speed boost | +15% | – | – | – |
| Consumer Goods Factories | +5% | – | – | – |
| Agency Upgrade Time | +15% | – | – | – |
| Lend-lease tension limit | – | +20% | +20% | – |
| Faction trade deal opinion factor | – | +25% | +50% | – |
| Trade extra resource per factory | – | – | – | +1 |

- **Embargoed Economy** — Poland only. Removable manually only if at war, or *Integrate Gdańsk Industries* or *Expand the Gdynia Seaport* is completed, or Poland owns neither Danzig (85) nor Gdynia (807), or it owns another coastal state.
- **Autarky** — Germany only, from *Autarky Efforts*, upgraded by *Autarky Achieved*.
- **Special Economic Zones** — British Raj or successors, from the *Special Economic Zones* focus. Switching away leaves the law in the list with an always-false trigger: it is permanently lost.

## Economy laws

Cost **150 PP**. The economy law sets the share of civilian factories tied up in consumer goods, factory construction/conversion costs and fuel efficiency. Higher tiers are strictly more efficient for construction. Total Mobilization's −3% recruitable population can be offset with the **Women in the Workforce** decision (100 PP; must be retaken if the country leaves the war).

**Civilian Economy** is the default; Germany, Italy, Japan and Communist China start on Partial Mobilization.

| Modifier | Civilian Economy | Early Mobilization | Partial Mobilization | War Economy | Total Mobilization |
|---|---|---|---|---|---|
| Consumer Goods Factories | +35% | +30% | +25% | +20% | +15% |
| Civilian Factory Construction Speed | −30% | −10% | – | – | – |
| Military Factory Construction Speed | −30% | −10% | +10% | +20% | +30% |
| Civilian Factory Conversion Cost | +30% | – | −10% | −20% | −30% |
| Military Factory Conversion Cost | +30% | – | −10% | −20% | −30% |
| Recruitable Population | – | – | – | – | −3% |
| Fuel Gain Per Oil | −40% | −25% | −10% | – | – |
| Fuel Capacity | −25% | – | – | – | – |
| Factory Energy Consumption | −30% | −15% | – | +25% | +50% |

**Quick answer — War Economy costs 150 PP and gives:** consumer goods +20% (i.e. 20% of civilian factories on consumer goods), military factory construction speed +20%, civilian and military factory conversion cost −20%, factory energy consumption +25%, no fuel penalty.

### Economy law requirements

| Law | Requirements |
|---|---|
| Civilian Economy | – |
| Early Mobilization | More than 15% war support |
| Partial Mobilization | More than 25% war support |
| War Economy | More than 50% war support, **and** one of: ruling party is Fascist or Communist; or (at war **and** an enemy holds more than 40% of this country's factory count) |
| Total Mobilization | At war; more than 80% war support; an enemy holds more than 50% of this country's factory count |

Country-specific gates: **Hungary** must not have *Treaty of Trianon* (Partial Mobilization also allowed after *Secret Rearmament*). The **United States**, once *Limited Intervention* is done and not in a defensive war, needs higher war support (30% / 50% / 75% / 90% for Early / Partial / War / Total) *and* congressional support of at least 58 Senators and 261 Representatives. **Turkey** with Battle for the Bosporus must not have *Devaluation of the Turkish Lira*, *Worsening Recession* or *Imminent Depression* active.

### Special economy laws

New Economic Policy has two levels: from *Back to the NEP*, then modified by *A Sustainable Economy*.

| Modifier | Undisturbed Isolation | Isolation | Collectivized Society | New Economic Policy | NEP (Sustainable Economy) | Totaler Krieg | Capital Investment Model | National Defense State | War Communism |
|---|---|---|---|---|---|---|---|---|---|
| Consumer Goods Factories | +50% | +40% | +15% | +15% | +10% | +15.0% | +15.0% | +15.0% | +15.0% |
| Civilian Factory Construction Speed | −50% | −40% | +15% | – | – | – | +15% | – | −10% |
| Military Factory Construction Speed | −50% | −40% | +30% | – | – | +20% | −15% | +30% | +20% |
| Dockyard Construction Speed | −50% | −40% | – | – | – | +20% | – | – | +20% |
| Infrastructure Construction Speed | – | – | – | – | – | – | +15% | – | – |
| Construction Speed | – | – | – | −15% | −20% | – | – | – | – |
| Civilian Factory Conversion Cost | +50% | +40% | −30% | – | – | −30% | −40% | −30% | – |
| Military Factory Conversion Cost | +50% | +40% | −30% | – | – | −30% | – | −30% | – |
| Factory Output | – | – | +70% | – | – | +5% | – | – | +5% |
| Dockyard Output | – | – | +70% | – | – | +5% | – | – | +5% |
| Max Factories In A State | – | – | +10% | – | +10% | – | – | – | +10% |
| Production Efficiency Retention | – | – | +10% | – | – | – | – | – | – |
| Production Efficiency Cap | – | – | −20% | – | – | – | – | – | – |
| Production Efficiency Growth | – | – | −20% | – | – | – | – | – | – |
| Recruitable Population | – | – | – | – | – | −2% | – | – | +2% |
| Fuel Gain Per Oil | −60% | −50% | – | – | – | – | – | – | – |
| Fuel Capacity | −45% | −35% | – | – | – | – | – | – | – |
| Agency Upgrade Time | +100% | +80% | – | – | – | – | – | – | – |
| Resistance Target | – | – | −20% | – | – | – | – | – | – |
| Research Speed | – | – | −10% | – | – | – | – | – | – |
| Trade Deal Opinion Factor | – | – | – | – | – | – | +75% | – | – |
| Stability | – | – | – | – | – | – | −15% | – | −10% |
| War support | – | – | – | – | – | – | – | +10% | – |
| Political Power | – | – | – | – | – | – | −10% | – | – |
| Factory Energy Consumption | −30% | −30% | +45% | +25% | +35% | +50% | +35% | +45% | +30% |

| Law | Who gets it / how it is removed |
|---|---|
| Undisturbed Isolation | United States at the 1936 start. Removable only with at least 50% war support, or at war, or after *Limited Intervention* |
| Isolation | Iceland at the 1936 start; the United States at the 1939 start or when the "Election: Public Demands Rearmament" event fires while on Undisturbed Isolation. Removable only with at least 75% war support, at war, or after *Limited Intervention*; also removed by *International Trade*, *United We Stand* or *International Relations* |
| Collectivized Society | Anarchist Spain, after *All Must Bear the Torch*. Cannot be removed |
| New Economic Policy | Soviet Union, after *Back to the NEP*; modified by *A Sustainable Economy*. Removable only with more than 75% surrender progress or if the ruling party is no longer Communist |
| Totaler Krieg | Germany, after the *Totaler Krieg* focus. Requires being at war with a major, more than 80% war support, and an enemy holding more than 50% more factories than Germany |
| Capital Investment Model | British Raj or successors, after *New Economic Policy*. Switching away removes it permanently |
| National Defense State | Japan, after *Prepare for the Final War* or *National Defense State*; replaces Total Mobilization. Re-taking requires being at war with a major or more than 75% war support, plus a country holding more than 50% of Japan's factory count |
| War Communism | Communist Japan, after the *War Communism* focus |

### US isolation laws and world tension

The starting US economy laws raise the world tension thresholds for diplomatic actions:

| Law | Join faction | Send volunteers | Lend-Lease | Guarantee | Generate war goal |
|---|---|---|---|---|---|
| Undisturbed Isolation | 20% | 20% | 50% | 75% | 100% |
| Isolation | 20% | 20% | 10% | 50% | 100% |

## Political advisors

Up to **three** political advisors. Every advisor carries at least one trait; most use one of the common traits below (the wiki does not list per-advisor political power costs on the Ideas page; **Inferred:** hiring one is an idea purchase, usually 150 PP, scaled by the "Political Advisor Cost" modifiers that many national spirits and leader traits carry). Advisors with a daily-support trait are the standard route to a coup or civil war — see [Politics, ideology and government](politics-ideology-government.md).

| Trait | Effects |
|---|---|
| Armaments Organizer | Civilian to military factory conversion cost: −20.00%; supply hub construction speed: +10.00% |
| Backroom Backstabber | Subversive activities cost: −25%; ideology drift defense: +25.0% |
| Captain of Industry | Civilian factory construction speed: +10.00%; infrastructure construction speed: +10.00%; railway construction speed: +10.00%; synthetic refinery construction speed: +10.00% |
| Communist Revolutionary | Daily communism support: +0.10 |
| Compassionate Gentleman | Improve relations opinion: +15%; compliance growth: +2%; resistance target: −5% |
| Democratic Reformer | Daily democracy support: +0.10 |
| Economist | Production efficiency cap: +5.00% |
| Editor | Political power gain: +5%; stability: +5.00% |
| Fascist Demagogue | Daily fascism support: +0.10 |
| Financial Expert | Consumer goods factories: −5% |
| Fortification Engineer | Land fort construction speed: +20%; coastal fort construction speed: +20%; anti-air construction speed: +20% |
| Humble Appeaser | War support: −5.00%; stability: +10.00% |
| Ideological Crusader | Same ideology monthly opinion: +100%; party popularity stability modifier: +10% |
| Illusive Gentleman | Operative slots: +1; agency upgrade time: −15% |
| Liberal Journalist | Daily democracy support: +0.05; political power gain: +5% |
| Marxist Fundamentalist | Daily communism support: +0.10; stability: +15.00% |
| National Integralist | Political power gain: +15%; weekly stability: +0.1% |
| Patriotic Socialist | Daily communism support: +0.05; war support: +10.00% |
| Popular Figurehead | Stability: +15.00% |
| Prince of Terror | Damage to garrisons: −25.00%; foreign subversive activities efficiency: −30%; non-core manpower: +2% |
| Propaganda Master | War support: +10.00% |
| Quartermaster General | Air base, naval base, rocket site, radar station and nuclear reactor construction speed: +15% each |
| Revolutionary Poet | Daily communism support: +0.05; political power gain: +15% |
| Silent Workhorse | Political power gain: +15% |
| Smooth-Talking Charmer | Improve relations maintain cost: −50%; trade deal opinion factor: +10.00% |
| Staunch Monarchist | Daily support for Non-Aligned: +0.10 |
| Technocrat | Civilian factory construction speed: +5.00%; research speed: +5.00% |
| Traditionalist Theorist | Daily support for Non-Aligned: +0.05; political power gain: +15% |
| War Industrialist | Military factory construction speed: +10%; naval dockyard construction speed: +10%; fuel silo construction speed: +10% |

## Design companies

A country may hire **one each of tank, naval, air and materiel designer, plus one industrial concern**. With **Arms Against Tyranny** the four designer slots are replaced by military industrial organizations (MIOs).

**Timing rule:** tank, naval and air designer bonuses apply only to equipment *designed while that company is hired*. Hiring a designer one day before designing a tank permanently stamps its bonuses on that design; replacing a designer applies only the new company's bonuses to later designs; a company never retroactively improves equipment researched before it was hired. Variants inherit the bonuses. (This is unlike national spirits that modify production cost, which apply to everything produced while active.) Some cases key off the day the chassis-unlocking research completed.

### Tank designers

Companies also typically carry +15% or +10% armor research speed.

| Trait | Effects |
|---|---|
| Heavy Tank Designer | Armor technology: armor +5%, hard attack +5% |
| Infantry Tank Designer | Armor technology: soft attack +5%, armor +5% |
| Medium Tank Designer | Armor technology: reliability +5%, soft attack +5% |
| Mobile Tank Designer | Armor technology: maximum speed +5%, reliability +10% |
| Tank Designer | Armor technology: reliability +5% |

### Ship designers

Companies also typically carry +15% or +10% naval research speed.

| Trait | Effects |
|---|---|
| Atlantic Fleet Designer | Carrier: armor +50%, HP +10%. Capital ships: armor +10%, heavy attack +10% |
| Battlefleet Designer | Capital ships: armor +15%, heavy attack +15%. Screens: torpedo attack +25%, sub detection −25% |
| Coastal Defense Fleet Designer | Carrier: production cost −25.00%, max range −50%. Capital ships: production cost −25.00%, armor −20%, heavy attack −20%, max range −50%. Screens: production cost −25.00%, max range −50%. Submarine: production cost −25.00%, max range −50% |
| Escort Fleet Designer | Screens: max range +35%, sub detection +10%, max speed +10%, production cost +10.00% |
| Mediterranean Fleet Designer | Capital ships: max range −25%, max speed +10%. Screens: max range −25%, max speed +10% |
| Pacific Fleet Designer | Carrier: deck size +1, armor −15%, max range +25%. Capital ships, screens and submarines: max range +25% |
| Raiding Fleet Designer | Carrier: surface visibility −10.00%, max speed +10%. Capital ships: surface visibility −10.00%, max speed +10%, heavy attack −10%. Screens: surface visibility −10.00%, max speed +10%. Submarine: sub visibility −10.00%, surface visibility −10.00%, max speed +10% |
| Ship Designer | None |

### Aircraft designers

Companies also typically carry +15% or +10% air research speed.

| Trait | Effects |
|---|---|
| Aircraft Designer | None |
| CAS Designer | Close air support and carrier CAS: ground attack +10%, reliability +10% |
| Heavy Aircraft Designer | Strategic bomber: strategic bombing +10% |
| Light Aircraft Designer | Fighter and carrier fighter: agility +10%, max speed +10% |
| Medium Aircraft Designer | Heavy fighter, tactical bomber and scout plane: reliability +20% |
| Naval Aircraft Designer | Naval bomber and carrier naval bomber: range +10%, naval attack +10%. Carrier fighter: range +10%, agility +10%. Carrier CAS: range +10%, naval attack +10% |

### Materiel designers

Artillery Designer, Infantry Equipment Designer, Motorized Equipment Designer and Support Equipment Designer have no trait effects beyond their typical +15% or +10% research speed.

### Industrial concerns

| Trait | Effects |
|---|---|
| Electronics Concern | Electronics research speed: +15% |
| Industrial Concern | Industrial research speed: +15% |
| Railway Company | Railway construction speed: +15.00%; supply hub construction speed: +15.00%; train production cost: −25.00%; train armor: +10% |
| Refining Concern | Industrial research speed: +10%; synthetic resources research speed: +15% |

## Military staff

### Theorist (1 slot)

| Trait | Effects |
|---|---|
| Air Warfare Theorist | Air doctrine cost: −10% |
| Assault Aviation | Operational Integrity doctrine cost: −15% |
| Blitzkrieg Theorist | Armor technology max speed: +10%; Mobile Warfare doctrine cost: −15% |
| Close Air Support Proponent | Battlefield Support doctrine cost: −15% |
| Dive Bomber | Close air support ground attack: +10%; air doctrine cost: −10% |
| Grand Battleplan Expert | Grand Battle Plan doctrine cost: −15% |
| Grand Fleet Proponent | Fleet in Being doctrine cost: −15% |
| Mass Assault Expert | Mass Assault doctrine cost: −15% |
| Military Theorist | Land doctrine cost: −10% |
| Mobile Warfare Expert | Mobile Warfare doctrine cost: −15% |
| Naval Aviation Pioneer | Base Strike doctrine cost: −15% |
| Naval Theorist | Naval doctrine cost: −10% |
| Nuclear Scientist | Nuclear research speed: +15% |
| Rocket Scientist | Rocket research speed: +15% |
| Submarine Specialist | Trade Interdiction cost: −15% |
| Superior Firepower Expert | Superior Firepower cost: −15% |
| Victory Through Airpower | Strategic Destruction cost: −15% |

### Military chiefs (1 army + 1 navy + 1 air)

Chiefs also grant daily experience in their branch: **Specialist +0.2, Expert +0.3, Genius +0.4** per day. For the chief of army, attack modifiers apply to both soft and hard attack whether attacking or defending, and the defense modifier applies to defense or breakthrough depending on the role in combat.

| Chief of Army trait | Modifier | Specialist | Expert | Genius |
|---|---|---|---|---|
| Old Guard | Experience gain army factor −10%; political power gain +10% | — | — | — |
| Army Defense | Army defense factor | +5% | +10% | +15% |
| Army Drill | Division training time | −5% | −10% | −15% |
| Army Maneuver | Divisions speed | +5% | +10% | +15% |
| Army Morale | Division recovery rate | +4% | +8% | +12% |
| Army Offense | Army attack factor | +5% | +10% | +15% |
| Army Organization | Division organization | +4% | +8% | +12% |
| Army Planning | Planning speed | +5% | +10% | +15% |
| Army Reformer | Experience gain army factor | +5% | +10% | +15% |

| Chief of Navy trait | Modifier | Specialist | Expert | Genius |
|---|---|---|---|---|
| Old Guard | Experience gain navy factor −10%; political power gain +10% | — | — | — |
| Commerce Raiding | Convoy raiding efficiency | +10% | +15% | +20% |
| Decisive Battle | Capital ship attack / capital ship armor / screen attack / screen defense | +5% each | +10% each | +15% each |
| Naval Aviation | Carrier air agility / attack / targeting | +4% / +3% / +3% | +8% / +6% / +7% | +15% / +10% / +12% |
| Naval Maneuver | Naval speed | +5% | +10% | +15% |
| Naval Reformer | Experience gain navy factor | +5% | +10% | +15% |

| Chief of Air trait | Modifier | Specialist | Expert | Genius |
|---|---|---|---|---|
| Air Reformer | Experience gain air factor | +5% | +10% | +15% |
| Air Safety | Air accidents chance | −5% | −10% | −15% |
| All-Weather | Bad weather penalty | −10% | −20% | −30% |
| Ground Support | Air support | +5% | +10% | +15% |
| Night Operations | Night operations penalty | −10% | −20% | −30% |

### Military high command (3 slots)

High command advisors that buff a battalion type are weighted by that battalion's share of the division's combat battalions. Attack modifiers apply to soft and hard attack in both roles; defense modifiers apply to defense or breakthrough depending on the role. Two advisors giving the same bonus stack additively.

| Trait | Modifiers | Specialist | Expert | Genius |
|---|---|---|---|---|
| Air Combat Training | Ace generation chance | – | +10% | +15% |
| Air Superiority | Air superiority agility / attack / defense | – | +3% each | +5% each |
| Airborne Assault | Paradrop agility / attack / defense | +3% / +1% / +3% | +5% / +2% / +5% | – |
| Amphibious Assault | Amphibious invasion speed | +5% | +10% | +15% |
| Anti-Submarine | Submarine detection | +10% | +15% | – |
| Armor | Armor division attack / defense | +5% / +5% | +10% / +10% | +15% / +15% |
| Army Logistics | Division attrition | −4% | −8% | – |
| Army Regrouping | Division recovery rate | +4% | +8% | +12% |
| Artillery | Artillery attack / defense | +10% / +5% | +15% / +10% | +20% / +15% |
| Bomber Interception | Interception agility / attack / defense | +2% each | +3% each | – |
| Capital Ships | Capital ship armor / attack | +5% / +5% | +10% / +10% | – |
| Carriers | Sortie efficiency | – | +15% | – |
| Cavalry | Cavalry and motorized attack / defense | +5% each | +10% each | +15% each |
| Close Air Support | CAS agility / attack / defense | – | +3% each | +5% each |
| Commando | Special forces attack; special forces cap | +5% / +3 | +10% / +6 | +15% / +9 |
| Concealment | Enemy air support | −5% | −10% | −15% |
| Entrenchment | Entrenchment speed | – | +8% | – |
| Fleet Logistics | Naval max range factor | +5% | +10% | – |
| Infantry | Infantry division attack / defense | +5% / +10% | +10% / +15% | +15% / +20% |
| Naval Air Defense | Naval AA attack | +8% | +15% | – |
| Naval Aviation | Naval air agility / attack / targeting from carriers | – | +8% / +6% / +7% | +15% / +10% / +12% |
| Naval Strike | Naval agility / bombing / targeting | +2% each | +3% each | – |
| Screens | Screen attack / defense | – | +10% / +15% | – |
| Strategic Bombing | Bomber agility / attack / defense; strategic bombing | – | +2% each, +5% | +3% each, +9% |
| Submarines | Submarine attack / defense | – | +15% / +10% | – |
| Tactical Bombing | Ground support | – | +15% | – |

## National spirits

A national spirit is a modifier idea describing a country's unique advantages or disadvantages. Key rules:

- A country can hold several at once, and they are visible in the political menu.
- They are **granted, removed or modified by national focuses, events and decisions** — they are not bought with political power like laws and advisors.
- Many are country-unique; the generic ones below come from the generic focus tree and can appear on many nations.
- Unlike design-company bonuses, a spirit that changes production cost applies to everything produced while it is active, regardless of when the equipment was researched.
- They are not the same thing as officer corps spirits (see the Officer corps mechanic).
- All North and South American countries carry the **Monroe Doctrine** spirit.
- Releasable countries (Protectorate of Albania, Kumul Khanate, Vichy France, Free France, Confederacy of American States, Unaligned States of America, Italian State of East Africa, Reorganized National Government of the Republic of China, Slovakia, Protektorat Böhmen-Mähren, Carpatho-Ukraine) have their own spirits documented on their country pages.

### Generic national spirits

These come from the generic focus tree and can appear on many nations.

| Generic spirit | Effects |
|---|---|
| Collectivist Ethos | Daily Democracy support: –0.02 |
| Deterrence | Land fort construction speed: +20.00%; Coastal fort construction speed: +20.00%; Anti-air construction speed: +20.00%; Military factory construction speed: +20.00% |
| Foreign Expeditions | Divisions required for sending volunteer force: -50.0% |
| Internationalism | Daily Communism support: +0.10 |
| Ideological Fanaticism | War support: +5.00%; Division Attack on core territory: +10%; Division Defense on core territory: +10%; Rule Can Create Factions |
| Indoctrination | Weekly Manpower: +400; Stability: +5.00% |
| Liberty Ethos | Trade deal opinion factor: +20.00% |
| Militarism | Recruitable Population: 2.00%; Damage to Garrisons: -10.00% |
| Military Youth | Mobilization speed: +25.00%; Recruitable Population: 1.00% |
| Nationalism | Daily Fascism support: +0.10 |
| Neutral Foreign Policy | Join faction tension limit: +100.0%; Send volunteers tension limit: +20.0%; Guarantee tension limit: +100.0%; AI Modifier: Desire to be in or expand a faction: −100; AI Modifier: Threat receptivity: +1.0%; Embargo tension limit: +250.0% |
| Paramilitarism | Division training time: -10.0%; Supply Combat Penalties on Core Territory: -15.0% |
| Political Commissars | Division Recovery Rate: +10.0% |
| Political Correctness | Foreign subversive activities efficiency: –75% |
| Secret Weapons Initiatives | Special Project Speed: +5.00% |
| Special Forces | Special Forces Capacity Multiplier: +2.0% |
| Volunteer Corps | Divisions required for sending volunteer force: -25.0% |
| Why We Fight | Stability: +10.00%; War support: +10.00% |

### Starting national spirits by country

Spirits present at game start (1936 unless the country page says otherwise). "without X" means this version of the spirit applies when DLC X is not active.

| Country | National spirit | Effects | DLC / notes |
|---|---|---|---|
| Afghanistan | King Zahir Shah | Stability: +10.00% | Graveyard of Empires |
| Afghanistan | Pashtunwali | Political Power Gain: -40% Army experience Gain: -20.0% Navy experience Gain: -20.0% Air experience Gain: -20.0% Stability: +20.00% Daily support for Non-Aligned: +0.10 | Graveyard of Empires |
| Afghanistan | Quami | Army experience Gain: +2.0% Division Defense on core territory: +3.0% Irregular Infantry Defense: +5.00% Irregular Infantry Speed: +5.00% Irregular Infantry Organization: +5.00% | Graveyard of Empires |
| Afghanistan | Subsistence Economy | Stability: +20.00% Production efficiency cap: -35.00% Production efficiency growth: -50.00% Factory output: -50.00% | Graveyard of Empires |
| Afghanistan | Turkish Military Mission | Divisions speed: +5.00% Army experience Gain: +10.0% Division Attack: +5.0% Division Defense: +5.0% | Graveyard of Empires |
| Argentina, Bolivia, Brazil, Canada, Chile, Mexico, Paraguay, Uruguay, VenezuelaAnd all other American countries | Monroe Doctrine | — | base game |
| Argentina | Infamous Decade | Stability: -10.00% War support -10.00% Political Advisor Cost: +25% Daily Support for Unaligned: +0.02 | Trial of Allegiance |
| Argentina | Legacy of the Naval Arms Race | Dockyard output: -15.00% Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 Dockyard construction speed: -40.00% | Trial of Allegiance |
| Argentina | Political Corruption | Political Power Gain: +10% War support: -20.00% Construction Speed: -10.00% Production efficiency cap: -10.00% | Trial of Allegiance |
| Argentina | The Roca-Runciman Treaty | Consumer Goods Factories factor: 10.0% Resources to Market: +20% Trade Laws Cost: +10% Economy Laws Cost: +10% Civilian factory construction speed: +5.00% | Trial of Allegiance |
| Aussa | Warriors Skilled in Desert Warfare | Heat Attrition: -30.00% Supply Consumption: -10.0% Irregular Infantry Attack: +10.00% Irregular Infantry Defense: +15.00% Irregular Infantry Speed: +5.00% | base game |
| Australia | Great Depression | Consumer Goods Factories factor: 40.0% Stability: −10.00% Factory output: −15.00% Dockyard output: −15.00% | without Thunder at Our Gates |
| Australia | Unratified Westminster Act | Can decline call to war | base game |
| Australia | Citizen Army | Division Attack on Non-Core territory: -25.0% Division Defense on Non-Core territory: -25.0% | Thunder at Our Gates |
| Australia | Poor Population Growth | Monthly Population: -10.0% | Thunder at Our Gates |
| Australia | The Great Depression | Consumer Goods Factories factor: 40.0% Stability: -10.00% Factory output: -15.00% Dockyard output: -15.00% | Thunder at Our Gates |
| Austria | Austrofascism | Stability: +5.00% Daily Fascism Support: +0.02 Acceptance of Fascist Diplomacy: +50 Daily Support for Unaligned: +0.03 | Götterdämmerung |
| Austria | Phönix Insurance | Political Power Gain: +15% Recruitable population Factor: +15% Stability: +5.00% War support: +5.00% | Götterdämmerung |
| Austria | Recovering From Economic Depression | Consumer Goods Factories factor: 20.0% Factory output: −10.00% | Götterdämmerung |
| Austria | Treaty of Saint-Germain-en-Laye | Factory output: −50.00% Facility Construction speed: −100.00% Military Factory construction speed -75.00% So long as this National Spirit is active, conscription law cannot be raised beyond 'Volunteer Only'. Units cannot be trained, disbanded or have their templates modified Can send volunteers: no Will be removed 16 July, 1940 (1658 days) | Götterdämmerung |
| Austria | Widespread Unemployment | Political Power Gain: -10% Stability: -10.00% | Götterdämmerung |
| Belgian Congo | An Uncontrollably Vast Nation | Political Power Gain: -20% Recruitable population Factor: -15% Consumer Goods Factories factor: 15.0% Stability: -10.00% War support: -10.00% Construction Speed: -10.00% Resistance Target: +15% | Götterdämmerung |
| Belgian Congo | Force Publique | Supply Consumption: -5.00% Army Leader Cost: +100.0% Division Defense on core territory: +5.00% Daily Autonomy progress gain: -0.2 Maximum Command Power Increase: -50 Daily Command Power Gain Multiplier: -50% Hot acclimatization gain factor: +15.0% Equipment Capture Ratio Modifier: +10.0% Resistance Target: -5% | Götterdämmerung |
| Belgian Congo | The Invisible Roof | Stability: -10.00% Research Speed: -15.00% Daily Autonomy progress gain: +0.2 | Götterdämmerung |
| Belgium | Chasseurs Ardennais | Mountaineers: Forest: Movement Effective Change: +10% Attack Effective Change: +20% Defense Effective Change: +20% Mountain: Movement Effective Change: -10% Attack Effective Change: -20% | Götterdämmerung |
| Belgium | Corruption | Daily Political Power Gain: -0.25 Stability: -20.00% Construction Speed: -20.00% Daily Fascism Support: +0.10 | Götterdämmerung |
| Belgium | Economic Downturn | Consumer Goods Factories factor: 25.0% Factory output: -20.00% | Götterdämmerung |
| Belgium | Language Barriers | Daily Political Power Gain: -0.10 Stability: -10.00% War support: -10.00% | Götterdämmerung |
| Belgium | Scars of the Great War | Division Organization: -15.0% Recruitable population Factor: -15% War support: -30.00% Military factory construction speed: -20.00% | Götterdämmerung |
| Bolivia | The Era of National Regression | Political Power Gain: -20% Stability: -10.00% War support: -5.00% Will be removed if Greater Bolivia is restored: Has full control of Acre (940), Antofagasta (506), Chaco Boreal (688) | Trial of Allegiance |
| Bolivia | The Toll of the Chaco War | Recruitable population Factor: -15% War support: -15.00% Division Attack: -10.0% Justify War goal time: +30.0% Will be removed 1 November, 1939 (1400 days) | Trial of Allegiance |
| Brazil | Legacy of the Naval Arms Race | Dockyard output: -15.00% Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 Dockyard construction speed: -40.00% | Trial of Allegiance |
| Brazil | Separatist Sentiments | Stability: -10.00% War support: -10.00% | Trial of Allegiance |
| Brazil | State of Emergency | Stability: -5.00% Daily Communism Support: +0.05 | Trial of Allegiance |
| Brazil | Undiversified Economy | Production efficiency cap: -20.00% Production efficiency growth: -20.00% Factory output: -20.00% | Trial of Allegiance |
| Brazil | Weak Government | Political Power Gain: -20% Stability: -15.00% Daily Command power Gain Multiplier: -40% Daily Support for Unaligned: +0.02 | Trial of Allegiance |
| British Malaya | Colonial Exploitation | Civilian industry to overlord: +15.00% Resources to overlord: +10.00% | base game |
| British Malaya | Ketuanan Melayu | Recruitable population factor: -25% Stability: -10.00% Ideology drift defense: -15.0% | base game |
| British Raj | Agrarian Society | Recruitable population Factor: -70% | without Graveyard of Empires |
| British Raj | Marginalized Muslim Community | Recruitable population Factor: -20% Stability: -10.00% | base game |
| British Raj | Princely States | Daily Autonomy progress gain: -0.1 | base game |
| British Raj | Risk of Famine | A famine will trigger if one of these are true: We lose a starting Indian state and fail to take it back within 30 day(s) (Aden being excluded) The new controller is not a releasable that is occupied by us at the start of the game The new controller is not our subject | base game |
| British Raj | Agrarian Society | Mobilization speed: -72.00% Recruitable population Factor: -72% Conscription Laws Cost: +216% | Graveyard of Empires |
| British Raj | Great Depression | Consumer Goods Factories factor: +40.0% Factory output: -15.00% Dockyard output: -15.00% Stability: -15.00% | Graveyard of Empires |
| Bulgaria | Army Restrictions | Factory Output: -25.00% Dockyard Output: -25.00% Cannot increase conscription law or declare wars. Cannot train units, disband units, or edit unit templates. Cannot produce armor, aircraft or ships Can access international markets (Puppets and Overlords can always access each other's market) () | Battle for the Bosporus |
| Bulgaria | IMRO | Daily Political Power Gain: -0.30 Stability: -10.00% Improve Relations opinion: -15.00% | Battle for the Bosporus |
| Bulgaria | Second National Catastrophe | Stability: -10.00% Weekly Stability: -0.30% War support: -10.00% Will be removed if Greater Bulgaria is restored: Has full control of Sofia, Plovdiv, Moesia, Burgas, Southern Serbia, Macedonia, Central Macedonia, Thrace, Dobrudja, Northern Dobrudja. | Battle for the Bosporus |
| Canada | Conscription Crisis among French Canadians | Recruitable population Factor: −30% | base game |
| Canada | Great Depression | Consumer Goods Factories factor: 50.0% Factory output: −20.00% Dockyard output: −20.00% | base game |
| Chile | Legacy of the Naval Arms Race | Dockyard output: -15.00% Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 Dockyard construction speed: -40.00% | Trial of Allegiance |
| Chile | Near Anarchic Society | Political Power Gain: -15% Stability: -25.00% War support: -10.00% Daily Fascism Support: +0.02 | Trial of Allegiance |
| Chile | The Chilean Economy | Resource Gain Efficiency: -10.00% Consumer Goods Factories factor: 10.0% Stability: -5.00% Construction Speed: -15.00% Factory output: -15.00% Dockyard output: -5.00% | Trial of Allegiance |
| Chile | The Hacienda - Inquillinaje System | Recruitable population Factor: -10% Stability: -5.00% Production efficiency cap: +15.00% Daily Communism Support: +0.02 | Trial of Allegiance |
| Chile | The Mapuche Conflict | Recruitable population Factor: -5% Consumer Goods Factories factor: 5.0% War support: -10.00% Production Efficiency Retention: -5.00% | Trial of Allegiance |
| Chile | The Republican Guard | Division training time: -15.0% Recruitable population Factor: +5% Division Defense on core territory: +10.0% Ideology drift defense: +15.0% | Trial of Allegiance |
| China | Army Corruption | Mobilization speed: -35.00% Division Organization: -2.0% Division Attack: -30.0% Division Defense: -30.0% | without No Compromise, No Surrender |
| China | German Military Advisors | Land Doctrine Cost: -10.00% | without No Compromise, No Surrender |
| China | Incompetent Officers | Daily Command Power Gain Multiplier: -70% | without No Compromise, No Surrender |
| China | Ineffective Bureaucracy | Recruitable Population factor: -35.00% | without No Compromise, No Surrender |
| China | Low Inflation | Consumer Goods Factories factor: 10.0% Factory Output: -5.00% | without No Compromise, No Surrender |
| China | Nine Power Treaty | — | without No Compromise, No Surrender |
| China | Aviation Affairs Commission | Air experience Gain: -20.0% Air Accidents Chance: +25.0% | No Compromise, No Surrender |
| China | Corruption in the Administration | Daily Political Power Gain: +0.35 Consumer Goods Factories factor: 25.0% Construction Speed: -10.00% Free repair: -25.00% Economy Laws Cost: +65% | No Compromise, No Surrender |
| China | Corruption in the Armed Forces | Division Organization: -5.0% Recruitable population Factor: -78% Supply Consumption: +10.0% Division Recovery Rate: -25.0% Division Attack: -5.0% Division Defense: -15.0% Max Entrenchment: -1.0 Railway Construction speed: -15.00% | No Compromise, No Surrender |
| China | Illicit Trade | Consumer Goods Factories factor: 25.0% Factory output: -15.00% | No Compromise, No Surrender |
| China | Inefficient Economy | Production efficiency growth: -35.00% Base Fuel Gain: -50.00% | No Compromise, No Surrender |
| China | Neglected Countryside | Research Speed: -20.00% Daily Communism Support: +0.05 | No Compromise, No Surrender |
| China | Nine Power Treaty | Consumer Goods Factories factor: 16.0% Resources to Market: 16.0% Justify War goal time on us: -16.0% | No Compromise, No Surrender |
| Chinese Soviet Republic | Aftermath of the Long March | Construction Speed: -50.00% Factory Output: -15.00% | without No Compromise, No Surrender |
| Chinese Soviet Republic | Low Popular Support | Stability: -18.00% War Support: -18.00% | without No Compromise, No Surrender |
| Chinese Soviet Republic | Power Struggles | Conscription Laws cost: +25% Trade Laws cost: +25% Economy Laws cost: +25% Political Advisor Cost: +25% | without No Compromise, No Surrender |
| Chinese Soviet Republic | Red Army Weakened | Army Organization Regain: -10.00% Training time: +20.00% Reinforce Rate: -1.0% | without No Compromise, No Surrender |
| Chinese Soviet Republic | Agrarian Society | Construction Speed: -10.00% Research Speed: -15.00% Factory Output: -10.00% | No Compromise, No Surrender |
| Chinese Soviet Republic | Defunct State Bank | Consumer Goods Factories factor: 25.0% Stability: -10.00% | No Compromise, No Surrender |
| Chinese Soviet Republic | The Central Committee | Justify War goal time: +50.0% | No Compromise, No Surrender |
| Chinese Soviet Republic | The Chinese Red Army | Army experience Gain: -15.0% Division Organization: -10.0% Recruitable population Factor: -10% Division Attrition: -5.0% Division Attack: -10.0% Armor Division Attack: -10.0% Training time: +10.00% Max planning factor: -5.0% | No Compromise, No Surrender |
| Czechoslovakia | Divided Nation | Recruitable Population: -0.50% Stability: -20.00% | without Peace for Our Time |
| Czechoslovakia | Škoda Works | Factory output: +10.00% Facility construction speed: +5.00% | without Peace for Our Time |
| Czechoslovakia | Agrarian Politics | Consumer Goods Factories factor: 15.0% Party Popularity Stability Modifier: +5.00% Industrial Research Speed: -10% | Peace for Our Time |
| Czechoslovakia | Ceskoslovenska Armada | Division Experience Gain: +5.0% Division Organization: -15.0% Non-Combat Out of Supply Penalties: +10.0% Training time: +10.00% Supply Combat Penalties on Core Territory: -10.0% | Peace for Our Time |
| Czechoslovakia | Divided Nation | Daily Political Power Cost: +0.30 Stability: -20.00% Ideology drift defense: -30.0% | Peace for Our Time |
| Czechoslovakia | Industrialist's Veto | War support: -15.00% Lack of Resources Penalty: +10.00% Factory Energy Consumption: +10.00% Industrial Concern Cost: -5% Military factory construction speed: +15.00% | Peace for Our Time |
| Czechoslovakia | Tatíček Masaryk | Stability: +15.00% | Peace for Our Time |
| Czechoslovakia | The Sudetenland Quandary | Passive Effect: If Austria, Germany, or any other German Country that borders us justifies or gain a War Goal on us while either North Sudetenland (69), South Sudetenland (972) or Czeské Slezsko (74) are controlled by us: (All Controlled Sudetenland States): Add Sudetenland Paramilitary Activity which grants: Intel to Enemies: +10% Division Defense on core territory: -10.0% Local Land fort Repair Speed: -10.00% This Effect can only happen once | Peace for Our Time |
| Denmark | Danish Industrial Capabilities | Consumer Goods Factories factor: 30.0% Production Efficiency Retention: -5.00% Factory Output: -10.00% Dockyard Output: -10.00% Equipment Conversion Speed: -5% | Arms Against Tyranny |
| Denmark | Economic Crisis | Monthly Population: -10.0% Weekly Stability: -0.10% Daily Democracy Support: -0.05 Daily Support for Unaligned: +0.02 | Arms Against Tyranny |
| Denmark | Neglected Military | Mobilization speed: -20.00% Surrender Limit: -20.00% Planning Speed: -10.0% | Arms Against Tyranny |
| Dutch East Indies | Mismanaged Administration | Daily Political Power Gain: -0.25 Consumer Goods Factories factor: 20.0% Stability: -30.00% Construction Speed: -10.00% Research Speed: -15.00% | Thunder at Our Gates |
| Dutch East Indies | Netherlands Most Precious Jewel | Can raise autonomy to Free | Thunder at Our Gates |
| Dutch East Indies | Royal Netherlands East Indies Army | Army experience Gain: -5.0% Recruitable population Factor: -75% Division Attack: -7.5% Division Attack: -2.5% Training time: -20.00% | Thunder at Our Gates |
| Dutch East Indies | The Great Depression | Resources to Market: -70% | Thunder at Our Gates |
| Estonia | Democratic Opposition | Political Power Gain: -10% Stability: -15.00% War support: -10.00% Daily Democracy Support: +0.05 | No Step Back |
| Estonia | Low Vaps Tension | Recruitable Population Factor: -10% Stability: -10.00% Conscription Laws Cost: +25% Daily Fascism Support: +0.02 | No Step Back |
| Ethiopia | Air Force in Infancy | Air Accidents Chance: +15.0% Air Attack: -15% Enemy Air Support: +25.00% Air Doctrine Cost: +50.00% | By Blood Alone |
| Ethiopia | Conservative High Command | Infantry Division Attack: +10.0% Research Speed: -15.00% Maximum Command Power Increase Multiplier: -25% Land Doctrine Cost: +50.00% | By Blood Alone |
| Ethiopia | Corrupt Bureaucracy | Construction Speed: -25.00% Production Efficiency Cap: -10.00% Research Speed: -25.00% | By Blood Alone |
| Ethiopia | Ethiopian Industry | Consumer Goods Factories: 5.0% Production Efficiency Retention: -10.00% Factory Output: -10.00% Dockyard Output: -10.00% | By Blood Alone |
| Ethiopia | No Naval Tradition | Ship Refitting Cost: +25% Ship Repair Speed:: -10% Naval Doctrine Cost: +50.00% | By Blood Alone |
| Ethiopia | On Our Own | Can join factions | By Blood Alone |
| Ethiopia | The Heroes of Adwa | War support: +10.00% ( Italy) Attack bonus against country: +10.0% | By Blood Alone |
| Ethiopia | The International Red Cross | Division Recovery Rate: +10.0% Enemy Air Support: -5.00% | By Blood Alone |
| Ethiopia | Traditional Warfare | Army experience Gain: -20.0% Division Organization: -5.0% Supply Consumption: -10.0% Entrenchment speed: -50.0% Division Defense: -15.0% Max Entrenchment: -3.0 Infantry Attack: +5.00% Irregular Infantry Attack: +10.00% | By Blood Alone |
| Finland | Sisu | Division Recovery Rate: +5% Division Defense on core territory: +10% | base game |
| France | Disjointed Government | Daily Political Power Cost: +0.80 Stability: -10.00% Surrender Limit: -50.00% | base game |
| France | Full Employment | Recruitable population Factor: -25% | base game |
| France | Inefficient Economy | Factory output: -20.00% Dockyard output: -20.00% | base game |
| France | London Naval Treaty Signatory | Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 | base game |
| France | Political Violence | — | base game |
| France | Protected by the Maginot Line | Planning Speed: -25.0% Max Planning: +25.0% | base game |
| France | Victors of the Great War | Recruitable population: -0.30% War support: -5.00% Land Doctrine Cost: +50.00% | base game |
| Gansu Ma, Guangdong Clique, Guangxi Clique, Hebei-Chahar, Khotan Ma, Ningxia Ma, Northeastern Army, Qinghai Ma, Shandong Clique, Shanxi, Sichuan Clique, Sinkiang, Yunnan | Commonplace Looting | Consumer Goods Factories factor: 10.0% Division Recovery Rate: +5.0% Construction Speed: -5.00% | No Compromise, No Surrender |
| Gansu Ma, Guangdong Clique, Hebei-Chahar, Khotan Ma, Ningxia Ma, Northeastern Army, Qinghai Ma, Shandong Clique, Sichuan Clique | Government Corruption | Political Power Gain: -10% Stability: -10.00% | No Compromise, No Surrender |
| Gansu Ma, Guangdong Clique, Hebei-Chahar, Khotan Ma, Ningxia Ma, Northeastern Army, Qinghai Ma, Shandong Clique, Sichuan Clique | Ineffective Bureaucracy | Daily Political Power Gain: -0.25 | No Compromise, No Surrender |
| Gansu Ma, Khotan Ma, Ningxia Ma, Qinghai Ma | Ma Clique Collective | Cavalry Attack: +5.0% | No Compromise, No Surrender |
| Gansu Ma, Guangdong Clique, Hebei-Chahar, Khotan Ma, Ningxia Ma, Northeastern Army, Qinghai Ma, Shandong Clique, Sichuan Clique | Warlord State | Political Power Gain: -5% Recruitable Population Factor: +5% Division Attrition: -5.0% Supply Consumption: -3.0% Stability: -5.00% Research Speed: -3.00% Daily Command power Gain Multiplier: -15% This spirit is removed upon the completion of either of the focuses Power Struggle, The Yan'an Incident and Proclaim Rival Government | No Compromise, No Surrender |
| German Reich | Bitter Loser | Ideology drift defense: +50% Can create factions | base game |
| German Reich | Deutsches Heer | Division Organization: +5.0% Supply Consumption: +15% Planning Speed: +25.0% | base game |
| German Reich | Kriegsmarine | Screening bonus when using only capital ships: +10.0% Naval Defense: -10.00% | base game |
| German Reich | Luftwaffe | Air manpower requirement: +10.00% Air Accidents Chance: +10.0% | base game |
| German Reich | MEFO Bills | Consumer Goods Factories factor will increase by 3.0% each month up to 100.0%. The monthly increase will be higher based on the amount of non-core states controlled by German Reich. If Consumer Goods Factories factor reaches 100.0% additional penalties will be applied. Consumer Goods Factories: 10.0% Civilian Intelligence to others: -25.0% Army Intelligence to others: -25.0% Navy Intelligence to others: -25.0% Airforce Intelligence to others: -25.0% Military factory construction speed: +10.00% Naval dockyard construction speed: +10.00% | base game |
| Greece | Agrarian Society | Recruitable Population Factor: -45% Factory Output: -30.00% | Battle for the Bosporus |
| Greece | Debt to the I.F.C. | Consumer Goods Factories factor: 30.0% Stability: -10.00% | Battle for the Bosporus |
| Greece | Foreign Monopolies | Consumer Goods Factories factor: 40.0% Trade deal opinion factor: +25.00% Economy Laws Cost: +75% Trade Laws Cost: +75% | Battle for the Bosporus |
| Greece | George II | Stability: -5.00% Daily Support for Unaligned: +0.01 | Battle for the Bosporus |
| Greece | Political Instability | Political Power Gain: -15% The Monarchists are Loyal. Effects: Stability: +10% Recruitable Population Factor: +20% The Republicans are Hostile. Effects: Stability: -15% The Communists are Hostile. Effects: Stability: -15% The Fascists are Inconsequential. Effects: No effect. | Battle for the Bosporus |
| Greece | Schachtplan | Consumer Goods Factories factor: -25.0% Resources to Market: +30% Economy Laws Cost: +25% Trade Laws Cost: +25% Civilian factory construction speed: +15.00% | Battle for the Bosporus |
| Guangdong Clique, Guangxi Clique | Local Unease | Political Power: -5% Stability: -10.00% | No Compromise, No Surrender |
| Guangxi Clique, Qinghai Ma, Shanxi, Sinkiang, Xibei San Ma, Yunnan | Government Corruption | Political Power Gain: -10% Stability: -10.00% | base game |
| Guangxi Clique, Qinghai Ma, Shanxi, Sinkiang, Xibei San Ma, Yunnan | Ineffective Bureaucracy | Daily Political Power Gain: -0.25 | base game |
| Guangxi Clique, Qinghai Ma, Shanxi, Sinkiang, Xibei San Ma, Yunnan | Warlord State | Political Power Gain: -5% Recruitable Population Factor: +5% Division Attrition: -5.0% Supply Consumption: -3.0% Stability: -5.00% Research Speed: -3.00% Daily Command power Gain Multiplier: -15% This spirit is removed upon the completion of either of the focuses Power Struggle, The Yan'an Incident and Proclaim Rival Government | base game |
| Hungary | Treaty of Trianon | Recruitable Population: -0.50% Military Factory construction speed -50.00% Can access international market (Puppets and Overlords can always access each other's market) () | without Götterdämmerung |
| Hungary | Gömbös Trade Treaty | Political Power Gain: -15% Consumer Goods Factories factor: -10.0% Construction Speed: +5.00% Daily Fascism Support: +0.01 Allows for Arms Trade with Germany | Götterdämmerung |
| Hungary | Hungarian National Defense Association | Recruitable Population Factor: 10% War support: +5.00% Daily Fascism Support: +0.01 | Götterdämmerung |
| Hungary | Levente Associations | Recruitable Population Factor: 10% Ideology drift defense: +15.0% | Götterdämmerung |
| Hungary | Treaty of Trianon | Army Experience Gain: -15.0% Air Experience Gain: -25.0% Recruitable Population: -0.50% Factory Output: -10.00% Military factory construction speed: -50.00% Military Industrial Organization Research Bonus: -10% Funds Gain: -10% Can access international market (Puppets and Overlords can always access each other's market) () | Götterdämmerung |
| Iceland | Christian X | Stability: -10.00% Division Defense on Core Territory: +5.0% Daily Support for Unaligned: +0.01 | Arms Against Tyranny |
| Iceland | The Icelandic Economy | Construction Speed: -10.00% Production efficiency cap: -10.00% Research Speed: -10.00% Factory Output: -10.00% Dockyard Output: -10.00% | Arms Against Tyranny |
| Iran | Anglo-Iranian Oil Company | Resource Gain Efficiency: -15.00% Factory output: -10.00% Resources to Market: +20% | Graveyard of Empires |
| Iran | Azerbaijani Resistance | Stability: -10.00% War support: -10.00% | Graveyard of Empires |
| Iran | Islamic Traditions | Stability: +10.00% Research Speed: -10.00% Political Advisor Cost: +25% | Graveyard of Empires |
| Iran | Kurdish Resistance | Stability: -10.00% War support: -10.00% | Graveyard of Empires |
| Iran | Rural Feudalism | Political Power Gain: +5% Recruitable population Factor: -5% Construction Speed: -2.00% Research Speed: -5.00% | Graveyard of Empires |
| Iraq | Agrarian Society | Recruitable population Factor: -20% Consumer Goods Factories factor: 15.0% Construction Speed: -10.00% Factory output: -15.00% | Graveyard of Empires |
| Iraq | Anglo-Iraqi Treaty | Political Power Gain: -10% Stability: -20.00% ( United Kingdom) Attack bonus against country: -10.0% ( United Kingdom) Defense bonus against country: -10.0% | Graveyard of Empires |
| Iraq | Royal Iraqi Army | Army experience Gain: -3.0% Division Organization: -5.0% Recruitable population Factor: -5% Planning Speed: -10.0% Hot acclimatization gain factor: +15.0% | Graveyard of Empires |
| Iraq | The Golden Square | Political Power Gain: -20% Stability: -20.00% Daily Fascism support: +0.02 | Graveyard of Empires |
| Italy | London Naval Treaty Signatory | Carrier Max Cost: 10250 Cruiser Max Cost: 5700 Heavy Ship Max Cost: 11500 | base game |
| Italy | Military Industry | Armor Research Speed: -15% Weapons and Equipment Research Speed: -15% Artillery Research Speed: -15% Air Research Speed: -15% Naval Research Speed: -15% Production Efficiency Cap: -10.00% Production Efficiency growth: -5.00% Production Efficiency Base: -5.00% Factory Output: -10.00% | base game |
| Italy | Regia Aeronautica | Ace generation chance: +10.00% Naval Mission Efficiency: -10% Air Accidents Chance: +5.0% Night Operations Penalty: +15.00% Bad Weather Penalty: +15.00% Air Superiority Bonus in Combat: +5.0% Air Doctrine Cost: +10.00% | base game |
| Italy | Regia Marina | Fleet Coordination: -5% Naval Detection: -10% Spotting Speed: -10% Screening Efficiency: +5.0% Naval Doctrine Cost: +10.00% Attack when in combat alongside the Pride of the Fleet: +10.00% | base game |
| Italy | Regio Esercito | Divisions speed: -10.00% Divisions Organization: -10.0% Org Loss when Moving: +15.0% Max Entrenchment: +10.00% Land Doctrine Cost: +10.00% | base game |
| Italy | Ricostruzione Industriale | Aircraft Designer Cost: -15% Tank Designer Cost: -15% Naval Designer Cost: -15% Materiel Designer Cost: -15% Industrial Concern Cost: -35% Civilian factory construction speed: +5.00% | base game |
| Italy | Victor Emmanuel III | Stability: +5% | base game |
| Italy | Vittoria Mutilata | Justify war goal time: −5% Acceptance of Communist Diplomacy: −10 Acceptance of Democratic Diplomacy: −10 Acceptance of Fascist Diplomacy: +10 | base game |
| Japan | Army and Naval Air Services | Separate Air Services, which grants Air Research Speed: -10% Air Wing Experience loss when killed: +10% Naval Mission Efficiency: +10% Untrained pilots penalty for new Air Wings: +10% | base game |
| Japan | Early Industrialization Efforts | Consumer Goods Factories factor: 30.0% Lack of Resources Penalty: +10.00% Research Speed: -3.00% Factory Bomb Vulnerability: +25.00% | base game |
| Japan | Imperial Army | Japanese Armor Doctrine, which grants Armor Research Speed: -10% All Tank Equipment: Production cost: +10.00% Armor Division Attack: -10.0% Tanks & Armor Variants: Jungle: Attack Effective Change: +10% Defense Effective Change: +10% Supply Consumption: +20.0% Division Recovery Rate: +5.0% Division Defense: -5.0% Artillery Attack: -10.0% Initiative: +10.0% | base game |
| Japan | Imperial Influence | Current Faction Levels: Meddling Army Faction, which grants All Infantry and Support Equipment: Production cost: +2.50% All Artillery Equipment: Production cost: +2.50% Fighter and CAS: Production cost: +2.50% Army Fuel Capacity: -2.50% Meddling Navy Faction, which grants All Carrier Aircraft: Production cost: +2.50% All Warships: Production cost: +2.50% Navy Fuel Consumption: +2.50% Meddling Zaibatsu Faction, which grants Economy Laws Cost: +20% Infrastructure: construction speed: +10.00% Civilian factory construction speed: +10.00% Meddling Civic Faction, which grants Daily Political Power Gain: +0.05 Recruitable population Factor: -5% Stability: +5.00% War support: -10.00% Trade Laws Cost: +25% | base game |
| Japan | Imperial Navy | Naval Detection: -10% Number of ships in the first contact: +10% Naval Max Range Factor: +10.00% Escort efficiency: -15.0% Accident chance: +10.00% Torpedo hit chance: +15.00% | base game |
| Japan | London Naval Treaty Signatory | Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 | base game |
| Japan | Militarism | Research Speed: -5.00% Justify War goal time: -20.0% Conscription Laws Cost: -25% Civilian factory construction speed: -10.00% | base game |
| Japan | State Shintoism | Surrender Limit: +10.00% War support: +20.00% | base game |
| Khotan Ma | Widespread Unrest | Division Organization: -3.0% Recruitable population Factor: -5% Division Recovery Rate: +5.0% Stability: -20.00% War support: -5.00% | No Compromise, No Surrender |
| Khotan Ma, Sinkiang | Battle for Sinkiang | Can Join Factions: No | No Compromise, No Surrender |
| Latvia | Democratic Opposition | Political Power Gain: -10% Stability: -15.00% War support: -10.00% Daily Democracy Support: +0.05 | No Step Back |
| Latvia | Pērkonkrusts | Recruitable Population Factor: -20% Stability: -15.00% Land Doctrine Cost: +25.00% Conscription Laws Cost: +50% Daily Fascism Support: +0.10 | No Step Back |
| Lithuania | Agrarian Society | Recruitable Population Factor: -50% Consumer Goods Factories factor: 6.0% Factory Output: -20.00% | No Step Back |
| Lithuania | Low Iron Wolf Threat | Recruitable Population Factor: -15% Daily Command Power Gain: -0.05 Conscription Laws Cost: +10% Daily Fascism Support: +0.05 | No Step Back |
| Lithuania | The Seimas | Stability: -15.00% Economy Laws Cost: +15% Political Advisor Cost: +15% Daily Democracy Support: +0.05 | No Step Back |
| Lithuania | Underfunded Military | Army Leader Cost: +50.0% Daily Command Power Gain Multiplier: -50% Land Doctrine Cost: +25.00% | No Step Back |
| Manchukuo | Banditry | Stability: -10.00% War Support: -10.00% | base game |
| Manchukuo | Kwantung Veto | Conscription Laws cost: +25% Trade Laws cost: +25% Economy Laws cost: +25% Political Advisor Cost: +25% | base game |
| Manchukuo | Low Legitimacy | Stability: -50.00% War Support: -50.00% | base game |
| Manchukuo | The Kangde Emperor | Political Power Gain: +5% | base game |
| Mengjiang | Stretched Administration | Recruitable population Factor: -5% Consumer Goods Factories factor: 10.0% Construction Speed: -5.00% | base game |
| Mengjiang | The Paillingmiao Council | Political Power Gain: +10% Ideology drift defense: +15.0% | base game |
| Mengjiang | A Disorganized Army | Division Organization: -5.0% Recruitable population Factor: -5% Division Attack: -10.0% Division Defense: -10.0% | No Compromise, No Surrender |
| Mengjiang | Communist Revolutionaries | Daily Communism Support: +0.01 | No Compromise, No Surrender |
| Mengjiang | Mongol Banners | Irregular Infantry Attack: +10.00% Irregular Infantry Defense: +10.00% Allows for the raising of Irregular Divisions when at war | No Compromise, No Surrender |
| Mexico | Callistas | Political Power gain: -20% Construction Speed: -10.00% | base game |
| Mexico | Caudillo Tensions Moderate | Stability: -5.00% | base game |
| Mexico | Oil Concessions | — | base game |
| Mexico | Politicized Army | Military Leaders Cost: +100.0% Planning Speed: -20.0% | base game |
| Mexico | Weak Church | Factory Output: +10.00% | base game |
| Nationalist Spain | Recovering From Civil War | Consumer Goods Factories: 20.0% Construction Speed: -10.00% Factory Output: -20.00% Dockyard Output: -20.00% Join faction tension limit: +50.0% | base game |
| Nationalist Spain | Carlism | Recruitable population: 1.00% Infantry Division Attack: +5.0% Infantry Division Defense: +5.0% | La Résistance |
| Nationalist Spain | Expand Conscription | Recruitable population: 2.00% | La Résistance |
| Nepal | Royal Nepalese Army | Special Forces Attack: +5.0% Special Forces Defense: +5.0% Special Forces Capacity Multiplier +75.0% | base game |
| Netherlands | Aloof Neutrality | Join faction tension limit: +100.0% Send volunteers tension limit: +50.0% Guarantee tension limit: +100.0% AI Modifier: Desire to be in or expand a faction: −100 AI Modifier: Threat receptivity: +1% | base game |
| Netherlands | De Crisisjaren | Construction Speed: -50.00% | base game |
| Netherlands | Shell-shocked Spectator of the Great War | Recruitable Population Factor: -25% Factory Output: -25.00% Dockyard Output: -10.00% | base game |
| Netherlands | Weak Government | Daily Political Power Cost: +0.50 Stability: -10.00% | base game |
| Netherlands | Wilhelmina | Popular Figurehead Stability: +15.00% | base game |
| New Zealand | British Commonwealth Loyalty | Stability: +10.00% Overlord trade cost: -20.00% | base game |
| New Zealand | The Government Railways Board | Political Power Gain: -10% Railway construction speed: -20.00% | base game |
| New Zealand | The Great Depression | Daily Political Power Cost: +0.60 Resource Gain Efficiency: -20.00% Consumer Goods Factories factor: 30.0% Construction Speed: -5.00% | base game |
| Norway | Anti-Communist Sentiment | Daily Fascism Support: +0.01 | Arms Against Tyranny |
| Norway | Complacent Cabinet | Daily Political Power Gain: -0.25 Division training time: +60.0% Trade Laws Cost: +50% Economy Laws Cost: +50% Theorist Cost: 120% | Arms Against Tyranny |
| Norway | Crumbling Fortifications | Land fort effectiveness: -50% Coastal fort effectiveness: -50% | Arms Against Tyranny |
| Norway | Obsolete Armed Forces | Divisions speed: -25.00% Division Organization: -20.0% Division Attack: -30.0% | Arms Against Tyranny |
| Norway | The Hard Thirties | Consumer Goods Factories factor: 55.0% Construction Speed: -30.00% | Arms Against Tyranny |
| Paraguay | The Aftershock of the Triple Alliance | Monthly Population: -60.0% Will be removed if controlling Formosa (957), Punta Porá (504) Will be removed 16 November, 1940 (1780 days) | Trial of Allegiance |
| Paraguay | The Toll of the Chaco War | Recruitable population Factor: -15% War support: -15.00% Division Attack: -10.0% Justify War goal time: +30.0% Will be removed 1 November, 1939 (1400 days) | Trial of Allegiance |
| Philippines | Island Nation | Convoy speed while retreating: +15% Visibility: -5.00% | base game |
| Philippines | American Interference | Technology sharing bonus: +20.00% Daily Autonomy progress gain: -0.1 | No Compromise, No Surrender |
| Philippines | Philippine Army | Army experience Gain: -80.0% Recruitable population Factor: -50% Factory output: -90.00% Dockyard output: -50.00% Training Time: +40.00% Daily Command power Gain Multiplier: -20% | No Compromise, No Surrender |
| Philippines | The Great Depression | Any ideology drift will align with the ruling party Daily Political Power Gain: -0.75 Resource Gain Efficiency: -25.00% Consumer Goods Factories factor: 50.0% Construction Speed: -25.00% Join faction tension limit: +100.0% | No Compromise, No Surrender |
| Poland | Looming Peasant's Strike | — | P |
| Poland | Low Sanation Left Opposition | Stability: -5.00% Daily Support for Unaligned: +0.02 | P |
| Poland | Low Sanation Right Opposition | War support: -10.00% Daily Support for Unaligned: +0.05 | P |
| Poland | The April Constitution | Political Power Gain: -15% Conscription Laws Cost: +15% Economy Laws Cost: +15% Political Advisor Cost: +15% Daily Support for Unaligned: +0.05 | P |
| Portugal | Unreliable Army | Division Organization: -10.0% Recruitable Population Factor: -25% War Support: -5.00% Division Attack: -5.0% | La Résistance |
| Portugal | Unstable Republic | Daily Political Power Gain: -0.50 Weekly Stability: -0.50% Construction Speed: -20.00% | La Résistance |
| Republican Spain | Carlism | Weekly Stability: -0.30% Division Attack: -10.0% Division Defense: -10.0% Daily Support for Unaligned: +0.05 | La Résistance |
| Republican Spain | Military Disloyalty | Military Leader Cost: +100.0% Cannot train units, disband units, or edit unit templates. | La Résistance |
| Republican Spain | National Strikes | Stability: -10.00% Construction Speed: -10.00% Factory Output: -10.00% Dockyard Output: -10.00% | La Résistance |
| Republican Spain | Political Violence | Stability: -15.00% Cannot Assign Ministers & Laws: Yes | La Résistance |
| Romania | King Carol II's Lifestyle | — | base game |
| Romania | Neutral Foreign Policy | Join faction tension limit: +100% Send volunteers tension limit: +20% Guarantee tension limit: +100% Embargo tension limit: +250% AI Modifier: Threat receptivity: +1% AI Modifier: Desire to be in or expand a faction: −100 | base game |
| Siam | Army of Siam | Supply Consumption: -10.0% Supply Range: +15% Military factory construction speed: +10.00% | without Thunder at Our Gates |
| Sichuan Clique | A Loose Unity | Political Power Gain: -10% Stability: -10.00% Division Attack on core territory: -5.0% Division Defense on core territory: -10.0% | No Compromise, No Surrender |
| South Africa | History of Segregation | Recruitable Population Factor: -55% | base game |
| South Africa | Ossewabrandwag | Factory Output: -10.00% Dockyard Output: -10.00% Daily Fascism Support: +0.01 | base game |
| Soviet Union | Five Year Plan | Consumer Goods Factories factor: +10.0% Production Efficiency Cap: +5% Production Efficiency Growth: -15% Civilian factory construction speed: +5% | base game |
| Soviet Union | Home of the Revolution | Ideology drift defense: +50.0% Can create factions | base game |
| Soviet Union | Politicized Military | Division Defense on core territory: +3.0% Ideology drift defense: +10.0% Commander Abilities Cost: +10.00% Air Doctrine Cost: +20.00% Land Doctrine Cost: +20.00% Naval Doctrine Cost: +20.00% | base game |
| Soviet Union | Soviet Air Force | Air Wing Experience loss when killed: +30% Ace generation chance: -50.00% Air Wing Training Experience Gain: -10% Air Accidents Chance: +75.0% Night Operations Penalty: +30.00% Bad Weather Penalty: +30.00% Air Wing Mission Experience Gain: +10% | base game |
| Soviet Union | The Red Army | Army experience Gain: -10.0% Division Organization: -15.0% Experienced soldier losses: +25.0% Conscription Laws Cost: -10% | base game |
| Soviet Union | Trotskyite Plot? | Political Power gain: -15% Stability: -20.00% | base game |
| Sweden | En Svensk Tiger | Ideology drift defense: +10.0% Justify wargoal time on us: +10.0% | without Arms Against Tyranny |
| Sweden | Neutral Foreign Policy | Join faction tension limit: +100.0% Send volunteers tension limit: +20.0% Guarantee tension limit: +100.0% Embargo tension limit: +250.0% AI Modifier: Threat receptivity: +1.0% AI Modifier: Desire to be in or expand a faction: −100 | base game |
| Sweden | Folkhemmet | Stability: +25.00% War support: -25.00% Infrastructure construction speed: +20.00% Military factory construction speed: -20.00% Civilian factory construction speed: +20.00% Naval dockyard construction speed: -20.00% | Arms Against Tyranny |
| Sweden | Hungersköld | Sweden risks strikes or riots if Stability is under 68% Will be removed if either of the following are true: Has more than 45 Civilian factories including trade Has constructed more than 14 Civilian factories excluding trade Gain 120 Political Power upon removal | Arms Against Tyranny |
| Sweden | King Gustaf V | Former Autocrat Political Power Gain: -10% Acceptance of Fascist Diplomacy: +20 Acceptance of Unaligned Diplomacy: +20 Daily Support for Unaligned: +0.01 Daily Command power Gain Multiplier: +15% | Arms Against Tyranny |
| Sweden | Severe lack of ammunition | Division Attack: -10.0% Division Defense: -10.0% | Arms Against Tyranny |
| Switzerland | Foreign Fascist Propaganda | Daily fascist support: +0.04 | By Blood Alone |
| Switzerland | Swiss Neutrality | Improve relations opinion: -20.00% Join faction tension limit: +100.0% Send volunteers tension limit: +20.0% Guarantee tension limit: +100.0% Justify War goal time on us: +250.0% Embargo Tension Limit: +250.0% Army Chief Cost: +200% Daily Democracy Support: +0.01 | By Blood Alone |
| Tibet | Dmag Dpung Bod | Cold acclimatization gain factor: +10.0% Armor Research Speed: -5% Air Research Speed: -5% | base game |
| Tibet | Ganden Podrang | Stability: +10.00% War support: -10.00% | base game |
| Turkey | Birinci Beş Yıllık Sanayi Planı | Civilian factory Construction Speed: +5.00% Construction Technology Research Speed: +5% | Battle for the Bosporus |
| Turkey | Disorganized Armed Forces | Fleet Coordination: -15% Divisions speed: -10.00% Divisions Organization: -8.00% Air Accidents Chance: +15.0% War support: -15.00% Training time: +25.00% Minimum training level: -10% | Battle for the Bosporus |
| Turkey | Kemalist Officers | Army experience gain: -10.0% Stability: +5.00% Max Planning: +10.0% | Battle for the Bosporus |
| Turkey | Sectarian Woes | Stability: -15.00% War support: -15.00% Turkey's internal divisions are represented geographically through State Modifiers: the Kemalists can be found in the west and in the north, the religious Traditionalists can be found in the central hinterlands as well as in the south, while the Kurdish people can be found in the south-east of the nation. Interactions with the different Factions can be accessed through the Decisions Tab, as well as through some Focus Effects and Event Options. | Battle for the Bosporus |
| Turkey | Widespread Illiteracy | Political Power gain: -5% Stability: -5.00% Research Speed: +5.00% | Battle for the Bosporus |
| United Kingdom | British Stoicism | Ideology drift defense: +50.0% Can Create Factions | base game |
| United Kingdom | King George V | Popular Figurehead Stability: +15.00% | base game |
| United Kingdom | London Naval Treaty Signatory | Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 | base game |
| United Kingdom | The War to End All Wars | Recruitable population Factor: -30% | base game |
| United States | Home of the Free | Ideology drift defense: +20.0% Cannot Join Factions lead by another ideology Can Create Factions | base game |
| United States | London Naval Treaty Signatory | Carrier Max Cost: 9500 Cruiser Max Cost: 5300 Heavy Ship Max Cost: 10000 | base game |
| United States | Monroe Doctrine Enforcer | — | base game |
| United States | The Great Depression | Daily Political Power cost: +1.00 Resource Gain Efficiency: -20.00% Recruitable population Factor: -50% Consumer Goods Factories factor: 60.0% Join faction tension limit: +20.0% | base game |
| Uruguay | Low Amounts of External Debts | Consumer Goods Factories factor: 10.0% Construction Speed: +5.00% | Trial of Allegiance |
| Venezuela | Blockade Inactive | Foreign Powers can blockade our oil shipments to Fascist aligned powers if they have more than 2 Capital Ships in the Caribbean Sea | base game |
| Yugoslavia | Anti-German Military | Ideology drift defense: +5.0% | base game |
| Yugoslavia | Croatian Opposition | Stability: -30.00% | base game |
| Yugoslavia | Macedonian Opposition | Conscription Laws Cost: +25% Trade Laws Cost: +25% Economy Laws Cost: +25% Political Advisor Cost: +25% | base game |
| Yugoslavia | Serbian General Staff | Military Leader Cost: +50.0% Max Planning: +10.0% | base game |
| Yugoslavia | Slovene Nationalism | Production efficiency growth: -10.00% | base game |
