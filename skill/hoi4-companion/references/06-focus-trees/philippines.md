---
title: Philippine National Focus Tree
category: focus-trees
tags: [philippines, focus tree, national focus, no compromise no surrender, unique tree]
game_version: "1.19"
dlc: [No Compromise, No Surrender]
sources:
  - https://hoi4.paradoxwikis.com/Philippine_national_focus_tree
---

## Summary

The Philippine national focus tree (requires No Compromise, No Surrender) offers nine branches across economic, military, and ideological paths. Early choices shape relations with the United States or alternative powers, gate access to military and naval development, and unlock strategic focuses for independence, resistance, or territorial expansion. Without the DLC, the Philippines uses the generic focus tree instead.

See [Philippines](../05-countries/philippines.md) for the country's 1936 starting profile.
See [01-mechanics/national-focus.md](../01-mechanics/national-focus.md) for generic/continuous focuses — this document covers the nation-specific tree only.

## United States Army Forces in the Far East Branch

Historical early branch centered on alliance with the United States and military buildup in the Far East.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **United States Army Forces in the Far East** | Is ally of USA | None | (Effect text incomplete on wiki) |
| **Appoint MacArthur** | USAFFE; is ally of USA | None | Bypass if USA: Douglas MacArthur is current country leader |
| **Bring in Eisenhower** | Appoint MacArthur; is ally of USA | None | 1× 100% cost reduction for Land Doctrine; Army experience +25; Navy experience +25; Air experience +25; USA gets event Eisenhower Requested By The Philippines |
| **Subordinate Philippine Department** | Bring in Eisenhower; is ally of USA | None | Jonathan Wainwright becomes General (+1 skill) |
| **USAFFE Headquarters** | Subordinate Philippine Department; is ally of USA | None | (Effect text incomplete on wiki) |
| **Utang na loob** | USAFFE Headquarters; is ally of USA | None | −25% cost and +5% defense for Last Stand; unlocks decision: Request Indefinite Stay for MacArthur |
| **Police Chief Eisenhower** | Utang na loob AND Bring in Eisenhower; Eisenhower active in country | None | Eisenhower remains in Philippines permanently, cannot be recalled by USA |
| **Military Requisitions** | Appoint MacArthur; is ally of USA | None | (Effect text incomplete on wiki) |
| **Small Arms and Artillery Requisition** | Military Requisitions; is ally of USA; completed ≥1 of: Peg the Peso to the Dollar, Pro Hacendados, or Nationality Act | None | (Effect text incomplete on wiki) |
| **Trucks and Transport Requisition** | Small Arms and Artillery Requisition; is ally of USA; completed ≥2 of: Peg the Peso to the Dollar, Pro Hacendados, or Nationality Act | None | (Effect text incomplete on wiki) |
| **Mariveles Naval Base** | Military Requisitions; is ally of USA; completed ≥2 of: Peg the Peso to the Dollar, Pro Hacendados, or Nationality Act | None | Bataan (1027) gains +2 building slots, +2 naval dockyards |
| **Far East Air Force** | Military Requisitions; is ally of USA; completed ≥1 of: Peg the Peso to the Dollar, Pro Hacendados, or Nationality Act | None | (Effect text incomplete on wiki) |
| **Aircraft Requisition** | Far East Air Force; is ally of USA; completed ≥2 of: Peg the Peso to the Dollar, Pro Hacendados, or Nationality Act | None | (Effect text incomplete on wiki) |
| **Expand US Bases** | (Trucks and Transport Requisition OR Aircraft Requisition OR Mariveles Naval Base); is ally of USA; completed ≥2 of: Peg the Peso to the Dollar, Pro Hacendados, or Nationality Act | None | (Effect text incomplete on wiki) |
| **United States Asiatic Fleet** | Expand US Bases; is ally of USA; completed all 3 of: Peg the Peso to the Dollar, Pro Hacendados, Nationality Act | None | (Effect text incomplete on wiki) |
| **Gunboat Diplomacy** | United States Asiatic Fleet | War Plan Rainbow Five | (Effect text incomplete on wiki) |
| **War Plan Rainbow Five** | United States Asiatic Fleet; in faction with USA; in faction with (France or UK); ≥1 ships | Gunboat Diplomacy | (Effect text incomplete on wiki) |

## Declare Military Emergency Branch

Authoritarian militaristic branch unlocked by flag PHI_military_emergency_flag. Focuses on nuclear weapons development, aggressive war, and imperial conquest.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **Declare Military Emergency** | Flag: PHI_military_emergency_flag (always false on wiki; normally unlocked via event) | None | National spirit Restore Order for 180 days: stability +2.00%/week, war support +0.50%/week; counts as completed American economic focus (flag: PHI_usa_focus_done) |
| **Weapons of War** | Declare Military Emergency | None | If not researched Atomic Research: −2.0 years AoT, +100% research bonus for next 1 Atomic Research; Manila gains 1 nuclear facility; hire nuclear scientist (Nuclear specialization +2); breakthrough Nuclear Research +25.00% |
| **Pre-emptive Strikes** | Weapons of War | None | Dynamic modifier Pre-emptive Strikes: max planning factor +10.0%, justify wargoal time −10.0%, wargoal tension limit −80.0%, dockyard output +10.00%, production efficiency +10.00% |
| **Sunset Empires** | Pre-emptive Strikes | None | 2× random owned controlled state: +2 building slots, +2 military factories each (total +4 building slots, +4 military factories); 1× random coastal state: +2 building slots, +2 dockyards |
| **Land of the Setting Sun** | Sunset Empires; not in faction with Japan | None | If Japan exists: declare war on Japan; modify Pre-emptive Strikes: production efficiency cap +5.0%, navy organization +10.0%, naval max range +15.0%, dockyard output +10.0% |
| **Traitors Back Home** | Land of the Setting Sun; not in faction with USA | None | If USA exists: declare war on USA; modify Pre-emptive Strikes: production efficiency cap +5.0%, factory output +15.0%, dockyard output +5.0% |
| **Sea of Cobalt** | Sunset Empires; researched Atomic Research | None | Tiered effects: if not researched Atomic Research (unlikely): −2.0 years AoT, +100% bonus; if no nuclear reactor: breakthrough Nuclear Research +75.00%; if researched nuclear reactor: add 1 random nuclear reactor, breakthrough +50.00%; if all above: add 1 heavy water nuclear reactor, breakthrough +50.00%; national spirit Sea of Cobalt: nuclear bomb production +10%, nuclear warfare projects +10%, nuclear reactor construction +25.00% |
| **The Sun Has Set** | Sunset Empires; not in faction with UK | None | If UK exists: declare war on UK; modify Pre-emptive Strikes: production efficiency cap +5.0%, air range +10.0%, air mission efficiency +10.0% |
| **End Colonialism** | The Sun Has Set | None | Modify Pre-emptive Strikes: compliance growth +10.0%, resistance growth −10.0%, non-core manpower +10.0% |
| **Cobalt Supremacy** | (Land of the Setting Sun OR The Sun Has Set) AND Sea of Cobalt | None | Replace Sea of Cobalt national spirit with Cobalt Supremacy: nuclear bomb production +25%, nuclear warfare projects +10%, nuclear reactor construction +50.00% |

## Subject... Surrender Branch

Reconquista/resistance branch unlocked when Philippines loses control of Manila (327). Focuses on guerrilla warfare, partisan organization, and eventual liberation.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **Subject... Surrender** | (Automatic) Losing control of all of Manila (327) | None | Dynamic modifier Philippine Resistance: equipment capture +50.0%; weekly exiled manpower +100; if Douglas MacArthur active: joins USA |
| **I Shall Return** | Subject... Surrender; (is subject of another country OR (not in faction AND not faction leader)) | None | Become government in exile (legitimacy 35 if subject, 20 if in faction); modify Philippine Resistance: legitimacy gain +50.0%, exile manpower to host +10.0%; unlock decisions: Request Equipment from Host, Exchange Military Insights with Host; +10000 manpower |
| **Submarine Supplies** | I Shall Return; in faction with USA | None | National spirit Submarine Supply Drops: supply consumption −10.0%, division defense on core +5.0%, encirclement penalty −15.0%; if Early Submarine not researched: add technology, create 4 S-class submarines from USA |
| **Soldiers In Hiding** | Subject... Surrender | None | Modify Philippine Resistance: CAS damage reduction +20.0%, weekly manpower +100; add 1 offmap military factory |
| **The Hunters** | Soldiers In Hiding | None | Modify Philippine Resistance: special forces capacity +20.0%, terrain traits XP +20.0%, resistance target in occupied states +5.0%, garrison damage +5.0%; gain 3 brigades of Hunters ROTC when Grassroot Guerillas completes |
| **Hukbalahap** | Subject... Surrender | None | If not completed Legalize Communist Party: Luis Taruc becomes General; otherwise: Luis Taruc +250 experience, gain Camouflage Expert (CAS damage reduction +50.0%, air CAS bonus −50.0%); modify Philippine Resistance: resistance target +10.0%, garrison damage +5.0%, communism support +0.02/day; if Partido Komunista coup completed and not PHI_american_intervention_is_over: political power gain +10%, resistance decay −10%, garrison damage +10.0%, high command cost −33% |
| **The Cry** | Hukbalahap | None | Modify Philippine Resistance: recruitable population +2.0%, division organization +5.0%; gain 3 Hukbalahap brigades when Grassroot Guerillas completes |
| **Local Resistance** | Subject... Surrender | None | If Encourage Chinese Immigration completed: Philippine Resistance: resistance target +10.0%; otherwise: +5.0%; Nieves Fernandez available as political advisor (division attack/defense on core +5.0%, research +5.00%, resistance growth +10%) |
| **Juramentado** | Local Resistance | None | Rule: can use kamikaze pilots; modify Philippine Resistance: army organization regain +20.0%; gain 3 Juramentado brigades when Grassroot Guerillas completes |
| **Exile Support** | (Submarine Supplies OR The Hunters) | None | +300 infantry equipment, +150 support equipment to stockpile; +2 offmap civilian factories |
| **Grassroot Guerillas** | (The Hunters OR The Cry OR Juramentado) | None | Every occupied core state: add modifier Strong Guerrilla Presence (resistance decay −30%, strategic redeployment disabled); spawn 3 guerrilla brigades per completed prerequisite focus (liberated/lightly-occupied states prioritized) |
| **Reconquista** | (Exile Support OR Grassroot Guerillas) | None | Modify Philippine Resistance: division attack on core +10.0%, war support +0.50%/week (combat casualties) |

## Commonwealth of the Philippines Branch

Large economic/political branch centered on Great Depression recovery, independence, modernization. Subdivided into three sub-branches: Pro/Anti Hacendados, Nationality Act/Open Borders, and Treaty of Manila.

### Pro Hacendados / Anti Hacendados Sub-branch

First-tier mutual-exclusion split determining economic approach and relations with wealthy landowners.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **Pro Hacendados** | (Quezon City Campus OR Reduce Unnecessary Expenditure OR Subsidies OR Basic Welfare OR Encourage Asian Trade); ≥5 focuses from previous tier completed | Anti Hacendados | Political power +50; random state +2 building slots +2 civilian factories; if Partido Komunista coup completed and not PHI_american_intervention_is_over: America threat −10%; replace The Great Depression with Shaken Economy modifier; National Defense Act focus −35 days |
| **Anti Hacendados** | (Quezon City Campus OR Reduce Unnecessary Expenditure OR Subsidies OR Basic Welfare OR Encourage Asian Trade); ≥5 focuses from previous tier completed | Pro Hacendados | Add/modify Japan Aligned Ideology (daily support +0.05 to Japan's current ruling party ideology); if Partido Komunista coup completed and not PHI_american_intervention_is_over: America threat +10%; replace The Great Depression with Shaken Economy modifier (construction speed +10.0%); remove Manuel Roxas as political advisor; speed up: Luzon Transport, Mindanao Transport, Land Reform, Bill of Rights, National Defense Act (all −35 days) |
| **Investment Fund** | Pro Hacendados; no investment plans active | None | Activate one of three investment missions: 1) Infrastructure Development (grants 2 civilian factories if completed), 2) Establish New Trade Relations (requires ≥3 regional trade partners, level-6 naval base, ≥1 new naval dockyard), 3) Increase Industrial Efficiency (requires infrastructure in Bataan/Central Islands) |
| **Sugar Barons** | (Pro Hacendados OR Anti Hacendados) | None | Unlock sugar excise decisions; if Open Borders or Nationality Act completed: modify Recovering Economy (fuel per oil +15.0%); otherwise modify Shaken Economy (fuel per oil +15.0%); random state +1 building slot +1 civilian factory, +1 building slot +1 naval dockyard; if Partido Komunista coup and not PHI_american_intervention_is_over: America threat −10% |
| **San Miguel** | Sugar Barons | None | Modify San Miguel Brewery concern: war support (combat casualties) +0.10%/week, war support (sunk convoys) +0.10%/week, war support (enemy bombing) +0.10%/week |
| **Luzon Transport** | (Pro Hacendados OR Anti Hacendados); controls Luzon (623) | None | Luzon +1 infrastructure +1 building slot; Bataan +1 infrastructure +1 building slot; Manila +1 infrastructure +1 building slot; Anti Hacendados −35 days |
| **Textile Mills** | Luzon Transport | None | Random state +2 building slots +2 civilian factories |
| **Expand Gold Mining** | (Pro Hacendados OR Anti Hacendados) | None | If Open Borders or Nationality Act: modify Recovering Economy (consumer goods −5.0%, daily political power +0.05); otherwise modify Shaken Economy (consumer goods −5.0%, daily political power +0.05) |
| **Encourage Gold Exports** | Expand Gold Mining | None | Modify Marsman and Company concern (consumer goods −10.0%); if Open Borders or Nationality Act: modify Recovering Economy (consumer goods −5.0%); otherwise Shaken Economy (consumer goods −5.0%) |
| **Mindanao Transport** | (Pro Hacendados OR Anti Hacendados); controls Northern Mindanao (1026) | None | Northern Mindanao +1 infrastructure +1 building slot; Davao +1 infrastructure +1 building slot; Zamboanga +1 infrastructure +1 building slot; unlock convoys-for-military-equipment decisions; Anti Hacendados −35 days |
| **Mineral Prospecting** | Mindanao Transport | None | Modify Benguet Corporation concern (resource gain efficiency +10.00%); unlock prospecting decisions |
| **Land Reform** | (Pro Hacendados OR Anti Hacendados) | None | If Open Borders or Nationality Act: modify Recovering Economy (consumer goods −5.0%); otherwise Shaken Economy (consumer goods −5.0%); Anti Hacendados −35 days |
| **Bill of Rights** | Land Reform | None | Political power +75; stability +5.00%; war support +10.00%; Anti Hacendados −35 days |
| **Japanese Advisors** | Anti Hacendados; at peace with Japan | None | When either Japanese Advisors or Observers completes: Yuitsu Tsuchihashi, Iwaichi Fujiwara become Generals, Okawachi Denshichi becomes Admiral; when both complete: national spirit Japanese Investment (180 days): +2 offmap civilian factories, +2 offmap military factories; if Arms Against Tyranny DLC and Align with Japan completed and Declare Military Emergency not completed: Mitsubishi concerns gain +1 size each |

### Nationality Act / Open Borders Sub-branch

Second-tier mutual-exclusion split determining immigration policy and economic recovery posture.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **Nationality Act** | (San Miguel OR Textile Mills OR Encourage Gold Exports OR Mineral Prospecting OR Bill of Rights); ≥5 focuses from previous tier completed | Open Borders | Replace Shaken Economy with Recovering Economy: daily political power +0.10, ideology drift defense +10.0%; National Defense Act −35 days |
| **Open Borders** | (San Miguel OR Textile Mills OR Encourage Gold Exports OR Mineral Prospecting OR Bill of Rights); ≥5 focuses from previous tier completed | Nationality Act | Add/modify Japan Aligned Ideology (daily support +0.05 to Japan's ruling party); replace Shaken Economy with Recovering Economy (compliance growth +10.0%, ideology drift −5.0%); speed up: Increase Sugar Exports, Encourage Chinese Immigration, National Defense Act (all −35 days) |
| **Luce-Celler Act** | Nationality Act; no investment plans active | None | Activate one of three investment missions (as per Investment Fund) |
| **Philippine-American Educational Foundation** | Nationality Act; completed Align with the USA, Peg the Peso to the Dollar, and Pro Hacendados | None | +1 research slot |
| **Government Filipinization** | (Nationality Act OR Open Borders) | None | Juan Samulong, Jose Laurel, Manuel Roxas: upgraded advisor traits; if Treaty of Manila completed: modify Economic Growth (ideology drift +10.0%, counterintelligence +0.20); otherwise modify Recovering Economy (ideology drift +10.0%, counterintelligence +0.20) |
| **Bicameral Legislature** | (Nationality Act OR Open Borders) | None | National spirit Government Reform (360 days): trade laws cost −50%, economy laws cost −50%, political advisor cost −50%; if Treaty of Manila: modify Economic Growth (daily political power +0.15, construction +5.0%); otherwise Recovering Economy (+0.15, +5.0%) |
| **Uncouple the Peso and Dollar** | (Nationality Act OR Open Borders); completed Peg the Peso to the Dollar | None | If Manila can build 2+ civilian factories: Manila +2 building slots +2 civilian factories +1 infrastructure; if Davao can build 1+ civilian factory: Davao +1 building slot +1 civilian factory +1 infrastructure |
| **Increase Sugar Exports** | (Nationality Act OR Open Borders) | None | If Treaty of Manila: modify Economic Growth (consumer goods −10.0%); otherwise Recovering Economy (−10.0%); Open Borders −35 days |
| **Break Chinese Monopoly** | (Nationality Act OR Open Borders) | Encourage Chinese Immigration | If Treaty of Manila: modify Economic Growth (consumer goods −5.0%); otherwise Recovering Economy (−5.0%); random state +2 building slots +2 civilian factories; stability −5.00%; China gets Seized Migrant Property event (opinion −25) |
| **Encourage Chinese Immigration** | (Nationality Act OR Open Borders) | Break Chinese Monopoly | If Treaty of Manila: modify Economic Growth (ideology drift −5.0%, civilian factory construction +10.0%, infrastructure construction +10.0%); otherwise Recovering Economy (same); China gets Welcomed Chinese Migrants (opinion +15); Open Borders −35 days |
| **Japanese Observers** | Open Borders; at peace with Japan | None | When either Japanese Advisors or Observers completes: Yuitsu Tsuchihashi, Iwaichi Fujiwara become Generals, Okawachi Denshichi becomes Admiral; when both complete: national spirit Japanese Investment (180 days) +2 offmap civilian/military factories each; if Arms Against Tyranny and Align with Japan and not Declare Military Emergency: Mitsubishi concerns +1 size |

### Treaty of Manila Sub-branch

Third-tier independence and post-war modernization branch unlocking high-tier economic and political focuses.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **Treaty of Manila** | (Government Filipinization OR Bicameral Legislature OR Uncouple the Peso and Dollar OR Increase Sugar Exports OR Break Chinese Monopoly OR Encourage Chinese Immigration); ≥4 focuses from previous tier; (fully independent OR (subject to USA AND autonomy > Integrated Puppet)) | None | Event Treaty of Manila; if overlord, Commonwealth becomes free; set flag leave_faction_happily_flag; replace Recovering Economy with Economic Growth (join faction tension 0%); known as The Philippines |
| **Universal Suffrage** | Treaty of Manila | None | Ruling party popularity +10.00%; national spirit Universal Suffrage: political power +10%, stability +5.00%, research +5.00% |
| **Modernization** | Treaty of Manila | None | 2× 50% research bonus for Electronics; 2× 25% research bonus for Production; modify Economic Growth (construction +15.0%) |
| **Bill of Rights for Veterans** | Universal Suffrage | None | War support +10.00%; modify Economic Growth (recruitable population +10.0%, war support (combat casualties) +0.25%/week) |
| **Revision of Taxation Laws** | Universal Suffrage | None | Modify Economic Growth (consumer goods −10.0%, daily political power +0.15) |
| **Rehabilitation Finance Corporation** | Modernization | None | National spirit Rehabilitation Finance Corporation: consumer goods −10.0%, factory repair +25.00%, free repair +25.00%, civilian factory construction +5.00% |
| **Department of Foreign Affairs** | Modernization; fully independent | None | Unlock Department of Foreign Affairs decisions; if (not Open Borders AND not Nationality Act AND has Japan Aligned Ideology): unlock Decrease Japanese Ideological Influence |
| **Economic Nationalism** | (Bill of Rights for Veterans AND Revision of Taxation Laws AND Rehabilitation Finance Corporation AND Department of Foreign Affairs) | None | 2× random state +2 building slots +2 civilian factories; modify Economic Growth (trade per factory −1, resource gain +10.0%, consumer goods −5.0%) |
| **Bell Trade Act** | (Bill of Rights for Veterans AND Revision of Taxation Laws AND Rehabilitation Finance Corporation AND Department of Foreign Affairs); USA opinion ≥30; (USA doesn't exist OR USA at war with Philippines for bypass) | None | 2× 50% research bonus for Industry and Excavation Technologies; random state +2 building slots +2 civilian factories; national spirit Bell Trade Act; USA: target country trade cost −15.00%, trade relations +30 |
| **Pearl of the Orient Seas** | (Economic Nationalism AND Bell Trade Act) | None | Replace Economic Growth with Pearl of the Orient Seas: factory output +10.0%, dockyard output +10.0%, navy organization +10.0% (flavor: economic prosperity); replace Rehabilitation Finance Corporation with Development Bank of the Philippines: consumer goods −5.0%, max factories per state +20%, civilian factory construction +5.00% |

## Petition the Supreme Court Branch

> ⚠️ Communist branch branch not documented on wiki.

_Not covered on the wiki._

## War for the Oceans Sub-branch (Expansion)

Post-independence naval/territorial expansion branch with claims across Pacific, Indian Ocean, and Southeast Asia.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **War for the Oceans** | (Treaty of Manila OR Second Philippine Republic OR Reino de Filipinas OR Pan Pacific Trade Union Secretariat OR Comintern) | None | Modify Island Nation dynamic modifier (dockyard output +10.0%, navy max range +15.0%); random coastal state +2 building slots +2 naval dockyards |
| **Assume the Naval Burden** | War for the Oceans; is ally of Japan; Japan ≥25 ships | Develop Naval Infrastructure | Japan gets event Commonwealth requests Control over Pacific Navy; if accept: Kiyoshi Hasegawa becomes Admiral, part of Japanese navy transferred to Philippines |
| **Develop Naval Infrastructure** | War for the Oceans | Assume the Naval Burden | Modify Island Nation (dockyard output +10.0%); random coastal state +2 building slots +2 naval dockyards |
| **Reunite Madagascar** | (Assume the Naval Burden OR Develop Naval Infrastructure) | None | Gains claims on Madagascar (543), Comoro Islands (708), Reunion (706), Mauritius (707); unlock decisions to core after control |
| **Take Pacific Islands** | (Assume the Naval Burden OR Develop Naval Infrastructure) | None | Gains claims on Hawaii, Johnston Atoll, Midway, Wake Island, Marshall Islands, Guam, Gilbert Islands, Tahiti, Phoenix Island, Ellice Islands, Saipan, Palau, Minamitorishima, Caroline Islands, Nauru, Line Islands, Bismarck, Bougainville, Solomon Islands, Nendo; if Palau exists: annex wargoal; unlock core decisions |
| **Malayo-Polynesia** | (Assume the Naval Burden OR Develop Naval Infrastructure) | None | Gains claims on Borneo region (Sabah, Kalimantan Barat, Sarawak, Sulawesi, Kuala Lumpur, Sumatra, West Java, Nusa Tenggara, Brunei, Singapore, Moluccas, Dutch New Guinea, Portuguese Timor, interior Borneo, Aru Islands, Kaiser-Wilhelmsland); unlock core decisions |
| **War of Oceania** | (Assume the Naval Burden OR Develop Naval Infrastructure) | None | Gains claims on Wellington, Canterbury, New Caledonia, Fiji, Samoa |
| **Conquest of Japan** | Develop Naval Infrastructure | None | Gains claims on Iwo Jima, Okinawa, Taiwan; if Taiwan exists: annex wargoal; gain Take Claimed State wargoal vs Japan |
| **Masters of the Pacific** | ((Reunite Madagascar OR Take Pacific Islands OR Malayo-Polynesia OR War of Oceania OR Conquest of Japan) AND ≥24 Austronesian claims from preceding focuses) | None | Gain new flag/name; modify Island Nation (navy max range +10.0%, air range +15.0%, supply consumption −10.0%); set cosmetic tag PHI_polynesia_tag |

## Offshore Patrol Branch

Naval defensive/development branch with focus on patrol boats, marines, and coastal protection.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **Offshore Patrol** | None | None | Random coastal state +2 building slots +2 naval dockyards; modify Island Nation (dockyard output +5.0%) |
| **Cavite Naval Base** | Offshore Patrol | None | Random coastal state (prioritize Bataan) +2 building slots +2 naval dockyards; Manila +1 naval headquarters if lacking one; modify Island Nation (dockyard output +5.0%, ship repair +10.0%); Cavite Naval Base (Refurbishment Repair Manufacturer) +1 size |
| **PT Boat Development** | Offshore Patrol; completed National Defense Act | None | −1.0 years AoT, +100% research bonus for next 1: All Screen Ship technologies; screen mastery +10%, patrol boat mastery +20% |
| **Marine Corps** | Offshore Patrol | None | If Arms Against Tyranny: 1× 25% doctrine cost reduction for Special Forces; +10.00% mastery bonus (240 days) for Marine Commandos/Expeditionary Units; 1× 100% research bonus for Marine technology; modify Island Nation (special forces capacity +5.0%, amphibious invasion +10.0%, special forces +10%); otherwise: just the modifiers and research |
| **Mosquito Fleet** | PT Boat Development | Devil Boats | National spirit Mosquito Fleet: light hull production −15.00%, light attack −5%, torpedo attack +10%, max speed +2%, HP −25% |
| **Fast Attack Craft** | Mosquito Fleet | None | Modify Island Nation (convoy raiding efficiency +5.0%, light gun hit +5.0%, torpedo hit +5.0%, torpedo screen penetration +5.0%) |
| **Devil Boats** | PT Boat Development | Mosquito Fleet | National spirit Devil Boats: cruiser production −10.00%, light attack −5%, torpedo attack +10%, max speed +2%, HP −15% |
| **Coastal Defense Ships** | Offshore Patrol | None | Add technology Coastal Defense Ships; national spirit Coastal Defense Ships: coastal defense ship armor +20%, light attack +10%, torpedo attack +10%, HP +15%, production −10.00% |
| **Philippine Naval Patrol** | (Fast Attack Craft OR Coastal Defense Ships) | None | Modify Island Nation (fleet coordination +5.0%, navy organization +10.0%, naval max range +15.0%, naval experience gain +0.1/day) |
| **Thalassocracy** | Philippine Naval Patrol | None | 3× random coastal state +2 building slots +2 naval dockyards; modify Island Nation (fleet coordination +10.0%, dockyard output +10.0%) |

## National Defense Act Branch

> ⚠️ Main army/air force branch focuses not documented on wiki. Appears to gate access to various military options and may be prerequisite for other branches. Listed as "Army/Air force branch" but detailed focus table missing.

_Not covered on the wiki._

## That's Not An Island! Sub-branch (Hidden)

Hidden experimental carrier branch (requires Arms Against Tyranny or Götterdämmerung for full effects).

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| **That's Not An Island!** | Flag: PHI_did_carrier_tech (hidden/easter egg); completed Philippine Air Force; has Aerodynamics/Avionics facility, Naval Engineering facility | None | Breakthrough Naval Engineering +50.00%; if Götterdämmerung: national spirit Habakkuk Carrier (ice carrier production −15.00%, ice aircraft carrier research +100%); 1× +50% research bonus for Pykrete Tech, 1× +100% for Carrier models; otherwise: 2× +100% research bonus for Carrier models |

## Notes on branches and bypasses

- **Rebuild Sakdalistas sub-branch** (Fascist/Spanish Reconciliation): Noted on wiki but not fully documented.
- Several focuses in early branches show incomplete effect text ("XXX" placeholder) on the source wiki.
- Military economic focuses (Pro Hacendados, Anti Hacendados, Nationality Act, Open Borders) gate requisition branches: each has a requirement like "completed ≥1" or "≥2" of the named focuses. Details on which ones gate which requisitions are scattered across multiple focus effect texts.
- **Anti Hacendados** speeds up multiple focuses (Luzon Transport, Mindanao Transport, Land Reform, Bill of Rights, National Defense Act) by 35 days each.
- **Open Borders** similarly speeds up three focuses (Increase Sugar Exports, Encourage Chinese Immigration, National Defense Act).
- American intervention flag **PHI_american_intervention_is_over** is checked in multiple focuses (Pro Hacendados, Sugar Barons, Hukbalahap) and gates America Threat modifications and special Partido Komunista coup effects.
- **Declare Military Emergency** is normally inaccessible (marked "always false") but gates the entire militaristic Weapons of War → nuclear → conquest branch. Unlocked via unspecified event.
- The **Japanese Advisors** and **Japanese Observers** focuses share a combined effect: completing both grants Japanese Investment national spirit and military industrial bonuses.
