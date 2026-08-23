---
title: Estonian National Focus Tree
category: focus-trees
tags: [estonia, focus tree, fascism, democracy, communism, baltic, scandinavian expansion, vaps]
game_version: "1.19"
dlc: ["No Step Back"]
sources:
  - https://hoi4.paradoxwikis.com/Estonian_national_focus_tree
---

## Summary

Estonia's unique national focus tree (requires No Step Back DLC; base game uses generic tree) offers four main ideological branches: Democratic (The Era of Silence), Communist (Restore the Worker's Republic), Fascist (Rally the Nation), and an industrial path (Rejoin the Railways). The tree features heavy customization through the Vaps threat mechanic, Baltic alliances, and ambitious Scandinavian expansionist paths for the Fascist branch. Key mechanics include building industry, managing political opposition, and deciding whether to resist enemies militarily or capitulate and go into exile.

See [Estonia](../05-countries/estonia.md) for the country's 1936 starting profile.

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focus mechanics.

## The Era of Silence Branch

Democratic/Non-aligned historical branch focused on domestic consolidation and removing the Vaps threat under Konstantin Päts' dictatorship.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| **The Era of Silence** | None | Restore the Worker's Republic, Rally the Nation | +100 PP, +10.00% Stability; activates missions Vaps Marching on Tallinn and Crackdown on the Vaps | Starting point for authoritarian path; must manage Vaps threat |
| **Establish the Rahvuskogu** | The Era of Silence | — | +5.00% Democracy popularity; reduces Democratic Opposition national spirit levels; −5% PP gain, −10.00% Stability, −5.00% War support; +0.05/day Democracy support | Drafting new constitution to restore democratic traditions |
| **Isamaaliit** | The Era of Silence | — | Gain Isamaaliit national spirit (+15% PP gain); reduces Democratic Opposition; available political advisor Jaan Tõnisson (+0.10/day Democracy support) | Establishing ruling party for dictatorship |
| **Secure the Chamber of Deputies** | Establish the Rahvuskogu + Isamaaliit | — | +1 random building slot, +1 civilian factory in home area; reduces Democratic Opposition further | Consolidating control over civilian government |
| **Modernize Tallinn** | Secure the Chamber of Deputies | — | +2 random building slots, +2 civilian factories in home area | Industrial development of capital city |
| **Exploit the Banks** | Secure the Chamber of Deputies | — | Gain Exploited Banking Sector national spirit (−3.0% Consumer Goods Factories) | Leveraging Päts' banking connections |
| **Secure the National Council** | Establish the Rahvuskogu + Isamaaliit | — | Gain National Council of Estonia national spirit (+10.00% Production efficiency cap, +10.00% Factory output, +10 Army experience) | Centralizing local government representation |
| **Support Independent Militaries** | Secure the National Council | — | +2 random building slots, +2 military factories in home area; +10.00% War support | Arming independent military factions |
| **Break the Silence** | Modernize Tallinn + Exploit the Banks; requires <5% EKP, <5% Vapsid, >25% RKE support | Squash the Opposition | +20.00% Democracy popularity; RKE becomes ruling party; hold public elections every 4 years; remove all Democratic Opposition spirits | Democratic restoration path; mutually locks out authoritarian consolidation |
| **Squash the Opposition** | Modernize Tallinn + Exploit the Banks; requires <10% RKE support | Break the Silence | +10.00% Non-Aligned popularity; remove Very Low Democratic Opposition | Authoritarian consolidation path; keeps dictatorship intact |
| **Revisit the Economic Policy** | Modernize Tallinn + Exploit the Banks + Support Independent Militaries | — | Increase Economy Law level; +2 random building slots, +2 civilian factories in home area | Detaching economy from Soviet dependency |
| **Corporate Chambers** | Revisit the Economic Policy; requires not Civilian Economy or Early Mobilization | — | Gain Corporate Chambers national spirit (−20% Consumer Goods Factories, +20% Max Factories in a State) | Corporatist economic model bypassing leftist opposition |
| **Fight the Vaps** | The Era of Silence; requires one Vaps Tension spirit active (Low/Moderate/High/Impending) | — | +150 PP; unlocks Fight the Vaps decisions; +30 days to Vaps Marching on Tallinn mission | Suppressing right-wing paramilitaries; bypassed if all Vaps tension spirits removed |
| **Republican Defence League** | Fight the Vaps | — | Gain Republican Defence League national spirit (−10.0% Division training time) | United paramilitary organization |
| **Women's Defence League** | Republican Defence League | — | Allow women military pilots; modify Republican Defence League spirit (+5.00% Recruitable Population) | Naiskodukaitse integration; +10.0% Division training time total |
| **Cave to Enemy Pressure** | Republican Defence League; not in faction | Fortify Tallinn, Fortify the Border | If invaded, option to become subject rather than fight to the end | Peaceful capitulation path; bypassed if in faction |

## Formalize the Baltic Entente / Beyond the Baltic Sub-branch

Democratic Baltic alliance branch allowing coordination with Latvia and Lithuania, potential Scandinavian alliance, or unification efforts.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| **Formalize the Baltic Entente** | Break the Silence OR Squash the Opposition; must be fully independent, not in faction; Latvia/Lithuania must exist and not be in faction; they must not have completed this focus | Beyond the Baltic | Send diplomatic event to Latvia/Lithuania seeking cooperation; unlock decisions to Formalize the Baltic Entente and Abandon the Entente | Alliance formation requires careful diplomatic timing; bypassed if already in faction with Latvia/Lithuania |
| **The Baltic Economic Union** | Break the Silence + Formalize the Baltic Entente; must be faction leader | — | +1 offmap Civilian factory; Estonia and all Baltic states in faction gain Baltic Economic Pact spirit (−2.5% Consumer Goods Factories, +5.00% Factory output) | Creates shared economic benefits for all members |
| **Look North** | Formalize the Baltic Entente; must have agreed to Baltic Entente, be faction leader | — | Send diplomatic event to Norway/Sweden/Finland/Denmark seeking Baltic Entente expansion | Extending alliance northward to Scandinavian nations |
| **The Pan-Baltic Bank** | The Baltic Economic Union; must be faction leader | — | Estonia and all Baltic states modify Baltic Economic Pact spirit (−5.0% Consumer Goods Factories, +10.00% Factory output) | Establishing unified financial system; stronger economic bonuses |
| **Baltic Defense Army** | The Baltic Economic Union; must be faction leader | — | +1 offmap Military factory; Estonia and all Baltic states gain Baltic Defense Army spirit (+30% Recruitable Population Factor, −10.00% Training time) | Military coordination between Baltic states |
| **Propose a Baltic Union** | The Pan-Baltic Bank + Baltic Defense Army; must be faction leader | — | Estonia and all Baltic states lose Baltic Defense Army and Baltic Economic Pact spirits; gain The Baltic Union spirit (+30% Recruitable Population Factor, −7.5% Consumer Goods Factories, +15.00% Factory output, −15.00% Training time) | Political consolidation enabling later unification choices |
| **Baltic Unification** | Propose a Baltic Union; must be faction leader | United but Separate | Send unification event to other Baltic states in faction; they accept and are annexed by Estonia, or are at war and Estonia gains Annex war goal | Absorbing other Baltic states into Estonia; requires control of faction |
| **United but Separate** | Propose a Baltic Union; must be faction leader | Baltic Unification | Modify The Baltic Union spirit (+3.00% Recruitable Population, +30% Recruitable Population Factor, −10.0% Consumer Goods Factories, +20.00% Factory output, −20.00% Training time); create 4 Estonian units in random state; gain Topple government war goal against non-faction Baltic states | Maintaining separate states but unified militarily; looser alternative to direct annexation |
| **Beyond the Baltic** | Break the Silence OR Squash the Opposition; must be fully independent, not in faction; requires Democratic major ally at peace | Beyond the Baltic | Send diplomatic event to UK (or other Democratic major) seeking guarantees/alliance | Seeking Western democratic guarantees instead of Baltic focus; requires peace |
| **Join the Allies** | Beyond the Baltic; must be fully independent, not in faction | — | Send diplomatic event to UK (or highest-ranking Democratic major) to join Allied faction | Formalizing entry into Western alliance if UK agrees; provides security umbrella |

## Rally the Nation Branch

Fascist ideological path centered on the Vaps Movement, enabling civil war, Finnish flipping, and extensive Scandinavian expansion into a Nordic/Finno-Ugric empire.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| **Rally the Nation** | None (root focus) | Restore the Worker's Republic, The Era of Silence | +10.00% Fascism popularity; unlock decision Incoming Government Crackdown; unlock The March Through Estonia decisions | Starting point for Vapsid path; enables civil war |
| **The March on Tallinn** | Rally the Nation; requires >40% Vapsid support | — | Add 35 days to Vaps Marching on Tallinn mission; remove decision Incoming Government Crackdown; AI Estonia likely gets civil war (Fascism vs. Non-Aligned), or Vapsid takes power without war; if Vapsid wins, become Fascist, remove Democratic Opposition | Civil war or coup; bypassed if already Fascist |
| **The Glory of War** | The March on Tallinn; must be Fascist | — | Gain Veteran Training spirit (+10.0% Army experience gain, −10.0% Division training time) | Training new generation from Vaps veterans |
| **Mobilize the Veterans** | The Glory of War; must be Fascist | — | Modify Veteran Training spirit (+10.0% Army experience gain, −25.0% Division training time) | Allowing denied Vaps members to serve; improved training bonuses |
| **The Vapsid Youth** | The Glory of War; must be Fascist | — | Gain Vapsid Youth spirit (+2.00% Recruitable Population, +0.10/day Fascism support) | Youth recruitment and radicalization |
| **Empower Finnish Militants** | The March on Tallinn; must be Fascist | — | Finland (if exists and independent) gets 360-day Vapsid Youth spirit (+0.10/day Fascism support); if Finland already Fascist or subject/doesn't exist, bypassed | Destabilizing Finland toward Fascism via Estonian support |
| **The Veteran's Government** | The March on Tallinn; must be Fascist | — | +150 PP; available political advisors: Johan Pitka (−5.0% Consumer Goods Factories, +0.05/day Fascism support), Hjalmar Mäe (+25% PP gain, +0.05/day Fascism support, +85 Acceptance of Fascist Diplomacy), Viktor Puskar (−0.50% non-core Manpower, +10% Recruitable Population Factor, −0.05/day Communism support) | Building Fascist government structure; strong PP and diplomatic bonuses |
| **Anti-Communist Militia** | The Veteran's Government; must be Fascist | Reach Out to Germany | Create 4 units in random state | Grassroots anti-Soviet military formation; path to independence from Germany |
| **Reach Out to Germany** | The Veteran's Government; must be Fascist; must be at peace with Germany and fully independent, not in faction; Germany must be Fascist faction leader and not in war | Anti-Communist Militia | Send diplomatic event to Germany seeking friendship treaties | German alliance path; requires specific conditions |
| **Baltic Shield** | Anti-Communist Militia OR Reach Out to Germany; must be Fascist | — | Every owned state bordering Communist state adds 2 Land forts | Defensive fortification against Soviet threat |
| **Join the Axis** | Reach Out to Germany; must be Fascist and at peace with Germany, fully independent, not in faction; Germany must be Fascist leader and not in war | — | Send diplomatic event to Germany seeking Axis entry | Joining German faction; requires prior German friendship focus |
| **The Brotherhood** | Baltic Shield + (Anti-Communist Militia OR Join the Axis); must be Fascist; Latvia/Lithuania must exist | — | If Lithuania is Fascist, Estonia annexes it; otherwise Estonia gains Annex war goal; same for Latvia | Absorbing or conquering other Baltic states; replaces diplomatic Baltic Union |
| **National Pride Marches in Finland** | Empower Finnish Militants; must be Fascist | — | Unlock The March Through Finland decisions | Organizing grassroots Fascist movement in Finland; bypassed if Finland doesn't exist, is subject, or already Fascist |
| **Finno-Estonian Supremacy League** | National Pride Marches in Finland; must be Fascist and fully independent; Finland must exist, be Fascist, and either subject or independent, not in faction (unless has Lone Wolf) | Unite Our Nations | Create faction Finnic Supremacy League (if Estonia not in faction); invite Finland (if not locked by Lone Wolf) | Two-nation Fascist league; foundation for larger expansion |
| **Seize Swedish Assets** | Finno-Estonian Supremacy League; must be Fascist and fully independent; Sweden must not exist or be subject | — | Estonia gains Annex war goal against Sweden | Coercive acquisition or conquest of Sweden |
| **Secure the Straits** | Seize Swedish Assets; must be Fascist and fully independent; Denmark must not exist or be subject | — | Estonia gains Annex war goal against Denmark | Controlling North Sea passage; enabling Atlantic expansion |
| **Occupy Norway** | Seize Swedish Assets; must be Fascist and fully independent; Norway must not exist or be subject | — | Estonia gains Annex war goal against Norway | Completing Scandinavian consolidation |
| **Estonia is Scandinavia** | Secure the Straits + Occupy Norway; all Swedish, Norwegian, Danish core states controlled by Estonia, subjects, or Finland (if in faction); must be Fascist and fully independent | — | Rename to The Nordic League; unlock decision Proclaim Nordic Unity; if Norway/Sweden/Denmark are AI subjects, Estonia annexes them; if Finland is AI subject/faction member, Estonia annexes Finland | Victory condition for Scandinavian conquest path; rebranding achievement |
| **Unite Our Nations** | National Pride Marches in Finland; Finland must be Fascist and (subject or independent), not in faction; must be Fascist | Finno-Estonian Supremacy League | Send event to Finland proposing unification; if accepted, Estonia annexes Finland | Direct annexation path (alternative to league formation); simpler but only works with Fascist Finland |
| **Proclaim Finno-Ugria** | Unite Our Nations; must be Fascist and fully independent; must own state with Finland core | — | Rename to Estonia-Finland; every Finland core state becomes Estonia core | Consolidating Finnic identity after annexation; territorial integration |
| **Unite the Sámi** | Proclaim Finno-Ugria; must be Fascist and fully independent | — | Estonia gains Conquer war goals against Norway and Sweden | Integrating Sámi territories; requires controlling Lapland, Petsamo, Murmansk, Finnmark, Troms, Nordland, Helgeland, Trøndelag, Norrbotten, Västerbotten (or alternative: Sweden/Norway are subject); bypassed if all listed states controlled |
| **Unite Karelia** | Proclaim Finno-Ugria; must be Fascist and fully independent | — | Claim states Salla, Olonets, Onega, Karjala; Estonia gains Conquer war goals against all countries owning these states | Pushing into Soviet territory; expanding Finnic claim |
| **Unite the Finnic Identity** | Unite the Sámi + Unite Karelia; must be Fascist and fully independent; states Trøndelag, Nordland, Norrbotten, Gävleborg, Murmansk, Onega, Olonets controlled/cores with 60% compliance | — | Rename to Finno-Ugria; transfer listed Scandinavian/Russian states to Estonia if subjects (Trøndelag, Nordland, Norrbotten, Murmansk, Arkhangelsk, Kargopol, Kotlas, Onega, Olonets, Pechora, Tobolsk, Northern Urals, Salekhard, Sverdlovsk, Zlatoust, Syktyvkar, Perm, Kirov, Vologda, Luga, Västerbotten, Helgeland, Troms, Finnmark, Jämtland, Nenets, Yamalia, Surgut, Udmurtia, Mari El) | Creating massive Finno-Ugric empire spanning Scandinavia, Baltics, and Western Russia; final conquest focus for Fascist path |

## The Threat on Our Border Sub-branch

Defensive and border fortification branch enabling choice between resisting Germany or Soviet Union with specific military bonuses and fortification strategies.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| **The Threat on Our Border** | Fight the Vaps OR The March on Tallinn; not in faction with both Germany and Soviet Union | — | Trigger event The True Enemy | Choosing primary enemy; must not be aligned with both powers |
| **Fortify Tallinn** | The Threat on Our Border; owns Pärnu | Cave to Enemy Pressure, Fortify the Border | Pärnu state: +4 Land forts (2 in separate provinces); Harju state: +6 Land forts (2 per province) | Capital defense strategy; concentrated defense around Tallinn; bypassed if doesn't own Pärnu |
| **Fortify the Border** | The Threat on Our Border; not a subject | Cave to Enemy Pressure, Fortify Tallinn | Tartu state: +2 Land forts | Border defense strategy; holds line against enemies; bypassed if subject |
| **Hold Saaremaa** | Fortify Tallinn; owns Saaremaa | — | Saaremaa state: +7 Land forts (4 in one province, 3 in another); set Kuressaare victory points to 15, Tallinn to 5 | Island fortress; establishing last-stand position; bypassed if doesn't own Saaremaa |
| **No Surrender** | Fortify Tallinn OR Fortify the Border | — | If Germany chosen as true enemy: gain Anti-German Military spirit (+10.0% attack vs. Germany, +10.0% defense vs. Germany); if Soviet Union chosen: gain Anti-Soviet Military spirit (+10.0% attack vs. USSR, +10.0% defense vs. USSR) | Ideological/tactical bonuses against chosen enemy based on true enemy choice |
| **The Long Push** | No Surrender; enemy chosen at >10% surrender progress and Estonia at >90% surrender progress | — | Gain The Long Push East national spirit (−20.00% Towed Anti-Tank Production cost) | Post-capitulation resistance and counteroffensive; requires driving enemy deep into surrender |

## Prepare for the Inevitable Sub-branch

Exile and resistance branch enabling continued production and military operations after capitulation; unlocked only after capitulating.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| **Prepare for the Inevitable** | Corporate Chambers OR Finno-Estonian Supremacy League OR Unite Our Nations; must have capitulated | — | +2 offmap Military factories, +2 offmap Civilian factories | Setting up government-in-exile and resistance support infrastructure |
| **The Forest Brothers** | Prepare for the Inevitable | — | Gain Forest Brothers national spirit (+10.0% Division attack on core territory, +10.0% Division defense on core territory) | Anti-communist partisan network (reference to historical Baltic resistance) |
| **Prepare an Industrial Resistance** | Prepare for the Inevitable; must have capitulated | — | Gain Influx of Exiles national spirit (+700 weekly Manpower for exiled government); +4 offmap Military factories | Industrial capacity in exile supporting resistance |
| **Prepare a Covert Resistance** | Prepare for the Inevitable; must have capitulated | — | If La Résistance DLC enabled: gain 1 random Agency Upgrade; +3 offmap Civilian factories; otherwise: 2× 100% research bonus for Electronics | Clandestine intelligence operations; DLC-dependent benefits |

## Notes on Incomplete Content

The wiki page structure indicates two additional major branches not detailed in the fetched content:
- **Rejoin the Railways Branch** — shared Baltic industrial branch requiring investment from Fascist/Democratic major
- **Restore the Worker's Republic Branch** — Communist branch enabling Soviet puppet or independence, Baltic/Scandinavian expansion

These branches were referenced in branch descriptions but full focus tables were not included in the fetched page data. Consult the original wiki page for complete tables on these branches.

## DLC and Availability

This tree requires **No Step Back** DLC. Without it, Estonia uses the Generic national focus tree (see [National Focus and Continuous Focus](../01-mechanics/national-focus.md)). Additional DLC-gated features:
- **La Résistance** — Affects Prepare a Covert Resistance focus (Agency upgrades vs. research bonus)
