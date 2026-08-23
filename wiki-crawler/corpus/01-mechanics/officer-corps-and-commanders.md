---
title: Officer Corps and Commanders
category: mechanics
tags: [officer-corps, spirits, command-power, commanders, generals, field-marshals, admirals, traits, battle-plan, army-planner, command-group]
game_version: "1.19"
dlc: [No Step Back, By Blood Alone]
sources:
  - https://hoi4.paradoxwikis.com/Officer_corps
  - https://hoi4.paradoxwikis.com/Commander
  - https://hoi4.paradoxwikis.com/Commander_trait
  - https://hoi4.paradoxwikis.com/Command_group
  - https://hoi4.paradoxwikis.com/Army_planner
  - https://hoi4.paradoxwikis.com/Battle_plan
  - https://hoi4.paradoxwikis.com/Government
---

## Summary

The officer corps tab (added in 1.11 Barbarossa) is where command power, military advisors and high command, doctrines, preferred tactics and — with No Step Back — army/navy/air **spirits** are managed. Commanders (generals, field marshals, admirals and, with By Blood Alone, divisional commanders) gain experience from combat, level up specialised skills, and earn or purchase traits. Battle plans convert command groups into AI-driven offensives and grant a planning bonus that adds attack and breakthrough.

## Command power

Command power (CP) lets the government bypass the chain of command and act on the military directly.

- **Base cap: 80.** Both the cap and daily growth are raised by doctrines, national spirits and army officer-corps spirits; hiring military chiefs and military high command raises the cap.
- **War support** modifies CP growth: **+50% CP gain** at maximum war support; **−95% CP gain** at minimum war support.
- Abilities can be one-off or continuously allocated (the CP stays reserved while the mission runs).

| Use | CP cost | Notes |
|---|---|---|
| Assign a commander trait | 15 | Same for generals, field marshals and admirals |
| Hire (promote) a general | 5 per existing general/field marshal | Capped at 80 |
| Hire an admiral | 5 per existing admiral | Capped at 80 |
| Promote a general to field marshal | 40 | Base cost; modified by personality traits |
| Set the country's preferred combat tactic | 20 | Officer corps tab |
| Send attaché | 50 (plus 100 political power) | Allocated for as long as the attaché is active |
| Air Supply mission | 0.05 per plane | Allocated while the mission runs; each plane gives 0.01 supply at full efficiency |
| More Ground Crews | 20 per air zone | +10% air efficiency in the zone; allocated while active |
| Commander abilities | Variable, per battalion | See ability table below |

### Attaché

Costs 100 political power + 50 CP (permanently allocated). Sender gains: shared military intelligence from the recipient, **15% of the Army/Navy/Air experience the recipient generates**, **+10% war support** (once only), and **+0.05 daily autonomy** if it is a puppet of the recipient.

## Military High Command and advisors

Generals and admirals become available as military advisors at **skill level 4**.

| Skill level | Advisor tier |
|---|---|
| 4 | Specialist |
| 6 | Expert |
| 8 | Genius |

Their acquired commander traits determine which high-command slot they can fill.

### Army high command

| High Command trait | Required commander trait | Bonuses (Specialist / Expert / Genius) |
|---|---|---|
| Army Regrouping | Organizer | +4% / +8% / +12% division recovery rate |
| Cavalry Officer | Cavalry Leader | +5% / +10% / +15% attack and defence for cavalry |
| Infantry Officer | Infantry Leader | +5% / +10% / +15% attack and +10% / +15% / +20% defence for infantry |
| Army Logistics | Skilled Staffer | −4% / −8% / −12% division attrition |
| Entrenchment | Engineer | +4% / +8% / +12% entrenchment speed |
| Armor | Panzer Leader | +5% / +10% / +15% attack and defence for armor |
| Commando | Commando | +5% / +10% / +15% attack for special forces; +3 / +6 / +10 special forces capacity |
| Amphibious Assault | Invader | +5% / +10% / +15% naval invasion speed |
| Combined Arms | Combined Arms Expert | +5% / +10% / +15% attack and defence for motorized and mechanized |
| Artillery | Fortress Buster | +10% / +15% / +20% attack and +5% / +10% / +15% defence for artillery |
| Concealment | Camouflage Expert | −5% / −10% / −15% enemy air support |

### Navy high command

| High Command trait | Required commander trait | Bonuses (Specialist / Expert / Genius) |
|---|---|---|
| Anti-Submarine | Sea Wolf | +10% / +15% / +20% submarine detection |
| Screens | Fleet Protector | +5% / +10% / +15% attack and +10% / +15% / +20% defence for screens |
| Carriers | Flight Deck Manager | +5% / +10% / +15% sortie efficiency |
| Capital Ships | Big Guns Expert | +5% / +10% / +15% attack and defence for capital ships |
| Submarines | Torpedo Expert | +10% / +15% / +20% attack and +5% / +10% / +15% defence for submarines |
| Naval Air Defense | Fly Swatter | +8% / +15% / +20% naval AA attack |
| Naval Strike | Torpedo Bomber | +2% / +3% / +5% naval bombing, naval targeting and naval agility |
| Fleet Logistics | Blue Water Expert | +5% / +10% / +15% naval max range factor |

### Army advisors (Chief of Army etc.)

| Advisor trait | Required commander trait | Bonuses (Specialist / Expert / Genius) |
|---|---|---|
| Army Offence | Offensive Doctrine | +5% / +10% / +15% division attack |
| Entrenchment | Defensive Doctrine | −2% / −4% / −6% mobilization speed and +3 / +5 / +7 max entrenchment |
| Army Reformer | Fast Planner | +5% / +10% / +15% army experience |
| Army Planning | Thorough Planner | +5% / +10% / +15% planning speed |
| Army Defense | Unyielding Defender | +5% / +10% / +15% division defense |
| Army Maneuver | Aggressive Assaulter | +5% / +10% / +15% division speed |
| Army Organization | Organization First | +4% / +8% / +12% division organization |
| Army Morale | Charismatic | −3% / −6% / −9% non-combat out-of-supply penalties |
| Army Drill | Expert Delegator | −5% / −10% / −15% division training time |

### Navy advisors

| Advisor trait | Required commander trait | Bonuses (Specialist / Expert / Genius) |
|---|---|---|
| Naval Maneuver | Superior Tactician | +5% / +10% / +15% naval speed |
| Commerce Raiding | Concealment Expert | +10% / +15% / +20% convoy raiding efficiency |
| Naval Reformer | Safety First | +5% / +10% / +15% naval experience |
| Naval Aviation | Dive Bomber | +3% / +6% / +10% naval air attack from carriers; +3% / +7% / +12% naval air targeting from carriers; +4% / +8% / +15% naval air agility from carriers |
| Decisive Battle | Marksman | +5% / +10% / +15% attack and defence for capital ships and screens |

## Doctrines and preferred tactics

- Each doctrine node has a **base cost of 100** of the matching experience type, modified by spirits, advisors and bonuses from focuses/events/decisions.
- The country's **preferred combat tactic** is set in the officer corps for **20 command power**; it raises the chance that commanders pick that tactic in land battles.

## Officer corps spirits (requires No Step Back)

Slot limits: **army command 3 spirits, navy command 3 spirits, air force command 2 spirits.** Costs are paid in the matching experience type and effects apply immediately.

### Army — Spirit of the Academy (20 army XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Bold Attack | Officers: 50% chance of +1 Attack on level up | — |
| Tenacious Defense | Officers: 50% chance of +1 Defense on level up | — |
| Meticulous Preparation | Officers: 50% chance of +1 Planning and +1 Logistics on level up | — |
| Best of the Best | Starting level of new army leaders +2; army intelligence to others −5%; new officers gain no personality traits on hiring | Democratic |
| Academy Scholarships | Army leader cost −30%; starting level of new army leaders +1; commander-as-advisor cost −75%; new officers gain no personality traits on hiring | Communist |
| Political Loyalty | Army leader cost −50%; party popularity stability modifier +10%; new officers guaranteed to start with Politically Connected or Media Personality (equal weight) | Fascist or Non-aligned |
| Inventive Leadership | Trickster, Commando and Invader trait XP gain +20%; new officers have a 75% chance to start with Commando, Trickster or Invader (equal weight) | — |
| Embrace the Future | New officers: 50% chance to start with Armor Officer; Panzer Leader trait XP gain +20% | Mobile Warfare |
| Engineering Schools | New officers: 50% chance to start with Engineer Officer; initiative +4%; Engineer trait XP gain +20% | Superior Firepower |
| Theatre Training | New officers: 50% chance to start with Brilliant Strategist or Inflexible Strategist (equal weight); terrain trait XP gain +20% | Grand Battle Plan |
| The Queen of Battle | New officers: 50% chance to start with Infantry Officer; Infantry Leader trait XP gain +20% | Mass Assault |
| Flexible Officers | Starting level of new army leaders +2; leader skill bonuses +10%; promotion cost −30%; army reassignment duration −30% | Norway, via Officers Academy |
| Whampoa Primacy | Army leader cost −15%; starting level of new army leaders +1; party popularity stability modifier +15%; planning speed −5%; max planning factor −5%; new officers guaranteed Politically Connected or Media Personality | China starts with this (No Compromise, No Surrender) |
| Cult of Heroism | Automatic free medal chance +50%; unit medal effectiveness −25% | Grand Battle Plan (No Compromise, No Surrender) |
| Professional Officer Corps | Division experience gain +15%; maximum command power +30 | — |

Terrain traits, for the Theatre Training bonus, are: Winter Specialist, Desert Fox, Swamp Fox, Mountaineer, Hill Fighter, Jungle Rat, Ranger, Urban Assault Specialist.

### Army — Spirit of the Army (35 army XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Elevated Engineering Corps | Entrenchment speed +10%; Railway Artillery bombardment +25%; Engineer company unit design cost −100% | — |
| Proper Heritage | Leader experience gain +10%; supply combat penalties on core territory −20%; Cavalry unit design cost −100% | Grand Battle Plan or Mounted Infantry |
| Relief of Command | Army experience gain +25%; army advisor cost −50% | Democratic |
| Ideological Loyalty | Weekly manpower +500; encirclement penalty −20% | Communist |
| State serves the Military | Offensive-war stability penalty modifier +10%; conscription law cost −25% | Fascist |
| Motorization Drive | Motorized and Mechanized combat XP gain +10% each; all Tanks, Motorized and Mechanized unit design cost −100% | Mobile Warfare |
| Overwhelming Firepower | Artillery combat XP gain +10%; unit design cost −100% for Support Artillery, Artillery, Motorized Artillery, Infantry, Bicycle battalion and all SP Artillery except Modern | Superior Firepower |
| Tip of the Spear | Extra paratrooper/marine supply grace +24 h; special forces cap +24; Marine, Mountaineer, Ranger and Paratrooper unit design cost −50% | Grand Battle Plan |
| Bayonett Strength | Infantry combat XP gain +10%; Infantry, Motorized, Mechanized and Bicycle battalion unit design cost −100% | Mass Assault |
| Accomplished Heritage | Grant medal cost −50%; field officer division penalty −100% | Requires By Blood Alone |
| Living off the Land | Division attrition +10%; non-combat out-of-supply penalties −10% | Mass Assault (No Compromise, No Surrender) |
| Subsidized Contracts | Armored car production cost −15%; light tank production cost −10%; armored support vehicle production cost −10% | Mobile Warfare or Armored Cavalry (No Compromise, No Surrender + La Résistance) |
| Spirit of Defiance | Resistance target in our enemy-occupied states +25%; resistance growth speed there +50% | Mass Assault, Guerilla War or People's Militia (No Compromise, No Surrender) |
| Intervention Specialists | Army experience from volunteers +50% | Superior Firepower or Expeditionary Warfare (No Compromise, No Surrender) |
| Legacy of the Legion | Winter attrition −5%; cold acclimatization gain factor +5%; retreating divisions speed +5%; army experience from volunteers +5%; Winter Specialist trait XP gain +10% | Czechoslovakia starts with this (Peace for Our Time) |

### Army — Spirit of Division Command (50 army XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Static Warfare | Entrenchment speed +10%; max entrenchment +10%; +100% additional chance for preferred tactic Elastic Defense | Grand Battle Plan or Great War Infantry |
| Flexible Organization | Division speed +5%; org loss when moving −15%; preferred-tactic selection cost −15 | Mobile Warfare or Infiltration Tactics |
| Aggressive Reconnaissance | Reconnaissance +15%; intelligence gained from combat +15%; +100% additional chance for Infiltration Assault | Mobile Warfare |
| Reserve Officers | Division training time −15% | Superior Firepower |
| Victory or Death | Organization loss when below 25% −15%; +100% additional chance for Mass Charge | Mass Assault |
| Maneuver Warfare | Division speed +5%; coordination +5%; +100% additional chance for Unexpected Thrust | Mobile Warfare |
| Smoke and Fire | Breakthrough +6%; +100% additional chance for Suppressive Barrage | Superior Firepower |
| Logistical Focus | Supply consumption −10%; navy/air fuel consumption −10%; +100% additional chance for Well-Planned Attack | Grand Battle Plan |
| Operational Reserves | HP +10%; +100% additional chance for Relentless Assault | Mass Assault |
| All-Arms Anti-tank Defense | Infantry equipment hard attack +25%; +100% additional chance for Tactical Withdrawal | Superior Firepower or Tank Destroyer Force (No Compromise, No Surrender) |
| Direct Fire Support | Light/Medium/Heavy/Modern SP Artillery hard attack +50%, piercing +100%; +100% additional chance for Overwhelming Fire | Superior Firepower or Self-propelled Support (No Compromise, No Surrender) |
| Rapid Emplacement | Towed Artillery/AA/AT and Towed & Motorized Rocket Artillery: breakthrough +10%, defense +10%; +100% additional chance for Breakthrough tactic | Superior Firepower or Flying Batteries (No Compromise, No Surrender) |
| Quick Improvisation | Planning speed +20%; daily command power gain +0.20; commander ability cost −20% | Mobile Warfare |

### Navy — Spirit of Naval Academy (20 navy XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Instilled Aggression | Admirals: 50% chance of +1 Attack on level up | — |
| Calculated Restraint | Admirals: 50% chance of +1 Defense on level up | — |
| Signals Training | Admirals: 50% chance of +1 Maneuvering and +1 Coordination on level up | — |
| Grand Fleet | Superior Tactician and Ironside trait XP gain +20%; new admirals 50% chance to start with Gunnery Expert | Fleet In Being |
| Convoy Warfare | Sea Wolf and Blockade Runner trait XP gain +20%; new admirals 50% chance to start with Sea Wolf or Blockade Runner (equal weight) | Trade Interdiction |
| Integrated Air Arm | Fleet Protector and Air Controller trait XP gain +20%; new admirals 50% chance to start with Aviation Enthusiast | Base Strike |
| Best of the Best | Starting level of new navy leaders +2; navy intelligence to others −5%; new admirals gain no personality traits | — |
| Academy Scholarships | Navy leader cost −40%; starting level of new navy leaders +1; new admirals gain no personality traits | — |
| Ship to Shore Training | Shore bombardment collateral damage +50%; Ironside trait XP gain +35% | Base Strike or Naval Gunfire Support (No Compromise, No Surrender) |
| Stay at your Posts | Accident chance −15%; Blockade Runner trait XP gain +35% | Trade Interdiction or Screen Support Focus (No Compromise, No Surrender) |

### Navy — Spirit of the Navy (35 navy XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Jeune École | Destroyer research speed +20%; light ship design cost −60% | Trade Interdiction or The New School |
| Flexible Contracts | Cruiser design cost −60%; naval MIO cost −80% | — |
| Integrated Designers | Ship module research speed +20% | Trade Interdiction |
| Naval Reform | Naval doctrine Mastery gain +10% | Base Strike |
| Naval Refit Yards | Ship refitting speed +25%; ship repair speed +15% | Fleet In Being |
| Global Presence | Battleship and heavy cruiser research speed +20%; heavy ship design cost −60% | Fleet In Being |
| Submarine Primacy | Submarine research speed +20%; submarine design cost −60% | Trade Interdiction |
| Mobile Force | Carrier research speed +20%; carrier design cost −60% | Base Strike |
| Sea Lane Denial | Minelaying research +30%; naval minelaying efficiency +15% | Trade Interdiction or Coastal Minelaying (No Compromise, No Surrender) |
| Fleet Interoperability | Naval research speed +5%; ship recovery rate +20% | No Compromise, No Surrender |

### Navy — Spirit of Naval Command (50 navy XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Close Combat | Screen attack +5%; torpedo screen penetration +5% | Trade Interdiction |
| Night Fighting | Night-time attack +10%; night-time spotting +10%; visibility −5% | Torpedo Primacy or Base Strike |
| Surprise Attacks | Retreat chance after initial stage +10%; retreat speed after initial stage +10% | Base Strike or Massed Carrier Fleet |
| Efficient Communications | Positioning +15% | Fleet In Being or Line of Battle |
| Surface Raiders | Retreat decision chance +10%; fleet speed while retreating +10%; screening bonus when using only capital ships +20% | Trade Interdiction or Armored Raiders |
| Decisive Battle | Naval hit chance +10%; retreat decision chance −10%; fleet speed while retreating −10%; torpedo hit chance +10% | Fleet In Being |
| Inclement Weather Experience | Bad weather penalty −40% | Trade Interdiction |
| Brave Commanders | Retreat decision chance −5%; chance to score critical hit +15% | Fleet In Being or Capital Hunters |
| Bureau of Ordnance | Torpedo hit chance −10% | United States starts with this |
| Naval Tripwire | Enemy fleet size penalty +20% | Trade Interdiction or Coastal Defense Fleet (No Compromise, No Surrender) |
| Scouting Force | Naval detection +10%; spotting speed +10% | Fleet In Being or Escort Carrier Support (No Compromise, No Surrender) |
| Fleet Defense | Screening efficiency +10%; fighter sortie efficiency +10% | Base Strike or Light Task Forces (No Compromise, No Surrender) |
| Rapid Concentration | Fleet coordination +15% | Base Strike or Fast Battleships (No Compromise, No Surrender) |
| Anti-aircraft Curtain | Naval AA attack +15% | Fleet In Being or Anti-Aircraft Battleships (No Compromise, No Surrender) |
| Selective Engagement | Visibility −10% | Trade Interdiction or Patrol Boats (No Compromise, No Surrender) |

### Air — Spirit of the Air Force (50 air XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Independent Air Force | Air advisor cost −75% | — |
| Industrial Destruction | Heavy aircraft research speed +5%; large plane design cost −75% | Strategic Destruction |
| Dive Bombing | CAS research speed +5%; small CAS airframe and small CAS carrier airframe design cost −75% | Battlefield Support |
| Material Destruction | Tactical bomber research speed +5%; medium plane design cost −75% | Operational Integrity |
| Industry Liasons | Light, medium and heavy aircraft research speed +15% each | — |
| Effective Training Programs | Air wing training experience gain +25% | — |
| Branch Independence Spirit | Air experience daily gain +0.10; airforce intelligence to others −5% | — |
| Air Crew Surveys | Air accident chance −25%; air doctrine Mastery gain factor +5% | — |

### Air — Spirit of Air Force Command (50 air XP each)

| Spirit | Effects | Prerequisites |
|---|---|---|
| Battlefield Air Interdiction | Escort efficiency +5%; ground attack factor +5% | — |
| CAG Night Fighting | Carrier night traffic +50%; carrier night penalty reduction +25% | United Kingdom |
| Veteran Air Instructors | Air wing experience loss when killed −25% | — |
| Centralized Control | Fighter detection +10%; air mission efficiency +10% | — |
| Steel Wings, Steel Hearts | Untrained pilots penalty for new air wings −33% | Communist |
| Airborne Heroes | Ace effectiveness +50% | — |
| Air Power Projection | Air power projection factor +10% | — |
| Massed Strike | Air superiority +5% | Operational Integrity |
| Continuous Strike | Air support mission efficiency +25% | Battlefield Support |
| Total Devastation | Strategic bombing +10% | Strategic Destruction |

## Commanders

### Hiring

- **Generals:** 5 CP per existing general, capped at 80 CP.
- **Admirals:** 5 CP per existing admiral, capped at 80 CP.
- New generals and admirals: **95% chance to start at skill level 1, 5% chance at level 2** — improved by Academy Scholarships and Best of the Best spirits.
- Commanders **cannot die or be dismissed** in normal play; some country-specific events remove historical commanders.
- **With By Blood Alone**, new generals are **promoted from divisional commanders** rather than randomly generated. The promoted officer's division loses **25% of its experience** (fully negated by the **Accomplished Heritage** spirit) and generates a replacement officer. The promoted officer keeps their divisional experience; with **≥400 experience** at promotion they also randomly gain a trait such as Infantry Officer, Cavalry Officer, Armor Officer or Engineer Officer, based on the battalions and support companies in their division.

### General vs field marshal vs admiral — unit limits

| Rank | Command limit | Penalty above the limit |
|---|---|---|
| General | **24 divisions**; **72 divisions** in Garrison Area mode (limit tripled) | Bonuses and XP gain reduced proportionally; the XP penalty reaches **100% at twice the limit** |
| Field marshal | **5 armies**, raised to **7** with Expert Delegator | — |
| Admiral | **10 task forces** | Bonuses and XP gain reduced proportionally |

- Promoting a general to field marshal costs **40 CP** and inflicts a temporary loss of one skill level (**Recently Promoted**: −1 to all four skills, expires after 100 days).
- **General traits and the field marshal's skill levels pass down to subordinate armies at 50% effect.** Personality-trait modifiers (Cautious, Old Guard, …) pass down at **full** effect.
- A field marshal used as an ordinary army commander has their field-marshal traits disabled, but flat skill bonuses from those traits (e.g. the +1 Attack from Offensive Doctrine) still apply.
- **Skilled Staffer** gives General Max Army Size +6 — this does *not* apply to field marshals.
- **Expeditionary Leader** (Australian generals) gives General Max Army Size −18 and General Max Army Group Size −4.

### Divisional commanders (officers)

- Every division always has a divisional commander. Purely flavour without By Blood Alone.
- They can accrue up to **8,000 experience**; that experience gives no benefit until promotion.
- With By Blood Alone they gain **4% of the experience their division earns in combat**, **+10% per medal the division holds**. They gain nothing from training. Their experience is **not lost** when the division takes manpower losses.
- Base game: **0% chance** a divisional commander is a woman (moddable).

### Skill levels

Experience required to reach each level:

| Level | General | Field Marshal | Officer (By Blood Alone) | Admiral | Admiral hit chance | Admiral coordination |
|---|---|---|---|---|---|---|
| 1 | 100 | 100 | 100 | 100 | +5% | +1% |
| 2 | 300 | 300 | 200 | 200 | +10% | +3% |
| 3 | 500 | 500 | 400 | 400 | +15% | +5% |
| 4 | 1000 | 1000 | 800 | 800 | +20% | +7% |
| 5 | 1500 | 1500 | — | 1600 | +25% | +9% |
| 6 | 2500 | 2500 | — | 3200 | +30% | +11% |
| 7 | 5000 | 5000 | — | 6400 | +35% | +13% |
| 8 | 7500 | 7500 | — | 12800 | +40% | +15% |
| 9 | 10000 | 10000 | — | 25600 | +45% | +17% |

Only **admirals** get a direct benefit from the generic skill level (the hit-chance and coordination columns above).

### Specialised skills

| General / field marshal skill | Effect per level |
|---|---|
| Attack | +2.5% soft attack and hard attack |
| Defense | +2.5% defense and breakthrough |
| Logistics | −2.5% supply consumption |
| Planning | +5% planning speed, +2% max planning |

| Admiral skill | Effect per level |
|---|---|
| Attack | +5% damage to enemy ships |
| Defense | +5% (ship armor up, enemy damage down) |
| Maneuvering | +1% fleet speed while retreating, +2.5% positioning |
| Coordination | Fleet coordination = (Level × 2) − 1 % |

Divisional commanders' skill levels give their division no benefit.

### Skill factor (level-up point distribution)

- On level-up a commander gains **3 points** spread randomly across the four specialised skills; the same skill can be hit multiple times.
- Default weights are **5 / 5 / 5 / 5** for both generals (Attack/Defense/Logistics/Planning) and admirals (Attack/Defense/Maneuvering/Coordination). Traits like Brilliant Strategist or Media Personality shift these weights.
- Academy spirits (Bold Attack, Signals Training, …) add **extra** points on top of the 3, and also apply when a focus grants a skill level.

## Commander abilities

All abilities cost CP scaled by the number of battalions under the commander.

| Ability | Effect on all divisions | Duration | Cooldown | CP per battalion | Availability |
|---|---|---|---|---|---|
| Extra Supplies | Supply grace +168 h; immediately adds 2 days of supplies | 7 days | 21 days | 0.20 | Commanders with Logistics Wizard (except British Raj after Quinine and Australia after its anti-malaria campaign) |
| Supply Quinine | Supply grace +240 h; attrition −12%; commander sickness chance −100%; heat attrition factor −35%; immediately adds 3 days of supplies | 10 days | 21 days | 0.15 | All British Raj commanders after Quinine; all Australian commanders after the anti-malaria campaign |
| Staff Office Plan | Planning speed +400% | 7 days | — | 0.12 | All commanders except Japan's after The Art of Warfare |
| Staff Office Plan (Japan) | Planning speed +400% | 9 days | — | 0.06 | All Japanese commanders after The Art of Warfare |
| Force Attack | Attack +20%; breakthrough +25%; org damage taken −100%; strength damage taken +60%; war support reduction on damaged +20%; cannot retreat while attacking | 7 days | — | 0.22 | All generals (except the upgraded Chinese/Japanese versions below) |
| Force Attack (upgrade) | Attack +25%; breakthrough +25%; org damage taken −100%; strength damage taken +25%; war support reduction on damaged +20%; cannot retreat while attacking | 7 days | — | 0.11 | China after Dare-to-Die Corps; Japan after its Banzai focuses |
| Force Attack (China) | As base Force Attack, plus does not lose entrenchment on attacking | 7 days | — | 0.22 | China after Know Thy Enemy |
| Last Stand | Defense +20%; entrenchment +25%; org damage taken −100%; strength damage taken +60%; war support reduction on damaged +20%; cannot retreat while defending | 7 days | — | 0.22 | All generals (except the upgraded versions) |
| Last Stand (upgrade) | Defense +20%; entrenchment +25%; org damage taken −100%; strength damage taken +60%; cannot retreat while defending | 7 days | — | 0.05 | Japan after Warrior Spirit; Nationalist Spain after Cultivate Fanaticism |
| Last Stand (Japan) | Same as upgrade | 10 days | — | 0.05 | Japan after Senjinkun Military Code or Indoctrination in the Military Academy |
| Last Stand (Sweden) | Defense +20%; entrenchment +25%; org damage taken −100%; strength damage taken +60%; war support reduction on damaged +20%; cannot retreat while defending | 7 days | — | 0.16 | Sweden after Winter Drill |
| Last Stand (Philippines) | Defense +25% (rest as Sweden version) | 7 days | — | 0.16 | Philippines after Utang na loob |
| Probing Attack | Attack −20%; keeps entrenchment while attacking | 7 days | — | 0.10 | Skirmisher trait |
| Siege Artillery | Fort damage from combat +200%; fort damage chance from combat +200%; fort attack +20% | 7 days | — | 0.10 | Fortress Buster trait |
| Glider Planes | Paratrooper transport space factor −10%; paratrooper organization after paradropping +200%; paratrooper AA defense +50% | 7 days | — | 0.10 | Paratroopers trait |
| Makeshift Bridges | River crossing speed penalty −40%; river attack +20% | 7 days | — | 0.10 | Improvisation Expert trait |
| Naval Assault Plan | Naval invasion preparation speed +50% | 7 days | — | 0.10 | Amphibious trait |
| Requisition Winter Gear | Cold weather acclimatization factor +50% | 7 days | — | 0.10 | Not available to anyone in-game |
| Stockpile Medical Supplies | Casualty trickleback +4% | 14 days | — | 0.22 | Deployed Army HQ with "Hospital Group Staff" division |
| Prepare Fallback Positions | Entrenchment speed +6 | 7 days | — | 0.12 | Deployed Army HQ with "Engineer Staff" division |
| Defense in Depth | Max planning −50%; max entrenchment +3 | Until cancelled | — | 0.10 | Deployed Army HQ with "Reconnaissance Staff" division |
| Exploit Breakthroughs | Org loss when moving −10%; plan preparation decay rate −20%; strength damage taken +40% | Until cancelled | — | 0.10 | Deployed Army HQ with "Logistics & Service Staff" division |
| Rotating Reserves | Reinforcement rate +6% | 7 days | — | 0.12 | Deployed Army HQ with "Signal & Intelligence Staff" division |

## Commander experience

General XP per hour of battle is built from:

- **Base value: 0.45.**
- **Division count:** each actively fighting division counts as **10%**. Divisions with fewer than 8 battalions + support companies count proportionally less (a 3-battalion division counts as 3.75%).
- **Damage comparison** (HP + organization dealt over the last 24 h): the side dealing more damage gets up to **400% of normal XP** (when dealing up to 400% as much damage as it took); the side dealing less has its XP scaled by the average equipment ratio × average organization ratio of its divisions including reserves (all divisions at half strength and half org → 25%). The two effects do not stack — each side gets one.
- **Decay:** XP gain decays linearly by **0.125% per combat hour**, bottoming out at **10% after 30 days**.
- **Multiple generals on one side:** each gets **50% + 50%/n** — 100%, 75%, 67% for 1, 2, 3 generals.
- **Command-limit penalty:** scales up to **100% at twice the normal limit**.
- **Modifiers:** national ideas and leader traits (Old Guard, Politically Connected …) stack **additively**.

Flat awards: **35 XP for overrunning** units and **35 XP for shattering** them.

A field marshal above a general also gains **30% of that general's experience**, including toward traits, but gains nothing from units that have no general.

| XP type | Division-combat-hours required per XP |
|---|---|
| General trait | 25 |
| General level | 50 |
| Field marshal trait | 200 |
| Field marshal level | 400 |

## Commander traits

### General / field marshal — personality traits

Cannot be earned through experience; generally do **not** affect subordinate leaders, and are the only traits that appear on newly hired generals.

| Trait | Personal modifier | Modifier | Skill | Skill factor | Notes |
|---|---|---|---|---|---|
| Old Guard | Experience gain −25% | Max entrenchment +1 | — | — | — |
| Brilliant Strategist | — | — | Attack +1, Planning +1 | Attack +1, Planning +1 | +25% chance on new leaders with Theatre Training |
| Inflexible Strategist | — | — | Defense +1, Logistics +1 | Defense +1, Logistics +1 | +25% chance on new leaders with Theatre Training |
| Politically Connected | Experience gain −10%, promotion cost −50% | — | — | Planning +1, Logistics +1 | +50% chance with Political Loyalty (guaranteed if Media Personality does not appear) |
| Brave | — | Division org loss when below 25% −10% | Defense +1 | — | British Raj after Sikh Religious Guarantees |
| War Hero | Promotion cost −50%, reassignment duration +50% | — | — | Attack +1, Planning +1 | Never appears randomly |
| Career Officer | Promotion cost −25% | — | — | Planning +1, Logistics +1 | — |
| Cautious | Chance to be wounded −50% | Planning speed −20% | — | Defense +1, Logistics +1 | — |
| Reckless | Chance to be wounded +50% | Planning speed +20% | — | Attack +1, Defense −1, Planning +1 | — |
| Media Personality | Reassignment duration +100% | — | — | Attack +1, Defense +1 | +50% chance with Political Loyalty (guaranteed if Politically Connected does not appear) |
| Harsh Leader | — | Division recovery rate −10% | Attack +1 | Attack +1, Logistics +1 | — |
| Bearer of Artillery | — | Artillery attack +15% | — | — | Only Wojtek, via the "Wojtek Never Drops A Crate" event |
| Infantry Officer | Infantry Leader XP factor +100% | — | — | Defense +1, Planning +1 | 50% chance on new generals with The Queen of Battle |
| Cavalry Officer | Cavalry Leader XP factor +100% | — | — | Attack +1, Logistics +1 | Cannot appear on new generals with By Blood Alone |
| Armor Officer | Panzer Leader XP factor +100% | — | — | Attack +1, Planning +1 | 50% chance with Embrace the Future (without By Blood Alone) |
| Engineer Officer | Engineer XP factor +100% | — | — | Attack +1, Planning +1 | 50% chance on new generals with Engineering Schools |
| Irregulars Officer | — | Non-combat out-of-supply penalties −10%; cavalry & camelry speed +5%; irregular infantry attack +5%; desert movement +10% | — | Attack +1, Planning +1 | Italy and Ethiopia |
| Ascari Officer | — | Cavalry, camelry and infantry defense +5%; desert defense +5% | — | Defense +1, Logistics +1 | Italy; guaranteed after Strengthen Ascari Corps or Forza Navale Speciale |
| Militia Officer | — | Militia defense +5%, militia speed +5%, militia organization +5% | — | Defense +1, Planning +1 | Switzerland (guaranteed); Italy, Germany; Finland/Sweden (AAT); Chile (guaranteed)/Brazil (ToA); Austria, Belgian Congo, Hungary (Götterdämmerung) |
| Cowed by Stalin | — | Division recovery rate −10%, reinforce rate −2% | Attack −2, Defense −2 | — | Soviet Union (NSB) purge events; removed by Lessons of War |
| Veteran Jaeger | Trickster, Winter Specialist, Commando, Swamp Fox, Ranger, Hill Fighter, Urban Assault Specialist and Invader XP factor +100% | Equipment capture ratio gain +3% | — | Attack +1, Logistics +1 | Finland (Arms Against Tyranny); never random |
| Promoted away from power | — | Attrition +4%, supply factor −5% | Planning −1, Logistics −1 | — | Sweden after Prevent a Counter-Revolution |
| Hero of Ethiopia | — | Organization +10%, infantry defense +5% | — | — | Ethiopia after Promote the War Heroes |
| Promoted from the Ranks | Promotion cost −50%, planning speed +10% | Reconnaissance +5% | — | — | Not attainable in-game |
| Inspirational Bagpiper | Chance to be wounded +65% | Division experience gain +10%, division HP +10% | — | — | United Kingdom; never random |
| Samurai Lineage | Planning speed +5%, chance to be wounded +10%, promotion cost −20% | — | — | — | Japan; stays loyal to the imperial faction in civil wars; never random |
| Expeditionary Leader | — | Division attack and defense on non-core territory +10% each; General Max Army Size −18; General Max Army Group Size −4 | — | — | Certain Australian generals; never random |
| Exiled Leader | — | Exiled divisions attack +10%, own exiled divisions attack +5%; exiled divisions defense +10%, own exiled divisions defense +5% | — | — | Commanders from hosting governments-in-exile |

### General — earned traits

Earned by accumulating trait-specific combat experience. **Each earned trait already held halves the gain rate for the rest** (half speed with one, one third with two, and so on).

| Trait | Effect | Experience gained while | XP required |
|---|---|---|---|
| Organizer | Planning speed +10% | Using a battle plan at army level (field marshal plans do not progress it) | 1000 |
| Cavalry Leader | Cavalry, motorized and mechanized attack +12% each | Cavalry + motorized + mechanized ratio > 40% | 1000 |
| Infantry Leader | Infantry division defense +13% | Infantry ratio > 80% | 1000 |
| Skilled Staffer | General Max Army Size +6 (not applied to field marshals); +2 logistics skill factor | Controlling at least 24 divisions | 2000 |
| Trickster | Reconnaissance +25% | Flanking the enemy or being flanked | 500 |
| Winter Specialist | Winter attrition −50% | Temperature below −10 °C | 500 |
| Engineer | River attack +5%, fort attack +10% | Combat has the Fort or River-crossing modifier | 700 |
| Panzer Leader | Armor speed +5%, armor division attack +16%; +2 attack skill factor | Armored ratio > 40% | 700 |
| Commando | Out of supply penalty −25% | Temperature below −15 or above 27; or combat has Paradrop or Naval Penalty modifier | 700 |
| Desert Fox | Desert: movement +5%, attack +10%, defense +10% | Fighting in Desert | 700 |
| Swamp Fox | Marsh: movement +5%, attack +10%, defense +10% | Fighting in Marsh | 700 |
| Mountaineer | Mountain: movement +5%, attack +10%, defense +10% | Fighting in Mountain | 700 |
| Hill Fighter | Hills: movement +5%, attack +10%, defense +10% | Fighting in Hills | 700 |
| Jungle Rat | Jungle: movement +5%, attack +10%, defense +10% | Fighting in Jungle | 700 |
| Ranger | Forest: movement +5%, attack +10%, defense +10% | Fighting in Forest | 700 |
| Urban Assault Specialist | Urban: movement +5%, attack +10%, defense +10% | Fighting in Urban | 500 |
| Invader | Amphibious invasion speed +30%, invasion preparation time −30% | Performing an amphibious invasion | 100 |

### Assignable traits — field marshal (15 CP each)

| Trait | Effect | Prerequisite trait | Exclusive with |
|---|---|---|---|
| Logistics Wizard | Supply consumption −15%; enables Extra Supplies ability | Organizer | — |
| Offensive Doctrine | Org loss when moving −30%; Attack skill +1 | — | Defensive Doctrine |
| Defensive Doctrine | Max entrenchment +30% | — | Offensive Doctrine |
| Fast Planner | Planning speed +25% | Organizer | Thorough Planner |
| Thorough Planner | Max planning +10% | Organizer | Fast Planner |
| Unyielding Defender | Defense +10%; increased chance of the Counter-Attack tactic | Inflexible Strategist | Aggressive Assaulter |
| Aggressive Assaulter | Breakthrough +10%; increased chance of Assault and Shock tactics | Brilliant Strategist | Unyielding Defender |
| Organization First | Reinforce rate +2% | — | — |
| Charismatic | Division recovery rate +10% | — | — |
| Expert Delegator | Field Marshal Max Army Group Size +2 | Skilled Staffer | — |

### Assignable traits — general (15 CP each)

| Trait | Effect | Prerequisite trait | Exclusive with |
|---|---|---|---|
| Panzer Expert | Armor division defense +10%; increased chance of Blitz and Encirclement tactics | Panzer Leader | Combined Arms Expert, Cavalry Expert |
| Combined Arms Expert | Motorized and mechanized defense +15% each; increased chance of Blitz and Encirclement | Panzer Leader or Cavalry Leader | Panzer Expert, Cavalry Expert |
| Cavalry Expert | Cavalry defense +10% | Cavalry Leader | Panzer Expert, Combined Arms Expert |
| Fortress Buster | Fort attack +15%; enables Siege Artillery ability | Engineer | Scavenger |
| Scavenger | Equipment capture ratio gain +3% | Engineer | Fortress Buster |
| Infantry Expert | Infantry division attack +10% | Infantry Leader | Ambusher |
| Ambusher | Max entrenchment +5.0; recon bonus while entrenched +25% | Infantry Leader | Infantry Expert |
| Amphibious | Extra marine supply grace +240 h; enables Naval Assault Plan ability | Invader | — |
| Naval Liaison | Shore bombardment bonus +25% | Invader | — |
| Skirmisher | Enables Probing Attack ability | Commando | — |
| Paratroopers | Extra paratrooper supply grace +240 h; enables Glider Planes ability | Commando | — |
| Camouflage Expert | Damage reduction against CAS +50%; enemy air support (CAS) bonus in combat −50% | Commando | — |
| Improvisation Expert | Movement bonus on land +10%; enables Makeshift Bridges ability | Trickster + at least one terrain trait | — |
| Guerilla Fighter | Entrenchment speed +50% | Trickster | — |
| Adaptable | Terrain penalty reduction +30% (applied after summing all other terrain modifiers; not applied to terrain features); cold and hot acclimation gain factor +10% each | At least two terrain traits | — |
| Winter Expert | Cold acclimation gain factor +40% | Winter Specialist | — |

### General — status traits (temporary)

| Trait | Effect | How gained / duration |
|---|---|---|
| Sick | Skill bonus factor −50%; cannot use abilities | Random for commanders not sick in the past 180 days when 75% of their divisions are in Jungle, Marsh or Desert. **2% base chance per day.** Expires after 30 days |
| Wounded | Skill bonus factor −50%; cannot use abilities | Random after winning or losing a battle: **0.1% if won, 0.5% if lost** (modifiable by traits). Expires after 90 days |
| Reassigned | Skill bonus factor −100%; cannot use abilities | Nationalist Spain's reassigned commanders at the start of the Spanish Civil War (La Résistance); expires after 60 days. Also 2 Siamese commanders for 4 years after Sideline Disloyal Officers |
| Recently Promoted | Attack −1, Defense −1, Planning −1, Logistics −1 | Gained on promotion to field marshal; expires after 100 days |
| Motivated | Division recovery rate +10%; Attack +1 | Completing the faction goal Subjugate the Faction; expires after 270 days |
| Wounded by Rioters | Skill bonus factor −75%; cannot use abilities | Sweden's Hungersköld low-stability riots (Arms Against Tyranny); expires after 120 days |
| Disillusioned with the government | Attack −3, Defense −3, Planning −3, Logistics −3 | Same Swedish riots; expires after 270 days |
| Determined | Attack +1, Defense +1 | Soviet Agitprop decision (NSB); British Raj (Graveyard of Empires); Indonesia and Siam (Thunder at Our Gates) |
| Substance Abuser | — | Japan |
| Substance Addict | Attack −2, Defense −2, Planning −2, Logistics −2 | Graveyard of Empires: after British Raj completes Third Opium War and at least one country accepts the opium trade. In practice only the Japanese commander with Substance Abuser can get it |
| Hidden Sympathies | — | Random owned general after the Lower Army Command Loyalty decision; these generals join the player's side in the civil war |
| Disgruntled | Attack −2, Defense −2, Planning −2, Logistics −2 | Not used by the game |
| Demoted | Attack −1, Defense −1, Planning −1, Logistics −1 | Not used by the game |

### Admiral — personality traits

| Trait | Effect | Notes |
|---|---|---|
| Old Guard | Leader experience gain −25% | — |
| Gentlemanly | Navy organization +5; enemy retreat chance +20% | — |
| Gunnery Expert | Ironside XP factor +100% | +50% chance on new leaders with Grand Fleet |
| Cuts Corners | Damage +20%, defense −10% | — |
| Chief Engineer | Chance to receive critical hit −5% | — |
| Media Personality | +10% fleet attack and defense while commanding the Pride of the Fleet | — |
| Bold | Naval speed +10%, damage +5% | — |
| Career Officer | Commander experience gain +10% | — |
| Battleship Adherent | Naval AA attack −20%; capital ship attack +10% | — |
| Aviation Enthusiast | Air Controller XP factor +100% | +50% chance on new leaders with Integrated Air Arm |
| Caustic Personality | Number of ships in first contact −25% | — |
| Craven | Retreat decision chance +25%; damage −5% | — |
| Naval Lineage | Number of ships in first contact +25%; retreat decision chance −25% | — |
| Cowed by Stalin | Retreat decision chance −25%; Attack −2, Defense −2 | Soviet Union (NSB); removed by Lessons of War |

### Admiral — earned traits

| Trait | Effect | Experience gained while | XP required |
|---|---|---|---|
| Blockade Runner | Retreat decision chance +20%; fleet speed while retreating +15%; convoy speed while retreating +5% | Task force in combat where every ship exceeds 32 knots | 500 |
| Sea Wolf | Submarine attack +20% | More than 80% submarines in fleet | 700 |
| Spotter | Spotting speed +10% | Spotting the enemy | 500 |
| Fleet Protector | Screening efficiency +20% | More than 50% screening vessels in fleet | 500 |
| Superior Tactician | Positioning +25% | Having the advantage in combat | 500 |
| Air Controller | Sortie efficiency +10%; naval air targeting from carriers +10% | Carrier with air wings on mission, or its air wings in the combat | 500 |
| Ironside | Capital ship armor +10% | Commanding or fighting capital ships | 500 |
| Cold Water Expert | Attrition −8% | Weather is Arctic Water | 1000 |
| Inshore Fighter | Fjords and Archipelagos: movement +10%, attack +10%, defense +10% | Fighting in Fjords and Archipelagos | 1000 |
| Blue Water Expert | Deep Ocean: movement +10%, attack +10%, defense +10% | Fighting in Deep Ocean | 1000 |
| Green Water Expert | Shallow Sea: movement +10%, attack +10%, defense +10% | Fighting in Shallow Sea | 1000 |

### Admiral — assignable traits (15 CP each)

No experience requirement; the number of assignable traits depends on the admiral's level.

| Trait | Effect | Prerequisite trait | Exclusive with |
|---|---|---|---|
| Concealment Expert | Visibility −10% | Blockade Runner | Lone Wolf |
| Lone Wolf | Enemy fleet size penalty +10% | Blockade Runner | Concealment Expert |
| Silent Hunter | Torpedo reveal chance −15% | Sea Wolf | Lancer |
| Lancer | Torpedo screen penetration +25% | Sea Wolf, Spotter, Fleet Protector or Superior Tactician | Silent Hunter |
| Search Pattern Expert | Spotting speed +20% | Spotter or Fleet Protector | — |
| Destroyer Leader | Destroyers: visibility −10%, naval damage +10%, torpedo hit chance +10% | Fleet Protector or Superior Tactician | — |
| Cruiser Captain | Light and heavy cruisers: naval speed +10%, naval damage +10% | Fleet Protector or Superior Tactician | — |
| Mine Craft | Naval minelaying efficiency +25%; minesweeping efficiency +25%; mine avoidance +25% | Superior Tactician | — |
| Flight Deck Manager | Sortie efficiency +10% | Air Controller | — |
| Ground Pounder | Shore bombardment bonus +25% | Ironside | — |
| Big Guns Expert | Capital ship attack +15% | Ironside | — |
| Safety First | Chance to receive critical hit −25% | Ironside | — |
| Smoke Screen Specialist | Retreat decision chance +25% | Lone Wolf or Concealment Expert | — |
| Torpedo Expert | Torpedo hit chance +10% | Silent Hunter or Lancer | — |
| Loading Drill Master | Torpedo cooldown −25% | Silent Hunter or Lancer | — |
| Hunter-Killer | Submarine attack +10%; submarine detection +20% | Destroyer Leader or Search Pattern Expert | — |
| Fly Swatter | Naval AA attack +10% | Destroyer Leader or Cruiser Captain | — |
| Fighter Director | Fighter sortie efficiency +20% | Flight Deck Manager | Dive Bomber, Torpedo Bomber |
| Dive Bomber | Carrier CAS: air support mission efficiency +10%, ground attack factor +10% | Flight Deck Manager | Fighter Director, Torpedo Bomber |
| Torpedo Bomber | Carrier naval bombers: naval mission efficiency +10%, naval bombing +10%, naval targeting +5% | Flight Deck Manager | Fighter Director, Dive Bomber |
| Marksman | Chance to score critical hit +10% | Big Guns Expert | Crisis Magician |
| Crisis Magician | Effects of sustained critical hits −50% | Safety First | Marksman |

### Political traits

Political traits have **no direct combat effect**. They mainly decide which side a leader takes in a civil war, and which leaders certain focuses affect. Examples: Nationalist Sympathies, Falangist Loyalties, Carlist Loyalties, Republican Loyalties, Stalinist Loyalties and Anti-Stalinist Loyalties (Spain, La Résistance); Zveno Member, Tsar Loyalist, Fatherland Front Sympathizer (Bulgaria, BftB); Kemalist Champion (Turkey, BftB); Staunch Monarchist, Venezelist Loyalist, Marxist Acolyte, Fascist Sympathizer (Greece, BftB); Veteran Anti-Bolshevik and Communist Sympathizer (Baltics, NSB); Sanation Left/Right Leader, Peasant Sympathiser (Poland, NSB); Monarchist Sympathizer, Stalinist, Trotskyist, Bukharinist, Foreign Military Advisor (Soviet Union, NSB); Commander in Chief (Switzerland, BBA); Fascist Sympathizer and Vitéz (Hungary, Götterdämmerung); Kodoha Sympathiser, Royal Lineage, Tōhōkai Sympathies, Army Loyalist, Civilian Government Supporter (Japan); Loyalty to Britain / Pakistan / India (British Raj, Graveyard of Empires); Golden Square Member (Iraq, Graveyard of Empires); Survivor of the Long March and Dubious Loyalty (Chinese tags, No Compromise No Surrender); Russian Empire Veteran (not attainable).

## Command groups

A command group is a set of divisions under one commander — an **army** (general) or an **army group** (field marshal). Command groups are tied to the theatre they operate in, and can be given custom colours and insignia.

### Exercising

- Any command group can exercise. Divisions gain unit experience up to **Regular**; the country gains army experience whenever exercising divisions are Trained or better.
- Commanders gain **no** experience from exercising, only from combat.
- Exercising divisions take **+5% equipment attrition** and their organization is set to **20%**, recovering over roughly a week after stopping.
- Shift-clicking the exercise order auto-cancels it when all troops reach Regular.

Country army-XP gain from exercising, simple case (fully equipped, fully fuelled, no training modifiers, division count unchanged recently):

```
experience = B/10 × S / C(today) = 0.093 × B / C(today)
```
- **B** = battalions + support companies in the division
- **S** = daily experience per division = **0.093**
- **C(day)** = number of divisions in the field and in training that day

General form:

```
interpolated division count(day) = max( C(day),
    interpolated count(prev day) + (C(day) − interpolated count(prev day)) × I − D )

experience = B/10 × S × T × F × R / interpolated division count(day)
```
- **T** = country training-time modifier (e.g. from Extensive Conscription)
- **F** = fuel factor, 0–1, from fuel availability in the division
- **R** = division's fighting strength ratio (reduced by missing manpower or equipment)
- **I** = interpolation factor = **0.002**
- **D** = interpolation decrease = **0.1**

## Army planner (Recruit & Deploy, hotkey U)

- Deployments are created from division templates ("Train"); "Add Unit" trains multiple in parallel, the number above trains sequentially. A spawn location must be chosen and, optionally, a command group or order to join on spawn.
- **A country may only train divisions requiring in total 75% of its currently fielded manpower, or 100,000 manpower — whichever is higher.**
- Finished divisions deploy at **Trained** (no combat modifier). A division that has passed the **20% minimum training level** can be deployed early at **Green** (−25% combat modifier). Exercising afterwards raises them to **Regular** (+25%).
- **Reinforcements:** manpower arrives in chunks of **10% of the division's maximum manpower** (less if the free pool is short). Delivery speed is **10 manpower per hour × the supply area's reinforcement delivery speed** (normally close to 1).
- **Lend-lease always has the highest equipment priority**, above everything else; changes require a diplomatic action.
- Deployments, reinforcements and upgrades each get a low / medium / high priority for equipment allocation during shortages.
- Division templates can be set to *downgrade* equipment (old small arms for garrison or training divisions), freeing modern equipment. **Changing a template's equipment authorisation costs no experience.**

## Battle plans

### Orders

| Order | Purpose |
|---|---|
| Front Line (Z) | Assembly line for an offensive; can be a whole border or a dragged sub-section. Divisions on a front line bordering a non-ally accumulate the **planning bonus** |
| Offensive Line (X) | The line/arrow drawn into enemy territory that the AI advances toward. Width and arc adjustable; ALT = edit mode, TAB shifts the arrow base |
| Spearhead (Shift+X) | One-province-wide advance along an exact traced path. **Armies only, never army groups.** Only usable past the army's front line or from a naval-invasion target. Ideal for encirclements |
| Fallback Line | Defensive line in controlled territory; the AI holds and counter-attacks. **No planning bonus**, but entrenchment accumulates |
| Area Defense (Garrison Area) | Guards an area rather than a line. Sub-options: Protect Victory Points, Guard Ports, Guard Coast, Protect Airbases, Guard Forts, Guard Supply Hubs and Railway. **Triples the commander's unit limit to 72 with no debuff** |
| Naval invasion | Amphibious assault; see below |
| Naval invasion with floating harbor | As above, requires one floating harbor in stockpile *(No Step Back)* |
| Paradrop | Airborne assault; see below |

Execution stance can be set to **careful / balanced / aggressive**.

### Planning bonus

- Accrues at the start of each day for a division that is at the starting position of an **offensive** battle plan (one containing at least one Offensive Line or Spearhead) and is **neither moving nor fighting**.
- A division accrues planning even if not assigned to the front line, so long as it is under the same commander who owns that front line.
- **Effect: +1% attack and +1% breakthrough per 1% planning.**
- **Base max planning bonus: 30%. Base daily gain: 2%** → 15 days to cap with no modifiers.
- **Each point of a general's Planning skill adds +2% to max planning and +5% to the daily accumulation rate, where the +5% is multiplicative on the 2% base.** Example: a general with Planning 4 → max planning 30% + 8% = **38%**, daily gain 2% × (1 + 20%) = **2.4%**, so 38 / 2.4 = **15.83 days** to cap.
- Also raised by land doctrines, national spirits, commander traits (Organizer, Fast Planner, Thorough Planner), officer spirits (Quick Improvisation) and certain political advisors.
- **Staff Office Plan** ability: **+400% planning speed for 7 days**.
- **Decay:** **−1% per day** while the division is managed by the battle-plan AI; **−3% per day** if the player issues manual commands.
- **Naval invasions normally gain no planning** — naval invasion planning gain has a −100% penalty against the 2%/day base. With Arms Against Tyranny's **Expeditionary Units** marine doctrine the penalty drops to **−80%**, so invasion units slowly accrue planning.

### Naval invasions

Two caps: the **division cap** (divisions per invasion order) and the **plan cap** (simultaneous invasion orders). Base values: **4 divisions per order, 1 plan at a time.**

Base naval tree (without Man the Guns):

| Year | Technology | Invasion division cap | Plan cap | Other |
|---|---|---|---|---|
| 1922 | Transport Ship | +2 | +2 | −30 prep days |
| 1940 | Landing Craft | +2 | +2 | +15% invasion defense; −30 prep days |
| 1944 | Advanced Landing Craft | +8 | +4 | +25% amphibious invasion; +50% invasion defense; −15 prep days |

Naval Support tree (with Man the Guns):

| Year | Technology | Invasion division cap | Plan cap | Other |
|---|---|---|---|---|
| 1922 | Transport Ship | +2 | +1 | −10 prep days |
| 1940 | Landing Craft | +4 | +3 | +15% invasion defense; −10 prep days |
| 1944 | Advanced Landing Craft | +5 | +4 | +25% amphibious invasion; +50% invasion defense; −10 prep days |

- **Arms Against Tyranny:** Elevate the Marine Corps gives **+2 division cap**; Expeditionary Task Forces gives **+1 plan cap**.
- An order with more divisions than the cap **will not execute** (map arrow reads "No divisions 0 Transports").
- Capacity is measured in **division count, not weight** — wider templates make stronger invasions at higher convoy cost.

**Preparation time:** with only the first level of naval invasion technology, **7 days per division** (1 division = 7 days, 10 divisions = 70 days). Reduced by Landing Craft (1940), Tank Landing Craft (1944), Mobile Warfare and Superior Firepower land doctrines, and the Base Strike fleet-in-being subdoctrine. Preparation starts immediately, even while divisions are still moving to the port. Parallel invasions from different ports to the same target are allowed within the plan cap.

**Convoys required per division = the division's weight, rounded up.** Battalion weights:

| Weight | Battalions |
|---|---|
| 0.1 | Support companies |
| 0.5 | Anti-Air, Anti-Tank, Artillery, Bicycle, Cavalry, Infantry, Mountaineers, Marines, Motorized Anti-Tank, Motorized Anti-Air, Motorized Artillery, Motorized Rocket Artillery, Paratroopers, Penal Battalion, Rocket Artillery, Truck-drawn Rocket Artillery |
| 0.6 | Camelry |
| 0.75 | Motorized Infantry |
| 0.8 | Armored Car |
| 1.0 | Amphibious Tank Battalion, Amtrac Battalion, Heavy/Light/Medium Amphibious Tank Battalion, Light SP Anti-Air, Light SP Artillery, Light Tank, Light Tank Destroyer, Mechanized Infantry |
| 1.25 | Medium SP Anti-Air, Medium SP Artillery, Medium Tank, Medium Tank Destroyer |
| 1.5 | Heavy SP Anti-Air, Heavy SP Artillery, Heavy Tank, Heavy Tank Destroyer, Modern SP Anti-Air, Modern SP Artillery, Modern Tank, Modern Tank Destroyer |
| 1.75 | Superheavy SP Anti-Air, Superheavy SP Artillery, Superheavy Tank, Superheavy Tank Destroyer |

**Naval supremacy:** more than **50% supremacy** is required in every sea zone the invasion arrow passes through, and it is only needed at the moment of launch. Supremacy by mission:

| Mission | Supremacy contribution |
|---|---|
| Strike Force | 100% |
| Naval Invasion Support | 100% |
| Patrol | 75% |
| Convoy Escort | 50% |
| Convoy Raiding | 25% |
| Minelaying | 25% |
| Minesweeping | 25% |
| Naval Exercises | 0% |
| Hold (in or out of port) | 0% |

Task forces on **Do Not Engage** contribute nothing. Per-ship supremacy scales with production cost and manpower (an Italian early battleship on Strike Force gives ≈356; an early destroyer ≈117). **Air superiority gives up to +100% to the effective ship count** (each ship counts double) when air superiority is 100% and planes cover 100% of the sea region; minelaying also adds a bonus.

**Naval intel efficiency:** at **≤10% intel, naval supremacy is halved**; the penalty improves linearly and disappears at **40% intel**. At least **40% naval intel efficiency** is needed to gain supremacy at all. Contributions (summed, 0–100%):

| Factor | Contribution |
|---|---|
| Enemy ideology | Democratic 20%, Non-aligned 20%, Communist 12.5%, Fascist 10% |
| Enemy trade law | Free trade 20%, Export focus 10%, Limited exports 5%, Closed economy 0% |
| Radar coverage | Up to 20% (one country-wide value, not per sea zone) |
| Fighting the enemy navy | Decays ≈ −0.2% per week |
| Spy networks *(La Résistance)* | Up to 40% |
| Infiltrate Navy operation *(LaR)* | 10% |
| Decrypted enemy ciphers *(LaR)* | 10% passive, 50% for 30 days |
| Intel from faction members *(LaR)* | 30% of the intel difference |
| Captured enemy operatives *(LaR)* | — |

The **Naval Department** intelligence agency upgrade multiplies the total by **1.25**.

Without La Résistance, decryption vs encryption gives instead:

| Own Decryption \ Enemy Encryption | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0% | 0% | 0% | 0% |
| 1 | 30% | 15% | 10% | 7.5% |
| 2 | 45% | 22.5% | 15% | 11.25% |
| 3 | 60% | 30% | 20% | 15% |

**Invasion combat:** landing troops take the standard **−50% amphibious penalty to attack and breakthrough** (modifiable by the division's Amphibious adjuster). On top of that, while protected by their transports they have **+50% breakthrough and −80% attack**, fading as the landing progresses (usually gone after **48 hours**). The **Amphibious Invasion Speed** modifier shortens that. **Invasion Defense** is additive with the +50% starting breakthrough (and also fades) and multiplicatively softens the landing penalty:

```
effective penalty = (−0.5 + modifiers) × max(0, 1 − Invasion Defense / 3.5)
```

**Post-invasion:** unless a port or city is captured, invaders are cut off and have **72 hours** before supplies run out. A **floating harbor** creates a temporary supply hub in the landing province, buying a few weeks.

### Paradrops

- Requires an air base with **at least 50 transport planes** to create the order, and **45 transport planes per assigned division** to execute.
- Requires **neutral air or ≥70% air superiority** in the departure, en-route and destination regions.
- The destination must be within transport range; provinces whose **air region's geographic centre** is out of range do not count, even if the province itself is in the range ring.
- Paradrops onto own/allied territory can execute any time; onto non-allied territory requires a state of war.

Transport planes required:

| Divisions | Base | Gliders (×0.9) | Doctrine (×0.5) | Gliders + Doctrine (×0.45) |
|---|---|---|---|---|
| 1 | 50 | 50 | 50 | 50 |
| 2 | 90 | 81 | 50 | 50 |
| 3 | 135 | 122 | 68 | 61 |
| 4 | 180 | 162 | 90 | 81 |
| 5 | 225 | 203 | 113 | 102 |
| 6 | 270 | 243 | 135 | 122 |
| 7 | 315 | 284 | 158 | 142 |
| 8 | 360 | 324 | 180 | 162 |
| 9 | 405 | 365 | 203 | 183 |
| 10 | 450 | 405 | 225 | 203 |
| 11 | 495 | 446 | 248 | 223 |
| 12 | 540 | 486 | 270 | 243 |

- **Glider Planes** ability (Paratroopers trait): −10% transport requirement for 7 days, 0.1 CP per battalion.
- **Strategic Air Lift Corps** special forces doctrine *(Arms Against Tyranny)*: −50% transport requirement.
- Both stack multiplicatively (×0.9 × 0.5); neither breaks the 50-plane minimum per order.
- Multiple orders from one base launch in **waves** in creation order, each wave taking about **4–8 hours**.

**Paradrop-capable division templates** must contain only paradrop-capable battalions and support companies. Only the **paratrooper battalion** is a paradrop-capable line battalion. Paradrop-capable support companies: Support Anti-Air, Support Anti-Tank, Support Artillery, Support Rocket Artillery, Cavalry Recon Detachment, Motorized Recon Company, Light Armored Recon Company, Engineer Company, Military Police, Maintenance Company, Field Hospital, Logistics Company, Signal Company, Helicopter Medevac *(Götterdämmerung)*, Airborne Light Armor *(AAT)*, Pioneers *(AAT)*, Recon Rangers *(AAT)*.

**Paradrop outcomes:**
- A disrupted drop loses **54.5%–90% of the division's strength**: **47.4%–99% of manpower** and **33.3%–98% of equipment**, plus up to 10% extra randomness. Losses occur even when the target province is empty and do not appear to depend on air superiority; **anti-air** raises disruption, and losses are much more common at **high latitudes** and into **coastal provinces**.
- Divisions land at **40% organization** regardless of disruption, with **−80% recovery rate for 120 hours** and **−30% attack and defense for 48 hours**.
- **Glider Planes** lets drops in the next 7 days land with much more organization (up to 100%) and take fewer disruption losses.

### Manual control and support attacks

- A division on a battle plan that receives a manual order returns to AI control after completing it.
- **Ctrl+right-click** (or Ctrl+Alt+right-click) an ongoing combat with an unengaged division to join as a **support attack** — the division helps without advancing into the province on victory. The AI also orders support attacks on its own.
- Allies' battle plans can be displayed (toggle in the lower-right corner), useful for coordination and for reading AI intentions.

## Cross-references

- [Manpower and experience](manpower-and-experience.md) — unit veterancy, medals, national experience pools.
- [Supply and logistics](supply-and-logistics.md) — supply grace, Logistics Wizard/Extra Supplies context.
- [Land combat](../02-land-warfare/land-combat.md) — terrain names used by terrain traits.
