---
title: Argentinean National Focus Tree
category: focus-trees
tags: [argentina, focus tree, trial of allegiance, communist, democratic, fascist, non-aligned, expansion, south america]
game_version: "1.19"
dlc: [Trial of Allegiance]
sources:
  - https://hoi4.paradoxwikis.com/Argentinean_national_focus_tree
---

## Summary

Argentina's unique focus tree (requires Trial of Allegiance DLC) offers five major ideological branches plus an industrial path, reflecting the country's complex mid-20th century politics. Each path delivers distinct military and industrial bonuses, faction options, and South American expansion mechanics. Without the DLC, Argentina uses the generic tree. See 01-mechanics/national-focus.md for generic/continuous focuses.

See [Argentina](../05-countries/argentina.md) for the country's 1936 starting profile.

## A Call to Reform Branch (Communist)

Communist path triggering a civil war. Paths diverge after revolution: Rodolfo Ghioldi (Soviet alignment) or Fanny Edelman (independent communist South America).

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **A Call to Reform** | Mutually exclusive with: The Clean Election, Roberto María Ortiz | Political Power +120; Communism popularity +5.00%; Stability −5.00%; Remove Political Corruption; Modify Infamous Decade (Stability +10.00%, War support +2.00%, Daily Communism support +0.05) | Starting focus; opens communist path |
| **Support the Spanish Republicans** | A Call to Reform; Spain not at civil war end; Spain (Republican) exists; one of: Anti-Fascist Worker's Revolution or Maintain the Second Republic completed | Political Power +50; Stability −5.00%; Unlock sending volunteers to Republican Spain (tension −50.0%, max +50.0%, cost −75.0%) | Volunteers lever |
| **Invite Ghioldi Back to Argentina** | A Call to Reform | Rodolfo Ghioldi returns as available advisor; Communism popularity +5.00% | Flags ARG_ghioldi_returns |
| **Legitimize the PCA** | Invite Ghioldi Back | Communism popularity +10.00%; Fascism popularity −5.00%; Non-Aligned popularity −5.00%; Manpower +5000 | Accelerates communist support |
| **Reach Out to the Soviet Union** | Legitimize the PCA; Soviet Union: Communist, not in civil war, Viva La Revolución not completed | Unlocks Vanguardia Socialista division template; creates 5× Vanguardia Socialista units in Chubut (955) on civil war start | Soviet military support trigger |
| **Unite the Workers of Argentina** | Legitimize the PCA | United Workers national spirit (365 days): Stability −10.00%, Daily Communism support +0.05 | Builds revolutionary fervor |
| **Viva La Revolución** | One of: Reach Out to the Soviet Union or Unite the Workers; >60% Communism support | Triggers civil war (Non-Aligned vs Communists); Rodolfo Ghioldi becomes Communist leader; War support +10.00%, Justify war goal time −10.0%, Daily Communism support +0.10; known as República Popular Argentina | Civil war trigger |
| **Align with the Soviets** | Viva La Revolución; Mutually exclusive with: Forge Our Own Future; at peace with Soviet Union; fully independent; not in faction; Soviet Union: faction leader, Communist, fully independent, not in faction with Argentina | Soviet Union: Opinion +80; Argentina joins Soviet-Argentine Relations group; Soviet Union gets event (Argentina seeks Comintern) | Locks in Soviet path |
| **Soviet Industrial Model** | Align with the Soviets | Buenos Aires (278): +1 building slot, +1 military factory; Santa Fe (956): +1 building slot, +1 military factory | Industrial boost |
| **Committee of State Security** | Soviet Industrial Model | La Résistance enabled: create intelligence agency, +2 operative slots; otherwise: Encryption +2, +25%, Decryption +25% | Intelligence branching |
| **Soviet Manufacturers** | Soviet Industrial Model | Arms Against Tyranny enabled: Rubin Design Bureau, MiG Design Bureau, GAZ available (each +1 size); otherwise: Naval research +15%, Air research +15%, Motorized research +15%, Rocket artillery +50% | Design company/MIO options |
| **Centralize Power** | One of: Soviet Manufacturers or Committee of State Security | Communism popularity +20.00%; Manpower +50000; Political Power +100 | Consolidates communist rule |
| **Forge Our Own Future** | Viva La Revolución; Mutually exclusive with: Align with the Soviets; fully independent, not in civil war, not in faction | Fanny Edelman becomes Communist leader (Feminist Revolutionary); Daily Communism support +0.10; creates Internacional Sudamericana faction | Alternative communist path; female leader |
| **Women in Industry** | Forge Our Own Future | Women in Industry national spirit: Consumer goods factor −15.0%, Production efficiency cap +7.50% | Workforce expansion |
| **Support the Farmers** | Women in Industry | Agrarian Reforms national spirit: Consumer goods −10.0%, Factory output +10.00%, Daily Communism support +0.01 | Rural support |
| **Socialist Volunteers** | Women in Industry | Socialist Volunteers national spirit: Volunteer tension −20.0%, max +3, cost −50.0%; rule: can send volunteer forces | International communist aid |
| **The Buenos Aires Conference** | One of: Support the Farmers or Socialist Volunteers | Event: choose Fanny Edelman (unlocks Unify/Liberate Continent) or Antonio Soto (unlocks Improve Patagonia) | Event-driven path split |
| **Liberate The Continent** | One of: Centralize Power or Buenos Aires Conference; Mutually exclusive with: Unify The Continent; Antonio Soto not leader; any non-communist nation in South America | Annex war goal on all non-communist South American nations | Conquest path |
| **Integrate The Americas** | Liberate The Continent | Unlocks South American Unity decisions; Socialist Unification national spirit: Recruitable population factor +5%, Stability +5.00%, War support +5.00%, Daily Communism support +0.20 | Conquest integration |
| **Unify The Continent** | Buenos Aires Conference; Mutually exclusive with: Liberate The Continent; Antonio Soto not leader; Communist ruling party; fully independent, not in faction | Sends faction invitations to communist South American nations; event: Unify the Continent | Diplomatic communist path |
| **Ocaso Escarlata** | One of: Unify The Continent or Liberate The Continent | Known as The South American Socialist Republics; Operación Ocaso Escarlata national spirit (730 days): Recruitable population +10%, Supply consumption −5.0%, War support +20.00%, Division attack +10.0%, Daily Communism support +0.15 | End-state: continental communism |
| **Improve Patagonia** | Buenos Aires Conference; Antonio Soto current leader; Río Negro (512), Chubut (955), Santa Cruz (954), Tierra del Fuego (953) owned/controlled | Río Negro: +1 slot, +1 civilian factory; Chubut: +1 slot, +1 civilian factory; Santa Cruz: +1 slot, +1 civilian factory; Tierra del Fuego: +1 slot, +1 civilian factory | Anarcho-syndicalist path |
| **Establish the Free Association** | Improve Patagonia | Free Association of Producers national spirit: Stability +10.00%, Military factory construction +5.00%, Civilian factory construction +5.00% | Anarchist ideology |
| **No Gods No Masters** | Establish the Free Association | Every South American state with occupation/resistance: Liberate war goal; ¡Liberación! national spirit: Army experience +0.20 daily, Supply consumption −5.0%, War support +10.00%, Division attack +10.0% | Liberation wars |
| **Workers Rights** | One of: Forge Our Own Future or Align with the Soviets | State Unions national spirit: Production efficiency cap +7.50%, Military factory construction +5.00%, Civilian factory construction +5.00%; Stability +10.00% | Worker protections |
| **Reform Our Industry** | Workers Rights | Random owned/controlled/cored state: +3 building slots, +3 civilian factories | Industrial growth |
| **Empower the FJC** | Reform Our Industry | FJC Empowered national spirit: Recruitable population +0.50% factor, +5% factor, War support +5.00%, Daily Communism support +0.02 | Youth mobilization |
| **State Atheism** | Empower the FJC; Mutually exclusive with: Liberation Theology | State Atheism national spirit: Stability −10.00%, War support +10.00%, Research speed +5.00% | Religious suppression |
| **Liberation Theology** | Empower the FJC; Mutually exclusive with: State Atheism | Liberation Theology national spirit: Political power gain +20%, Stability +20.00%, Research speed −5.00% | Religious tolerance path |
| **Socialist Researchers** | One of: State Atheism or Liberation Theology | +1 research slot | Research expansion |

## The Clean Election Branch (Democratic)

Democratic path via Unión Cívica Radical. Builds industry, reduces corruption, and forges international alliances or maintains internal focus.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The Clean Election** | Mutually exclusive with: A Call to Reform, Roberto María Ortiz | Political Power +120; Modify Infamous Decade (Stability +10.00%, War support −10.00%, Daily Democracy support +0.05) | Starting focus |
| **In Memory of Yrigoyen** | The Clean Election | Marcelo T. De Alvear becomes Democratic leader; Democracy popularity +15.00% | Historical democratic leader |
| **Anti-Corruption Policies** | In Memory of Yrigoyen | Remove Political Corruption; Anti-Corruption Policy modifier: Stability +15.00%, War support −20.00%, Production efficiency cap +10.00%, Daily Democracy support +0.03, Daily Unaligned support +0.02 | Integrity restoration |
| **Reinforce the Education System** | Anti-Corruption Policies | 1× 50% Electronics bonus; 1× 50% Industry bonus; 1× 100% Synthetic Rubber bonus | Research boosters |
| **University Reforms** | Reinforce the Education System | +1 research slot | Academic investment |
| **A True Democracy** | Anti-Corruption Policies | Stability +2.00%; Random fully controlled/cored state: +1 building slot, +1 civilian factory; Democracy popularity +5.00% | Democratic consolidation |
| **Promote Urbanization** | In Memory of Yrigoyen | Buenos Aires (278): +1 slot, +1 civilian factory; Santa Fe (956): +1 slot, +1 civilian factory | Urban development |
| **Secure the Opposition** | Promote Urbanization | Communism popularity −5.00%; Fascism popularity −5.00%; Non-Aligned popularity −5.00% | Opposition suppression |
| **Regulated National Salaries** | Promote Urbanization | Regulated Salaries national spirit: Stability +5.00%, Production efficiency cap +7.50%, Military factory construction +5.00%, Civilian factory construction +5.00% | Wage controls |
| **The Social Welfare Fund** | Regulated National Salaries | Social Welfare Fund national spirit: Consumer goods +2.0%, Stability +5.00%, Daily Democracy support +0.03; Buenos Aires (278): +3 building slots | Welfare state |
| **Argentina for All** | One of: A True Democracy or Secure the Opposition | Argentina for All national spirit: Recruitable population +15% factor, Stability +10.00%, Division defense on core +10.0%, Daily Democracy support +0.15 | Inclusive democracy |
| **Seek American Support** | Argentina for All; Mutually exclusive with: Internal Focus, Closer Ties With Britain; United States: Democratic, fully independent | Political Power +100; Opinion ↔ United States +50 | US alliance start |
| **U.S. Army Training** | Seek American Support; Mutually exclusive with: American Defense Investments | U.S. Army Training national spirit: Army experience +0.10 daily, Division defense on core +10.0%; 2× 25% Special Forces bonus | Military cooperation |
| **American Defense Investments** | Seek American Support; Mutually exclusive with: U.S. Army Training | Buenos Aires (278): +2 slots, +2 anti-air; Región Mesopotámica (510): +2 slots, +2 anti-air; Formosa (957): +2 slots, +2 anti-air | Air defense |
| **Joint Military Exercises** | One of: U.S. Army Training or American Defense Investments | Air experience +50; Navy experience +50; United States gets event | Military training |
| **Internal Focus** | Argentina for All; Mutually exclusive with: Seek American Support, Closer Ties With Britain | Political Power +100; Limited Exports trade law: Construction +5.00%, Research +1.00%, Factory output +5.00%, Dockyard output +5.00%, Resources to market +25%, Lend-lease tension +20.00%; Random owned/controlled/cored state: +1 slot, +1 civilian factory | Autarky path |
| **Alvear's Democracy** | Internal Focus | Leader gains Father of Argentine Democracy: Stability +20.00%, Party popularity stability +5.00%, Research speed +10.00%, Justify war goal time +10.0%, Daily Democracy support +0.05; loses Harsh Democrat | Leader buff |
| **Closer Ties With Britain** | Argentina for All; Mutually exclusive with: Seek American Support, Internal Focus; United Kingdom: exists, Democratic, at peace, fully independent | British-Argentinean Agreement national spirit: United Kingdom trade cost −20.00%; Opinion ↔ United Kingdom +50 | British alliance |
| **Royal Air Force Influence** | Closer Ties With Britain; Mutually exclusive with: Royal Navy Influence; United Kingdom: exists, Democratic, at peace, fully independent | Air experience +25; Aerodynamics breakthrough +25.00%; 3× 40% Aircraft bonus; if Arms Against Tyranny & By Blood Alone enabled: equipment subsidies (Fighter 500, CAS 500, Tactical Bomber 200) or By Blood Alone only: 200 British Fighter I, 100 British CAS I; otherwise: 200 British Fighter I, 100 British CAS I | Air partnership |
| **Royal Navy Influence** | Closer Ties With Britain; Mutually exclusive with: Royal Air Force Influence; United Kingdom: exists, Democratic, at peace, fully independent | Navy experience +25; Naval Engineering breakthrough +25.00%; 3× 40% Ships bonus; if Arms Against Tyranny enabled: Convoy subsidy 500; otherwise: 200 British Convoy | Naval partnership |
| **Reinforcing the Cooperation** | One of: Royal Navy Influence or Royal Air Force Influence; United Kingdom: exists, Democratic, at peace, fully independent | Democracy popularity +5.00%; Stability +5.00%; United Kingdom gets event (seeks closer cooperation, likely to accept with high opinion) | Cooperation deepening |
| **Bastion of Peace** | One of: Joint Military Exercises, Alvear's Democracy, or Reinforcing the Cooperation; Mutually exclusive with: Join the Allies; fully independent, not in faction | Political Power +50; War support +5.00%; creates Monroe Alliance faction; rules: can send volunteers, can create factions, cannot join factions | Neutral faction |

## Join the Allies / Align with the Monroe Doctrine Sub-branch

Democratic/shared path allowing Allies joining or regional alignment. Accessible from Clean Election branch.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Join the Allies** | One of: Joint Military Exercises, Alvear's Democracy, Reinforcing the Cooperation, or The American Push; Mutually exclusive with: Bastion of Peace, Reject the Allies; major democratic country faction leader, fully independent, not in faction | Random major democratic faction leader gets event (Argentina seeks to join); bypassed if already in Allies faction | Allies path |
| **Align with the Monroe Doctrine** | One of: Join the Allies or Bastion of Peace | Aligned with the Monroe Doctrine national spirit (730 days): Recruitable population +10% factor, Division defense on core +20.0%, Military factory construction +5.00%, Civilian factory construction +5.00% | Continental defense |
| **American Allyship** | Align with the Monroe Doctrine; United States: at war with major country, Democratic, at peace with Argentina | Close Ties with Washington national spirit (730 days): War support +5.00%, Construction speed +10.00%, Naval doctrine cost −5.00%, Daily Democracy support +0.01 | US cooperation |
| **Counter Intelligence Program** | American Allyship | La Résistance enabled: create intelligence agency; otherwise: Encryption +5.00%, Decryption +5.00% | Counter-espionage |
| **End Operation Bolívar** | Counter Intelligence Program; Germany: not same ideology as Argentina | La Résistance: Working Against Operation Bolívar national spirit: +2 operative slots; otherwise: Disrupted Operation Bolívar: Encryption +2, +25%, Decryption +25% | German espionage counter |
| **U.S. Marine Training Program** | American Allyship | 1× 50% Special Forces Doctrine cost reduction | Elite training |
| **The Red Scare** | U.S. Marine Training Program; Soviet Union: Communist, exists | Soviet Union opinion −80; Anti-Soviet Sentiments national spirit (730 days): War support +5.00%, Daily Communism support −0.1 (Soviet Union), Attack/Defense vs Soviet Union +10.0% | Anti-communist stance |
| **Extinguish South American Communism** | One of: The Red Scare or The Second Argentine Republic; communist South American nation exists | Puppet war goal on all communist South American nations | Regional anti-communism |
| **Pan-American Cooperation** | Align with the Monroe Doctrine; not completed: Joint Military Exercises or Reinforcing the Cooperation; Democratic; democratic South American nation exists, not in faction, fully independent | Sends faction invitations to democratic South American nations | Democratic bloc |
| **Recruitment Drive** | Pan-American Cooperation | Army experience +50; Manpower +20000 | War mobilization |
| **The Second Argentine Republic** | Recruitment Drive | Known as The Second Argentine Republic; guarantees all democratic South American nations | Regional guarantees |
| **Envoy to London** | Align with the Monroe Doctrine; United Kingdom: at war with major country, Democratic, at peace with Argentina | Close Ties with London national spirit (730 days): Recruitable population +5% factor, War support +5.00%, Air doctrine cost −5.00%, Daily Democracy support +0.01 | UK relations |
| **Study the Battle of the River Plate** | Envoy to London | 1× 50% Naval Doctrine cost reduction; Naval Engineering breakthrough +25.00% | Naval study |
| **Firmes Volamos** | Study the Battle of the River Plate | RAF Cooperation national spirit: Ace generation +10.00%, Air mission experience +20%, Air superiority efficiency +10% | RAF support |
| **Extinguish South American Fascism** | One of: Firmes Volamos or The Second Argentine Republic; fascist South American nation exists | Puppet war goal on all fascist South American nations | Regional anti-fascism |
| **Islas del Atlántico Sur** | Envoy to London; Falkland Islands (299) and South Georgia (720) not owned/controlled by Argentina; bypassed if both owned/controlled | Event to other nations: Argentina requests South Atlantic Islands ownership | Claims South Atlantic Islands |
| **Improving the Islands** | Islas del Atlántico Sur; Falkland Islands (299) and South Georgia (720) owned/controlled | Falkland Islands: +3 slots, +2 naval dockyards, +4 coastal forts, +2 naval bases; South Georgia: +3 slots, +2 naval dockyards, +4 coastal forts, +2 naval bases | Island fortification |

## Roberto María Ortiz Branch (Historical Non-Aligned)

Historical non-communist path. Emphasizes democracy and stability but allows military/fascist interventions. Splits into democratic (Clean Election), fascist (Work with Nationalists), or Perón-era leadership.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Roberto María Ortiz** | Mutually exclusive with: A Call to Reform, The Clean Election | Political Power +120; Modify Infamous Decade (Stability −5.00%, War support −5.00%, Daily Fascism support +0.03, Daily Unaligned support +0.03); Roberto María Ortiz becomes Concordancia leader | Historical start |
| **El Manifiesto Concordancia** | Roberto María Ortiz; Mutually exclusive with: Work With The Nationalists; any owned state can build +1 military factory | Non-Aligned popularity +5.00%; Democracy popularity +2.00%; Random owned/controlled/cored state (with factory capacity): +1 slot, +1 military factory | Democratic restoration |
| **Crackdown on Corruption** | One of: El Manifiesto Concordancia or Work With The Nationalists | Remove Political Corruption; Crackdown on Corruption modifier: Stability +10.00%, Production efficiency cap +10.00%, Daily Unaligned support +0.02, Daily Fascism support +0.02, War support −10.00% | Anti-corruption drive |
| **British Economics** | El Manifiesto Concordancia | British Economics national spirit: Trade laws cost −50%, Economy laws cost −50%, Daily Democracy support +0.05; Opinion ↔ United Kingdom +25 | British economic ties |
| **Import Substitution** | British Economics | Random owned/controlled/cored state (with factory capacity): +2 slots, +2 civilian factories | Industrial substitution |
| **Emphasis on Public Works** | Import Substitution | Public Works Investment national spirit (365 days): Stability +5.00%, Construction speed +10.00%, Infrastructure construction +15.00% | Depression relief |
| **Towards a Greater Argentina** | Emphasis on Public Works | Towards a Greater Argentina national spirit (730 days): Consumer goods −10.0%, Production efficiency cap +10.00%, Factory output +10.00% | Economic recovery |
| **Universidad de Buenos Aires** | Towards a Greater Argentina | +1 research slot | Education investment |
| **The Castillo Cabinet** | British Economics | Ramón Castillo becomes Concordancia leader; starts Military Dissent timed missions | Government transition |
| **Maintain the Status Quo** | The Castillo Cabinet; Mutually exclusive with: Consolidating Power | Political Power +50; Stability +10.00% | Conservative path |
| **Intervenciones Federales** | Maintain the Status Quo | Political Power +50; Stability +10.00%; unlocks Intervenciones Federales decisions (counteract Military Cells); bypassed if in civil war | Military management |
| **Subdue Dissension** | Intervenciones Federales (3 Federal Intervention Measures taken); bypassed if in civil war | Removes military cell modifiers; Subdued Dissension national spirit (365 days): Recruitable population −10% factor, Army leader cost +10.0%, Daily Democracy support +0.10, Daily Unaligned support +0.20 | Coup prevention |
| **Consolidating Power** | The Castillo Cabinet; Mutually exclusive with: Maintain the Status Quo; bypassed if in civil war | Removes 150 days from Imminent Military Coup timer; Non-Aligned popularity +15.00%; Democracy popularity −10.00%; Political Power +100; Stability −20.00% | Authoritarian shift |
| **March to Casa Rosada** | Consolidating Power; bypassed if in civil war | Ends Imminent Military Coup mission; Military takes over; gets event (Army Turns Against Us) | Military coup |
| **Balancing Act** | March to Casa Rosada | Arms Against Tyranny enabled: unlocks Balancing Act decisions (balance US/UK or Germany/Italy with equipment subsidies); otherwise: same decisions | Diplomatic neutrality |
| **Juan Perón** | Balancing Act; Juan Perón is active leader | Juan Perón becomes Non-Aligned (Peronism); Political power gain +10%, Stability +5.00%, Production efficiency cap +5.00%, Division defense on core +5.0%; promoted to Field Marshal | Peronist takeover |
| **Peronism** | Juan Perón | Peronism (Justicialism) party; Eva Perón available advisor (Recruitable population +5% factor, Stability +10.00%); Political Power +50; Random owned/controlled/cored state (with factory capacity): +1 slot, +1 civilian factory | Peronist consolidation |
| **The American Push** | One of: Balancing Act or Subdue Dissension | Event: United States requests German embargo | US pressure |
| **Reject the Allies** | The American Push; Mutually exclusive with: Join the Allies | Event: United States embargoes Argentina; Dedicated to Ourselves national spirit: Consumer goods −10.0%, Stability +5.00%, Improve relation cost +10%, Production efficiency cap +5.00%, Research speed +5.00% | US embargo path |
| **Our Own Path** | One of: Reject the Allies or Argentina First | Political Power +100; Our Own Path national spirit: Recruitable population +15% factor, War support +10.00%, Conscription laws cost −25% | Independent path |

## Work With The Nationalists Sub-branch (Fascist)

Fascist path via nationalist collaboration. Includes military government (Guardia Nacional) or UNF (Unión Nacional Fascista) branches, regional expansion, and Axis alignment options.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Work With The Nationalists** | Roberto María Ortiz; Mutually exclusive with: El Manifiesto Concordancia | Growing Nationalist Movement modifier: Daily Fascism support +0.05, Recruitable population +2% factor, Stability +5.00%, Daily Democracy support −0.02; removes military cell modifiers | Fascist pivot |
| **Cut Ties With Britain** | Work With The Nationalists | United Kingdom opinion −50; replaces Roca-Runciman Treaty with Anti-British Sentiment: Consumer goods −10.0%, War support +5.00%, Daily Fascism support +0.01 | British rupture |
| **Support Radical Nationalism** | Cut Ties With Britain | Modifies Growing Nationalist Movement: Daily Fascism support +0.10, Recruitable population +10.00%, War support +5.0%, Daily Democracy support −0.05 | Nationalist fervor |
| **Encourage German Investments** | Support Radical Nationalism; Germany: Fascist, exists | Buenos Aires (278): +1 slot, +1 military factory; 2× 50% Industry bonus; Opinion ↔ Germany +50 | German economic ties |
| **Guardia Nacional** | Encourage German Investments; Mutually exclusive with: Unión Nacional Fascista; >60% Fascism support; bypassed if Señor Hilter is leader | Military Government national spirit: Recruitable population +10% factor, War support +10.00%, Training time +15.00%, Daily Fascism support +0.15; known as Argentina Legionaria; Pedro Pablo Ramírez becomes Guardia Nacional leader; removes Growing Nationalist Movement | Military government |
| **Rapid Militarization** | Guardia Nacional | Random core state: +2 slots, +2 military factories; Rapid Militarization national spirit (365 days): War support +10.00%, Production efficiency cap +15.00%, Military factory construction +10.00% | Militarization |
| **Italo-Argentine Diplomacy** | Support Radical Nationalism; Italy: Fascist, exists | Joins Italian Argentine Agreement research group; Opinion ↔ Italy +50 | Italian research tie |
| **Unión Nacional Fascista** | Italo-Argentine Diplomacy; Mutually exclusive with: Guardia Nacional; >60% Fascism support; bypassed if Señor Hilter is leader | Spirit of the Conquistadors national spirit: War support +10.00%, Division attack +6.0%, Justify war goal time −20.0%, Daily Fascism support +0.15; known as Confederación Argentina; Nimio de Anquín becomes Fascist leader; removes Growing Nationalist Movement | Fascist civilian government |
| **Argentine Nationalism** | Unión Nacional Fascista | Argentine Nationalism national spirit: Recruitable population +7% factor, War support +10.00%, Civilian factory construction +6.00%; Random core state: +2 slots, +2 military factories | Nationalist mobilization |
| **War Division** | One of: Rapid Militarization or Argentine Nationalism | War Division national spirit (365 days): Weekly manpower +250, Daily Fascism support +0.12, Civilian factory construction +5.00% | War preparation |
| **Argentina First** | War Division; Mutually exclusive with: Join the Axis; fully independent, not in faction; bypassed if in faction | Political Power +50; War support +5.00% (if leaving faction); Argentina First national spirit: Army experience +0.10 daily, Recruitable population +10% factor, Stability +5.00%, War support +5.00%; creates Confederación Fascista faction; rules: can send volunteers, can create factions, cannot join factions | Fascist neutrality |
| **Join the Axis** | War Division; Mutually exclusive with: Argentina First; fully independent; Germany: exists, Fascist; bypassed if Germany doesn't exist or has been defeated | Germany gets event (Argentina seeks to join Axis) | Axis membership |
| **Revive the Colonial Plan** | Cut Ties With Britain; Mutually exclusive with: Establishing a Foothold; Germany: in faction with Argentina; Uruguay: exists, at peace, not subject, not in faction with Argentina; bypassed if Uruguay meets opposite conditions | Uruguay gets event (Argentina issues ultimatum for puppet) | Puppet Uruguay path |
| **Establishing a Foothold** | Cut Ties With Britain; Mutually exclusive with: Revive the Colonial Plan; Uruguay exists | Annex war goal on Uruguay | Conquest Uruguay path |
| **Corporatism** | Cut Ties With Britain | Political Power +50; Fascism popularity +10.00%; Buenos Aires (278): +2 slots, +2 military factories | Corporatist state |
| **Reestablish Ligas Patrióticas** | Corporatism | Stability +5.00%; unlocks Ligas Patrióticas division template; recruits 5× Ligas Patrióticas units in Buenos Aires (278) | Paramilitary mobilization |
| **Fascist Researchers** | Reestablish Ligas Patrióticas | +1 research slot | Research expansion |
| **Support the Spanish Coup** | Cut Ties With Britain; Spanish Civil War begun, not ended; Spain exists; Nationalist Spain flag set | Political Power +50; Stability −5.00%; unlock sending volunteers to Nationalist Spain (tension −50.0%, max +50.0%, cost −75.0%) | Spanish Civil War support |
| **Demand Compensation From Spain** | Support the Spanish Coup; Spanish Civil War ended; Nationalist Spain: not capitulated, owns Equatorial Guinea (297); Argentina sent volunteers to Nationalist Spain | Nationalist Spain gets event (Argentina demands Equatorial Guinea) | Spain compensation |
| **Invite Spanish Nationalists** | Support the Spanish Coup; Spanish Civil War ended; La Résistance enabled: any non-Nationalist Spain exists, not in civil war; otherwise: Spain is Fascist/Non-Aligned, not in civil war | Manpower +25000; Army experience +75 | Spanish nationalist refugees |

## Dominate the South Sub-branch (Expansion)

Conquest path for regional domination in South America. Prerequisites depend on earlier ideological choices (Reject Allies, Argentina First, or Join Axis). Delivers war goals and expansion mechanics.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Dominate the South** | One of: Reject the Allies, Argentina First, or Join the Axis | Preparing for War national spirit (730 days): War support +5.00%, Division attack on core +15.0%, Division defense on core +10.0%, Factory output +5.00%, Dockyard output +5.00%; event sent to South American countries | Expansion start |
| **Integrate Operation Bolívar** | Dominate the South | La Résistance enabled: create intelligence agency; Integrating Operation Bolívar national spirit: +2 operative slots; otherwise: Encryption +2, +25%, Decryption +25% | German espionage integration |
| **Release Hellmuth** | Integrate Operation Bolívar | Event: decide whether to free Osmar Hellmuth and employ him as operative or leave imprisoned | Intelligence recruitment |
| **Anti-American Propaganda** | Release Hellmuth; United States: Democratic, exists | United States opinion −80; Anti-American Propaganda national spirit (730 days): War support +5.00%, Daily Democracy support −0.10 (US), Attack/Defense vs US +10.0% | Anti-US stance |
| **Conquer The Republic of Paraguay** | Dominate the South; Mutually exclusive with: Paraguayan Ultimatum; Paraguay exists; bypassed if Paraguay meets opposite conditions | Annex war goal on Paraguay | War path vs Paraguay |
| **Paraguayan Ultimatum** | Dominate the South; Mutually exclusive with: Conquer The Republic of Paraguay; Paraguay exists; bypassed if Paraguay meets opposite conditions | Paraguay gets event (Argentina issues ultimatum for puppet) | Puppet path vs Paraguay |
| **Reach Out to Chile** | One of: Conquer Paraguay or Paraguayan Ultimatum; Mutually exclusive with: Chilean Ultimatum; Argentina: faction leader; Chile: at peace, not subject, not in faction; Santa Cruz (954) and Tierra del Fuego (953) owned/controlled by Argentina; bypassed if Chile meets opposite conditions | Chile gets event (Argentina seeks alliance); more likely to accept if Fascist/Non-Aligned and high opinion; cede Santa Cruz and Tierra del Fuego if accepted | Alliance path vs Chile |
| **Chilean Ultimatum** | One of: Conquer Paraguay or Paraguayan Ultimatum; Mutually exclusive with: Reach Out to Chile; Chile: at peace, not subject, not in faction; bypassed if Chile meets opposite conditions | Chile gets event (Argentina issues ultimatum for puppet) | Conquest path vs Chile |
| **The Old Enemy** | One of: Reach Out to Chile or Chilean Ultimatum; Brazil exists, not subject, not in faction with Argentina; bypassed if Brazil meets opposite conditions | Annex war goal on Brazil; Spirit of the Cisplatine War national spirit (730 days): War support +10.00%, Training time −25.00%, Daily Fascism support +0.15 (Brazil), Attack/Defense vs Brazil +10.0% | Brazilian conquest |
| **South American Unity** | The Old Enemy | Unlocks South American Unity decisions (integrate conquered territories); if completed Unión Nacional Fascista: known as La Confederación Sudamericana; if completed Guardia Nacional or Non-Aligned: known as La Sudamérica Legionaria | Continental unification |
| **Preparations for War** | Dominate the South | Build level 1 railway: Formosa (957) to Tucumán (508); Build level 1 railway: Santa Cruz (954) to Chubut (955); Santa Cruz: +1 supply hub; Formosa: +1 supply hub | Supply infrastructure |
| **The War Machine** | Dominate the South | Río Negro (512): +1 slot, +1 military factory; Santa Fe (956): +1 slot, +1 military factory; San Luis y La Pampa (958): +1 slot, +1 military factory | Military industrialization |
| **Secure the Borders** | The War Machine | 3 random army leaders without Ranger trait gain Ranger (Forest +5.0% movement, +10.0% attack, +10.0% defense); Tierra del Fuego (953), Santa Cruz (954), Chubut (955), Río Negro (512), Mendoza (511), San Juan y La Rioja (960), Tucumán (508), Los Andes (959), Región Mesopotámica (510): +1 land fort each | Border fortification |
| **Argentine Island Sovereignty** | Secure the Borders | Unlocks Island Negotiations decisions (peace deal with UK if not in larger war); Falkland Islands (299) and South Georgia (720) become cores; Annex war goal on UK if at peace with Argentina | South Atlantic Islands claims |

## Fourth Time's The Charm Branch (Easter Egg)

Hidden branch unlocked when Señor Hilter (a humorous character) becomes Argentina's leader. Highly satirical focus tree mimicking alternate history themes.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Fourth Time's The Charm** | Señor Hilter is leader of Argentina | Known as The Fourth Reich; removes Growing Nationalist Movement modifier | Hidden easter egg branch |
| **Guerra Relámpago** | Fourth Time's The Charm | Annex war goals on all non-fascist South American nations; gains cores on all former German states; event to South American capitals | Blitzkrieg expansion |
| **Arma Maravillosa** | Fourth Time's The Charm | If Atomic Research & Experimental Rockets researched: +1 breakthrough each; if Atomic only: 1× 50% Rocketry bonus, Nuclear research +50.00%; if Rockets only: 1× 50% Nuclear bonus, Aerodynamics +50.00%; if neither: gain Nuclear Reactor & Experimental Rockets techs | Wonder weapons research |
| **Recover The Ship** | Fourth Time's The Charm | Gains Panzerschiff technology; creates Deutschland-class capital ship variant; adds production line | Graf Spee recovery |

## Banco Central de la República Argentina Branch (Industrial)

Industrial and economic path available to all ideologies. Emphasizes factory construction, research, infrastructure, trade treaties, and resource extraction.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Banco Central de la República Argentina** | None (available to all paths) | Available as Central Bank concern: Industrial research speed +20%, Consumer goods factor −5.0% | Starting industrial focus |
| **Production Initiative** | Banco Central | 2× 50% Production bonus | Production tech boost |
| **Develop the Electricity Sector** | Production Initiative | 1× 50% Electronics bonus | Electrification |
| **Invest in Construction Guilds** | Develop the Electricity Sector | Argentine Construction Guilds national spirit: Construction speed +10.00% | Construction boost |
| **Technical Schools** | Invest in Construction Guilds; >45 factories | +1 research slot; available advisors: Vicente C. Gallo (Research speed +10.00%), Carlos Saavedra Lamas (Volunteer tension −20.0%, Justify war goal time ±30.0%) | Education/advisor option |
| **Industrial Expansion** | Banco Central | Random owned/controlled/cored state: +1 slot, +1 civilian factory; 2× 50% Industry bonus | General industrialization |
| **Rapid Urbanization** | Industrial Expansion; Buenos Aires (278), San Luis y La Pampa (958), Santa Fe (956) controlled | Buenos Aires, San Luis, Santa Fe: +1 slot each, +1 civilian factory each | Urban expansion |
| **Agricultural Improvements** | Industrial Expansion; one of: Río Negro (512), Santa Cruz (954), Chubut (955) owned/controlled | If Río Negro: +1 slot, +1 infrastructure; if Santa Cruz: +1 slot, +1 infrastructure; if Chubut: +1 slot, +1 infrastructure | Agriculture development |
| **Military Production Lines** | One of: Rapid Urbanization or Agricultural Improvements; Buenos Aires, Santa Fe controlled | Buenos Aires, Santa Fe: +1 slot each, +1 military factory each | Military factory expansion |
| **Capitalize the Beef Industry** | One of: Agricultural Improvements or Rapid Urbanization | Argentine Beef national spirit: Consumer goods −15.0%, Infrastructure construction +15.00% | Beef export focus |
| **Revisit the Roca-Runciman Treaty** | One of: Military Production Lines or Capitalize the Beef Industry; Mutually exclusive with: Revise the Roca-Runciman Treaty; not completed Cut Ties With Britain | Replaces Roca-Runciman with Eden-Malbrán Treaty: Consumer goods −10.0%, Resources to market +10%, Civilian factory construction +5.00%, Trade laws cost −10%, Economy laws cost −10% | Treaty renegotiation |
| **Revise the Roca-Runciman Treaty** | One of: Military Production Lines or Capitalize the Beef Industry; Mutually exclusive with: Revisit the Roca-Runciman Treaty; in faction; one of: Cut Ties completed or Viva La Revolución completed | Replaces Roca-Runciman with La Plata Treaty: Resources to market +10%, Trade laws cost −15%, Economy laws cost −15%, Civilian factory construction +10.00%; faction leader gets Argentine Beef Trade (Division attrition −5.0%, Supply consumption −5.0%, Consumer goods −5.0%, Supply efficiency +5%) | Revised trade agreement |
| **Reach out to the Great Powers** | Banco Central | Unlocks International Loan decisions; if accepted: International Loan modifier: Political power cost −20.0%, Resource gain efficiency +5.0%, Construction speed +4.0%, Factory output +6.0%, Dockyard output +6.0% | International loans |
| **Economic Tax Reforms** | Banco Central | Random owned/controlled/cored state (infrastructure capacity): +2 slots, +2 infrastructure | Tax reform |
| **Invest in the Roads** | Economic Tax Reforms | Invested in the Roads national spirit (365 days): Infrastructure construction +15.00% | Road investment |
| **Invest in the Railways** | Economic Tax Reforms | Invested in the Railways national spirit (365 days): Supply hub construction +30.00%, Railway construction +15.00%; available as Railway Company concern: Train cost +25%, Armor +15%, Supply hub construction +15%, Railway construction +15% | Rail investment |
| **Expand Steel Extraction** | One of: Invest in the Roads or Invest in the Railways; San Luis y La Pampa (958) controlled | San Luis: +8 steel production; if doesn't have modifier: Focus on Resource Extraction national spirit (365 days): Resource gain efficiency +15.00% | Steel extraction |
| **Expand Aluminum Extraction** | One of: Invest in the Roads or Invest in the Railways; Los Andes (959) controlled | Los Andes: +8 aluminum production; if doesn't have modifier: Focus on Resource Extraction national spirit (365 days): Resource gain efficiency +15.00% | Aluminum extraction |
| **Yacimientos Petrolíferos Fiscales** | One of: Expand Aluminum Extraction or Expand Steel Extraction | Unlocks Exploit la Vaca Muerta decision; available as Refining concern: Industrial research +20%, Synthetic resources research +35% | Oil company |
| **Economic Reactivation Act** | Banco Central | Economic Reactivation national spirit (365 days): Civilian factory construction +10.00% | Reactivation bill |
| **Immigration Wave** | Economic Reactivation Act | Sets flag JUNO_promote_immigration_flag; unlocks Promote Immigration to South America decisions | Immigration policy |
| **Develop Civilian Economy** | Immigration Wave | Random owned/controlled/cored state (civilian factory capacity): +2 slots, +2 civilian factories; Developed Civilian Economy national spirit (365 days): Consumer goods −15.0% | Civilian economy |
| **The Argentinean Metropole** | Develop Civilian Economy; Buenos Aires (278) controlled | Argentine Metropole national spirit: Recruitable population +5% factor, Stability +10.00%, Research speed +10.00% | Metropolitan development |

## Trial of Allegiance Shared Military Branches

This focus tree includes shared military branches from the Trial of Allegiance DLC. These branches unlock special national spirits and military bonuses based on the player's ideological choices and alliances with other South American nations. Specific details on conditional bonuses and requirements are integrated into the branches above. For detailed shared military mechanics, see the Trial of Allegiance shared military focus tree documentation.
