---
title: Yugoslavian National Focus Tree
category: focus-trees
tags: [yugoslavia, focus tree, western focus, communist, industrialization, air force, army, navy, balkan]
game_version: "1.19"
dlc: [By Blood Alone, Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Yugoslavian_national_focus_tree
---

## Summary

Yugoslavia has a unique six-branch focus tree offering ideological choices (Western, Soviet, or regional communist paths), internal political divisions (centralization vs autonomy), and military modernization options. The tree emphasizes managing ethnic tensions (Croat, Slovene, Macedonian opposition) while navigating great-power alignment. Key branches specialize in industrialization, air force, army, and navy modernization.

See [Yugoslavia](../05-countries/yugoslavia.md) for the country's 1936 starting profile.

## Western Focus branch

The non-communist political branch, permitting democratic alignment or Axis membership. Centralization vs autonomy choices gate many downstream focuses.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Western Focus** | None | Recognize the Soviet Union | Political Power: +120; gains national spirit "King Peter" (Stability: +10.00%) |
| **Friendship Treaty with Italy** | Western Focus | Reinforce Old Alliances | Political Power: +50; Italy gains Opinion +25 towards Yugoslavia; requires Italy at peace with Yugoslavia and fascist |
| **Reinforce Old Alliances** | Western Focus | Friendship Treaty with Italy | UK gains Opinion +25; France gains Opinion +25; both gain "Yugoslavia Purchasing Commission" (License acceptance: +20 when trading with Yugoslavia); requires UK, France at peace and not capitulated |
| **Attract Axis Capital** | Friendship Treaty with Italy or Reinforce Old Alliances | — | Gains national spirit "Axis Investments" (Production efficiency cap: +10.00%; Production efficiency growth: +5.00%); requires Germany or Italy at peace |
| **The Brigadistas** | Friendship Treaty with Italy or Reinforce Old Alliances | — | Permits volunteer forces; gains national spirit "The Brigadistas" (Send volunteers tension limit: −40.0%; Divisions required: −30.0%) for duration of Spanish Civil War; bypassed if Spanish Civil War ended or Yugoslavia at war |
| **Attract Allied Capital** | Friendship Treaty with Italy or Reinforce Old Alliances | — | Gains national spirit "Foreign Capital" (Consumer Goods Factories: −5%) |
| **Evolution** | Attract Axis Capital or Attract Allied Capital | Limited Self-Government | Stability: −10.00%; adds 1 building slot each to Backa (45), Serbia (107), Morava (108), West Banat (764), Kosovo (802), Southern Serbia (803) |
| **Crush the Ustasa** | Evolution | Establish the Banovina of Croatia | Activates missions: "The Ustasa Uprising" and "Circumvent the Ustasa Uprising"; requires Italy at peace and Yugoslavia controls Croat regions |
| **Establish the Banovina of Croatia** | Evolution | Crush the Ustasa | Removes national spirit "Croatian Opposition"; gains national spirit "Croat Nationalism Suppressed" for 1250 days (Political Power Gain: −15%); requires Yugoslavia controls Croatia (109), Dalmatia (103), Zara (163) |
| **Limited Self-Government** | Attract Axis Capital or Attract Allied Capital | Evolution | Removes "Slovene Nationalism"; releases Drava Banovina as puppet (creates 2 Militia units); creates expansion targets for Austria if it completed "Reclaiming the Balkan Territories"; requires Yugoslavia fully independent |
| **Slovenia for Support** | Crush the Ustasa or Establish the Banovina of Croatia | Ban Slovene Nationalist Parties | Removes "Slovene Nationalism"; grants North Slovenia (102) and Ljubljana (853) to Italy or Italy's subjects; loses cores on these states; Italy gains Opinion +50; requires Italy at peace and fascist |
| **Ban Slovene Nationalist Parties** | Crush the Ustasa or Establish the Banovina of Croatia | Slovenia for Support | Removes "Slovene Nationalism"; gains national spirit "Slovene Self-Government" for 1060 days (Production efficiency growth: −5.00%); Italy gains Opinion +5; requires Italy at peace |
| **Surrender Macedonia** | Slovenia for Support or Ban Slovene Nationalist Parties | Concessions for Macedonians | Removes "Macedonian Opposition"; grants Macedonia (106) and Southern Serbia (803) to Bulgaria; loses core on Macedonia; Bulgaria gains Opinion +50; requires Bulgaria at peace |
| **Concessions for Macedonians** | Slovenia for Support or Ban Slovene Nationalist Parties | Surrender Macedonia | Removes "Macedonian Opposition"; gains national spirit "Mild Macedonian Opposition" for 1060 days (Policy costs: +10%); requires Bulgaria at peace |
| **A United Autonomous Croatia** | Limited Self-Government | A Devolved Croatia | Removes "Croatian Opposition"; releases Banovina of Croatia as puppet (creates 4 Militia units); creates expansion targets for Austria; requires Yugoslavia fully independent and controls Croatia region |
| **A Devolved Croatia** | Limited Self-Government | A United Autonomous Croatia | Removes "Croatian Opposition"; releases Banovina of Croatia as puppet (creates 2 Militia units) and Banovina of Dalmatia (creates 1 Militia unit); requires Yugoslavia fully independent and controls Croatia/Dalmatia |
| **Divide Bosnia** | A United Autonomous Croatia or A Devolved Croatia | Protect Bosnia | Releases Banovina of Herzegovina and Bosnia-Herzegovina as puppets; creates 1 Militia unit each; requires Yugoslavia fully independent and controls Bosnia/Herzegovina |
| **Protect Bosnia** | A United Autonomous Croatia or A Devolved Croatia | Divide Bosnia | Releases Banovina of Bosnia as puppet (creates 3 Militia units); requires Yugoslavia fully independent and controls Bosnia |
| **Dissolve the Banate of Serbia** | Limited Self-Government | — | Removes "Macedonian Opposition" and "Serbian General Staff"; releases Vardar Banovina (Macedonia), Autonomous Region of Kosovo, and Zeta Banovina (Montenegro) as puppets; bypassed if Yugoslavia doesn't control key states |
| **Fortify Banat** | Dissolve the Banate of Serbia | Banat for Support, Autonomy for Slavic Transylvania | West Banat (764) and Backa (45) gain 3 land forts each on border provinces; Yugoslavia becomes Serbia; requires one of: Divide Bosnia, Protect Bosnia completed |
| **Banat for Support** | Dissolve the Banate of Serbia | Fortify Banat, Autonomy for Slavic Transylvania | Romania gains West Banat (764); Hungary gains Backa (45); both gain Opinion +50 and sign Non-aggression pacts; loses cores on these states; Yugoslavia becomes Serbia; requires one of: Divide Bosnia, Protect Bosnia completed |
| **Autonomy for Slavic Transylvania** | Dissolve the Banate of Serbia | Fortify Banat, Banat for Support | Releases Autonomous Region of Transylvania and Autonomous Region of Vojvodina as puppets; Yugoslavia becomes Serbia; requires one of: Divide Bosnia, Protect Bosnia completed |
| **Invite German Military Mission** | Surrender Macedonia, Concessions for Macedonians, Fortify Banat, Banat for Support, or Autonomy for Slavic Transylvania | — | Removes national spirit "Anti-German Military"; 1× 100% research bonus for Basic/Improved/Advanced medium tanks and Mechanised infantry; requires Germany at peace |
| **Sign the Tripartite Pact** | Surrender Macedonia, Concessions for Macedonians, Fortify Banat, Banat for Support, or Autonomy for Slavic Transylvania | End the Regency | Makes Germany/Italy offer Yugoslavia faction membership; Prince Paul becomes Fascist leader; daily Fascism support: +0.10; Fascism diplomacy acceptance: +75; requires Germany/Italy at peace and fascist, Yugoslavia fully independent; bypassed if already in Tripartite faction |
| **Surrender Italian Claims** | Sign the Tripartite Pact | Zara for Axis Membership | Loses cores on Zara (163), Litorale (736), Istria (852); seeks faction membership; requires Germany leading faction OR best fascist faction leader to approve |
| **Zara for Axis Membership** | Sign the Tripartite Pact | Surrender Italian Claims | Italy gets event "Zara for Alliance"; requires Italy at peace, fascist, controls Zara (163), in faction |
| **Claim Macedonia** | Surrender Italian Claims or Zara for Axis Membership | — | Owner of Macedonia gains core on Central Macedonia (731); Yugoslavia gets event "Yugoslavia Claims Macedonia"; bypassed if Yugoslavia owns Macedonia and Macedonia is in Yugoslav faction |
| **Greater Yugoslavia** | Claim Macedonia | — | Gains claims on all core states of Bulgaria; gets event "Yugoslavia Claims Bulgaria" |
| **All-Yugoslavian Regiments** | Greater Yugoslavia | — | Gains national spirit "All-Yugoslavian Regiments" (Recruitable Population: +1.00%); may grant Vasily Flug and Boris Shteifon as generals if certain global flags not set |
| **Invite Italian Naval Experts** | Surrender Italian Claims or Zara for Axis Membership | — | Joins Yugoslavian Naval Group technology sharing with Italy; Navy experience: +50; requires Italy in faction with Yugoslavia |
| **End the Regency** | Surrender Macedonia, Concessions for Macedonians, Fortify Banat, Banat for Support, or Autonomy for Slavic Transylvania | Sign the Tripartite Pact | Prince Paul retires; Peter II becomes Non-Aligned/Democratic leader; if before Sep 6 1941 gains "Underage Monarch" trait (Stability: +10.00%; all costs: +25%), else "Legitimate Heir" (Stability: +10.00%; Political Power Gain: +10%); requires date after Jan 1 1938 |
| **The Coronation** | Sign the Tripartite Pact or End the Regency | — | If Prince Paul ruling and Western Focus completed: Paul I becomes Fascist leader; all subject nations become Fascist; Stability: +15.00%; War support: +20.00%; Non-Aligned becomes "Peter's Loyalists"; otherwise renames Non-Aligned to "House Karađorđević" |
| **A Royal Wedding** | End the Regency | — | Gets event "The Grosvenor Gala"; requires Peter II as leader and no Underage Monarch trait |
| **Enforce Yugoslav Neutrality** | The Coronation + A Royal Wedding | A Royal Alliance | Gains national spirits "Armed Neutrality" (Division attack/defense on core territory: +10.0%; Justify time on us: +10.0%) and "Neutral Foreign Policy" (Join faction tension limit: +100.0%; Send volunteers limit: +20.0%; Guarantee limit: +100.0%) |
| **Fortress Yugoslavia** | Enforce Yugoslav Neutrality | — | Adds level 3 land forts: 6 in Dalmatia (103), 5 in Croatia (109), 5 in North Slovenia (102) if controlled, 1 in Ljubljana (853) if controlled |
| **A Royal Alliance** | The Coronation + A Royal Wedding | Enforce Yugoslav Neutrality | Attempts to join faction of royal marriage partner (Allies if Princess Alexandra chosen) |
| **Allied Air Combat School** | A Royal Alliance | — | Joins Yugoslavian Air Group technology sharing with UK; requires Yugoslavia in faction with UK |
| **Towards Independence** | Fortify Banat, Banat for Support, or Autonomy for Slavic Transylvania | A United Kingdom | Every subject nation in Europe gains 25.00 autonomy; Serbia gains Opinion +50; requires Yugoslavia fully independent |
| **The Defence Army of Yugoslavia** | Towards Independence | — | Grants "Yugoslavian Defence Army" division template (non-editable, training only); creates 1 unit in random state; every subject gains template and creates 1 unit |
| **Yugoslav Defence League** | The Defence Army of Yugoslavia | — | Permits faction creation; creates/joins "Balkan Defence League"; enables Yugoslavian Defence Army template editing; all subject nations in Europe become free and join faction; creates 1 unit; requires Yugoslavia fully independent |
| **A United Kingdom** | Fortify Banat, Banat for Support, or Autonomy for Slavic Transylvania | Towards Independence | Every subject nation in Europe loses 25.00 autonomy; Serbia gains Opinion −25 |
| **Guarantee Religious Liberties** | A United Kingdom | — | Gains national spirit "Freedom of Religion Guaranteed" (Stability: +10.00%) |
| **Reunite the Kingdoms** | Guarantee Religious Liberties | — | Gains cores on all subject states' core territories; annexes all subject nations originally part of Yugoslavia, Hungary, Bulgaria (if puppets); Serbia becomes Yugoslavia |

## Recognize the Soviet Union branch

Communist political path with options to join Comintern or create independent Balkan communist faction.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Recognize the Soviet Union** | None | Western Focus | Soviet Union gains Opinion +15; Romania loses "Balkan Pact" Opinion −25; requires Soviet Union at peace, Yugoslavia not capitulated, fascist ruling party |
| **Form Peasant Councils** | Recognize the Soviet Union | — | Gains national spirit "Peasant Councils" for 730 days (Daily Communism Support: +0.20) |
| **Mutual Economic Aid** | Recognize the Soviet Union | — | Gains national spirit "Yugoslavian Economic Aid" for 720 days (Consumer Goods Factories: −5.0%); Soviet Union gains same spirit for 365 days; requires Soviet Union at peace |
| **Local Militias** | Friendship Treaty with Italy, Reinforce Old Alliances, or Form Peasant Councils | — | Gains national spirit "Local Militias" (Recruitable Population: +2.00%) |
| **Abolish the Monarchy** | Form Peasant Councils + Mutual Economic Aid | — | KPJ becomes ruling party; removes "Peasant Councils"; gains national spirit "Empowered Peasant Councils" (Ideology drift defense: +25.0%; Construction Speed: +10.00%); requires >40% communist support and fully independent |
| **Join Comintern** | Abolish the Monarchy | Yugoslavian Path to Communism | Soviet Union/best communist faction leader gets event "[YUG] seeks to join faction"; requires not in faction, fully independent, Soviet Union at peace and communist; bypassed if already in Comintern |
| **Research Collaboration** | Join Comintern | — | Joins Yugo-Soviet Research group technology sharing with Soviet Union; requires Yugoslavia in faction with Soviet Union |
| **Yugoslavian Path to Communism** | Abolish the Monarchy | Join Comintern | Replaces "Empowered Peasant Councils" with "Supreme Peasant Councils" (Ideology drift defense: +50.0%; Construction Speed: +10.00%; Division attack/defense on core territory: +10.0%); requires not in faction |
| **Form the Federal Republic** | Join Comintern or Yugoslavian Path to Communism | — | Removes national spirits "Croatian Opposition", "Macedonian Opposition", "Slovene Nationalism" |
| **Federal Defense Council** | Form the Federal Republic | — | If has "Serbian General Staff": replaces with "Federal Defense Council" (Max planning: +10%; Defense: +10.00%); if has "Yugoslavian General Staff": replaces with same spirit |
| **Pan-Slavic Worker's Congress** | Yugoslavian Path to Communism | — | Permits faction creation; creates "Pan-Slavic Worker's Congress" faction; unlocks decisions to instigate peasant uprisings in Bulgaria/Albania; gets event "The Pan-Slavic Worker's Congress"; requires fully independent and not in faction |
| **Invite Bulgaria** | Pan-Slavic Worker's Congress | — | Bulgaria gets event "[YUG] invites [Bulgaria] to [faction]"; requires Bulgaria at peace, fully independent, communist, faction leader; bypassed if Bulgaria doesn't exist, is Yugoslav puppet, in faction, or banned communism |
| **Invite Albania** | Pan-Slavic Worker's Congress | — | Albania gets event "[YUG] invites [Albania] to [faction]"; requires Albania at peace, fully independent, communist, faction leader; bypassed if similar conditions |
| **Pan-Balkan Initiative** | Federal Defense Council + Invite Bulgaria + Invite Albania | — | Renames "Pan-Slavic Worker's Congress" to "Greater Balkan Worker's Congress"; unlocks decisions for uprisings in Greece, Romania, Hungary; requires faction leader and fully independent |
| **Invite Romania** | Pan-Balkan Initiative | — | Romania gets event "[YUG] invites [Romania] to [faction]"; requires Romania at peace, fully independent, communist, faction leader; bypassed if similar conditions |
| **Invite Greece** | Pan-Balkan Initiative | — | Greece gets event "[YUG] invites [Greece] to [faction]"; requires Greece at peace, fully independent, communist, faction leader; bypassed if similar conditions |
| **Invite Hungary** | Pan-Balkan Initiative | — | Hungary gets event "[YUG] invites [Hungary] to [faction]"; requires Hungary at peace, fully independent, communist, faction leader; bypassed if similar conditions |
| **Invite Turkey** | Invite Romania + Invite Greece + Invite Hungary | — | Turkey gets event "[YUG] invites [Turkey] to [faction]"; requires Turkey at peace, fully independent, communist, faction leader; bypassed if similar conditions |

> ⚠️ Recognize the Soviet Union line contains broken wiki template `[{{{1}}}]` (should be "communist"/"fascist" ruling party) — reconstructed from context.

## Industrialization Program branch

Industrial development offering resource extraction, factory building, university expansion, and infrastructure choices.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Industrialization Program** | None | — | 2× 100% research bonus for Industry |
| **Expand the Mining Industry** | Industrialization Program | — | Gains national spirit "Expanded Mining Industry" (Resource Gain Efficiency: +10.00%) |
| **Rare Minerals Exploitation** | Expand the Mining Industry | — | If Montenegro controlled: add 8 Tungsten to Montenegro (105); else random state (priority Kosovo) gains 8 Tungsten; if Croatia controlled: add 8 Chromium to Croatia (109); else random state (priority Dalmatia) gains 8 Tungsten; requires any owned core state fully controlled |
| **Exploit the Pannonian Deposits** | Rare Minerals Exploitation | — | Adds 8 Oil to Backa (45); requires Backa fully controlled |
| **Develop Civilian Industry** | Expand the Mining Industry | Develop Military Industry | 3 random fully controlled states (priority North Slovenia, Serbia, Croatia, Ljubljana) each gain 1 building slot and 1 civilian factory |
| **Develop Military Industry** | Expand the Mining Industry | Develop Civilian Industry | Random state: +3 building slots, +3 military factories |
| **Expand the University of Zagreb** | Develop Civilian Industry or Develop Military Industry | — | +1 research slot; requires no "Croatian Opposition" |
| **Integrated Rail Network** | Expand the University of Zagreb | Improve Serbian Rail Network | +1 infrastructure to all cored/controlled states and to faction members/subjects that are/were Bosnia, Bulgaria, Croatia, Herzegovina, Kosovo, Macedonia, Montenegro, Serbia, Slovenia, Transylvania, Hungary |
| **Improve Serbian Rail Network** | Expand the University of Zagreb | Integrated Rail Network | If controlling Backa/Montenegro/Serbia/Morava/West Banat: each gains 1 building slot and 1 infrastructure |
| **Improve Light Industry** | Integrated Rail Network or Improve Serbian Rail Network | — | 2 random fully controlled states (priority Bosnia, Macedonia) each gain 1 building slot and 1 civilian factory |
| **Develop Slovenian Industry** | Integrated Rail Network | — | If Ljubljana (853) controlled by Yugoslavia/subject/Slovenia in faction: gains 3 building slots, 1 civilian factory, 2 military factories; else if North Slovenia (102): same; requires Ljubljana or North Slovenia controlled |
| **Expand the University of Ljubljana** | Develop Slovenian Industry | — | +1 research slot; requires no "Slovene Nationalism" |
| **Local Self-management** | Develop Slovenian Industry | — | Gains national spirit "Local self-management" (Construction speed: +5.00%) |
| **Serbian Steel** | Improve Serbian Rail Network | — | Morava (108): +16 Steel production; requires Morava (108) fully controlled |
| **Expand the University of Belgrade** | Improve Serbian Rail Network | — | +1 research slot |
| **Central Management** | Expand the University of Belgrade | — | Gains national spirit "Central Management" (Factory output: +5.00%) |
| **Expand the Sarajevo Arsenals** | Local Self-management or Central Management | — | If Bosnia (104) controlled by Yugoslavia/subject/Bosnia in faction: +3 building slots, 1 civilian factory, 2 military factories; requires Bosnia fully controlled |

## Modernize the Air Force branch

Air force modernization offering domestic aircraft design or foreign licensing paths, with aircraft company options.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Modernize the Air Force** | None | — | 1× 50% cost reduction for Air Doctrine |
| **Local Developers** | Modernize the Air Force | Purchase Foreign | Gains national spirit "Indigenous Designs" (Air Research Speed: +15%) |
| **Ikarus** | Local Developers | — | If Arms Against Tyranny DLC: unlocks Ikarus as light aircraft designer (+1 size, +500 factory); else unlocks as aircraft designer; random state gains 1 building slot and 1 military factory |
| **Rogozarski** | Local Developers | — | If Arms Against Tyranny DLC: unlocks Rogozarski as multi-role aircraft designer (+1 size, +500 factory); else unlocks as aircraft designer; random state gains 1 building slot and 1 military factory |
| **Zmaj** | Local Developers | — | If Arms Against Tyranny DLC: unlocks Zmaj as heavy aircraft designer (+1 size, +500 factory); else unlocks as aircraft designer; random state gains 1 building slot and 1 military factory |
| **The IK-3** | Ikarus, Rogozarski, or Zmaj | — | If By Blood Alone DLC: creates Ikarus IK-3 fighter variant; else −2.0 years AoT or 300% research bonus for next 1 fighter research |
| **Heavy Fighter Project** | The IK-3 | — | 1× 100% research bonus for Heavy Fighter models |
| **Bomber Project** | The IK-3 | — | 1× 100% research bonus for Tactical Bomber models |
| **Purchase Foreign** | Modernize the Air Force | Local Developers | Events sent to Germany, Italy, UK, France requesting aircraft sales (if at peace with Yugoslavia) |
| **License Production** | Purchase Foreign | — | Gains national spirit "License Production" (Air license purchase cost: −50%) |
| **Fighter License** | License Production | Bomber License | Gets event "Fighter Competition"; requires not researched Ikarus S-49 or Nenadovic-Mitrovic; at least one major power has modern fighter and at peace |
| **Bomber License** | License Production | Fighter License | Gets event "Bomber Competition"; requires not researched Ikarus Tajfun or Zmaj R-1; at least one major power has modern bomber and at peace |

## Army Modernization branch

Army equipment, doctrine, and combat capability improvements including motor vehicles, armor, special forces, and doctrine development.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Army Modernization** | None | — | Army experience: +25 |
| **Motorize the Cavalry** | Army Modernization | — | 1× 300% research bonus for VTZ YS-4403 |
| **Motorized Logistics** | Motorize the Cavalry | — | 2× 100% research bonus for Field Hospitals and Logistics Company |
| **Armored Cavalry** | Motorize the Cavalry | — | 1× 100% research bonus for Mechanized models |
| **Tank Conversions** | Armored Cavalry | Modern Tanks | Gains national spirit "Tank Conversions" (Conversion speed bonus: +5.00%) |
| **Modern Tanks** | Armored Cavalry | Tank Conversions | 1× 100% research bonus for Armor technology |
| **Tank Licenses** | Modern Tanks | — | Gains national spirit "Tank Licenses" (Armor license purchase cost: −50%) |
| **Small Arms** | Army Modernization | — | 1× 100% research bonus for Infantry Weapons |
| **Domestic Artillery Production** | Small Arms | — | 1× 100% research bonus for Support Artillery |
| **Anti-Tank Defenses** | Domestic Artillery Production | — | 1× 300% research bonus for Anti-Tank |
| **Mountain Brigades** | Army Modernization | — | 1× 300% research bonus for Mountaineers Technology |
| **Independent Engineer Regiments** | Mountain Brigades | — | 1× 300% research bonus for Engineers Technology |
| **Motorized Recon Companies** | Independent Engineer Regiments | — | 1× 300% research bonus for Reconnaissance Company |
| **Form Parachute Battalions** | Motorized Recon Companies | — | 1× 300% research bonus for Airborne Technology |
| **Army Maneuvers** | Army Modernization | — | 1× 50% cost reduction for Land Doctrine |
| **Supremacy of Offense** | Army Maneuvers | Supremacy of Defense | +10.00% mastery for 180 days to all active Combat Support and Armor tracks; 1× 25% cost reduction for Land Doctrine |
| **Supremacy of Defense** | Army Maneuvers | Supremacy of Offense | +10.00% mastery for 180 days to all active Infantry and Operations tracks; 1× 25% cost reduction for Land Doctrine |
| **Artillery Regiments** | Supremacy of Offense or Supremacy of Defense | — | Gains national spirit "Artillery Regiments" (Towed Artillery Production Cost: −5.00%) |
| **Extreme Bravery** | Artillery Regiments | — | Permits Medal for Extreme Bravery award to field officers; requires By Blood Alone DLC and any neighbor major country at war with Yugoslavia |

## Expand the Shipyards branch

Naval development offering doctrine improvements, ship construction, and coastal defenses.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Expand the Split Shipyards** | None | Expand the Serbian Shipyards | Dalmatia (103): +2 building slots, +2 naval dockyards; requires Yugoslavia or faction member controls Dalmatia |
| **Contest the Adriatic** | Expand the Split Shipyards | — | 2× 50% cost reduction for Naval Doctrine; requires any owned state is coastal |
| **Replace the Dalmacija** | Contest the Adriatic | — | 1× 100% research bonus for Cruiser models; requires any owned state is coastal |
| **Heavy Cruiser Project** | Replace the Dalmacija | — | 1× 100% research bonus for Heavy Cruiser models; requires any owned state is coastal |
| **Expand the Serbian Shipyards** | None | Expand the Split Shipyards | Montenegro (105): +2 building slots, +2 naval dockyards; requires Yugoslavia or faction member controls Montenegro |
| **Coastal Defense** | Expand the Serbian Shipyards | — | Dalmatia (103): +2 coastal forts on coastline, +1 at naval base; Montenegro (105): +2 coastal forts on coastline, +1 at naval base; requires control of Dalmatia or Montenegro |
| **Naval Bombers** | Contest the Adriatic or Coastal Defense | — | 1× 100% research bonus for Naval Bomber models; requires any owned state is coastal |
| **Modern Destroyers** | Naval Bombers | — | 1× 100% research bonus for Destroyer models; requires any owned state is coastal |
| **Expand the Submarine Fleet** | Coastal Defense | — | 1× 100% research bonus for Submarine models; requires any owned state is coastal |

> ⚠️ Broken wiki templates `[{{{1}}}]` appear in Sign the Tripartite Pact, End the Regency, The Coronation, and Recognize the Soviet Union lines — reconstructed from context as ruling party ideology references (Fascist, Non-Aligned, Communist).
