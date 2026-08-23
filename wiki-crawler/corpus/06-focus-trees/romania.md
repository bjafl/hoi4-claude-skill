---
title: Romanian National Focus Tree
category: focus-trees
tags: [Romania, national focus, political, military, industrial]
game_version: "1.19"
dlc: [Arms Against Tyranny, Battle for the Bosporus, By Blood Alone]
sources:
  - https://hoi4.paradoxwikis.com/Romanian_national_focus_tree
---

## Summary

Romania has a unique national focus tree divided into seven branches: Preserve Greater Romania (foreign alliances), Civil Works/National Defense Industry (economic development), Balkans Dominance (regional military expansion), Institute Royal Dictatorship (domestic politics), Expand the Air Force, Army Maneuvers, and Expand the Galati Shipyards. The tree features non-mutually-exclusive ideological choices (unlike most trees) and extensive branching based on political path.

See [Romania](../05-countries/romania.md) for the country's 1936 starting profile.

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic and continuous focuses.

## Preserve Greater Romania Branch

Political branch handling foreign alliances and ideological paths. This root focus is mutually exclusive with Balkans Dominance; other ideologies within this branch are non-mutually-exclusive.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Preserve Greater Romania** | None | Mutually exclusive: Balkans Dominance. National spirit: Preserve Greater Romania (Guarantee tension limit −100%, Guarantee cost −50%) | Root of alliance-focused path |
| **A Deal With the Devil** | Preserve Greater Romania; at peace with USSR; USSR exists, fully independent, not in civil war | Communist popularity +10%. Gains opinion modifier "A Deal With the Devil" (+40) with USSR. USSR gains same modifier toward Romania (+40) | Opens Soviet path |
| **Form Peasant Militias** | A Deal With the Devil | National spirit: A Deal With the Devil (Communist support +0.01/day, Recruitable population +1.00%) | Communist political development |
| **Basing Rights for Soviet Union** | A Deal With the Devil; not in faction | Bypasses if Romania in faction with USSR. USSR gets event "Romania offers bases" (bypass condition) | Soviet military alliance |
| **Romanian Volunteer Brigades** | Basing Rights for Soviet Union | National spirit: Romanian Volunteer Brigades (Divisions required for sending volunteer force −100%, max volunteer force divisions +1, enables volunteer force sending) | Enables intervention in other conflicts |
| **Join Comintern** | Basing Rights for Soviet Union; not in faction; at peace with USSR; fully independent; USSR is faction leader. Any other country not in USSR faction, at peace with Romania | Bypasses if Romania in faction with USSR. USSR gets event "Romania seeks to join the Comintern" | Soviet alliance formalized |
| **Trade Treaty With Germany** | Preserve Greater Romania; at peace with Germany | Fascist popularity +5.00%. Trade relations with Germany +25, Germany gains same toward Romania | Opens Axis economic path |
| **Invite German Advisors** | Trade Treaty With Germany; at peace with Germany; either not in faction OR in faction with Germany | Permits Germany to station troops on Romanian soil. 2× 35% cost reduction for Land Doctrine | German military cooperation |
| **License German Equipment** | Invite German Advisors; either not in faction OR in faction with Germany | License German Equipment when dealing with Germany. License acceptance +20%, license production speed +25%, technology difference bonus +25% | German equipment access |
| **Join the Axis** | Invite German Advisors; not in faction; at peace with Germany; fully independent; Germany is faction leader; other countries not in Germany faction, at peace with Romania | Bypasses if Romania in faction with Germany. Germany gets event "Romania seeks to join the Axis" | Axis alliance formalized |
| **German-Romanian Oil Exploitation Company** | Join the Axis; in faction with Germany; Germany exists and fully independent | Random owned controlled state (prioritize Muntenia 46): Add 8 oil production. Germany gains 4 oil production in random owned controlled state | Economic cooperation; Muntenia oil priority |
| **Demand Transnistria** | Join the Axis; USSR owns and controls Balta-Tiraspol (834) | War goal against USSR (Conquer) | Expansion toward Soviet Union |
| **Renew Romanian-Polish Alliance** | Preserve Greater Romania; at peace with Poland; fully independent; Poland exists and fully independent | Democratic popularity +5.00%. Poland gets event "Romania wants to restore the Alliance" | Opens Western democratic path |
| **The Cordon Sanitaire** | Renew Romanian-Polish Alliance; not in faction; fully independent; has not capitulated; at least one of Poland or Czechoslovakia exists | Sets rule: Can Create Factions. Creates Cordon Sanitaire faction. Poland and Czechoslovakia (if existing, not capitulated, not subject, not in faction) get event "The Cordon Sanitaire" | Anti-ideological bloc with Poland/Czechoslovakia |
| **Demand a Western Guarantee** | Renew Romanian-Polish Alliance; fully independent; at peace with UK and France; UK fully independent; specific faction conditions | Bypasses if in faction with UK or France. France gets event "Romania demands Guarantee" (conditions on UK democratic status and faction membership); if UK not democratic or not in same faction, France is faction leader and gets event; if neither condition met, UK gets event | Western protection sought |
| **Military Modernization** | Demand a Western Guarantee | License Military Modernization when dealing with UK. License acceptance +60%, license production speed +25%, technology difference bonus +25% | British military cooperation |
| **Join the Allies** | Demand a Western Guarantee; not in faction; at peace with UK; fully independent; UK is faction leader and democratic; other countries not in UK faction, at peace with Romania | Bypasses if in faction with UK. UK gets event "Romania seeks to join the Allies" | Allies alliance formalized |
| **Joint Allied Staff College** | Join the Allies AND Military Modernization | 2× 35% cost reduction for Land Doctrine | Allied military cooperation |

## Civil Works / National Defense Industry Sub-branch

Industrial sub-branch enabling economic development. Accessible after starting either Preserve Greater Romania or Balkans Dominance.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Civil Works** | Preserve Greater Romania | 2× 100% research bonus for Industry | Industrial research boost |
| **National Defense Industry** | Balkans Dominance | Random owned controlled state (prioritize Oltenia 81, Moldova 79): Add 2 building slots + 1 military factory. Random owned controlled state (prioritize Oltenia 81, Moldova 79): Add 1 building slot + 1 military factory | Military factory expansion |
| **Agrarian Reform** | Civil Works OR National Defense Industry | National spirit: Agrarian Reform (Consumer goods factories −5%) | Sector restructuring |
| **Danubian Transport Network** | Agrarian Reform | 3 random owned controlled states: Add 1 infrastructure each | Transport improvement |
| **MALAXA** | Danubian Transport Network | Mutually exclusive: Invite Foreign Motor Companies. Random owned controlled state (prioritize Moldova 79): Add 3 building slots + 3 civilian factories | Domestic automobile industry |
| **Invite Foreign Motor Companies** | Danubian Transport Network | Mutually exclusive: MALAXA. Gets event "Invite Foreign Motor Companies" | Foreign licensing path |
| **Hunedoara Steel Works** | MALAXA OR Invite Foreign Motor Companies | Random owned controlled state (prioritize Transylvania 84): Add 2 building slots + 2 civilian factories + 12 steel production | Steel capacity expansion |
| **Invest In the IAR** | MALAXA OR Invite Foreign Motor Companies | Random owned controlled state (prioritize Oltenia 81): Add 3 building slots + 3 military factories. If Arms Against Tyranny enabled: IAR available as MIO (Light Aircraft Designer), gains 1 size + Heavy Armed Aircraft trait (air attack +5%, ground attack +5%), funds +2500. Otherwise: IAR design company grants air research +5%, fighter air attack +10%, carrier fighter air attack +10%, CAS ground attack +10%, carrier CAS ground attack +10% | Aircraft industry with Arms Against Tyranny MIO option |
| **Expand Ploiesti Oil Production** | Hunedoara Steel Works AND Invest In the IAR; has full control of Muntenia (46) | Muntenia (46): Add 24 oil production | Major oil resource exploitation |
| **Expand the University of Bucharest** | Expand Ploiesti Oil Production; has more than 50 factories | Gain 1 research slot | Research capacity |
| **Exploit the Baita Mines** | Expand the University of Bucharest | National spirit: Exploit the Baita Mines (Nuclear reactor construction speed +25%) | Uranium exploitation; nuclear focus |

## Balkans Dominance Branch

Political branch focusing on regional military expansion through puppet states and conquest. Root mutually exclusive with Preserve Greater Romania.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Balkans Dominance** | None | Mutually exclusive: Preserve Greater Romania. National spirit: Balkans Dominance (War goal justify time −25%, can create factions). Replaces "The Balkan Pact" (+25 opinion) with "Incongruous Neighbors" (−30 opinion) toward Bulgaria and Hungary; all countries with Balkan Pact toward Romania lose it and gain Incongruous Neighbors | Root of regional dominance path; reshapes neighbor relations |
| **Puppet Bulgaria** | Balkans Dominance; fully independent; 150%+ army strength vs Bulgaria; 400K+ manpower in divisions; Bulgaria exists, fully independent, at peace with Romania | Bypasses if Bulgaria is puppet/doesn't exist or (not at war, capitulated, Romania controls Sofia 48 + Plovdiv 212 + Burgas 211 + Moesia 801). Bulgaria gets event "Romanian Pressure" | Bulgarian subjugation |
| **Secure Greece** | Puppet Bulgaria; fully independent; 100%+ army strength vs Greece; 500K+ manpower in divisions; Greece exists, not in faction with Romania | Bypasses if Greece is puppet of Romania/doesn't exist. Gains Puppet (Focus) war goal vs Greece | Greek containment |
| **Secure the Bosporus** | Secure Greece; fully independent; 150%+ army strength vs Turkey; 750K+ manpower in divisions; Turkey exists, at peace with Romania | Bypasses if Turkey is puppet of Romania. Gains Puppet (Focus) war goal vs Turkey | Turkish control; Mediterranean access |
| **Divide Yugoslavia** | Puppet Bulgaria; fully independent; 150%+ army strength vs Yugoslavia; 500K+ manpower in divisions; Yugoslavia exists, fully independent, not in faction with Romania | Bypasses if Yugoslavia at war, is subject of Romania, or doesn't exist; OR if Romania has war goal vs Yugoslavia. If Yugoslavia at war or subject: gains annex war goal vs Yugoslavia. Otherwise: unlocks "The Partition of Yugoslavia" decisions. Gains flag invited_to_split_yugo | Yugoslav partition |
| **Align Hungary** | Balkans Dominance; fully independent; 150%+ army strength vs Hungary; 400K+ manpower in divisions; Hungary exists, at peace with Romania | Bypasses if Hungary is puppet of Romania/doesn't exist. Hungary gets event "Romania demands changes to the government" | Hungarian pressure |
| **Split Czechoslovakia** | Align Hungary; 150%+ army strength vs Czechoslovakia; 500K+ manpower in divisions; Czechoslovakia exists and fully independent | Germany gets event "Romania offers to split Czechoslovakia" | German coordination on Czechoslovakia |

## Institute Royal Dictatorship Branch

Political branch managing the King's power and Romania's domestic ideology. Extensive branching with conditional focusing and government changes.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Institute Royal Dictatorship** | Independent; less than 50% support for PCR (communist), Garda de Fier, or Frontul Renasterii Nationale | Political power +120. Carol II becomes leader (Non-Aligned, Hedonist). Stability −5.00%. Politics: FRN becomes ruling party. No public elections. Loses national spirit: Neutral Foreign Policy | Royal dictatorship established |
| **Fortify the Borders** | Institute Royal Dictatorship | National spirit: Fortify the Borders (Land fort construction +20.00%, Coastal fort construction +20.00%) | Border defense focus |
| **Revise the Constitution** | Institute Royal Dictatorship | Bypasses if Carol II is not country leader. Carol II gains traits: Camarilla Leader (Trade laws cost −25%, Conscription cost −25%, Economy cost −25%, High command cost −25%, Air chief cost −25%, Army chief cost −25%, Navy chief cost −25%). National spirit: The Sentinel of the Motherland (Recruitable population +1.00%) | Constitutional reinforcement of royal power |
| **His Majesty's Loyal Government** | Align Hungary AND Fortify the Borders AND Revise the Constitution; mutually exclusive: Flexible Foreign Policy; fully independent; current party is Non-Aligned; Carol II is leader; one of following true: Hungary aligned OR Hungary is subject of Romania OR Romania owns North Transdanubia (155) + Tiszántúl (154) + Northern Hungary (43) + Burgenland (975) + Steiermark-Kärnten (976) | Political power +120 | Loyalist government path |
| **Militarize the Sentinels** | His Majesty's Loyal Government; current party Non-Aligned; Carol II is leader | Modifies The Sentinel of the Motherland: Division recovery rate +10.0%, Recruitable population +1.00% | Paramilitary militarization |
| **All Parties Must End** | Militarize the Sentinels; current party Non-Aligned; Carol II is leader | Replaces King Carol II's Lifestyle with King Carol II (Democratic support +0.02/day). Carol II loses Hedonist trait (Stability −5.00%) | Carol II political reformation |
| **Flexible Foreign Policy** | Revise the Constitution; mutually exclusive: His Majesty's Loyal Government; fully independent | National spirit: Flexible Foreign Policy (Improve relations maintain cost −50%) | Pragmatic diplomacy path |
| **Appoint Pro-Allied Government** | Flexible Foreign Policy; independent; UK is faction leader; current party is Democratic | Removes national spirits: Iron Guard, National Christian Party, Securitate. If Flexible Foreign Policy not previously modified: modify by adding join faction tension limit −100.0%, democratic popularity +35.00%, unlocks Change of Allegiance decisions and decision to Join the Allies, stability −5.00%. Gains opinion +20 with UK; UK gains opinion +20 toward Romania | Democratic Allied alignment |
| **Constitutional Guarantees** | Appoint Pro-Allied Government | National spirit: Constitutional Guarantees (Factory output +5.00%). Removes national spirits: Iron Guard, National Christian Party, Securitate | Constitutional democratic safeguards |
| **Handle the King** | Constitutional Guarantees; mutually exclusive: Force Abdication; fully independent; Carol II is leader OR current party is Democratic | If Carol II is leader: Carol II retires, PNL becomes ruling party, public elections held. Replaces King Carol II's Lifestyle with King Carol II (Democratic support +0.02/day) | Carol II removed from power (democratic path) |
| **Appoint Pro-Soviet Government** | Flexible Foreign Policy; independent; USSR is faction leader; current party is Communist | Removes national spirits: Constitutional Guarantees, National Christian Party, Iron Guard. If Flexible Foreign Policy not previously modified: modify by join faction tension limit −100.0%, communist popularity +35.00%, stability −5.00%, gain opinion +20 with USSR (USSR reciprocates). If Battle for the Bosporus enabled and not in faction with Turkey as faction leader: every country with Balkan Pact loses it toward Romania; Bulgaria and Hungary lose Balkan Pact (−30) and gain Incongruous Neighbors (−30). Unlocks Change of Allegiance decisions and decision to Join the Comintern | Communist Soviet alignment |
| **Securitate** | Appoint Pro-Soviet Government | If doesn't have Securitate national spirit: gains national spirit Securitate (Foreign subversive activities efficiency −40%, Damage to garrisons −10.00%). If has Constitutional Guarantees: removes Constitutional Guarantees, National Christian Party, Iron Guard | Secret police establishment (Soviet path) |
| **Appoint Pro-Axis Government** | Flexible Foreign Policy; independent; Germany is faction leader; current party is Fascist | Removes national spirits: Constitutional Guarantees, National Christian Party, Securitate. If Flexible Foreign Policy not previously modified: modify by join faction tension limit −100.0%, fascist popularity +35.00%, stability −5.00%. Mihail Strudza available as political advisor (Fascist demagogue, communist support +0.10/day). Gains opinion +20 with Germany (Germany reciprocates). If Battle for the Bosporus enabled and not in faction with Turkey as faction leader: Romania loses Balkan Pact toward all holders; Bulgaria and Hungary lose Balkan Pact (−30) and gain Incongruous Neighbors (−30). Unlocks Change of Allegiance decisions and decision to Join the Axis. Cancels guarantee independence with Yugoslavia, Czechoslovakia, Greece, Turkey; gains West Banat (764) claim | Fascist Axis alignment; regional claims |
| **Iron Guard** | Appoint Pro-Axis Government; mutually exclusive: National Christian Party | Ion Antonescu becomes Fascist party leader (Conducător). Non-core manpower +2.00%, foreign subversive activities efficiency +30%, damage to garrisons −25.00%. Ion Antonescu stops being Chief of Army/Field Marshal. Fascist party renamed to Garda de Fier. Removes national spirits: The Sentinel of the Motherland, Constitutional Guarantees, National Christian Party, Securitate. National spirit: Iron Guard (Land fort construction −20.00%, Foreign subversive activities efficiency −20%, Division attack on core +5.00%, Division defense on core +5.00%) | Extreme fascist path |
| **National Christian Party** | Appoint Pro-Axis Government; mutually exclusive: Iron Guard | Octavian Goga becomes Fascist party leader (Anti-Democrat). Stability +10.00%, Democratic support −0.02/day, Democratic diplomacy acceptance −50. Fascist party renamed to Partidul National Crestin. Removes national spirits: The Sentinel of the Motherland. National spirit: National Christian Party (Consumer goods factories −5.00%). Removes: Constitutional Guarantees, Iron Guard, Securitate | Conservative fascist path |
| **Force Abdication** | Securitate OR Iron Guard OR National Christian Party; mutually exclusive: Handle the King; fully independent; more than 35% support for PNL OR PCR OR Garda de Fier | Carol II retires. If democracy > communism and democracy > fascism: PNL becomes ruling party, public elections held. If communism > fascism and communism > democracy: PCR becomes ruling party, no elections. If fascism > communism and fascism > democracy: Garda de Fier becomes ruling party, no elections. Replaces King Carol II's Lifestyle with Figurehead King Michael (Stability +5.00%). Removes The Sentinel of the Motherland if present. Gains for 360 days: King Carol Emptied Accounts (Consumer goods factories +15%, Political power gain −0.25/day). News event "King Carol II Abdicates" in 1 day | Carol II abdication; Michael I assumed kingship |
| **King Michael's Coup** | Force Abdication; independent; at war OR more than 25% world tension | If Poland has Michael I as leader: Romania known as Provisional Kingdom of Poland-Romania, FRN becomes ruling party, no elections, Romania becomes personal union puppet of Poland. Otherwise: Michael I becomes Democratic party leader, PNL becomes ruling party, public elections held. Removes Iron Guard if present. Unlocks decisions: Join the Allies, Join the Axis, Join the Comintern | Michael I coup; conditional Polish union |
| **The Royal Foundation** | Revise the Constitution | Gain 1 research slot | Cultural research foundation |
| **Crack Down on Extremism** | Institute Royal Dictatorship; fully independent; has not completed Iron Guard or National Christian Party | Ion Antonescu becomes Fascist party leader (Conducător). Non-core manpower +2.00%, foreign subversive activities efficiency −35%, division attack on core +5.00%, damage to garrisons −25.00%. Ion Antonescu stops being Chief of Army/Field Marshal. Fascist party renamed to Garda de Fier | Moderate fascism under military control |

## Expand the Air Force Branch

Air force branch developing Romanian aviation, fighter production, and bombing capabilities.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Expand the Air Force** | None | Air experience +25. Random owned controlled state (prioritize Muntenia 46, Moldova 79): Add 3 air bases. Random owned controlled state (prioritize Muntenia 46, Moldova 79): Add 3 air bases | Air force foundation |
| **The White Squadron** | Expand the Air Force; at war | National spirit: White Squadron (Experienced soldier losses −10.0%) | Air ambulance service (women pilots); morale boost |
| **Acquire Licenses** | Expand the Air Force; mutually exclusive: Local Development | National spirit: Acquire Licenses (Air license purchase cost −50%, License production speed from tech difference +20%) | Foreign aircraft licensing |
| **Air Defense** | Acquire Licenses; mutually exclusive: Ground Support | +20.00% mastery bonus for 240 days to all Operational Integrity tracks. 1× 50% cost reduction for Air Doctrine | Anti-air focus |
| **Aquire Fighters** | Air Defense; doesn't have IAR 109G or IAR 410; must have modern fighter offer and be at peace with at least one of: Germany, France, Italy, UK, USA | Gets event "Fighter Competition" | Fighter procurement via competition |
| **Ground Support** | Acquire Licenses; mutually exclusive: Air Defense | +20.00% mastery bonus for 240 days to all Battlefield Support tracks. 1× 50% cost reduction for Air Doctrine | CAS focus |
| **Medium Bombers** | Ground Support | 1× 100% research bonus for Tactical Bomber models | Tactical bomber research |
| **Local Development** | Expand the Air Force; mutually exclusive: Acquire Licenses | National spirit: Local Development (Fighter production cost −10.00%, Carrier fighter −10.00%, CAS −10.00%, Carrier CAS −10.00%, CV naval bomber −10.00%, Naval bomber −10.00%, Tactical bomber −10.00%, Heavy fighter −10.00%, Strategic bomber −10.00%, Ace generation chance +10.00%) | Domestic aircraft production cost reduction |
| **Air Superiority** | Local Development; mutually exclusive: Strategic Bomber Force | +10.00% mastery bonus for 240 days to all Fighter Aircraft tracks | Fighter mastery emphasis |
| **IAR 80** | Air Superiority | If By Blood Alone not enabled: (If Fighter II researched: 2-year ahead of time reduction + 100% bonus for next Light Fighter research). Otherwise: (If Improved Small Airframe not researched: 2-year ahead of time reduction + 100% bonus for Improved Small Airframe research; creates IAR 80 fighter variant). Otherwise: creates IAR 80 on Improved Small Airframe gain | Romanian fighter development |
| **CAS** | Air Superiority | 1× 100% research bonus for Close Air Support models | CAS aircraft research |
| **Strategic Bomber Force** | Local Development; mutually exclusive: Air Superiority | 1× 100% research bonus for Strategic Bomber models | Strategic bombing emphasis |
| **Heavy Bombers** | Strategic Bomber Force | 1× 100% research bonus for Strategic Bomber models | Heavy bomber research |
| **Nuclear Bomb Project** | Heavy Bombers | Breakthrough progress: Nuclear Research +75.00%. 1× 100% research bonus for Nuclear Technology | Nuclear weapons development |

## Army Maneuvers Branch

Army branch developing ground forces, infantry, armor, and tank destroyer capabilities.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Army Maneuvers** | None | Army experience +50 | Army foundation |
| **Army War College** | Army Maneuvers | National spirit: Army War College (Army leader cost −30.0%). 2-skill general Barbu Paraianu appears | Leadership training |
| **The ZB-53** | Army War College | 1× 100% research bonus for Infantry Weapons | Infantry equipment modernization |
| **Vanatori De Munte** | The ZB-53; has researched Mountain Infantry I | Gain Mountaineer unit with 9 battalions. 1× 100% research bonus for Mountaineers technology | Mountain infantry specialization |
| **Artillery Modernization** | The ZB-53 | 1× 100% research bonus for Support Artillery | Artillery upgrade |
| **Mountain Artillery** | Vanatori De Munte AND Artillery Modernization | Enables Mountain Gun Artillery (Mountains: attack +8%, movement +15%) and Anti-Tank (Mountains: attack +8%, movement +15%) | Mountain warfare support |
| **Modern AT Guns** | Artillery Modernization; mutually exclusive: Mobile Tank Destroyers | 2× 75% research bonus for Anti-Tank | Anti-tank gun focus |
| **Royal Guards Divisions** | Army Maneuvers | Gain unit with 7 infantry + 2 artillery battalions | Elite guard formation |
| **Reserve Divisions** | Royal Guards Divisions; mutually exclusive: The Armored Division | National spirit: Reserve Divisions (Recruitable population factor +7%) | Reserve manpower expansion |
| **The Armored Division** | Royal Guards Divisions; has buildable light tank OR medium tank; mutually exclusive: Reserve Divisions | Gain 2 units with 4 motorized + engineer company + support artillery and (if Basic Medium Tank Chassis researched: 4 medium tanks; else: 4 light tanks). If cavalry recon researched: adds cavalry recon | Armored division formation |
| **Acquire Modern Tanks** | Reserve Divisions OR The Armored Division | National spirit: Aquire Modern Tanks (Armor license purchase cost −25%) | Tank licensing |
| **Mobile Tank Destroyers** | Artillery Modernization AND Acquire Modern Tanks; mutually exclusive: Modern AT Guns | If Arms Against Tyranny enabled: Leonidas Works available as MIO (Mobile Tank Destroyers), funds +2500. Otherwise: Leonidas Works design company grants Armor research +5%, Light Tank Destroyer (Reliability +20%, Hard attack +5%, Piercing +5%), Medium Tank Destroyer (Reliability +20%, Hard attack +5%, Piercing +5%), Heavy Tank Destroyer (Reliability +20%, Hard attack +5%, Piercing +5%), Armor (Reliability +5%, tank designer, conversion speed +10.00%) | Tank destroyer focus with Arms Against Tyranny MIO option |
| **The Maresal** | Mobile Tank Destroyers | 2-year ahead of time reduction + 100% research bonus for Heavy Tank models | Heavy tank destroyer development |

## Expand the Galati Shipyards Branch

Naval branch developing naval capacity, coastal defense, and Black Sea dominance.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Expand the Galati Shipyards** | None | Navy experience +25. Random owned controlled state: Add 2 building slots + 2 naval dockyards | Naval foundation |
| **Coastal Defense Navy** | Expand the Galati Shipyards; mutually exclusive: Black Sea Dominance | If Arms Against Tyranny enabled: Galati Shipyards available as MIO (Coastal Defense Production), funds +2500. Otherwise: Galati Shipyard design company grants Naval research +15%, Light hull (Light attack +10%, Max range −50%, Production cost −20.00%), Cruiser (Light attack +10%, Max range −50%, Production cost −20.00%) | Coastal defense focus with Arms Against Tyranny MIO option |
| **Coastal Defense Ships** | Coastal Defense Navy | National spirit: Coastal Defense Ships (Cruiser: armor +20%, light attack +10%, production cost −10.00%). Adds technology Coastal Defence Ships | Coastal ship design |
| **Torpedo Boats** | Coastal Defense Ships | Modifies Coastal Defense Ships to: (Cruiser: armor +20%, heavy attack +10%, production cost −10.00%; Light hull: torpedo attack +20%) | Torpedo emphasis |
| **Black Sea Dominance** | Expand the Galati Shipyards; mutually exclusive: Coastal Defense Navy | If Arms Against Tyranny enabled: Braila Shipyards available as MIO (Battle Line Ship Builders), funds +2500. Otherwise: Braila Shipyards design company grants Naval research +15%, Cruiser (Heavy attack +20%, max range −50%, armor +20%), Heavy ship (Heavy attack +20%, max range −50%, armor +20%) | Capital ship focus with Arms Against Tyranny MIO option |
| **Modern Destroyers** | Coastal Defense Navy OR Black Sea Dominance | 1× 300% research bonus for Destroyer models | Destroyer development |
| **Modern Submarines** | Modern Destroyers | 1× 100% research bonus for Submarine models | Submarine warfare capability |
| **Torpedo Bombers** | Modern Destroyers | 1× 100% research bonus for Naval Bomber models | Naval air support |
| **Capital Ships** | Black Sea Dominance | 2× 100% research bonus for Heavy Cruiser models, Battleship models, Battlecruiser models | Capital ship development |
| **Expand the Marine Regiment** | Capital Ships | 2× 50% research bonus for Transport models and Marine technology. If Arms Against Tyranny enabled: 2× 50% cost reduction for Special Forces Doctrine | Naval invasion capability |
