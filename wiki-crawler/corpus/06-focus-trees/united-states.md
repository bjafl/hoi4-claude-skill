---
title: American National Focus Tree
category: focus-trees
tags: [united-states, focus tree, political, military, economic, democracy, communism, fascism, civil war]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/American_national_focus_tree
---

## Summary

The United States has a unique four-branch national focus tree (plus one joint branch). The main **Continue the New Deal / Reestablish the Gold Standard** branch is democratic and economic, offering paths to address the Great Depression; it diverges into two sub-branches: **Limited Intervention** (for earlier foreign involvement) and **Neutrality Act** (for isolation). Left-edge **Suspend the Persecution** and right-edge **America First** are communist and fascist branches respectively, both triggering civil wars if progressed. Three military branches—**War Plans Division** (enables war planning and diplomatic decisions), **War Department** (army and air force), and **Two Ocean Navy Act** (naval expansion)—run parallel and can be pursued alongside any political path.

See [United States](../05-countries/united-states.md) for the country's 1936 starting profile.

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses (all countries share these).

## Continue the New Deal / Reestablish the Gold Standard Branch

Main political/economic branch. Requires ruling party to be Democratic. Split into democratic center path (both sub-branches share many early focuses), communist *Suspend the Persecution* path (left edge), and fascist *America First* path (right edge). All paths are mutually exclusive—choosing one locks out the others.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Continue the New Deal** | None; mutually exclusive with **Reestablish the Gold Standard** | 70 | Political Power +150 | Starts the New Deal path; required for **Suspend the Persecution** |
| **Reestablish the Gold Standard** | None; Franklin Delano Roosevelt is not current leader; mutually exclusive with **Continue the New Deal** | 70 | National spirit **On the Gold Standard** (consumer goods factories +5%, stability +10%); up to 4 Senators and 20 Representatives oppose | Right-center path; required for **America First** |
| **WPA** | **Continue the New Deal** | 70 | Political Power +150 | ----- |
| **Agricultural Adjustment Act** | **WPA**; support of ≥49 Senators and ≥218 Representatives; bypassed if Great Depression spirit is already removed | 70 | Great Depression reduced: shifts from **The Great Depression** → **Slow Recovery** (PP cost −0.35/day, resource gain +5%, recruitable population +10%, consumer goods −5%) → **Slow Economic Growth** (PP cost −0.40/day, resource gain +5%, recruitable population +20%, consumer goods −7%); up to 8 Senators and 40 Representatives oppose; unlocks decision **Pay Farm Subsidies** | 230-day delay until next New Deal focus available |
| **Fair Labor Standards Act** | **Agricultural Adjustment Act**; support of ≥49 Senators and ≥218 Representatives | 70 | Same Great Depression reduction as above; up to 8 Senators and 40 Representatives oppose | 230-day delay until next New Deal focus available |
| **Federal Housing Act** | **Fair Labor Standards Act**; support of ≥49 Senators and ≥218 Representatives | 70 | Same Great Depression reduction; up to 8 Senators and 40 Representatives oppose; 5 random US states gain +1 building slot each | ----- |
| **Scientific Research & Development Office** | **WPA** | 70 | +1 research slot | ----- |
| **Rubber Reserve Company** | **Scientific Research & Development Office** | 70 | 2× 100% research bonus for Synthetic Rubber | ----- |

### Democratic Center Sub-branches

Splits into **Limited Intervention** or **Neutrality Act** (mutually exclusive). Both lead toward **Lend Lease Act** and **Arsenal of Democracy**.

#### Limited Intervention Path

Allows early foreign intervention (volunteers, guarantees, lend-lease) at cost of higher world tension and harder economy mobilization.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Limited Intervention** | **Continue the New Deal** or **Reestablish the Gold Standard**; support of ≥58 Senators and ≥261 Representatives; current ruling party democratic; no Fascist Demagogue or Communist Revolutionary in government; mutually exclusive with **Neutrality Act** | 70 | National spirit **Limited Intervention** (join faction tension −25%, send volunteers tension −35%, guarantee tension −20%, economy laws cost +100%, conscription laws cost +100%); up to 8 Senators and 40 Representatives oppose; stability −10% if war support 20–40%, −20% if war support <20%; harder economy mobilization | ----- |
| **War Propaganda** | **Limited Intervention**; current ruling party democratic | 70 | War support +10%; if war support <40%, up to 4 Senators and 20 Representatives oppose | ----- |
| **Focus on Europe** | **War Propaganda**; current ruling party democratic; mutually exclusive with **Focus on Asia**; bypassed if already at war with Germany, UK, or France | 70 | Unlocks Intervention Mandate decisions (allows Congress to authorize military action) | ----- |
| **Office of Strategic Services** | **Focus on Europe** | 70 | If La Résistance DLC off: national spirit **Office of Strategic Services** (decryption +20%, decryption research speed +5%, encryption research speed +5%); if La Résistance DLC on: national spirit **Office of Strategic Services** (strengthen resistance efficiency +25%, infiltration effectiveness +25%) | Founded OSS (WWII intelligence agency, CIA precursor) |
| **Focus on Asia** | **War Propaganda**; current ruling party democratic; mutually exclusive with **Focus on Europe**; at peace with Japan and China | 70 | Unlocks Intervention Mandate decisions | ----- |
| **MAGIC** | **Focus on Asia** | 70 | National spirit **MAGIC** (spotting chance +20%) | References breaking Japanese encryption codes |

#### Neutrality Act Path

Restricts foreign policy (cannot intervene in Europe or Asia), improves economy recovery, allows more gradual mobilization.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Neutrality Act** | **Continue the New Deal** or **Reestablish the Gold Standard**; support of ≥39 Senators and ≥174 Representatives; >95% Democratic support; no Fascist Demagogue or Communist Revolutionary; mutually exclusive with **Limited Intervention** | 70 | Political Power +200; war support −5%; if Arms Against Tyranny DLC on: national spirit **Neutrality Act** (join faction tension +25%, send volunteers tension +50%, guarantee tension +50%, embargo tension +150%, US cannot buy/sell arms to countries at war); if DLC off: national spirit **Neutrality Act** (join faction tension +25%, send volunteers tension +50%, guarantee tension +50%); if war support <40%, up to 5 Senators and 25 Representatives support; declaring war over Panay Incident: stability −30%, war support −10% | Prevents intervention in Europe or Asia; limits **Lend Lease Act** requirements |
| **Arsenal of Democracy** | **Neutrality Act**; >95% Democratic support; bypassed if no building slots available | 70 | Navy experience +50, army experience +50, air experience +10; 2 random US states gain +3 building slots and +3 military factories; 2 random US states gain +3 building slots and +3 naval dockyards | Can be taken after **Neutrality Act** |

#### Shared Focuses (Both Paths Lead Here)

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Lend Lease Act** | **Limited Intervention** or **Neutrality Act**; if war support >40%, ≥49 Senators and ≥218 Representatives; if war support ≤40%, ≥58 Senators and ≥261 Representatives; >95% Democratic support; if **Neutrality Act** complete, requires a major country of same ideology at war with >0% surrender | 70 | Replaces **Limited Intervention** or **Neutrality Act** with national spirit **Lend Lease Act** (lend-lease tension −100%); if war support >60% and not at war, up to 5 Senators and 25 Representatives support; if 40–60% and not at war, up to 4 Senators and 20 Representatives oppose; if <40% and not at war, up to 25 Senators and 100 Representatives oppose; if at war, up to 8 Senators and 40 Representatives oppose | Allows Lend-Lease |
| **Black Chamber Operation** | **Office of Strategic Services** or **Arsenal of Democracy** | 70 | If La Résistance DLC off: 2× 100% research bonus for Encryption/Decryption; if DLC on: national spirit **Black Chamber Operation** (propaganda mission effects +25%, boost ideology mission effects +25%) | Underground propaganda network in Americas |
| **Scientist Haven** | **Black Chamber Operation** or **Arsenal of Democracy**; current ruling party democratic | 70 | +1 research slot | Welcomes intellectuals fleeing oppression |
| **Manhattan Project** | **Scientist Haven** | 70 | If nuclear tech not researched: 1× 50% research bonus for Nuclear Technology + 50% breakthrough progress for Nuclear Research + national spirit **Manhattan Project** (nuclear research special projects speed +5%); if nuclear tech already researched: 100% breakthrough progress for Nuclear Research + same spirit | Atomic bomb development |
| **The Giant Wakes** | **Arsenal of Democracy**; at war or war support >30% or >95% Democratic support; bypassed if **Homeland Defense Emergency Act** spirit active | 70 | If economy law is **Undisturbed Isolation** or **Isolation**: change to **Civilian Economy** (consumer goods 35%, military/civilian conversion cost +30%, fuel gain −40%, fuel capacity −25%, factory construction −30%); otherwise: political power +100 | Switches from isolation to mobilization |
| **Wartime Industry** | **The Giant Wakes**; >95% Democratic support | 70 | National spirit **Wartime Industry** (civilian-to-military factory conversion cost −50%); available as design company **General Motors** (+15% industrial research speed, +5% factory output) | Retooling civilian factories |
| **Military Construction** | **Arsenal of Democracy**; at war or war support >30% | 70 | Army experience +10; Continental US state with ≥4 free slots gains +5 building slots and +5 military factories; random US states gain +2 infrastructure each (Louisiana, Texas, California prioritized) | Infrastructure and factory boom |
| **USACE Projects** | **Military Construction**; war support >30% or at war | 70 | Continental US state with ≥2 free slots gains +3 building slots and +3 military factories; random US state with ≥3M population and ≥2 infrastructure slots gains +3 infrastructure; air experience +50, navy experience +50, army experience +10 | Army Corps of Engineers mobilization |

### Reestablish the Gold Standard Sub-branches (Right-Center Path)

Alternative to New Deal; focuses on limited government and business-friendly policies.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Adjusted Compensation Act** | **Reestablish the Gold Standard**; support of ≥49 Senators and ≥218 Representatives | 70 | National spirit **Adjusted Compensation Payment** for 180 days (consumer goods +5%); reduces Great Depression same as Agricultural Adjustment Act; up to 4 Senators and 20 Representatives oppose | Veterans pension focus |
| **Labor-Management Relations Act** | **Adjusted Compensation Act**; support of ≥49 Senators and ≥218 Representatives | 70 | National spirit **Labor-Management Relations Act** (production efficiency cap +5%); if communist support <10%, up to 4 Senators and 20 Representatives oppose; if ≥10%, up to 8 Senators and 40 Representatives oppose | Anti-union business focus |
| **Protectionist Tariffs** | **Labor-Management Relations Act** | 70 | Reduces Great Depression; trade law changes to **Export Focus** (consumer goods 35%, construction speed +10%, research speed +5%, factory output +10%, dockyard output +10%, resources to market +50%) | ----- |
| **Income Tax Reform** | **Protectionist Tariffs**; support of ≥58 Senators and ≥261 Representatives | 70 | Reduces Great Depression; up to 8 Senators and 40 Representatives oppose; unlocks decision **Extend the Tax Breaks** | Tax cuts focus |
| **American Institute of Sciences** | **Income Tax Reform** | 70 | +1 research slot | ----- |

## Suspend the Persecution Sub-branch (Communist Path)

Far-left branch leading to **Communist States of America**. Requires **Continue the New Deal** and sufficient communist support. Triggers civil war if progressed far enough. Multiple focuses allow civil war escalation.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Suspend the Persecution** | **Continue the New Deal** | 70 | Stability −5%; available as political advisor **Earl Browder** (Communist Revolutionary, +0.10 daily communism support) | Entry to communist path |
| **Desegregate the Armed Forces** | **Suspend the Persecution**; >10% communist support or Harry S. Truman is current leader | 70 | National spirit **Armed Forces Desegregation** (recruitable population +2%) | ----- |
| **Full Desegregation** | **Desegregate the Armed Forces**; >20% communist support | 70 | Replaces **Armed Forces Desegregation** with national spirit **Full Desegregation** (recruitable population +20%); up to 25 Senators and 100 Representatives oppose; **civil war trigger** (Silver Legion protests or escalates into violence) | Major destabilization |
| **Democratic Socialism** | **Desegregate the Armed Forces**; >35% communist support; bypassed if communist party already ruling | 70 | Communist Party USA becomes ruling party; public elections held; communism popularity +25% | Ideological shift |
| **Union Representation Act** | **Suspend the Persecution**; support of ≥58 Senators and ≥261 Representatives; part of government has Communist Revolutionary trait or communist ruling party; has not completed **Limited Intervention** or **Neutrality Act** | 70 | If support <58 Senators and <261 Representatives: stability −10%; ensures comfortable majority in Congress (persisted through elections); disables congressional opposition/support events; **civil war trigger** (Silver Legion protests or escalates into violence) | Congress control |
| **Old Age Pension Act** | **Union Representation Act**; support of ≥49 Senators and ≥218 Representatives | 70 | Stability +10%; up to 4 Senators and 20 Representatives oppose | ----- |
| **Accumulated Wealth Tax Act** | **Union Representation Act**; part of government has Communist Revolutionary trait or communist ruling party; support of ≥58 Senators and ≥261 Representatives | 70 | National spirit **Accumulated Wealth Tax Act** (consumer goods −5%); reduces Great Depression; communism support +5%; if >30% communist support and communist not ruling, up to 8 Senators and 40 Representatives oppose; if <30% communist support and communist not ruling, up to 25 Senators and 100 Representatives oppose | Wealth redistribution |
| **Liberty for the Philippines** | **Full Desegregation** and **Democratic Socialism**; communist party ruling; Philippines exists | 70 | If Philippines is US subject: Philippines becomes free; if US is faction leader, Philippines joins faction | Decolonization |
| **Pacific Decolonisation** | **Liberty for the Philippines** | 70 | If Dutch East Indies exists and is subject: gain Puppet war goal against it; if Papua is not owned by Papua New Guinea, gain Conquer war goal against Papua controller | Anti-colonial focus |
| **Guarantee the American Dream** | **Old Age Pension Act** and **Accumulated Wealth Tax Act** | 70 | War support +10%; ensures Illinois, Indiana, Iowa, Michigan, Minnesota, Wisconsin remain with government in civil war (no Neutral Bloc secesssion) | Civil war preparation |
| **Worker Management Act** | **Guarantee the American Dream**; support of ≥58 Senators and ≥261 Representatives; part of government has Communist Revolutionary trait or communist ruling party | 70 | National spirit **Worker Management Act** (factory output +5%); reduces Great Depression; communism support +5%; if >30% communist support and communist not ruling, up to 8 Senators and 40 Representatives oppose; if <30%, up to 25 Senators and 100 Representatives oppose | Workers control factories |
| **Militia Organization Act** | **Guarantee the American Dream**; support of ≥58 Senators and ≥261 Representatives | 70 | National spirit **Militia Organization Act** (division training time −10%); up to 4 Senators and 20 Representatives oppose | Citizen soldier emphasis |
| **Communal Property Act** | **Worker Management Act** and **Militia Organization Act**; support of ≥58 Senators and ≥261 Representatives | 70 | Communism support +5%; reduces Great Depression; if >30% communist support and communist not ruling, up to 8 Senators and 40 Representatives oppose; if <30%, up to 25 Senators and 100 Representatives oppose; unlocks decision **Communal Domain** (Panama Canal gains +1 building slot) | Eminent domain expansion |
| **Reintegration** | **Communal Property Act**; at war with **Confederacy of American States** or civil war has started | 70 | Unlocks decision **Readmit State to the Union** (adds +2 Senators initially supporting government) | Post-civil war reconciliation |

## America First Sub-branch (Fascist Path)

Far-right branch leading to **Confederated States of America** and aggressive global expansion. Requires **Reestablish the Gold Standard** and sufficient fascist support. Triggers civil war if progressed far enough. War goals and territorial conquest dominate this path.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **America First** | **Reestablish the Gold Standard** | 70 | Available as political advisor **Charles Coughlin** (Fascist Demagogue, +0.10 daily fascism support); fascism support +5% | Entry to fascist path |
| **Extend the Chinese Exclusion Acts** | **America First**; support of ≥39 Senators and ≥174 Representatives | 70 | Up to 30 Senators and 125 Representatives support; China's leader gains opinion modifier (−100 toward US) | Anti-China racism |
| **Empower the HUAC** | **Labor-Management Relations Act** and **Extend the Chinese Exclusion Acts** | 70 | Available as political advisor **Joseph McCarthy** (Anti-Communist Crusader, stability +5%, communism support −0.10/day); unlocks decision **Investigate the Opposition** (stability −5%, up to 5 Senators and 25 Representatives support) | McCarthyism |
| **Ally With the Silver Shirts** | **America First**; >15% Silver Legion of America support; part of government has Fascist Demagogue trait; has not completed **Limited Intervention** or **Neutrality Act**; bypassed if fascist party already ruling | 70 | Up to 10 Senators and 50 Representatives support; unlocks decision **Intimidate Political Opponents** (stability −10%, up to 5 Senators and 25 Representatives support); fascism support +2%; **civil war trigger** (Protests in the Capital or The Ten-Million-March) | Militia alliance |
| **Voter Registration Act** | **Empower the HUAC**; >15% Silver Legion support; support of ≥58 Senators and ≥261 Representatives | 70 | Ensures comfortable majority in Congress (persisted through elections); disables congressional opposition/support events; if democracy >75%, stability −10%; **civil war trigger** (Protests in the Capital or The Ten-Million-March) | Authoritarian election control |
| **National Prosperity Program** | **Ally With the Silver Shirts**; >20% Silver Legion support | 70 | Stability +5% | Economic recovery |
| **Privatize the TVA** | **National Prosperity Program** | 70 | Tennessee gains +2 building slots; national spirit **Privatization of State-owned Companies** (infrastructure construction speed +10%) | Free-market policy |
| **De-Regulate the Banking Sector** | **National Prosperity Program** | 70 | National spirit **De-Regulated Banking Sector** (military factory construction speed +10%, civilian factory construction speed +10%) | Financial deregulation |
| **National Employment Strategy** | **Privatize the TVA** and **De-Regulate the Banking Sector** | 70 | Replaces **De-Regulated Banking Sector** with **National Employment Strategy** (production efficiency growth +10%); reduces Great Depression | Matching workers to jobs |
| **Invite Foreign Support** | **Ally With the Silver Shirts** | 70 | Unlocks decision group **Search for Foreign Supporters** (approach major countries for material support) | Nazi and Japanese aid |
| **Send Lindbergh To Germany** | **Invite Foreign Support** | 70 | Air experience +75; available as Chief of Air Force **Charles Lindbergh** (fighter fuel usage −10%, pilot training experience gain +15%) | Charles Lindbergh consulting role |
| **Work With the Bund** | **Send Lindbergh To Germany**; at peace with Germany; bypassed if in civil war | 70 | Stability +5%; Germany gains opinion modifier toward US (+35); ensures Ohio, Missouri, Wisconsin, Illinois, Indiana, Michigan remain with government in civil war | German-American Bund coordination |
| **Recruit the Free Corps** | **Send Lindbergh To Germany** | 70 | Unlocks decision **Raise the Free Corps** (raises loyal infantry units in government-held areas) | German Freikorps model |
| **War Powers Act** | **America First**; support of ≥58 Senators and ≥261 Representatives; >30% Silver Legion support | 70 | National spirit **War Powers Act** (offensive war penalty stability −20%, defensive war penalty stability −20% → modified to +20%); sets rule: can create factions | Executive warmaking power |
| **Honor the Confederacy** | **National Employment Strategy** and **Work With the Bund**; in civil war or fascist/non-aligned ruling party | 70 | Unlocks decision group **Honor the Confederacy** (rebuild trust in civil war by reconnecting with past) | Southern reconciliation |
| **Seize Cuba** | **War Powers Act**; >35% war support; bypassed if own/control Cuba or at war with Cuba or Cuba is subject or have annex goal | 70 | Gain Annex war goal against Cuba (if controlling), or Take State war goal against Cuba controller | Hegemonic ambition |
| **Eliminate the Southern Threat** | **Seize Cuba**; bypassed if Mexico is subject, does not exist, or at war with US | 70 | Mexico's leader receives event **The United States demands Treaty of Consultation and Friendship** | Mexican subjugation |
| **Manifest Destiny** | **War Powers Act** | 70 | National spirit **Manifest Destiny** (justify war goal time −35%) | Expansionist ideology |
| **The Canadian Corridor** | **Manifest Destiny**; controller of British Columbia (473), Prince Rupert (471), Yukon Territory (864) is a third country; bypassed if these provinces are controlled, owned, or owner at war with US or subject | 70 | Controller of British Columbia receives event **The Canadian Corridor** | Canada subjugation path |
| **North American Dominion** | **Eliminate the Southern Threat** and **The Canadian Corridor**; bypassed if Cuba, Haiti, Dominican Republic, Guatemala, Canada, Mexico, Honduras, Nicaragua, Panama, Costa Rica do not exist or are at war/subject | 70 | These countries (if not at war and not subjects) receive event **The United States demands Control over Foreign Policy** | Hemispheric hegemony |
| **Strategic Interests** | **North American Dominion**; bypassed if Kuala Lumpur, Penang, Chūsei-Zenra, Hong Kong, Gibraltar controller at war with US or controlled | 70 | Controllers of Kuala Lumpur, Hong Kong, Gibraltar (or their overlords) receive event **US demands Territories** | Global base network |
| **Protect South America** | **Strategic Interests**; bypassed if Brazil, Venezuela, Colombia, Ecuador, Peru, Bolivia, Paraguay, Argentina, Chile, Uruguay do not exist or are at war/subject | 70 | These countries (if not at war and not subjects) receive event **The South-American Security Summit** | South American subjugation |
| **Pacific Pacification** | **North American Dominion**; Australia and New Zealand exist; bypassed if both do not exist or are at war/subject | 70 | Australia and New Zealand (or their overlords if subjects) receive event **The United States demand colonial holdings** (if not at war) | Oceania subjugation |
| **Secure Asia** | **Pacific Pacification**; bypassed if Siam, Dutch East Indies, and Indochina controllers are at war, subjects, or do not exist | 70 | If Siam/Indonesia/Vietnam/Laos/Cambodia not subject and not at war: receive event **The United States exerts pressure**; if Dutch East Indies is subject, overlord receives **US demands control over colonies**; if Indochina not at war: **The United States demands Indochina** | Asian colonial seizure |
| **Global Hegemony** | **Protect South America** and **Secure Asia** | 70 | Gain Puppet war goals against every major power not US and not already at war with US | Final fascist objective |

## War Plans Division Branch

Parallel military branch enabling war planning, decisions, and regional dominance preparations. No prerequisites; runs independently from political branches.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **War Plans Division** | None | 70 | Available as Chief of Army **Walter Krueger** (Army Planning Expert, planning speed +10%); unlocks War Plans decisions | Military planning hub |
| **Intervention in the Americas** | **War Plans Division** | 70 | National spirit **Intervention in the Americas** (planning speed +5%) | Americas war prep |
| **War Plan Green** | **Intervention in the Americas** | 70 | Unlocks decision **Execute War Plan Green**: infrastructure construction speed +10%, Mexico attack/defense bonus +10% | Mexico contingency |
| **Reaffirm Monroe Doctrine** | **Intervention in the Americas** | 70 | Trade opinion +1 with all American nations; unlocks Intervention Mandate decisions | Diplomatic influence |
| **War Plan Gray** | **Reaffirm Monroe Doctrine** | 70 | Unlocks decision **Execute War Plan Gray**: invasion preparation time −50%, amphibious invasion speed +10% | Caribbean contingency |
| **Hemisphere Defense** | **War Plan Gray** | 70 | If US not in faction: create **Treaty of Reciprocal Assistance** (Treaty of Rio, Americas faction); if faction leader and Latin American country same ideology and not at war and independent: invite to faction | Pan-American alliance |
| **War Plan Crimson** | **Intervention in the Americas** | 70 | Unlocks decision **Execute War Plan Crimson**: land fort construction speed +10%, Canada attack/defense bonus +10% | Canada contingency |
| **Intervention in Europe** | **War Plans Division** | 70 | National spirit **Intervention in Europe** (daily command power gain +10%); if La Résistance DLC on: George Musulin becomes an operative | Europe war prep |
| **War Plan Gold** | **Intervention in Europe** | 70 | If La Résistance on: René Joyeuse becomes operative; unlocks decision **Execute War Plan Gold**: France attack/defense bonus +10% | France contingency |
| **War Plan Silver** | **Intervention in Europe** | 70 | If La Résistance on: Joe Savoldi becomes operative; unlocks decision **Execute War Plan Silver**: Italy attack/defense bonus +10% | Italy contingency |
| **War Plan Black** | **Intervention in Europe** | 70 | Germany gains opinion modifier toward US (−50); if La Résistance on: William G Sebold becomes operative; unlocks decision **Execute War Plan Black**: Germany attack/defense bonus +10% | Germany contingency |
| **Destroyers For Bases** | **War Plan Black**; Germany and UK exist; UK democratic and at war at peace with US; bypassed if Bermuda, Newfoundland, Leeward Islands, Bahamas, Jamaica, Trinidad not controlled by UK or UK does not exist | 70 | UK receives event **Destroyers for Bases Agreement** (requires approval); US becomes owner/controller of Bermuda, Newfoundland, Leeward Islands, Bahamas, Jamaica, Trinidad | 1940 historical deal |
| **War Plan White** | **Intervention in Europe** | 70 | Soviet Union gains opinion modifier toward US (−50); if La Résistance on: Serge Obolensky becomes operative; unlocks decision **Execute War Plan White**: Soviet Union attack/defense bonus +10% | Anti-communist contingency |
| **Anti-Bolshevik Aid** | **War Plan White**; Soviet Union not in civil war | 70 | Unlocks decision **Guns for the Anti-Bolshevik War** (send 1000 infantry equipment to countries at war with USSR, oldest first) | Support for anti-Soviet forces |
| **War Plan Red** | **Intervention in Europe** | 70 | UK gains opinion modifier toward US (−50); unlocks decision **Execute War Plan Red**: spotting chance +10%, UK attack/defense bonus +10% | British contingency |
| **War Plan Ruby** | **War Plan Red** | 70 | Unlocks decision **Execute War Plan Ruby**: spotting chance +10%, British Raj attack/defense bonus +10% | India contingency |
| **War Plan Scarlet Garnet** | **War Plan Red** | 70 | Unlocks decision **Execute War Plan Scarlet-Garnet**: spotting chance +10%, Australia and New Zealand attack/defense bonus +10% | British Dominion contingency |
| **Intervention In Asia** | **War Plans Division** | 70 | Alexander Vandegrift becomes a general | Asia war prep |
| **War Plan Orange** | **Intervention In Asia** | 70 | Japan gains opinion modifier toward US (−50); unlocks decision **Execute War Plan Orange**: invasion prep time −25%, amphibious invasion speed +10%, Japan/Manchukuo/Mengkukuo attack/defense bonus +10% | Japan contingency (primary threat) |
| **War Plan Yellow** | **Intervention In Asia** | 70 | Unlocks decision **Execute War Plan Yellow**: China/Communist China/Shanxi/Yunnan/Xibei San Ma/Guangxi Clique/Sinkiang attack/defense bonus +10% | China contingency |
| **Defense of the Pacific** | **War Plan Orange** and **War Plan Yellow**; Japan exists; Japan not democratic ruling party | 70 | Attu Island, Midway Island, Wake Island, Guam, Phoenix Island each gain +2 coastal forts and +2 naval bases | Pacific fortress |

## War Department Branch

Combined military-industrial and doctrine branch covering army, air force, and general military organization.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **War Department** | None | 70 | National spirit **War Department** (maximum command power increase +20) | Military administration |
| **Selective Training Act** | **War Department**; if world tension <50% or not at war, ≥58 Senators and ≥261 Representatives; otherwise ≥39 Senators and ≥174 Representatives | 70 | If mobilization law is **Disarmed Nation** or **Volunteer Only**: change to **Limited Conscription** (recruitable population +2.5%); otherwise political power +150; if war support <10%, set to 10%; if war support <40%, up to 8 Senators and 40 Representatives oppose | Draft authorization |
| **First Special Service Force** | **Selective Training Act** | 70 | Army experience +5; 1× 100% research bonus for Paratroopers I–II, Mountain Infantry I–II, Engineer Company I–III, Recon Company I–III | Special forces development |
| **Louisiana Maneuvers** | **Selective Training Act** | 70 | Army experience +20; 1× 50% cost reduction for Land Doctrine; **George S. Patton** gains +1 skill level | War games training |
| **Airborne Divisions** | **Louisiana Maneuvers** | 70 | National spirit **Airborne Divisions** (special forces capacity multiplier +5%); if Arms Against Tyranny DLC on: +1 free special forces branch specialism + 2× 25% cost reduction for Special Forces Doctrine | Paratroop doctrine |
| **Army of the United States** | **Louisiana Maneuvers** | 70 | National spirit **Army of the United States** (mobilization speed +20%); **Omar Bradley** and **Mark W. Clark** gain +1 skill level | Massive army expansion |
| **Women's Armed Service Integration Act** | **Army of the United States**; support of ≥49 Senators and ≥218 Representatives | 70 | National spirit **Women's Armed Service Integration Act** (recruitable population +2%) | Female military service |
| **Support Rock Island** | **Selective Training Act** | 70 | 2× 100% research bonus for Support Artillery and Support technology | Artillery support doctrine |
| **Tank Experiments** | **Support Rock Island** | 70 | Land Warfare breakthrough +50%; 1× 100% research bonus for Armor technology | Tank development |
| **Tank Destroyer Doctrine** | **Tank Experiments**; mutually exclusive with **Main Battle Tanks** | 70 | If Arms Against Tyranny DLC on: available as Military Industrial Organization **Tank Destroyer Board** (+2 sizes, mobile tank destroyers); if DLC off: available as design company **Tank Destroyer Board** (armor research speed +15%, light/medium/heavy tank destroyer production cost −10%, piercing +10%, hard attack +25%) | Asymmetric tank warfare |
| **Main Battle Tanks** | **Tank Experiments**; mutually exclusive with **Tank Destroyer Doctrine** | 70 | If Arms Against Tyranny DLC on: available as Military Industrial Organization **Detroit Arsenal** (+2 sizes, standardized production); if DLC off: available as design company **Detroit Arsenal** (armor research speed +15%, medium tank/light tank production cost −10%) | Unified tank doctrine |
| **Armored Infantry** | **Tank Destroyer Doctrine** or **Main Battle Tanks** | 70 | 2× 100% research bonus for Motorized | Motorized combined arms |
| **Build the Pentagon** | **War Department** | 70 | National spirit **The Pentagon** (planning speed +10%) | Military headquarters |
| **Department of Defense** | **Build the Pentagon** | 70 | Replaces **War Department** with national spirit **Department of Defense** (maximum command power increase +10, daily command power gain +10%) | Renamed War Department |
| **Air War Plans Division** | **War Department** | 70 | Air experience +25; 2× 50% cost reduction for Air Doctrine; national spirit **Air War Plans Division** (fighter/heavy fighter production cost −10%) | Air force planning |
| **Air Support** | **Air War Plans Division**; mutually exclusive with **Strategic Bombing** | 70 | Air experience +25; national spirit **Air Support** (close air support/tactical bomber production cost −10%) | Tactical air focus |
| **CAS Effort** | **Air Support** | 70 | 1× 100% research bonus for Close Air Support models | Ground-support aircraft |
| **Tactical Bomber Effort** | **Air Support** | 70 | Air experience +25; 2× 100% research bonus for Tactical Bomber models | Tactical bomber doctrine |
| **US Army Air Force** | **Tactical Bomber Effort** | 70 | 2× 50% cost reduction for Air Doctrine | Army air force integration |
| **Strategic Bombing** | **Air War Plans Division**; mutually exclusive with **Air Support** | 70 | Air experience +25; national spirit **Strategic Bombing** (strategic bomber production cost −10%) | Strategic air campaign |
| **Escort Fighters** | **Air Support** or **Strategic Bombing** | 70 | 1× 300% research bonus for Heavy Fighter models | Long-range escort fighters |
| **Combined Bomber Offensive** | **Strategic Bombing**; at war; in faction with Germany, Japan, Italy, Soviet Union, France, or UK | 70 | Air experience +25; 1× 100% research bonus for Heavy aircraft; national spirit **Combined Bomber Offensive** (strategic bomber range +50%) | Coordinated bombing with allies |
| **US Air Force** | **Combined Bomber Offensive** | 70 | National spirit **US Air Force** (air doctrine cost −10%) | Independent air force (postwar) |

### Two Ocean Navy Act Sub-branch

Naval expansion and doctrine branch under **War Department**.

| Focus | Prerequisites | Cost | Effects | Notes |
|---|---|---|---|---|
| **Two Ocean Navy Act** | **War Department**; if world tension <50% or not at war, ≥58 Senators and ≥261 Representatives; otherwise ≥39 Senators and ≥174 Representatives; controls California and New York | 70 | Up to 8 Senators and 40 Representatives oppose; California gains +5 building slots and +5 naval dockyards; New York gains +5 building slots and +5 naval dockyards; **Ernest King** gains +1 skill level | Two-ocean navy |
| **Maritime Commission** | **Two Ocean Navy Act** | 70 | National spirit **Maritime Commission** (dockyard construction speed +10%) | Cargo ship coordination |
| **Liberty Ships** | **Maritime Commission** | 70 | National spirit **Liberty Ships** (amphibious invasion speed +10%, trade convoy production cost −25%) | Mass cargo production |
| **Bureau of Ships** | **Two Ocean Navy Act** | 70 | Navy experience +50; national spirit **Bureau of Ships** (naval equipment experience cost −10%, heavy ship/carrier/cruiser/light hull/submarine production cost −5%); removes **Bureau of Ordnance** (torpedo hit chance −10%); **Chester W. Nimitz** and **William Halsey Jr.** gain +1 skill level | Unified naval R&D |
| **Battleship Primacy** | **Bureau of Ships**; mutually exclusive with **Carrier Primacy** | 70 | Naval Engineering breakthrough +25%; 2× 100% research bonus for Battleship models | Dreadnought doctrine |
| **Advanced Mahanian Doctrine** | **Battleship Primacy** | 70 | +10% mastery bonus for 180 days on all Capital Ships tracks | Mahan naval theory |
| **Advanced Basing** | **Advanced Mahanian Doctrine** | 70 | Guam gains +2 naval bases; if Manila controller is US subject, gains +2 naval bases | Pacific base network |
| **Carrier Primacy** | **Bureau of Ships**; mutually exclusive with **Battleship Primacy** | 70 | Naval Engineering breakthrough +25%; 2× 100% research bonus for Carrier models; creates Essex-class Carrier variant on researching Improved Carrier | Fleet carrier doctrine |
| **Bureau of Aeronautics** | **Carrier Primacy** | 70 | 1× 100% research bonus for Naval Bomber models and Naval aircraft | Naval air development |
| **Naval Radar** | **Bureau of Aeronautics** | 70 | Naval Engineering breakthrough +25%; Aerodynamics and Avionics breakthrough +50%; 1× 100% research bonus for Radar technology | Detection technology |
| **Escort Effort** | **Bureau of Ships** | 70 | National spirit **Escort Effort** (light hull production cost −10%) | Anti-submarine destroyer focus |
| **Convoy Tactics** | **Escort Effort** | 70 | Navy experience +25; +50 mastery on all Screens tracks; +10% mastery bonus for 180 days on active Screens tracks; if No Compromise, No Surrender DLC on: creates Casablanca-class Carrier variant on Escort Carrier research | Trade defense |
| **Fleet Submarines** | **Bureau of Ships**; completed special project Cruiser Submarine | 70 | 2× 100% research bonus for Submarine models; Naval Engineering breakthrough +25%; national spirit **Fleet Submarines** (fleet submarine research speed +100%, production cost −10%) | Long-range submarine warfare |
| **Unrestricted Submarine Warfare** | **Fleet Submarines** | 70 | National spirit **Unrestricted Submarine Warfare** (submarine surface detection +10%, sub visibility −10%) | Unrestricted raiding |
| **Fund The Navy** | **Two Ocean Navy Act** | 70 | 3× 50% cost reduction for Naval Doctrine | Naval doctrine development |
| **Expand The USMC** | **Fund The Navy** | 70 | If Arms Against Tyranny DLC on: 2× 25% cost reduction for Special Forces Doctrine; if DLC off: 1× 100% research bonus for Marines II–III | Marine Corps expansion |
| **Amphibious Operations** | **Expand The USMC** | 70 | 2× 100% research bonus for Transport models | Amphibious assault doctrine |

## Establish the ABDACOM Branch

Joint branch coordinate with Australia, Dutch East Indies, Siam, France, Netherlands, and United Kingdom for ABDA (American, British, Dutch, Australian) Command in southeast Asia. Details on separate wiki page (see sources).

---

> ⚠️ Incomplete wiki information: the Establish the ABDACOM branch is documented on a separate joint focus page and is not fully detailed in the main American focus tree article. The table of contents and navigation links suggest the complete tree structure exists, but only the overview reference appears here.
