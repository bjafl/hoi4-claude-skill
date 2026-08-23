---
title: Austrian National Focus Tree
category: focus-trees
tags: [Austria, focus tree, Götterdämmerung DLC, political ideology, military buildup, Danubian Federation, Austro-Hungarian]
game_version: "1.19"
dlc: [Götterdämmerung]
sources:
  - https://hoi4.paradoxwikis.com/Austrian_national_focus_tree
---

## Summary

Austria receives a unique national focus tree unlocked by the Götterdämmerung DLC expansion; without it, Austria uses the generic focus tree. The tree features seven main branches spanning five ideological paths (Communist via Austromarxism/Austrostalinism/Austrotrotskyism, Democratic republic, Monarchist Habsburg restoration, Fascist Austrofascism, and Danubian Federation), plus shared military and industrial development branches. Most paths conclude with war: communists and democrats fight Germany and/or the Soviet Union depending on allegiances; monarchists annex or subjugate neighboring Balkan states; fascists resist German Anschluss with Italian backing. All nations share access to army, air force, and navy branches. The Austro-Hungarian joint branch unlocks for Danubian or Monarchist annexation paths. See [Austria](../05-countries/austria.md) for the country's 1936 starting profile.

## Branch Structure Overview

The Austrian national focus tree comprises **7 primary branches, 14 sub-branches, and 1 joint branch:**

**Ideological/Political Branches:**
- **Repeal the May Constitution** — Unlocks Communist (Austromarxism), Democratic (Republic), and Monarchist (Habsburg) paths; mutually exclusive with Fascist path
- **Totalitarian Safety** — Historical Fascist path, independent of May Constitution

**Shared Sub-branches** (vary by ideology chosen):
- Gain Schutzbund Support (militia recruitment, Communist/Democratic)
- Intervention in Spain (Spanish Civil War support, Communist/Democratic)
- Universität Wien (research bonus, Communist/Democratic)
- The Right to Rearm (Treaty of Saint-Germain removal, Democratic/Danubian)
- Deal with the German Threat (war goals, Communist/Democratic/Danubian)
- The Danubian Federation (political union, leads to joint branch)
- Reinstate the Herrenhaus (Monarchist entry)
- The Legacy of an Empire (Monarchist)
- The War Against Bolshevism (Monarchist/Danubian)
- Demand Hungarian Submission (Monarchist annexation, unlocks joint branch)
- A Royal Alliance/Reclaim Habsburg (Monarchist alliances)
- Reform the Central Powers/etc. (Monarchist/historical late-game)
- Restoring the Right to Our Flag/Purchasing Alaska (Liechtenstein variant)
- Bring Hungary Back Into the Fold (Monarchist annexation chain)

**Functional Military/Industrial Branches** (pursue independently):
- **Regulate the Finance Sector** — Industrial recovery, infrastructure, building slots
- **Österreichische Luftstreitkräfte** — Air force technology, air bases, anti-air, radar
- **Secret Rearmament** — Army bonuses, design companies, land forts
- **Re-Establish the Navy** — Naval industry and technology

**Joint Branch:**
- **Indivisible and Inseparable** — Austro-Hungarian union (any member can complete; originator forms Austria-Hungary flag)

---

## Repeal the May Constitution Branch

Entry point for democratic and communist paths. Mutually exclusive with Totalitarian Safety (fascist path). Repealing ends Austrofascism modifier and opens ideological choice.

### Core Focuses (Repeal the May Constitution)

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Repeal the May Constitution | None | Totalitarian Safety | Political Power +50; Remove Austrofascism dynamic modifier; Heinrich Maier operative gained; Remove Austrofascism opinion modifier (opinion Germany −40) | Entry point for non-fascist paths |
| Legalize Political Opposition | Repeal the May Constitution | — | Political Power +50; Communism +2.50%, Democracy +2.50% popularity; Bruno Kreisky (Meticulous Lawyer) political advisor; Stability +5.00%; Ideology drift defense +10.00%; Daily Democracy Support +0.02, Communism Support +0.01 | Mandatory for further choices |
| Reichsbund der Österreicher | Repeal the May Constitution | — | Stability +10.00%; Fascism −5.00% popularity | Legitimist option (does not lock out other paths) |

### Austromarxism Sub-branch (Communist Path)

Communist ideological path. Early focus enables choice between Austromarxism (middle ground), alignment with Soviet Stalinism, or Trotskyism; civil war mechanics based on communism support levels.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Austromarxism | Legalize Political Opposition OR Reichsbund der Österreicher; >20% KPÖ support if Rally the People | Hold Elections; Reinstate the Herrenhaus | Austromarxism dynamic modifier (Factory output +10.0%, Production efficiency growth +5.0%); Otto Bauer (Father of Austromarxism) advisor; Daily Communism Support +0.03, Democracy Support +0.02; Stability +10.00% | Core communist identity; conditional branching when aligning with Soviets later |
| Rally the People | Austromarxism; >20% KPÖ support | — | Political Power +50; Stability −10.00%; Daily Communism Support +0.02, Democracy Support +0.01; Dynamic modifier changes (Austrostalinism/Austrotrotskyism if those modifiers present) | Prerequisite for escalation to civil war |
| Root out the Nationalists | Rally the People | — | Party reorganization (DNSAP banned, Vaterländische Front rebranded); Fascism −5.00% popularity; War support −5.00% base; bypass if already Communist ruling party; Hidden: complex party popularity and leadership shuffles | Consolidates control; can bypass civil war if >60% communism support |
| Renouncing the Treaty | Rally the People | — | Remove Treaty of Saint-Germain-en-Laye national spirit; Italy, France, UK, USA get diplomatic events (breach notification); bypass if treaty already removed | Rearmament unlock; shared with Democratic paths |
| Emergency Measures | Root out the Nationalists + Renouncing the Treaty | — | National spirit (720 days): Military factory construction +20.00%, Civilian factory construction +20.00%, Railway construction +10.00%, Land fort construction +10.00% | Industrial mobilization phase |
| Reclaiming Red Vienna | Emergency Measures; >30% KPÖ support | — | **Complex civil war outcome:** If >60% communism support at completion, straight KPÖ rule with no civil war. Otherwise, civil war spawning Schutzbund units (Niederösterreich 3×, Democratic side) vs Heimwehr (Oberösterreich 1×, if Militia Support absent); Stability consequences; Hidden: various unit creation and party control shifts | **Major branching point:** success or civil war determines next path viability |
| Seek Soviet Support | Reclaiming Red Vienna; peace+independence with USSR; Soviet exists | Raiding Old Military Stockpiles | Political Power +150; Soviet gets event "Communists in Austria Seek our Support"; If accepted by USSR: Soviet 730-day spirit (Lend-lease tension limit −30.0%, Max volunteer divisions +3, Divisions required for volunteers −100.0%), opinion Austria +15 | Requires Soviet agreement; locks out independent stockpile path |
| Raiding Old Military Stockpiles | Reclaiming Red Vienna | Seek Soviet Support | 1,500 Infantry Equipment + 500 Support Equipment to stockpile; 200 motorized transport (or pre-motorization truck) if researched Motorized Infantry | Independent resource path; mutually exclusive with Soviet support |
| Promoting the Worthy | Seek Soviet Support | — | Eduard Barger: +1 skill, +1 attack, +1 planning, +1 logistics; Emil Liebitzky: +1 skill, +1 defense, +1 planning, +1 logistics; Julius Deutsch: +1 planning, +2 logistics (if Properly Trained Militias done) | General experience and trait gains |
| Politicized General Staff | Seek Soviet Support | — | Conditional modifier (Austrostalinism/Austrotrotskyism/Austromarxism): Theorist cost −10.0%, High Command cost −10.0%, Command power daily gain +15.0%; Random owned state creates Infanterie Division | Military command improvements |
| Align with the Soviets | Promoting the Worthy + Politicized General Staff; peace+independence with USSR; Soviet exists; bypass if USSR doesn't exist | — | **Soviet ideology lock:** If USSR completed The Centre → Austrostalinism modifier (Factory output +10.00%, Ideology drift defense +15.0%). If USSR completed Long Live the Workers' Government → Austrotrotskyism modifier (Subversive activities −25%, War support +5.00%). Leadership changes conditional on faction doctrine; Soviet gets reciprocal event | **Locks communist ideology to Soviet alignment** |
| A New Beginning | Seek Soviet Support OR Raiding Old Military Stockpiles; not in civil war | — | Conditional modifier updates; Daily Communism Support +0.03; Stability +15.0%; Political Power Gain +10.0% | Peace consolidation after civil war or stockpile transition |
| Properly Trained Militias | Raiding Old Military Stockpiles | — | Remove Militia Support spirit if present; if Gain Schutzbund Support done: create Schutzbund Division in Niederösterreich; otherwise Julius Deutsch and Theodor Körner become generals; The People's Army dynamic modifier (Militia Attack/Defense/Speed +30.0%); unit spawning conditional | Militia professionalization |
| The People's Army | Raiding Old Military Stockpiles | — | Conditional The People's Army modifier: Recruitable population +15.0%, Mobilization speed +10.0%; if Gain Schutzbund Support done, Schutzbund divisions spawn in random states | Recruitment boost; synergizes with Schutzbund |
| A Safe Harbor For Dissidents | Properly Trained Militias + The People's Army | — | Conditional modifier updates (Communism +0.02 daily, Production efficiency +5.0%); Olga Taratuta joins from Ukraine; War support +5%, Stability −10%, Recruitable population +10%, Communism daily +0.03 | Political exiles recruitment |
| Re-Establish Rote Hilfe | A Safe Harbor For Dissidents | — | Stability +5.00%; Malke Schorr (The Red Helper) advisor; Weekly Manpower +30, Daily Communism Support +0.03; Egon Schönhof (Communist Lawyer) advisor (Conscription/Trade/Economy law cost −10%); Communism daily +0.03 | Historical organization revival |
| Join the Comintern | Align with Soviets + A New Beginning; independence; not in faction; Soviet faction leader exists; bypass if already in Comintern | Establish the Danubian Bloc | Soviet Union gets event "Austria Seeks to Join the Comintern" | Soviet faction membership path |
| Establish the Danubian Bloc | A New Beginning + A Safe Harbor For Dissidents; independence | Join the Comintern | Create faction named "Danubian Bloc"; enable can-create-factions rule | Alternative to Comintern (own faction path) |
| Centralize the Industrial Sector | Align with Soviets + A New Beginning | — | Conditional modifier: Military factory construction +10.0%, Civilian factory construction +10.0% (applies to Austrostalinism or Austrotrotskyism modifiers) | Centralized Soviet-style economy |
| Cut Ties With the Church | A New Beginning | — | Remove Heinrich Maier (Secretive Priest) advisor; Civilian Intelligence +20%, Operative slots +1, Agency upgrade time −20.0%; Daily Democracy/Communism Support +0.02; Remove Theodor Innitzer (Fascist Cardinal) (Stability −5%, War support +3%, Fascism daily +0.05); Conditional Stability/Research +5.0% | Secularization via Soviet alignment |
| Encourage Communist Sentiments | Centralize the Industrial Sector OR Cut Ties With the Church; bypass if all Danube countries communist or have rejected influence | — | Unlock decisions to Encourage Communist Sentiments in Danubian countries and historically-interested nations | Danubian expansion mechanic |
| Rapid Revolution | Encourage Communist Sentiments; not in faction or meeting conditions | Meticulous Preparations | Political Power +100, Command power +25.0; Conditional Planning Speed +10.0% | Aggressive expansion posture |
| Meticulous Preparations | Encourage Communist Sentiments | Rapid Revolution | Political Power +25; Stability +10.00%, War support +5.00%; Conditional Max planning factor +10.0% | Defensive consolidation posture |
| Demanding the Liberation of Workers | Rapid Revolution OR Meticulous Preparations; bypass if Danube countries already communist or rejected influence | — | Unlock decisions to Demand Liberation of Workers in previously influenced nations | Influence escalation mechanic |
| The Union of Danubian Socialists | Demanding the Liberation of Workers | — | Rename to "The Union of Danubian Socialists"; Conditional War goal justify time −10.0%, Annex cost −10.0% (Austrostalinism/Austrotrotskyism modifiers) | Identity shift and expansion focus |
| The Correct Form of Communism | The Union of Danubian Socialists; not in Soviet faction; not completed Align with Soviets; peace with USSR; USSR independent | Seize the Galician Lands | Gain Annex war goal against Soviet Union | Anti-Soviet communist splinter path |
| Seize the Galician Lands | The Union of Danubian Socialists; independence | The Correct Form of Communism | Core Kraków (88), Stanisławów (89), Lwów (91); Gain Retake core war goals against state owners | Historic Galician reclamation (vs USSR) |

### Gain Schutzbund Support / Intervention in Spain / Universität Wien Branch

Shared sub-branch for Communist and Democratic paths. Militia recruitment, Spanish Civil War intervention, and research/education bonuses.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Gain Schutzbund Support | Rally the People OR Rebuild the Democratic Systems OR A New Constitution; AND (Austromarxism completed OR (Democracy ruling party AND Karl Renner leader)) | — | Create Schutzbund Division division template; Conditional Militia Support spirit (Stability −10%, Militia Attack/Defense +15.00%, Speed +10.00%); Julius Deutsch general (if Properly Trained Militias not done); Unit spawning: if Austromarxism + civil war path, 3× Schutzbund in Niederösterreich, vs 1× Heimwehr in Oberösterreich | Paramilitary formalization |
| Intervention in Spain | Emergency Measures OR Seek Support from the Guarantors; Spanish Civil War started and not ended; Spain exists; Democrat or Communist ruling party | — | Add relation rule override (can send volunteers); If no Volunteer Effort spirit: 720-day spirit (Send volunteers tension limit −50.0%, Max volunteer divisions +3, Divisions required −100.0%) | Limited intervention window (Spanish war ends ~1939) |
| Inviting exiles from Spain | Intervention in Spain; Spanish war ended and fascist won; Spain exists | Celebrating the Victory in Spain | Manpower +5,000; Army experience +10; Spain opinion −50 | Refugee intake (fascist victory scenario) |
| Celebrating the Victory in Spain | Intervention in Spain; sent volunteers; Spanish war ended; Spain exists; Democrat or Communist | Inviting exiles from Spain | Republican Spain OR Spain gets event "Austria Seeks Compensation For Their Help" | Reparations (republican victory scenario) |
| Universität Wien | A New Beginning OR Join the Allies OR The Alpine Federation | — | Gain 1 Research Slot | Education initiative |
| Women's Education Initiative | Universität Wien | — | Women in Academia spirit (Research Speed +10.00%); Marianne Pollak (Socialist Feminist) advisor (Political Power daily +0.05); Weekly Stability +0.50%; Daily Communism Support +0.05; Hedy Lamarr scientist available | Gender equality and scientific progress |
| Scientific Grants | Universität Wien | — | Nuclear Research breakthrough +25.00%; Nuclear Efforts spirit (Nuclear Warfare Special Projects +10%, Nuclear facility construction +10.00%) | Nuclear program initialization |

### Hold Elections Sub-branch (Democratic Path)

Democratic republic path. Mutually exclusive with Austromarxism and Reinstate the Herrenhaus. Establishes democracy, then chooses between major power alliance (Allies) or regional federation (Alpine).

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Hold Elections | Legalize Political Opposition OR Reichsbund der Österreicher; >20% Democracy support OR (Karl Renner leader AND Democracy ruling party) | Austromarxism; Reinstate the Herrenhaus | Political Power +50; Democracy +5.00% popularity; Democratic support +0.04 daily; Stability +10.00%; War support −5% | Democratic formalization |
| Rebuild the Democratic Systems | Hold Elections | — | Political Power +50; Stability +5.00%; Democracy daily +0.03; Ideology drift defense +5.0%; Democratic support +0.03 daily | Democratic consolidation |
| A New Constitution | Rebuild the Democratic Systems | — | Political Power +50; Stability +5.00%; Democracy daily +0.02; War support +5.00%; Democratic support +0.02 daily; By Blood Alone approval (enables later paths) | Constitutional reform |
| Seek Support from the Guarantors | A New Constitution; at peace with guarantee countries (France, UK, USSR); all exist | — | France, UK, USSR get events to guarantee Austria; diplomatic relation improvements | Protective alliance seeking |
| Join the Allies | Seek Support from the Guarantors; France or UK guarantees Austria; independent | The Alpine Federation; The Danubian Federation (Democratic variant) | France or UK gets event "Austria Seeks to Join the Allies"; if accepted: join Allies faction | Faction membership with Western powers |
| The Alpine Federation | Seek Support from the Guarantors; independent; no guarantee from major power | Join the Allies; The Danubian Federation (Democratic) | Create "Alpine Federation" faction; enable can-create-factions rule; Democratic ideological bloc | Regional alliance alternative |
| Support Republican Spain | A New Constitution OR Join the Allies OR The Alpine Federation; Spanish war ongoing; Spain exists; Democrat ruling party (bypasses if already supporting) | — | Add volunteers relation rule override; 720-day Volunteer Effort spirit (tensions −50%, max volunteers +3, divisions −100%); Spain opinion +25 | Spanish civil war intervention (republican side) |
| Offer Military Attache to Spain | Support Republican Spain; at peace with Spain; Spanish war in progress; Spain exists | — | Spain gets event "Austria Offers Military Attache"; Spanish Republican Army experience +10 if accepted | Advisor sharing |
| Continue Our Isolation | A New Constitution | — | Isolation national spirit (500 days): Faction influence on us −50.0%, Fascism/Communism/Democracy support +0.01 daily; stability +5.0% | Isolationist path (third option vs Allies/Alpine) |
| Restore Austrian Puppet | Rebuild the Democratic Systems; Czechoslovakia exists and is independent; at peace with Czechoslovakia | — | Czechoslovakia gets event "Austria Demands our Submission"; if accepts puppet; occupation puppet war goal against Czechoslovakia | Czechoslovak puppet attempt |
| Czechoslovak Alliance | Rebuild the Democratic Systems; Czechoslovakia independent; at peace | — | Czechoslovakia gets event "Austria Seeks Alliance"; if accepts: opinion +50 and mutual guarantee | Defensive pact |
| Yugoslav Alliance | Rebuild the Democratic Systems; Yugoslavia independent; at peace | — | Yugoslavia gets event "Austria Seeks Alliance"; if accepts: opinion +50 and mutual guarantee | Balkan alliance |
| Romanian Alliance | Rebuild the Democratic Systems; Romania independent; at peace | — | Romania gets event "Austria Seeks Alliance"; if accepts: opinion +50 and mutual guarantee | Eastern alliance |

---

## Totalitarian Safety Branch

Historical Fascist path. Austria remains Fascist, opposes German Anschluss through Italian alliance and democratic major backing. Can support Nationalist Spain. Modifies Austrofascism modifier with military bonuses. Mutually exclusive with Repeal the May Constitution.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Totalitarian Safety | None | Repeal the May Constitution | Fascism +10.00% popularity; Stability +10.00%; War support −10%; Against German pressure; entry to fascist path | Maintains Austrofascism |
| Denounce the Red Menace | Totalitarian Safety | — | Communism −2.50% popularity; Fascism +2.50%; Stability +2.50% | Anticommunist messaging |
| Restore Coroneted Stability | Totalitarian Safety; has crowned regent or wants royal prestige | — | Stability +10.00%; War support +5%; Monarchy messaging | Legitimist-fascist hybrid |
| Increase Political Influence | Totalitarian Safety; not in conflict | — | Political Power +100; Stability +5%; Fascism daily +0.01 | Political consolidation |
| Bring Back the Corporations | Totalitarian Safety | — | Corporations national spirit: Fascism daily +0.03; War support +10%; Production efficiency −5% | Corporate state ideology |
| Support the Nationalist Front | Totalitarian Safety; Spanish war ongoing; Spain fascist exists (Nationalist Spain); at peace | — | Nationalist Spain gets event "Austria Supports Nationalist Spain"; volunteers/lend-lease options | Fascist solidarity in Spain |
| Send Volunteers to Spain | Support the Nationalist Front; at peace with Nationalist Spain; Spanish war in progress | — | Volunteer Effort spirit (720 days): volunteers tension −50%, max +3, divisions −100%; Fascism daily +0.02 in Austria | Spanish intervention (fascist side) |
| Negotiate with Italy | Totalitarian Safety; Italy independent; at peace; Italy fascist | — | Italy gets event "Austria Seeks Fascist Alliance"; if accepts: opinion +40, can military access | Axis alignment |
| Italian Guarantee | Negotiate with Italy; Italy guarantees Austria or mutual pact formed | — | Stability +10.00%; Fascism +5.00% popularity; War support +10%; German pressure reduced (diplomatic event) | Italian protective umbrella |
| Austrofascism Revisited | Totalitarian Safety; Austrofascism modifier present | — | Austrofascism modifier strengthened: Stability +20%, War support +10%, Army morale +15%, Fascism daily +0.05 | Strengthen fascist doctrine |
| Reorient the Heimwehr | Totalitarian Safety | — | Heimwehr paramilitaries strengthened; Infantry equipment +500; Fascism +0.02 daily | Paramilitarization |
| Armed Neutrality | Totalitarian Safety; maintains independence/not in major faction | — | National spirit (armed neutrality): War support −5%, Construction speed +10%, Fascism daily +0.01 | Armed neutrality posture |
| Stand Alone | Totalitarian Safety; independence; Fascism popular | — | Stability +10%; War support +10%; Independence guarantee | Isolationist fascism |
| Oppose the Anschluss | Armed Neutrality OR Stand Alone; Italy allied (pact/guarantee); at peace with Italy | — | War goal against Germany (Anschluss prevention); Italy opinion +25 | Resists German annexation |

---

## Regulate the Finance Sector Branch

Industrial recovery and expansion. Addresses Great Depression aftermath, increases resource extraction, factory infrastructure, building slots.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Regulate the Finance Sector | None (independent) | — | Economic adviser gains bonus (Economics speed +5%); Civilian factory construction +10.00%; Production efficiency growth +5.0% | Industrial opening |
| Promote Economic Growth | Regulate the Finance Sector | — | Civilian factories +1 in key economic states; Infrastructure building +20%; Stability +5% | Factory buildout |
| Increase Trade | Regulate the Finance Sector; has tradeable resources | — | Trade value +30%; Commercial agreements available; Resources export income +10% | Export focus |
| Boost Agricultural Output | Regulate the Finance Sector | — | Agricultural resource production +30%; Supply consumption −5% | Farming enhancement |
| Improve Mining Operations | Regulate the Finance Sector | — | Metal and ore extraction +40%; Mining buildings upgraded | Resource extraction |
| Accelerate Construction | Promote Economic Growth OR Improve Mining Operations | — | Construction speed +15%; Building slot recovery in states | Infrastructure buildout |
| Establish Luxury Goods Production | Increase Trade | — | Consumer goods +20%; Stability +5%; Trade income +10% | Trade good production |
| Recover the Economy | Promote Economic Growth + Accelerate Construction | — | Remove any economic penalties; Stability +10%; Fascism/Democracy support +0.01 daily depending on doctrine | Great Depression recovery |
| Encourage Private Investment | Recover the Economy | — | Civilian factory construction +20%; Private economy preferred; Democratic support +0.02 daily | Private sector emphasis |
| Focus on the Public Sector | Recover the Economy | — | Military factory construction +20%; Public sector focus; Communist support +0.02 daily | Public sector emphasis |

---

## Österreichische Luftstreitkräfte Branch

Air force development. Air bases, anti-air, radar, air force technology researched/upgraded. Upgrades Österreichische Luftstreitkräfte modifier.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Österreichische Luftstreitkräfte | None (independent) | — | Air bases +1 in strategic regions; Air force doctrine research bonus +10%; Österreichische Luftstreitkräfte modifier added (Air force attack +5%) | Air force establishment |
| Expand Air Bases | Österreichische Luftstreitkräfte | — | Air base construction +30%; Infrastructure for air operations +20% | Airfield network |
| Fighter Development | Österreichische Luftstreitkräfte | — | Fighter aircraft research speed +15%; Fighter equipment production +10% | Fighter focus |
| Anti-Air Capabilities | Österreichische Luftstreitkräfte | — | Anti-air construction +25%; Anti-air defense +20%; Radar station construction +15% | Air defense |
| Radar Network | Anti-Air Capabilities | — | Radar stations +2 in strategic states; Detection range +50%; Air interception +15% | Early warning system |
| Reconnaissance Aircraft | Österreichische Luftstreitkräfte | — | Reconnaissance aircraft production +15%; Air superiority +10%; Intelligence gathering +10% | Reconnaissance capability |
| Strengthen Luftstreitkräfte | Expand Air Bases + Anti-Air Capabilities; Österreichische Luftstreitkräfte modifier present | — | Modifier strengthened: Air force attack/defense +10%, Air base capacity +30%, Construction speed +10% | Air force modernization |
| Bomber Development | Österreichische Luftstreitkräfte | — | Tactical bomber research +20%; Strategic bomber research +10%; Bombing efficiency +15% | Bombing capability |
| Upgrade Aircraft Production | Fighter Development OR Bomber Development | — | Aircraft factory production +20%; Equipment efficiency +10% | Production scaling |
| Close Air Support Doctrine | Anti-Air Capabilities; Army focuses in progress | — | CAS research speed +15%; Land warfare integration +10%; Support for army operations | Ground-air coordination |

---

## Secret Rearmament Branch

Army buildup and modernization. Army bonuses, design companies, land forts, division equipment. Upgrades Österreichisches Bundesheer modifier and equivalents.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Secret Rearmament | None (independent) | — | Army experience +25; Land doctrine research +10%; Österreichisches Bundesheer modifier added (Infantry attack +5%, Army morale +5%) | Military buildup start |
| Infantry Expansion | Secret Rearmament | — | Infantry equipment production +20%; Infantry divisions training −15%; Conscription recruitment +10% | Troop expansion |
| Equipment Development | Secret Rearmament | — | Infantry weapons research speed +15%; Support equipment +10%; Army equipment production +20% | Weapons modernization |
| Fortification Program | Secret Rearmament | — | Land fort construction +25%; Infrastructure fortification +15%; Defense bonus +10% | Defensive line building |
| Tank Development | Secret Rearmament | — | Tank research speed +20%; Tank equipment production +15%; Armored warfare doctrine +10% | Armor focus |
| Artillery Advancement | Secret Rearmament | — | Artillery research speed +15%; Artillery equipment production +15%; Field artillery doctrine +10% | Artillery modernization |
| Motorized Logistics | Equipment Development | — | Motor transport production +20%; Supply consumption −10%; Motorized units speed +15% | Logistics modernization |
| Design Company Establishment | Equipment Development OR Artillery Advancement | — | Gain design companies for tank/artillery/infantry weapons; Design company production bonuses | Industrial design capability |
| Strengthen Bundesheer | Infantry Expansion + Fortification Program; Österreichisches Bundesheer modifier present | — | Modifier strengthened: Infantry attack/defense +10%, Discipline +5%, Morale recovery +10% | Army professionalization |
| Mechanized Warfare | Tank Development + Motorized Logistics | — | Mechanized division doctrine +15%; Mechanized warfare research +20%; Armor-infantry coordination +15% | Blitzkrieg-style tactics |
| Elite Officer Corps | Secret Rearmament + 3+ army focuses | — | Army experience +50; Officer skill bonuses +1 across multiple generals; Command power gain +10% | Military excellence |
| Expand Our Military | Strengthen Bundesheer; sufficient manpower and resources | — | Conscription laws cost −20%; Recruitment speed +30%; Military factory output +10% | Mass mobilization |

---

## Re-Establish the Navy Branch

Naval industry and technology. Naval bases, dockyards, naval research. Upgrades Österreichische Kriegsmarine modifier and equivalents.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Re-Establish the Navy | None (independent) | — | Naval base construction +30%; Dockyard output +10%; Naval technology research +10%; Österreichische Kriegsmarine modifier added (Naval attack +5%) | Navy rebuilding |
| Expand Naval Infrastructure | Re-Establish the Navy; has coastal states | — | Dockyard construction +20%; Naval base expansion +25%; Port capacity +15% | Shipbuilding capacity |
| Submarine Development | Re-Establish the Navy | — | Submarine research speed +20%; Submarine production +15%; Naval doctrine research (Submarine focus) +10% | Submarine emphasis |
| Surface Fleet | Re-Establish the Navy | — | Heavy cruiser/battleship research speed +15%; Surface combat doctrine +10%; Naval combat strength +15% | Surface fleet emphasis |
| Naval Aviation Integration | Re-Establish the Navy; Air force branch in progress | — | Naval bomber research speed +15%; Carrier aircraft production +10%; Naval-air coordination +10% | Naval air power |
| Mine Warfare | Re-Establish the Navy | — | Mine production +40%; Anti-submarine warfare +15%; Mine-laying effectiveness +20% | Mine capability |
| Strengthen Kriegsmarine | Expand Naval Infrastructure + Submarine Development OR Surface Fleet; Österreichische Kriegsmarine modifier present | — | Modifier strengthened: Naval attack/defense +10%, Ship maintenance cost −10%, Dockyard efficiency +20% | Naval modernization |
| Fleet Modernization | Surface Fleet OR Submarine Development; sufficient resources | — | Fleet composition updated; Ship upgrade speed +20%; Obsolete ship replacement +30% | Fleet renewal |
| Naval Doctrine Refinement | Naval Aviation Integration OR Mine Warfare | — | Naval doctrine research +20%; Torpedo effectiveness +15%; Naval engagement tactics +15% | Doctrine advancement |
| Expand Naval Operations | Strengthen Kriegsmarine; has docking facilities | — | Fleet size cap +30%; Naval force projection range +50%; Naval supply consumption −10% | Operational reach |

---

## Indivisible and Inseparable (Austro-Hungarian Joint Branch)

Joint branch available to any Austro-Hungarian nation (Austria, Hungary, as subjects) after completing The Danubian Federation OR Demand Hungarian Submission. Grants military and industrial bonuses to all Austro-Hungarian faction members. Originator can form Austria-Hungary flag.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Austro-Hungarian Alliance | The Danubian Federation (Austria) OR Demand Hungarian Submission (Austria); OR Hungary in Austro-Hungarian federation; at peace | — | Hungary opinion +50 (if not puppet); Austro-Hungarian members gain shared bonuses; Daily Communism/Democracy/Fascism/Monarchy support +0.01 (all members) | Confederation establishment |
| Coordinate Economic Policies | Austro-Hungarian Alliance; Austro-Hungarian members in faction | — | All members: Military factory construction +10%, Civilian factory construction +10%; Trade within faction −25% tariff; Industry efficiency +15% across confederation | Economic integration |
| Unified Military Command | Austro-Hungarian Alliance | — | All members: Army attack +10%, Army defense +10%, Division training −10%; Shared command bonuses; Officers from Austria can advise subject nations | Military coordination |
| Shared Intelligence Network | Austro-Hungarian Alliance | — | All members: Civilian intelligence +20%, Operative slots +1, Agency upgrade time −15%; Shared intelligence data between members | Intelligence cooperation |
| Form Austria-Hungary | Austro-Hungarian Alliance; all historically Austro-Hungarian territories under full Austrian control or Austro-Hungarian faction control; originating nation has 80%+ of Austro-Hungarian cores | — | Austria renamed to "Austria-Hungary"; flag changed; Historical prestige +50; War support +15%; Stability +20% | Formation of historical empire flag |
| Restore the Throne | Form Austria-Hungary; not Soviet; sufficient stability; monarchy path taken | — | Restore Kaiser title if Habsburg line; Otto von Habsburg (or successor) reinstated as figurehead; National spirit (Restored Monarchy): Stability +10%, War support +10%, Democracy/Communism support −0.01 daily | Monarchist restoration (AH variant) |
| Common Defense Pact | Austro-Hungarian Alliance; at peace with all members | — | All members: Defensive pact mutual guarantee; War support −5% (peace modifier); Opinion each other +50; Faction cohesion +20% | Defense guarantees |
| Expand Austro-Hungarian Sphere | Form Austria-Hungary; sufficient military | — | Unlock decisions to bring Balkans/Danubian nations into Austro-Hungarian sphere (puppet or annexation paths); diplomatic leverage +50% vs smaller nations | Imperial expansion |
| Austro-Hungarian Economic Bloc | Coordinate Economic Policies + Common Defense Pact | — | All members: Trade efficiency +20%, Resource sharing within bloc +50%, Consumer goods satisfaction +10%; Economic autonomy bonus from bloc membership | Trade bloc formation |

---

## Democratic Monarchy Variant & Liechtenstein Path

*[Democratic Monarchy sub-paths enable Austria to restore constitutional monarchy (separate from communist/fascist paths) if path conditions met.]*

**Liechtenstein Variant Path:** Unlocked when Otto von Habsburg becomes general (via event after *Inviting the Royals of Liechtenstein* if Alois of Liechtenstein leads Austria). Austria replaced by Liechtenstein flag. Can pursue:
- **Restoring the Right to Our Flag** — War goal against Haiti (463 state) for historical flag
- **Purchasing Alaska** — Purchase Alaska (state 463) from another nation

---

## Other Democratic Path Branches

**Hold Elections sub-paths** continue with military/industrial development (Secret Rearmament, Österreichische Luftstreitkräfte, Re-Establish Navy, Regulate Finance) and can merge into shared branches (Deal with the German Threat, Right to Rearm, Spanish intervention).

**Danubian Federation Democratic variant** allows Austria to form multi-nation faction (non-Soviet, non-Axis) attracting Balkans; opens Austro-Hungarian joint branch if Hungary joins or is conquered.

**Deal with the German Threat** (shared Communist/Democratic/Danubian): War goal generation vs Germany and Fascist nations; timing and scope depend on path (communist vs democratic alliance priorities differ).

---

## Notes

- This file documents the Götterdämmerung DLC national focus tree (patch 1.19). Without the DLC, Austria uses the generic tree.
- Many focuses have conditional effects (different outcomes if particular modifiers, rulers, or prior focus chains active). The table condensations indicate key branches but cannot exhaust all permutations.
- Civil war mechanics for communist path depend on communism support % at focus completion (>60% prevents war).
- Multiple paths have cosmetic name changes (e.g., Austromarxism → Austrostalinism or Austrotrotskyism) based on Soviet alignment; mechanical effects remain in modifier descriptions.
- Austro-Hungarian joint branch allows any Austro-Hungarian nation (Austria or Hungary) to complete focuses, but originator (Austria) alone can form Austria-Hungary flag.

