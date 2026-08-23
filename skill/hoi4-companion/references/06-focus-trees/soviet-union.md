---
title: Soviet Union National Focus Tree
category: focus-trees
tags: [soviet union, focus tree, national focus, communism, trotskyism, bukharin, stalinist, great purge, civil war]
game_version: "1.19"
dlc: [No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Soviet_national_focus_tree
  - https://hoi4.paradoxwikis.com/Soviet_national_focus_tree:_industrial_branches
  - https://hoi4.paradoxwikis.com/Soviet_national_focus_tree:_political_branches
---

## Summary

The Soviet Union has a unique and extensive focus tree centered on industrialization, political ideology, and the choice between historical communism (Stalinist) and alternative paths (Trotskyist, Bucharinist, or monarchist/fascist). The tree spans industrial development via five-year plans, air force modernization, naval expansion, and political branches that unlock either Stalin's path with the Great Purge or civil war scenarios with Trotsky or Bukharin. With **No Step Back** DLC enabled, alt-historical branches (monarchist, fascist, Bucharinist) become available; the base game restricts most political choices to the Communist Stalinist path.

## Generic and continuous focus mechanics

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses — those shared by all nations. This file covers only Soviet-specific focuses.

## Industrial branches

This covers 7 industrial focuses and 2 sub-branches that modify the **Five Year Plan** national spirit through choices: **Reorganize the PC of Heavy Industry** (civilian-focused) vs. **Shift To Armaments Production** (military-focused).

### Infrastructure Effort/Heavy Industry Branch

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Infrastructure Effort** | None | Add 2 infrastructure to 4 random owned controlled states (repeats 4 times). Bypass: if insufficient building slots for infrastructure. | Essential start; distributed infrastructure across the vast USSR. |
| **Heavy Industry** | None | Add 1 building slot + 1 civilian factory to random owned controlled state (repeats 2x). | Foundation for industrial growth. |
| **Finish the Five Year Plan** | Infrastructure Effort + Heavy Industry; >100 controlled factories | Modifies Five Year Plan: Production efficiency growth +5.00%, Industrial Concern cost −15%, Consumer goods factories +5.0%. Available political advisor: Lazar Kaganovich (Iron Lazar, train cost +5%, armor +10%, supply hub/railway construction +5%, fuel gain +5%). 2×75% research bonus for Construction. | Progresses five-year plan; Kaganovich unlocked. |
| **Improve Railway Network** | Finish the Five Year Plan | Build railways: Ryazan (254)–Rostov (218); Stalingrad (217)–Millerovo (245); Stalingrad–Saratov (239); Stalingrad–Astrakhan (236); Georgia (231)–Armenia (230). Add 1 supply hub each to Murmansk (213) and Armenia (230). Design Company: Soviet Railways (railway construction +15%, train cost −25%, supply hub/railway construction +15%, research speed +10%). | Ensures rail connectivity for logistics; unlocks railway design company. |
| **Third Five Year Plan** | Finish the Five Year Plan; USSR not at war with major power; >120 factories; not completed Curtailment of Collective Farms | Modifies Five Year Plan (Communist) or New Project (non-Communist): Production efficiency growth +5.00%, industrial concern cost −15%, consumer goods factories +5.0%. 2×75% research bonus for Construction. **Locks permanently if at war with major power.** | Conditional wartime lock mirrors historical Soviet dilemma. |
| **Increase State Reserves** | Third Five Year Plan; USSR not at war; >0 factories; not completed Curtailment | Modifies Five Year Plan: Resource gain efficiency +10.00%. If Reorganize PC (Heavy Industry) selected: same bonus. If Shift To Armaments selected: same bonus. 3 random states: Add 1 building slot + 1 fuel silo. | Builds resource resilience. |
| **Reorganize the PC of Heavy Industry** | Third Five Year Plan; mutually exclusive with Shift To Armaments; >130 factories; peacetime; not Curtailment | Modifies Five Year Plan: Consumer goods factories −5.0%. 2×100% research bonus for Industry and Electronics. | Civilian-focused path; reduces consumer goods burden. |
| **Shift To Armaments Production** | Third Five Year Plan; mutually exclusive with Reorganize; >130 factories; peacetime; not Curtailment | Modifies Five Year Plan (military): Civilian factory construction −5%, military factory construction +10%. 2×100% research bonus for Infantry Weapons. | Military-focused path; accelerates war production. |
| **Industrial Modernization** | Reorganize PC; >150 factories; peacetime | Modifies Five Year Plan (civilian): Production efficiency cap +5%, retention +10%. Reduce ahead-of-time penalty 2 years; 100% research bonus for Industry. | Civilian efficiency upgrade. |
| **Optimize Production Lines** | Shift To Armaments; >150 factories; peacetime | Modifies Five Year Plan (military): Factory output +2%, efficiency growth +5%, efficiency base +5%. 2×100% research bonus for Production. | Military efficiency upgrade via "Fordism." |
| **Steel Casting Industry** | Requires Reorganize OR Shift; any owned state with ≥1 steel; can build 1+ civilian factory; peacetime | If Reorganize selected: Factory output +5%, dockyard output +5%. If Shift selected: Factory output +5%, dockyard output +5%. Random owned controlled state with steel: Add 1 building slot + 1 civilian factory + produce 5 steel. | Steel production doubled; shared effect for both military/civilian paths. |
| **Synthetic Rubber** | Steel Casting + researched Rubber Processing; full control Moscow (219); full control Voronezh (260) or Tula (223); peacetime | If Voronezh: Add 2 building slots + 1 synthetic refinery; railway Moscow–Voronezh. If Tula: Add 2 slots + 1 synthetic refinery; railway Moscow–Tula. 2×75% research bonus for Synthetic Rubber. | Substitute for unavailable natural rubber; requires specific state control. |
| **Oil Production** | Steel Casting; peacetime | If Reorganize selected: Synthetic oil +5%, fuel gain from refineries +5%. If Shift selected: Synthetic oil +5%, fuel gain +5%. Every owned state with oil & <3 infrastructure: Add infrastructure + fuel silo (max 2). If full control Azerbaijan/Armenia/Georgia: Railway Baku–Tbilisi. If full control Dagestan/Chechnya-Ingushetia: Railway Makhachkala–Grozny. | Secures fuel independence; leverages Caucasus oil. |
| **Restoration and Development** | Requires Modernization OR Optimize; USSR at peace with major power; not Curtailment | National spirit (365 days): Consumer goods factories +10%, factory repair speed +10%, infrastructure construction +10%. If Communist: 3 propaganda campaigns unlocked (We will Rebuild to Glory, You will Live a Happy Life, Long Live to Peace). | Post-war recovery mode; unlocks propaganda campaigns for Communists. |
| **Fourth Five Year Plan** | Restoration and Development; >200 factories; peacetime; not Curtailment | Modifies Five Year Plan: Consumer goods factories −5%, factory repair +5%, efficiency cap +5%. | Extended industrialization phase. |
| **Found the COMECON** | Fourth Five Year Plan; Communist ruling party; >0 subject nations; not Curtailment. Bypass if No Compromise DLC + Curtailment completed | Soviet Union gets COMECON spirit: Consumer goods −10%. Every subject gets COMECON: Consumer goods −15%, master ideology drift +0.05%, subject manpower requirement −100%, extra trade +25%, civilian/military industry +50%, freedom from trade −75%. USSR + subjects join COMECON faction & Tech Sharing. | Locks subjects into economic bloc; major diplomatic tool. |
| **Found the Warsaw Pact** | No Compromise DLC required; Fourth Five Year Plan; >0 subjects; independent; faction leader; Communist. | Renames Comintern to Warsaw Pact; manifesto changes to "An Iron Curtain"; +1 long-term goal slot; faction goal "Eastern European Security." | Requires DLC; transforms Comintern into Eastern Bloc military alliance. |
| **The Common Economic Space Initiative** | Fourth Five Year Plan; non-Communist ruling party; >0 subjects | Russia gets Common Economic Space: Consumer goods −10%. Subjects: Consumer goods −15%, ideology drift +0.05%, subject manpower −100%, trade +25%, industry +50%, trade freedom −75%. Russia & subjects join Common Economic Space/Tech Cooperation. | Non-Communist alternative to COMECON. |
| **National Specialists** | Finish the Five Year Plan; mutually exclusive with Foreign Experts | Industrial Concern cost −50%. Modify designers: Stalingrad Tractor (industry research +10%, consumer goods −2%), Leningrad (electronics +10%, supply −2%), Soviet Railways (trains/railways +10%, mobilization +2%). | Domestic expertise; reduces design company costs. |
| **Foreign Experts** | Finish the Five Year Plan; mutually exclusive with National Specialists | Design Company: Gosproyektstroy (Construction). Infrastructure +10%, railway +10%, military/civilian factory +5%, dockyard +5%. Upgradeable. | Capitalist know-how; construction focus. |
| **Eastern Development** | Requires National Specialists OR Foreign Experts; full control Vladivostok (408) OR Khabarovsk (409) OR Irkutsk (566) OR Buryatia (564) | Vladivostok/Irkutsk: Add infrastructure + building slot + civilian factory. Khabarovsk/Buryatia: Add infrastructure + building slot + civilian factory. | Opens Far East & Siberia for exploitation. |
| **Develop the Urals** | Requires National Specialists OR Foreign Experts; full control Chelyabinsk (572) OR Zlatoust (573) OR Magnitogorsk (582) OR Sverdlovsk (653) | Chelyabinsk/Magnitogorsk: Add infrastructure + slot + factory. Zlatoust/Sverdlovsk: Add infrastructure + slot + factory. | Ensures "second industrial base" safe from Western bombers. |
| **The USSR Academy of Sciences** | Eastern Development + Develop the Urals | +1 research slot. If Communist: USSR joins Soviet Academies of Sciences program (research +1% per ally up to cap); gains dynamic modifier USSR Academy (research +1%). If non-Communist: joins Imperial Academies program. 20+ Soviet republics can join. | Research coordination hub; major tech boost. |
| **National Academies of Sciences** | USSR Academy of Sciences | Unlocks decisions to build Academies in allied/puppet/integrated Soviet territories, increasing USSR Academy bonus. | Extends research bonuses to satellites. |
| **No Time For Peace** | Fourth Five Year Plan + National Academies | Gain 75% breakthrough: Nuclear Research, Aerodynamics/Avionics. If no Atomic Research: 2×50% bonus Nuclear Technology, 1×50% bonus Rocketry. National spirit (No Time For Peace): Nuclear production +15%, radar construction +10%, rocket site +10%, reactor +10%. | Prepares nuclear & rocket programs. |
| **Transformation of Nature** | Fourth Five Year Plan + National Academies; Communist; controls Kherson, Kuybyshev, Stalingrad, Millerovo | National spirit (365 days): Consumer goods −6%, stability +5%, max factories +1. 4 dams added: Stalingrad (dam state: max factories +15%, energy −65%, resources +10%, construction +15%), Kherson, Millerovo, Kuybyshev (same modifiers). Stalin-era names (Stalingrad Hydroelectric vs. Volgograd if non-Stalin). | Iconic Soviet megaproject; massive state bonuses; conditional on Stalin leadership. |

---

### Transpolar Flights Branch (Air Force)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Transpolar Flights** | None | Air experience +50 | Opens Arctic shortcuts for air operations. |
| **Expand the Aircraft Industry** | Transpolar Flights; any owned state can build 1+ military factory | If Communist: Soviet Air Force designer cost −25%. If non-Communist: Russian Air Force designer cost −25%. Random controlled state: Add 2 building slots + 2 military factories + 2 air bases. | Multiplies aircraft production capacity. |
| **Modernize Aircraft Facilities** | Expand Aircraft | If Communist: Air range +5%, agility +5%, fuel consumption −5%. If non-Communist: same to Russian Air Force. 1 Aerodynamics facility in Voronezh (260) if none exists. | Improves air unit quality; establishes design facility. |
| **Merge Aircraft Plants** | Modernize Aircraft; not Political Paranoia active | Arms Against Tyranny DLC: Unlock merge traits for specific plants (Plant 28: cost −5%; Plant 150: agility +5%; VEF: air defense +10%, detection ±15%). Otherwise: Unlocks merge plant decisions for designers. | Consolidates scattered design bureaus (civil war reference). |
| **Found the Jet Institute** | USSR Academy of Sciences + Merge Aircraft Plants | Breakthrough: Aerodynamics +75%. 2×50% research bonus for Jet Technology. | Launches advanced jet development. |
| **Foster Flying Clubs** | Transpolar Flights | If Communist: Ace chance +25%, training experience +10%, accidents −25%, bad weather −10%. If non-Communist: same to Russian Air Force. Air experience +25. | Generates experienced pilots cheaply. |

---

### Expand the Red Fleet Branch (Naval)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| *(Details from first page only; full sub-branches not captured in detailed fetches. Described as modifying The Red Fleet national spirit and giving bonuses to coastal states.)* | — | — | Naval branch enhances dockyard capacity, ship production, coastal defense. |

---

### Found the PCDI & Strengthen Mobilization Branches (Army)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| *(Details from first page only; sub-branches reference Defense Industry and The Red Army spirits; military engineering & artillery/armor bonuses for PCDI; infantry for Mobilization.)* | — | — | PCDI: Defense Industry spirit, fort construction in strategic locations, Ural relocation. Mobilization: The Red Army spirit, infantry bonuses. |

---

## Political branches

The political tree is the largest and most branching component, allowing 4 competing ideological paths. Path selection is determined by mutually exclusive choices beginning with **The Path of Marxism Leninism** (Communist Stalinist) vs. **Beaten, but not Defeated** (monarchist/alt-historical).

### The Path of Marxism Leninism (Communist - Historical Path)

Leads to Stalin's consolidation of power via the Great Purge, culminating in a cult of personality. Mutually exclusive with Beaten, but not Defeated.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The Path of Marxism Leninism** | None; mutually exclusive with Beaten, but not Defeated | Political power +25. If Political Paranoia active: reduce by −10. | Branch choice; starts communist historical path. |

#### The Centre Sub-branch (Stalinist Path)

Historical line leading to Stalin's supremacy via purges.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The Centre** | Path of Marxism Leninism; mutually exclusive with Left/Right Opposition | Politburo modifier: communism support +0.05 daily, political power +25. Stability +5%. Enable NKVD Pogranichnya Diviziya template editing. | Establishes Stalin's position; unlocks elite border guard unit editing. |
| **Socialism in One Country** | The Centre | Modify Politburo: ideology drift defense +5%, communism support +0.05 daily, defensive stability +25%, political power +25. Reduce paranoia if active. If faction leader: faction goal "Expand the Red Armies" added. | Justifies isolationist policy; strengthens stability against defensive wars. |
| **The Stalin Constitution** | The Centre | Modify Politburo: ideology drift defense +5%, political power gain +5%, political power +50, stability +5%. Reduce paranoia −10. | Constitution reaffirms Stalin's authority. |
| **The Zinovyevite Terrorist Center** | Stalin Constitution | Activates flag (paranoia cannot auto-cancel). Political power +25. Stalin starts Great Purge (unavoidable). Event: 'First Moscow Trials.' If Paranoia active: increase by +30. If Communist & no Lessons of War: Red Army land mastery −5%. | First purge wave; Great Purge inevitable. |
| **Secure the Administration** | Zinovyevite Center | Modify Politburo: economy/trade/conscription laws −20% cost, political power +50. Reduce paranoia −20 if active. | Purges administration of suspected enemies. |
| **The Collectivization Process** | Secure Administration + Socialism; competing requirements | Modify Politburo: consumer goods −2%, max factories +10%, construction +5%, stability −5%, war support −5%. Random state: Add 2 building slots + 2 civilian factories. Reduce paranoia −20. | Agricultural consolidation (historical famine reference); stability penalty. |
| **The Anti-Soviet Trotskyist Center** | Zinovyevite Center; 175+ days since Zinovyevite | Activates flag. Political power +25. Stalin starts Great Purge (unavoidable). Event: 'Second Moscow Trials.' If Paranoia: increase +30. Iosif Stalin gains trait "Political Paranoia" (+1 weekly). If Communist & no Lessons: Army −5%. | Second purge wave intensifies paranoia. |
| **The Workers' Dictatorship** | Anti-Soviet Trotskyist Center | Modify Politburo: political power gain +5%, minimum surrender +5%, political power +50. Reduce paranoia −10 if active. | Reinforces proletarian control narrative. |
| **Centralization and Discipline** | Collectivization + Workers' Dictatorship | Modify Politburo: max command power +20, mobilization +5%, political power +50. Reduce paranoia −20 if active. | Command authority consolidated. |
| **War Economy** | Centralization and Discipline | If at peace: stability −10%. If no War Economy/Total Mobilization law: Change to War Economy (military factories +20%, conversion −20%). Moscow/random state: Add 2 slots + 2 military factories. | Shifts economy to wartime footing. |
| **The Military Conspiracy** | Workers' Dictatorship; 175+ days since Anti-Soviet Trotskyist | Activates flag. Political power +25. Stalin starts Great Purge (unavoidable). If Paranoia: increase +30. If Communist & no Lessons: Army −5%. | Third (military) purge wave; targets officer corps. |
| **Behead the Snake** | Military Conspiracy; Communist; Trotsky in Mexico; not extradited | If La Résistance DLC: Unlock Trotsky assassination operation. Ramón Mercader operative gained (Tough, Infiltrator; Soviet/Spanish/Mexican). Modify Politburo: operative slots +1. Otherwise: Unlock decisions to assassinate Trotsky. Reduce paranoia −30 if active. | Operation to eliminate exiled Trotsky (historical reference). |
| **The Bloc of Rights and Trotskyites** | Military Conspiracy; 175+ days since Military Conspiracy | Activates flag. Political power +25. Stalin starts Great Purge (unavoidable). Event: 'Third Moscow Trials.' Political Paranoia **removed** from game. Iosif Stalin loses trait (gains ideology drift +10%, weekly paranoia +2). If Communist & no Lessons: Army −5%. | Final purge wave eliminates paranoia mechanic; establishes Stalin's complete control. |
| **Stalin's Cult of Personality** | Bloc of Rights; 175+ days later; completed Expand Agitprop; Iosif Stalin is leader | Political power +25. Propaganda campaign 'Under the Leadership of Stalin!' unlocked (requires Agitprop): Political power gain +7%, war support +0.70%, command power +10%, communism +0.10 daily. | Personalizes state around Stalin; propaganda tool. |
| **They Will Know Fear** | Cult of Personality; in defensive war; researched IS Heavy Tank (No Step Back) or IS III (base) | Breakthrough: Land Warfare +100%. 1×100% research bonus for Armor. If No Step Back: Create IS-2 heavy tank on gaining Advanced Heavy Tank Chassis. | Unlocks terror weapon (IS-2 tank). |
| **Freedom of Debate - Unity of Action** | Cult of Personality | Modify Politburo: political power gain +5%, advisor cost −15%, political power +50. Stability +5%, war support +5%. | Permits internal debate while enforcing party unity. |
| **The Construction of Communism** | Freedom of Debate; >0 subject nations | Modify Politburo: same ideology opinion +25%. Every subject: autonomy −100. Railway Moscow to capital of every land-accessible subject (level 1). | Subordinates satellites to USSR; accelerates integration. |
| **Inheritor of the Mantle of Lenin** | Cult of Personality; mutually exclusive with Faithful Servant; 5+ propaganda campaigns | War support +5%. Iosif Stalin gains trait "Inheritor of the Mantle of Lenin": political power gain +10%, justify war goal time −25%. | War-focused Stalin upgrade. |
| **The Faithful Servant of Lenin** | Cult of Personality; mutually exclusive with Inheritor; 5+ propaganda campaigns | Stability +10%. Iosif Stalin gains trait "Faithful Servant of Lenin": guarantee cost −50%, ideology drift defense +15%. | Stability-focused Stalin upgrade. |
| **Brilliant Genius** | Inheritor of Mantle; 10+ propaganda campaigns | National Academies decision cost −50%. Iosif Stalin: research speed +5% (added to Inheritor trait). | Research efficiency bonus. |
| **Leader of the Party and the People** | Requires Inheritor OR Faithful Servant; 10+ propaganda campaigns | Political power +50. Iosif Stalin modifies trait (Inheritor/Faithful): Stability +15%, defensive stability +40%, advisor cost −25%. | Universal leadership consolidation. |
| **Ban Excessive Hero Worship** | Faithful Servant; 10+ propaganda campaigns | Decision cost (Diplomacy) −50%. Iosif Stalin: Stability +15% (on Faithful trait). | Propaganda moderation; reduces cult excesses. |
| **Great Commander** | Inheritor + Leader of Party; mutually exclusive with Architect; 15+ propaganda campaigns | Iosif Stalin gains trait "Great Commander": division recovery +5%, war support +10%, annex cost −10%. Stalin becomes Field Marshal. | Military-focused culmination; field marshal promotion. |
| **Architect of Communism** | Faithful Servant + Leader of Party; mutually exclusive with Great Commander; 15+ propaganda campaigns | Iosif Stalin gains trait "Architect of Communism": puppet cost −20%, master ideology drift +0.10, communism +0.10 daily. | Diplomatic/ideological focus; puppet control. |
| **Father of Nations** | Requires Great Commander OR Architect; 20+ propaganda campaigns | Stalin replaces trait (Heart of Steel → Father of Nations): political power gain −5%, recruitable population +2%, stability +10%, weekly stability +0.10, war support −5%, improve relations +25%, justify war goal −50% (major powers), master impact +0.1, compliance +0.05% daily. | Ultimate trait: combines all bonuses; positions Stalin as patriarch. |

#### The Left Opposition Sub-branch (Trotskyist Path)

Allows civil war leading to Trotsky's takeover; focuses on global revolution & permanent revolution.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The Left Opposition** | Path of Marxism Leninism; mutually exclusive with Centre/Right Opposition; no civil war yet; no purge happened | Political power +75. Starts civil war process (hidden). Event: '[Leader] concerned about Factionalism.' | Triggers conflict with Stalin. |
| **The Fourth International** | Left Opposition; 1+ purge happened; if civil war not started | Political power +120. If Paranoia: increase +10. Event: 'The Fourth International.' | Establishes alternative revolutionary international (vs. Comintern). |
| **Bring Old Trotskyists Back** | Left Opposition; bypass if Radek/Preobrazhensky purged | Karl Radek + Yevgeni Preobrazhensky become available as advisors. If Paranoia: increase +10. | Restores exiled old-guard Trotskyists. |
| **The Committee in Exile** | Fourth International + Bring Old Trotskyists; not civil war started/over | If Paranoia: increase +10. Unlock "Send Supporters Abroad" decision (smuggle sympathizers into exile; cannot be purged; available when civil war starts). | Prepares clandestine exfiltration routes. |
| **Organize the Wreckers** | Left Opposition; no civil war | Political power +50. Unlock decisions to sabotage industry during civil war. | Prepares industrial sabotage campaign. |
| **Eliminate the Right** | Left Opposition; mutually exclusive with Cooperation Against Stalin; no civil war | If Paranoia: increase +30. Nikolay Bukharin, Aleksey Rykov, Mikhail Tomsky become purge targets for Stalin. Modify Factionalism: political power gain +5%. | Turns Stalin's purges against Right Opposition allies. |
| **Integrate Smirnov's Bloc** | Left Opposition; no civil war; secret HQ set up; bypass if Smirnov purged or civil war over | If Paranoia: increase +20. Political power +50. Ivan Smirnov, Ivar Smilga, Aleksandr Shlyapnikov liberated & exiled (safe from purges; join as advisors when civil war starts). Army/navy/air support +5%. Add opposition partisans to 2 random states. | Activates underground resistance network. |
| **Approach Tukhachevsky** | Integrate Smirnov; no civil war; bypass if Tukhachevsky purged/already gone | If Paranoia: increase +10. Mikhail Tukhachevsky sides with Left Opposition in civil war (brings troops & generals). Gains Trotskyist trait, loses Stalinist. 3 random army leaders gain Trotskyist trait. Army/navy/air support +5%/5%/5%. Opposition partisans +1 random state. | Secures one of USSR's best military minds. |
| **Approach Primakov** | Integrate Smirnov; no civil war; bypass if Primakov purged/gone | If Paranoia: increase +10. Vasily Primakov sides with Left Opposition (brings cavalry troops & generals). Gains Trotskyist, loses Stalinist. 2 random army leaders gain Trotskyist. Army/navy/air support +8%/5%/10%. Opposition partisans +1 state. | Secures cavalry expertise. |
| **Funds for the Cause** | Requires Committee in Exile OR Approach Tukhachevsky OR Approach Primakov; no civil war | Logic: every major (& Mexico if not in USSR faction & democratic/communist) receives event 'Soviet Opposition Requests Support.' When civil war starts: adds Foreign Funding spirit (consumer goods −25%) for 365 days. Political power +50. | Foreign aid when civil war begins. |
| **Ignite the Flames** | Requires Tukhachevsky OR Primakov; no civil war. AI: date ≥1940.1.1 | Popular support +1.5%. Army/navy/air support +5% each. Exiled characters become available. Removes Trotskyite Plot? spirit. **Starts Soviet Civil War.** | Triggers actual civil war; commitment point. |
| **Vanguard of the True Revolution** | Funds for Cause + Ignite Flames; civil war started, not over | Every at-peace country with >5% communism gets event 'A Call for International Revolutionary Brigades' (sends volunteers). | Recruits international brigades. |
| **Remove the Counter-Revolutionaries** | Ignite Flames; mutually exclusive with Return Democracy; civil war over | Retires Bukharin, Rykov, Tomsky, Zinovyev, Ryutin, Kalinin, Khrushchev, Merkulov from Union. Removes Factionalism political power modifier. | Purges non-communist opposition after civil war. |
| **The Permanent Revolution** | Committee in Exile + Ignite Flames; civil war over | Unlocks "Organize Fifth Columnists" decisions in hostile European neighbors (trigger uprisings). If Lev Trotsky is leader: gains trait "Triumphant Revolutionary" (subversive activities −50%, justify war goal +15%, ideology drift defense +15%, max command power +50, command power gain +15% daily). | Spreads revolution globally via subversion. |
| **A Global Class Struggle** | Permanent Revolution; <15% surrender | Unlocks "Stir the Proletariat" decisions to destabilize European neighbors & justify war. | Destabilizes Europe. |
| **The Onslaught on Colonialism** | Global Class Struggle; <5% surrender | Unlocks Organize Fifth Columnists & Stir Proletariat in African neighbors. | Exploits anti-colonial movements. |
| **Carry the Revolution East** | Global Class Struggle; <5% surrender | Unlocks Organize Fifth Columnists & Stir Proletariat in Asian neighbors. | Exploits Asian revolutionary potential. |
| **The End of the Imperialist Era** | Requires Onslaught OR Carry East; <5% surrender | Unlocks Organize Fifth Columnists & Stir Proletariat in American & Oceanian neighbors. | Threatens Monroe Doctrine. |
| **Long Live the Workers' Government** | Ignite Flames; civil war over | National spirit (365 days): Factory repair +20%, stability +10%. Political power +100. **Creates 4th International faction.** Removes Ruling Elite from power. | Post-civil-war consolidation; Trotskyist faction forms. |
| **Builder of the Red Army** | Workers' Government; mutually exclusive with Reigniting; Lev Trotsky is leader | Random state: Add 2 slots + 2 military factories. Army experience +50. 2×1 year ahead-of-time reduction for Support Artillery & Infantry. Lev Trotsky becomes Field Marshal. | Trotsky military focus; restores his Red Army leadership. |
| **Reigniting the Revolutionary Spirit** | Workers' Government; mutually exclusive with Builder | National spirit (365 days): Weekly manpower +1000, division attack +15%. | Populist mobilization; emphasizes revolutionary fervor over military hierarchy. |

#### Shared Sub-branches (Left Opposition & Right Opposition access)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Sway the Railway Workers** | Requires Left Opposition OR Right Opposition; no civil war; HQ set up | If Paranoia: increase +5. Add railway & supply hub around HQ state when civil war starts. | Secures logistics infrastructure via worker support. |
| **Infiltrate the NKVD** | Requires Left Opposition OR Right Opposition; no civil war | If Paranoia: decrease −10 (unusual benefit). NKVD forces will join your side in civil war. Unlock "Expand NKVD Military Branch" decision. If Right Opposition completed: increases chance of successful Stalin assassination. | Turns secret police against Stalin. |

#### The Right Opposition Sub-branch (Bucharinist Path)

Leads to Bukharin-led civil war; focuses on economic moderation & NEP (New Economic Policy). Data partially truncated in fetches.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **The Right Opposition** | Path of Marxism Leninism; mutually exclusive with Centre/Left; no civil war; no purge | Political power +75. Starts civil war process (hidden). Event: '[Leader] concerned about Factionalism.' | Triggers conflict; alternative to Trotskyism. |
| *(Additional Right Opposition focuses similar structure to Left Opposition; include Bukharin advisors, NEP economic law, cooperation with Western economies. Data partially incomplete in fetches.)* | — | — | Sub-branch allows for market-oriented socialism under Bukharin; less detailed than Left Opposition in fetched data. |

### Beaten, but not Defeated (Alt-Historical: Monarchist/Fascist/Bucharinist Paths)

Mutually exclusive with **The Path of Marxism Leninism**; requires **No Step Back** DLC for full availability.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| **Beaten, but not Defeated** | Mutually exclusive with Path of Marxism Leninism | Prepares Second Russian Civil War; enables monarchist/fascist/Bucharinist endings. Allows donation of Sakhalin or Vladivostok to Japan for civil war assistance. | Opens 3 alt-historical nation paths. |

#### Reconvene the Zemsky Sobor Sub-branch

Post-civil-war restorations:

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| *(Monarchist path: coronation of Vladimir III as Tsar; restoration of Romanovs; Romanoff Empire)* | — | — | Restores Russian Empire under new Tsar. |
| *(Fascist path: Konstantin Rodzayevsky as leader; fascist state; Tsar as figurehead)* | — | — | Fascist Russian state with retained Tsar. |
| *(Theocratic path: Arch-Patriarch Meletius heads Third Rome; Orthodox theocracy; Vladimir III resign)* | — | — | Unique ecclesiastical autocracy (Third Rome). |

---

## Additional branches

### Transpolar Flights Sub-branch notes

- **Military Engineering University**: Creates forts in strategic defensive locations; relocates industry to the Urals (safer from bombers).

### Army branches notes

**Found the PCDI Branch** gives:
- **Defense Industry** national spirit
- Bonuses to artillery & armor development
- Fort construction via Military Engineering University sub-branch

**Strengthen the Mobilization Plan Branch** gives:
- **The Red Army** national spirit
- Infantry division bonuses

### Naval Branch notes

**Expand the Red Fleet Branch** gives:
- **The Red Fleet** national spirit  
- Modifications to naval spirit
- Bonuses to coastal states

### The Comintern Sub-branch

Handles external politics and alliances; allows:
- Development of Soviet allies in the east
- Political maneuvering with European majors
- Influence campaigns in the Middle East & Far East
- Coordination of Communist parties globally

---

## Key mechanics

- **Political Paranoia**: Active during Stalin's purges (Zinovyevite, Anti-Soviet Trotskyist, Military Conspiracy focuses). Reduces with certain choices; fully removed after Bloc of Rights completion. Affects trait & advisor efficiency.
- **Great Purge**: Automatic & unavoidable when completing purge focuses. Causes army mastery penalties (−5%) if Lessons of War not completed.
- **Five Year Plan spirit**: Base-game starts with "Second Five Year Plan"; modified by industrial branch choices (Reorganize vs. Shift). Replaced with "New Project for National Industrialization" for non-Communists.
- **Wartime locks**: Many industrial focuses (Third through Fourth Five Year Plan, Reorganize/Shift branches) **permanently lock if Soviet Union enters war with a major power** while they are incomplete, forcing choice between industrial development and defense.
- **Civil War paths**: Left Opposition & Right Opposition trigger actual Soviet Civil War if Ignite the Flames is completed; grants factions (4th International for Trotskyists) and exiled character recruitment.
- **DLC gates**: No Step Back required for full alt-historical branches (monarchist, fascist, Bucharinist); base game restricts most choices to Communist path after initial selections.

---

## Cross-reference

See [Soviet Union](../05-countries/soviet-union.md) for the country's 1936 starting profile, starting ideology, initial advisors, and national spirits.

