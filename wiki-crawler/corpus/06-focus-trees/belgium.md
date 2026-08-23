---
title: Belgium national focus tree
category: focus-trees
tags: [Belgium, national focus, Götterdämmerung, fascism, democracy, communism, neutrality, European Union]
game_version: "1.19"
dlc: [Götterdämmerung]
sources:
  - https://hoi4.paradoxwikis.com/Belgian_national_focus_tree
---

## Summary

Belgium's unique national focus tree (requires Götterdämmerung) comprises six major branches structured around its core decision tree: neutrality, government crisis, and two power-blocs (fascist Rexist/VNV, democratic/socialist, and communist paths). The tree opens with three simultaneous tracks — defensive military preparedness, government resigns (triggering a snap election), and industrial/colonial developments — that branch into incompatible paths after a royal appointment. Success paths lead either to fortress Belgium (defensive neutrality and economic recovery) or outward expansion (Axis/Burgundy, European Federation, or Soviet alignment), each with unique industrial, military, and territorial bonuses. Without Götterdämmerung, Belgium uses the generic tree.

See [Belgium](../05-countries/belgium.md) for the country's 1936 starting profile.

For generic/continuous focuses available to all countries, see [National Focus and Continuous Focus](../01-mechanics/national-focus.md).

## Perpetual Neutrality/Government Resigns Branch

The opening branch declaring Belgium's neutral stance and triggering the governmental crisis. Both **Perpetual Neutrality** and **Government Resigns** can progress simultaneously before diverging.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Perpetual Neutrality** | None | Bypasses if: at war or completed *Growing Threat of Fascism* | Dynamic modifier: join faction tension +100.0%, justify war goal time +100.0%, guarantee tension +100.0%, construction speed +10.0% |
| **Independent, Neutral and Loyal** | Perpetual Neutrality | Bypasses if: at war or completed *Growing Threat of Fascism*; requires modifier not active | Builds on neutrality: infrastructure/military/civilian factory construction +10.0%, justify war goal time +50.0%, send volunteers tension +100.0%, lend-lease tension +100.0%. By Blood Alone adds: embargo tension +100.0% |
| **Repudiate Treaty With France** | Independent, Neutral and Loyal | If completed *Defense Bill*: remove Scars of the Great War; else reduce it by: war support +15.0%, recruitable population +5.0%, division organization +5.0%. Cancels guarantees with France/UK if they had them |
| **Dyle Plan** | Repudiate Treaty With France; at peace with France and UK (bypasses if at war with either) | France and UK gain +15 opinion toward Belgium; more likely to aid if war breaks out |
| **Government Resigns** | None | Gets event *The Government Resigns and Snap Election*; corruption modifier: daily political power +0.10, construction speed +5.0%, daily fascism support −0.04 |
| **Investigate Bribery Charges** | Government Resigns | Further corruption reduction: daily political power +0.05, stability +5.0%, construction speed +10.0%, daily fascism support −0.04 |

### Defensive Neutrality Sub-branch

Defensive military buildup focused on land fortifications and entrenchment.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Defensive Neutrality** | Independent, Neutral and Loyal | Land fort construction speed +5.0%, max entrenchment +1.0 (or upgrades if already active) |
| **Belgian Gates** | Defensive Neutrality | Adds to dynamic modifier: max entrenchment +1.0, land fort construction speed +5.0% | Tank obstacles; iron constructions to deny passage |
| **Iron Wall** | Belgian Gates | Land fort construction speed +5.0%, land fort effectiveness +5.0%, max entrenchment +1.0 |
| **Our Southern Neighbour** | Iron Wall (bypasses if at war with France) | Event: *France: Friend or Foe?* |
| **Protect Against France** | Our Southern Neighbour | Adds 1 land fort each to Charleroi/Kortrijik/NW Kortrijik; Wallonie (34) and Vlaanderen (6) each gain 1 land fort if slots available |
| **National Redoubt at Antwerp** | Defensive Neutrality; controls Antwerpen (6598) or Brussels (516); can build 1 fort in Brussels or 2 in Antwerpen (bypasses if cannot) | Vlaanderen (6): +1 land fort; Antwerpen (977): +2 land forts if 2 slots available |
| **Fortify Liege** | National Redoubt at Antwerp; controls Wallonie (34) and can build 1 land fort there (bypasses if cannot) | Builds level 1 land fort in Wallonie along Meuse; adds 3 forts to three provinces in the state |
| **Eben Emael Fortress** | Fortify Liege; controls Liège (11519) and can build 2 land forts there (bypasses if cannot) | Wallonie (34): +2 land forts if 2 slots available | Named after historical fortress overlooking Albert Canal |
| **Koningshooikt-Wavre Line** | Iron Wall AND Eben Emael Fortress | Modifies dynamic modifier: max land fort level +1, max coastal fort level +1 | KW Line provides second defensive line of trenches, pillboxes, Belgian gates |
| **Mobilize the Nation** | *Our Southern Neighbour* OR *Koningshooikt-Wavre Line*; no *Lack of Junior Officers* modifier | Recruitable population +1.50%; gets temporary modifier *Lack of Junior Officers* for 180 days: army experience −5.0%, division organization −5.0%, daily command power −5% |
| **Defensive Reorganization** | Mobilize the Nation AND Koningshooikt-Wavre Line | Replaces *Defensive Neutrality* with *Defensive Reorganization*: max entrenchment +2.0, land fort construction speed +5.0%, land fort effectiveness +5.0% |
| **Flooded Tank Barriers** | Koningshooikt-Wavre Line | All owned states in Vlaanderen/Antwerpen/Wallonie/Ardennes gain: division defense on core territory +10.0%, attacking divisions speed −25.00% |
| **Dam the Consequences** | Flooded Tank Barriers; controls Eupen-Malmedy (3488) | Ardennes (980) dams receive 1.00 level damage at −80% repair speed. Adds *Dam Blown (Belgium)* (360 days): local manpower −50%, divisions speed −25.00%, strategic redeployment disabled, available resources −25%, supply impact +50% |

### Defense Bill Sub-branch

Military development through officer academies, doctrine, and arms manufacturing.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Defense Bill** | Independent, Neutral and Loyal | Command power +50, army experience +25. If completed *Repudiate Treaty With France*: remove *Scars of the Great War*; else reduce it by: military factory construction +20.0%, recruitable population +10.0%, war support +15.0%, division organization +10.0% |
| **Royal Military Academy** | Defense Bill | +1 research slot; dynamic modifier: max planning factor +10.0% |
| **Multi-Language Courses** | Royal Military Academy | Modifies *Royal Military Academy*: division organization +10.0% | Leverages bilingual officer corps (French/Dutch speakers) |
| **Resist and Bite** | Multi-Language Courses | 2× 25% doctrine cost reduction for Special Forces. By Blood Alone: +10.00% mastery for 240 days to Jaeger Traditions and Rangers Jungle Training; +100% research bonus for Rangers. Arms Against Tyranny: +10.00% mastery to Cold Weather Specialists and Elevate the Mountaineers; +100% research for Mountaineers. Otherwise: +100% research for Mountaineers | Chasseurs Ardennais elite unit |
| **Belgian Special Forces** | Resist and Bite | Arms Against Tyranny: +1 free special forces branch specialism, +25% cost reduction for Special Forces Doctrine; Eddy Blondeel becomes general |
| **Interpreters** | Belgian Special Forces | National spirit *Belgian Interpreters*: paratrooper/marine/mountaineer special forces cap contribution −15% each, special forces cap +5. Shared with faction members |
| **Department of Telecommunications** | Royal Military Academy | Modifies *Royal Military Academy*: initiative +15.0% | Radio and carrier pigeons |
| **Center For Advanced Military Studies** | Multi-Language Courses AND Department of Telecommunications | Modifies *Royal Military Academy*: division attack +5.0% |
| **Senior Officer Training** | Center For Advanced Military Studies | Every employed army leader: +1 planning skill, +1 logistics skill. Modifies *Royal Military Academy*: starting logistics/planning skill +1 for new leaders | Identifies lazy-clever as best officers |
| **Center of Nuclear Chemistry** | Center For Advanced Military Studies | Dynamic modifier *Academies of Belgium*: nuclear research special projects speed +5.0%; breakthrough progress +25.00% | Access to Congolese uranium |
| **Department of Ballistic Metrology** | Royal Military Academy | Modifies *Royal Military Academy*: artillery attack +10.0% |
| **Excellent Anti-Tank Guns** | Department of Ballistic Metrology | 2× 100% research bonus for Anti-Tank. Enables trait in support and line anti-tank: hard attack +10%, piercing +10%. Tank destroyer and motorized anti-tank: hard attack +10%, piercing +10%. Adds technology: Bofors Anti-Tank gun | Belgian metallurgy excellence |
| **Fonderie Royale de Canons Liege** | Department of Ballistic Metrology | Arms Against Tyranny: FRCA gains +2 sizes, funds +20.00%, military industrial research +5.00%; Vickers-Armstrong Belgium +1 size with Fonderie Royal Canons trait; Renault Belgium +1 size with same trait (piercing +15%, hard attack +10%). Otherwise: FRCA (artillery designer) +15% research; Vickers-Armstrong (tank designer) armor +15%, armor tech reliability +5%, soft attack +5%; Renault (mobile tank) armor +15%, armor tech max speed +5%, reliability +5% | Established 1803 by Napoleon |
| **Junior Officer Training** | Royal Military Academy | Army experience +50; 2× 50% cost reduction for Land Doctrine |
| **Strategic Doctrine Development** | Junior Officer Training | 2× 50% cost reduction for Land Doctrine |
| **Belgian Tank Development** | Fonderie Royale de Canons Liege AND Strategic Doctrine Development | 2× 50% research bonus for Armor technology |
| **Doctrinal Innovations** | Strategic Doctrine Development | 1× 50% cost reduction for Land Doctrine, 1× 50% cost reduction for Special Forces Doctrine |
| **Modernized Army** | Defensive Reorganization AND Senior Officer Training AND Doctrinal Innovations | Dynamic modifier *Academies of Belgium*: special projects speed +10.0%; breakthrough progress Land Warfare +50.00% |
| **Increased Length of Service** | Defense Bill; no *Lack of Junior Officers* modifier | Adds/modifies *Mobilize the Nation*: recruitable population +1.50%; if new, gets 180-day *Lack of Junior Officers*: army experience −5.0%, division organization −5.0%, daily command power −5% |
| **FN Herstal** | Defense Bill | Arms Against Tyranny: FN Herstal +1 size, funds +20.00%, military industrial research +5.00%, outsourced production trait ±5.00%. Otherwise: FN Herstal (infantry equipment designer) weapons +15% research; reduces *Economic Downturn* by: factory output +5.0% |
| **Poudreries Réunies de Belgique** | FN Herstal; Vlaanderen (6) fully controlled (bypasses if not controlled) | Vlaanderen: +2 building slots, +2 military factories; reduces *Economic Downturn* by: factory output +5.0% | Munitions specialist |
| **Minerva-Imperia** | FN Herstal AND Dyle Plan | Arms Against Tyranny AND La Résistance: both MIO operations gain +1 size, +20.00% funds, +5.00% military industrial research (Knight Engines trait: reliability +5%, max speed +10%). Otherwise: Minerva-Imperia Automobiles (motorized equipment designer) +15% research; reduces *Economic Downturn* by: factory output +5.0% |
| **Legacy of the Great War** | Minerva-Imperia; at war | National spirit: army experience +10.0%, division organization +10.0%, recruitable population +10.0%, division attack on core territory +10.0%, division defense on core territory +10.0% | Flanders remembrance |

### Government of National Unity Sub-branch

Political path auto-completed during the *Government Resigns* event sequence.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Government of National Unity** | Government Resigns; mutually exclusive with *Vandervelde Minority* | Auto-completed by event outcome | Paul van Zeeland forms unity coalition |
| **Royal Intervention** | Repudiate Treaty With France AND Investigate Bribery Charges AND Government of National Unity; has modifier *Collapsing Government* | Event: *The Royal Appointment*; King chooses between Paul-Émile Janson (liberal) or Leon Degrelle (fascist) |

### Paul-Émile Janson Sub-branch

Historical democratic path; auto-completed if Janson wins the royal appointment.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Paul-Émile Janson** | Royal Intervention; mutually exclusive with *Degrelle* | Auto-completed by event outcome | Janson becomes democratic leader; removes *Collapsing Government*; stability +5%; royal appointee modifier |
| **Plan de Man** | Paul-Émile Janson | Reduces *Economic Downturn* by: consumer goods factories factor −10.0% | Builds on unemployment reduction (23.5% → 15%) |
| **Economic Recovery** | Dyle Plan AND Plan de Man | Event: *Budgetary Crisis*; national spirit *Economic Recovery*: factory output +10.00%, dockyard output +10.00% |
| **Adriaan Martens Crisis** | Economic Recovery | Event: *Adriaan Martens Crisis*; modifies *Corruption*: daily political power +0.05, stability +5.0%, daily fascism support −0.02 | Fascist collaborator appointed to Royal Academy of Medicine |
| **Benelux Union** | Adriaan Martens Crisis; mutually exclusive with *Tripartite Government*; fully independent; Spaak is leader | If has *Language Barriers*: remove it. As faction leader: rename faction. Else if in faction: leave and create *Benelux Union*. Else: create *Benelux Union*. Invites Netherlands and Luxembourg if democratic/non-aligned |
| **The Council of Europe** | Benelux Union; fully independent | As faction leader: rename to *European Union*. Else if in faction: leave and create *European Union*. Else: create *European Union*. Unlocks decisions for EU expansion/development. Becomes European President. Events: Otto von Habsburg offer, EU formation |
| **Tripartite Government** | Adriaan Martens Crisis; mutually exclusive with *Benelux Union*; Pierlot is leader | Removes *Language Barriers*; stability +10.00%, war support +10.00% | Coalition of democratic parties under Pierlot |
| **Broken Neutrality** | Tripartite Government; has modifier *Perpetual Neutrality* | Event: *The Future of Belgian Neutrality* |

### Degrelle Sub-branch

Fascist path; auto-completed if Degrelle wins the royal appointment. Two further branches: Rexist (Paul-Émile Janson alternative path) and VNV (Vlaamsch Nationaal Verbond; leads to territorial expansion via Burgundy/Dietsland).

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Degrelle** | Royal Intervention; mutually exclusive with *Paul-Émile Janson* | Auto-completed by event outcome | Degrelle becomes fascist leader; war support +5.00%, daily fascism +0.03, rules: can send volunteer forces; removes *Collapsing Government*; fascism +15.00%, modifies *Corruption*: daily political power +0.05, stability +5.0% |
| **Support the Rexists** | Degrelle; mutually exclusive with *Constitutional Crisis* | Lucien Lippert general; fascism +5.00%, stability +5.00% |
| **Support the VNV** | Degrelle; mutually exclusive with *Support the Rexists* and *Constitutional Crisis* | Lucien Lippert general; fascism +5.00%; Belgium renamed *Vlaanderen*; cosmetic tag set to BEL_vnv_dominant |
| **Dissolve Political Parties** | Support the Rexists; >50% Rex support | National spirit (365 days): daily democracy −0.05, communism −0.03, unaligned −0.01 |
| **The Flemish Question** | Support the Rexists; >40% Rex support | Event: *The Flemish Question* (choose linguistic standard) |
| **Christian Corporatism** | The Flemish Question; >50% Rex support | Random fully controlled cored state: +2 building slots, +2 civilian factories; another state: +1 building slot, +1 military factory |
| **Legacy of the Soldier King** | The Flemish Question; >50% Rex support | Dynamic modifier *Rexist Legion*: division attack on core +10.0%, division defense on core +10.0% | King Albert inspiration |
| **The Lost Tribe** | Christian Corporatism AND Legacy of the Soldier King; >60% Rex support | Improves *Rexist Legion*: recruitable population +15.0%, land night attack +5.0%. Luxembourg gets annex war goal; if accepts, annexes and becomes core |
| **Invite German Tank Developers** | The Lost Tribe | Arms Against Tyranny: Daimler-Benz MIO +2 sizes. Otherwise: Daimler Benz tank designer +10% armor research, production cost −5.00%, reliability +5%, truck/mechanized production cost −5.00% |
| **The Walloon Legion** | The Lost Tribe; >80% Rex support | Improves *Rexist Legion*: division organization +5.0%, infantry attack +10.0%, infantry defense −5.0% |
| **The New Ruhr** | The Walloon Legion; >90% Rex support; Ardennes (980) owned/controlled | Random non-Ardennes state: +2 building slots, +2 civilian/+2 military factories. Ardennes: +2 building slots each factory type; state category upgrades (up to megalopolis) with +1/+2 building slots per tier |
| **Join Axis** | *The Lost Tribe* OR *Burgundy Rising*; mutually exclusive with *Strength and Brotherhood*; fully independent, not in faction, no *Perpetual Neutrality*, at peace with Germany, Germany is fascist (bypasses if already in Axis) | Germany gets event *Belgium Requests to join the Axis* |
| **Abandon Neutrality** | *Support the Rexists* OR *Support the VNV*; has *Perpetual Neutrality*; >40% Rex support | Removes *Perpetual Neutrality* |
| **The French Horse And the Red Rider** | *Support the Rexists* OR *Support the VNV*; >40% Rex support | By Blood Alone: embargo France. Else: trade relations −100. Luxembourg gets demand annexation event (accept: annex; refuse: annex war goal). World tension +2.0% |
| **Nationalize the Banks** | *Abandon Neutrality* OR *The French Horse And the Red Rider*; >50% Rex support | Reduces *Economic Downturn* by: consumer goods factories factor −10.0% |
| **Royal Commander In Chief** | *Abandon Neutrality* OR *The French Horse And the Red Rider*; >50% Rex support | King Leopold III becomes field marshal; Lambert Chardome general. Clears country flag; if *BEL_leopold_flag* set, Leopold doesn't buckle to surrender pressure if invaded |
| **International Stipend** | *Abandon Neutrality* OR *The French Horse And the Red Rider*; >50% Rex support | +2 offmap civilian factories |
| **Civil Service Purge** | *Nationalize the Banks* OR *Royal Commander In Chief* OR *International Stipend*; >60% Rex support | Modifies *Corruption*: daily political power +0.05, stability +10.0%, construction speed +5.0%, daily fascism −0.05 |
| **Traditional Family Values** | *Nationalize the Banks* OR *Royal Commander In Chief* OR *International Stipend*; >60% Rex support | National spirit: monthly population +10%; stability +5.00%, political power +100 |
| **The European Crusade** | Civil Service Purge AND Traditional Family Values | If Rexist path: dynamic modifier *The European Crusade*: recruitable population +10.0%, supply consumption −10.0%, production efficiency cap +5.0%. If VNV path: division organization +5.0%, attack vs majors +5.0%, defense vs majors +5.0% |
| **Belgian Renaissance** | The European Crusade | Improves *The European Crusade*: research speed +5.0% |

### VNV Expansion to Burgundy/Dietsland/Belgica

Continuation of the VNV branch leading to territorial expansion into Low Countries and France.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Revitalize Nederlands** | Support the VNV | Replaces *Language Barriers* with *Dutch Language Primacy*: daily political power −0.10, recruitable population +5%, stability −5.00% |
| **Flanders Ascendant** | Revitalize Nederlands; no *Perpetual Neutrality*; bypasses if Luxembourg/Netherlands don't exist | If Luxembourg exists: annex war goal. If Netherlands exists: annex war goal for Luxembourg |
| **Dietsland** | Flanders Ascendant; Netherlands: all core states controlled by Belgium/subject; Luxembourg: all core states controlled by Belgium/subject; Belgium: all core states controlled by Belgium/subject | Belgium renamed *Dietsland*. Gains cores on Dutch states in Europe: Holland (7), Brabant (35), Friesland (36). Hidden: these become cores |
| **Belgian East Indies** | Dietsland; owns at least one of: Sumatra (672), West Java (335), Kalimantan Barat (334), Sulawesi (673), West Nusa Tenggara (667), The Moluccas (668), Dutch New Guinea (669), Aru Islands (738), Suriname (309), Curaçao (695) | All such states: compliance +25.0% |
| **Demand Calais** | Dietsland | Event: *How Should We Get Calais?* (buy, trade Congo, demand, or fight) | Kales (Calais) was part of County of Flanders |
| **Burgundy Rising** | Demand Calais; Nord-Pas-de-Calais (29) fully controlled | Belgium renamed *Burgundy*. National spirit *Burgundian Heritage*: political power +5%, consumer goods factories −5%, recruitable population +5%, construction speed +5.00%. Nord-Pas-de-Calais becomes core |
| **Strength and Brotherhood** | Burgundy Rising; mutually exclusive with *Join Axis*; fully independent, not in faction, no *Perpetual Neutrality* | Sets rule: can create factions. Creates *Pride of the Golden Lion* faction |
| **Demand Further Gallic Concessions** | Burgundy Rising | Gains claims on: Nord-Pas-de-Calais (29), Picardy (785), Champagne (18), Alsace-Lorraine (28), Franche-Comte (17), Bourgogne (27). Takes claimed state war goal against France. Unlocks decisions to gain cores if occupied |
| **Belgica** | Demand Further Gallic Concessions; controls Nord-Pas-de-Calais, Picardy, Champagne, Alsace-Lorraine, Franche-Comte, Bourgogne (all by Belgium or subjects) | Belgium renamed *Belgica*. National spirit *Pax Belgica*: political power +10%, recruitable population +10%, consumer goods factories −5.0%, construction speed +5.00%, resistance target −5%, daily compliance +0.01% | Roman Belgica heritage |

### Constitutional Crisis Sub-branch

Democratic/Socialist path triggered if Pierlot blocks Degrelle's appointment.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Constitutional Crisis** | Degrelle; mutually exclusive with *Support the Rexists* | Politics: regency committee becomes ruling party; public elections held; Pierlot becomes democratic leader; surrender limit +10.00%, war support +10.00%, daily democracy +0.05, democracy +10.00% |
| **Kings Abdication** | Constitutional Crisis | Charles, Count of Flanders gains Royal Regent (daily political power +0.10, stability +10.00%); Leopold removed; daily political power +0.10, stability +5.00% |
| **Snap Election** | Kings Abdication | Event: *The Snap Election* (Pierlot or Spaak as forerunners) |
| **Liberal Victory** | Snap Election | Auto-completed if Pierlot wins | Hubert Pierlot leads; promises defense |
| **Socialist Victory** | Snap Election | Auto-completed if Spaak wins | Paul-Henri Spaak (Labour) leads; maintains border integrity |
| **Diplomatic Rapprochement** | Liberal Victory | Removes *Perpetual Neutrality* if has it. UK/France/major democratic gets event *Belgium Requests our Aid* | Open about friendships |
| **Join Allies** | Diplomatic Rapprochement; not in faction, fully independent | UK/France/US faction leader or random major gets event *Belgium seeks to join the Faction* |
| **Expression of Belgian Unity** | *Liberal Victory* OR *Socialist Victory* | Removes *Language Barriers* if has it | Diverse identities as strength |
| **Anti-Corruption Taskforce** | *Liberal Victory* OR *Socialist Victory* | Modifies *Corruption*: construction speed +5.0%, daily fascism −0.02 |
| **Belgian Maginot** | *Expression of Belgian Unity* OR *Anti-Corruption Taskforce*; can build 3+ land forts in Ardennes/Vlaanderen/Wallonie/Antwerpen on Dutch border; bypasses if cannot | If has *Defensive Neutrality*: modify by division defense on core +5.0%. Else if has *Defensive Reorganization*: modify by division defense on core +5.0%. Else: gets *Defensive Neutrality* with division defense on core +5.0%. Adds forts along Dutch border (hidden: 3 in Ardennes, 3 in Wallonie, 3 in Antwerpen, 3 in Vlaanderen) | Extension of French Maginot |
| **Expedite Fort Construction** | Belgian Maginot | If no land warfare facility: adds 1 in Wallonie or random state (if can build). If *Defensive Neutrality*: modify by land fort construction +15.0%. Else if *Defensive Reorganization*: modify by land fort construction +15.0%. Else: gets *Defensive Neutrality* with land fort construction +15.0% |
| **Democratization of Education** | Belgian Maginot | National spirit: research speed +5.00% | Social contract emphasis |
| **Unity Makes Strength** | *Expedite Fort Construction* OR *Democratization of Education* | Reduces *Economic Downturn* by: consumer goods factories −10.0%. War support +5.00%, stability +10.00%. Removes *Perpetual Neutrality*. If no defensive modifier: gets *Defensive Neutrality* with surrender limit +10.0%, training time −25.0%, mobilization speed +10.0%. Else modifies existing by same stats |
| **Better Than Maginot** | Unity Makes Strength; has land warfare facility | Completes special project *Stronghold network* (unlocks building: Stronghold network). If *Defensive Reorganization*: modify by land fort effectiveness +10.0%. Else: modify *Defensive Neutrality* by land fort effectiveness +10.0% | Trenches, bunkers, artillery emphasis |

### Raise the Red Flag/Soviet Guarantee/Support the European Project Sub-branch

Shared Socialist/Communist path offering two distinct trajectories after *Socialist Victory*.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Raise the Red Flag** | *Socialist Victory* OR *International Socialist Bureau* | Modifies *Socialist Sentiments*: daily communism +0.02, party popularity, stability +10.0%, stability +5.0%, war support +5.0%. Unlocks decisions to turn Belgium communist |
| **Soviet Guarantee** | *Socialist Victory* OR *Raise the Red Flag*; mutually exclusive with *Support the European Project*; any country: USSR exists, communist, fully independent, at peace; bypasses if USSR doesn't exist or isn't communist or has capitulated | If USSR exists and communist: USSR gets event *Belgium Requests our Aid* (likely to accept if completed *Raise the Red Flag*); if accepts: guarantee Belgium, opinion +15 both ways. By Blood Alone: equipment subsidy 1500.00 construction cost. Else: 1000K infantry equipment added to stockpile |
| **Invite Soviet Tank Developers** | Soviet Guarantee | By Blood Alone: Kirov MIO +2 sizes. Else: Kirov tank designer +15% armor research, armor tech armor +5%, hard attack +5% |
| **Join Comintern** | Soviet Guarantee; USSR: exists, communist, not in faction, fully independent | Random country (USSR): gets event *Belgium seeks to join the Comintern* |
| **Support the European Project** | *Socialist Victory* OR *International Socialist Bureau*; mutually exclusive with *Soviet Guarantee*; fully independent | If faction leader: rename to *European Union*. Else if in faction: leave and create *European Union*. Else: create *European Union*. Invites UK, France, Luxembourg, Netherlands, Spain if democratic/communist/independent. Events: Otto von Habsburg offer, EU formation |
| **European Community** | Support the European Project | Unlocks decisions for EU development. Becomes European President. Event: *The European Union Forms* |

## Monetary Reconstruction Branch

Industrial focus on economic recovery from post-WWI devastation and the Great Depression.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Monetary Reconstruction** | None | Reduces *Economic Downturn*: factory output +5.0%, daily political power +0.05 | Post-WWI hyperinflation recovery |
| **Stabilize Currency** | Monetary Reconstruction | Further reduces *Economic Downturn*: factory output +10.0% |
| **Stock Market Recovery** | Stabilize Currency | Further reduces *Economic Downturn*: factory output +10.0%, daily political power +0.05 |
| **International Cooperation** | Stock Market Recovery | Unlocks decision to trade with neighbors; international opinion +10% |
| **Economic Downturn** | Monetary Reconstruction (alternative: international focus) | National spirit: factory output −15.0% | Background modifier Belgium starts with |
| **Belgian Commerce** | Stock Market Recovery | Dockyard output +10.00%, trade route cost −5.0% |
| **Industrial Consolidation** | Stock Market Recovery | Random state: +1 building slot each civilian/military factory |
| **Fuel Acquisition** | International Cooperation | Trade agreement with oil-rich nation; fuel production +10.0% |

## Congo Investments Branch

Joint branch shared with Belgian Congo; focuses on colonial development, Force Publique military, and determining Congo's future.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Congo Investments** | None (available early) | Building slots in Belgian Congo; compliance +10% |
| **Reinforce Force Publique** | Congo Investments | Force Publique division equipment modernization; Belgian Congo can train divisions |
| **Colonial Holdings** | Reinforce Force Publique | Belgian Congo: building slots +2; compliance growth +10% |
| **Decide Congo's Future** | Colonial Holdings | Events/options on Congo's administrative status (autonomy, integration, independence) |
| **Extract Resources** | Congo Investments | Strategic resources: rubber, oil; production +10% |
| **Colonial Expansion** | Extract Resources | Can expand into neighboring African territories; annexation war goals on adjacent states |

> ⚠️ The Congo Investments Branch is jointly managed with Belgian Congo (separate country tag). See [Joint Congo](../01-mechanics/national-focus.md) for shared mechanics.

## Belgian Air Force Branch

Air power buildup and aircraft industry development.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Belgian Air Force** | None | Air experience +50; random state (prioritize Wallonie) gains +2 air bases |
| **Develop Belgian Air Industry** | Belgian Air Force | Random state gaining 2+ military factory slots: +2 building slots, +1 military factory. 2× 50% research bonus for Aircraft |
| **Design Innovation** | Develop Belgian Air Industry | 1× 100% research bonus for Light Fighter I–II or next CAS model (depending on choice) |
| **Helicopter Development** | Design Innovation (Helicopter path) | Research bonus for helicopter technology; unlocks helicopter production |
| **Jet Aircraft Focus** | Develop Belgian Air Industry | 1× 100% research bonus for Jet Fighter or Jet Strategic Bomber (depending on choice) |
| **Air Base Network** | Belgian Air Force | Multiple owned states: +1 air base each |
| **Anti-Air Defenses** | Belgian Air Force | Air defense buildings +10% construction speed; anti-air research bonus |
| **Aircraft Production Focus** | Design Innovation OR Jet Aircraft Focus | Random state: +2 military factory building slots, +2 military factories; aircraft production efficiency +5% |

## Re-Establish Belgian Navy Branch

Naval reconstruction and technology development; Belgium starts with minimal navy after 1927 abolition.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Re-Establish Belgian Navy** | None (any coastal state controlled) | Navy experience +50; random coastal state: +3 building slots, +3 naval dockyards | Navy abolished post-WWI; revival now needed |
| **Submarine Doctrine** | Re-Establish Belgian Navy | 1× 100% research bonus for Submarine I–II |
| **Cruiser Development** | Re-Establish Belgian Navy | 1× 100% research bonus for Light/Heavy Cruiser I–II |
| **Battleship Program** | Cruiser Development | 1× 100% research bonus for Battleship I |
| **Naval Bases Expansion** | Re-Establish Belgian Navy | Multiple coastal states: +2 naval dockyards each |
| **Trade Protection** | Re-Establish Belgian Navy | Research bonus for Naval Patrol doctrine; production efficiency +10% for destroyers/corvettes |
| **Torpedo Technology** | Submarine Doctrine | 1× 100% research bonus for Torpedo I–II |
| **Naval Base Fortification** | Naval Bases Expansion | Coastal defense buildings +15% construction speed; naval base level +1 |
| **Destroyer Escort Program** | Trade Protection | 1× 100% research bonus for Destroyer I–II |

## The King Surrenders Branch

Triggered when Belgium surrenders and becomes a government in exile; allows choices between republican/monarchist legitimacy and resistance/alignment paths.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The King Surrenders** | Belgium has capitulated and become exile | Event; country flag set for government in exile status | King Leopold III orders unconditional surrender (controversial) |
| **Remove the Monarchy** | The King Surrenders | Removes royal traits; becomes republic; stability −10.0%, political power +50 (paradoxical benefit of avoided royalist conflict) |
| **Restore Leopold III** | The King Surrenders | Restores Leopold as figurehead; war support −10.0%, legitimacy +20% |
| **Install Charles** | The King Surrenders | Charles, Count of Flanders becomes king; alternate monarchist path; stability +10.0% |
| **Rebuild Military in Exile** | The King Surrenders | Builds exile army training; army experience +50; can produce equipment in host nation |
| **Rally Belgian Resistance** | The King Surrenders | Unlocks decisions for resistance operations in occupied Belgium; compliance/resistance target modifiers on occupied states |
| **Government Legitimacy** | *Remove the Monarchy* OR *Restore Leopold III* OR *Install Charles* | Political power +100; diplomatic opinion +20% (legitimacy in eyes of allies) |
| **Exile Government Authority** | Government Legitimacy | War support +5.00%, stability +10.00%; recognized by faction allies |
| **Return and Restore** | Government Legitimacy; occupies former Belgian territories | Event option to transition from exile to restored government; cores restored; legitimacy complete |

---

## Notes on Dynamic Modifiers and National Spirits

Belgium's focus tree makes extensive use of dynamic modifiers (which stack and persist across related focuses) and temporary national spirits (which have fixed durations or persist for specific conditions):

- **Perpetual Neutrality** / **Defensive Neutrality** / **Defensive Reorganization**: These form a chain where later focuses replace/upgrade earlier versions with new modifiers while retaining accumulated bonuses.
- **Scars of the Great War**: Debuff Belgium starts with; most paths reduce or remove it.
- **Economic Downturn**: Base modifier Belgium starts with; reduced incrementally through Monetary Reconstruction and political paths.
- **Language Barriers**: Debuff limiting division organization and political power gain; removed by most political victory paths (Benelux, Council of Europe, Tripartite Government, Expression of Belgian Unity, etc.).
- **Academies of Belgium**: Meta-modifier accumulating research bonuses from multiple Defense Bill focuses.
- **Rexist Legion** / **The European Crusade**: Fascist path military/political bonuses.
- **Defensive Neutrality** modifiers: Include construction speed, entrenchment, fort effectiveness, and surrender mechanics.

## Strategic Paths Summary

Belgium's 1936 tree has three main strategic trajectories:

1. **Fortress Belgium** (Defensive Neutrality + Democratic/Socialist paths): Maximize fortifications, army training, and alliances (Allies/EU); economic recovery through Pierre Spaak or Pierlot; resist invasion through entrenchment and mobilization. Slow to medium military growth; defensive focus.

2. **Fascist Expansion** (Degrelle + Rexist/VNV paths): Rapid military buildup under Rexist or Vlaamsch Nationaal Verbond; low-economic-penalty through authoritarian centralization; territorial expansion via Burgundy → Dietsland → Belgica (Low Countries + Northern France); potential Axis alignment. Medium-to-fast military growth; expansionist focus.

3. **Communist/Soviet** (Socialist Victory + Soviet Guarantee or Comintern): Align with USSR; modest research sharing and equipment subsidies; ideological buildup; potential for European federation (democratic variant) or Soviet bloc (communist variant). Slow-to-medium growth; diplomatic focus.

All paths benefit from early Perpetual Neutrality/Independent, Neutral and Loyal declarations for construction speed and tension modifiers, and from Dyle Plan (opinion with France/UK) if pursuing democratic routes.

Note: Without Götterdämmerung DLC, Belgium falls back to the generic national focus tree.
