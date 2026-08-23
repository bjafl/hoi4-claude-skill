---
title: Lithuanian National Focus Tree
category: focus-trees
tags: [lithuanian, focus tree, fascist, monarchist, democratic, baltic, iron wolf, seimas]
game_version: "1.19"
dlc: [No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Lithuanian_national_focus_tree
---

## Summary

Lithuania's unique focus tree (requires No Step Back) centers on the Seimas government under Antanas Smetona in 1936, offering three main ideological paths: a Fascist branch led by Augustinas Voldemaras and the Iron Wolf partisans, a Monarchist branch crowning Mindaugas III, and a Democratic/Non-aligned branch. The tree includes expansionist claims on Polish, Baltic, and Soviet territories, internal political competition, and options to appease or resist regional powers.

See [Lithuania](../05-countries/lithuania.md) for the country's 1936 starting profile.

For the generic and continuous focus mechanics shared by all nations, see [National Focus and Continuous Focus](../01-mechanics/national-focus.md).

## Tree overview

The Lithuanian focus tree comprises three main branches plus five ideological/strategic sub-branches arising from the initial **Reconvene the Seimas** focus (the sole fascist entry point). The shared Baltic branches (**Rejoin the Railways** and **Restore the Worker's Republic**) are documented separately on the wiki; this document covers Lithuania's unique fascist, monarchist, and democratic paths.

## Reconvene the Seimas Branch (Fascist path)

This is the only entry point to the unique Lithuanian tree; all other paths branch from it.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Reconvene the Seimas** | None | Restore the Worker's Republic | Stability +5.00%; Political Power +100. Unlocks advisors Aleksandras Stulginskis (Fascism support −0.05/day, Unaligned support −0.05/day) and Jonas Staugaitis (Political Power +5%, Ideology drift defense +15.0%). Activates mission: Iron Wolf Partisans. Economy/Trade Laws cost −25%. |
| **Free Voldemaras** | Reconvene the Seimas; Iron Wolf Partisans active; >20% Geležinis Vilkas support | Exile Voldemaras | Unlocks Augustinas Voldemaras as advisor (Political Power +10%, Fascism support +0.10/day, Fascist diplomacy acceptance +40). Unlocks Iron Wolf threat-management decisions. Replaces Iron Wolf National Spirits progressively: Iron Wolf Volunteers → Iron Wolf Military (Recruitable Population +10%, Command Power gain +0.15/day, Conscription cost −20%), then escalates through threat levels. |
| **Exile Voldemaras** | Reconvene the Seimas; Fascist ruling party | Free Voldemaras | Augustinas Voldemaras retires. Reduces Iron Wolf threat levels; if escalated to Impending Uprising, replaces with Iron Wolf Military. Otherwise fascism support −10.00%. Removes Iron Wolf spirits if not already at Military level. |
| **Organize the Iron Wolf** | Free Voldemaras; Iron Wolf Partisans active | — | Advances Iron Wolf threat replacement chain as per Free Voldemaras. |
| **Lithuanian Activist Front** | Free Voldemaras OR Exile Voldemaras; Iron Wolf Partisans active | — | National spirit: Lithuanian Paramilitarists (Recruitable Population +1.00%). Pranas Saladžius becomes general. Manages Iron Wolf threat escalation. |
| **The Iron Wolf Youth** | Organize the Iron Wolf AND Lithuanian Activist Front | — | National spirit: Military Youth (Recruitable Population +2.00%). |
| **A New Kind of Iron Wolf** | Lithuanian Activist Front | — | 1× 100% research bonus for Mechanized. National spirit: The New Iron Wolf (Mechanized Attack +5.0%, Mechanized Defense +5.0%). Manages Iron Wolf threat escalation. |
| **Rapid Fortifications in the East** | The Iron Wolf Youth | — | If owns Wilno (784): 3 Land forts on all border provinces. Otherwise: 3 Land forts on border provinces in Kaunas (11). |
| **Defence From Above** | Rapid Fortifications in the East | — | Add 2 Anti-air in capital. |
| **Root Out the Iron Wolf** | Exile Voldemaras | — | Removes all Iron Wolf National Spirits. Fascism support −10.00%. Disables Iron Wolf Partisans mission. |
| **The Forest Brothers** | The Iron Wolf Youth OR Root Out the Iron Wolf | — | National spirit: Forest Brothers (Division Attack/Defense on core territory +10.0%). |
| **Unify the Military** | Organize the Iron Wolf; >40% Geležinis Vilkas support; Iron Wolf Partisans active | — | Geležinis Vilkas becomes ruling party. Fascism support +15.00%. Removes Underfunded Military and The Seimas spirits. Disables Iron Wolf Partisans mission. Grants Iron Wolf Military spirit if not present (Recruitable Population +10%, Command Power gain +0.15/day, Conscription cost −20%). |

## Seimas Branch: Polish and Soviet Expansion (Fascist core)

These focuses are available after **Unify the Military** and deal with Lithuania's territorial ambitions.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Seek Ties with Germany** | Unify the Military; at peace with Germany; fully independent; Germany is faction leader & fascist | Fortify Memel | Sends event to Germany (or most qualified fascist faction leader) requesting entry to Axis. Bypass: already in Axis with Germany as leader. |
| **Fortify Memel** | Unify the Military; controls Klaipeda (188); fully independent | Seek Ties with Germany | Klaipeda adds 3 Land forts. Germany gets Fortified Memeland opinion (Lithuania −25), making them less likely to allow faction entry. Bypass: already doesn't control Klaipeda. |
| **Proclaim Greater Lithuania** | Seek Ties with Germany OR Fortify Memel | — | Lithuania renamed to Greater Lithuania. Claims on 27 states across Belarus, Ukraine, Russia (Wilejka, Nowogródek, Polesie, Vitebsk, Minsk, Bobruysk, Gomel, Wołyn, Proskuriv, Zhytomyr, Vinnytsia, Kiev, Cherkasy, Poltava, Chernigov, Sumy, Kharkov, Dnipropetrovsk, Nikolayev, Odessa, Smolensk, Roslavl, Bryansk, Kaluga, Tula, Orel, Kursk, Belgorod, Mozyr, Balta-Tiraspol). |
| **Demand Vilnius** | Seek Ties with Germany OR Fortify Memel; Wilno (784) not owned by Lithuania or its faction/subject | — | If Wilno owner is not a subject: sends event demanding it. Otherwise: event to overlord. Bypass: Lithuania owns/controls Wilno or has it as subject. |
| **Lay Claim to Lower Lithuania** | Fortify Memel; not in faction with Germany | — | Königsberg (763) becomes core. Gain Conquer war goal against Königsberg owner. |
| **Claim Livonia** | Seek Ties with Germany OR Fortify Memel; Latvia or Estonia exist, fully independent, not in faction with Lithuania | — | If Latvia exists (indep., not subject, not faction): Gain Annex war goal. If Estonia exists (indep., not subject, not faction): Gain Annex war goal. States gain cores on Lithuania: Zemgale (809), Vidzeme (12), Rīga (808), Latgale (810), Kurzeme (190), Saaremaa (811), Harju (812), Virumaa (813), Pärnu (13), Tartu (191). |
| **Support Polish Fascists** | Demand Vilnius | Invade Poland; Request Polish Occupation | Poland exists, not capitulated, hasn't banned fascism, not in faction; Lithuania fully independent. Bypass: Poland doesn't exist or is Lithuania's subject. Sends event to Poland (or faction leader) to join Polish-Lithuanian Supremacy League. If Poland is fascist but Lithuania in faction: sends to faction leader. If Poland not fascist: Unlocks Support Polish Falangism decisions. |
| **Invade Poland** | Demand Vilnius | Support Polish Fascists; Request Polish Occupation | Poland exists, not capitulated, not in faction; Lithuania fully independent. Gain Annex war goal against Poland. Bypass: Poland's cores all owned by Lithuania. |
| **Request Polish Occupation** | Demand Vilnius | Support Polish Fascists; Invade Poland | Poland in faction; (Poland doesn't exist OR (Poland capitulated AND at war with Lithuania)); Lithuania owns a Polish core state. Gets event to faction allies controlling Polish cores. Bypass: all Polish cores controlled by Lithuania. |
| **Restore Order** | Support Polish Fascists OR Invade Poland OR Request Polish Occupation; Poland doesn't exist or capitulated or is Lithuania's subject; Poland is AI. | — | If Poland doesn't exist: Create Poland; Lithuania transfers owned Polish cores to it. Poland becomes collaboration government. Bolesław Piasecki becomes leader. National spirit: Unruly Falangist (War support +5.00%, Generate war goal tension −50.0%, Justify time −25.0%). Otherwise: Transfer Polish cores to Lithuania; Poland becomes collaboration government. Ermland-Masuren becomes Polish core. |
| **Restore Greater Lithuania** | Proclaim Greater Lithuania AND Restore Order; controls Smolensk (242), Roslavl (243), Bryansk (224), Kaluga (205), Tula (223), Orel (222), Kursk (220), Belgorod (240) with >80% compliance or cores; controls Wilejka (96), Nowogródek (95), Polesie (94) with same condition | — | Every state with greater_lithuania_flag not already a core becomes a core of Lithuania. |

## Lithuanian Preservationism Sub-branch (Non-aligned Military Dictatorship)

These focuses modify the Reconvene the Seimas branch and can establish a military dictatorship.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Lithuanian Preservationism** | Reconvene the Seimas; Non-aligned ruling party | — | Political Power +100. National spirit (360 days): Lithuanian Preservationism (Democracy/Communism/Fascism support −0.05/day, Unaligned support +0.05/day). Modifies The Seimas spirit: Stability +5.00%, Ideology drift defense +10.00%, Political Advisor cost −5%, Economy Laws cost −5%. |
| **A Martial Prime Minister** | Exile Voldemaras AND Lithuanian Preservationism | A King for Our People; A Priestly Prime Minister | Stasys Raštikis becomes political advisor (Army experience gain +10.0%, Max Command Power +20, Command Power gain +10%). War support +15.00%. |
| **A Priestly Prime Minister** | Exile Voldemaras AND Lithuanian Preservationism | A King for Our People; A Martial Prime Minister | Vladas Mironas becomes political advisor (Political Power gain +15%, Stability +10.00%). Political Power +100. |
| **The Nation and its Power** | A King for Our People OR A Martial Prime Minister OR A Priestly Prime Minister | — | National spirit: Presidential Powers (Political Power gain +0.05/day, War support +15.00%). |
| **State Media** | The Nation and its Power | — | National spirit: State Media (Stability penalty modifier +10.00%, War support +10.00%, Communism/Fascism support −0.02/day). |
| **Presidential Reform** | The Nation and its Power | — | Modifies Presidential Powers spirit to: Political Power gain +0.15/day, Party Popularity Stability modifier −15.00%, War support +15.00%. Modifies Underfunded Military to Competent Military (Army experience gain +0.10/day, Recruitable Population +20%, Army Leader cost −5.0%, Command Power gain multiplier +5%). Political Power +100. |
| **Exploit the International Bank** | State Media | — | National spirit: Exploited Banking Sector (Consumer Goods Factories −3.0%). |
| **A Corporatist Economy** | State Media AND Presidential Reform | — | National spirit: Corporate Chambers (Consumer Goods Factories −2.0%, Max Factories in a State +20%). |
| **The Nationalist Council** | A Martial Prime Minister OR A Priestly Prime Minister | — | Modifies The Seimas spirit to: Stability +10.00%, Ideology drift defense +20.00%, Political Advisor cost −10%, Economy Laws cost −10%. |
| **Expand the Military Budget** | Presidential Reform AND A Martial Prime Minister AND The Nationalist Council | — | Modifies Competent Military to Expanded Military (Army experience gain +0.10/day, Recruitable Population +30%, Army Leader cost −10.0%, Command Power gain multiplier +15%, Land Doctrine cost −10.00%, Conscription cost −10%). Army experience +40. |
| **Peasant Reform** | The Nationalist Council AND A Priestly Prime Minister | — | Every owned cored state (except Polish cores & Wilno): +2 Building slots, +1 Infrastructure. National spirit: Peasant Militia (Recruitable Population +2.50%). |
| **Martial Law** | A Corporatist Economy AND Expand the Military Budget | — | Modifies Expanded Military spirit. Escalates economy law: War Economy (Conscription cost −10%, Civilian↔Military conversion cost −20.00%, Military factory construction +20.00%) or to Total Mobilization (Recruitable Population −3.00%, War Economy consumer goods 10%, conversion cost −10.00%, military factory construction +10.00%). |
| **Merge the Military and Civilian Governments** | Expand the Military Budget | Restore Public Elections; The Indivisible Power of the State | Stasys Raštikis becomes Non-aligned leader. Lithuania renamed to Lithuanian Junta if not Baltic Federation. Non-aligned support +15.00%. |
| **Enforce Martial Rule** | Martial Law AND Merge the Military and Civilian Governments; Estonia or Latvia exist, fully independent, not in faction | Beyond the Baltic; Formalize the Baltic Entente | If Estonia exists (indep., not subject, not faction): Gain Puppet war goal. If Latvia exists (indep., not subject, not faction): Gain Puppet war goal. |

## A King for Our People Sub-branch (Monarchist)

Restores the monarchy under Karl Gero von Urach (Mindaugas III) and enables claims on Greater Lithuania, Poland, and the Baltic states.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **A King for Our People** | Exile Voldemaras AND Lithuanian Preservationism; Non-aligned ruling party | A Martial Prime Minister; A Priestly Prime Minister | Lithuania renamed to Kingdom of Lithuania. Gets event: King Mindaugas III. National spirit: Mindaugas III (Stability +10.00%, War support +5.00%). |
| **Establish Royal Guards** | A King for Our People; not capitulated | — | National spirit: The King's Guard (Special Forces Capacity multiplier +5.00%, Special Forces Division training −10.00%). Create 2 Lithuanian units in random owned states. |
| **A New Noble Class** | A King for Our People | — | Replaces The Seimas with The Ennobled Seimas (Political Power gain +15%, Stability +5.00%, Ideology drift defense +10.00%, Unaligned support +0.05/day). |
| **Abolish the Presidency** | Establish Royal Guards AND A New Noble Class | — | Non-aligned party renamed House von Urach; Mindaugas III loses old spirit. Mindaugas III becomes leader; gains King of Lithuania title. National spirit: The Soldier King (Stability +10.00%, War support +5.00%, Division Recovery Rate +10.0%). |
| **Claim Livonia** | Abolish the Presidency; not Polish-Lithuanian Commonwealth | — | If not Polish-Lithuanian Commonwealth: Lithuania renamed to Kingdom of Livonia. Cores on Estonian states (Pärnu, Tartu, Saaremaa, Harju, Virumaa) and Latvian states (Vidzeme, Kurzeme, Rīga, Zemgale, Latgale). If Estonia exists (indep., not subject): Gain Annex war goal. If Latvia exists (indep., not subject): Gain Annex war goal. |
| **Seize East Prussia** | Claim Livonia | — | Ermland-Masuren (5) and Königsberg (763) become cores. Bypass: both already cores. |
| **Claim Greater Lithuania** | Claim Livonia | — | Claims on 28 eastern states (Wilejka, Nowogródek, Polesie, Vitebsk, Minsk, Bobruysk, Gomel, Wołyn, Proskuriv, Zhytomyr, Vinnytsia, Kiev, Cherkasy, Poltava, Chernigov, Sumy, Kharkov, Dnipropetrovsk, Nikolayev, Odessa, Smolensk, Roslavl, Bryansk, Kaluga, Tula, Orel, Kursk, Belgorod, Mozyr, Balta-Tiraspol). Gain Conquer war goal against Soviet Union. |
| **Support Monarchism in Poland** | Abolish the Presidency | — | If Poland has completed Support Monarchism in Lithuania: Sets POL_banned_monarchy_flag for both; sends event "The Two Kings Dilemma" to Poland. Otherwise: Sends "Lithuania Claims Our Throne" to Poland. Unlocks "Our Claim to Poland" decisions. |
| **Arm Monarchist Militants** | Support Monarchism in Poland; Poland exists, indep., not subject | — | Unlocks decision: Arm Monarchist Militants. Bypass: Poland doesn't exist, is subject, or banned monarchy. |
| **The Kingdom of Poland** | Support Monarchism in Poland; Poland is subject of Lithuania OR banned monarchy OR has >80% monarchy support; Lithuania at peace & fully independent | — | Sends event to Poland (or monarchy supporters). Effects if accepted: Poland becomes Personal Union subject of Lithuania. Otherwise: Gain Puppet war goal. Bypass: all Polish cores controlled by Lithuania. |
| **Restore the Commonwealth** | The Kingdom of Poland; Poland is subject OR (all states either not Polish cores OR owned by Lithuania with >50% compliance); not already formed | — | If Poland AI: annexes Poland; generals with POL_monarchy_sympathies_flag become Lithuanian. Otherwise: sends annexation event to Poland. Lithuania renamed to Polish-Lithuanian Commonwealth. Gains cores on Lithuanian and Polish states, and Latvian states. Bypass: Commonwealth already exists elsewhere. |
| **The Greater Commonwealth** | Seize East Prussia AND Claim Greater Lithuania AND Restore the Commonwealth; controls Wilejka, Nowogródek, Polesie, Vitebsk, Minsk, Bobruysk, Gomel, Wołyn, Proskuriv, Zhytomyr, Vinnytsia, Kiev, Cherkasy, Poltava, Chernigov, Sumy, Kharkov, Dnipropetrovsk, Nikolayev, Odessa, Smolensk, Roslavl, Bryansk, Kaluga, Tula, Orel, Kursk, Belgorod, Mozyr, Crimea, Ermland-Masuren, Königsberg, Oberschlesien, Niederschlesien, Ostmark, Hinterpommern, Balta-Tiraspol | — | Every state that is core (Lithuania, Kashubia, Ukraine, or listed above) becomes Lithuanian core. |
| **Expand Lithuanian Shipyards** | Restore the Commonwealth; any owned controlled cored coastal state | — | Random owned controlled cored coastal state: +3 Building slots, +3 Naval dockyards. |
| **Polish-Lithuanian Railways** | Restore the Commonwealth; controls/subjects Aukštaitija (815), Wilno (784), Kaunas (11), Sūduva (814), Białystok (97) | — | Build level 1 railway from Wilno to Žemaitija; Białystok to Sūduva; Kaunas to Aukštaitija. |
| **Merge the Arms Industries** | Polish-Lithuanian Railways | — | Random owned controlled cored state: +2 Building slots, +2 Military factories. Another: +1 Building slot, +1 Military factory. |
| **Merge the Civilian Industries** | Merge the Arms Industries | — | Random owned controlled cored state: +2 Building slots, +2 Civilian factories. Another: +1 Building slot, +1 Civilian factory. |
| **Push Through Ruthenia** | Polish-Lithuanian Railways; controls/subjects Polesie (94), Wołyn (93), Zhytomyr (201), Kiev (202) | — | Build level 1 railway from Polesie to Kiev. |
| **Warsaw to Crimea Railway** | Push Through Ruthenia; controls/subjects Crimea (137); controls/subjects all Ukrainian states except Southern Bessarabia | — | Build level 1 railways from Kiev to Crimea and Odessa to Crimea. |

## Formalize the Baltic Entente / Beyond the Baltic Sub-branch (Democratic)

This sub-branch allows Lithuania to ally with other Baltic states or join the Allies.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Beyond the Baltic** | Merge the Military and Civilian Governments OR Restore Public Elections OR The Indivisible Power of the State; fully independent; not in faction; exists democratic faction leader (major, at peace) not in faction with UK; exists democratic power not in faction with Lithuania at peace | Enforce Martial Rule; Formalize the Baltic Entente | Sends event to UK (if faction leader, democratic, at peace, not warring with Lithuania) or most qualified democratic faction leader requesting guarantees. Bypass: already in faction with UK, or in faction with democratic faction leader. |
| **Join the Allies** | Beyond the Baltic; fully independent; democratic faction leader major at peace, not in faction with Lithuania | — | Sends event to UK (if faction leader, democratic, at peace, not warring) or most qualified democratic leader requesting faction entry. Bypass: already in faction with UK or democratic faction. |
| **Formalize the Baltic Entente** | Merge the Military and Civilian Governments OR Restore Public Elections OR The Indivisible Power of the State; fully independent; not in faction; Estonia or Latvia exist & not in faction or neither has completed Formalize the Baltic Entente | Enforce Martial Rule; Beyond the Baltic | Sends Baltic Cooperation event to Estonia (if indep., not faction) and Latvia (if indep., not faction). Latvia and Lithuania unlock decisions: Formalize the Baltic Entente and Abandon the Entente. Bypass: already in faction with Estonia or Latvia. |
| **Look North** | Formalize the Baltic Entente; agreed to join entente; faction leader; Finland/Norway/Sweden/Denmark at least one not in faction | — | Sends Baltic Cooperation event to Finland (if not in faction; checks for "The Lone Wolf" spirit blocking faction entry), Norway (if not faction), Sweden (if not faction), Denmark (if not faction). |
| **The Baltic Economic Union** | Formalize the Baltic Entente AND Restore Public Elections; Latvia; faction leader | — | Lithuania: +1 offmap Civilian factory. Lithuania and all Baltic countries in faction: National spirit: Baltic Economic Pact (Consumer Goods Factories −2.5%, Factory output +5.00%). |
| **The Pan-Baltic Bank** | The Baltic Economic Union; faction leader | — | Lithuania and Baltic countries modify Baltic Economic Pact to: Consumer Goods Factories −5.0%, Factory output +10.00%. |
| **Baltic Defense Army** | The Baltic Economic Union; faction leader | — | Lithuania: +1 offmap Military factory. Lithuania and Baltic countries: National spirit: Baltic Defense Army (Recruitable Population +30%, Training time −10.00%). |
| **Propose a Baltic Union** | The Pan-Baltic Bank AND Baltic Defense Army; faction leader | — | Lithuania and Baltic countries: Remove Baltic Defense Army and Baltic Economic Pact spirits. National spirit: The Baltic Union (Recruitable Population +30%, Consumer Goods Factories −7.5%, Factory output +15.00%, Training time −15.00%). |
| **Baltic Unification** | Propose a Baltic Union | United but Separate | Every Baltic country in faction with Latvia: sends unification event. If accept: annexed by Lithuania. If decline: Lithuania gains Annex war goal against them. Non-faction Baltic countries: Lithuania gains Topple government war goal. |
| **United but Separate** | Propose a Baltic Union | Baltic Unification | Lithuania and Baltic countries: modify The Baltic Union to: Recruitable Population +3.00%, +30%, Consumer Goods Factories −10.0%, Factory output +20.00%, Training time −20.00%. Create 4 Lithuanian units (9 Infantry each) in random states. Every Baltic non-faction country: Lithuania gains Topple government war goal. |

## Integrate the Opposition / Rastiki's Military Reforms Sub-branch (Flexible Path)

This sub-branch has no ideology prerequisite and allows democratic shifts, political advisors, and relations management with Poland, Germany, and the Soviet Union.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Integrate the Opposition** | Reconvene the Seimas | — | Political Power +100. Unlocks advisors: Kazys Grinius (Democracy support +0.10/day), Vytautas Petrulis (Consumer Goods Factories −5.0%, Unaligned support +0.05/day), Ernestas Galvanauskas (Fascism support −0.05/day, Fascist diplomacy acceptance −40). |
| **Patriotic Socialism** | Integrate the Opposition | — | National spirit: Patriotic Socialism (Factory output +10.00%, Democracy support +0.05/day). |
| **Peace with Poland** | Patriotic Socialism; Poland exists | Soviet Mutual Assistance | Sends event to Poland requesting peace. Bypass: Poland doesn't exist or is Lithuania's subject, or mutual guarantees exist. |
| **Strength in Unity** | Peace with Poland; Poland exists, owns & controls Wilno (784); not completed Soviet Mutual Assistance | — | Sends event to Poland requesting permanent peace. Bypass: Poland doesn't exist, Lithuania guaranteed by Poland & vice versa & owns Wilno. |
| **Rastiki's Military Reforms** | Reconvene the Seimas | — | Jonas Černius becomes Field Marshal. Antanas Gustaitis and Kazys Skučas become generals. Army experience +40. |
| **Patriotic Education** | Rastiki's Military Reforms | — | National spirit: Patriotic Education (Recruitable Population +10%, Stability +10.00%, Land Doctrine cost −10.00%, 1× 50% Land Doctrine cost reduction). |
| **Soviet Mutual Assistance** | Patriotic Education; Soviet Union exists, indep., no civil war, not in faction with Poland, at peace with Germany, fully independent | Peace with Poland | Sends to Lithuania: conditional on German focus completions and Soviet-Polish relationship. If Germany completed Oppose Hitler & Rally the Wehrmacht & USSR communist & not warring Poland: USSR will cede Wilno to Lithuania when Molotov-Ribbentrop fulfilled. Otherwise if same conditions but not at war with Poland: USSR gets event for partition. Otherwise: Lithuania gains Conquer war goal against Poland. |
| **Victory in Trust** | Soviet Mutual Assistance | — | National spirit: Victory in Trust (Army experience gain +0.10/day, War support +10.00%, Command Power gain +0.10/day). |
| **Purge Popular Resistance** | Rastiki's Military Reforms; not democratic ruling party | — | If Non-aligned: +15.00% Non-aligned support. National spirit (180 days): Purged Popular Resistance (Democracy/Communism support −0.10/day, Fascism/Unaligned support +0.10/day). If Fascist: +20.00% Fascism support; same spirit. If Communist: +20.00% Communism support; reversed penalties (Democracy/Fascism −0.10/day, Communism +0.10/day). |
| **Anti-Communist Militia** | Purge Popular Resistance | — | Communism support −5.00%. Create 2 Lithuanian units in random owned states. If Soviet Union is communist: USSR gets Anti-Soviet opinion (Lithuania −20). |
| **Arrest the Nazis in Memel** | Purge Popular Resistance; owns Klaipeda (188) | — | Fascism support −5.00%; Stability +5.00%. Klaipeda adds 3 Land forts. If Germany is fascist or imprisoned fascist leadership: Germany gets Arrested party members opinion (Lithuania −20). Bypass: doesn't own Klaipeda. |
| **A Reminder of the True Enemy** | Anti-Communist Militia OR Arrest the Nazis in Memel | — | Sends event to Lithuania: The True Enemy (choose which power is primary threat). |
| **Restore Public Elections** | Peasant Reform AND A Reminder of the True Enemy; Strength in Unity OR Victory in Trust; >30% LKDP support; not in democracy; mutually exclusive with military dictatorship focus | Merge the Military and Civilian Governments; The Indivisible Power of the State | LKDP becomes ruling party. Public elections held. Bypass: already democratic. |
| **The Indivisible Power of the State** | A Reminder of the True Enemy; Strength in Unity OR Victory in Trust; Non-aligned or Fascist ruling party | Merge the Military and Civilian Governments; Restore Public Elections | Country leader gains Dictator title. Political Power gain +25%. |

## Prepare for the Inevitable / Appease the Russians / Appease the Germans Sub-branch (Endgame)

This sub-branch becomes available after A Reminder of the True Enemy and offers paths to resist occupation, prepare exile government, or appease a specific power.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Prepare for the Inevitable** | Restore Public Elections OR The Indivisible Power of the State; capitulated | Appease the Russians; Appease the Germans | +2 offmap Military factories, +2 offmap Civilian factories. |
| **Prepare a Covert Resistance** | Prepare for the Inevitable; capitulated | — | If La Résistance enabled: gain one random Agency Upgrade, +3 offmap Civilian factories. Otherwise: 2× 100% Electronics research bonus. |
| **Prepare an Industrial Resistance** | Prepare for the Inevitable; capitulated | — | Latvia: National spirit: Influx of Exiles (Weekly Exiled Government Manpower +700). +4 offmap Military factories. |
| **Appease the Russians** | Restore Public Elections OR The Indivisible Power of the State; not named Germany as true enemy | Prepare for the Inevitable; Appease the Germans | Current Soviet party support +20.00%; Gains Appeasement opinion (USSR +25). USSR gains Appeasement opinion (Lithuania +25). |
| **Appease the Germans** | Restore Public Elections OR The Indivisible Power of the State; not named Germany as true enemy | Prepare for the Inevitable; Appease the Russians | Current German party support +20.00%; Gains Appeasement opinion (Germany +25). Germany gains Appeasement opinion (Lithuania +25). |
| **Offer Basing Rights** | Appease the Russians OR Appease the Germans | — | Depending on appeased power: Current Soviet party support +15.00%; USSR gets event "Lithuania Offers Basing Rights!" OR Current German party support +15.00%; Germany gets event "Lithuania Offers Basing Rights!" |
| **Occupation** | Offer Basing Rights; not in faction | — | In event appeased nation invades: offered option to become subject rather than fight. |

## Democratic path: Restore Public Elections

Once **Restore Public Elections** is completed, Lithuania becomes democratic (LKDP ruling party). Democratic progression allows the Allies path, Baltic Entente, and economic union with the other Baltic states. The democratic path emphasizes diplomatic alliances over territorial expansion and offers the option to form a Baltic Union (either through unification or maintaining separate independence while deepening military/economic integration).
