---
title: Chinese Warlords National Focus Trees
category: focus-trees
tags: [warlords, china, political, military, industrial, shared focus tree]
game_version: "1.19"
dlc: ["No Compromise, No Surrender"]
sources:
  - https://hoi4.paradoxwikis.com/Communist_Chinese_Warlord_national_focus_tree
  - https://hoi4.paradoxwikis.com/Nationalist_Chinese_Warlord_national_focus_tree
  - https://hoi4.paradoxwikis.com/Warlords_national_focus_tree
  - https://hoi4.paradoxwikis.com/Warlords_national_focus_tree_(base_game)
---

## Summary

A shared focus tree used by 12 minor Chinese warlord factions (Gansu Ma, Guangdong Clique, Guangxi Clique, Hebei-Chahar, Khotan Ma, Ningxia Ma, Northeastern Army, Qinghai Ma, Shandong Clique, Shanxi, Sichuan Clique, Sinkiang) in the base game; the No Compromise, No Surrender DLC adds three major branches allowing warlords to unify with Nationalist China (adopting that tree), Communist China (adopting that tree), or forge an independent path. Shared branches are "Invite Foreign Investors" (industrial support) and "Develop the Capital State" (industrial planning). See [01-mechanics/national-focus.md](../01-mechanics/national-focus.md) for generic/continuous focuses.

---

## Base Game Warlords National Focus Tree

Available to Guangxi Clique, Shanxi, Sinkiang, Xibei San Ma, and Yunnan in base game (without DLC).

### Secure Internal Politics Branch

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Secure Internal Politics** | None | Political Power: +120; Non-Aligned Party Leader becomes leader of communist, fascist, and democratic parties | Entry focus |
| **Cooperation With the Nationalists** | Secure Internal Politics; mutually exclusive with Cooperation With the Communists, Opposition; at peace with Nationalist China or fully independent | Stability: +5.00%; Nationalist China gains opinion +50; Communist China gains opinion −50 | Leads to nationalist unification path |
| **Technological Cooperation** | Cooperation With the Nationalists | China and warlord join Technological Cooperation group | Research sharing benefit |
| **New Model Province** | Cooperation With the Nationalists | Stability: +10.00% | Prestige focus |
| **Root Out Corruption** | New Model Province; mutually exclusive with Embrace the Opium Trade | Removes national spirit Government Corruption | Anti-corruption path |
| **Embrace the Opium Trade** | New Model Province; mutually exclusive with Root Out Corruption | Gets national spirit Embrace the Opium Trade (Consumer Goods Factories −15%) | Revenue path (stability cost) |
| **Land Reform** | Root Out Corruption | Every owned state: +1 building slot | Peasant support |
| **Cooperation With the Communists** | Secure Internal Politics; mutually exclusive with Cooperation With the Nationalists, Opposition; at peace with Communist China or fully independent | Stability: +5.00%; Communist China gains opinion +50; Nationalist China gains opinion −50 | Leads to communist unification path |
| **Communist Technological Cooperation** | Cooperation With the Communists | China and warlord join Technological Cooperation group | Research sharing benefit |
| **Land Redistribution** | Cooperation With the Communists | Stability: +10.00% | Peasant support (communist path) |
| **Opposition** | Secure Internal Politics; mutually exclusive with Cooperation With the Nationalists, Cooperation With the Communists | Gain Border Conflict with Nationalist China and Communist China | Independent path |

### Industrial Investment Branch

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Industrial Investment** | None | Industry research bonus: 1× 100% | Entry focus |
| **Develop the Capital** | Industrial Investment; at peace | Capital state: if <4 infrastructure add 2, if <5 add 1; +1 building slot; +1 civilian factory | Capital development |
| **Expand our Industry** | Industrial Investment; at peace | Add 2 building slots, add 2 civilian factories to a random owned state | Factory expansion |
| **Develop Mining** | Industrial Investment; at peace | Add 1 building slot, add 1 civilian factory to capital state; add 1 building slot, add 1 military factory to a random state | Resource extraction |
| **Military Buildup** | Industrial Investment; at peace | Add 2 building slots, add 2 military factories to a random owned state | Armament focus |

### Strengthen Warlord Authority Branch

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Strengthen Warlord Authority** | None | Modifies national spirit Warlord State | Entry focus |
| **Cavalry Focus** | Strengthen Warlord Authority; mutually exclusive with Mountaineer Focus | Gets national spirit Cavalry Traditions (cavalry division attack +10%, cavalry division defense +5%) | Cavalry specialization |
| **Mountaineer Focus** | Strengthen Warlord Authority; mutually exclusive with Cavalry Focus | Gets national spirit Mountaineer Traditions (mountaineer division attack +10%, mountaineer division defense +5%) | Mountaineer specialization |
| **Warlord Prestige** | Cavalry Focus or Mountaineer Focus | War support: +10.00%; Political Power: +75 | Prestige and authority |

---

## DLC Warlords National Focus Tree (requires No Compromise, No Surrender)

Expands the base game tree with a major three-way split and adds country-specific branches for Sinkiang and Khotan Ma. Available to all 12 warlord tags.

### Secure Internal Politics Branch (DLC)

Same structure as base game, with mutually exclusive paths leading to three different unified focus trees.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Secure Internal Politics** | None | Political Power: +120; Non-Aligned Party Leader becomes leader of all ideologies | Entry focus |
| **Cooperation With the Nationalists** | Secure Internal Politics; mutually exclusive with Cooperation With the Communists, Opposition | Stability: +5.00%; gains Cooperation With the Nationalists opinion modifier from Nationalist China (+50) and Communists (−50); allows Border Conflicts from communist-aligned warlords | Leads to Nationalist Chinese Warlord tree |
| **Cooperation With the Communists** | Secure Internal Politics; mutually exclusive with Cooperation With the Nationalists, Opposition | Stability: +5.00%; gains Cooperation With the Communists opinion modifier from Communists (+50) and Nationalists (−50); allows Border Conflicts from nationalist-aligned warlords | Leads to Communist Chinese Warlord tree |
| **Opposition** | Secure Internal Politics; mutually exclusive with Cooperation With the Nationalists, Cooperation With the Communists | Unlocks Border Clash decisions against both Chinas; allows siding with Japan; enables proclaiming a rival government with choice of ideology and focus tree | Independent warlord path |

### Develop the Capital State Branch (DLC)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Develop the Capital State** | None | Random owned state: +2 building slots, +2 civilian factories; capital state: if <4 infrastructure add 2, else if <5 add 1 | Industrial entry |
| **Develop our Infrastructure** | Develop the Capital State | Capital state: if <4 infrastructure add 2, else if <5 add 1 | Infrastructure focus |
| **Expand Industrial Capacity** | Develop the Capital State | Random owned state with building capacity: +2 building slots, +2 civilian factories | Factory expansion |
| **Military Production** | Develop the Capital State | Random owned state with building capacity: +2 building slots, +2 military factories | Military buildup |
| **Research Cooperation** | Develop the Capital State or Develop our Infrastructure or Expand Industrial Capacity | +1 research slot | Research boost |
| **Accelerated Industrialization** | Research Cooperation and at peace | Random owned state: +1 building slot, +1 civilian factory; gets national spirit Accelerated Industrialization (construction speed +10%, production efficiency growth +5%) | Late-game industrial push |

### Strengthen Warlord Authority Branch (DLC)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Strengthen Warlord Authority** | None | Modifies national spirit Warlord State; adds authority bonuses | Entry focus |
| **Cavalry Expertise** | Strengthen Warlord Authority; mutually exclusive with Mountaineer Expertise | Gets national spirit Cavalry Expertise (cavalry division attack +10%, cavalry division defense +5%, cavalry division speed +10%) | Cavalry specialization |
| **Mountaineer Expertise** | Strengthen Warlord Authority; mutually exclusive with Cavalry Expertise | Gets national spirit Mountaineer Expertise (mountaineer division attack +10%, mountaineer division defense +5%) | Mountaineer specialization |
| **Military Readiness** | Cavalry Expertise or Mountaineer Expertise | War support: +10.00%; Political Power: +100; Army experience: +50 | Military preparation |
| **Warlord's Pride** | Military Readiness | Political Power: +150; national spirit Warlord's Pride (division attack on core territory +5%, division defense on core territory +5%) | Late prestige focus |

### Sinkiang-Exclusive Branch (requires No Compromise, No Surrender)

Available only to Sinkiang.

#### Office of Sinkiang Border Defense Branch

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Office of Sinkiang Border Defense** | None; Sinkiang only | Political Power: +100; gets national spirit Sinkiang Border Defense | Entry focus |
| **Strengthen the Garrison** | Office of Sinkiang Border Defense | War support: +10.00%; army experience: +50; gets national spirit Border Garrison (division attack on core territory +5%) | Military strengthening |
| **Establish Border Patrols** | Office of Sinkiang Border Defense; mutually exclusive with Cooperate with the USSR | Gets national spirit Border Patrols (foreign subversive activities efficiency −20%, operative recruitment time −15%, operative slot +1 if La Résistance enabled) | Espionage focus |
| **Purge Separatists** | Establish Border Patrols | Political Power: +75; Stability: +10.00%; gets national spirit Purged Separatists | Security control |

#### Cooperate with the USSR Branch (Sinkiang)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Cooperate with the USSR** | None; Sinkiang only; mutually exclusive with Establish Border Patrols | Soviet Union gains opinion +50; gets national spirit Soviet Cooperation (industrial research speed +15%, military research speed +10%) | USSR alignment path |
| **Accept Soviet Military Aid** | Cooperate with the USSR | Soviet Union lends 10 volunteer divisions (motorized); gets national spirit Soviet Military Support | Direct military support |
| **Soviet Economic Support** | Cooperate with the USSR; mutually exclusive with Accept Soviet Military Aid | Random owned state: +3 building slots, +3 civilian factories | Economic support path |
| **Sheng's Autonomy** | Soviet Cooperation or Soviet Economic Support; mutually exclusive with March into Khotan | Sheng Shicai becomes King; Sinkiang becomes fully independent; can choose to join Comintern, China (non-aligned), or oppose China; gets national spirit Sheng Shicai's Kingdom (political power +10%) | Monarchist path |

#### March into Khotan (Sinkiang)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **March into Khotan** | Either border defense path (Establish Border Patrols or Soviet Cooperation/Economic Support); not Sheng's Autonomy | Declares war on Khotan Ma; Khotan Ma becomes independent (not puppet); releases Kumul Khanate; Sinkiang can annex Khotan Ma | Military unification |
| **Expand Eastward** | March into Khotan | Sinkiang may declare war on Kashgaria for further expansion | Continued expansion option |
| **Sinkiang Autonomous SSR** | March into Khotan and Cooperate with the USSR path; mutually exclusive with the other post-Khotan options | Joins Comintern as puppet of Soviet Union; becomes Sinkiang Autonomous SSR; gets communist government; gets national spirit Soviet Puppet State (research speed +10%, production efficiency +5%, consumer goods factories −10%) | Soviet puppet path |
| **Join Nationalist China** | March into Khotan and non-cooperative with USSR; mutually exclusive with Soviet puppet or independent path | Joins China (Nationalist); Sinkiang remains non-aligned but allied; gets national spirit Nationalist Alliance | Nationalist alignment |
| **Independent Sinkiang** | March into Khotan; no USSR cooperation; mutually exclusive with Soviet puppet or Nationalist paths | Becomes fully independent with strong government; gets national spirit Sinkiang Independence (war support +10%, political power gain +10%) | Full independence path |

### Khotan Ma-Exclusive Branch (requires No Compromise, No Surrender)

Available only to Khotan Ma.

#### Undermine KMT Rule Branch

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Undermine KMT Rule** | None; Khotan Ma only | Political Power: +75; gets national spirit Anti-KMT Movement | Entry focus |
| **Uyghur Nationalism** | Undermine KMT Rule; mutually exclusive with Accept KMT Supremacy | Removes Muslim Ma Clique national spirit; becomes Khotan Emirate (changes government name); Uyghurs gain control; gets national spirit Uyghur Emirate (division attack +10%); gains claims on Soviet Central Asian territories (Ferghana region) | Uyghur independence path |
| **Accept KMT Supremacy** | Undermine KMT Rule; mutually exclusive with Uyghur Nationalism | Stability: +10.00%; joins China faction if willing; gets national spirit KMT Loyal State | Nationalist alignment |
| **British Support** | Uyghur Nationalism | United Kingdom and British Raj can send volunteers to Khotan Ma; United Kingdom gains opinion +50 | British alliance |
| **British Military Mission** | British Support | Gets British military advisors; army experience: +100; gets national spirit British Military Advisors (army organization regain +5%, planning speed +10%) | Military training |
| **Anti-Communist Defense** | Uyghur Nationalism; mutually exclusive with Sino-Soviet Pact | Gets national spirit Anti-Communist Stance (division attack against communist nations +10%, division defense against communist nations +10%); gains bonus against Chinese Soviet Republic and Sinkiang | Anti-communist focus |
| **Sino-Soviet Pact** | Uyghur Nationalism; mutually exclusive with Anti-Communist Defense | Gains claims on Soviet Central Asia; gets national spirit Soviet Alignment (research speed +10%); can declare war on Soviet territories | Soviet alignment |
| **Defense Reorganization** | Anti-Communist Defense or Sino-Soviet Pact | Army experience: +150; gets national spirit Reformed Military (division training time −15%); gets unique cavalry division template | Military preparation |

---

## Communist Chinese Warlord National Focus Tree (requires No Compromise, No Surrender)

Adopted by warlords completing "The Yan'an Incident" when aligned with Communist China. Unlocked after choosing "Cooperation With the Communists" and reaching sufficient stability.

### Strengthen the Central Secretariat Branch

Internal Politics branch focusing on Soviet alignment or independence.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Strengthen the Central Secretariat** | None | Political Power: +120 | Entry focus |
| **Toe the Soviet Line** | Strengthen the Central Secretariat; mutually exclusive with Focus on the Interior; Soviet Union ruling party same; at peace with USSR; fully independent or USSR subject | Soviet Union gains Pro-Soviet Government opinion (+50); Political Power: +50; Stability: −5.00% | Soviet alignment path |
| **Aid from Soviet Bolsheviks** | Toe the Soviet Line | Random owned state: +2 building slots, +2 civilian factories | Soviet industrial support |
| **Soviet Advisors** | Toe the Soviet Line | Pavel Mif and Otto Braun join as advisors; Political Power: +75; Army experience: +50; Command power: +10 | Soviet expertise transfer |
| **Industrialization of Nature** | Soviet Advisors or Aid from Soviet Bolsheviks | Random owned state: +1 building slot, +1 civilian factory; gets national spirit Urbanization Efforts (construction speed +5%, consumer goods factories −5%) | Industrial development |
| **Comintern Integration** | Industrialization of Nature; Soviet ruling party same; at peace with USSR; fully independent or USSR subject; not in faction or bypass if already in faction with USSR | Soviet Union receives event to recruit warlord to Comintern | Comintern membership path |
| **Focus on the Interior** | Strengthen the Central Secretariat; mutually exclusive with Toe the Soviet Line | Soviet Union gains Turned Their Backs On Us opinion (−50); Political Power: +50; Stability: +5.00% | Independence path |
| **Rally the Industry** | Focus on the Interior | Random owned state: +2 building slots, +2 civilian factories, +1 military factory | Independent industrialization |
| **Reorganize our Ranks** | Focus on the Interior | Army experience: +75; gets national spirit Rural Army (division attack +5%, division defense +5%) | Military organization |
| **Agrarian Socialism** | Rally the Industry or Reorganize our Ranks | Stability: +5.00%; Communism popularity +10.00%; gets national spirit Agrarian Socialism (political power +0.01 daily, consumer goods factories −5%) | Agrarian focus |
| **Forging our own Path** | Agrarian Socialism; fully independent; bypass if in faction | Can create factions; creates Mutual Assistance Bloc faction | Independent faction path |
| **Proclaim the People's Republic** | Comintern Integration or Forging our own Path; army strength ≥50% of Nationalist China; ≥50 factories; no Aftermath of the Long March spirit | Political Power: +150; becomes People's Republic of China; receives event | Unification path |
| **New Economic Direction** | Proclaim the People's Republic; at peace | Gets national spirit Finalized Industrial Plan (construction speed +10%, production efficiency cap +5%, production efficiency growth +5%, production efficiency base +7.50%) | Economic reorganization |
| **Move The Capital** | Proclaim the People's Republic; controls Beiping; fully independent | Changes capital to Beiping (Beijing); Beiping: +5 building slots, +3 civilian factories; Stability: +10.00% | Capital relocation |

### Land Redistribution Branch

Research and popular support expansion.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Land Redistribution** | None; bypass if no Low Popular Support spirit | Modifies Low Popular Support: Stability +4.00%, War support +4.00% | Entry focus (peasant support) |
| **Literacy Programs** | Land Redistribution | +1 research slot | Research boost |
| **China Medical University** | Literacy Programs; ≥35 factories; <5 research slots | +1 research slot | Education advancement |
| **Form the Academy of Sciences** | China Medical University; ≥70 factories; <5 research slots | +1 research slot | Research infrastructure |
| **Enforce the Three Rules** | Land Redistribution; bypass if no Low Popular Support spirit | Modifies Low Popular Support: Stability +7.00%, War support +7.00% | Discipline and trust |
| **Permit Opium Trade** | Enforce the Three Rules; mutually exclusive with Ban the Opium Trade | Gets national spirit Permit Opium Trade (consumer goods factories −15%); gets national spirit Government Corruption (political power −10%, stability −10.00%) | Revenue option (corruption cost) |
| **Ban the Opium Trade** | Enforce the Three Rules; mutually exclusive with Permit Opium Trade | Stability: +5.00% | Moral authority option |
| **Abolish the Land Rent** | Permit Opium Trade or Ban the Opium Trade; has Low Popular Support spirit; bypass if no Low Popular Support spirit | Removes Low Popular Support; Political Power: +150; Stability: +10.00% | Land reform completion |

### The Capital Base Area Sub-branch

External politics and military preparation.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The Capital Base Area** | Land Redistribution; capital state fully controlled | Capital state: if <4 infrastructure add 2, if <5 add 1; +1 building slot | Capital strengthening |
| **Prepare For War With Japan** | The Capital Base Area; not subject of Japan; bypass if at war with Japan | War support: +10.00% | Anti-Japanese preparation |
| **Anti-Japanese Expedition** | Prepare For War With Japan; not subject of Japan; conditions involving Manchukuo/Japan occupation | Unlocks Anti-Japanese Expedition decision; enables guerrilla warfare | Infiltration focus |
| **Government of National Defense** | Prepare For War With Japan; at peace with Nationalist China; fully independent; bypass if in faction | Nationalist China receives diplomatic event if leader exists; or warlord creates Government of National Defense faction | United front attempt |
| **Confrontation With the Warlords** | Government of National Defense; fully independent; bypass if conditions met for other warlords | All Chinese nations receive diplomatic events; targeted warlords receive demands | Warlord consolidation |
| **Focus on China** | The Capital Base Area; not subject of Nationalist China | Gets national spirit Focus on China (division defense on core territory +5%, division attack on core territory +5%) | Internal focus |
| **Exploit the Weak Neighbours** | Focus on China; neighboring warlords exist, weaker and not allied | Gains Annex war goal against weaker warlords | Territorial expansion |
| **Infiltration** | Focus on China; Nationalist China exists and not overlord; bypass if China is communist | Unlocks Infiltrate Nationalist Areas decisions | Infiltration tactics |
| **Revolutionary Military Commission** | Confrontation With the Warlords or Infiltration | Gets national spirit Revolutionary Military Commission (command power +20) | Military coordination |
| **Provoke Japan** | Anti-Japanese Expedition and Revolutionary Military Commission; not subject of Japan; bypass if at war with Japan or specific Manchukuo conditions | Unlocks Provoke Japan decision (25% each: Arms Factory Sabotaged, Civilian Factory Sabotaged, Bridge Blown, Patrol Ambushed) | Escalation trigger |
| **Protracted Warfare** | Provoke Japan; mutually exclusive with Mobile Warfare | Gets national spirit Protracted Warfare (division defense on core territory +20.00%) | Long-war strategy |
| **People's War** | Protracted Warfare | Gets national spirit People's War (infantry weapons production cost −10%, resistance growth in occupied states +50%) | Popular resistance |
| **Mobile Warfare** | Provoke Japan; mutually exclusive with Protracted Warfare | Gets national spirit Mobile Warfare (army organization regain +10%, division attack on core territory +20%) | Offensive strategy |
| **100 Regiments Campaign** | Mobile Warfare | Unlocks Launch 100 Regiments Offensive decision (division attack on core territory +25% for 180 days) | Major offensive |
| **Central Military Commission** | Revolutionary Military Commission | Replaces Revolutionary Military Commission with Central Military Commission (command power +10 increase, command power gain multiplier +10%) | Military centralization |
| **People's Liberation Army** | Central Military Commission | If has Red Army Weakened, remove it; get People's Liberation Army (organization regain +10%, training time −20%, reinforce rate +1%) | Army transformation |
| **People's Volunteer Army** | Central Military Commission | Gets national spirit People's Volunteer Army (max volunteer divisions +5, send volunteers tension −100%, volunteer divisions required −100%) | Volunteer corps |
| **Military Intelligence Department** | Revolutionary Military Commission | Kang Sheng joins as political advisor if available; Stability: +5.00%; Political Power: +50; random state: +1 building slot, +1 civilian factory | Espionage establishment |
| **Central Security Bureau** | Military Intelligence Department | Stability: +10.00% | Security apparatus |

### Invite Foreign Investors Branch

Shared industrial support branch. See Communist Chinese Warlord wiki page for details; summarized here as industrial and political support from major powers in exchange for economic concessions.

---

## Nationalist Chinese Warlord National Focus Tree (requires No Compromise, No Surrender)

Adopted by warlords completing their Nationalist alignment path when allied with Nationalist China. Unlocked after choosing "Cooperation With the Nationalists."

### Restoration of the Chinese Empire Branch

Imperial restoration path unique to Nationalist Warlords (distinct from Communist path).

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Restoration of the Chinese Empire** | None | Political Power: +120; gets national spirit A New Empire (stability −20%, war support −20%) | Entry focus |
| **Imperial Authority** | Restoration of the Chinese Empire; fully independent; controls Beiping | Removes Warlord State spirit; gets national spirit Imperial Authority | Authority consolidation |
| **Adopt the Twelve Symbols** | Restoration of the Chinese Empire; fully independent | Gets national spirit Imperial Symbols (national unity +10%, legitimacy +10%) | Symbolic restoration |
| **Reinstate the New Imperial Code** | Restoration of the Chinese Empire; fully independent | Modifies Low Legitimacy: Stability −20.00%, War support −20.00% | Legal framework |
| **Reestablish Xinhua Palace** | Restoration of the Chinese Empire; fully independent; controls Beiping | Beiping: +5 building slots; if <4 infrastructure add 2, else if <5 add 1 | Capital restoration |
| **Claim the Mandate of Heaven** | Adopt the Twelve Symbols and Reinstate the New Imperial Code and Reestablish Xinhua Palace; fully independent; controls Beiping | Can create factions; modifies Low Legitimacy (2): Stability −10%, War support −10% | Celestial legitimacy |
| **Five Races Under One Union** | Claim the Mandate of Heaven; fully independent | Modifies A New Empire: Political power gain +15%, army experience gain +10%, recruitable population +5%, stability +10%, construction speed +10%, research speed +8% | Multiethnic governance |
| **Zhonghua Minzu** | Five Races Under One Union; fully independent | Replaces Low Legitimacy (3) with A Legitimate Dynasty (division attack on core territory +10%, division defense on core territory +10%, stability +10%, war support +10%) | National consciousness |
| **Never Another National Protection War** | Claim the Mandate of Heaven; fully independent; bypass if all Chinese nations defeated/allied/subjugated | Hidden effect: news event; gains Annex war goals against all non-allied Chinese nations | Unification path |
| **Tianxia** | Never Another National Protection War; fully independent | Leader trait: replaces Son of Heaven with Celestial Emperor; Stability +15%, division attack +5%, division defense +5%, justify war goal time −25%, ideology drift defense +50%; if no Ineffective Bureaucracy: Political Power +150, Stability +5%, Democracy popularity +5% | Celestial mandate secured |
| **Reestablish the Beiyang Army** | Claim the Mandate of Heaven; fully independent | Gets national spirit The New Beiyang Army (army experience +0.10 daily, mobilization speed +10%, recruitable population +2%, division attack on core territory +10%, division defense on core territory +5%) | Military reform (historic) |
| **Reestablish the Wuwei Corps** | Reestablish the Beiyang Army; fully independent | Modifies The New Beiyang Army (recruitable population +5%, division defense on core territory +10%) | Imperial guards |

### Military Affairs Commission Branch

Army reorganization and reform.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Military Affairs Commission** | None | Gets national spirit Military Affairs Commission (command power +10 increase, army experience +0.05 daily) | Entry focus |
| **Fortify Shanghai** | Military Affairs Commission; Nationalist China controls Shanghai; Shanghai controlled by China | Shanghai and all provinces along southern Yangtze: set land fort level 2 (Shanghai city level 3); Shanghai coastal fort level 2 | Defense preparation |
| **The Chinese Hindenburg Line** | Fortify Shanghai; no enemy controls Shanghai or Anhui | Shanghai and Yangtze provinces: land fort level 3 (Shanghai city level 4, coastal fort level 3); Huangshan and southern Yangtze: land fort level 2 | Fortification network |
| **Army Reform** | Military Affairs Commission; bypass if no Army Corruption spirit | Unlocks Army Reform decisions (remove Army Corruption in 3 steps of 100 army experience each + 90 days; then remove Incompetent Officers for 200 army experience) | Corruption removal |
| **60 Divisions Plan** | Army Reform | Unlocks 60 Divisions Plan decision; when selected activates Bolster Our Ranks mission (−25% division training time for 180 days) | Modernization program |
| **Bureau of Investigation And Statistics** | Military Affairs Commission | Stability: +10%; if Dai Li available and China doesn't exist, Dai Li joins as political advisor (operative slots +1, agency upgrade −15%, non-core manpower +2%, foreign subversive −30%, damage to garrisons −25%, political power −0.02 daily); if La Résistance disabled: same effects as separate spirit | Secret police establishment |
| **Whampoa Military Academy** | Bureau of Investigation And Statistics | Every army leader: +1 planning skill; gets national spirit Whampoa Military Academy (army leader cost −30%, new leaders +1 starting planning, command power +20) | Officer training |

### Unified Industrial Planning Branch

Industrial and economic focus.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Unified Industrial Planning** | None | 2× 100% research bonus for Industry | Entry focus |
| **Expand the Academica Sinica** | Unified Industrial Planning; at peace or ≥70% stability | +1 research slot | Research advancement |
| **Chemical Research Institute** | Expand the Academica Sinica; ≥75 factories; <5 research slots | +1 research slot | Chemical weapons research |
| **Rural Reconstruction Movement** | Unified Industrial Planning; controls Henan, Hunan, Sichuan | Henan, Hunan, Sichuan: +1 infrastructure each | Rural development |
| **Mining Commission** | Rural Reconstruction Movement; no Economic Collapse spirit | Gets industrial concern Mining Commission (resource gain efficiency +10%, inflation penalty, consumer goods +10%, factory output −5%) | Mining industry |
| **Taiyuan Arsenal** | Mining Commission; controls Shanxi; no Economic Collapse | Shanxi: +3 building slots, +3 military factories; inflation penalty, consumer goods +10%, factory output −5% | Military production |
| **Develop the Hanyang Arsenal** | Mining Commission; no Economic Collapse | Random state: +3 building slots, +3 military factories; inflation penalty, consumer goods +10%, factory output −5% | Arsenal expansion |
| **Financial Policy** | Unified Industrial Planning | Random owned cored state: +2 building slots, +2 civilian factories | Financial stability |
| **Price Controls** | Financial Policy; has Low Inflation spirit (or better) | Reduces inflation (consumer goods −10%, factory output +5%) | Price stabilization |
| **Grain Tax** | Price Controls | Gets national spirit Grain Tax (consumer goods −10%, war support −7%, stability −7%) | Tax policy (famine risk) |
| **Reform the National Bank** | Price Controls; Low Inflation or better | Reduces inflation (consumer goods −10%, factory output +5%) | Banking reform |
| **Forced Loans** | Reform the National Bank; Low Inflation or better | Unlocks Forced Loans decision (costs 100 political power, −3% stability, −3% war support; reduces inflation; re-enactable every 90 days) | Emergency financing |

### Invite Foreign Investors Branch

Shared industrial support branch. See Nationalist Chinese Warlord wiki page for details; provides international economic and military support.

---

> ⚠️ The "Invite Foreign Investors Branch" referenced by both Communist and Nationalist warlord trees is documented on the respective wiki pages; specific focuses and effects not fully extracted here. This appears to be a shared industrial branch providing options for obtaining foreign investment and military aid (US, British, German, Soviet, Japanese depending on warlord ideology and alignment).

---

## Cross-tree Mechanics

- **Mutually Exclusive Paths:** Warlords must choose between Nationalist (nationalist tree), Communist (communist tree), or Opposition (independent path) early in their focus tree; this choice is mutually exclusive and locks out alternative trees.
- **Conditional Effects:** Many focuses have prerequisites involving faction membership, territorial control, ruler ideology, or relations with major powers (China, Soviet Union, Japan).
- **Country-Specific Branches:** Sinkiang and Khotan Ma have unique branches not available to other warlords; other warlords share the base branches.
- **Tree Conversion:** Choosing to cooperate with Nationalist or Communist China replaces the warlord tree entirely with either the Nationalist Chinese Warlord or Communist Chinese Warlord tree, respectively.
