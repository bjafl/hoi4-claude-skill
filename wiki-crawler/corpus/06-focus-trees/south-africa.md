---
title: South African National Focus Tree
category: focus-trees
tags: [south africa, focus tree, dominion, commonwealth, independence, fascism, communism, african colonies]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/South_African_national_focus_tree
---

## Summary

South Africa's unique focus tree offers six major branches and two ideological sub-branches. The core decision path lies between remaining in the Commonwealth (War Measures Act branch) or abandoning Westminster for independence, which then splits into Fascist (Afrikaner Broederbond) or Communist (Empower the Workers) routes. Side branches provide industrial expansion, military doctrine research, and air/naval development. Key feature: the Anti-Colonialist Crusade path (Communist only) allows declaring war on colonial powers to liberate African territories.

See [South Africa](../05-countries/south-africa.md) for the country's 1936 starting profile.

## War Measures Act/Support the Policy of Appeasement branch

Commonwealth-aligned path; reinforces cooperation with British Empire and focuses on war preparation.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| War Measures Act | World Tension >20% OR current ruling party is not Democratic | Support the Policy of Appeasement | Political Power: +120 |
| Emergency Workers | War Measures Act | | Gains national spirit: Emergency Workers (Infrastructure construction: +7%, Military factory construction: +7%, Civilian factory construction: +7%) |
| Cape Garrison Artillery | Emergency Workers | | Add level 2 Coastal fort to all home coastal provinces and naval bases |
| Reconstitute the Cape Corps | Cape Garrison Artillery | | Modifies History of Segregation spirit: Recruitable Population Factor: −40% |
| Expand the Cape Corps | Reconstitute the Cape Corps | Outlaw Strikes | Removes History of Segregation spirit |
| Support the Policy of Appeasement | Britain has not enforced loyalty; AND (is UK subject OR Britain decolonized + in UK faction + UK at peace) | Abandon Westminster | Political Power: +120; Available advisor: Sir Patrick Duncan (Democratic Reformer, Democracy support: +0.10/day) |
| CSIR | War Measures Act + Support the Policy of Appeasement; member of Commonwealth Research | | 10% Technology Sharing bonus from Commonwealth Research |
| Police Windhoek | Support the Policy of Appeasement | | Modifies Ossewabrandwag spirit (Factory output: −10%, Dockyard output: −10%); loses Anti-British Sentiment modifier |
| Joint Air Training Scheme | CSIR | | Gains national spirit: Joint Air Training Scheme (all aircraft Range: +10%; Fighter/Heavy Fighter Air Attack: +5%; CAS/Carrier CAS Ground Attack: +5%; Naval Bomber/CV Naval Bomber Naval Attack: +5%; Tactical Bomber Ground Attack: +5%; Strategic Bomber Strategic Bombing: +5%; Transport Plane; Ace generation chance: +10%) |
| Desert Equipment | Joint Air Training Scheme | | Gains national spirit: Desert Equipment (Heat Attrition: −50%, Hot acclimatization gain: +10.0%) |
| Suppress the Stormjaers | Joint Air Training Scheme + Police Windhoek | | Removes Ossewabrandwag spirit |
| Secure Interests in Africa | Suppress the Stormjaers + Desert Equipment + at peace with UK + UK fully independent | | UK gets event "South Africa Requests African Mandate" (UK must approve) |
| Native Laws Amendment Act | Police Windhoek OR Support the Afrikaner Broederbond | | Gains national spirit: Cheap Labor (Recruitable Population: −5%, Factory output: +3%, Dockyard output: +3%) |
| Work for All Poor | Native Laws Amendment Act | | Modifies Cheap Labor spirit (adds Consumer Goods Factories: −3%) |
| Outlaw Strikes | Work for All Poor | Expand the Cape Corps | Modifies Cheap Labor spirit (Consumer Goods Factories: −8%, Factory output: +6%, Dockyard output: +6%) |

## Abandon Westminster branch

Independence path; enables choice of ideology (Fascism or Communism) via sub-branches.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| Abandon Westminster | Britain has not enforced loyalty | Support the Policy of Appeasement | Gains national spirit: Abandon Westminster (1095 days; Daily autonomy progress: +0.5; Daily Democracy support: −0.03) |

### Support the Afrikaner Broederbond sub-branch (Fascist)

Fascist path with civil war, German alignment, or independent Africa-focused faction.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| Support the Afrikaner Broederbond | Abandon Westminster + Britain has not enforced loyalty | Empower the Workers | Modifies Abandon Westminster spirit (Daily Democracy support: −0.03; Daily Fascism support: +0.03) |
| Support Ossewabrandwag | Support the Afrikaner Broederbond + (fully independent OR Dominion/Satellite + autonomy >65%) + Britain has not enforced loyalty | | Army Experience: +15; Modifies Ossewabrandwag spirit (Daily Fascism support: +0.01; Foreign subversive activities efficiency: −40%; Damage to Garrisons: −10%) |
| Celebrate the Great Trek | Support the Afrikaner Broederbond + Britain has not enforced loyalty | | Political Power: +120 |
| Voortrekker Monument | Support Ossewabrandwag OR Native Laws Amendment Act | | Gains national spirit: Voortrekker Monument (Stability: +7%, Daily autonomy progress: +0.5) |
| Support Nazification of South-West Africa | Support Ossewabrandwag + GNP >20% support + autonomy >Colony + controls Khomas, Karas, Kunene, Otjozondjupa (541, 893, 894, 895) + Britain has not enforced loyalty | South Africa First | Khomas (541): +2 building slots, +1 military factory, +1 civilian factory, +2 air bases, +1 naval base, +2 land forts; Karas (893): +2 land forts; Otjozondjupa (895): +2 land forts |
| South Africa First | Celebrate the Great Trek + (fully independent OR Dominion/Satellite + autonomy >75% + not fighting alongside UK) + Britain has not enforced loyalty | Support Nazification of South-West Africa | UK: South Africa becomes free, leaves Allies; South Africa gains: can create factions, Stability: +10%; Political Power: +70 |
| Support the German Coup | Support Nazification of South-West Africa + GNP >25% + controls Khomas (541) + (fully independent OR Dominion/Satellite + autonomy >80%) + Britain has not enforced loyalty | | **Bypass:** if current ruling party is Fascist. **Effect:** Civil war starts (Fascist Nationalists in South-West vs. Democratic Unionists in rest); Fascist capital in Cape (681), controls Transvaal (275), Cape (681), Natal (719); Democratic capital in Khomas (541), gains 35% Communist popularity |
| Reclaim Boer Colonies | South Africa First + Britain has not enforced loyalty | | Gains Conquer war goal vs UK; targets Bechuanaland (542), Rhodesia (545) |
| Commemorate the Battle of Blood River | Support Nazification of South-West Africa + Voortrekker Monument + Britain has not enforced loyalty | | Modifies Voortrekker Monument spirit (Stability: +7%, Recruitable Population: +0.50%, Daily autonomy progress: +0.75) |
| German Scientists | Support the German Coup + German Reich is Fascist + in Axis faction + Britain has not enforced loyalty | | German Reich joins Axis Research tech group with South Africa |
| A King for Our People | Support the German Coup OR South Africa First + King Edward VIII exiled + Britain has not enforced loyalty | | Gains national spirit: Edward VIII (Division Organization: +2.0%, Division Recovery Rate: +2.0%, Stability: +5%) |
| Support Axis Interests | Support the German Coup + controls Bechuanaland (542), Rhodesia (545), Tanganyika (546) + Britain has not enforced loyalty | | Add 1 building slot + 2 Infrastructure in any of: Léopoldville (295), Coquilhatville (538), Luanda (540), Bechuanaland (542), Lourenço Marques (544), Rhodesia (545), Tanganyika (546), Stanleyville (718), Manica e Sofala (896), Zambezia-Moçambique (897) (if controlled) |

### Empower the Workers sub-branch (Communist)

Communist path with two strategic routes: Soviet alignment or Anti-Colonialist Crusade (unique liberation war branch).

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| Empower the Workers | Abandon Westminster + Britain has not enforced loyalty | Support the Afrikaner Broederbond | Modifies Abandon Westminster spirit (Daily autonomy progress: +1; Daily Democracy support: −0.03; Daily Communism support: +0.03) |
| Support Spain | Empower the Workers + Spain in civil war + (Fascism current party OR SACP >10% support) + (fully independent OR Dominion/Satellite + autonomy >65%) + Britain has not enforced loyalty | | Gets event "Support for Spain" |
| Repeal the Native Representation Act | Empower the Workers + SACP >10% support + Britain has not enforced loyalty | | Political Power: +120; Gains national spirit: Black Volunteers (Recruitable Population: +1%, War support: +5%); Modifies Ossewabrandwag spirit (Factory output: −10%, Dockyard output: −10%) |
| Equal Opportunity Employment | Repeal the Native Representation Act + Britain has not enforced loyalty | | Gains national spirit: Equal Opportunities (Factory output: +5%, Dockyard output: +5%); Removes Ossewabrandwag spirit |
| Burn the King's Portraits | Support Spain OR Repeal the Native Representation Act + SACP >35% support + (autonomy >70% OR fully independent) + Britain has not enforced loyalty | | Political Power: +120; Communism popularity: +15%; triggers "Anti-Royalist riots in South Africa" news event |
| Anti-Colonialist Crusade | Burn the King's Portraits + fully independent + Britain has not enforced loyalty | Join Comintern | Gain base War support: +10%; UK leaves Allies; UK, France, Belgium, Portugal gain Anti-Colonialist Crusaders opinion (−100) |
| Union of the African People | Anti-Colonialist Crusade + Britain has not enforced loyalty | | **If No Compromise, No Surrender DLC:** Creates faction "African People's Union" + 1 initiative point. **Otherwise:** Creates faction "African People's Union"; triggers news event. |
| Liberate Portuguese Colonies | Union of the African People + (Mozambique doesn't exist OR Angola doesn't exist) + Britain has not enforced loyalty | | Gains Conquer war goal vs Portugal; targets Luanda (540), Lourenço Marques (544) |
| Liberate Belgian Colonies | Liberate Portuguese Colonies + Zaire doesn't exist + Britain has not enforced loyalty | | Gains Conquer war goal vs Belgium; targets Coquilhatville (538), Stanleyville (718), Léopoldville (295) |
| Liberate British Colonies | Union of the African People + (Kenya doesn't exist OR Zimbabwe doesn't exist) + Britain has not enforced loyalty | | Gains Conquer war goal vs UK; targets Tanganyika (546), Nairobi (547), Uganda (548), Bechuanaland (542), Rhodesia (545) |
| Join Comintern | Burn the King's Portraits + Soviet Union is Communist faction leader + not in civil war + at peace with South Africa + fully independent + Britain has not enforced loyalty | Anti-Colonialist Crusade | **Bypass:** if already in Comintern. **Effect:** Soviet Union gets event "South Africa Requests Membership in the Comintern" |
| Support the World Revolution | Join Comintern + Britain has not enforced loyalty | | Gains national spirit: Support the World Revolution (Subversive activities cost: −50%, War support: +5%) |
| Invite Soviet Advisors | Support the World Revolution + Soviet Union exists + Britain has not enforced loyalty | | Gains national spirit: Soviet Advisors (Division Organization: +5.0%, Planning Speed: +5.0%); 1× 50% cost reduction for Land Doctrine; if has Mass Assault: +10.00% mastery bonus for 180 days, else +5.00% mastery bonus for 180 days |
| Research Treaty with USSR | South Africa: Invite Soviet Advisors; Soviet Union: exists + fully independent + Britain has not enforced loyalty | | Soviet Union gets event "Research treaty with South Africa" (must approve) |
| Demand Madagascar | Join Comintern OR Anti-Colonialist Crusade + Soviet Union agreed to Pact + France capitulated + exists + controller of Madagascar (543) is not Communist + at peace with South Africa + Britain has not enforced loyalty | | **Bypass:** if controller already at war with South Africa. **Effect:** Controller of Madagascar (543) gets event "South Africa Demands Madagascar" (must approve) |

## South African Railways branch

Industrial expansion; factories, mining, infrastructure, research slots.

| Focus | Prerequisites | Effects |
|---|---|---|---|
| South African Railways | – | If missing Civilian Train technology: gains it. 15 units of British available as design company; gains South African Railways design company (Train/Railway research: +15%, Train production cost: −25%, Train reliability: +10%, Supply Hub construction: +15%, Railway construction: +15%) |
| Expand the Mining Industry | South African Railways | Random state: +2 building slots, +2 civilian factories; 1× 100% research bonus: Excavation I–V |
| Heavy Engineering | South African Railways | 1× 100% research bonus: Industry |
| Infrastructure Effort | Expand the Mining Industry OR Heavy Engineering | 4 random owned/controlled states: +1 Infrastructure each (if free building slots) |
| Armament Effort | Infrastructure Effort | Random state: +2 building slots, +2 military factories |
| South African Steel | Infrastructure Effort + controls Transvaal (275) | Transvaal (275): +16 Steel production |
| Pretoria Arms | Armament Effort + South African Steel | Random state: +2 building slots, +2 military factories |
| Expand the Rand Mines | South African Steel | Gains national spirit: Gold Exports (Consumer Goods Factories: −5%) |
| Fund the University of South Africa | Pretoria Arms OR Expand the Rand Mines | Gain +1 research slot |
| Establish the Atomics Energy Board | Fund the University of South Africa | If missing Atomic Research: 1× 50% research bonus for Nuclear Technology. Otherwise: Gain +75.00% Nuclear Research breakthrough |
| The Cape Defense Institute | Establish the Atomics Energy Board + fully independent | Gain +1 research slot |
| Defense Collaboration Initiative | Establish the Atomics Energy Board + fully independent + at war + in faction + (own factories >50 OR faction member has >50 factories) | Gain +1 research slot |

## Special Service Battalion branch

Land doctrine and equipment research; army experience, weapons, artillery.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| Special Service Battalion | – | | Army Experience: +10; 1× 25% cost reduction for Land Doctrine |
| Improve the Three Oh Three | Special Service Battalion | | 1× 100% research bonus: Infantry Weapons |
| Q Services Corps | Special Service Battalion | | 2× 100% research bonus: Motorized, Logistics Company I–IV |
| South African Military College | Improve the Three Oh Three OR Q Services Corps | | Army Experience: +10; 1× 50% cost reduction for Land Doctrine |
| Expand the South African Artillery | Improve the Three Oh Three OR South African Military College | | 1× 100% research bonus: Support Artillery |
| SA Engineer Corps | South African Military College OR Q Services Corps | | 1× 100% research bonus: Support technology |
| Equipment Effort | Expand the South African Artillery OR SA Engineer Corps | | 1× 100% research bonus: Infantry Weapons and Support Artillery |
| Mechanization Effort | Equipment Effort | | 1× 100% research bonus: Mechanized models |
| South African Special Forces | Equipment Effort OR SA Engineer Corps | | 1× 100% research bonus: Airborne Technology, Marine technology, Mountaineers Technology; **(requires Arms Against Tyranny):** 2× 50% cost reduction: Special Forces Doctrine |
| Armor Effort | Mechanization Effort OR South African Special Forces | | 1× 100% research bonus: Armor technology |

## Commit to the Five-Year Plan branch

Air force doctrine and fighter/bomber research; air experience, air bases.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| Commit to the Five-Year Plan | – | | Air Experience: +25; Random state: +2 air bases; 1× 50% cost reduction for Air Doctrine |
| Improve the Hawker Hartbees | Commit to the Five-Year Plan | Replace the Blenheim | 1× 100% research bonus: Light Fighters |
| Replace the Blenheim | Commit to the Five-Year Plan | Improve the Hawker Hartbees | 1× 100% research bonus: Tactical Bomber models, Close Air Support models, Naval Bomber models |
| Perfect the "Cab-Rank" Technique | Improve the Hawker Hartbees OR Replace the Blenheim | | Air Experience: +25; +10.00% mastery bonus for 180 days to all Heavy Aircraft tracks |
| Desert Air Force | Perfect the "Cab-Rank" Technique | | 1× 100% research bonus: Close Air Support models |
| Secure the Cape Sea Route | Perfect the "Cab-Rank" Technique OR Replace the Blenheim | | 1× 100% research bonus: Naval Bomber models |
| Retain Experienced Pilots | Desert Air Force OR Secure the Cape Sea Route | | Air Experience: +35; 1× 50% cost reduction for Air Doctrine |

## Seaward Defense Force branch

Naval doctrine, dockyard expansion, and submarine/destroyer research; navy experience, naval bases.

| Focus | Prerequisites | Mutually exclusive | Effects |
|---|---|---|---|
| Seaward Defense Force | – | | Navy Experience: +25; Random coastal state: +1 building slot, +1 naval dockyard; 1× 50% cost reduction for Naval Doctrine |
| Protect the Trade | Seaward Defense Force | Disrupt the Trade | +10.00% mastery bonus for 240 days to all active Screens tracks |
| Disrupt the Trade | Seaward Defense Force | Protect the Trade | +10.00% mastery bonus for 240 days to all active Submarines tracks |
| Expand the Simon's Town Base | Protect the Trade OR Disrupt the Trade | | Random coastal state: +2 building slots, +2 naval dockyards; if Cape (681) controlled: add level 2 Coastal fort |
| Anti Submarine Tactics | Expand the Simon's Town Base | | −2.0 years ahead of time penalty + 100% research bonus for next Destroyer models research |
| Submarine Warfare | Expand the Simon's Town Base | | −2.0 years ahead of time penalty + 100% research bonus for next Submarine models research |
| Prepare Overseas Offensive | Anti Submarine Tactics | Strengthen the Cape Garrison Artillery | 1× 50% cost reduction for Naval Doctrine; 1× 100% research bonus: Marine technology, Transport models |
| Strengthen the Cape Garrison Artillery | Submarine Warfare | Prepare Overseas Offensive | Add level 3 Coastal fort to all home coastal provinces; add level 1 Coastal fort to all home provinces with naval bases |

## Cross-references

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focus mechanics and the base focus tree structure.
