---
title: Politics, Ideology and Government
category: mechanics
tags: [politics, ideology, government, political power, stability, war support, command power, elections, coup, party popularity, country leader traits]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Ideology
  - https://hoi4.paradoxwikis.com/Government
  - https://hoi4.paradoxwikis.com/Political_parties_and_leaders
  - https://hoi4.paradoxwikis.com/Country_leader_traits
---

## Summary

Every country belongs to one of four **ideology groups** — Democracy, Communism, Fascism, Non-Aligned — each with sub-ideologies, its own diplomacy rules, world-tension thresholds and peace-conference cost modifiers. The ruling party is decided by party popularity: elections, coups and civil wars are the three in-game routes to a change of ruling ideology. Domestic play is driven by four resources: **political power** (base +2/day), **stability**, **war support** and **command power**. Country leaders carry traits that modify all of these.

## The four ideology groups

Ideology **group** (Democracy / Communism / Fascism / Non-Aligned) determines diplomatic rules and occupation options. Ideology **type** (sub-ideology, e.g. Stalinism vs Marxism) is mostly flavour: it gates a handful of alt-history focuses (Communist Italy, Right Opposition USSR, Fascist Poland) and sets opinion:

| Relationship | Opinion modifier |
|---|---|
| Same ruling party (same sub-ideology) | +20 opinion |
| Same ideology group, different sub-ideology | +10 opinion |

### Sub-ideology list

| Group | Sub-ideologies |
|---|---|
| Democracy | Conservatism, Liberalism, Socialism (democratic socialism), Populism |
| Communism | Marxism, Leninism, Stalinism, Anti-Revisionism, Anarchist Communism, Buddhist Socialism |
| Fascism | Nazism, Generic Nazism, Fascism, Falangism, Rexism, Emperor Fascism |
| Non-Aligned | Despotic, Oligarchic, Moderatism, Centrism, Anarchism, Militarism |

Anarchism (Non-Aligned) uses a different ideology icon in the politics/diplomacy view.

### Diplomacy rules by group

| Rule | Democracy | Communism | Fascism | Non-Aligned |
|---|---|---|---|---|
| Declare war on same ideology group without a war goal | No | — | — | — |
| Guarantee other ideologies | Yes | — | — | — |
| Guarantees lower World Tension | Yes | — | — | — |
| Can puppet a country | No | Yes | Yes | Yes |
| Can justify against countries that have generated no World Tension | No | Yes | Yes | Yes |
| Can create/prepare collaboration governments | No | Yes | Yes | Yes |
| Can force another country's government to adopt its ideology | Yes | Yes | Yes | Yes |
| Can send volunteer forces | No | Yes | Yes | No |
| Can host governments in exile | Yes | — | — | — |

Democracies cannot occupy territory owned by neutral countries — it is handed to the owner instead.

### World Tension thresholds by group

Values are the tension required (or the modifier to the requirement) for each action.

| Action | Democracy | Communism | Fascism | Non-Aligned |
|---|---|---|---|---|
| Generate war goal | +100% | — | — | +50% |
| Join faction | +80% (capped at 50% during a defensive war) | requirement −10% | requirement −10% | +40% |
| Send Lend-Lease | +50% | +50% | +50% | +60% |
| Send volunteers | +50% | — | — | +40% |
| Guarantee independence | +25% | — | — | +40% |

### Group modifiers

| Modifier | Democracy | Communism | Fascism | Non-Aligned |
|---|---|---|---|---|
| Civilian intelligence to others | +20% | +10% | +15% | +20% |
| Army intelligence to others | +5% | +7.5% | +10% | +10% |
| Navy intelligence to others | +20% | +12.5% | +10% | +20% |
| Airforce intelligence to others | +5% | +7.5% | +10% | +10% |
| Embargo cost modifier | −50% | — | — | — |
| Embargo threshold factor | +50% | −50% | — | — |
| Impact of war declaration on World Tension | −75% | −25% | — | −75% |
| Impact of joining a faction on World Tension | −90% | −50% | — | −90% |
| Faction trade opinion modifier | +50% | — | — | — |
| Time to justify war while at war with a major power | — | — | −80% | — |
| Ideology drift defence | — | — | — | −30% |

### Peace conference cost modifiers

| Modifier | Democracy | Communism | Fascism |
|---|---|---|---|
| Annex cost | +30% | — | −10% |
| Liberate cost | −10% | +30% | +30% |
| Puppet cost | +20% | −10% | −5% |
| Change ideology on a Fascist country | −10% | — | — |
| Change ideology on a Communist country | −10% | — | — |

Non-Aligned has no peace-conference modifiers.

### Unique occupation laws

| Group | Exclusive occupation law |
|---|---|
| Democracy | Local Autonomy |
| Communism | Liberated Workers |
| Fascism | Brutal Oppression |
| Non-Aligned | none |

See [Civil war and occupation](civil-war-and-occupation.md) for the full occupation law table.

## Starting ideologies (1936 unless noted)

### Democratic
- **Majors — Liberal:** United States, United Kingdom, France. **Socialist:** France (1939).
- **Conservative minors:** Belgium, British Burma, British Malaya, Czechoslovakia, Haiti, Honduras, Ireland, Liberia, Luxembourg, Netherlands, Commonwealth of the Philippines, Romania, South Africa, Spain, Switzerland, Republic of Syria.
- **Liberal minors:** Bolivian Republic, Chile, Colombia, Costa Rica, Cuba, Dominion of Canada, Ecuador (1939), Lebanese Republic, Panama, Iceland, Republic of Paraguay, Uruguay (1939).
- **Socialist minors:** Australia, Denmark, Chile (1939), Cuba (1939), Ecuador, New Zealand, Norway, Sweden.
- **Populist minors:** Second Brazilian Republic.

### Communist
- **Major — Stalinist:** Soviet Union.
- **Marxist minors:** Chinese Soviet Republic, Mongolian People's Republic, Paraguay (1939).
- **Stalinist minors:** Mongolian People's Republic (1939), Sinkiang, Tannu Tuva.

### Fascist
- **Majors:** German Reich (Nazism), Italy (Fascism).
- **Fascist minors:** Dominican Republic, El Salvador, Peru, Siamese Empire (1939), Slovakia (1939), Venezuela.
- **Emperor-Fascist minors:** Manchukuo.

### Non-Aligned
- **Despotic:** Albania, Argentina (with Trial of Allegiance disabled), Austria, Sultanate of Aussa, Bhutan, Brazil (1939), Bulgaria, China, Ethiopia, Kingdom of Greece (1939), Gansu Ma, Guangdong Clique, Guangxi Clique, Guatemala, Hebei-Chahar, Iran, Iraq, Khotan Ma, Mengjiang, Nepal, Ningxia Ma, Nicaragua, Northeastern Army, Sultanate of Muscat and Oman, Paraguay (1939), Portugal, Qinghai Ma, Kingdom of Romania (1939), Saudi Arabia, Shandong Clique, Shanxi, Kingdom of Siam, Nationalist Spain (1939), Tibet, Emirate of Transjordan, Turkey, Uruguay, Xibei San Ma, Yemen, Yugoslavia, Yunnan. (The Chinese warlord clique entries are the No Compromise, No Surrender versions.)
- **Oligarchic:** Kingdom of Afghanistan, Belgian Congo (Götterdämmerung), Dutch East Indies (Thunder at Our Gates), Estonia, Kingdom of Hungary, Latvia, Lithuania, Mandatory Palestine, Poland.
- **Moderate:** Argentina (Trial of Allegiance, or 1939), Mexico.
- **Centrist:** British Raj, Bolivia (1939), Finland, Kingdom of Greece.
- **Militarist:** Japanese Empire.

## Party popularity and changing ideology

Each country tracks popularity for all four ideology groups (summing to 100%). Popularity is moved by ideas/advisors ("daily support" modifiers), focuses, events and decisions, and is resisted by the **ideology drift defence** modifier.

A country can change ruling ideology in four ways:

1. **Election** while another ideology has **more than 50% support** — an event lets power change hands peacefully with no civil war. See Election events.
2. **Coup** (see event table below).
3. **Winning a civil war.** The support level of the challenging ideology decides how many troops and states each side starts with. See [Civil war and occupation](civil-war-and-occupation.md).
4. Console command `set_ruling_party <ideology>`.

### Ideology-drift and coup/civil-war event chain

Appointing an ideology-changing political advisor ("[Ideology] on the Rise") starts the chain. Choosing *Internal support* speeds the coup route; choosing *Popular support* speeds the popularity-growth route.

| Event | Requirements | Mean time to happen | Effects |
|---|---|---|---|
| [Ideology] on the Rise | Fires on appointing an ideology-changing minister | Immediate | Option 1: Internal support — increases chance of a coup. Option 2: Popular support — increases chance of support-increasing events |
| [Ideological] Sympathies in government/military | Minister for that ideology | 500 days (250 if Internal support chosen) | Makes a future coup possible |
| Class Conflicts Divide | At least 20% popularity | 365 days (~182 if Popular support chosen) | +5% popularity, −5% stability |
| Soldiers Desert to Communist Partisans | At least 30% popularity; can only be active once | 365 days (~182 if Popular support chosen) | +5% popularity; until government change: +0.05% popularity/day, −0.20% recruitable population |
| Coup | "Sympathies in government/military" event has happened; not a major and not a puppet. Communism: at least 40% popularity (cannot create a second People's Republic of China). Fascism: at least 30% popularity | 100 days (halved at 50%+ popularity) | Immediately changes the country's ideology; Reign of Terror for two years (+10% political power) |
| The [Month] Revolution (communist) | Minister; at least 40% popularity; cannot create a second People's Republic of China | 365 days (×0.75 if Popular support chosen) | Option 1: civil war with 60% of the country opposed, plus Reign of Terror for two years (+10% political power). Option 2: do nothing |
| Civil War for Fascism | At least 25% popularity | 365 days (×0.75 if Popular support chosen) | Option 1: civil war with 70% of the country opposed (60% if popularity is at least 40%), plus Reign of Terror for two years (+10% political power). Option 2: do nothing |
| Fascist Assault Divisions Form | At least 30% popularity; can only be active once | 365 days (halved if Popular support chosen) | +5% popularity; until government change: +0.05% popularity/day, +0.2% recruitable population, −5% stability |
| The Threat of Communism | At least 25% popularity; at least one neighbouring country is communist | 365 days (halved if Popular support chosen) | +10% popularity |
| [Ideological] Demonstrations | Not a puppet; at least 50% popularity | 30 days | Option 1: Suppress — −10% popularity, −5% revolutionaries. Option 2: Ignore — −5% revolutionaries. Option 3: Allow — government changes, −5% stability |

**Key numeric takeaways:** coups need 40% (communist) / 30% (fascist) popularity and are impossible for majors and puppets; fascist civil-war event fires from 25% popularity; communist revolution event needs 40%; peaceful election takeover needs >50%.

## Elections

Elections run in most Democracies and some Non-Aligned countries, plus Paraguay, El Salvador and Peru at game start. Communist USA, communist/fascist Mexico, fascist Poland and Communist China can gain elections through their focus trees. The gap between elections is country-specific and ranges from **1 to 8 years**; the next election date is shown in the politics and diplomacy tabs. A party with **above 50% popularity** at an election wins and becomes the ruling party. The United States, Spain and Greece have unique national-affair election events.

## Political power

Political power (PP) is the leader's influence over domestic affairs. **Stored PP is capped between −500 and 2000.**

### Generation

Base rate is **+2 per day** on Regular difficulty.

| Difficulty | PP gain modifier |
|---|---|
| Civilian | +50% |
| Recruit | +25% |
| Regular | +0% |
| Veteran | −10% |
| Elite | −15% |

Stability scales PP gain: **−50% at 0% stability, no modifier at 50%, +20% at 100%** stability. (The stability section below lists the same effect as the +10%/−20% bonus/penalty band used in the stability UI tooltip; the wiki quotes both figures.)

> ⚠️ The Government page gives PP gain from stability as −50%…+20%, while its own stability section gives −20%…+10%. Treat the stability-section figures (+10% at 100%, −20% at 0%) as the ones matching the in-game tooltip.

### Spending

| Sink | Cost |
|---|---|
| National focus | 1 PP per day for the focus's duration (typically 70 days) |
| Adding an idea/law/advisor | usually 150 PP (see [Laws and advisors](laws-and-advisors.md) for exact per-law costs) |
| New general or admiral | 5 PP for the first, +5 per commander already owned |
| Justify war goal — Conquest | 50 PP base, +5 if the target has the Neutral Foreign Policy national spirit, +10 PP per extra state added to the claim |
| Justify war goal — Retake core state | 25 PP |
| Guarantee independence | 25 PP for the first, +25 for each subsequent guarantee (25 / 50 / 75 …) |
| Improve relations | 10 PP to start, then 0.2 PP/day (same ideology) or 0.4 PP/day (different ideology) |
| Send attaché | 100 PP (plus 50 command power allocated) |

Decisions sit between focuses and events and can be instantaneous or timed; open the decisions tab with the gavel icon or **Shift+Q**.

### Leaders with PP modifiers (examples)

| Country | Leader | Trait | Modifiers |
|---|---|---|---|
| German Reich | Adolf Hitler | Der Führer | Weekly war support (combat casualties): +0.10%; AI desired divisions factor: +20%; political power gain: +10%; compliance growth speed: −2%; resistance target: +5% |
| Soviet Union | Iosif Stalin | Heart of Steel | Stability: −10%; war support: +5%; political power gain: +5%; improve relations opinion: −5%; autonomy master impact: −0.10 |
| United Kingdom | Edward VIII | Inexperienced Imperialist | Political power gain: −30%; stability: +5%; justify war goal time: −25% |

## Stability

Stability (0–100%) represents popular support for the government. It is rounded down for display and effects (81.6% behaves as 81%), though stored at higher precision.

**Above 50%** — bonuses scale linearly from nothing at 50% to full value at 100%:

| At 100% stability | Value |
|---|---|
| Political power gain | +10% |
| Factory output | +20% |
| Dockyard output | +20% |
| Consumer goods factor | −20% |

**Below 50%** — penalties scale linearly from nothing at 50% to full value at 0%:

| At 0% stability | Value |
|---|---|
| Political power gain | −20% |
| Factory output | −50% |
| Dockyard output | −50% |

Stability also drives **resistance target** in occupied territory: +0% at 100% stability up to **+20% at 0% stability**. While at war, low stability can trigger crises up to and including a civil war.

### Stability modifiers

Total stability = base stability (0–100, moved by events/focuses/decisions) + permanent modifiers, capped to 0–100. Excess from permanent modifiers is not lost — it buffers future negatives.

| Modifier | Value |
|---|---|
| Being at war | −20% |
| War support during war | 0% at 100% war support down to −30% at 0% war support |
| Ruling party popularity | 0% at 0% popularity up to +15% at 100% popularity (raised to up to +25% with the Political Loyalty officer corps spirit) |
| "Popular Figurehead" ruler trait or political advisor | +15% each (they stack) |
| Japan-only ruler modifier | +60% |

Because of the war penalty, a country with 100% base stability, 100% ruling-party popularity and an ongoing war sits at 95% and cannot reach 100% until the war ends.

## War support

War support (0–100%) is the population's willingness to endure war. Many laws and focuses require a war support floor. 50% is neutral.

| At 100% war support | Value |
|---|---|
| Mobilization speed | +30% |
| Army attack on core territory | +10% |
| Army defense on core territory | +10% |
| Command power gain | +50% |

| At 0% war support | Value |
|---|---|
| Mobilization speed | −50% |
| Command power gain | −95% |
| Surrender limit | −30% |
| — | May cause a crisis while at war |

Sources of war support change:

| Source | Value |
|---|---|
| Being in an offensive war | −20% |
| Being in a defensive war | +20% |
| Active attaché in another country | +10% |
| Having a pride of the fleet | +5% |

## Command power

Command power (CP) lets the government bypass the chain of command. **Base cap is 80**; both cap and growth rate are raised by doctrines, national spirits, army officer corps spirits, and by hiring military chiefs and high command. War support scales CP growth (+50% at 100%, −95% at 0%).

| Use | Description | CP cost | Notes |
|---|---|---|---|
| Assign a commander trait | Assign a trait to a commander with an empty trait slot | 15 | Generals, field marshals and admirals alike |
| Hire/promote a general | Promote an officer to general (By Blood Alone renames this to "promote an officer") | 5 per existing general and field marshal | Maximum cost 80 CP |
| Hire an admiral | New admiral to command fleets | 5 per existing admiral | Maximum cost 80 CP |
| Promote a general to field marshal | Enables commanding an army group | 40 | Base cost; modified by personality traits |
| Send attaché | Only while at peace, only to a country at war | 50 | CP stays allocated while the mission runs; also costs 100 PP |
| Air supply mission | Transport planes drop supply (0.01 supply per supply plane at full efficiency) | 0.05 per plane | Allocated while active |
| More Ground Crews | +10% air efficiency in an air zone | 20 per zone | Allocated while active and planes operate there |
| Commander abilities | Temporarily buff troops under a general/field marshal | Variable | Cost scales with total battalions under the ability |

### Attaché

Costs the sender **100 PP + 50 CP** (the CP stays allocated). Only a country at peace may send one, only to a country at war.

Sender receives:
- Military intelligence shared by the receiving country
- 15% of the army, navy and air experience the receiving country generates
- War support +10% (once only)
- If the sender is a puppet of the receiver: daily autonomy +0.05

Receiver gets (not stacking with multiple attachés):
- Division organization +2%
- Planning speed +10%
- If the receiver is the puppet of the sender: daily autonomy −0.05

The AI generally declines attachés from countries whose opinion of it is below +20 (base reluctance −50). Any country at war with the receiver can event-demand recall; refusing costs a variable amount of PP and worsens relations.

**Inferred:** attachés neither raise nor are limited by world tension, so the Spanish Civil War and the Second Sino-Japanese War are cheap, tension-free army/navy/air XP faucets for any country, and the +10% war support helps push democracies into Limited Conscription or Germany into War Economy early.

## Political parties and leaders

Every party is tied to one country leader and one sub-ideology. If the game files define no leader for an ideology, a random one is generated (random leaders can roll 0, 1 or 2 generic traits). Not every country has unique party names for all four ideologies. Full per-country party lists live on the wiki's *Political parties and leaders* page (and *Political parties and leaders (releasable countries)*); the country files in `05-countries/` carry the per-nation detail. The starting popularity split for the seven majors:

| Country | Ruling leader (1936) | Sub-ideology | Party | Popularity of the other parties at start |
|---|---|---|---|---|
| German Reich | Adolf Hitler (Der Führer) | Nazism | NSDAP — 40% | Zentrum (Conservatism, Konrad Adenauer) 35%; DNVP (Despotic, generic) 15%; KPD (Stalinism, Wilhelm Pieck) 10% |
| Soviet Union | Iosif Stalin (Heart of Steel) | Stalinism | VKP(B) — 88% | Trudoviks (Socialism, Aleksandr Kerensky) 10%; VFP (Fascism, Konstantin Rodzaevsky) 2%; Non-Aligned 0% |
| United Kingdom | Stanley Baldwin (Conservative Grandee) | Liberalism | Conservative Party — 97% | BUF (Fascism, Oswald Mosley) 2%; CPGB (Stalinism, Harry Pollitt) 1%; House of Windsor (Centrism) 0% |
| France | Pierre Laval (Tenacious Negotiator) | Liberalism | Parti Radical — 64% | PCF (Stalinism, Maurice Thorez) 30%; Action Française (Centrism, Charles Maurras) 15%; Mouvement Franciste (Nazism, Marcel Bucard) 1% |
| United States | Franklin Delano Roosevelt (Dislikes Germany) | Liberalism | Democratic Party — 98% | CPUSA (Marxism, Earl Browder) 1%; Silver Legion (Fascism, William Dudley Pelley) 1%; Non-Aligned 0% |
| Italy | Benito Mussolini (Il Duce) | Fascism | PNF — 76% | PPI (Socialism, Comitato di Liberazione Nazionale) 22%; PNM (Despotic, Vittorio Emanuele III) 5%; PCI (Marxism, Palmiro Togliatti) 2% |
| Japanese Empire | Keisuke Okada (Moderate Politician) | Militarism | Kyokoku Itchi Naikaku — 40% | Kokumin Dōmei (Fascism, Kenzō Adachi) 35%; Rikken Minseitō (Liberalism, Tetsu Katayama) 23%; JCP/Kōza-ha (Marxism, Kyuichi Tokuda) 2% |

Notable alternate leaders and how they take power (majors):

| Country | Leader | Route to power | Trait(s) |
|---|---|---|---|
| German Reich | Heinrich Himmler / Hermann Göring | Oster Conspiracy chain, the Himmler-Putsch, Hitler Found Dead, or focus The True Successor | — |
| German Reich | Wilhelm II | Focus Military Dictatorship | Anti-Democrat, Imperial Connections |
| German Reich | Wilhelm III | Focus Return of the Kaiser | Popular Figurehead |
| Soviet Union | Lev Trotsky | Event The Soviet Civil War after focus The Left Opposition | Permanent Revolutionary |
| Soviet Union | Lavrenty Beriya | Event The Death of Stalin | Unscrupulous Orchestrator |
| Soviet Union | Nikolay Bukharin / Aleksey Rykov | Soviet Civil War or Army Arrests Lavrenty Beria after focus The Right Opposition | Defender of the Peasantry / Organizer of Labor and Defense |
| United Kingdom | Winston Churchill | Event Chamberlain Resigns or focus Motion of No Confidence | British Bulldog |
| United Kingdom | Neville Chamberlain | Event Stanley Baldwin resigns | Appeaser, Rearmer |
| United Kingdom | Edward VIII | Focus King's Party | Inexperienced Imperialist |
| France | Léon Blum | Focus Form the Popular Front | Reluctant Interventionist, Stout Defender |
| France | Charles de Gaulle | Event French Armistice after German victory | — |
| France | Philippe Pétain | Event French Armistice after German victory | — |
| United States | Harry S. Truman | Event Roosevelt Passes Away | — |
| United States | Douglas MacArthur | 1944 elections (if he campaigned), or decision Constitutional Convention for the fascist path | American Caesar |
| Italy | Italo Balbo / Dino Grandi | Focus Italo Balbo / focus Dino Grandi | Aviation Hero / Silver Tongue |
| Italy | The Grand Council of Fascism | Focus Depose Mussolini | The Grand Council |
| Italy | Vittorio Emanuele III | Focus Monarchia d'Italia, German focus Assassinate Mussolini, or the monarchist civil war | The Soldier King |
| Japan | Hirohito | Focus Empower the Emperor or focus The Chrysanthemum Throne | Emperor Showa |
| Japan | Hideki Tojo | Focus Tojo's Premiership | IJA Prime Minister |
| Japan | Fumimaro Konoe | Focus Konoe's First Cabinet (Militarist) or The Imperial Rule Assistance Association (Emperor Fascist) | Noble Prime Minister |

## Country leader traits

A leader may hold one or several traits; traits give country-wide modifiers, and some only change AI behaviour. Randomly generated leaders roll 0–2 of the **generic** traits below; scripted leaders may also hold one.

### Generic traits

| Trait | Effect |
|---|---|
| Armaments Organizer | Civilian to Military factory conversion cost: -20% Supply Hub construction speed: +10% |
| Captain of Industry | Civilian factory construction speed: +10% Infrastructure construction speed: +10% Railway construction speed: +10% Synthetic refinery construction speed: +10% |
| Compassionate Gentleman | Improve relations opinion: +25% Compliance Growth Speed: +2% Resistance Target: -5% Stability: +5.00% |
| Deal Broker | Trade Laws Cost: -25% Conscription Laws Cost: -25% Economy Laws Cost: -25% |
| Eager Collaborator | Max volunteer force divisions: +2 Improve relations maintain cost: -100% Acceptance of Fascist Diplomacy: +75 |
| Economist | Production efficiency cap: +5% Consumer Goods Factories factor: -5% |
| Editor | Political Power Gain: +5% Stability: +5.00% |
| Financial Expert | Consumer Goods Factories factor: -15% |
| Fortification Engineer | Land fort construction speed: +20% Coastal fort construction speed: +20% Anti-air construction speed: +20% |
| Hawk | War support: +10.00% Stability: -5.00% Justify War goal time: -10% |
| Humble Appeaser | War support: -5.00% Stability: +10.00% |
| Ideological Crusader | Same ideology monthly opinion: +100% Party Popularity Stability Modifier: +10% |
| Nation Builder | Political Power Gain: +10% Stability: +5.00% Improve relations opinion: +5% |
| National Integralist | Political Power Gain: +15% Weekly Stability: +0.10% |
| Quartermaster General | Air base construction speed: +15% Naval base construction speed: +15% Rocket site construction speed: +15% Radar station construction speed: +15% Nuclear reactor construction speed: +15% |
| Reluctant Interventionist | Stability: +5.00% Lend-lease tension limit: -20% Lend-lease request tension limit: -20% |
| Retired Officer | War support: +5.00% High Command Cost: -25% Air Chief Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% |
| Silent Workhorse | Political Power Gain: +15% |
| Smooth-Talking Charmer | Improve relations maintain cost: -50% Trade deal opinion factor: +10% Political Power Gain: +5% |
| Tenacious Negotiator | Political Power Gain: +10% Trade deal opinion factor: +25% |
| University Rector | Research Speed: +10.00% |
| Vengeful Industrialist | Civilian factory construction speed: +10% Infrastructure construction speed: +10% Military factory construction speed: +10% Daily Fascism Support: +0.01 War support: +5.00% |
| War Industrialist | Military factory construction speed: +10% Naval dockyard construction speed: +10% Fuel silo construction speed: +10% |

### Unique traits

Only specific leaders can hold these, from game start or via focuses, decisions and events.

| Trait | Effect |
|---|---|
| Dictator | Political Power Gain: +25% Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% |
| Warrior Code | Political Power Gain: +5% AI Modifier: Call Ally Desire: -40 AI Modifier: Join Ally Desire: -30 |
| Underage Monarch | Stability: +10.00% Political Advisor Cost: +25% Trade Laws Cost: +25% Conscription Laws Cost: +25% Economy Laws Cost: +25% |
| Legitimate Heir | Stability: +10.00% Political Power Gain: +10% |
| Collaborator King | Daily Fascism Support: +0.10 Acceptance of Fascist Diplomacy: +75 Political Power Gain: +10% |
| Imperial Sanction | ( China)Generate War goal tension limit against country: +75% ( The Chinese Soviet Republic)Generate War goal tension limit against country: +75% ( Shanxi)Generate War goal tension limit against country: +75% ( The Guangxi Clique)Generate War goal tension limit against country: +75% ( Yunnan)Generate War goal tension limit against country: +75% ( Qinghai Ma)Generate War goal tension limit against country: +75% ( Sinkiang)Generate War goal tension limit against country: +75% |
| Emperor Shōwa | Stability: +60.00% |
| Stout Defender | AI Modifier: Focus on Defense: +50% |
| Warmonger | AI Modifier: Focus on Offense: +50% |
| Inexperienced Imperialist | Political Power Gain: -30% Stability: +5.00% Justify War goal time: -25% |
| Inexperienced Socialist | Political Power Gain: -15% Stability: +5.00% Daily Communism Support: +0.06 |
| The Strongman of Tibet | War support: +5.00% Stability: +5.00% Daily Fascism Support: +0.05 |
| Autocratic Imperialist | War support: +5.00% Stability: +5.00% Justify War goal time: -25% |
| Cabinet Crisis | Political Power Gain: -50% Stability: -10.00% |
| Unpopular Monarch | Political Power Gain: -30% Stability: -20.00% |
| Socialite Connections | Trade Laws Cost: -25% Economy Laws Cost: -25% Factory output: +10% |
| Her Majesty Queen Wallis, First of Her Name, by the Grace of God Queen of the Americas, Grand Admiral of the Royal American Navy, Duchess of Wallington, Duchess of Manhattan, Duchess of Long Island, Countess of Orange, Countess of O'ahu, Marquise of New Orleans, Baroness of Springfield, Baroness of Hollywood, Baroness of Central Park, Grand Socialite, Protector of Liberty, Northwest Vanguard of Alaska, Avenger of the Boston Tea Party, Terror of Wallington, D.C. | Daily Support for Unaligned: +0.05 |
| Inexperienced Monarch | Political Advisor Cost: +25% Trade Laws Cost: +25% Conscription Laws Cost: +25% Economy Laws Cost: +25% High Command Cost: +25% Air Chief Cost: +25% Army Chief Cost: +25% Navy Chief Cost: +25% |
| Headstrong | Political Power Gain: +15% |
| Popular Queen | Stability: +15.00% Factory output: +5% Dockyard output: +5% |
| Stammer | Political Power Gain: -10% |
| Humble | Daily Support for Unaligned: +0.05 Consumer Goods Factories factor: -15% |
| British Bulldog | War support: +10.00% Political Power Gain: +5% |
| Appeaser | War support: -5.00% |
| Rearmer | Factory output: +5% |
| Conservative Grandee | Political Power Gain: +5% Political Advisor Cost: -10% |
| Famous Aviator | Tactical Bomber: Range: +5% Fighter: Range: +5% |
| Spirit Of Genghis | Cavalry Attack: +10% Naval Bomber: Range: +10% Naval Attack: +10% |
| Noble Ulanqab Intellectual | Research Speed: +5.00% Consumer Goods Factories factor: -10% Political Power Gain: -5% |
| Borjigin Descendant | Cavalry Attack: +5% War support: +10.00% Justify War goal time: -15% |
| Nationalist Education Enthusiast | Research Speed: +10.00% War support: +5.00% |
| Expert Unifier | Compliance Growth Speed: +2% Political Power Gain: +5% |
| The Dutch Nobleman | Stability: -5.00% Consumer Goods Factories factor: -10% |
| Defender of the Homeland | Division Defense on core territory: +10% |
| Idealist Revolutionary | Stability: +10.00% Political Power Gain: +5% War support: -5.00% |
| King Father | Stability: +10.00% War support: +5.00% |
| King of Luang Prabang | Stability: +5.00% Political Power Gain: +5% |
| The Emperor of the Purple Forbidden City | Political Power Gain: +15% |
| Rebellious Republican | Daily Democracy Support: +0.06 War support: +10.00% |
| Champion of the Lao Issara | Daily Democracy Support: +0.06 War support: +5.00% Stability: +5.00% |
| Head of the Khmer Issarak | Daily Communism Support: +0.06 Justify War goal time: -15% Political Power Gain: +5% |
| The Vietnamese Third Way | Daily Fascism Support: +0.02 Justify War goal time: -10% Political Power Gain: +5% |
| The Red Prince (LAO) | Daily Communism Support: +0.06 Stability: +10.00% |
| Renowned Revolutionary Poet | Daily Communism Support: +0.10 Stability: +10.00% War support: +10.00% |
| Chairman of the Inner Mongolian People's Revolutionary Party | Daily Communism Support: +0.10 Recruitable population Factor: +5% War support: +10.00% |
| Pan-Mongolian Stalinist | Daily Communism Support: +0.05 Recruitable population Factor: +5% War support: +10.00% Justify War goal time: -10% |
| The Dragon King | Stability: +10.00% Recruitable population Factor: +5% Division Defense on core territory: +10% |
| Socialist Revolutionary | Daily Communism Support: +0.05 Political Power Gain: +10% War support: +10.00% |
| Social Reformer | Daily Support for Unaligned: +0.02 Political Power Gain: +10% War support: +10.00% |
| Figurehead Emperor | Political Power Gain: +10% Stability: +10.00% Daily Support for Unaligned: +0.10 Research Speed: +5.00% |
| Duban | Recruitable population Factor: +5% |
| The King of Sinkiang | Recruitable population Factor: +10% Ideology drift defense: +50% Division Defense on core territory: +5% Justify War goal time: -15% |
| Turncoat Revolutionary | Acceptance of Communist Diplomacy: -40 War support: +5.00% |
| The Wild Horse | War support: +5.00% Cavalry Attack: +10% Cavalry Defense: +10% |
| Tulku | Justify War goal time on us: +10% Party Popularity Stability Modifier: +10% |
| Taoist Devotee | Stability: +10.00% War support: +10.00% |
| Governor of Sinkiang | Political Power Gain: +10% Construction Speed: +5% |
| Champion Father of the Faithful | Political Power Gain: +10% Construction Speed: +5% War support: +10.00% Division Attack: +10% Division Defense: +10% |
| Ghazi | Division Attack: +5% Division Defense: +5% |
| The Bandit Warlord | Equipment Capture Ratio Modifier: +2% War support: +5.00% Stability: -5.00% Division Attrition: -5% |
| Governor of Sichuan | Acceptance of Communist Diplomacy: -40 Political Power Gain: +10% Construction Speed: +5% Division Attack: +3% |
| Fierce Leader | Surrender Limit: +15% Division Defense on core territory: +10% |
| King of the Southern Skies | Air Superiority Mission Efficiency: +5% Night Operations Penalty: -5% Air Support Mission Efficiency: +5% Air experience Gain: +0.10 daily |
| King of Yunnan | Construction Speed: +10% Daily Political Power Gain: +0.10 Resource Gain Efficiency: +10% |
| Reckless Commander | Division Attack: +3% Org Loss when Moving: -5% Divisions speed: +3% |
| Model Governor | Division Defense on core territory: +10% Construction Speed: +5% Division Attack on core territory: +5% |
| Unreliable Opportunist | Political Power Gain: +10% Divisions speed: +3% Division Defense on core territory: -5% |
| Proven Loyalty | Political Power Gain: +10% Divisions speed: +3% Division Defense on core territory: +5% Division Attack on core territory: +5% |
| Traitor Warlord | Political Power Gain: -10% Divisions speed: +5% Division Attack: +5% Division Defense on core territory: +3% |
| King of Ningxia | Division Attack on core territory: +8% Division Defense on core territory: +8% Acceptance of Fascist Diplomacy: -40 Acceptance of Communist Diplomacy: -40 |
| Staunch Anti-Communist | Acceptance of Communist Diplomacy: -40 Daily Communism Support: -0.10 Division Attack: +3% |
| Devout Leader | Political Power Gain: +5% Stability: +5.00% |
| Padishah | Acceptance of Communist Diplomacy: -40 Division Attack: +3% |
| Emir of Khotan | Acceptance of Communist Diplomacy: -50 Division Defense on core territory: +5% War support: +5.00% |
| Young Marshall | Stability: -10.00% Defensive War Penalty Stability Modifier: +30.00% |
| Popular Governor | Stability: +5.00% Political Power Gain: +10% Improve relations maintain cost: -10% |
| Loyal Warlord | Acceptance of Communist Diplomacy: -40 War support: +5.00% Cavalry Attack: +5% Cavalry Defense: +5% |
| Rikken Minseitō Leader | Stability: +10.00% Political Power Gain: +10% Daily Democracy Support: +0.05 Civilian factory construction speed: +5% |
| Military Prime Minister | Daily Support for Unaligned: +0.05 Land Doctrine Cost: -10% Army experience Gain: +0.03 daily Political Power Gain: -10% |
| Noble Prime Minister | War support: +5.00% Political Power Gain: +10% |
| IJA Prime Minister | Daily Fascism Support: +0.05 Land Doctrine Cost: -10% Division Defense on core territory: +5% Stability: -5.00% |
| IJN Prime Minister | Daily Fascism Support: +0.05 Naval Doctrine Cost: -15% Base Strike (grand doctrine) Mastery gain: +15.00% War support: +5.00% |
| Diplomatic Prime Minister | Stability: +5.00% War support: -5.00% Political Power Gain: +5% Acceptance of Democratic Diplomacy: +15 |
| Emperor Shōwa (2) | Ideology drift defense: +20% Stability: +5.00% War support: +5.00% Political Power Gain: +5% |
| Emperor Genka | War support: +10.00% Political Power Gain: +10% Justify War goal time: -10% |
| Sesshō | War support: +5.00% Political Power Gain: +5% Stability: +5.00% |
| Tōhōkai Leader | Daily Fascism Support: +0.10 War support: +10.00% Recruitable population Factor: +5% |
| Nichiren Marxist | Stability: +10.00% War support: -10.00% Political Power Gain: +10% Justify War goal time: -25% |
| First Chairman of the Japanese Communist Party | Political Power Gain: +15% Ideology drift defense: +30% |
| First Secretary of the Japanese Communist Party | Political Power Gain: +5% Daily Communism Support: +0.04 |
| Sōtō | Political Power Gain: +10% Army experience Gain: +10% |
| Meiji's True Successor | Construction Speed: +5% Research Speed: +2.00% |
| The Heavenly Sovereign | Justify War goal time: -15% Stability: +5.00% War support: +5.00% Recruitable population Factor: +5% |
| Guided by Amaterasu | Justify War goal time: -15% Stability: +5.00% War support: +5.00% Recruitable population Factor: +5% |
| Embodying Empress Jingū | Justify War goal time: -20% Political Power Gain: +5% War support: +10.00% Recruitable population Factor: +10% Generate War goal tension limit: -50% |
| Embodying Empress Jingū (and Zheng Yi Sao) | Navy experience Gain: +0.20 daily Convoy Raiding Efficiency: +20% Dockyard output: +15% Naval dockyard construction speed: +10% Justify War goal time: -20% Political Power Gain: +5% War support: +10.00% Recruitable population Factor: +10% Generate War goal tension limit: -50% |
| Staunch Traditionalist | Division Attack: +5% Division Defense: +5% Naval Doctrine Cost: +10% Air Doctrine Cost: +10% Research Speed: -2.00% |
| Protector of the Eternal Empire | Division Attack on core territory: +5% Division Defense on core territory: +5% Division Recovery Rate: +5% Division Organization: +5% |
| Governor-General of Korea | Resistance Target: -5% Daily Democracy Support: -0.02 Daily Communism Support: -0.02 Stability: -10.00% |
| Japanese Puppet | Stability: -5.00% Daily Fascism Support: +0.02 |
| His Highness King Yi of Changdeokgung | War support: +10.00% Recruitable population: +2.00% |
| Unam | Resistance Target: -10% Stability: -5.00% Political Power Gain: +10% |
| Mongyang | War support: -5.00% Stability: +10.00% Political Power Gain: +5% |
| Suryong | Recruitable population Factor: +10% War support: +5.00% Daily Communism Support: +0.10 |
| Moderate Politician (Non-Aligned) | Acceptance of Democratic Diplomacy: +20 Ideology drift defense: -15% War support: -5.00% Political Power Gain: +10% |
| Moderate Politician (Democratic) | Daily Democracy Support: +0.02 Stability: -5.00% War support: -5.00% Political Power Gain: +10% |
| Socialist Politician (JAP) | Daily Democracy Support: +0.03 Daily Communism Support: +0.03 War support: -5.00% Political Power Gain: +10% |
| Shakai Taishūtō Leader | Daily Democracy Support: +0.05 Daily Communism Support: +0.03 Political Power Gain: +10% Production efficiency growth: +5% Stability: +5.00% |
| Popular Diplomat | Daily Democracy Support: +0.05 War support: -5.00% Stability: +5.00% Political Power Gain: +10% |
| The Tokugawa Heir | Daily Democracy Support: +0.05 War support: -5.00% Stability: +5.00% Political Power Gain: +15% |
| Rikken Seiyūkai Leader | Daily Democracy Support: +0.05 War support: +5.00% Political Power Gain: +5% Military factory construction speed: +5% |
| Jimintō Leader | Daily Democracy Support: +0.10 War support: +10.00% Political Power Gain: +10% Military factory construction speed: +5% |
| Moderate Navy Leader | Daily Democracy Support: +0.05 War support: +10.00% Navy experience Gain: +0.05 daily Naval dockyard construction speed: +10% |
| Anti-Communist Prime Minister | Acceptance of Fascist Diplomacy: +20 War support: -5.00% Political Power Gain: +5% Stability: +5.00% Daily Communism Support: -0.03 |
| Indomitable Perseverance | Division Recovery Rate: +4% |
| Generalissimo | Defensive War Penalty Stability Modifier: +40.00% AI Modifier: Desired Divisions Factor: +5% |
| Blue Shirt Connections /(0) | War support: +5.00% Stability: +5.00% Daily Fascism Support: +0.02 |
| Blue Shirt Connections /(1) | War support: +5.00% Stability: +5.00% Daily Fascism Support: +0.05 |
| Leader of the Chinese Brotherhood | War support: +5.00% Political Power Gain: +5% Daily Fascism Support: +0.05 |
| Great Architect | Construction Speed: +1% |
| Dislikes Germany | The AI will be more likely to antagonize Germany. |
| Dislikes the USSR | The AI will be more likely to antagonize the Soviet Union. |
| Likes Germany | The AI will be more likely to ally Germany. |
| Likes Mexico | The AI will be more likely to ally Mexico. |
| Likes the Allies | The AI will be more likely to antagonize the UK, France and USA. |
| Master Maneuverer | Political Power Gain: +15% |
| Staunch Constitutionalist | Ideology drift defense: +50% |
| First Lady of the Republic | War support: +5.00% Stability: +5.00% |
| Cornered Fox | Division Defense: +15% Division Recovery Rate: +10% |
| Permanent Revolutionary | Political Power Gain: -15% Justify War goal time: +15% Subversive activities cost: -30% Maximum Command power Increase: +30 |
| Triumphant Revolutionary | Justify War goal time: +15% Subversive activities cost: -50% Maximum Command power Increase: +50 Ideology drift defense: +15% Daily Command power Gain Multiplier: +15% |
| Exiled Revolutionary | Subversive activities cost: -50% Ideology drift defense: +30% |
| Railroad Enthusiast | Railway construction speed: +25% |
| Strongman of San Luis Potosí | Division Recovery Rate: +5% Political Power Gain: +10% |
| Revolutionary General | Resistance Growth Speed in our states occupied by the enemy: +25% Conscription Laws Cost: -25% Economy Laws Cost: -25% Theorist Cost: -25% |
| Fascist Militia Leader | War support: +5.00% |
| Cristero General | Recruitable population: +1.00% |
| Primate of México | Stability: +5.00% |
| El Jefe Máximo | Political Advisor Cost: -25% Political Power Gain: +10% |
| Protector of the Campesinos | Civilian factory construction speed: +10% Infrastructure construction speed: +10% |
| Refounder of México | Stability: +5.00% Trade deal opinion factor: +20% |
| The Gentleman President | Stability: +5.00% Improve relations maintain cost: -50% |
| Conservative Nationalist | Stability: +10.00% Infrastructure construction speed: +20% |
| Conservative Nationalist /(LaR) | Weekly Stability: +0.50% Infrastructure construction speed: +20% |
| The Silver President | Consumer Goods Factories factor: -15% Acceptance of Fascist Diplomacy: +50 |
| The Dean of Mexican Marxism | Stability: +5.00% Factory output: +10% |
| Staunch Stalinist | Factory output: +10% Ideology drift defense: +15% |
| Devoted Trotskyist | War support: +5.00% Subversive activities cost: -25% |
| Fascist Sympathies | Acceptance of Fascist Diplomacy: +70 |
| Anti-Communist | Acceptance of Communist Diplomacy: -50 Daily Communism Support: -0.01 |
| Camarilla Leader | Political Advisor Cost: -25% Trade Laws Cost: -25% Conscription Laws Cost: -25% Economy Laws Cost: -25% High Command Cost: -25% Air Chief Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% |
| Hedonist | Stability: -5.00% |
| Constitutional Monarch | Weekly Stability: +1.00% Daily Political Power Gain: +0.10 |
| Duke of Orléans | Daily Support for Unaligned: +0.10 |
| Count of Paris | Max Factories in a State: +5% |
| Reluctant Veteran | War support: +5.00% Recruitable population Factor: +5% |
| Proletariat Internationalist | War support: +5.00% Non-core Manpower: +2.50% |
| Anti-Democrat | Acceptance of Democratic Diplomacy: -50 Daily Democracy Support: -0.02 Stability: +10.00% |
| Emergency Powers | Daily Political Power Gain: +0.50 |
| Popular Figurehead (2) | Stability: +5.00% |
| Popular Figurehead (3) | Stability: +10.00% |
| American Caesar | High Command Cost: -25% Air Chief Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% Division Attack on core territory: +10% Division Defense on core territory: +10% |
| Great War Hero | War support: +5.00% Stability: +5.00% Division Attack on core territory: +10% Division Defense on core territory: +10% Division Recovery Rate: +5% |
| Oberkommando der Marine | Fleet Coordination: +15% Ship Recovery Rate: +10.0% Navy experience Gain: +0.08 daily Division Organization: -5% |
| Burggraf und Graf zu Dohna-Schlobitten | Division Attack on core territory: +5% Division Defense on core territory: +5% Division Recovery Rate: +5% |
| Fürst von Pless, Graf von Hochberg, Freiherr zu Fürstenstein | Division Attack on core territory: +5% Division Defense on core territory: +5% Stability: +10.00% |
| The Sword of Islam | War support: +5.00% Weekly Manpower: +100 Division Recovery Rate: +5% |
| Imperial Connections | Political Power Gain: -10% Improve relations opinion: -15% Political Advisor Cost: -25% Trade Laws Cost: -25% Conscription Laws Cost: -25% Economy Laws Cost: -25% High Command Cost: -25% Air Chief Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% |
| Oberster Kriegsherr | Conscription Laws Cost: -25% High Command Cost: -25% Air Chief Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% |
| Kaiserin of the People | Weekly Stability: +0.10% Stability: +5.00% War support: +5.00% Division Defense on core territory: +10% Political Power Gain: +15% |
| Victoria III | Stability: +5.00% |
| Incognito | Daily Fascism Support: +0.10 Ideology drift defense: +15% |
| Nationalist Symbol | War support: +5.00% Stability: +5.00% Division Attack on core territory: +10% Division Defense on core territory: +10% |
| Champion of Peace (1) | War support: -30.00% Generate War goal tension limit: +100% |
| Champion of Peace (2) | War support: -24.00% Generate War goal tension limit: +80% |
| Champion of Peace (3) | War support: -18.00% Generate War goal tension limit: +60% |
| Champion of Peace (4) | War support: -12.00% Generate War goal tension limit: +40% |
| Champion of Peace (5) | War support: -6.00% Generate War goal tension limit: +20% |
| Economic Reformer | Trade Laws Cost: -33% Economy Laws Cost: -33% Consumer Goods Factories factor: -15% |
| Strict Austerity Adherent | Stability: -15.00% Economy Laws Cost: +50% Consumer Goods Factories factor: -30% |
| Defeatist | War support: -10.00% Surrender Limit: -25% |
| Little Churchill | War support: +5.00% Resistance Growth Speed in our states occupied by the enemy: +15% |
| Wilhelmina | Stability: +15.00% |
| Disdain for Politicians (1) | Political Power Gain: +5% Daily Communism Support: -0.01 Daily Fascism Support: -0.01 Daily Democracy Support: -0.01 |
| Disdain for Politicians (2) | Political Power Gain: +10% Daily Communism Support: -0.02 Daily Fascism Support: -0.02 Daily Democracy Support: -0.02 |
| Queen of the People | War support: +10.00% Resistance Target in our states occupied by the enemy +25% |
| Leider | War support: +10.00% Acceptance of Fascist Diplomacy: +50 |
| Comintern Workhorse | Same ideology monthly opinion: +100% Subversive activities cost: -50% |
| Veteran Communist | Stability: +5.00% Factory output: +5% |
| Indecisive | Stability: +5.00% Political Power Gain: -5% |
| Figurehead President | Stability: -5.00% Political Power Gain: +5% |
| Great Survivor | Stability: +10.00% Mobilization speed: +15% |
| El Director | Planning Speed: -10% Max planning: +10% Division Attack on core territory: +15% Division Defense on core territory: +15% |
| Sins of the Father | Military factory construction speed: +10% Daily Political Power Gain: -0.10 High Command Cost: -34% Air Chief Cost: -34% Army Chief Cost: -34% Navy Chief Cost: -34% |
| Empire Builder | War support: +5.00% Justify War goal time: -25% |
| Jefe | War support: +5.00% |
| Caudillo (1) | Damage to Garrisons: -15% High Command Cost: -15% |
| Caudillo (2) | Damage to Garrisons: -15% High Command Cost: -15% Maximum Command power Increase: +20 Daily Command power Gain Multiplier: +25% |
| Lion of the Rif | War support: +10.00% Division Organization: +5% |
| The Sacred King | Stability: +10.00% |
| Disgraced Monarch | Consumer Goods Factories factor: -15% Stability: -10.00% |
| The Legitimist | Stability: +5.00% War support: +5.00% |
| Divided Interests | Division Attack on core territory: +5% Division Defense on core territory: -5% Research Speed: -10.00% |
| Our Right to Survive | War support: +10.00% Division Defense on core territory: +10% |
| Anarchist Zeal | Daily Support for Unaligned: +0.05 War support: +10.00% Minimum training level: -10% |
| Militant Socialist | War support: +5.00% ( The Soviet Union)Attack bonus against country: +10% ( The Soviet Union)Defense bonus against country: +10% |
| Constitutional Monarch (Minor) | Weekly Stability: +0.50% Daily Political Power Gain: +0.10 |
| Arkhigos | Daily Communism Support: -0.02 Daily Democracy Support: -0.02 Acceptance of Fascist Diplomacy: +35 Division Defense on core territory: +5% |
| Divisive Absolute Monarch | Stability: -10.00% Political Advisor Cost: -15% High Command Cost: -15% Air Chief Cost: -15% Army Chief Cost: -15% Navy Chief Cost: -15% |
| Royal Puppet | Daily Support for Unaligned: +0.02 Weekly Stability: -3.00% |
| Elected Monarchist Puppet | Stability: -5.00% |
| Ethnarch | Stability: +10.00% War support: +15.00% Daily Political Power Gain: +0.15 Political Advisor Cost: -25% |
| Professional Crisis Solver | Stability: +5.00% Daily Political Power Gain: +0.05 |
| The Banker | Stability: +5.00% Economy Laws Cost: -33% Consumer Goods Factories factor: -10% Acceptance of Democratic Diplomacy: +50 Acceptance of Fascist Diplomacy: -25 Acceptance of Communist Diplomacy: -25 |
| The Young Magnate | Civilian factory construction speed: +10% Railway construction speed: +10% Synthetic refinery construction speed: +10% Trade deal opinion factor: +25% Acceptance of Democratic Diplomacy: +25 |
| Polemarch | War support: +5.00% Justify War goal time: -15% |
| Likes Turkey | The AI will be more likely to ally Turkey. |
| Archon | Daily Political Power Gain: +0.15 Justify War goal time: -25% AI Modifier: Focus on Offense: +50% AI Modifier: Desire to be in or expand a faction: -90 |
| Autokratōr | Daily Political Power Gain: +0.15 War support: +10.00% Justify War goal time: -50% AI Modifier: Focus on Offense: +50% AI Modifier: Desire to be in or expand a faction: -100 |
| Basileus | Daily Political Power Gain: +0.25 War support: +10.00% Conscription Laws Cost: -25% Military Leader Cost: -20% Justify War goal time: -50% AI Modifier: Focus on Offense: +50% AI Modifier: Desire to be in or expand a faction: -100 |
| Father of the Turks | Stability: +30.00% Political Advisor Cost: -30% High Command Cost: -30% Air Chief Cost: -30% Army Chief Cost: -30% Navy Chief Cost: -30% Conscription Laws Cost: -25% Economy Laws Cost: -25% |
| Father of the Turks (1) | Stability: +30.00% Political Advisor Cost: -22% High Command Cost: -22% Air Chief Cost: -22% Army Chief Cost: -22% Navy Chief Cost: -22% Conscription Laws Cost: -18% Economy Laws Cost: -18% |
| Father of the Turks (2) | Stability: +30.00% Political Advisor Cost: -15% High Command Cost: -15% Air Chief Cost: -15% Army Chief Cost: -15% Navy Chief Cost: -15% Conscription Laws Cost: -12% Economy Laws Cost: -12% |
| Father of the Turks (3) | Stability: +30.00% Political Advisor Cost: -8% High Command Cost: -8% Air Chief Cost: -8% Army Chief Cost: -8% Navy Chief Cost: -8% Conscription Laws Cost: -5% Economy Laws Cost: -5% |
| Father of the Turks (4) | Stability: +30.00% |
| The Absentee President | Political Power Gain: -30% |
| Infirm | Political Power Gain: -25% Political Advisor Cost: +25% High Command Cost: +25% Air Chief Cost: +25% Army Chief Cost: +25% Navy Chief Cost: +25% Conscription Laws Cost: +25% Economy Laws Cost: +25% |
| Gentle Scholar | Stability: +15.00% War support: -10.00% Political Advisor Cost: -25% High Command Cost: -15% Air Chief Cost: -15% Army Chief Cost: -15% Navy Chief Cost: -15% |
| Caliph | War support: +25.00% Weekly Manpower: +1250 Mobilization speed: +25% |
| Calipha | War support: +20.00% Weekly Manpower: +2000 Mobilization speed: +25% |
| The First Ottoman Sultana | Stability: +15.00% War support: +10.00% Daily Compliance Gain: +0.01% Political Advisor Cost: -33% High Command Cost: -33% Air Chief Cost: -33% Army Chief Cost: -33% Navy Chief Cost: -33% |
| Crown Regent | Stability: +15.00% Political Power Gain: -15% |
| Mareşal | Political Power Gain: +5% War support: +10.00% Mobilization speed: +10% Division Attack on core territory: +5% |
| Millî Şef | Stability: +10.00% Justify War goal time on us: +200% Ideology drift defense: +25% Division Defense on core territory: +5% |
| Man of the Nation | Stability: +10.00% Daily Political Power Gain: +0.05 Political Advisor Cost: -15% |
| Liberal Democratic Paragon | Daily Political Power Gain: +0.05 Ideology drift defense: +33% Improve relations opinion: +25% Trade deal opinion factor: +25% |
| The Statist | Consumer Goods Factories factor: -10% Political Power Gain: +10% Military factory construction speed: +5% Civilian factory construction speed: +5% |
| The Academic | Consumer Goods Factories factor: -10% Political Power Gain: +10% Factory output: +5% Production efficiency growth: +5% |
| Celebrity Junta Leader | Stability: +15.00% Political Power Gain: -15% |
| Reluctant Stalinist | War support: +10.00% Factory output: +10% Civilian to Military factory conversion cost: -25% |
| The Humbled Knyaz | Political Power Gain: -30% Stability: -10.00% |
| Freedom Fighter | Stability: +25.00% War support: +15.00% Division Defense on core territory: +10% |
| Experienced Insurgent | War support: +15.00% Maximum Command power Increase: +25 Daily Command power Gain Multiplier: +25% Defensive War Penalty Stability Modifier: +40.00% |
| Liberal Corporatist | Infrastructure construction speed: +10% Ideology drift defense: +15% Research Speed: +2.00% |
| Father of the Canadian Welfare State | Civilian factory construction speed: +5% Stability: +10.00% |
| The Canadian Führer | Political Power Gain: +15% War support: +5.00% Daily Fascism Support: +0.02 |
| Counter Insurgency Expert | Required Garrisons: -25% Damage to Garrisons: -15% Recruitable population: +0.20% |
| Pioneer of the Canadian Social Gospel | Mobilization speed: +15% Stability: +5.00% Daily Communism Support: +0.02 Daily Support for Unaligned: +0.02 |
| Grey Wolf | War support: +15.00% Conscription Laws Cost: -30% Justify War goal time: -50% Recruitable population: +1.00% |
| Tsar Unifier | War support: -10.00% Daily Support for Unaligned: +0.05 Ideology drift defense: +25% |
| The Old Coup-Maker | Civilian factory construction speed: +10% Research Speed: +5.00% War support: +10.00% Stability: -10.00% |
| Dreams of a New Byzantium | War support: +10.00% Stability: -10.00% Offensive War Penalty Stability Modifier: +20.00% Justify War goal time: -15% Generate War goal tension limit: -50% Master impact: -0.15 Extra military and civilian factories from subjects: +40% |
| The Bloody Professor | Master Ideology Drift: +0.10 War support: +5.00% Mobilization speed: +10% Daily Fascism Support: +0.10 Foreign subversive activities efficiency: -50% Weekly Stability: -0.20% Justify War goal time: -35% |
| Hardened Officer | Recruitable population Factor: +5% Division Defense on core territory: +5% Entrenchment speed: +5% Max Entrenchment: +5 |
| Incompetent Leader | Political Power Gain: -15% |
| No Designated Regency | Political Power Gain: -5% Stability: -10.00% Ideology drift defense: -25% Political Advisor Cost: +15% |
| The Hero of the Leipzig Trials | Political Power Gain: +15% Political Advisor Cost: -10% Daily Communism Support: +0.10 Justify War goal time on us: +25% Improve relations opinion: +15% Same ideology monthly opinion: +30% |
| Political Manipulator | Political Power Gain: +10% Join faction tension limit: -25% Acceptance of Fascist Diplomacy: +50 Improve relations maintain cost: -50% |
| Elected Regency Council | Political Power Gain: +5% Stability: +10.00% Political Advisor Cost: -10% |
| Elected Regency Council (Pro-Axis) | Political Power Gain: +5% Stability: +10.00% Political Advisor Cost: -10% Acceptance of Fascist Diplomacy: +50 |
| Elected Regency Council (Pro-Allies) | Political Power Gain: +5% Stability: +10.00% Political Advisor Cost: -10% Acceptance of Democratic Diplomacy: +50 |
| Tsankov heads the Regency Council | Master Ideology Drift: +0.10 War support: +5.00% Mobilization speed: +10% Daily Fascism Support: +0.10 Foreign subversive activities efficiency: -50% Weekly Stability: -0.20% Justify War goal time: -35% |
| Lukov heads the Regency Council | Recruitable population Factor: +5% Division Defense on core territory: +5% Entrenchment speed: +5% Max Entrenchment: +5 |
| Filov heads the Regency Council | Political Power Gain: +10% Join faction tension limit: -25% Acceptance of Fascist Diplomacy: +50 Improve relations maintain cost: -50% |
| Mushanov heads the Regency Council | War support: -5.00% Stability: +10.00% |
| Nazi Sympathizer | Daily Fascism Support: +0.10 Same ideology monthly opinion: +75% |
| Grand Duchess of Luxembourg | Daily Support for Unaligned: +0.12 Stability: +10.00% War support: +10.00% |
| By the Conquering Lion of the Tribe of Judah,His Imperial Majesty Haile Selassie I, King of Kings, Lord of Lords, Elect of God(1) | Ideology drift defense: +10% Political Power Gain: +5% Mobilization speed: +5% |
| By the Conquering Lion of the Tribe of Judah,His Imperial Majesty Haile Selassie I, King of Kings, Lord of Lords, Elect of God(2) | Ideology drift defense: +10% Political Power Gain: +10% Mobilization speed: +5% Stability: +5.00% |
| By the Conquering Lion of the Tribe of Judah,His Imperial Majesty Haile Selassie I, King of Kings, Lord of Lords, Elect of God(3a) | Ideology drift defense: +10% Political Power Gain: +10% Mobilization speed: +5% Stability: +10.00% Puppet cost: -10% Maximum Command power Increase Multiplier: +10% Guarantee tension limit: -20% |
| By the Conquering Lion of the Tribe of Judah,His Imperial Majesty Haile Selassie I, King of Kings, Lord of Lords, Elect of God(3b) | Ideology drift defense: +10% Political Power Gain: +10% Mobilization speed: +5% Stability: +5.00% Recruitable population Factor: +5% Daily Compliance Gain: +0.10% Justify War goal time on us: +25% |
| By the Conquering Lion of the Tribe of Judah,His Imperial Majesty Haile Selassie I, King of Kings, Lord of Lords, Elect of God(4) | Ideology drift defense: +10% Political Power Gain: +10% Mobilization speed: +5% Stability: +10.00% Puppet cost: -10% Maximum Command power Increase Multiplier: +10% Guarantee tension limit: -20% Recruitable population Factor: +5% Daily Compliance Gain: +0.10% Justify War goal time on us: +25% |
| Imperator Absentis | Surrender Limit: -20% Political Power Gain: +5% |
| God of the Rastafari | Compliance Growth Speed: +20% Daily Compliance Gain: +0.01% Stability: +10.00% Ideology drift defense: +50% |
| The Crowned Adder | Stability: -15.00% Improve relations opinion: -40% Division Attack on core territory: +15% Acceptance of Unaligned Diplomacy: +30 |
| The Crowned Adder (2) | Improve relations opinion: -20% Division Attack on core territory: +15% Acceptance of Unaligned Diplomacy: +30 |
| The Tainted Ras | Production efficiency growth: -10% Consumer Goods Factories factor: +10% Equipment Capture Ratio Modifier: +25% Acceptance of Unaligned Diplomacy: +30 |
| The Tainted Ras (2) | Production efficiency growth: -10% Consumer Goods Factories factor: +10% Equipment Capture Ratio Modifier: +25% Acceptance of Unaligned Diplomacy: +30 Stability: +5.00% |
| Inexperienced Sultan | Stability: -10.00% Daily Political Power Cost: +0.30 Justify War goal time: -30% Acceptance of Unaligned Diplomacy: +30 |
| Inexperienced Sultan (2) | Stability: +5.00% Justify War goal time: -30% Acceptance of Unaligned Diplomacy: +30 |
| Gallant Doctor | Ideology drift defense: +10% Mobilization speed: +5% Political Power Gain: +10% |
| The Red Ras | Division Defense on core territory: +5% Political Power Gain: +10% Daily Democracy Support: +0.10 |
| King of Ethiopia | Stability: +10.00% Political Power Gain: -5% Political Advisor Cost: -25% |
| Liberator of Jimma | Stability: +10.00% Daily Political Power Cost: -0.10 Justify War goal time: -30% Acceptance of Unaligned Diplomacy: +30 Political Power Gain: +10% |
| Liberator of Ethiopia | Division Attack on core territory: +15% Acceptance of Unaligned Diplomacy: +30 Political Power Gain: +10% Stability: +10.00% |
| Liberator of Gojjam | Consumer Goods Factories factor: +20% Equipment Capture Ratio Modifier: +25% Acceptance of Unaligned Diplomacy: +30 Stability: +10.00% Political Power Gain: +10% |
| Anarcho-Communism | Surrender Limit: +20% Division Defense on core territory: +15% Stability: -5.00% Mobilization speed: +5% |
| Revolutionary Council | Surrender Limit: +20% Division Attack on core territory: +15% War support: +10.00% Recruitable population Factor: +5% |
| The Rich Sultan | Factory output: +5% Consumer Goods Factories factor: +10% Political Power Gain: +10% |
| Il Duce | Political Power Gain: +10% Maximum Command power Increase Multiplier: -10% Economy, Trade and Conscription Laws Cost: -15% |
| Il Duce (Providence) | Political Power Gain: +15% Maximum Command power Increase Multiplier: -10% Stability: +5.00% Economy, Trade and Conscription Laws Cost: -15% |
| Il Duce (Strengthen) | Political Power Gain: +15% Maximum Command power Increase Multiplier: -10% Ideology drift defense: +10% Recruitable population Factor: +10% Daily Fascism Support: +0.10 Economy, Trade and Conscription Laws Cost: -15% |
| Il Duce (Providence + Strengthen) | Political Power Gain: +15% Maximum Command power Increase Multiplier: -10% Stability: +5.00% Ideology drift defense: +10% Recruitable population Factor: +10% Daily Fascism Support: +0.10 Economy, Trade and Conscription Laws Cost: -15% |
| Il Duce (Devotion) | Political Power Gain: +15% Maximum Command power Increase Multiplier: -10% Stability: +10.00% Ideology drift defense: +15% Recruitable population Factor: +15% Daily Fascism Support: +0.10 Economy, Trade and Conscription Laws Cost: -15% |
| Il Duce (Heroes) | Political Power Gain: +15% Stability: +10.00% Ideology drift defense: +15% Recruitable population Factor: +15% Daily Fascism Support: +0.10 Economy, Trade and Conscription Laws Cost: -15% |
| Lion Tamer | Party Popularity Stability Modifier: +10% Surrender Limit: +5% Damage to Garrisons: -15% |
| Lion Tamer (2) | Party Popularity Stability Modifier: +10% Surrender Limit: +5% Damage to Garrisons: -15% War support: +5.00% Offensive War Penalty Stability Modifier: +10.00% |
| Capo Supremo | Subject Manpower requirement: +15% Master impact: -0.15 Puppet cost: -10% Militia Organization: +10% |
| Minister of Foreign Affairs (Ad Interim) | Improve relations opinion: +7% Damage to Garrisons: -7% |
| Minister of Justice (Ad Interim) | Improve relations maintain cost: -25% Resistance Decay Speed: +2% |
| Minister of Education (Ad Interim) | Research Speed: +1.00% Stability: +2.00% |
| Minister of Corporations (Ad Interim) | Factory output: +2% Dockyard output: +2% |
| The Soldier King | Daily Command power Gain Multiplier: +5% Stability: +5.00% Army experience Gain: +5% |
| King of Albania | Stability: +2.00% Party Popularity Stability Modifier: +10% Compliance Growth Speed: +10% Non-core Manpower: +2.50% |
| Emperor of Ethiopia | Stability: +2.00% Party Popularity Stability Modifier: +10% Compliance Growth Speed: +10% Non-core Manpower: +2.50% |
| Eager Commander | Maximum Command power Increase Multiplier: +15% Daily Command power Gain Multiplier: +10% Stability: +5.00% Army experience Gain: +5% |
| Supreme Pontiff | Improve relations opinion: +25% Justify War goal time: -25% |
| Temperamental | Improve relations opinion: -35% Justify War goal time: -25% Commander Abilities Cost: -15% Master impact: -0.50 |
| Grand Master of the Equestrian Order of the Holy Sepulcher of Jerusalem | Cavalry Attack: +10% Division Organization: +3% Maximum Command power Increase Multiplier: +25% Political Power Gain: -10% |
| Master of Politics | Party Popularity Stability Modifier: +15% Political Power Gain: +10% Consumer Goods Factories factor: -5% |
| Resistance Leader | Political Power Gain: +10% Damage to Enemy Garrisons in our states occupied by the enemy: +10% Resistance Target in our states occupied by the enemy +10% Resistance Decay Speed in our states occupied by the enemy: -10% High Command Cost: -25% |
| Moderate Reformist | Political Advisor Cost: -25% Stability: +10.00% Consumer Goods Factories factor: -10% |
| Anti-Fascist Committee | Political Power Gain: -30% Factory output: +10% Dockyard output: +10% |
| Indisposed Political Scientist | Daily Communism Support: +0.05 Stability: +5.00% Political Power Gain: -5% Antonio Gramsci needs time to recover from his severe illness, this trait will be significantly improved in the future. |
| Cultural Hegemony Theorist | Daily Communism Support: +0.10 Stability: +10.00% Political Power Gain: +10% Research Speed: +3.00% Daily Compliance Gain: +0.05% Surrender Limit: +10% |
| Conservative Communist | Political Power Gain: +10% Acceptance of Democratic Diplomacy: +50 Stability: +10.00% War support: -5.00% |
| Staunch Anti-Fascist | Same ideology monthly opinion: +25% War support: +10.00% Political Power Gain: +10% |
| The Grand Council | Political Power Gain: -1% Stability: -5.00% |
| Aviation Hero | Political Power Gain: +5% Daily Fascism Support: +0.05 Air Research Speed: +5% |
| Military Modernizer | Air Doctrine Cost: -15% Land Doctrine Cost: -15% Coordination: +2% Daily Command power Gain: +0.10 |
| Silver Tongue | Improve relations opinion: +20% Improve relations maintain cost: -20% Justify War goal time: -15% Foreign subversive activities efficiency: -10% |
| Silver Tongue (No LaR) | Improve relations opinion: +20% Improve relations maintain cost: -20% Justify War goal time: -15% |
| Father of the Empire | Political Power Gain: +5% Daily Fascism Support: +0.05 Recruitable population Factor: +10% |
| Political Reformer (1) | All Advisors Cost: -25% |
| Political Reformer (2, no LaR) | Ideology drift defense: +5% Research Speed: +2.50% All Advisors Cost: -25% |
| Political Reformer (2) | Ideology drift defense: +5% Research Speed: +2.50% Operative slots: +1 All Advisors Cost: -25% |
| Tomislav II, King of Croatia | Stability: -25.00% Political Power Gain: +15% Fleet Coordination: +20% Breakthrough against minor countries: +30% |
| The Fascist Lawyer | Daily Political Power Gain: +0.25 Consumer Goods Factories factor: -10% Puppet cost: -40% |
| Head of the National Committee | War support: +10.00% Mountaineers Attack: +10% Mountaineers Speed: +10% Mountaineers Organization: +15% |
| Third Duke of Aosta | Political Power Gain: +10% War support: +5.00% Daily Command power Gain: +0.05 |
| Viceroy of Africa Orientale Italiana | Required Garrisons: -10% Daily Compliance Gain: +0.10% |
| The Iron Duke | Resistance Growth Speed: -15% Damage to Garrisons: -10% |
| Duke of Calabria and Castro | Political Power Gain: +10% War support: +5.00% Daily Command power Gain: +0.05 |
| Commander in Chief | Army experience Gain: +0.40 daily Division Defense: +15% Daily Command power Gain: +0.07 |
| Popular Dictator | Division Defense: +15% Division Attack: +10% War support: +15.00% Stability: +10.00% |
| Radical Democrat | Daily Democracy Support: +0.07 Civilian factory construction speed: +10% |
| Democratic Capitalist | Daily Democracy Support: +0.03 Construction Speed: +5% |
| Cantonal Conservative | Party Popularity Stability Modifier: +10% Daily Political Power Gain: +0.10 Daily Democracy Support: +0.05 |
| Anarchist | Daily Communism Support: +0.05 |
| Trade Unionist (SWI) | Daily Communism Support: +0.05 Production efficiency cap: +5% Lack of Resources Penalty: -30% |
| Fascist Appeaser | Daily Fascism Support: +0.03 Improve relations opinion: +20% Surrender Limit: -10% |
| Fascist | Daily Fascism Support: +0.07 Stability: -10.00% War support: +10.00% |
| Fascist Propagandist | Daily Fascism Support: +0.07 War support: +15.00% |
| Fascist Recruiter | Daily Fascism Support: +0.07 Stability: -10.00% War support: +10.00% Recruitable population Factor: +10% |
| Corporatist | Daily Democracy Support: -0.05 Surrender Limit: -10% Improve relations opinion: -10% Daily Political Power Gain: +0.30 |
| Social Democrat | Daily Political Power Gain: +0.10 Stability: +5.00% Daily Communism Support: +0.03 Daily Democracy Support: +0.05 |
| Socialist Pacifist | Daily Communism Support: +0.05 War support: -20.00% Daily Political Power Gain: +0.25 Stability: +5.00% |
| Pragmatic Democrat | Daily Democracy Support: +0.05 Stability: +10.00% |
| Conservative Democrat | Daily Democracy Support: +0.05 Political Power Gain: -10% Stability: +5.00% |
| Militaristic Democrat | Daily Democracy Support: +0.03 Daily Command power Gain: +0.07 |
| Militaristic Nationalist | Daily Support for Unaligned: +0.05 War support: +10.00% Improve relations opinion: -10% Surrender Limit: +20% |
| Nationalistic Industrialist | Daily Support for Unaligned: +0.07 Lack of Resources Penalty: -30% War support: +10.00% |
| Soviet Spy | Intel network strength gain factor: +20% Daily Communism Support: +0.05 War support: +10.00% |
| Diplomat | Improve relations opinion: +30% Trade deal opinion factor: +50% Ideology drift defense: +20% Intel network strength gain factor: +15% |
| Intelligence Officer | Agency upgrade time: -15% Decryption: +10% Army Intelligence: +30% Operative slots: +1 |
| Humanitarian | Daily Democracy Support: +0.05 War support: -15.00% Join faction tension limit: -15% Civilian Intelligence: +15% Political Power Gain: +50% |
| Weapons Designer | Production efficiency cap: +10% Daily Support for Unaligned: +0.03 Materiel Military Industrial Organization cost: -75% Research Speed: +10.00% |
| Socialist Politician | Political Power Gain: +5% Party Popularity Stability Modifier: +10% Political Advisor Cost: -15% Conscription Laws Cost: +10% Trade Laws Cost: -10% |
| Liberal Politician | Party Popularity Stability Modifier: +5% Political Advisor Cost: -15% Consumer Goods Factories factor: -10% Economy Laws Cost: +15% Trade Laws Cost: -15% |
| Communist Politician | Political Power Gain: +5% Party Popularity Stability Modifier: +5% Trade Laws Cost: -10% Consumer Goods Factories factor: -20% Recruitable population: +1.50% |
| Conservative Politician | War support: +10.00% Military factory construction speed: +5% Conscription Laws Cost: -10% Recruitable population: +2.50% All Military Advisors Cost: -15% |
| Right-wing Populist | Political Power Gain: +5% Party Popularity Stability Modifier: +10% War support: +5.00% Monthly Population: +5% Conscription Laws Cost: +15% Economy Laws Cost: -10% Trade Laws Cost: -10% Recruitable population: +1.50% |
| Sovereign of Elefantordenen | Party Popularity Stability Modifier: +5% War support: +5.00% Conscription Laws Cost: -10% Economy Laws Cost: -10% Trade Laws Cost: +15% Recruitable population: +2.50% All Military Advisors Cost: -15% |
| Fascist Militarist | War support: +10.00% Military factory construction speed: +5% Conscription Laws Cost: -10% Economy Laws Cost: -10% Trade Laws Cost: +15% Recruitable population: +1.50% All Military Advisors Cost: -10% |
| Fascist Populist | Political Power Gain: +5% Party Popularity Stability Modifier: +10% War support: +10.00% Conscription Laws Cost: -10% Economy Laws Cost: -10% Trade Laws Cost: +15% Recruitable population: +1.50% |
| Political Unity | Conscription Laws Cost: -10% Economy Laws Cost: -10% Trade Laws Cost: -10% Recruitable population: +2.50% Weekly War support (Combat Casualties): +0.10% Weekly War support (Enemy Bombing): +0.10% Weekly War support (Sunk Convoys): +0.10% All Advisors Cost: -25% |
| Overlords Plenipotentiary | Political Power Gain: -5% Conscription Laws Cost: +5% Economy Laws Cost: +5% Trade Laws Cost: +5% Consumer Goods Factories factor: -10% Weekly Balance of Power Change: -0.50% Master Ideology Drift: +0.01 |
| Kokoomus Policies | Consumer Goods Factories factor: -10% |
| Member of the Suojeluskunta | Minimum Surrender Limit: +15.00% Stability: -5.00% Ideology drift defense: +15% |
| Member of the Suojeluskunta (Improved) | Minimum Surrender Limit: +30.00% Stability: -5.00% Ideology drift defense: +25% Justify War goal time when at war with a major: -35% Maximum Command power Increase Multiplier: +25% |
| Paasikivi Doctrine | War support: -5.00% Stability: +5.00% Improve relations maintain cost: -10% Acceptance of Democratic Diplomacy: +50 Acceptance of Communist Diplomacy: +50 |
| Paasikivi Doctrine (Improved) | War support: -5.00% Stability: +10.00% Improve relations maintain cost: -20% Acceptance of Democratic Diplomacy: +50 Acceptance of Communist Diplomacy: +50 Daily Compliance Gain: +0.10% Research Speed: +10.00% |
| Backed by Political Coalition | Political Power Gain: +10% Political Advisor Cost: -25% Trade Laws Cost: -25% Economy Laws Cost: -25% |
| White Liberal | Political Power Gain: +5% Production efficiency cap: +5% Daily Support for Unaligned: +0.05 |
| White Liberal (Improved) | Political Power Gain: +10% Production efficiency cap: +10% Daily Support for Unaligned: +0.10 |
| Expansionist Policies | Generate War goal tension limit: -25% Justify War goal time: -25% Reduced cost for Take States action on Soviet cores in Peace Conferences. |
| Sotamarsalkka | Recruitable population: +1.00% War support: +5.00% Stability: -5.00% Defensive War Penalty Stability Modifier: +10.00% |
| Sotamarsalkka (Improved) | Recruitable population: +2.00% War support: +10.00% Stability: -5.00% Defensive War Penalty Stability Modifier: +20.00% |
| Architect of Finnish Corporatism | Trade Laws Cost: -33% Economy Laws Cost: -33% Consumer Goods Factories factor: -15% Max Factories in a State: +1 Construction Speed: +15% |
| Pragmatic Socialist | War support: -5.00% Party Popularity Stability Modifier: +10% Political Advisor Cost: -20% Acceptance of Communist Diplomacy: -35 |
| Champion of National Cooperation | Party Popularity Stability Modifier: +20% Political Advisor Cost: -20% Acceptance of Communist Diplomacy: -70 Conscription Laws Cost: -33% Economy Laws Cost: -33% Recruitable population: +2.00% |
| Committed Anti-Fascist | Same ideology monthly opinion: +25% Max volunteer force divisions: +2 Agency upgrade time: -15% Ideology drift defense: +50% |
| Unbreakable Anti-Fascist | Same ideology monthly opinion: +25% Max volunteer force divisions: +4 Agency upgrade time: -30% Ideology drift defense: +50% Root Out Resistance mission effects: +20% War support: +10.00% |
| Committed Anti-Fascist (No LaR) | Same ideology monthly opinion: +25% Max volunteer force divisions: +2 Foreign subversive activities efficiency: -15% Ideology drift defense: +50% |
| Unbreakable Anti-Fascist (No LaR) | Same ideology monthly opinion: +25% Max volunteer force divisions: +4 Foreign subversive activities efficiency: -30% Ideology drift defense: +50% Subversive activities cost: -20% War support: +10.00% |
| Devoted Communist | Factory output: +10% Resistance Activity Chance: -10% Daily Compliance Gain: +0.05% |
| Stalin's Puppet | Construction Speed: +10% Finnish goods will flow to the Soviet Union, granting them temporary bonuses to Consumer Goods and Supply. |
| International Communist | Same ideology monthly opinion: +100% Subversive activities cost: -50% Recruitable population: +2.00% War support: +5.00% |
| Crown Prince of Finland | Acceptance of Fascist Diplomacy: +75 Political Power Gain: +10% Stability: +5.00% Daily Support for Unaligned: +0.10 Recruitable population: +2.50% Reduced cost for Take States action in Peace Conferences. Cost for Estonian cores is further reduced. |
| Grandpa Väinämöinen | Consumer Goods Factories factor: -15% Required Garrisons: -30% |
| Tribal Warrior | Divisions speed: +5% Org Loss when Moving: -15% Initiative: +4% |
| Veteran Guerrilla Fighter | War support: +10.00% Recruitable population Factor: +15% Division Defense on core territory: +10% |
| Committee Against the Finnish White Terror | Breakthrough against minor countries: +6% |
| Supporting party in power | Political Advisor Cost: +25% Economy Laws Cost: +25% Trade Laws Cost: +25% Conscription Laws Cost: +25% |
| Minor opposition party in power | Stability: -5.00% |
| Rearmament Proponent | War support: +5.00% Infantry Equipment: Production cost: -5.00% |
| Rearmament Adherent | War support: +10.00% Infantry Equipment: Production cost: -10.00% |
| Chaos and confusion | Political Power Gain: -25% |
| Solidified Mandate | Political Power Gain: +5% Trade Laws Cost: -10% Economy Laws Cost: -15% Stability: +2.50% |
| Mandate of the people | Political Power Gain: +10% Trade Laws Cost: -20% Economy Laws Cost: -30% Stability: +5.00% |
| Admiral of industry | Civilian factory construction speed: +17% Infrastructure construction speed: +17% Railway construction speed: +17% Synthetic refinery construction speed: +17% |
| Close ties to the military | Maximum Command power Increase: +30 Training time: -10% |
| Landsfader | Division Defense on core territory: +6% Division Attack on core territory: +6% Supply Combat Penalties on Core Territory: -8% |
| Respectful occupier | Resistance Target: -10% Resistance Growth Speed: -15% Resistance Activity Chance: -20% |
| Education for all | Research Speed: +6.00% |
| Every barrel counts | Supply Consumption: -5% Air Fuel Consumption: -5% Navy Fuel Consumption: -5% |
| Reluctant towards Rearmament | Conscription Laws Cost: +15% War support: -5.00% |
| High Defense Budget | Recruitable population: +2.00% |
| Former Autocrat | Political Power Gain: -10% Acceptance of Fascist Diplomacy: +20 Acceptance of Unaligned Diplomacy: +20 Daily Support for Unaligned: +0.01 Daily Command power Gain Multiplier: +15% |
| The Great | Max training: +15% Division Experience Gain: +15% Experienced soldier losses: -25% Recruitable population: +2.00% Non-core Manpower: +2.00% |
| The Eternal | Max training: +15% Division Experience Gain: +15% Experienced soldier losses: -25% Recruitable population: +3.00% Non-core Manpower: +2.00% Resistance Target: -5% Damage to Garrisons: -10% |
| The Spider | Land Night Attack: +10% Night Operations Penalty: -10% Night-time Attack: +10% |
| Untethered | Divisions speed: +10% Org Loss when Moving: -10% |
| Mild Mannered (No LaR) | Trade deal opinion factor: +20% Improve relations maintain cost: -25% Subversive activities cost: -25% |
| Mild Mannered | Trade deal opinion factor: +20% Improve relations maintain cost: -25% Own operative capture chance: -5% |
| Unbreakable | No Entrenchment Lose On Attack: yes Division Attack: -5% Division Defense: +15% |
| Hyena | Equipment Capture Ratio Modifier: +10% |
| Lucky | Reinforce Rate: +2% Chance to score Critical Hit: +10% Chance to Receive Critical Hit: -10% |
| Amnesiac | Rocket Damage: +15% Political Power Gain: -10% Planning Speed: -20% Coordination: -20% |
| Trusty (No LaR) | Trade deal opinion factor: +20% Improve relations opinion: +0.25 Foreign subversive activities efficiency: +30% |
| Trusty | Trade deal opinion factor: +20% Improve relations opinion: +0.25 Stage Coup effectiveness: +25% Infiltration effectiveness: +25% Strengthen Resistance effectiveness: +35% Sabotage Industry effectiveness: +35% Sabotage Resources effectiveness: +35% Sabotage Infrastructure effectiveness: +35% |
| Hot Tempered Reformer | Stability: -5.00% Political Power Gain: +10% Daily Democracy Support: +0.01 |
| National Romanticist | Justify War goal time: -10% Ideology drift defense: +25% |
| Revolutionary Educator | Party Popularity Stability Modifier: +15% Research Speed: +10.00% |
| The Strict Regent | Political Power Gain: -15% Stability: +10.00% Factory output: +5% |
| Independence Advocate | Daily Autonomy progress gain: +0.10 All Autonomy gain: +20% Party Popularity Stability Modifier: +15% |
| The Navy King | Naval Doctrine Cost: -10% Navy experience Gain: +20% |
| Transportation Enthusiast | Train: Production cost: -15.00% Truck: Production cost: -15.00% |
| Anti-Stalinist Marxist | Acceptance of Communist Diplomacy: -20 Trade deal opinion factor: +10% Justify War goal time: -10% |
| Minister of Education | Research Speed: +6.00% |
| Minister of Education (Upgraded) | Research Speed: +10.00% Political Power Gain: +5% |
| Popular Figurehead (AFG) | Stability: +10.00% Daily Support for Unaligned: +0.02 Political Power Gain: +5% |
| Cautious Modernizer | Stability: +10.00% Infrastructure construction speed: +10% Acceptance of Fascist Diplomacy: +50 Acceptance of Democratic Diplomacy: -50 |
| The Red Prince (AFG) | Daily Communism Support: +0.01 Daily Democracy Support: +0.02 Acceptance of Communist Diplomacy: +50 War support: +10.00% |
| Continuity Prime Minister | Stability: +10.00% Infrastructure construction speed: +5% Construction Speed: +5% |
| Reactionary Prime Minister | Stability: -10.00% Division Defense on core territory: +10% Recruitable population Factor: +5% |
| The Radical Monarch | Justify War goal time: -25% Production efficiency cap: +5% Defensive War Penalty Stability Modifier: +10.00% |
| Savior of the Holy Lands | Stability: +20.00% War Penalty Stability Modifier: +30.00% Division Defense on core territory: +10% |
| Sovereign of the Ascendancy | Political Power Gain: +20% Damage to Garrisons: -10% Justify War goal time: -50% Stability: +20.00% |
| He Who Puts His Faith in God | Political Power Gain: +20% Stability: +5.00% Daily Support for Unaligned: +0.03 |
| Follower of Islam | Division Defense on core territory: +10% Division Attack on core territory: +10% Stability: +5.00% |
| Last of the Bukharans | Division Defense on core territory: +5% Division Attack on core territory: +5% Political Power Gain: -5% Recruitable population Factor: +5% |
| Caliph /(AFG) | Division Defense on core territory: +5% Division Attack on core territory: +5% Political Power Gain: +10% Weekly Manpower: +500 |
| Legacy of the Durrani | Division Attack: +5% Division Defense: +5% Recruitable population: +1.50% Resistance Target: -5% |
| Diminished Authority | Political Power Gain: -20% Stability: +5.00% Research Speed: -3.00% |
| Iranian Revanchist | War support: +10.00% War Penalty Stability Modifier: +10.00% Justify War goal time: -25% Generate War goal tension limit: -25% |
| Fascist Dynasty | War support: +10.00% Political Power Gain: +5% Daily Fascism Support: +0.03 |
| Temporary Government | Political Power Gain: -10% War Penalty Stability Modifier: +10.00% Political Advisor Cost: +50% |
| General Secretary | Daily Communism Support: +0.03 Research Speed: +2.00% Division Defense on core territory: +10% Division Attack on core territory: +5% |
| The Golden Emir | Daily Support for Unaligned: +0.03 Daily Fascism Support: +0.03 Research Speed: -2.00% Division Defense on core territory: +5% Division Attack on core territory: +5% Recruitable population Factor: +5% |
| Comrade Fahd | Daily Communism Support: +0.05 Division Defense on core territory: +10% |
| Bismarck of the Arabs | Political Power Gain: +10% Stability: +5.00% Ideology drift defense: +15% |
| The Military Sheikh | Division Defense on core territory: +15% Cavalry Attack: +10% Cavalry Defense: +10% Recruitable population: +2.00% |
| Emir of Transjordan | Stability: +10.00% Political Power Gain: +5% |
| Experienced High Commissioner | Infrastructure construction speed: +10% Political Power Gain: +5% |
| Arab-Fascist Adherent | Political Power Gain: +10% War support: +5.00% |
| Pro-Western Iraqi Nationalist | Daily Democracy Support: +0.05 Stability: +10.00% War support: +5.00% |
| The Caliph | Daily Support for Unaligned: +0.02 Acceptance of Communist Diplomacy: -50 Political Power Gain: +10% Stability: +20.00% War support: +20.00% Justify War goal time: -50% Division Defense on core territory: +10% Division Attack on core territory: +10% |
| Anti-British Social Reformer | Stability: +5.00% Daily Support for Unaligned: +0.02 Research Speed: +5.00% Acceptance of Democratic Diplomacy: -30 |
| British Lackey | Political Power Gain: -10% Acceptance of Democratic Diplomacy: +50 Improve relations maintain cost: -100% Justify War goal time on us: +50% |
| Hashemite Regent | Stability: +5.00% Political Advisor Cost: -50% Political Power Gain: +10% |
| Pro-Hashemite Politician | Stability: -5.00% Improve relations maintain cost: -100% Political Advisor Cost: -50% Political Power Gain: +10% |
| Prince of the Believers | Ideology drift defense: +50% Political Power Gain: +5% Recruitable population Factor: +5% War support: +10.00% |
| Unifier of Muscat and Oman | Construction Speed: +5% Political Power Gain: +5% |
| Fraudulent Industrialist | Political Power Gain: +5% Construction Speed: +15% Stability: -5.00% |
| Radical Antipersonnel | Political Power Gain: +5% Daily Democracy Support: +0.03 Daily Support for Unaligned: +0.01 |
| Conservative Traditionalist | Political Power Gain: +5% Daily Support for Unaligned: +0.03 |
| Moderate Dictator | Daily Fascism Support: +0.03 War support: +10.00% Acceptance of Fascist Diplomacy: +30 |
| Brigadier General | Mobilization speed: +5% Recruitable population Factor: +10% |
| Argentine Nationalist | Justify War goal time: -10% War support: +10.00% Recruitable population Factor: +10% |
| Harsh Democrat | Stability: +10.00% Daily Democracy Support: +0.10 Acceptance of Democratic Diplomacy: +40 |
| Feminist Revolutionary | Recruitable population: +1.00% Daily Communism Support: +0.10 |
| Communist Insurrectionist | War support: +10.00% Daily Communism Support: +0.10 Justify War goal time: -10% |
| Anarcho-syndicalist | Daily Communism Support: +0.10 War support: +10.00% Minimum training level: -10% |
| Prominent Centrist | Stability: +20.00% Daily Democracy Support: +0.02 |
| Peronism | Division Defense on core territory: +5% Political Power Gain: +10% Stability: +5.00% Production efficiency cap: +5% |
| Father of the Poor | Stability: +5.00% Recruitable population Factor: +2% |
| Sugar King | Stability: -5.00% Consumer Goods Factories factor: -5% |
| Reluctant Integralist | Political Power Gain: -10% Daily Fascism Support: +0.03 War support: +10.00% Defensive War Penalty Stability Modifier: +10.00% |
| Authoritarian Populist | Political Power Gain: +10% Daily Support for Unaligned: +0.01 Party Popularity Stability Modifier: +5% |
| Politically Educated | Daily Support for Unaligned: +0.02 Economy Laws Cost: -10% Trade Laws Cost: -10% |
| The White Dove | Daily Support for Unaligned: +0.02 Air Accidents Chance: +5% Divisions speed: +2% Stability: +5.00% |
| Emperor of Brazil | Stability: +10.00% War support: +10.00% Political Power Gain: +10% Division Defense on core territory: +10% Division Attack on core territory: +10% |
| Political Paranoia | Ideology drift defense: +10% Political Paranoia increases by 1 weekly |
| Political Paranoia (Advanced) | Ideology drift defense: +10% Political Paranoia increases by 2 weekly |
| Heart of Steel | Stability: -10.00% War support: +5.00% Political Power Gain: +5% Improve relations opinion: -5% Master impact: -0.10 |
| Heart of Steel (Opposition) | Stability: -10.00% War support: +5.00% Improve relations opinion: -5% Master impact: -0.10 |
| Inheritor of the Mantle of Lenin | Political Power Gain: +10% Justify War goal time: -25% |
| Inheritor of the Mantle of Lenin (Genius) | Political Power Gain: +10% Justify War goal time: -25% Research Speed: +5.00% |
| Inheritor of the Mantle of Lenin (Leader) | Political Power Gain: +10% Justify War goal time: -25% Party Popularity Stability Modifier: +15% Defensive War Penalty Stability Modifier: +40.00% Political Advisor Cost: -25% |
| Inheritor of the Mantle of Lenin (Final) | Political Power Gain: +10% Justify War goal time: -25% Research Speed: +5.00% Party Popularity Stability Modifier: +15% Defensive War Penalty Stability Modifier: +40.00% Political Advisor Cost: -25% |
| Faithful Servant of Lenin | Ideology drift defense: +15% Guarantee Cost: -25% |
| Faithful Servant of Lenin (Worship) | Ideology drift defense: +15% Guarantee Cost: -25% Stability: +15.00% |
| Faithful Servant of Lenin (Leader) | Ideology drift defense: +15% Guarantee Cost: -25% Party Popularity Stability Modifier: +15% Defensive War Penalty Stability Modifier: +40.00% Political Advisor Cost: -25% |
| Faithful Servant of Lenin (Final) | Ideology drift defense: +15% Guarantee Cost: -25% Stability: +15.00% Party Popularity Stability Modifier: +15% Defensive War Penalty Stability Modifier: +40.00% Political Advisor Cost: -25% |
| Great Commander | War support: +10.00% Division Recovery Rate: +5% Annex cost: -10% |
| Architect of Communism | Daily Communism Support: +0.10 Master Ideology Drift: +0.10 Puppet cost: -20% |
| Father of Nations | Weekly Stability: +0.10% Daily Compliance Gain: +0.05% Justify War goal time when at war with a major: -50% Recruitable population: +2.00% |
| Authority Undermined | Ideology drift defense: +5% Political Power Gain: +10% Political Paranoia increases by 2 weekly |
| Unscrupulous Orchestrator | Intel network strength gain factor: +15% Own operative capture chance: -10% Counter intelligence: +0.10 Stability: -10.00% |
| Unscrupulous Orchestrator (No Lar) | Subversive activities cost: -35% War support: +10.00% Stability: -10.00% |
| The Siberian Lenin | Resistance Activity Chance: -10% Damage to Garrisons: -10% Operative slots: +1 Resistance Decay Speed: +10% Stability: -5.00% |
| Strong Party Discipline | Ideology drift defense: +15% Daily Compliance Gain: +0.05% Resistance Decay Speed: +10% Stability: +10.00% Surrender Limit: +10% |
| Defender of the Peasantry | Political Power Gain: +10% Stability: +5.00% Research Speed: +2.00% Acceptance of Democratic Diplomacy: +50 Civilian intelligence to others: +15.0% Factory output: -5% |
| Hero of the Peasantry | Political Power Gain: +15% Stability: +10.00% Research Speed: +5.00% Acceptance of Democratic Diplomacy: +50 Civilian intelligence to others: +15.0% Factory output: -2% |
| Organizer of Labor and Defense | Consumer Goods Factories factor: -15% Division Defense on core territory: +5% Army experience Gain: +5% Research Speed: -3.00% |
| Born Agitator | Political Power Gain: +10% Recruitable population Factor: +15% Division Recovery Rate: +5% Stability: -5.00% Compliance Growth Speed: -5% |
| The Faded Star | Research Speed: +3.00% Stability: +10.00% Daily Compliance Gain: +0.05% Political Power Gain: -10% Ideology drift defense: -10% |
| Defier of the Sun God | Division Recovery Rate: +5% Compliance Growth Speed: +5% ( The Empire of Japan)Attack bonus against country: +10% ( The Empire of Japan)Defense bonus against country: +10% |
| Supreme Representative of God on Earth | Stability: +10.00% War support: +10.00% Ideology drift defense: +100% |
| Fascist Orchestrator | Political Advisor Cost: -33% High Command Cost: -33% Air Chief Cost: -33% Army Chief Cost: -33% Navy Chief Cost: -33% Master impact: -0.30 Military factory construction speed: +5% Naval dockyard construction speed: +5% |
| Emperor and Autocrat of All the Russias | Resistance Growth Speed in our states occupied by the enemy: +10% Required Garrisons: -15% War support: +5.00% |
| Émigré Connections | Weekly Manpower: +2000 Consumer Goods Factories factor: -10% |
| Desperate Gambit | Division Attack on core territory: +10% Division Defense on core territory: +10% Resistance Growth Speed in our states occupied by the enemy: +25% |
| Dysfunctional Assembly | Weekly Stability: -0.20% Daily Political Power Gain: -0.50 |
| Democratic Reformer | Daily Democracy Support: +0.10 |
| Staunch Monarchist | Daily Support for Unaligned: +0.10 |
| Conducător | Damage to Garrisons: -25% Foreign subversive activities efficiency: -35% Non-core Manpower: +2.00% Division Attack on core territory: +5% |
| Vodca | Political Power Gain: +5% Division Attack on core territory: +5% Division Defense on core territory: +5% |
| Council Communist | Political Power Gain: -30% Factory output: +10% Dockyard output: +10% |
| Anti-Colonialist | Stability: +10.00% Political Power Gain: +5% Daily Democracy Support: +0.05 |
| Konbuang Dynasty Descendant | Justify War goal time: -15% Daily Support for Unaligned: +0.05 Political Power Gain: +10% |
| Mon Dynasty Descendant | War support: +10.00% Daily Fascism Support: +0.05 |
| Founder of the Burmese Way to Socialism | War support: +5.00% Recruitable population Factor: +10% Daily Communism Support: +0.05 |
| Monarchist Media Mogul | Daily Support for Unaligned: +0.10 War Penalty Stability Modifier: +10.00% |
| Democratic Crusader | Daily Fascism Support: -0.05 Daily Communism Support: -0.05 Daily Democracy Support: +0.05 Acceptance of Democratic Diplomacy: +40 |
| Latvian Militant | Daily Support for Unaligned: +0.05 War support: +10.00% Daily Command power Gain Multiplier: +10% Conscription Laws Cost: -10% |
| The King of the Castle | Daily Support for Unaligned: +0.10 Political Power Gain: +10% |
| Leftist Minister | Stability: +10.00% Acceptance of Democratic Diplomacy: +85 |
| Sanation Militarist | Daily Support for Unaligned: +0.05 Land Doctrine Cost: -10% Army experience Gain: +0.04 daily |
| Sanation Militarist (Falangist) | Daily Fascism Support: +0.05 Army experience Gain: +0.04 daily |
| Patriotic Guerilla | Weekly Exiled Government Manpower: +700 Daily Legitimacy Gain: +0.10 Division Attack: +10% Division Defense: +10% |
| Polish Legionary | Weekly Exiled Government Manpower: +700 Division Attack on core territory: +15% Division Defense on core territory: +15% |
| Democratic Restorationist | Weekly Exiled Government Manpower: +700 Daily Legitimacy Gain: +0.10 Daily Democracy Support: +0.10 |
| King of the Exiles | Weekly Exiled Government Manpower: +700 Daily Legitimacy Gain: +0.10 Division Attack on core territory: +5% Division Defense on core territory: +5% |
| Anti-Bolshevik Leftist | Daily Communism Support: +0.05 Recruitable population Factor: +15% |
| Devoted Marxist | Daily Communism Support: +0.05 Same ideology monthly opinion: +100% Stability: +10.00% |
| Revolutionary | Daily Communism Support: +0.05 Division Attack on core territory: +10% Division Defense on core territory: +10% |
| Independent Leftist | Division Recovery Rate: +10% Division Attack on core territory: +5% Division Defense on core territory: +5% |
| Pro-Soviet | Ideology drift defense: +15% Daily Autonomy progress gain: +0.50 |
| The Last Romanov? | Stability: -20.00% |
| The Last Romanov | Stability: -5.00% |
| The Last Romanov! | Stability: +20.00% War support: +10.00% Political Power Gain: +10% |
| Peasant Hero | Stability: +10.00% Recruitable population Factor: +5% |
| Champion of Front Morges | War support: +10.00% Training time: -10% Conscription Laws Cost: -10% |
| He Who Bears the Throne | Stability: +20.00% War support: +20.00% Ideology drift defense: +50% |
| Father of Polish Nationalism | Political Power Gain: +10% Stability: +10.00% Daily Fascism Support: +0.10 |
| Unruly Falangist | Generate War goal tension limit: -50% Justify War goal time: -25% War support: +5.00% |
| Unruly Falangist Marionette | Political Power Gain: +10% Resistance Growth Speed: -10% War support: -10.00% |
| The Cossack-King | Justify War goal time: -25% Cavalry Attack: +15% Cavalry Defense: +15% |
| Cossack Ataman | Justify War goal time: -25% Generate War goal tension limit: -50% Cavalry Attack: +15% Cavalry Defense: +15% |
| Royal Legitimist | Political Power Gain: +10% Daily Compliance Gain: +0.05% Stability: +5.00% |
| Patriot King | Stability: +5.00% War support: +10.00% |
| King of Galicia and Lodomeria | Political Power Gain: +10% |
| The Soldier King (POL) | Division Recovery Rate: +10% |
| King of Lithuania | Stability: +10.00% War support: +5.00% |
| Skanderbeg II | Stability: +5.00% War support: +10.00% Division Defense on core territory: +10% Recruitable population: +1.50% |
| Reformist Menshevik | Research Speed: +5.00% Stability: +5.00% Construction Speed: +5% Acceptance of Democratic Diplomacy: +30 |
| Pro-Allied Governor-General | Acceptance of Democratic Diplomacy: +30 Political Power Gain: +5% War support: +5.00% Daily Compliance Gain: -0.02% |
| Pro-Allied Governor-General (2) | Acceptance of Democratic Diplomacy: +50 Political Power Gain: +8% War support: +5.00% Daily Compliance Gain: -0.01% |
| Mwami of Burundi | Daily Support for Unaligned: +0.10 Division Defense on core territory: +10% Stability: +5.00% |
| Pro-German Mwami | Daily Support for Unaligned: +0.05 Daily Fascism Support: +0.05 Division Defense on core territory: +10% War support: +5.00% |
| Umwami of Rwanda | Daily Support for Unaligned: +0.10 Division Defense on core territory: +10% War support: +5.00% |
| Litunga of the Barotse | Daily Support for Unaligned: +0.10 Division Defense on core territory: +10% Stability: +5.00% War support: +5.00% |
| Sultan of Sokoto | Daily Support for Unaligned: +0.10 Justify War goal time: -25% War support: +10.00% |
| Unifier of Central Arabia | Justify War goal time: -25% War support: +10.00% |
| Pan-Africanist Socialist | Ideology drift defense: +10% Division Defense on core territory: +10% Division Attack on core territory: +5% Resistance Target: -5% |
| Provincial Governor of Léopoldville | Political Power Gain: +15% Stability: +5.00% Construction Speed: +5% |
| Trade Unionist (COG) | Daily Communism Support: +0.05 Production efficiency cap: +10% Lack of Resources Penalty: -15% |
| Emergency Powers (COG) | All Autonomy gain: +5% Political Power Gain: +10% War support: +5.00% |
| Great Leader | Political Power Gain: +10% Ideology drift defense: +50% War support: +5.00% Stability: +5.00% |
| God Upon the Earth | Political Power Gain: +15% Ideology drift defense: +50% War support: +5.00% |
| N'gangue M'voumbe Oussangueme | Political Power Gain: +10% Stability: +5.00% |
| The Embodiment of God | War support: +10.00% Justify War goal time: -30% Generate War goal tension limit: -25% |
| Founding Father of the Congolese Nation | Political Power Gain: +10% Daily Democracy Support: +0.05 Political Advisor Cost: -25% Trade Laws Cost: -15% Economy Laws Cost: -15% |
| Manikongo of the Kingdom of Kongo | Daily Support for Unaligned: +0.05 Division Defense on core territory: +10% Political Power Gain: +5% |
| Nyim of Kuba | Daily Support for Unaligned: +0.05 Division Attack on core territory: +5% Resistance Target: -10% |
| Mâ Loango | Daily Support for Unaligned: +0.05 Stability: +10.00% War support: +5.00% |
| The Carlist Habsburg Pretender | Political Power Gain: +5% Recruitable population: +1.50% |
| The Habsburg Hetman | Division Defense on core territory: +15% Cavalry Attack: +10% Recruitable population: +1.00% |
| Duke of Teschen, King of Bohemia, Margrave of Moravia | Division Defense on core territory: +15% Mobilization speed: +10% Recruitable population: +1.00% |
| Head of the Imperial House of Mexico | Stability: +15.00% Recruitable population: +1.50% |
| Regent of Hungary | Stability: +5.00% War support: +5.00% Political Power Gain: -15% |
| Regent of Hungary (2) | Stability: +5.00% War support: +5.00% Political Power Gain: -5% Daily Support for Unaligned: +0.01 |
| Regent of Hungary (3) | Stability: +5.00% War support: +10.00% Daily Support for Unaligned: +0.02 Justify War goal time: -10% |
| The Undermined Regent | Stability: -5.00% War support: -5.00% Political Power Gain: -10% Ideology drift defense: -25% |
| The Apostolic King | War support: +5.00% Division Defense on core territory: +10% Daily Support for Unaligned: +0.05 |
| The Habsburg Prince | Recruitable population: +0.50% Political Power Gain: +10% |
| Ardent Stalinist | Ideology drift defense: +50% Division Defense on core territory: +10% Daily Communism Support: +0.02 |
| Revolutionary Internationalist | Non-core Manpower: +2.00% Justify War goal time: -15% Daily Compliance Gain: +0.01% |
| Vengeful Stalinist | Division Attack: +10% Division Defense: +5% Daily Communism Support: +0.15 Political Power Gain: +5% |
| Socialist Bulwark | Political Power Gain: +5% Division Defense on core territory: +15% Daily Communism Support: +0.02 Daily Democracy Support: +0.02 |
| Árpád's Successor | Attack against major countries: +5% Defense against major countries: +10% |
| Heir of Árpád, Andrew and Matthias Corvinius | Attack against major countries: +10% Defense against major countries: +10% War support: +10.00% |
| Poglavnik | Political Power Gain: -5% Stability: -5.00% War support: +10.00% Recruitable population Factor: +5% |
| Popular Among Paramilitaries | Daily Fascism Support: +0.02 Recruitable population Factor: +10% Division Defense on core territory: +15% |
| Volksgruppenführer der Deutschen in Ungarn | Daily Fascism Support: +0.10 Recruitable population Factor: +5% Militia Attack: +5% |
| The Hungarian Lenin | Recruitable population Factor: +5% Consumer Goods Factories factor: -5% Daily Communism Support: +0.03 |
| Duke of Mecklenburg-Schwerin, King of the Hungarians | Acceptance of Fascist Diplomacy: +75 Resistance Growth Speed: -10% Political Power Gain: +15% |
| The Old Warden | Recruitable population: +0.50% Division Defense on core territory: +10% |
| Popular Aviator | Stability: +5.00% Air experience Gain: +10% Air Doctrine Cost: -15% |
| National-Socialist Irredentist | Daily Fascism Support: +0.05 War support: +10.00% Justify War goal time: -15% |
| Veteran President | Political Power Gain: +15% Stability: +10.00% |
| Christian Academic | Research Speed: +5.00% Stability: +10.00% |
| Duke of Södermanland, King of the Hungarians | Daily Democracy Support: +0.03 Daily Support for Unaligned: +0.05 Stability: +10.00% War support: +10.00% |
| Ban of the Great Kingdom of Croatia-Slavonia | Stability: -10.00% War support: +10.00% Division Defense on core territory: +5% |
| Archduke of Austria-Este | Stability: -5.00% War support: +5.00% Division Defense on core territory: +10% |
| Blessed Monarch | Stability: +15.00% Recruitable population Factor: +5% |
| Popular Liberal | Stability: +10.00% Political Power Gain: +10% Daily Democracy Support: +0.05 |
| Nemzetvezető | Political Power Gain: +10% Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +15% Stability: +5.00% |
| National-Socialist Count | Daily Fascism Support: +0.10 Same ideology monthly opinion: +75% Political Power Gain: +10% |
| Apostolic King of Hungary | Daily Fascism Support: +0.05 War support: +5.00% Air experience Gain: +0.10 daily Political Power Gain: -15% |
| Shrewd Regent | Stability: +15.00% Daily Political Power Cost: +0.15 |
| Sovereign of The Norwegians | Stability: +20.00% Daily Political Power Cost: -0.05 Consumer Goods Factories factor: +10% |
| Democratic Powerhouse | Daily Democracy Support: +0.08 Stability: +15.00% War support: -15.00% |
| Stern Communist (NOR) | Daily Communism Support: +0.09 Surrender Limit: +20% Political Power Gain: -5% |
| Conciliatory Socialist | Stability: +10.00% Daily Communism Support: +0.01 |
| Fascist Lackey | Daily Fascism Support: +0.08 Stability: -10.00% War Penalty Stability Modifier: +15.00% War support: +10.00% |
| Fascist Dilettante | Daily Fascism Support: +0.01 Stability: -15.00% War support: -10.00% Resistance Decay Speed: -15% |
| Fascist Landssviker | Daily Fascism Support: +0.01 Stability: -15.00% War support: -10.00% Resistance Decay Speed: -18% |
| Ruthless Administrator | Daily Fascism Support: +0.12 Stability: +15.00% Resistance Decay Speed: +10% |
| The Tobacco Tycoon | Consumer Goods Factories factor: -10% Infrastructure construction speed: +10% Civilian factory construction speed: +5% |
| Popular Reformer | Stability: +5.00% War support: -3.00% Political Power Gain: +5% |
| Temperate Miners Unionist | Stability: +5.00% Resource Gain Efficiency: +10% |
| Germanophile Officer | Daily Fascism Support: +0.03 War support: +20.00% Army experience Gain: +0.10 daily Resistance Decay Speed: -25% Stability: -20.00% |
| Polarizing Leader | Invasion Preparation Speed: +15% Chance to score Critical Hit: +15% Weekly Manpower: +500 Justify War goal time: -50% Base Fuel Gain: +100% Construction Speed: +20% Research Speed: +10.00% Production efficiency cap: +10% Production efficiency growth: +30% Lack of Resources Penalty: -50% |
| Wielder of Emergency Powers | Consumer Goods Factories factor: -10% Military factory construction speed: +5% Naval dockyard construction speed: +5% |
| Under Fascist Pressure | Acceptance of Fascist Diplomacy: +50 Daily Fascism Support: +0.03 Stability: -10.00% Surrender Limit: -15% |
| Embraced Fascism | Acceptance of Fascist Diplomacy: +50 Daily Fascism Support: +0.03 War support: +5.00% Surrender Limit: +10% |
| Abolished Austrofascism | Daily Support for Unaligned: +0.03 Daily Democracy Support: +0.05 Stability: +5.00% Surrender Limit: +10% |
| Protector of Austrian Independence | Daily Democracy Support: +0.02 Stability: +5.00% Surrender Limit: +25% War Penalty Stability Modifier: +25.00% Division Defense on core territory: +2% |
| Right-Wing Democrat | Daily Democracy Support: +0.05 Daily Fascism Support: +0.03 Stability: +5.00% Ideology drift defense: +25% |
| Archduke of Austria | Political Power Gain: +10% Daily Support for Unaligned: +0.03 Stability: +5.00% War support: +5.00% Recruitable population: +0.50% |
| Fürst von und zu Liechtenstein | Political Power Gain: +10% Daily Support for Unaligned: +0.03 Stability: +5.00% War support: +5.00% Recruitable population: +0.50% |
| Elizabeth..? | ( United Kingdom)Compliance Growth Speed: +1% |
| Propagandist Artist | Daily Fascism Support: +0.05 Ideology drift defense: +15% |
| Fascist Prince of House Starhemberg | Daily Support for Unaligned: +0.03 Daily Fascism Support: +0.05 War support: +10.00% Militia Attack: +5% Recruitable population: +0.50% |
| Determined Prime Minister | Surrender Limit: +10% War support: +10.00% Daily Democracy Support: +0.05 |
| Corrupt Old Guard | Stability: +5.00% Consumer Goods Factories factor: +10% Ideology drift defense: +25% |
| Royal Appointee | Stability: +5.00% |
| Diplomatic Titan | Trade extra resource per factory: +2 Daily Communism Support: +0.01 |
| Le Patron | Daily Communism Support: +0.01 Daily Fascism Support: -0.01 Join faction tension limit: -20% Guarantee tension limit: -20% |
| Belgian Inquisitor | Daily Fascism Support: +0.03 War support: +5.00% |
| Belgian Fuhrer | Daily Fascism Support: +0.05 War support: +10.00% |
| Man with a Plan | Daily Communism Support: +0.03 Production efficiency growth: +10% Production efficiency cap: +10% |
| King of the Belgians | Stability: +10.00% Recruitable population Factor: +15% Daily Support for Unaligned: +0.01 Division Defense on core territory: +10% |
| Prisoner-King | Stability: +10.00% Daily Support for Unaligned: +0.03 |
| Unknown Sympathies | Stability: -10.00% War support: -10.00% Daily Political Power Gain: +0.20 Daily Support for Unaligned: +0.01 |
| Royal Regent | Stability: +10.00% Daily Political Power Gain: +0.10 |
| Quiet Royal | Stability: +5.00% Daily Political Power Gain: +0.10 |
| Charles, King of the Belgians | Stability: +15.00% Daily Political Power Gain: +0.15 Party Popularity Stability Modifier: +25% Improve relations opinion: +25% |
| Democratic Liberator of the Homeland | Stability: +15.00% Daily Democracy Support: +0.03 Party Popularity Stability Modifier: +25% Political Power Gain: +15% Ideology drift defense: +25% |
| Reichskommissar | Political Power Gain: -10% Division Defense on core territory: -5% Recruitable population Factor: +10% Non-core Manpower: +3.00% Ideology drift defense: +50% Resistance Target: -10% |
| Reichsprotektor | Political Power Gain: -5% Division Defense on core territory: -5% Non-core Manpower: +3.00% Ideology drift defense: +25% Resistance Target: -5% |
| Governor-General | Stability: -10.00% Division Defense on core territory: -10% Recruitable population Factor: +15% Non-core Manpower: +3.00% |
| Der Führer | Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Political Power Gain: +10% Compliance Growth Speed: -2% Resistance Target: +5% |
| Der Führer (Wehrmacht) | Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Political Power Gain: +10% Compliance Growth Speed: -2% Resistance Target: +5% Supply Range: -10% Daily Command power Gain Multiplier: +10% All Military Advisors Cost: -15% |
| Der Führer (Neurath) | Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Political Power Gain: +10% Compliance Growth Speed: -2% Resistance Target: +5% Justify War goal time: +15% Army experience Gain: +10% Air experience Gain: +10% Navy experience Gain: +10% |
| Der Führer (Führerprinzip) | Political Power Gain: +25% Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Party Popularity Stability Modifier: +10% Compliance Growth Speed: -2% Resistance Target: +5% |
| Der Führer (Führerprinzip + Wehrmacht) | Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Political Power Gain: +25% Party Popularity Stability Modifier: +10% Compliance Growth Speed: -2% Resistance Target: +5% Supply Range: -10% Daily Command power Gain Multiplier: +10% All Military Advisors Cost: -15% |
| Der Führer (Führerprinzip + Neurath) | Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Political Power Gain: +25% Party Popularity Stability Modifier: +10% Compliance Growth Speed: -2% Resistance Target: +5% Justify War goal time: +15% Army experience Gain: +10% Air experience Gain: +10% Navy experience Gain: +10% |
| Loyal Inner Circle | Special Project Speed: +5.00% Production efficiency cap: +10% Maximum Command power Increase Multiplier: +25% Construction Speed: +5% |
| Der Führer (Todt) | Daily Political Power Gain: +0.25 Civilian factory construction speed: +10% Infrastructure construction speed: +10% Railway construction speed: +10% Military factory construction speed: +10% Naval dockyard construction speed: +10% |
| Der Führer (Speer) | Daily Political Power Gain: +0.25 Construction Speed: +5% Daily Fascism Support: +0.01 Factory output: +10% Dockyard output: +10% |
| Der Führer (Göring) | Daily Political Power Gain: +0.25 Resource Gain Efficiency: +5% Production efficiency cap: +5% Production efficiency growth: +5% Production Efficiency Base: +5.00% Production efficiency retention: +5% |
| Der Führer (Himmler, Abwehr) | Daily Political Power Gain: +0.25 Damage to Garrisons: -25% Foreign subversive activities efficiency: -30% Non-core Manpower: +2.00% Subversive activities cost: -25% Operative slots: +1 Counter intelligence: +0.20 Intelligence gained from Combat: +25.00% |
| Der Führer (Himmler, SS) | Daily Political Power Gain: +0.25 Damage to Garrisons: -25% Foreign subversive activities efficiency: -30% Non-core Manpower: +4.00% Subversive activities cost: -25% Operative slots: +1 Counter intelligence: +0.20 Intelligence gained from Combat: +25.00% Resistance Growth Speed: -15% Compliance Growth Speed: -10% Special Forces Capacity Multiplier: +5% |
| Der Führer (Goebbels) | Daily Political Power Gain: +0.25 War support: +10.00% Daily Fascism Support: +0.20 Party Popularity Stability Modifier: +10% Surrender Limit: +10% Offensive War Penalty Stability Modifier: +10.00% Defensive War Penalty Stability Modifier: +10.00% Operative slots: +2 Boost Ideology mission effects: +15% Strengthen Resistance efficiency: +15% |
| Der Führer (Goebbels, no LaR) | Daily Political Power Gain: +0.25 War support: +10.00% Daily Fascism Support: +0.20 Party Popularity Stability Modifier: +10% Surrender Limit: +10% Offensive War Penalty Stability Modifier: +10.00% Defensive War Penalty Stability Modifier: +10.00% Subversive activities cost: -50% |
| Der Führer (Hess) | Daily Political Power Gain: +0.25 Same ideology monthly opinion: +100% Funds Gain: +15% Military Industrial Organization Research Bonus: +15% Recruitable population Factor: +5% Political Power Gain: +15% Conscription Laws Cost: -25% Trade Laws Cost: -25% Economy Laws Cost: -25% Research Speed: +5.00% |
| Der Führer (Hess, no AAT) | Daily Political Power Gain: +0.25 Same ideology monthly opinion: +100% Tank Designer Cost: -35% Materiel Designer Cost: -35% Aircraft Designer Cost: -35% Naval Designer Cost: -35% Recruitable population Factor: +5% Political Power Gain: +15% Conscription Laws Cost: -25% Trade Laws Cost: -25% Economy Laws Cost: -25% Research Speed: +5.00% |
| Der Führer (Bormann) | Daily Political Power Gain: +0.25 Political Advisor Cost: -50% Theorist Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% Air Chief Cost: -25% High Command Cost: -25% Recruitable population Factor: +5% Political Power Gain: +15% Conscription Laws Cost: -25% Trade Laws Cost: -25% Economy Laws Cost: -25% Research Speed: +5.00% |
| Loyalty of the Wehrmacht | War support: +5.00% Stability: +5.00% |
| Supreme Commander of the Armed Forces | War support: +5.00% Stability: +5.00% Division Recovery Rate: +5% Resistance Growth Speed: -2% |
| The Supreme Leader | War support: +5.00% Stability: +5.00% Division Recovery Rate: +10% Non-core Manpower: +1.00% Resistance Growth Speed: -5% Division Attack: +5% Division Defense: +5% Master impact: -0.10 |
| The Iron Maiden | War support: +15.00% Justify War goal time: -10% Ideology drift defense: +50% Division Attack: +5% Division Defense: +5% Division Recovery Rate: +5% |
| Oberste Heeresleitung | Political Power Gain: -15% Stability: -10.00% Max planning factor: +10.0% Army experience Gain: +10% Navy experience Gain: +10% Air experience Gain: +10% High Command Cost: -25% Air Chief Cost: -25% Army Chief Cost: -25% Navy Chief Cost: -25% |
| Stern Communist (GER) | Daily Communism Support: +0.10 Surrender Limit: +10% Political Power Gain: +5% Party Popularity Stability Modifier: +10% War support: +10.00% Militia Defense: +5% Militia Attack: +5% Militia Organization: +5% |
| Pragmatic Trade Unionist | Political Power Gain: -10% Party Popularity Stability Modifier: +15% Political Advisor Cost: -25% Production efficiency cap: +5% Production Efficiency Base: +5.00% |
| Inflexible Communist Organizer | Daily Communism Support: +0.05 Political Power Gain: +10% Surrender Limit: +10% |
| Staunch Stalinist /GER) | Daily Communism Support: +0.05 Political Power Gain: +10% Surrender Limit: +20% Construction Speed: +10% Production efficiency growth: -10% |
| Traditionalist | Political Power Gain: +10% Stability: +10.00% Acceptance of Communist Diplomacy: -50 Acceptance of Fascist Diplomacy: -50 Construction Speed: +5% |
| Staunch Social Democrat | Political Power Gain: +10% Production efficiency growth: +5% Production Efficiency Base: +5.00% Offensive War Penalty Stability Modifier: -10.00% Acceptance of Communist Diplomacy: -25 Acceptance of Fascist Diplomacy: -50 Master impact: -0.10 |
| Pragmatic Socialist | Political Power Gain: +10% Political Advisor Cost: -25% Improve relations opinion: +10% Stability: +10.00% Acceptance of Democratic Diplomacy: +25 Master impact: -0.10 |
| The General Secretary | Same ideology monthly opinion: +10% |
| Our Enemy's Enemy | Daily Political Power Gain: +0.05 Stability: -10.00% War Penalty Stability Modifier: +5.00% War support: +10.00% Division Attack on core territory: +15% Division Recovery Rate: +10% Political Advisor Cost: +25% Trade Laws Cost: +25% Conscription Laws Cost: +25% Economy Laws Cost: +25% |
| Head of the Personality Cult | Equipment Capture Ratio Modifier: +15% Daily Political Power Gain: +0.15 Stability: +10.00% War Penalty Stability Modifier: +5.00% Division Attack on core territory: +5% Division Defense: +5% Division Recovery Rate: +10% Recruitable population: +1.00% |
| De Facto Leader | Daily Political Power Gain: +0.10 Stability: +10.00% War Penalty Stability Modifier: +5.00% Division Recovery Rate: +8% |
| Out for Revenge | Stability: -10.00% War support: +10.00% Division Recovery Rate: +10% Army experience Gain: +0.15 daily Training time: -3% |
| Supreme Chairman (1) | Military factory construction speed: +3% Factory output: +3% |
| Supreme Chairman (2) | Military factory construction speed: +5% Factory output: +3% |
| Supreme Chairman (3) | Political Power Gain: +5% Military factory construction speed: +5% Factory output: +3% |
| Supreme Chairman (4) | Political Power Gain: +5% Military factory construction speed: +10% Factory output: +3% |
| Supreme Chairman (5) | Political Power Gain: +10% Military factory construction speed: +10% Factory output: +5% Dockyard output: +5% |
| One of 28½ | Same ideology monthly opinion: +10% Stability: +5.00% War Penalty Stability Modifier: +5.00% |
| Maoism (1) | Political Power Gain: +5% Maximum Command power Increase: +5 |
| Maoism (2) | Political Power Gain: +5% Daily Command power Gain: +0.05 Maximum Command power Increase: +5 |
| Maoism (3) | Political Power Gain: +10% Daily Command power Gain: +0.10 Maximum Command power Increase: +20 Encirclement penalty: -5.0% |
| Maoism (4) | Political Power Gain: +10% Daily Command power Gain: +0.10 Maximum Command power Increase: +15 Encirclement penalty: -10.0% Equipment Capture Ratio Modifier: +5% Division Defense: +5% |
| Maoism (5) | Political Power Gain: +15% Daily Command power Gain: +0.20 Maximum Command power Increase: +20 Encirclement penalty: -15.0% Equipment Capture Ratio Modifier: +10% Division Defense: +8% |
| Cautious Arbiter | Political Power Gain: +10% War support: -5.00% Acceptance of Communist Diplomacy: +30 |
| Viceroy Emeritus | Generate War goal tension limit: +10% |
| Nation Builder | Political Power Gain: +10% Stability: +5.00% Improve relations opinion: +5% |
| Puppet President | Resistance Target: -5% Stability: +5.00% |
| Pioneer Marxist | Daily Communism Support: +0.10 Recruitable population Factor: +5% |
| Radical Leader | Daily Communism Support: +0.10 Minimum Surrender Limit: +15.00% Resistance Growth Speed in our states occupied by the enemy: +15% |
| Political Hacendado | Trade Laws Cost: -50% Economy Laws Cost: -25% Consumer Goods Factories factor: -10% |
| Revolutionary President | Recruitable population Factor: +10% Political Power Gain: +5% Stability: +5.00% War support: +5.00% |
| Philippine Nationalist Leader | War support: +10.00% Daily Fascism Support: +0.10 Division Attack on core territory: +5% Division Defense on core territory: +5% |
| Chief Justice | Political Power Gain: +5% Daily Democracy Support: +0.05 Stability: +10.00% |
| Supreme Marshal | Political Power Gain: +15% Weekly War support (Combat Casualties): +0.10% AI Modifier: Desired Divisions Factor: +20% Max planning: +10% Division Organization: +10% |
| Supreme Commissioner | Stability: +10.00% Weekly War support (Combat Casualties): +0.10% Max planning: +15% |
| No Government | Stability: -25.00% Political Power Gain: -25% Weekly Stability: -1.00% |
| Resistance Connections | Political Power Gain: +10% Damage to Enemy Garrisons in our states occupied by the enemy: +10% Resistance Decay Speed in our states occupied by the enemy: -10% High Command Cost: -33% |
| Generallissimo | Defensive War Penalty Stability Modifier: +40.00% Minimum Surrender Limit: +10.00% Surrender Limit: +5% |
| Generalissimo of All of China | Defensive War Penalty Stability Modifier: +40.00% Minimum Surrender Limit: +10.00% Political Power Gain: +10% Daily Support for Unaligned: +0.10 Surrender Limit: +5% |
| Victor of the War of Resistance | Stability: +10.00% Daily Command power Gain Multiplier: +10% |
| Civilian Unifier | Master impact: -0.02 |
| Civilian Unifier (Upgraded) | Master impact: -0.04 Political Power Gain: +5% Annex Subject Cost Factor: -15.00% Surrender Limit: +5% |
| Civilian Unifier (Upgraded 2) | Master impact: -0.06 Political Power Gain: +5% Annex Subject Cost Factor: -25.00% Surrender Limit: +5% |
| Asian Unifier and Liberator | Master impact: -0.08 Political Power Gain: +5% Annex Subject Cost Factor: -25.00% Daily Compliance Gain: +0.01% Surrender Limit: +10% |
| The Northern Bastion | Daily Command power Gain Multiplier: +5% Defensive War Penalty Stability Modifier: +10.00% |
| Bridge Builder | Political Power Gain: +10% Ideology drift defense: +30% Infrastructure construction speed: +20% |
| The Path to Chinese Reconstruction | Daily Fascism Support: +0.08 War support: +10.00% Division Defense on core territory: +5% Division Attack on core territory: +5% |
| The Path to Chinese Reconstruction (No LaR) | Daily Fascism Support: +0.08 War support: +10.00% Division Defense on core territory: +5% Division Attack on core territory: +5% |
| Son of Heaven | Ideology drift defense: +15% Party Popularity Stability Modifier: +10% |
| Celestial Emperor | Ideology drift defense: +50% Party Popularity Stability Modifier: +15% Justify War goal time: -25% Division Attack: +5% Division Defense: +5% |
| Continental Rōnin (Expert) | Air Superiority: +5% Division Organization: +5% Air experience Gain: +0.30 daily |
| Batllista Traditionalist | Daily Support for Unaligned: +0.01 Daily Democracy Support: +0.01 Justify War goal time on us: +10% |
| The German Connection | Improve relations maintain cost: -30% Daily Fascism Support: +0.05 Political Power Gain: +10% War support: +5.00% |
| Pan-Americanist Caudillo | Maximum Command power Increase Multiplier: +10% Division Defense on core territory: +10% Division Attack on core territory: +5% Justify War goal time: -50% Generate War goal tension limit: -100% |
| Pro-Allied Politician | Daily Democracy Support: +0.03 Acceptance of Democratic Diplomacy: +15 Political Power Gain: +10% War support: +5.00% Lend-lease tension limit: -50% |
| León de Tarapacá | Stability: +5.00% Political Power Gain: +10% Ideology drift defense: +5% |
| El Jefe | Recruitable population: +1.50% War support: +10.00% |
| Gobernar es Educar | Research Speed: +10.00% Stability: +5.00% |
| Easter Island Socialist | Daily Communism Support: +0.10 Resistance Growth Speed: -15% Political Power Gain: +10% |
| Stock Market Financier | Consumer Goods Factories factor: -10% Civilian factory construction speed: +5% |
| The Workers' President | Daily Communism Support: +0.05 Stability: +10.00% Production efficiency cap: +5% Compliance Growth Speed: +2% |
| The General President | Resistance Growth Speed: -5% Daily Command power Gain Multiplier: +15% Division Attack on core territory: +5% Division Defense on core territory: +10% |
| Sapa Inca | Resistance Growth Speed: -5% Daily Command power Gain Multiplier: +25% Division Attack on core territory: +5% Division Defense on core territory: +10% |
| Resplendent King of El Dorado | Stability: +10.00% War support: +10.00% Division Attack on core territory: +5% Division Defense on core territory: +10% |
| High Chief of Hispaniola | Navy experience Gain: +0.10 daily Division Attack on core territory: +5% Division Defense on core territory: +10% |
| The National Socialist Vanguard | Recruitable population Factor: +5% Division Attack: +5% War support: +10.00% |
| Fascist Educator | Daily Fascism Support: +0.05 Research Speed: +15.00% |
| Devoted Trotskyist (JUNO) | Divisions required for sending volunteer force: -40% Max volunteer force divisions: +30% Send volunteers tension limit: -50% |
| Popular Among the People | Ideology drift defense: +25% Compliance Growth Speed: +2% Stability: +10.00% |
| Spearhead of the Alianza Democrática de Chile | Daily Communism Support: +0.02 Daily Democracy Support: +0.03 Stability: +15.00% War support: +5.00% |
| Popular Lawyer | Stability: +10.00% Political Power Gain: +20% |
| Friend of Healthcare | Monthly Population: +10% Weekly Manpower: +100 |
| Roi d'Araucanie et de Patagonie (1) | Stability: -10.00% War support: -10.00% Daily Support for Unaligned: +0.02 Division Defense on core territory: +5% |
| Roi d'Araucanie et de Patagonie (2) | Stability: -5.00% War support: -5.00% Daily Support for Unaligned: +0.06 Division Defense on core territory: +5% |
| Roi d'Araucanie et de Patagonie (3) | Daily Support for Unaligned: +0.08 Division Defense on core territory: +5% Attack against major countries: +5% Defense against major countries: +10% |
| Defender of Araucanía | Division Attack on core territory: +5% Division Defense on core territory: +10% War support: +5.00% |
| Modern Abajino Lonko | War support: +15.00% Stability: +5.00% |
| The Legacy of 1881 | Division Attack: +5% Division Defense: +10% |
| Unpopular Economist | Stability: -20.00% Political Power Gain: -10% Economy Laws Cost: -30% Consumer Goods Factories factor: -25% |
| Founder of the Bolivian Socialist Falange | Political Power Gain: +15% Justify War goal time: -20% Daily Fascism Support: +0.05 |
| Military Socialist | Army experience Gain: +0.05 daily Division Defense on core territory: +20% Ideology drift defense: +15% |
| Revolutionary Writer | Ideology drift defense: +25% Resistance Growth Speed in our states occupied by the enemy: +30% Daily Communism Support: +0.03 Political Power Gain: +10% Stability: +5.00% War support: +5.00% |
| Revolutionary Febrerista Hero | Ideology drift defense: +50% Division Defense on core territory: +15% Political Power Gain: +10% |
| Leader of the Red Banner | Division Attack: +5% Recruitable population Factor: +10% |
| The President of Victory | Party Popularity Stability Modifier: +20% War support: +5.00% Political Power Gain: -15% Stability: -10.00% |
| The Permanent Leader | Surrender Limit: +20% Resistance Target: -5% Recruitable population Factor: +10% War support: +5.00% |
| Cult of Personality | Division Defense on core territory: +10% Division Attack on core territory: +5% Stability: +5.00% War support: +5.00% |
| Bandit Revolutionary | Stability: -10.00% War support: +20.00% Non-Combat Out of Supply Penalties: -10% Recruitable population Factor: +5% |
| Rapa Nui 'Ariki | Stability: +10.00% War support: +5.00% Division Defense on core territory: +25% Generate War goal tension limit: -40% Non-core Manpower: +10.00% |
| Cultural Preserver and Scholar | Political Power Gain: +10% Stability: +10.00% Max Factories in a State: +40% |
| People's Revolutionary Council | Ideology drift defense: +20% Division Attack on core territory: +10% Political Power Gain: +10% |
| People's United Freedom Council | Division Attack on core territory: +5% Division Defense on core territory: +10% Mobilization speed: +15% Recruitable population Factor: +10% |
| Republican People's Council | Recruitable population: +2.00% Recruitable population Factor: +10% Daily Democracy Support: +0.05 |
| Corporativist Advisory Board | Attack against major countries: +20% Divisions speed: +10% Construction Speed: +10% |
| The True Emperor of France and the Americas | Division Attack on core territory: +5% Division Defense on core territory: +10% War support: +10.00% Stability: +10.00% Daily Command power Gain Multiplier: +20% |
| Grand King of the Chilean Fatherland | Resistance Growth Speed: -10% Political Power Gain: +15% Division Defense on core territory: +10% Division Attack on core territory: +5% |
| Aligned With Stalin | Ideology drift defense: +25% Daily Communism Support: +0.03 Stability: +5.00% Same ideology monthly opinion: +100% |
| Council of the ANL | War support: +15.00% Stability: -5.00% Daily Communism Support: +0.03 Military factory construction speed: +10% Civilian factory construction speed: +10% |
| Unpopular | Stability: -10.00% |
| Dynasty Founder | Political Power Gain: +5% Stability: -5.00% Cavalry Attack: +5% |
| Renaissance Man | Political Power Gain: +10% Research Speed: +5.00% |
| Dynastic Reformer | Stability: +15.00% Recruitable population Factor: +5% |
| Anti-Shah Democrat | Political Power Gain: +10% Acceptance of Unaligned Diplomacy: -15 Daily Democracy Support: +0.05 Stability: +5.00% |
| Supreme Leader | Political Power Gain: -10% Daily Support for Unaligned: +0.02 Stability: +10.00% War support: +10.00% |
| Glory of Cyrus the Great | Justify War goal time: -25% War Penalty Stability Modifier: +30.00% Division Defense on core territory: +10% Annex cost: -10% |
| Shahanshah | Non-core Manpower: +2.50% Party Popularity Stability Modifier: +2% Compliance Growth Speed: +10% |
| Hesitant King | Daily Autonomy progress gain: +0.20 Party Popularity Stability Modifier: -10% |
| Compliant King | Daily Autonomy progress gain: +0.30 Stability: +20.00% |
| Savior of Iran | War support: +5.00% Stability: +20.00% Division Attack on core territory: +10% Division Defense on core territory: +10% |
| Rightful King | Political Power Gain: +10% Stability: -2.00% |
| Nationalistic Freedom Fighter | Division Attrition: -4% Supply Consumption: -4% Land Night Attack: +5% |
| In Prison | Division Defense: -20% Division Attack: -20% |
| Netaji | Daily Support for Unaligned: +0.08 Party Popularity Stability Modifier: +15% Military factory construction speed: +10% |
| Hindu Nationalist | Resistance Target: -5% Annex cost: -25% Justify War goal time: -33% Division Attack on core territory: +15% |
| He who would become Death... | Division Attack: +12% Additional Overwhelming Fire Tactic Chance if it is Preferred tactic: +100.00% Division training time: -15% Generate War goal tension limit: -100% Join faction tension limit: -100% |
| Destroyer Of Worlds | Nuclear facility construction speed: +20% Nuclear Bomb Production Rate Military factory construction speed: +15% Civilian factory construction speed: -15% |
| Father of Pakistan | Surrender Limit: +10% Division Defense on core territory: +15% Division Attack on core territory: +10% Political Power Gain: +10% Stability: +12.00% |
| Government Exodus | Political Advisor Cost: +75% Trade Laws Cost: +75% Conscription Laws Cost: +75% Economy Laws Cost: +75% Army Chief Cost: +50% |
| Flexible Industrialist | Production efficiency retention: +15% Military to Civilian factory conversion cost: -20% Civilian to Military factory conversion cost: -20% |
| Frugal Pennypincher | Production efficiency growth: -7% Production Efficiency Base: -5.00% Production efficiency cap: +15% |
| The Government Connection | Daily Political Power Gain: +0.10 Party Popularity Stability Modifier: +10% Daily Support for Unaligned: +0.10 |
| Ruthless Tycoon | Resistance Target: +5% Trade extra resource per factory: +1 Resource Gain Efficiency: +10% Construction Speed: +5% |
| Shareholder Democracy | Daily Support for Unaligned: +0.05 Party Popularity Stability Modifier: +22% |
| Staunch Imperialist | Freedom gain by lend lease to overlord: -0.30 Daily Autonomy progress gain: -0.40 Civilian industry to overlord: +15.00% |
| Staunch Imperialist | Freedom gain by lend lease to overlord: -0.15 Daily Autonomy progress gain: -0.20 Civilian industry to overlord: +15.00% |
| Staunch Imperialist | Freedom gain by lend lease to overlord: -0.15 Daily Autonomy progress gain: -0.20 Civilian industry to overlord: +10.00% Stability: +10.00% |
| Seasoned Administrator | Resistance Activity Chance: -20% Damage to Garrisons: -35% Garrison Penetration Chance: -25% |
| Aloof Authority | Freedom gain by lend lease to overlord: -0.10 Daily Autonomy progress gain: -0.10 Civilian industry to overlord: +5.00% |
| Aloof Authority (Alt) | Freedom gain by lend lease to overlord: -0.10 Daily Autonomy progress gain: -0.10 Civilian industry to overlord: +5.00% Master Ideology Drift: +0.20 |
| Aloof Authority (Alt consult) | Freedom gain by lend lease to overlord: -0.10 Daily Autonomy progress gain: -0.10 Civilian industry to overlord: +5.00% Master Ideology Drift: +0.20 Stability: +10.00% |
| Belligerent Viceroy | Stability: -15.00% Factory output: +10% Recruitable population Factor: +10% |
| Spiritual Leader | Daily Political Power Gain: +0.10 Stability: +5.00% Daily Democracy Support: +0.05 Party Popularity Stability Modifier: +8% |
| Skeptical Towards Industrialization | War support: -5.00% Conscription Laws Cost: +33% |
| Socialist Modernizer | Research Speed: +7.00% Consumer Goods Factories factor: -10% |
| Top Down Heavy Policies | Stability: -5.00% War Penalty Stability Modifier: -5.00% |
| Minority Leader | Compliance Growth Speed: -8% |
| Authoritarian | Daily Fascism Support: +0.10 Daily Support for Unaligned: +0.05 Military factory construction speed: +10% Daily Compliance Gain: -0.01% |
| Under the Guise of Democracy | Resistance Target: -6% Daily Command power Gain Multiplier: +15% Daily Democracy Support: +0.01 Daily Communism Support: +0.02 Daily Support for Unaligned: +0.02 |
| Patron of Education | Research Speed: +8.00% |
| The Reformer Maharaja | Stability: +10.00% Resistance Growth Speed in our states occupied by the enemy: +10% |
| The Bengal Advocate | Political Power Gain: +8% War support: +5.00% Stability: +5.00% |
| Baluchistan's Sovereign | Division Defense on core territory: +10% Division Attack on core territory: +10% |
| Visionary Maharaja | Civilian factory construction speed: +6% Infrastructure construction speed: +12% |
| Guardian of the Hills | War support: +8.00% Terrain traits XP Gain: +15.00% |
| Financial Strategist | Civilian factory construction speed: +8% Stability: +5.00% |
| Scholar King | Research Speed: +8.00% |
| Heir to the Empire | Stability: +10.00% Division Defense on core territory: +10% Division Attack on core territory: +5% Political Power Gain: +5% |
| The Last Viceroy | Invasion Preparation Speed: +15% Dockyard output: +10% Planning Speed: +20% Max planning factor: -10.0% Coordination: -5% Fleet Coordination: -10% |
| Timur's Successor | Ideology drift defense: +25% Stability: +10.00% War support: +20.00% Justify War goal time: -50% |

### Finnish Personal Agenda traits (requires Arms Against Tyranny)

These drive Finland's Public Trust mechanic rather than giving flat modifiers.

| Trait | Effect |
|---|---|
| Personal Agenda (Svinhufvud) | Eradicate Socialism: Having less than 1% support for democratic and communism ideologies will increase Public Trust.Concerning Support for Socialists: Having more than 9% support for democratic or communism ideologies will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Kallio) | Eradicate Extremists: Having less than 1% support for fascism and communism ideologies will increase Public Trust.Concerning Support for Extremists: Having more than 9% support for fascism or communism ideologies will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Ryti) | Dream of Greater Finland: Occupying Finnish core states owned by an enemy will increase Public Trust.Concerning Support for Socialists: Having more than 9% support for democratic or communism ideologies will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Mannerheim) | Reliable Leader: Being at war will increase Public Trust.Appointed Regent: Being at peace will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Paasikivi) | Realist Conservative: Having more than 95% Stability will increase Public Trust.Caretaker: Having less than 60% Stability will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Annala) | Strong Nation: Having more than 300.000 Manpower in the field and less than 5% Surrender Progress while at war will increase Public Trust.Concerning Support for Socialists: Having more than 9% support for democratic or communism ideologies will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Tanner) | United Nation: Controlling Karjala and every owned state while having more than 95% support for democratic ideology will increase Public Trust.Concerning Support for Extremists: Having more than 9% support for fascism or communism ideologies will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Aaltonen) | Anti-Fascist Crusade: Having a contribution of more than 10% War Participation in all active wars and less than 5% Surrender Progress while being at war against a Fascist country will increase Public Trust.Divided Proletariat: Having less than 80% support for communism ideology will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Leino) | Obliteraded European Fascism: Having less than 1% support for fascism ideology while keeping Europe free of Fascist governments will increase Public Trust.Divided Proletariat: Having less than 80% support for communism ideology will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (Kuusinen) | A Solar System of Organizations: Having all Scandinavian and Baltic core states controlled by Finland or an ally will increase Public Trust.Forgotten Finno-Karelians: Not controlling the states of Karjala, Kola, Onega and Olonets will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
| Personal Agenda (von Hesse) | Dream of Greater Finland: Occupying Finnish core states owned by an enemy will increase Public Trust.Concerning Support for Socialists: Having more than 9% support for democratic or communism ideologies will decrease Public Trust.Finnish Sovereignty Threatened: Losing control over a Finnish core state will decrease Public Trust. |
