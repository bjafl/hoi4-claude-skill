---
title: French National Focus Trees
category: focus-trees
tags: [france, focus tree, free france, vichy france, political power, national spirit]
game_version: "1.19"
dlc: ["La Résistance"]
sources:
  - https://hoi4.paradoxwikis.com/French_national_focus_tree
  - https://hoi4.paradoxwikis.com/Free_French_national_focus_tree
  - https://hoi4.paradoxwikis.com/Vichy_French_national_focus_tree
---

## Summary

France as a major power gets a unique 5-branch national focus tree with 7 political sub-branches, organized around economic development (Devalue the Franc), military rearmament (defensive vs. offensive paths), political ideology (left/right, communist/fascist/monarchist/democratic), and naval/air expansion. With *La Résistance* DLC enabled, France fractionalizes: Free France (government-in-exile) and Vichy France (collaborationist state) each get their own trees upon capitulation. See [France](../05-countries/france.md) for the country's 1936 starting profile, and [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses.

## Metropolitan France (Base Game Tree)

France's main focus tree divides into five major branches: industrial development (Devalue the Franc), military rearmament (Begin Rearmament with defensive/offensive paths), political choice (Form the Popular Front vs. Revive the National Bloc), naval rearmament, and air focus. Two of these lead to political sub-branches (communist, fascist, monarchist, democratic).

### Devalue the Franc Branch (Industrial)

Economic and colonial development branch offering research slots and factory bonuses.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Devalue the Franc** | None | — | National spirit (365 days): Consumer Goods Factories −5%, Stability −5.00% |
| **Develop the Metropole** | Devalue the Franc | — | Stability +5.00% |
| **Autoroutes** | Devalue the Franc | — | 4 random cored states with <4 infrastructure: +1 infrastructure each |
| **Develop the Colonies** | Devalue the Franc | — | All non-core owned states (not in Europe) with resistance: Compliance +10.0% |
| **Invest in Metropolitan France** | Develop the Metropole | — | 2 random cored neighboring states: +2 building slots and set state flags for industrial expansion |
| **Invest in Algerian France** | Develop the Metropole OR Develop the Colonies | — | Algerian states (Algiers, Constantine, Tlemcen): +2 building slots, set industrial expansion flags |
| **Invest In West Africa** | Develop the Colonies | — | West African colonies: +2 building slots, set colonial industry flags |
| **Invest In Indochina** | Develop the Colonies | — | Indochinese states: +2 building slots, set colonial industry flags; −150 autonomy for any subject Vietnam/Cambodia/Laos |
| **Invest In Syria** | Develop the Colonies | — | Syrian/Lebanese states: +2 building slots, set colonial industry flags; −150 autonomy for any subject Syria/Lebanon |
| **Industrial Expansion** | Invest in Metropolitan France OR Invest in Algerian France | — | +2 civilian factories to all invested metropolitan states |
| **Colonial Industry** | Invest in Algerian France OR Invest In West Africa OR Invest In Indochina OR Invest In Syria | — | +2 civilian factories to all invested colonial states |
| **Support the Grandes Écoles** | Industrial Expansion | Requires <5 research slots | +1 research slot |
| **Military Factories** | Industrial Expansion OR Colonial Industry | — | +2 building slots and +2 military factories to all invested states |
| **Form the National Research Center** | Colonial Industry | Requires <5 research slots | +1 research slot |
| **Global Integration** | Colonial Industry | — | National spirit: Global Investments; Resource Gain Efficiency +10.00% |

### Begin Rearmament Branch (Military)

Army-focused branch with two mutually exclusive paths: defensive (fortifications, defensive doctrine) or offensive (mobile warfare, mechanization). Both paths converge at Army Reform, which removes the starting debuff **Victors of the Great War**.

#### Defensive Path

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Begin Rearmament** | >12% war support | — | 2 random cored states: +2 building slots and +2 military factories each |
| **Defensive Focus** | Begin Rearmament | Aggressive Focus | Command power +30; Maxime Weygand available as Chief of Army (Division Defense +10.0%) |
| **Firepower Kills** | Defensive Focus | Methodical Battle | National spirit: Towed Artillery Production cost −10.00% |
| **Levée en masse** | Firepower Kills | — | Army experience +5; National spirit: Infantry Equipment Production cost −10.00% |
| **Grande Batterie** | Levée en masse | — | Army experience +5; 1× 100% research bonus for Support Artillery |
| **Char de Bataille** | Grande Batterie | — | Army experience +5; 1× 100% research bonus for Heavy Tank models |
| **Division Cuirassée** | Char de Bataille; has researched Renault B1 or basic heavy/medium tank chassis | — | Create 2 French Division Cuirassée units in capital |
| **Methodical Battle** | Defensive Focus | Firepower Kills | 2× 65% cost reduction for Land Doctrine |
| **Fortification Focus** | Methodical Battle | — | National spirit: Land fort construction speed +10.00%, Coastal fort construction speed +10.00% |
| **Alpine Forts** | Fortification Focus; Savoy controlled | — | Event: Extension of the Alpine Line; Italy gains Alpine Forts modifier (−50 opinion) |
| **Extend the Maginot Line** | Alpine Forts; Champagne, Nord-Pas-de-Calais, Picardy controlled; has **Protected by the Maginot Line** | — | Event: Extension of the Maginot Line; Belgium gains Extend the Maginot Line modifier (−50 opinion); Germany gains +25 opinion bonus |

#### Offensive Path

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Aggressive Focus** | Begin Rearmament | Defensive Focus | Army experience +25; Maurice Gamelin available as Chief of Army (Division Attack +10.0%) |
| **Battle of Maneuver** | Aggressive Focus | Air Dominance | Charles de Gaulle available as theorist (Land Doctrine research speed +10%, Armor max speed +10%, Army experience gain +0.05/day) |
| **Motorized Focus** | Battle of Maneuver | — | Army experience +5; National spirit: Motorized Production cost −10.00% |
| **Mechanized Focus** | Motorized Focus | — | Army experience +5; 1× 100% research bonus for Mechanized models |
| **Automitrailleuses** | Mechanized Focus | — | Army experience +5; 1× 100% research bonus for Light Tank and Medium Tank models |
| **Air Dominance** | Aggressive Focus | Battle of Maneuver | National spirit: Fighter Production cost −10.00%, Close Air Support Production cost −10.00% |
| **CAS Focus** | Air Dominance | — | 2× 100% research bonus for Close Air Support models |
| **Air-Ground Cooperation** | CAS Focus | — | 2× 50% cost reduction for Air Doctrine |
| **Flying Artillery** | Air-Ground Cooperation | — | National spirit: Tactical Bomber Ground Attack +15%, Close Air Support Ground Attack +15% |

#### Both Paths Converge

| Focus | Prerequisites | Effects |
|---|---|---|
| **Infantry Tanks** | Defensive Focus OR Aggressive Focus | If *Arms Against Tyranny* enabled: Renault funds +2000; otherwise Hotchkiss available as infantry tank designer (Armor research speed +15%, soft attack +5%, armor +5%) |
| **Special Forces** | Infantry Tanks | National spirit: Special Forces Capacity Multiplier +2.0%; +1 free Special Forces branch specialism |
| **Fusiliers Marins** | Special Forces | 2× 50% research bonus for Transport and Marine technology; if *Arms Against Tyranny* enabled: 2× cost reduction for Special Forces Doctrine |
| **Army Reform** | One of: Char de Bataille, Extend the Maginot Line, Automitrailleuses, Flying Artillery; does NOT have **Disjointed Government** | Lose **Victors of the Great War**; Army experience +10; 2× 50% cost reduction for Land Doctrine; if *Arms Against Tyranny* enabled: Renault funds +2000, otherwise AMX available as mobile tank designer (Armor research speed +15%, max speed +5%, reliability +5%) |

### Form the Popular Front / Revive the National Bloc Branch (Political & Industrial)

Core political split. Choosing **Form the Popular Front** (left path, leads to communist sub-branches) is mutually exclusive with **Revive the National Bloc** (right path, leads to fascist/monarchist branches). Both converge on the democratic branch with Spanish intervention decisions and industrial reforms.

#### Form the Popular Front (Left Path)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Form the Popular Front** | None | Revive the National Bloc | Léon Blum becomes Democratic party leader (Reluctant Interventionist); Stability +5.00%; Lend-lease tension limit −20.0%; AI focuses on defense (+50.0%) |
| **Reform the Labour Laws** | Form the Popular Front | — | National spirit: Matignon Agreements; Consumer Goods Factories +5%, Stability +10.00%; Factory output −10.00%, Dockyard output −10.00%; lose **Factory Strikes** |
| **Nationalize Key Industries** | Reform the Labour Laws | — | Modifies **Inefficient Economy**: Factory output +10.00%, Dockyard output +10.00% (bypassed if already removed) |
| **Reorganize the Aviation Industry** | Nationalize Key Industries | — | Random owned cored state: +2 building slots and +2 military factories; unlocks 5 decisions for aviation industry reorganization (north/west/center/southeast/southwest) |
| **Form the State Arsenals** | Nationalize Key Industries | — | 2 random owned cored states: +2 building slots and +2 military factories each; if *Arms Against Tyranny*: AMX available with +1 size |
| **General Work Council** | Reorganize the Aviation Industry AND Form the State Arsenals | — | Lose **Inefficient Economy** (bypassed if already removed) |
| **Dirigisme** | General Work Council | — | National spirit: Civilian-to-military factory conversion cost −50.00%, Economy Laws cost −50.00% |
| **National Champions** | General Work Council | — | 4 random owned cored states (2× military, 2× civilian): +2 building slots and factories each |
| **Ban the Leagues** | Form the Popular Front; has **Political Violence** | — | Lose **Political Violence**; Stability +(Democracy support % × −0.5) |

#### Revive the National Bloc (Right Path)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Revive the National Bloc** | None | Form the Popular Front | Current leader gains: Tenacious Negotiator; Political Power gain +10%; Trade deal opinion factor +25.00% |
| **Ban Communism** | Revive the National Bloc; has **Political Violence**; not communist | — | National spirit: Communism Banned; Communism support −0.25 daily; Stability +(Communism popularity % × −0.25); lose **Political Violence** |
| **Laissez-Faire** | Revive the National Bloc | Agricultural Protectionism | 3× 150% research bonus for Industry |
| **Agricultural Protectionism** | Revive the National Bloc | Laissez-Faire | National spirit: Civilian factory construction speed +7.50% |
| **Protect the Rights of Man** | Laissez-Faire OR Agricultural Protectionism | — | Stability +5.00% |
| **Freedom Front** | Protect the Rights of Man | — | If **Utilize the Leagues** not complete: Democracy popularity decreases by Fascism popularity, Fascism popularity decreases conversely; otherwise Fascism popularity increases by Democracy × 0.3, Democracy popularity decreases. If has **Political Violence**: gets event "Protests descend into violence" |
| **Economic Devolution** | Laissez-Faire OR Agricultural Protectionism | — | Modifies **Inefficient Economy**: Factory output +10.00%, Dockyard output +10.00% (bypassed if already removed) |
| **Promote Entrepreneurship** | Economic Devolution | — | National spirit: Entrepreneurship; Military factory construction speed +5.00%, Naval dockyard construction speed +5.00% |
| **Stimulate the Dynamic Market** | Freedom Front OR Promote Entrepreneurship | — | National spirit: Market Dynamism; Industrial research speed +5%, Production efficiency cap +10.00%, Production efficiency growth +10.00% |

#### Shared Focuses (Both Paths)

| Focus | Prerequisites (from either path) | Effects |
|---|---|---|
| **Intervention in Spain** | Form the Popular Front OR Revive the National Bloc; Spanish Civil War ongoing; not yet ended; is fully independent | Unlocks "Intervention in the Spanish Civil War" decisions |

### Invite Communist Ministers Sub-Branch

Only available if **Form the Popular Front** chosen and Spain intervention not completed; leads to communist rule or revolutionary path.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Invite Communist Ministers** | Form the Popular Front; not completed Review Foreign Policy; fully independent | — | If has **Political Violence**: gets event "Protests descend into violence"; Communism +5.00% popularity; Stability +(Communism popularity × 0.25); (bypassed if already communist) |
| **Strengthen the Unions** | Invite Communist Ministers; fully independent | — | Communism +5.00% popularity; if **Political Violence** active: gets event "Protests descend into violence" (bypassed if already communist) |
| **Women's Suffrage** | Invite Communist Ministers; fully independent | — | National spirit: Women's Suffrage; Political Power gain +0.25 daily; Communism +5.00% popularity |
| **Celebrate the Commune** | Strengthen the Unions; fully independent | — | Communism +5.00% popularity (bypassed if already communist) |
| **Industrial Collectivization** | Strengthen the Unions AND Women's Suffrage | — | 1 random owned cored controlled state: +2 building slots and +2 civilian factories (bypassed if owns any non-core states in Europe or cannot build civilians) |
| **Agricultural Collectivization** | Industrial Collectivization | — | National spirit: Recruitable Population +15%; Stability −5.00% if >40% Neutrality + Fascism support |
| **Legal Equality** | Women's Suffrage; fully independent | — | If has **Political Violence**: gets event "Protests descend into violence"; Communism +5.00% popularity |
| **Force the Issue** | Celebrate the Commune OR Legal Equality; fully independent; >45% communist support | — | Stability +(Democracy popularity × −0.25); Communist Parti Communiste Française becomes ruling party; lose **Disjointed Government** (bypassed if already communist) |
| **Reconciliation** | Force the Issue | Revolution To the Utmost | Stability +10.00% |
| **Constitutional Convention** | Reconciliation | — | Political Power +120 |
| **Anti-Fascist Coalition** | Constitutional Convention; not in faction | Loyalty To Moscow, Loyalty To the Cause (both alternatives) | René Nicod becomes communist leader; Manpower +5%, War support +5.00%; communist party renamed Union populaire français; creates or joins anti-fascist faction depending on faction leaders and neighbor alignment |
| **Revolution To the Utmost** | Force the Issue | Reconciliation | (Not detailed in wiki excerpt) |
| **Loyalty To Moscow** | (Alternative paths) | Anti-Fascist Coalition, Loyalty To the Cause | (Not detailed in wiki excerpt) |
| **Loyalty To the Cause** | (Alternative paths) | Anti-Fascist Coalition, Loyalty To Moscow | (Not detailed in wiki excerpt) |

> ⚠️ Revolution To the Utmost, Loyalty To Moscow, and Loyalty To the Cause branches truncated in source; full effects not available on this extract.

### Leftist Rhetoric Sub-Branch

Only available if *La Résistance* DLC **not** enabled; allows transition to communism without the detailed sub-branches.

(Placeholder: specific focus structure not provided in fetched data; this branch is superseded if La Résistance is active.)

### The Blum-Viollette Proposal Sub-Branch

Colonial and ethnic policy branch; allows France to core Algeria, manipulate colonial compliance/resistance, or lose industry bonuses.

(Specific focuses: not fully detailed in extracted section; structure available on wiki.)

### Review Foreign Policy Sub-Branch

Diplomatic branch allowing alliance choices: Little Entente, support Finland, join Allies, or form Stresa Front.

(Specific focuses: not fully detailed; options include diplomatic faction alignment.)

### Utilize the Leagues Sub-Branch

Fascist path branch (available via **Revive the National Bloc**); allows France to become fascist with claims, alliances (Latin Entente), and German alignment options.

(Specific focuses: not fully detailed; leads to Axis and colonial expansion focuses.)

### The Council of Rambouillet Sub-Branch (Requires La Résistance)

Monarchist restoration branch; restores the French monarchy from three houses: Orléanist, Légitimist, or Bonapartist, each with distinct wargoals and diplomatic options.

(Specific focuses: three parallel sub-sub-branches for each house; not fully detailed in extract.)

### Right Wing Rhetoric Sub-Branch

Only available if *La Résistance* DLC **not** enabled; allows transition to fascism without the detailed sub-branches.

(Placeholder: specific focus structure not provided in fetched data; this branch is superseded if La Résistance is active.)

### Naval Rearmament Branch

Grants navy experience and naval research bonuses.

(Specific focuses: not detailed in extracted section.)

### Air Focus Branch

Grants air experience and air research bonuses.

(Specific focuses: not detailed in extracted section.)

### Establish the ABDACOM Branch

(Not documented in extracted section.)

---

## Free France (Government-in-Exile, Requires La Résistance)

Free France's focus tree activates after France capitulates but before Free France leader (typically Charles de Gaulle) is removed. The tree focuses on cultivating resistance in occupied France, recruiting colonial territories, and eventually restoring the French state. Two main branches.

### Refus Absurde Branch (Resistance Cultivation)

Develops resistance networks in occupied territories and reduces enemy compliance gains.

| Focus | Prerequisites | Requirements/Bypass | Effects |
|---|---|---|---|
| **Refus Absurde** | — | Requires (if Man the Guns enabled): >40% legitimacy; OR (without MTG): >14 factories; at peace. Bypassed if already lacks **Defeatism** | Lose national spirit **Defeatism** |
| **The Maquis** | Refus Absurde | — | National spirit: Maquis; Resistance Growth Speed +10% in enemy-occupied core states; occupied core states with <3 infrastructure: Resistance Target +10.0% |
| **Reach Out To Trade Unions** | Refus Absurde | — | National spirit: Connections To Trade Unions; Resistance Growth Speed +10% in enemy-occupied core states |
| **Cooperation With the Communists** | Reach Out To Trade Unions | — | National spirit: Communist Cooperation; Resistance Growth Speed +10% in enemy-occupied core states; if Parti Communiste Français support <14%: Communism +5.00% popularity |
| **Connections To Industrialists** | Refus Absurde | — | National spirit: Industrialist Connections; Compliance Growth Speed −15% in enemy-occupied core states |
| **The Civil And Military Organization** | Connections To Industrialists | — | Replace national spirit: Industrialist Connections → Civil And Military Organization; Resistance Growth +5%, Compliance Growth −15% in enemy-occupied core states |
| **National Council of the Resistance** | Cooperation With the Communists AND The Civil And Military Organization AND Form the National Committee | — | Replace national spirit: Civil And Military Organization → National Council of the Resistance; Resistance Growth Speed +10%, Compliance Growth Speed −25% in enemy-occupied core states |
| **National Uprising** | National Council of the Resistance | — | National spirit (90 days): National Uprising; Equipment Capture Ratio Gain +35.0%, Supply Grace +336.0 hours |
| **French Forces of the Interior** | National Council of the Resistance | — | Creates weak infantry units in every liberated core state |

### Appeal To the French Nation Branch (Restoration & Colonial Recruitment)

Restores Free France's legitimacy, recruits overseas colonial territories, and sets groundwork for retaking France.

| Focus | Prerequisites | Requirements | Effects |
|---|---|---|---|
| **Appeal To the French Nation** | — | Charles de Gaulle is current leader | Manpower +10000; Legitimacy +15; Infantry Equipment +5000 units; (if MTG not enabled: additional Manpower +10000 and Infantry +5000) |
| **Appeal To Overseas Territories** | Appeal To the French Nation | — | Colonial territories have chance to switch to Free France side; +2 offmap civilian factories |
| **Intervention In North Africa** | Appeal To Overseas Territories | All North African states (Casablanca, Marrakech, Algiers, Tlemcen, Constantine, Tunisia, Gabès) not controlled by Free France; controller not in faction with and not subject to Free France | Unlocks decision: Prepare Coup in North Africa; Unlocks decision: Promise Independence to North Africa |
| **Intervention In West Africa** | Appeal To Overseas Territories | All West African states not controlled by Free France; controller not in faction/subject to Free France | Unlocks decision: Prepare Coup in West Africa; Unlocks decision: Promise Independence to West Africa; Unlocks decision: Invasion in West Africa |
| **Intervention In Syria** | Appeal To Overseas Territories | All Syrian states (Deir-az-Zur, Aleppo, Damascus, Lebanon) not controlled by Free France; controller not in faction/subject to Free France | Unlocks decision: Prepare Coup in Syria; Unlocks decision: Promise Independence to Syria; Unlocks decision: Invasion in Syria |
| **Intervention In Indochina** | Appeal To Overseas Territories | All Indochinese states (Tonkin, Laos, South Annam, Cambodia) not controlled by Free France; controller not in faction/subject to Free France | Unlocks decision: Prepare Coup in Indochina; Unlocks decision: Promise Independence to Indochina; Unlocks decision: Invasion in Indochina |
| **Intervention In Central Africa** | Appeal To Overseas Territories | All Central African states (Chad, Equatorial Africa, Cameroon, Middle Congo, Gabon) not controlled by Free France; controller not in faction/subject to Free France | Unlocks decision: Prepare Coup in Central Africa; Unlocks decision: Promise Independence to Central Africa; Unlocks decision: Invasion in Central Africa |
| **Intervention In Madagascar** | Appeal To Overseas Territories | Madagascar not controlled by Free France; controller in faction with OR (not subject to Free France) | Unlocks decision: Prepare Coup in Madagascar; Unlocks decision: Promise Independence to Madagascar |
| **Form the National Committee** | Any of: Intervention In North/West/Central Africa, Intervention In Syria, Intervention In Indochina, Intervention In Madagascar; >90 Legitimacy; (if MTG not enabled: >24 factories) | — | War support +10.00%; Stability +10.00% |
| **Form the Provisional Government** | Form the National Committee | Controls Île de France (16) | If has **Defeatism**: lose it; Change focus tree to French Focus Tree (returns to metropolitan tree) |
| **Continue the Fight** | Appeal To the French Nation | — | +2 offmap military factories; Marie-Pierre Koenig becomes general; Georges Catroux becomes general |
| **The Free French Navy** | Continue the Fight | — | +50 convoy units; Émile Muselier becomes naval commander |
| **Colonial Recruitment** | Continue the Fight | Any owned state: Controlled by Free France, not a core of Free France | National spirit: Colonial Recruitment; Non-core Manpower +5.00% |
| **The Regiment Normandie** | Continue the Fight | Any enemy country at war with Soviet Union; Free France at peace with Soviet Union | Air Experience +25; Soviet Union receives 100 units of French light airframe planes |

---

## Vichy France (Collaborationist Puppet, Requires La Résistance)

Vichy France's focus tree activates after France capitulates and transitions to the Vichy regime. The tree focuses on implementing Pétain's National Revolution, rebuilding military capacity (partly through German technology exchange), suppressing resistance, and eventually either breaking from German occupation or solidifying collaboration.

### Emergency Powers To Pétain Branch

All of Vichy's focuses fall within this single branch, reflecting the subordinate status of the state and the centrality of Pétain's regime. Focuses split into multiple parallel paths: cultural/economic policy (National Revolution, economic planning, labor reforms), military readiness (rebuild army, modernize air force, learn from Germany), and resistance suppression (Legionary Service, Milice).

| Focus | Prerequisites | Requirements | Effects |
|---|---|---|---|
| **Emergency Powers To Pétain** | — | Philippe Pétain is current leader | Philippe Pétain gains: Emergency Powers (Daily Political Power Gain +0.50); lose national spirit **Disjointed Government** (if still in effect) |
| **The National Revolution** | Emergency Powers To Pétain | — | Stability +10.00% |
| **Long-Term Economic Planning** | The National Revolution | — | 2× 100% research bonus for Industry |
| **Aid Small Businesses** | Long-Term Economic Planning | — | Random core state with build capacity: +2 building slots and +2 civilian factories |
| **Venerate the Craftsman** | Aid Small Businesses | — | National spirit: Venerate the Craftsman; Production efficiency cap +10.00% |
| **Down With Marianne** | The National Revolution | — | National spirit (730 days): Down With Marianne; Democratic support −0.10 daily |
| **Up With Jeanne d'Arc** | Down With Marianne | — | National spirit (730 days): Up with Jeanne d'Arc; Fascism support +0.075 daily, Unaligned support +0.025 daily |
| **Celebrate Motherhood** | Up With Jeanne d'Arc | — | Stability +5.00% |
| **Prosecute the Losers** | The National Revolution | — | War support +5.00% |
| **Concessions to the Germans** | Prosecute the Losers | Île de France (16) controlled by German Reich | Unlocks "Concessions to the Germans" decisions; reduces **Occupation Costs** impact via 3 decisions (each costs 25 PP): Military access to Germany, Subsidise Germany's aircraft production (at Vichy's aircraft cost), Send guest workers (boost Germany's production efficiency growth) |
| **Mandatory Work Service** | Concessions to the Germans | — | Modifies **Occupation Costs**: Consumer Goods Factories −5%; National spirit: Mandatory Work Service; Stability −10.00% |
| **A Nation Reborn** | Venerate the Craftsman AND Celebrate Motherhood AND Mandatory Work Service | — | Stability +10.00% |
| **End the Occupation** | A Nation Reborn | Does NOT control Île de France (16) | Set rule: Can Create Factions; Lose **Occupation Costs**; Lose all penalties to aircraft cost if previously subsidised Germany; Germany receives event "An end to the Occupation" |
| **The National Bureau of Statistics** | Emergency Powers To Pétain | — | National spirit: National Bureau of Statistics; Research Speed +10.00% |
| **The Legionary Service Order** | Emergency Powers To Pétain | — | National spirit: Legionary Service Order; Resistance Growth Speed −10% |
| **Form the Milice** | The Legionary Service Order | — | Replace national spirit: Legionary Service Order → Milice; Resistance Growth Speed −20% |
| **Anti-Bolshevist Volunteers** | The Legionary Service Order | Île de France (16) NOT controlled by Vichy; Vichy at peace with controller; at peace with Vichy; any enemy country is major power and communist | National spirit: Anti-Bolshevist Volunteers; Max volunteer force divisions +3; Attack vs. Soviet Union +10.0%, Defense vs. Soviet Union +10.0% |
| **Rebuild the Military** | Emergency Powers To Pétain | — | National spirit: Rebuild the Military; Military factory construction speed +10.00% (bypassed if >34 military factories) |
| **Finish the Naval Buildup** | Rebuild the Military | — | Navy Experience +50; Random coastal core state: +2 naval dockyards |
| **Hidden Materials** | Rebuild the Military | — | National spirit: Hidden Materials; Production efficiency growth +5.00% |
| **Analyze Our Defeat** | Hidden Materials | — | 2× 50% cost reduction for Land Doctrine |
| **Modernize the Air Force** | Rebuild the Military | — | 2× 200% research bonus for: Fighter models, Close Air Support models, Tactical Bomber models |
| **Learn from the Enemy** | Modernize the Air Force | — | Vichy joins "Learning from the enemy" technology sharing group with German Reich |
| **Buy from the Enemy** | Learn from the Enemy | — | National spirit: Buy from the Enemy; License purchase cost −50% |

---

## Strategic Notes

**Metropolitan France:** The early political choice (Popular Front vs. National Bloc) is crucial and locks out parallel industrial/diplomatic paths. The communist path leads to civil war and alignment with the Soviet bloc; the right path preserves stability and allows fascism or monarchy restoration (if La Résistance enabled). The Begin Rearmament split (defensive vs. offensive doctrine) influences division templates and doctrine research. Spain intervention decisions activate once the Political branch is sufficiently developed.

**Free France:** Requires surviving as an independent government-in-exile after capitulation—Charles de Gaulle's presence is essential. The dual strategy of cultivating resistance (Refus Absurde) and recruiting overseas territories (Appeal to French Nation) generates legitimacy for the government-in-exile and allows consolidation before attempting to restore metropolitan France. The Final focus, Form the Provisional Government, requires Île de France and returns the nation to the French tree after liberation.

**Vichy France:** Heavily constrained by occupation; initial focuses remove the debuff **Disjointed Government**. The regime must choose cultural/economic policy (National Revolution line, Pétain's ideology) and military rebuilding, with collaboration options (subsidise Germany, send workers) that reduce occupation penalties. Anti-Bolshevist Volunteers and End the Occupation offer late-game autonomy if Île de France is liberated or German control weakens.
