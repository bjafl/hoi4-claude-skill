---
title: Norwegian National Focus Tree
category: focus-trees
tags: [norway, national focus tree, nordic, arms against tyranny, communist, democratic, fascist, monarchist]
game_version: "1.19"
dlc: [Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Norwegian_national_focus_tree
---

## Summary

Norway's unique focus tree (requires Arms Against Tyranny DLC) branches into communist, democratic, fascist, and monarchist paths with shared military and industrial development. The communist branch splits between Stalinist/Soviet alignment and Trotskyist permanent revolution; the democratic path diverges at government direction (historical neutrality vs. aggressive preparation); the fascist/monarchist branch allows fascist coup or monarchist restoration with Nordic expansion claims. The Nordic Council joint-focus system allows coordination with Denmark, Finland, Iceland, and Sweden.

See [Norway](../05-countries/norway.md) for the country's 1936 starting profile.

## A Resurgent Labor Movement Branch

Communist start branch (mutually exclusive with Vote of No Confidence, Continue Nygaardsvold's Government, The Stumbling Storting).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **A Resurgent Labor Movement** | None | Political Power +100; Removes Anti-Communist Sentiment spirit; Base Stability −5.00%; Communism Support +5.00% |

### Compromise with the NKP Sub-branch

Stalinist path: befriends Soviet Union and joins their war with Finland.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Compromise with the NKP** | A Resurgent Labor Movement; not Prosecute the NKP; Lev Trotskij not active | Communism Support +15.00%; Political Power +65; Sets NOR_going_stalinist flag; If SU communist faction leader: Opinion +35 (or −40 if went Left Opposition); Lev Trotskij unavailable; Kirsten Hansteen advisor available (Recruitable Population +2.00%, Research Speed +3.00%) |
| **Communist Education Centers** | Compromise with the NKP; ruling party communist | Political Power +50; Spirit: Communist Education Centers (Political Power Gain +0.15/day, Recruitable Population +25%, Communism Support +0.01/day) |
| **Co-opt the Secret Army** | Communist Education Centers | Creates 5 Norwegian Hemmelige Hæren units; Fascism Support −12.00% |
| **Field Hospitals** | Co-opt the Secret Army | Army Experience +50; Manpower +1000; 2× 100% Research bonus for Field Hospitals |
| **Expanded Conscription Drive** | Field Hospitals | Spirit Expanded Conscription (730 days): Manpower +300/week, Training Time −20.00% |
| **Revive Pomor Trade** | Communist Education Centers; Troms (924) and Finnmark (925) fully controlled; SU at peace and doesn't have Arkhangelsk | Soviet event; if accept: Finnmark +2 building slots +2 civilian factories; Troms +1 building slot +1 civilian factory; Arkhangelsk +1 building slot +1 civilian factory |
| **Join the Comintern** | Co-opt the Secret Army; Revive Pomor Trade; fully independent; Soviet communist faction leader | Soviet event (if accept: Norway joins Comintern); Sets NOR_included_in_generic_political flag |
| **Soviet Industrial Cooperation** | Revive Pomor Trade; communist faction leader exists | Event to communist faction leader; if accept: 3 random states each get +3 building slots +3 military factories; Industrial Collaboration (Opinion +30 both ways) |
| **Invite Soviet Designers** | Join the Comintern; Soviet Industrial Cooperation; communist faction leader exists | Unlocks MIOs: Morozov Design Bureau Nord, Rubin Design Bureau Nord, GAZ Nord (each +3 sizes) |
| **War in Finland** | Compromise with the NKP; Workers and Farmers Rise; SU exists/at war with Finland; Historical Focus on | Spirit Liberate Finland (730 days): Manpower +200/week, Stability +5.00%, War Support +5.00%, Communism Support +0.01/day; Attack vs Finland +15.0%; Breakthrough vs Finland +20.0%; Army/Navy/Air Experience +25 each; Political Power +60; War goal: Topple Government (Finland) |

### The Seeds of Revolution Sub-branch

Shared communist civil war path (both Stalinist and Trotskyist).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **The Seeds of the Revolution** | Compromise with the NKP OR Prosecute the NKP; over 10% NKP support | Political Power +50; Communism Support +8.00%; Unlocks Rouse Proletariat decisions |
| **The Voice of the People** | The Seeds of the Revolution; over 20% NKP support | Communism Support +10.00%; Stability +5.00%; Political Power +50; Unlocks Communist Propaganda Campaign decision |
| **Organize Partisan Militias** | The Seeds of the Revolution; over 20% NKP support | Manpower +5000; Allows training Communist Militias via decisions |
| **Demand Nationalizations** | The Seeds of the Revolution; over 20% NKP support | If 3+ states <1 civilian factory: 3 random states each +1 building slot +1 civilian factory |
| **Workers and Farmers Rise** | Voice of the People; Organize Partisan Militias; Demand Nationalizations; total support >8%; not communist; over 35% NKP support (or bypasses if communist) | Removes Hard Thirties spirits; removes Birger Ljungberg advisor (−10% Land Doctrine Cost); retires Kristian Laake; Launches Communist Civil War; Scripted NOR_start_communist_civil_war |
| **Send the King Back to Denmark** | Workers and Farmers Rise; not in civil war; ruling party communist | Denmark/UK/Sweden event: King Haakon VII and Prince Olav join that country; or if none accept: retires both; removes Hard Thirties; Stability +20.00%; Communism Support +20.00%; Political Power +100; Sets NOR_included_in_generic_political flag |
| **Nationalize the Hydro Plants** | Send the King Back to Denmark | Political Power +75; Replaces Norsk Hydro with Folks Hydro (Aluminum +10); Infrastructure Construction +10.00%; Civilian Factory Construction +5.00%; Industrial Research +1% |
| **Worker Armies** | Send the King Back to Denmark | 2 states with <4 infrastructure: +2 infrastructure each; 3 random states: +2 building slots +2 civilian factories each |
| **Expand Military Industry** | Send the King Back to Denmark | 3 random states: +2 building slots +2 military factories each |
| **A New Norway** | Nationalize the Hydro Plants; Worker Armies; Expand Military Industry; over 75% NKP support; Has An Independent Norway modifier (requires Stalinist flag or Trotskyist embrace) | If Stalinist: renamed Den Norske Sovjetrepublikken; modifies An Independent Norway: Division Organization +15.0%, Navy Organization +10.0%, Stability +20.0%, War Support +15.0% |

### Prosecute the NKP Sub-branch

Anti-Stalinist communist path: opposes Soviet Union, defends Finland in Winter War.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Prosecute the NKP** | A Resurgent Labor Movement; not Compromise with the NKP | Communist party renamed to Arbeiderklassens Samlingsparti; Communism Support +7.50%; Political Power +50; Jeanette Olsen advisor available (Construction Speed +12.00%, Communism Support +0.05/day); Sets NOR_going_against_stalin flag; SU opinion −40 (unless SU hasn't done Left Opposition) |
| **Squash Dissent** | Consolidate Power; Prosecute the NKP; over 50% NKP support; fully independent | Branch requirement for Reawaken Permanent Revolution |
| **Reawaken the Permanent Revolution** | Squash Dissent; Prosecute the NKP; over 50% NKP support; fully independent | If Nordic communists exist and independent: creates Northern People's Union faction; otherwise if SU Trotskyist: joins Comintern; else creates Norintern faction; Spirit The Permanent Revolution (1095 days): Political Power +0.50/day, Division Recovery Rate +20.0%, War Support +10.00%, Justify War Goal Time −40.0%, Offensive War Stability +30.00%; War goals: Annex vs Sweden/Finland/Denmark/Iceland if not communist/not in faction |
| **Defend Finland** | Workers and Farmers Rise; Prosecute the NKP; over 60% War Support; fully independent; not civil war; Finland exists/at peace/hasn't capitulated; Finland owns Karjala/Salla/Petsamo | If Finland at peace: Guarantee Finland; otherwise: Joins Finland vs SU; War Support +20%; Political Power +100; Manpower +15000; SU Opinion −50 (wants to defend Finland against us); Finland Opinion +40 |
| **Norwegian Engineering** | Reawaken the Permanent Revolution | Unlocks MIO Policy: Permanent Industrial Revolution (MIO Production Resource −10.00%, MIO Research Bonus +10%); Thunes Mekaniske Verksted +1000 funds; Akers Mekaniske Verksted +1000 funds; Norsk Sprængstofindustri +1000 funds |
| **Crush Stalin** | Defend Finland; Reawaken the Permanent Revolution; over 75% War Support; fully independent; not civil war | Spirit Crush Stalin (730 days): Manpower +500/week, Stability +10.00%, War Support +20%, Communism Support +0.07/day (vs SU); Attack vs SU +30.0%; Breakthrough vs SU +30.0%; Army/Navy/Air Experience +25 each; Political Power +75; War goal: Topple Government (SU) if at peace |

### Consolidate Power Sub-branch

Shared communist/democratic path after political divergence.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Consolidate Power** | Prosecute the NKP OR Vote of No Confidence; has Anti-Communist Sentiment OR (doesn't have it AND communist) | If communist: Communism Support −10.00%; if democratic: Democracy Support −10.00%; Political Power +100 |
| **Squash Dissent** | Consolidate Power | Stability +10.00%; if communist: Communism Support −5.00%; if democratic: Democracy Support −5.00%; Jonas Lie advisor available (Army Experience +0.30/day, Training Time −10.0%) |
| **Denounce the German Reich** | Consolidate Power; fully independent; not civil war | If communist: Communism Support +15.00%; if democratic: Democracy Support +15.00%; Political Power +100; War Support +15.00%; if Germany fascist major: Opinion −30 (they denounced us); all democratic countries: Opinion +15 (they denounced tyranny) |
| **Prepare for War** | Squash Dissent; Denounce the German Reich | 3 random states: +1 building slot +1 military factory; 3 random states: +1 building slot +1 naval dockyard; 4 random states: +3 air bases; if NOR_going_dem_allied flag: unlocks Expand Military Industry decision; Manpower +10000 |
| **Proactive Defense** | Reawaken the Permanent Revolution OR Prepare for War OR Join the Allies; over 75% War Support | War Support +15.00%; Command Power +50.0; Army/Navy/Air Experience +30 each; every MIO: +800 funds; if democratic not in faction and Nordic alliance not created: if No Compromise DLC: creates Nordic Council faction; otherwise creates Nordic Council; completes Form the Nordic Council |
| **Secure the Swedish Iron Ore** | Proactive Defense; fully independent; Sweden exists; not subject/not in faction (bypasses if subject) | War goal: Annex (Sweden); Spirit Attack Sweden (730 days): Attack vs Sweden +25.0%, Breakthrough vs Sweden +20.0% |
| **Secure Denmark** | Proactive Defense; fully independent; Denmark exists; not subject/not in faction (bypasses if subject) | War goal: Annex (Denmark); Spirit Attack Sweden (730 days): Attack vs Denmark +25.0%, Breakthrough vs Denmark +20.0% |
| **Crush Hitler** | Secure Swedish Iron Ore OR Secure Denmark; fully independent; Germany/major fascist exists | Spirit Crush Hitler (730 days): Manpower +550/week, Stability +20.00%, War Support +25.00%, Communism Support +0.08/day (vs Germany); Attack vs Germany +40.0%; Breakthrough vs Germany +40.0%; Army/Navy/Air Experience +25 each; Political Power +75; War goal: Topple Government (Germany/fascist major) if at peace |

## Vote of No Confidence Branch

Alternative democratic path: aggressive military preparation, opposes Nygaardsvold government.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Vote of No Confidence** | Mutually exclusive with Continue Nygaardsvold's Government, The Stumbling Storting, A Resurgent Labor Movement | Sets NOR_going_dem_allied flag; Unlocks Prepare State For War (uses convoys/Political Power for National Preparedness); removes Complacent Cabinet spirit; gets event No Confidence Vote; Base Stability −25.00%, War Support +5.00%, Democracy Support −10.00%; Johan H. Andresen becomes democratic leader |
| **Liberal Conservative Alliance** | Vote of No Confidence | Stability +15.00%; Democracy Support +10.00%; Political Power +50 |
| **Join the Allies** | Denounce the German Reich; Liberal Conservative Alliance; fully independent; UK exists/not capitulated/democratic faction leader/at peace | UK event (if accept: Norway joins Allies); if UK faction leader at peace: event to UK; otherwise: event to best democratic ally; Political Power +75; Democracy Support +15.00%; Sets NOR_included_in_generic_political flag |
| **Invite Foreign investment** | Liberal Conservative Alliance | Event to every major democratic country at peace; if accept: +2 offmap civilian factories; gains Investing in Us (Opinion +30) |
| **Sabotage Unions** | Liberal Conservative Alliance | Spirit Reduced Worker Rights (548 days): Consumer Goods Factories −30.0% |
| **Invite Transnational Manufacturers** | Invite Foreign investment | Unlocks Military Industrial Organizations: Chrysler De Havilland (funds +1000), Chrysler (funds +1000) |
| **Contain the Labor Movement** | Sabotage Unions; Weathering the Storm to Come | Communism Support −10.00%; Democracy Support +10.00%; Fascism Support +8.00%; Political Power +50; War Support +15.00% |
| **Uproot Secret Army** | Contain the Labor Movement | Command Power +30; Fascism Support −10.00%; adds 2.00K Norwegian Infantry Equipment to stockpile |
| **Support Finland in Winter War** | Contain the Labor Movement; Rearm for Defense; SU at war with Finland; Finland at peace/not capitulated (bypasses if Finland doesn't exist/communist/in SU faction) | Army Experience +15; War Support +5.00%; Finland: Command Power +20; adds 2.00K Krag–Jørgensen M1918 carbine + 200 Support Equipment + 25 Convoy to stockpile |
| **Protect Finnmark From the Bolsheviks** | Uproot Secret Army; Support Finland in Winter War; owns Finnmark (925) | Manpower +3000; Finnmark: +3 land forts |

### Weathering the Storm to Come Sub-branch

Democratic military preparation (shared with alternative democratic/fascist defense branches).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Weathering the Storm to Come** | Continue Nygaardsvold's Government OR Vote of No Confidence; ruling party democratic; not Complacent Cabinet | 2 random states: +1 building slot +1 military factory; War Support +10.00%; if NOR_going_dem_allied: unlocks decisions (Expedite Training, Prioritize Production, Offensive Push, Focus On Defense); else unlocks state development decisions (Defend State, Emergency Production, Deploy Militias) |
| **The Neutrality Guard** | Weathering the Storm to Come; ruling party democratic | Creates Nøytralitetsvakt division template; Army Experience +20; 1× 50% Research bonus for Military Police I; Oslofjord (110): +4 Nøytralitetsvakt units |
| **Restore the Public Trust in the Storting** | Weathering the Storm to Come OR Broken Gun Policies; ruling party democratic | Stability +5.00%; War Support +10.00%; Political Power +65; Command Power +25.0; Democracy Support +10.00%; if NOR_going_dem_allied: unlocks Economic Relief Measures decision |
| **Rearm for Defense** | The Neutrality Guard; Restore the Public Trust in the Storting; ruling party democratic | 1× 100% Research bonus for Infantry Weapons; Spirit Defensive Rearmament: Equipment Conversion Speed +15%, Land Fort Construction +20.00%, Coastal Fort Construction +25.00%; unlocks Focus On Training decision; Consumer Goods Factories −5.0%, Production Efficiency Cap −10.00%, Training Time −15.00%; if not completed Vote of No Confidence: removes The Broken Gun spirit; when war breaks out: unlocks Integrate Militias decision |
| **Patrol Our Coast** | Rearm for Defense; ruling party democratic | Random state: +2 building slots +2 naval dockyards; 2× 75% Research bonus for Destroyer models; 2× 75% Research bonus for Naval Minelaying Technology; if NOR_going_dem_allied: unlocks Naval Expansion decision (Navy Experience +0.15/day, Factory Output −20.00%, Dockyard Output +25.00%, Military Factory Construction −15.00%, Civilian Factory Construction −15.00%, Naval Dockyard Construction +25.00%); else: unlocks Naval Expansion decision (Naval Base Construction +20.00%, Naval Dockyard Construction +15.00%) |
| **Coastal Defense** | Patrol Our Coast OR Restart Public investment; ruling party democratic | Every coastal state except Oslofjord/Nordland: +1 coastal fort; Oslofjord: +2 coastal forts; Nordland: +2 coastal forts; unlocks Public Investment Drive decision (Construction Speed +20.00%, Production Efficiency Cap −10.00%, Factory Output −15.00%, Training Time +10.00%) |
| **Fortify Norway** | Patrol Our Coast OR Restart Public investment; ruling party democratic | Every state except Oslofjord/Nordland: +1 land fort; Oslofjord: +2 land forts; Nordland: +2 coastal forts |

### Replace Laake Sub-branch

Democratic military reform (removes liberal pacifist advisor, improves army).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Replace Laake** | The King's No OR Uproot Secret Army | Retires Kristian Laake; gets event Laake's Replacement |
| **Reform the Army** | Replace Laake | Removes Birger Ljungberg advisor (−10% Land Doctrine Cost, +75% Conscription Laws Cost); Army Experience +50; Command Power +60.0; Political Power +75; War Support +20.00%; unlocks Modernize Armed Forces decision (Command Power −25.0, removes 100 convoy after 45 days; when removed: modifies Obsolete Armed Forces spirit: Division Speed +10.00%, Division Organization +10.0%, Division Attack +10.0%) |
| **Improved Training** | Reform the Army | Spirit Improved Training (730 days): Army Experience Gain +25.0%, Training Time −30.00%, Minimum Training Level +15% |
| **Officers Academy** | Reform the Army | Army Experience +75; Command Power +50.0; unlocks Spirit of the Academy (Flexible Officers: leader starting level +2, skill bonuses +10.0%, promotion cost −30.0%, army reassignment duration −30.0%) |
| **Offensive Doctrines** | Improved Training; Officers Academy | 2× 50% Cost reduction for Land Doctrine; 2× 60% Cost reduction for Special Forces Doctrine; Army/Navy/Air Experience +50 each; Command Power +50.0 |

### Forsvarets Intelligence Service / The King's No Sub-branches

Government-in-exile focuses (requires La Résistance DLC for intelligence agency; accessed when capitulated).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Forsvarets Intelligence Service** | Requires La Résistance DLC; Support Finland in Winter War OR Rearm for Defense; ruling party democratic | +2 offmap civilian factories; Creates Intelligence Agency |
| **The King's No** | King's No allow trigger (see below); Coastal Defense OR Fortify Norway; at war; ruling party democratic | Sets NOR_mobile_gov_days_remove = 7; Oslofjord (110): set as government HQ; removes Anti-Communist Sentiment spirit; unlocks decisions (Move Capital to State, Prepare Exile); Sets NOR_included_in_generic_political flag |
| **Prince Olav's Inspiration** | The King's No; has capitulated; ruling party democratic | Legitimacy +20; Political Power +50; adds 25 convoy to stockpile; Stability +10.00% then +25.00%; Prince Olav becomes naval commander |
| **Establish Milorg** | The King's No; has capitulated; ruling party democratic | Unlocks decisions (Procure and Distribute Weapons, Training Exercises with Norway) |
| **Use XU** | Establish Milorg; has capitulated; ruling party democratic | If La Résistance: Kasper Skjeggenes and Astrid Løken become operatives; unlocks Foment Resistance in Norway decision; else: Spirit XU (Civilian Intelligence +30%, Army Intelligence +15%) |
| **Recruit Norwegian Refugees** | Establish Milorg; has capitulated; ruling party democratic | Command Power +50.0; Political Power +100; Manpower +10000 |
| **Preparing the Return to Norway** | Use XU; Recruit Norwegian Refugees; has capitulated; ruling party democratic | Unlocks Support Rebellion in Norway decision; King Haakon VII becomes naval commander; (if Bamse flag: flavor text) |
| **Approach the Coordinating Committee** | The King's No; has capitulated; ruling party democratic | Spirit Coordinating Committee: Resistance Target in our occupied states +20%, Resistance Growth Speed +10% |
| **Approach Kretsen** | The King's No; has capitulated; ruling party democratic | Spirit Kretsen: Compliance Growth Speed in our occupied states −15% |
| **Empower Sivorg** | Approach the Coordinating Committee; Approach Kretsen; has capitulated; ruling party democratic | Legitimacy +10; Political Power +25; replaces Kretsen and Coordinating Committee spirits with Sivorg: Resistance Target +30%, Resistance Growth Speed +20%, Compliance Growth Speed −25%; adds 50 convoy to stockpile |

## Continue Nygaardsvold's Government Branch

Historical democratic path: pacifist focus, demilitarization, social reform (mutually exclusive with Vote of No Confidence, A Resurgent Labor Movement, The Stumbling Storting).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Continue Nygaardsvold's Government** | None | Political Power +100; sets NOR_going_dem_historical flag; gets event Nygaardsvold's Cabinet; Stability +5.00%, War Support −5.00% |
| **Broken Gun Policies** | Continue Nygaardsvold's Government; ruling party democratic | Spirit The Broken Gun: Production Efficiency Cap −15.00%, Civilian Factory Construction +25.00%; Democracy Support +2.50%; unlocks Develop State decisions (civilian construction speed, military construction penalties) |
| **Leaving the Hard Thirties Behind** | Continue Nygaardsvold's Government; ruling party democratic | Modifies The Hard Thirties spirit to either (Consumer Goods −35.0%, Construction −15.00%) or (Consumer Goods −15.0%, Construction −7.00%) or removes it; then Stability +5.00%, War Support +5.00%, Communism Support +5.00%, Democracy Support +3.00% |
| **Cut Military Budget** | Broken Gun Policies; Leaving the Hard Thirties Behind; ruling party democratic | Modifies The Broken Gun spirit: Consumer Goods −15.0%, Production Efficiency Cap −20.00%, Civilian Factory Construction +25.00% |
| **Social Incrementalism** | Cut Military Budget; ruling party democratic | Stability +10.00%; Democracy Support +5.00%; modifies The Broken Gun: Consumer Goods −20.0%, Production Efficiency Cap −25.00%, Civilian Factory Construction +30.00%; removes Complacent Cabinet; Kirsten Hansteen advisor available (Recruitable Population +2.00%, Research Speed +3.00%, Communism Support +0.06/day) |
| **Print More Money** | Leaving the Hard Thirties Behind; ruling party democratic | Modifies The Hard Thirties (as above) or removes it; then gets spirit Printing Money: Consumer Goods −20.0%, Civilian Factory Construction +20.00% |
| **Restart Public investment** | Social Incrementalism; Print More Money; ruling party democratic | Modifies The Hard Thirties (as above) or removes it; then Democracy Support +10.00% |
| **Bail Out Towns** | Leaving the Hard Thirties Behind; ruling party democratic | 3 random states: +1 building slot +1 civilian factory each |

## The Stumbling Storting Branch

Fascist/Monarchist start (mutually exclusive with Continue Nygaardsvold's Government, Vote of No Confidence, A Resurgent Labor Movement).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **The Stumbling Storting** | None | Gets event The Storting Stumbles; Stability −20.00%, Democracy Support −5.00% |

### Lurk in the Shadows Sub-branch

Fascist path: covert support building, recruitment from political chaos (mutually exclusive with The Royal Chamberlain's Overture).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Lurk in the Shadows** | The Stumbling Storting; not The Royal Chamberlain's Overture | Sets NOR_going_fascist flag; finds biggest/local fascist; Political Power +50; Fascism Support +5.00%; unlocks Build support in Norway decision |
| **Ask for Support** | Lurk in the Shadows; not Quisling's Coup | Major fascist country at peace exists; event to fascist country: if accept: Fascism Support +0.10/day; Military Access; otherwise: nothing |
| **The Quisling Path** | Lurk in the Shadows; not The Royal Chamberlain's Overture | Recruits Norwegian fascists; Fascism Support +10.00%; if Vidkun Quisling alive: becomes available as Political Advisor |
| **Civil War (Fascist)** | The Quisling Path; Fascism Support >30%; not communist; not royal alignment | Launches fascist civil war; If on historical: triggers based on game state; otherwise: standard civil war against democratic |

> ⚠️ broken wiki template reconstructed: `[{{{1}}}]` markers in source wiki (appearing before ideology names like "Communist", "Democratic", "Fascist", "Monarchist") indicate ideology/government form labels interpreted from context.

### Quisling's Coup Sub-branch

Fascist civil war and options post-victory: conquer Nordic territories or puppet to Germany.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Quisling's Coup** | Historical democratic or fascist path; launches civil war; puts Vidkun Quisling in power | Completes Quisling civil war; Vidkun Quisling appointed to leadership; allows choice of Nordic claims or German puppet |
| **Claim the Norwegian Throne** | Quisling's Coup; fascist path post-victory | War goals vs Sweden/Denmark; territorial claims on Nordic regions |
| **Become a German Puppet** | Quisling's Coup; fascist path post-victory | Option to become puppet of Germany; trade sovereignty for German support |

### Claims on Denmark / Claims on Sweden Sub-branch

Expansion focuses (shared fascist/monarchist): demands territory from Nordic neighbors and parts of Soviet Union.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Claims on Denmark** | Shared fascist/monarchist expansion; fully independent | War goal: Annex (Denmark); Fascism Support +5.00% |
| **Claims on Sweden** | Shared fascist/monarchist expansion; fully independent | War goal: Annex (Sweden); Fascism Support +5.00% |
| **Claims on Soviet Union** | Shared fascist/monarchist expansion (rarely taken monarchist path); fully independent | War goal: Annex (SU northern states); allows Nordic territorial claims in Soviet lands |

### The Royal Chamberlain's Overture Sub-branch

Monarchist path: restores King Haakon VII with regent Peder Anker Wedel-Jarlsberg, Nordic expansion, cores on Atlantic Islands and Soviet states (mutually exclusive with Lurk in the Shadows).

| Focus | Prerequisites | Effects |
|-------|---|---|
| **The Royal Chamberlain's Overture** | The Stumbling Storting; not Lurk in the Shadows | Legitimizes monarchy; Haakon VII ruled with regent Wedel-Jarlsberg; Democratic Support +10.00%; unlocks monarchist expansion focuses |
| **Restore Royal Authority** | The Royal Chamberlain's Overture | Monarchy Support +10.00%; removes Stumbling Storting penalties; allows claim focuses |
| **Claim Atlantic Islands** | Restore Royal Authority | War goals: Annex (Greenland, Faroe Islands, Iceland); cores several northern Atlantic territories |
| **Claim Soviet Territories** | Restore Royal Authority; fully independent | War goals: Annex (parts of SU: Karelia, northern Soviet regions); claims on Soviet northern frontier |

## Start Rearmament Branch

Army focus branch: bonuses to army technology, modifies The New Hæren national spirit.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Start Rearmament** | None (army branch start) | Army Technology Research Speed +10.00%; modifies The New Hæren spirit (army doctrine/experience bonuses) |
| **Expand the Army** | Start Rearmament | Manpower +5.00 daily; Recruitable Population +2.00%; army construction speed +10.00% |
| **Modernize Equipment** | Start Rearmament | Infantry Weapons Research Speed +15.00%; Support Equipment Research Speed +15.00%; Army Experience +50 |
| **Doctrine Development** | Modernize Equipment | Land Doctrine Research Speed +10.00%; Cost reduction for doctrines; Army Experience +75 |

## Building an Independent Norway Branch

Industrial branch: industrial bonuses, modifies An Independent Norway national spirit.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Building an Independent Norway** | None (industrial branch start) | Civilian Factory Construction +10.00%; Infrastructure Construction +10.00%; modifies An Independent Norway spirit |
| **Expand Civilian Industry** | Building an Independent Norway | Random states: +2 building slots +2 civilian factories; Civilian Factory Output +5.00% |
| **Focus on Quality** | Building an Independent Norway | Improve factory efficiency; Production Efficiency Cap +5.00%; research speed +3.00% |
| **Resource Development** | Expand Civilian Industry | Unlocks mining/resource extraction decisions; ore/lumber production +15.00% |
| **Industrial Research Initiatives** | Focus on Quality | Industrial Research Speed +10.00%; unlocks special production decisions |

## Hærens Flyvevaaben Branch

Air force branch: air bases, air force technology bonuses, modifies Hærens Flyvevaaben or Luftforsvaret national spirit.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Hærens Flyvevaaben** | None (air branch start) | Air Force Technology Research Speed +10.00%; Air Experience +25; modifies Hærens Flyvevaaben (or Luftforsvaret if already using modern name) spirit |
| **Expand the Air Force** | Hærens Flyvevaaben | Random states: +3 air bases; Fighter Research Speed +10.00%; Air Experience +50 |
| **Develop Air Doctrine** | Hærens Flyvevaaben | Air Doctrine Research Speed +10.00%; Doctrine Cost Reduction; Air Experience +75 |
| **Aircraft Modernization** | Expand the Air Force | Jet Fighter/Tactical Bomber/Naval Bomber Research Speed +15.00%; Air Experience +100 |

## Sjøforsvaret Branch

Naval branch: naval industry bonuses, modifies Sjøforsvaret national spirit.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Sjøforsvaret** | None (naval branch start) | Naval Industry Research Speed +10.00%; Navy Experience +25; modifies Sjøforsvaret spirit |
| **Expand Naval Industry** | Sjøforsvaret | Random states: +2 building slots +2 naval dockyards; Dockyard Output +5.00%; Navy Experience +50 |
| **Naval Doctrine Development** | Sjøforsvaret | Naval Doctrine Research Speed +10.00%; Doctrine Cost Reduction; Navy Experience +75 |
| **Submarine Modernization** | Expand Naval Industry | Submarine Research Speed +20.00%; Cruiser Research Speed +10.00%; Navy Experience +100 |

## Form the Nordic Council Branch

Joint focus available to Nordic faction members (Denmark, Finland, Iceland, Norway, Sweden). Allows Nordic coordination on shared goals.

| Focus | Prerequisites | Effects |
|-------|---|---|
| **Form the Nordic Council** | A Nordic country creates a faction with another Nordic country; any Nordic faction member can complete this | Unlocks Nordic faction benefits; shared research modifiers +5.00%; faction cohesion bonuses; allows Nordic members to assist each other's wars via faction mechanics |
| **Nordic Unity** | Form the Nordic Council | Faction cohesion +10.00%; all faction members: War Support +5.00%; Opinion bonuses within faction +25 |
| **Coordinated Defense** | Nordic Unity | All Nordic faction members gain defensive bonuses vs external threats; Army/Navy/Air defense coordination; shared intelligence agencies |
| **Nordic Economic Integration** | Form the Nordic Council | Unlocks joint trade agreements; civilian factory outputs +3.00% per faction member; research speed +2.00% per faction member |

---

**Note:** This tree requires the Arms Against Tyranny DLC for the unique focuses. Without it, Norway uses the generic national focus tree. The communist, democratic, and fascist paths are mutually exclusive at the start via three root focuses: *A Resurgent Labor Movement*, *Vote of No Confidence/Continue Nygaardsvold's Government*, and *The Stumbling Storting*. The government-in-exile focuses (The King's No and related) unlock only when capitulated as democratic. See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses (all countries).
